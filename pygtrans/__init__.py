"""谷歌翻译"""

from .ApiKeyTranslate import ApiKeyTranslate
from .DetectResponse import DetectResponse
from .LanguageResponse import LanguageResponse
from .Null import Null
from .Translate import Translate
from .TranslateResponse import TranslateResponse

__apikey__ = '<your-apikey>'

__title__ = 'pygtrans'
__description__ = 'Google Translate, support APIKEY'
__url__ = 'https://github.com/foyoux/pygtrans'
__version__ = '1.0.1'
__author__ = 'foyou'
__author_email__ = 'yimi.0822@qq.com'
__license__ = 'MIT'
__copyright__ = f'Copyright 2021 {__author__}'
__ide__ = 'PyCharm - https://www.jetbrains.com/pycharm/'


__all__ = ['Translate', 'ApiKeyTranslate', 'Null', 'LanguageResponse', 'DetectResponse', 'TranslateResponse']
