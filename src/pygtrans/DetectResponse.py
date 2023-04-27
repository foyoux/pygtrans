"""DetectResponse"""


class DetectResponse:
    """DetectResponse"""

    def __init__(self, language: str, isReliable: bool = True, confidence: float = 1.0):
        """

        :param language: 检测到的语言
        :param isReliable: (已弃用) 表示语言检测结果是否可靠
        :param confidence: (已弃用) 此语言检测结果的置信度
        """

        self.language = language
        self.isReliable = isReliable
        self.confidence = confidence

    def __repr__(self):
        return self.__class__.__qualname__ + f'(language={repr(self.language)}, isReliable={repr(self.isReliable)}, confidence={repr(self.confidence)})'
