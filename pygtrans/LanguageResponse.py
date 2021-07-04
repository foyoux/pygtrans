class LanguageResponse:
    def __init__(self, language: str, name: str = None):
        """

        :param language: 语言代码
        :param name: 语言名字
        """

        self.language = language
        self.name = name
