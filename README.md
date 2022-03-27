# pygtrans

谷歌翻译, 支持 **APIKEY**

- [Github](https://github.com/foyoux/pygtrans)
- [语言支持列表](https://pygtrans.readthedocs.io/zh_CN/latest/langs.html)

[![](https://img.shields.io/github/v/release/foyoux/pygtrans)](https://github.com/foyoux/pygtrans/releases) ![](https://img.shields.io/github/last-commit/foyoux/pygtrans) [![Downloads](https://static.pepy.tech/personalized-badge/pygtrans?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/pygtrans)



## 安装

[![](https://img.shields.io/pypi/pyversions/pygtrans)](https://pypi.org/project/pygtrans/) 

```bash
pip install -U pygtrans
```


## 基本功能

- [x] 获取语言支持列表
- [x] 自动检测语言, 支持批量
- [x] 文本/HTML 翻译, 支持批量
- [x] 支持 TTS


## 快速入门

```python
from pygtrans import Translate

client = Translate(proxies={'https': 'http://localhost:10809'})

# 检测语言
text = client.detect('Answer the question.')
assert text.language == 'en'

# 翻译句子
text = client.translate('Look at these pictures and answer the questions.')
assert text.translatedText == '看这些图片，回答问题。'

# 批量翻译
texts = client.translate([
    'Good morning. What can I do for you?',
    'Read aloud and underline the sentences about booking a flight.',
    'May I have your name and telephone number?'
])
assert [text.translatedText for text in texts] == [
    '早上好。我能为你做什么？',
    '大声朗读并在有关预订航班的句子下划线。',
    '可以给我你的名字和电话号码吗？'
]

# 翻译到日语
text = client.translate('请多多指教', target='ja')
assert text.translatedText == 'お知らせ下さい'

# 翻译到韩语
text = client.translate('请多多指教', target='ko')
assert text.translatedText == '조언 부탁드립니다'

# 文本到语音
tts = client.tts('やめて', target='ja')
open('やめて.mp3', 'wb').write(tts)
```



## 最佳实践

1. `pygtrans`中包含两个翻译模块
   1. `Translate`: 
      - 完全免费，支持批量
      - 从2021年9月15日开始, 需要翻墙才能使用, 具体参考 [#8](https://github.com/foyoux/pygtrans/issues/8)
   2. `ApiKeyTranslate`: 需要有效的谷歌翻译 **API KEY**，[谷歌提供免费试用](https://cloud.google.com/translate/docs/quickstarts)
2. `Translate`的最佳实践:
   1. `http` 代理：`Translate(proxies={"https": "http://localhost:10809"})`
   2. `socks5` 代理: `Translate(proxies={"https": "socks5://localhost:10808"})`
   3. **重要**：尽量一次性多翻译，减少请求次数，参考 [#13](https://github.com/foyoux/pygtrans/issues/13)，比如一次性翻译 2000 / 5000 / 10000

