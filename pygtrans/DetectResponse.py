"""文本片段的语言检测结果"""
from dataclasses import dataclass


@dataclass
class DetectResponse:
    language: str
    """检测到的语言"""
    isReliable: bool = True
    """(已弃用) 表示语言检测结果是否可靠"""
    confidence: float = 1.0
    """(已弃用) 此语言检测结果的置信度"""
