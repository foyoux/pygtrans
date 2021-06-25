"""测试Translate"""

from pygtrans import *

cn = Translate()


# def test_langusges():
#     """支持语言列表"""
#     """默认 self.target"""
#     lang1 = cn.languages()
#     assert isinstance(lang1, list)
#     for i in lang1:
#         assert isinstance(i, LanguageResponse)
#         if i.language == 'zh-CN':
#             assert i.name.find('中文') != -1
#     """自定义 target='en'"""
#     lang2 = cn.languages(target='en')
#     assert isinstance(lang2, list)
#     for i in lang2:
#         assert isinstance(i, LanguageResponse)
#         if i.language == 'zh-CN':
#             assert i.name.find('Chinese') != -1


def test_detect_language():
    """检测语言"""
    d1 = cn.detect('Hello')
    assert isinstance(d1, DetectResponse)
    assert d1.language == 'en'
    """批量检测"""
    d2 = cn.detect('你好')
    assert isinstance(d2, DetectResponse)
    assert d2.language != 'en'


def test_translate_text():
    """单个翻译"""
    t1 = cn.translate('你好', target='en')
    # assert t1.detectedSourceLanguage == 'zh-CN'
    """批量翻译"""
    t2 = cn.translate_and_detect(['程序员', '早起早睡'], target='en')
    assert isinstance(t2, list)
    # for i in t2:
    #     print(i)
