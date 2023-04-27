"""表示一个失败的结果"""
import requests


class Null:
    """
    :param response: 请求失败的 :class:`requests.Response` 对象
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.msg = f'{self.response.status_code}: {requests.status_codes._codes[self.response.status_code]}\n{self.response.text}'

    def __repr__(self):
        return self.msg
