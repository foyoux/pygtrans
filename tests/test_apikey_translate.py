"""测试 ApiKeyTranslate"""

from pygtrans import ApiKeyTranslate, TranslateResponse, LanguageResponse, DetectResponse, split_list_by_content_size
from pygtrans import __apikey__

api_key = __apikey__


# proxies = {
#     'http': 'http://localhost:10809',
#     'https': 'http://localhost:10809'
# }


def test_translate():
    """测试构造函数"""
    # client = ApiKeyTranslate(api_key=api_key, target='en', source='zh-CN', proxies=proxies)
    client = ApiKeyTranslate(api_key=api_key, target='en', source='zh-CN')
    t = client.translate('喜欢你, 怎么办')
    assert isinstance(t, TranslateResponse)
    assert t.translatedText.find('you') != -1


"""默认构造"""
# client = ApiKeyTranslate(api_key=api_key, proxies=proxies)
client = ApiKeyTranslate(api_key=api_key)


def test_supported_languages():
    """支持语言列表"""
    """默认 self.target"""
    lang1 = client.languages()
    assert isinstance(lang1, list)
    for i in lang1:
        assert isinstance(i, LanguageResponse)
        if i.language == 'zh-CN':
            assert i.name == '中文(简体)'
    """自定义 target='en'"""
    lang2 = client.languages(target='en')
    assert isinstance(lang2, list)
    for i in lang2:
        assert isinstance(i, LanguageResponse)
        if i.language == 'zh-CN':
            assert i.name == 'Chinese (Simplified)'


def test_detect_language():
    """检测语言"""
    d1 = client.detect('Hello')
    assert isinstance(d1, DetectResponse)
    assert d1.language == 'en'
    """批量检测"""
    d2 = client.detect(['Hello', 'Love'])
    assert isinstance(d2, list)
    for i in d2:
        assert isinstance(i, DetectResponse)
        assert i.language == 'en'


def test_translate_text():
    """单个翻译"""
    t1 = client.translate('你好', target='en')
    assert t1.detectedSourceLanguage == 'zh-CN'
    """批量翻译"""
    t2 = client.translate(['我喜欢你, 怎么办', '早起早睡'], target='en')
    assert isinstance(t2, list)
    # for i in t2:
    #     print(i.translatedText)


def test_detect_128():
    d1 = client.detect(['A'] * 150)
    assert isinstance(d1, list)
    assert len(d1) == 150


def test_translate_128():
    d1 = client.translate(['A'] * 150)
    assert isinstance(d1, list)
    assert len(d1) == 150


def test_split_list_by_content_size():
    assert split_list_by_content_size(['11', '22', '33'], 4) == [['11', '22'], ['33']]
    assert split_list_by_content_size(['11', '22', '33'], 3) == [['11'], ['22'], ['33']]


def test_dt_102400():
    t1 = client.translate(['love you ' * 100] * 1024)
    assert isinstance(t1, list)
    assert len(t1) == 1024
    t2 = client.detect(['love you ' * 100] * 1024)
    assert isinstance(t2, list)
    assert len(t2) == 1024
