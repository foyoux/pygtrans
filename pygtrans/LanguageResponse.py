class LanguageResponse:
    def __init__(self, language: str, name: str = None):
        """

        :param language: 语言代码
        :param name: 语言名字
        """

        self.language = language
        self.name = name

    def __repr__(self):
        return self.__class__.__qualname__ + f'(language={self.language}, name={self.name})'
