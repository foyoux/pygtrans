"""文本翻译"""
from dataclasses import dataclass


@dataclass
class TranslateResponse:
    translatedText: str
    """翻译成目标语言的文本。"""
    detectedSourceLanguage: str = None
    """如果初始请求中没有传递源语言，则自动检测初始请求的源语言。如果通过了源语言，则不会自动检测语言，并且将省略此字段。"""
    model: str = None
    """翻译模型。可以是基于短语的机器翻译 (PBMT) 模型的基础，也可以是神经机器翻译 (NMT) 模型的 nmt。如果您的请求中没有包含模型参数，则该字段不会包含在响应中。"""
