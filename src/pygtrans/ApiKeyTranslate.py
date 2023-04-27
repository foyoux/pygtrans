"""通过 ``Google Cloud Translate APIKEY`` 进行翻译
如果你没有 ``APIKEY``, 请使用 :class:`pygtrans.Translate.Translate`

基本功能:
    #. 获取语言列表
    #. 语言检测, 支持批量检测
    #. 文本翻译, 支持批量, 支持 html 模式翻译
"""
import math
import time
from typing import List, Union, Dict, overload

import requests

from .DetectResponse import DetectResponse
from .LanguageResponse import LanguageResponse
from .Null import Null
from .TranslateResponse import TranslateResponse


def split_list(obj_list: List, sub_size: int = 128) -> List[list]:
    """split list

    :param obj_list: list object
    :param sub_size: sub list size
    :return: List[list]
    """
    if not isinstance(obj_list, list):
        return [[obj_list]]
    if sub_size < 1:
        sub_size = 1
    return [obj_list[i:i + sub_size] for i in range(0, len(obj_list), sub_size)]


def split_list_by_content_size(obj_list: List[str], content_size: int = 102400) -> List[List[str]]:
    """..."""
    if content_size < 1:
        content_size = 1
    if len(obj_list) == 1 or len(''.join(obj_list)) <= content_size:
        return [obj_list]

    mid = math.ceil(len(obj_list) / 2)
    ll = []
    ll.extend(split_list_by_content_size(obj_list[:mid], content_size=content_size))
    ll.extend(split_list_by_content_size(obj_list[mid:], content_size=content_size))
    return ll


class ApiKeyTranslate:
    """
    :param api_key: str: 谷歌云翻译APIKEY, `查看详情 <https://cloud.google.com/docs/authentication/api-keys>`_
    :param target: str: (可选) 目标语言, 默认: ``zh-CN``, :doc:`参考列表 <target>`
    :param source: str: (可选) 源语言, 默认: ``auto`` (自动检测), :doc:`参考列表 <source>`
    :param fmt: str: (可选) 文本格式, ``text`` | ``html``, 默认: ``html``
    :param model: str: (可选) 翻译模型. 可以是 base 使用 Phrase-Based Machine Translation (PBMT) 模型，
        或者 nmt 使用 Neural Machine Translation (NMT) 模型。如果省略，则使用 nmt。如果模型是 nmt，
        并且 NMT 模型不支持请求的语言翻译对，则使用 PBMT 模型翻译请求。
    :param proxies: (可选) eg: `proxies = {'http': 'http://localhost:10809','https': 'http://localhost:10809'}`

    基本用法:
        >>> from pygtrans import ApiKeyTranslate
        >>> client = ApiKeyTranslate(api_key='<api_key>')
        >>> langs = client.languages()  # 此种方式的语言列表, 请使用此方法获取
        >>> langs[0]
        LanguageResponse(language='sq', name='阿尔巴尼亚语')
        >>> text = client.translate('Google Translate')
        >>> text.translatedText
        '谷歌翻译'
        >>> text.detectedSourceLanguage
        'en'
        >>> texts = client.translate(['안녕하십니까', 'こんにちは'])
        >>> texts[0].translatedText
        '你好'
        >>> texts[0].detectedSourceLanguage
        'ko'
        >>> texts[1].translatedText
        '你好'
        >>> texts[1].detectedSourceLanguage
        'ja'
    """
    _BASE_URL: str = 'https://translation.googleapis.com/language/translate/v2'
    _LANGUAGE_URL: str = f'{_BASE_URL}/languages'
    _DETECT_URL: str = f'{_BASE_URL}/detect'
    _LIMIT_SIZE = 102400

    def __init__(
            self, api_key: str,
            target: str = 'zh-CN',
            source: str = None,
            fmt: str = 'html',
            model: str = 'nmt',
            proxies: Dict = None
    ):
        self.api_key = api_key
        self.target = target
        if source == 'auto':
            # '不提供' 替换 'auto'，'auto' 会导致 400，参数错误。
            source = None
        self.source = source
        self.fmt = fmt
        self.model = model
        self.session = requests.Session()

        if proxies is not None:
            self.session.trust_env = False
            self.session.proxies = proxies

    def languages(self, target: str = None, model: str = None) -> Union[List[LanguageResponse], Null]:
        """语言支持列表"""
        if target is None:
            target = self.target
        if model is None:
            model = self.model
        response = self.session.get(self._LANGUAGE_URL, params={'key': self.api_key, 'target': target, 'model': model})
        if response.status_code == 200:
            return [LanguageResponse(**i) for i in response.json()['data']['languages']]
        return Null(response)

    @overload
    def detect(self, q: str) -> DetectResponse:
        """..."""

    @overload
    def detect(self, q: List[str]) -> List[DetectResponse]:
        """..."""

    def detect(self, q: Union[str, List[str]]) -> Union[DetectResponse, List[DetectResponse], Null]:
        """语言检测, 支持批量

        :param q: 字符串或字符串列表
        :return: 成功则返回: :class:`pygtrans.TranslateResponse.DetectResponse` 对象,
            或 :class:`pygtrans.TranslateResponse.DetectResponse` 对象列表, 这取决于 `参数: q` 是字符串还是字符串列表.
            失败则返回 :class:`pygtrans.Null.Null` 对象

        基本用法:
            >>> from pygtrans import ApiKeyTranslate
            >>> client = ApiKeyTranslate(api_key='<api_key>')
            >>> d1 = client.detect('Hello')
            >>> d1.language
            'en'
            >>> assert isinstance(client.detect(['Hello', 'Google']), list)

        """
        ll = []
        for ql in split_list(q):
            for qli in split_list_by_content_size(ql):
                for i in range(1, 4):
                    response = self.session.post(self._DETECT_URL, params={
                        'key': self.api_key
                    }, data={
                        'q': qli
                    })
                    if response.status_code == 429:
                        time.sleep(5 * i)
                        continue
                    break
                # noinspection PyUnboundLocalVariable
                if response.status_code != 200:
                    return Null(response)
                ll.extend([DetectResponse(**i[0]) for i in response.json()['data']['detections']])
        if isinstance(q, str):
            return ll[0]
        return ll

    @overload
    def translate(
            self, q: str, target: str = None, source: str = None, fmt: str = None, model: str = None
    ) -> TranslateResponse:
        """..."""

    @overload
    def translate(
            self, q: List[str], target: str = None, source: str = None, fmt: str = None, model: str = None
    ) -> List[TranslateResponse]:
        """..."""

    def translate(
            self, q: Union[str, List[str]], target: str = None, source: str = None, fmt: str = None,
            model: str = None
    ) -> Union[TranslateResponse, List[TranslateResponse], Null]:
        """文本翻译, 支持批量

        :param q: str: 字符串或字符串列表
        :param target: str: (可选)  目标语言, 默认: ``self.target``, :doc:`查看支持列表 <target>`
        :param source: str: (可选)  源语言, 默认: ``self.source``, :doc:`查看支持列表 <source>`
        :param fmt: str: (可选) 文本格式, ``text`` | ``html``, 默认: ``self.format``
        :param model: str: (可选) 翻译模型, ``nmt`` | ``pbmt``, 默认: ``self.model``
        :return: 成功则返回: :class:`pygtrans.TranslateResponse.TranslateResponse` 对象,
            或 :class:`pygtrans.TranslateResponse.TranslateResponse` 对象列表, 这取决于 `参数: q` 是字符串还是字符串列表.
            失败则返回 :class:`pygtrans.Null.Null` 对象

        .. 谷歌API调用限制
            最大并发量: 128
            最大请求体大小: 102400 bytes

        基本用法:
            >>> from pygtrans import ApiKeyTranslate
            >>> client = ApiKeyTranslate(api_key='<api_key>')
            >>> text = client.translate('Google Translate')
            >>> text.translatedText
            '谷歌翻译'
            >>> text.detectedSourceLanguage
            'en'
            >>> texts = client.translate(['안녕하십니까', 'こんにちは'])
            >>> texts[0].translatedText, texts[1].translatedText
            ('你好', '你好')
        """

        if target is None:
            target = self.target
        if source == 'auto':
            source = None
        if source is None:
            source = self.source
        if fmt is None:
            fmt = self.fmt
        if model is None:
            model = self.model

        ll = []
        for ql in split_list(q):
            for qli in split_list_by_content_size(ql):
                for i in range(1, 4):
                    response = self.session.post(self._BASE_URL, params={
                        'key': self.api_key, 'target': target, 'source': source, 'format': fmt, 'model': model
                    }, data={'q': qli})
                    if response.status_code == 429:
                        time.sleep(5 * i)
                        continue
                    break
                # noinspection PyUnboundLocalVariable
                if response.status_code != 200:
                    return Null(response)

                ll.extend([TranslateResponse(**i) for i in response.json()['data']['translations']])

        if isinstance(q, str):
            return ll[0]
        return ll
