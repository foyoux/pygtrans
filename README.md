# pygtrans

**pygtrans**: *python google translate* 

谷歌翻译, 支持 **APIKEY**

- [github](https://github.com/foyoux/pygtrans)
- [pypi](https://pypi.org/project/pygtrans/)
- [文档](https://pygtrans.readthedocs.io/zh_CN/latest/)

![](https://img.shields.io/pypi/pyversions/pygtrans) ![](https://img.shields.io/github/v/release/foyoux/pygtrans) ![](https://img.shields.io/github/last-commit/foyoux/pygtrans)

## 基本功能

- [x] 获取语言支持列表
- [x] 自动检测语言, 支持批量
- [x] 文本/HTML 翻译, 支持批量


## 安装
**环境要求**: `>= python 3.6`

```bat
pip install pygtrans
```

或者

```
pip install pygtrans -i https://pypi.org/simple
```



## 快速入门

```python
from pygtrans import Translate

client = Translate()
text = client.translate('Google Translate')
print(text.translatedText)  # 谷歌翻译
```

## 基本介绍

`pygtrans`包中有两个需要关心的模块
1. `Translate`: 通过`谷歌翻译`API接口实现, 可直接使用, 但可能不稳定
2. `ApiKeyTranslate`: 通过`Google Cloud Translate APIs`实现, 需要提供一个有效的`APIKEY`, [谷歌提供免费试用](https://cloud.google.com/translate/docs/quickstarts)

### 二者的差异

|                 |                           缺点                           |    优点    |
| :-------------: | :------------------------------------------------------: | :--------: |
|    Translate    | 可能不稳定(使用频率), 需要更换`User-Agent`或者使用IP代理 | 可直接使用 |
| ApiKeyTranslate |   试用结束后, 需要`money`&单个字符串限制`102400`bytes    | 无使用限制 |

#### 关于不稳定的问题 

1. 首先这是一个无法避免的问题, 任何类似工具都会存在这样的问题;
2. 在我测试(根本没请求几次)的过程中, 出现 `429 Too Many Requests` 的情况, 检查后发现是 `User-Agent` 没有设置上去, 
   修正后, 再没出现过. 如果大家后续碰到此种情况, 可放到 `issues` 中讨论, 因为我目前还不知道多高的频率会被限制, 
   只测试过几次循环 100 次请求, 期间未出现问题.

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
- **语言检测**: 方法`detect`不支持批量检测, 如需批量检测请使用 [`translate_and_detect`](https://pygtrans.readthedocs.io/zh_CN/latest/pygtrans.html#pygtrans.Translate.Translate.translate_and_detect) 方法

```python
from pygtrans import Translate

client = Translate()
d = client.detect('你好')
assert d.language == 'zh-CN'
```
- **文本翻译**: 使用`translate`方法, 默认就是`HTML`模式翻译, 详细参数设置请移步至 [pygtrans文档](https://pygtrans.readthedocs.io/zh_CN/latest/pygtrans.html#pygtrans.Translate.Translate)

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

- 修改默认语言, 请移步至 [pygtrans文档](https://pygtrans.readthedocs.io/zh_CN/latest/pygtrans.html#pygtrans.Translate.Translate)

### 使用`ApiKeyTranslate`

请参考 [pygtrans文档](https://pygtrans.readthedocs.io/zh_CN/latest/pygtrans.html#module-pygtrans.ApiKeyTranslate)




## 本文档可能会有所滞后, `pip install pygtrans` 亲自尝试下吧~

### [有问题?](https://github.com/foyoux/pygtrans/issues/new)
## 欢迎大家反馈和建议



