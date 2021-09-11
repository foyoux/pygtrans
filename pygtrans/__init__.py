"""谷歌翻译"""

from .ApiKeyTranslate import ApiKeyTranslate, split_list_by_content_size
from .DetectResponse import DetectResponse
from .LanguageResponse import LanguageResponse
from .Null import Null
from .Translate import Translate
from .TranslateResponse import TranslateResponse

__apikey__ = '<your-api-key>'

__title__ = 'pygtrans'
__description__ = 'Google Translate, support APIKEY'
__url__ = 'https://github.com/foyoux/pygtrans'
__version__ = '1.1.1'
__author__ = 'foyou'
__author_email__ = 'yimi.0822@qq.com'
__license__ = 'GPL-3.0'
__copyright__ = f'Copyright 2021 {__author__}'
__ide__ = 'PyCharm - https://www.jetbrains.com/pycharm/'

__all__ = [
    'Translate', 'ApiKeyTranslate', 'Null', 'LanguageResponse', 'DetectResponse', 'TranslateResponse',
    'split_list_by_content_size'
]
