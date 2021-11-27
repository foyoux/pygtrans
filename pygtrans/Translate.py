"""通过调用 ``google.com`` | ``google.cn`` | ``...`` web接口进行翻译
如果你有 **google cloud translate apikey**, 请使用 :class:`pygtrans.ApiKeyTranslate`

基本功能:
    #. 语言检测, 支持批量检测
    #. 文本翻译, 支持批量, 支持 html 模式翻译
"""
import base64
import random
import time
from typing import List, Union, overload, Dict

import requests

from .DetectResponse import DetectResponse
from .Null import Null
from .TranslateResponse import TranslateResponse


class Translate:
    """
    :param target: str: (可选) 目标语言, 默认: ``zh-CN``, :doc:`查看完整列表 <target>`
    :param source: str: (可选) 源语言, 默认: ``auto`` (自动检测), :doc:`查看完整列表 <source>`
    :param fmt: str: (可选) 文本格式, ``text`` | ``html``, 默认: ``html``
    :param user_agent: str: (可选) 用户代理, 这个参数很重要, 不设置或错误设置非常容易触发 **429 Too Many Requests** 错误,
        默认: ``GoogleTranslate/6.18.0.06.376053713 (Linux; U; Android 11; GM1900)``, 所以用户可以不用提供.
        这个默认 ``User-Agent`` 很稳定, 暂时未发现 ``429 错误``, 如果出现 ``429``, 建议 **模仿默认 进行构造**,
        或者进行 `反馈 <https://github.com/foyoux/pygtrans/issues/new>`_
    :param domain: str: (可选) 域名 ``google.com`` 及其可用平行域名 (如: ``google.cn``), 默认: ``google.cn``
    :param proxies: (可选) eg: proxies = {'http': 'http://localhost:10809', 'https': 'http://localhost:10809'}

    基本用法:
        >>> from pygtrans import Translate
        >>> client = Translate()
        >>> client.detect('谷歌翻译').language
        'zh-CN'
        >>> text = client.translate('Hello, Google')
        >>> text.translatedText
        '你好，谷歌'
        >>> texts = client.translate(['批量测试', '批量翻译'], target='en')
        >>> for text in texts:
        ...     print(text.translatedText)
        Batch test
        Batch translation
    """

    def __init__(
            self,
            target: str = 'zh-CN',
            source: str = 'auto',
            fmt='html',
            user_agent: str = None,
            domain: str = 'com',
            proxies: Dict = None
    ):
        self.target = target
        self.source = source
        self.fmt = fmt

        if user_agent is None:
            user_agent = f'GoogleTranslate/6.{random.randint(10, 100)}.0.06.{random.randint(111111111, 999999999)} (Linux; U; Android {random.randint(5, 11)}; {base64.b64encode(str(random.random())[2:].encode()).decode()})'

        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': user_agent
        }
        self.BASE_URL: str = 'https://translate.google.' + domain
        self.LANGUAGE_URL: str = f'{self.BASE_URL}/translate_a/l'
        self.DETECT_URL: str = f'{self.BASE_URL}/translate_a/single'
        self.TRANSLATE_URL: str = f'{self.BASE_URL}/translate_a/t'
        self.TTS_URL: str = f'{self.BASE_URL}/translate_tts'

        if proxies is not None:
            self.session.proxies = proxies

    def detect(self, q: str) -> Union[DetectResponse, Null]:
        """语言检测

        :param q: 需要检测的内容, 不支持批量, 如需批量, 请参阅: :func:`translate_and_detect`.
        :return: 成功则返回 :class:`pygtrans.DetectResponse.DetectResponse` 对象,
            失败则返回 :class:`pygtrans.Null.Null` 对象

        基本用法:
            >>> from pygtrans import Translate
            >>> client = Translate()
            >>> d = client.detect('こんにちは')
            >>> assert d.language == 'ja'
        """
        for _ in range(3):
            response = self.session.post(
                self.DETECT_URL,
                params={'dj': 1, 'sl': 'auto', 'ie': 'UTF-8', 'oe': 'UTF-8', 'client': 'at'},
                data={'q': q}
            )
            if response.status_code == 429:
                time.sleep(5)
                continue
            break
        if response.status_code != 200:
            return Null(response)
        rt = response.json()
        return DetectResponse(language=rt['src'], confidence=rt['confidence'])

    @overload
    def translate(self, q: str, target: str = None, source: str = None, fmt: str = None, ) -> TranslateResponse:
        """..."""

    @overload
    def translate(
            self, q: List[str], target: str = None, source: str = None, fmt: str = None
    ) -> List[TranslateResponse]:
        """..."""

    def translate(
            self, q: Union[str, List[str]], target: str = None, source: str = None, fmt: str = None
    ) -> Union[TranslateResponse, List[TranslateResponse], Null]:
        """翻译文本, 支持批量, 支持 html

        :param q: str: 字符串或字符串列表
        :param target: str: (可选)  目标语言, 默认: ``self.target``, :doc:`查看支持列表 <target>`
        :param source: str: (可选)  源语言, 默认: ``self.source``, :doc:`查看支持列表 <source>`
        :param fmt: str: (可选) 文本格式, ``text`` | ``html``, 默认: ``self.format``
        :return: 成功则返回: :class:`pygtrans.TranslateResponse.TranslateResponse` 对象,
            或 :class:`pygtrans.TranslateResponse.TranslateResponse` 对象列表, 这取决于 `参数: q` 是字符串还是字符串列表.
            失败则返回 :class:`pygtrans.Null.Null` 对象

        基本用法:
            >>> from pygtrans import Translate
            >>> client = Translate()
            >>> text = client.translate('Hello, Google')
            >>> text.translatedText
            '你好，谷歌'
            >>> texts = client.translate(['批量测试', '批量翻译'], target='en')
            >>> for text in texts:
            ...     print(text.translatedText)
            Batch test
            Batch translation
        """

        if not q:
            return []

        if isinstance(q, str):
            if q == '':
                return TranslateResponse('')

        for _ in range(3):
            response = self.__translate(q=q, target=target, source=source, fmt=fmt, v='1.0')
            if response.status_code == 429:
                time.sleep(5)
                continue
            break
        if response.status_code == 200:
            ll = [TranslateResponse(translatedText=i) for i in response.json()]
            if isinstance(q, str):
                return ll[0]
            return ll

        return Null(response)

    def __translate(
            self, q: Union[str, List[str]], target: str = None, source: str = None, fmt: str = None, v: str = None
    ):
        if target is None:
            target = self.target
        if source is None:
            source = self.source
        if fmt is None:
            fmt = self.fmt
        for _ in range(3):
            response = self.session.post(
                self.TRANSLATE_URL,
                params={'tl': target, 'sl': source, 'ie': 'UTF-8', 'oe': 'UTF-8', 'client': 'at', 'dj': '1',
                        'format': fmt, 'v': v},
                data={'q': q}
            )
            if response.status_code == 429:
                time.sleep(5)
                continue
            break
        return response

    def tts(self, q: str, target: str = None) -> Union[bytes, Null]:
        """语音: 实验性功能

        :param q: 只支持短语字符串
        :param target: 目标语言
        :return: 返回二进制数据, 需要自行写入文件, MP3
        """
        if target is None:
            target = self.target

        for _ in range(3):
            response = self.session.get(
                self.TTS_URL,
                params={
                    'ie': 'UTF-8',
                    'client': 'at',
                    'tl': target,
                    'q': q
                })
            if response.status_code == 429:
                time.sleep(5)
                continue
            break

        if response.status_code == 200:
            return response.content
        return Null(response)
