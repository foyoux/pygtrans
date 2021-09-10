# pygtrans

**pygtrans**: *python google translate*

谷歌翻译, 支持 **APIKEY**

- [github](https://github.com/foyoux/pygtrans)
- [pypi](https://pypi.org/project/pygtrans/)
- [文档](https://pygtrans.readthedocs.io/zh_CN/latest/)

![test badge](https://github.com/foyoux/pygtrans/actions/workflows/python-test.yml/badge.svg) [![](https://img.shields.io/pypi/pyversions/pygtrans)](https://pypi.org/project/pygtrans/) [![](https://img.shields.io/github/v/release/foyoux/pygtrans)](https://github.com/foyoux/pygtrans/releases) ![](https://img.shields.io/github/last-commit/foyoux/pygtrans) [![Downloads](https://static.pepy.tech/personalized-badge/pygtrans?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/pygtrans)

> 重新写的博文, 也许会清晰一点, 大家也可以看看
>
> https://juejin.cn/post/6986599019782864933/

## 基本功能

- [x] 获取语言支持列表
- [x] 自动检测语言, 支持批量
- [x] 文本/HTML 翻译, 支持批量
- [x] 支持 TTS
- [x] 支持 Edge 大声朗读

## 安装

**环境要求**: `>= python 3.6`

```bash
pip install pygtrans
```

或者

```bash
pip install pygtrans -i https://pypi.org/simple
```

必要时可以加个 `--upgrade` 参数

## 快速入门

```python
from pygtrans import Translate

client = Translate()

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

## 基本介绍

`pygtrans`包中有两个需要关心的模块

1. `Translate`: 通过`谷歌翻译`API接口实现, 可直接使用, 但可能不稳定
2. `ApiKeyTranslate`: 通过`Google Cloud Translate APIs`实现, 需要提供一个有效的`APIKEY`
   , [谷歌提供免费试用](https://cloud.google.com/translate/docs/quickstarts)

### 二者的差异

|                 |                             缺点                             |                            优点                             |
| :-------------: | :----------------------------------------------------------: | :---------------------------------------------------------: |
|    Translate    |                      稳定性无法得到保证                      | 免费, 可直接使用<br/>亲测这货一次性可以翻译 **10万** 个句子 |
| ApiKeyTranslate | 需要`money`<br/>翻译内容一次性最多 **102400** bytes<br/>一次性最多翻译 **
128** 个句子 |                          比较稳定                           |

- **Translate** 未作任何限制, 如果大家使用过程中出现问题, 请大家 [留言](https://github.com/foyoux/pygtrans/issues/new)
- **ApiKeyTranslate** 的官方限制, 已在代码中容错, 唯一需要注意的是: *单个句子不要超过* **102400** *bytes*

### 关于`Null`模块

表示一个失败的结果, 如果想判断翻译是否成功, 判断返回是否为`Null`对象即可

```python
from pygtrans import Translate, Null

client = Translate()
text = client.translate('Hello')
if isinstance(text, Null):
    print("翻译失败")
else:
    print("翻译成功")
```

*建议按需判断, 一般直接使用*

## 基本使用

### 使用`Translate`

- **获取支持语言**: 该功能从代码中删除, 以 [语言支持列表](https://pygtrans.readthedocs.io/zh_CN/latest/langs.html) 方式提供
- **语言检测**: 方法`detect`不支持批量检测,
  如需批量检测请使用 [`translate_and_detect`](https://pygtrans.readthedocs.io/zh_CN/latest/pygtrans.html#pygtrans.Translate.Translate.translate_and_detect)
  方法

```python
from pygtrans import Translate

client = Translate()
d = client.detect('你好')
assert d.language == 'zh-CN'
```

- **文本翻译**: 使用`translate`方法, 默认就是`HTML`模式翻译,
  详细参数设置请移步至 [pygtrans文档](https://pygtrans.readthedocs.io/zh_CN/latest/pygtrans.html#pygtrans.Translate.Translate)

```python
from pygtrans import Translate

client = Translate()
text1 = client.translate('English')
assert text1.translatedText == '英语'

text2 = client.translate('喜欢', target='en')
assert text2.translatedText == 'love'

# 批量翻译
texts = client.translate(['Hello', 'World'])
for text in texts:
    print(text.translatedText)
# 你好
# 世界
```

修改默认语言, 请移步至 [pygtrans文档](https://pygtrans.readthedocs.io/zh_CN/latest/pygtrans.html#pygtrans.Translate.Translate)

- **TTS**: 从文本到语言

```python
from pygtrans import Translate

client = Translate()
tts = client.tts('你好')
open('你好.mp3', 'wb').write(tts)
```

[你好.mp3](images/你好.mp3)

```python
tts = client.tts('やめて', target='ja')
open('やめて.mp3', 'wb').write(tts)
```

[やめて.mp3](images/やめて.mp3)

```python
tts = client.tts('一二三四五, 上山打老虎')
open('一二三四五.mp3', 'wb').write(tts)
```

[一二三四五.mp3](images/一二三四五.mp3)

```python
tts = client.tts("""
我的小鱼你醒了，还认识早晨吗？

昨夜你曾经说，愿夜幕永不降临。

你的香腮边轻轻滑落的，是你的泪，还是我的泪？

初吻吻别的那个季节，不是已经哭过了嘛？

我的指尖还记忆着，你慌乱的心跳。

温柔的体香里，那一绺长发飘飘。
""")
open('我的小鱼你醒了.mp3', 'wb').write(tts)
```

[我的小鱼你醒了.mp3](images/我的小鱼你醒了.mp3)

### 使用`ApiKeyTranslate`

请参考 [pygtrans文档](https://pygtrans.readthedocs.io/zh_CN/latest/pygtrans.html#module-pygtrans.ApiKeyTranslate)

### 使用`ReadAloud`

```python
"""Edge大声朗读演示

如果发现速度特别慢, 请前往 `https://www.ipaddress.com/`, 
对 `speech.platform.bing.com` 和 `azure.microsoft.com`
进行IP解析, 并反映到 hosts 文件中
eg:
    13.107.21.200	speech.platform.bing.com
    13.107.42.16	azure.microsoft.com
"""
from pygtrans import ReadAloud, Voice

if __name__ == '__main__':
    edge = ReadAloud()
    # 推荐使用 tts_edge
    # x = edge.tts_edge('老师, 节日快乐', out='1.mp3')
    x = edge.tts_azure('老师, 节日快乐', out='1.mp3')
    print(x)
    x = edge.tts_azure('老师, 节日快乐', out='2.mp3', voice=Voice.zh_TW_HsiaoChenNeural)
    print(x)
    x = edge.tts_azure('老师, 节日快乐', out='3.mp3', voice=Voice.zh_HK_HiuMaanNeural)
    print(x)
    x = edge.tts_azure('老师, 节日快乐', out='4.mp3', voice=Voice.zh_CN_YunyangNeural)
```

## 本文档可能会滞后, `pip install pygtrans` 亲自尝试下吧~

### [有问题?](https://github.com/foyoux/pygtrans/issues/new)

## 欢迎大家反馈和建议



