"""语言对象"""
from dataclasses import dataclass


@dataclass
class LanguageResponse:
    language: str
    """语言代码"""
    name: str = None
    """语言名字"""
