# pygtrans

谷歌翻译, 支持 **APIKEY**

[![](https://img.shields.io/github/v/release/foyoux/pygtrans)](https://github.com/foyoux/pygtrans/releases) ![](https://img.shields.io/github/last-commit/foyoux/pygtrans) [![Downloads](https://static.pepy.tech/personalized-badge/pygtrans?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/pygtrans)

## 安装

[![](https://img.shields.io/pypi/pyversions/pygtrans)](https://pypi.org/project/pygtrans/)

```shell
# 推荐
pip install -U pygtrans
```

```shell
# 可选
pip install git+ssh://git@github.com/foyoux/pygtrans.git
pip install git+https://github.com/foyoux/pygtrans.git
```

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

## 支持的语言

<details><summary>支持的源语言，共 242 种</summary>
<p>

```json
{
  "auto": "检测语言",
  "ab": "阿布哈兹语",
  "sq": "阿尔巴尼亚语",
  "aa": "阿法尔语",
  "ar": "阿拉伯语",
  "alz": "阿卢尔语",
  "am": "阿姆哈拉语",
  "ach": "阿乔利语",
  "as": "阿萨姆语",
  "az": "阿塞拜疆语",
  "awa": "阿瓦德语",
  "av": "阿瓦尔语",
  "ee": "埃维语",
  "ay": "艾马拉语",
  "ga": "爱尔兰语",
  "et": "爱沙尼亚语",
  "oc": "奥克语",
  "or": "奥利亚语",
  "om": "奥罗莫语",
  "os": "奥塞梯语",
  "tpi": "巴布亚皮钦语",
  "bew": "巴达维语",
  "ban": "巴厘语",
  "ba": "巴什基尔语",
  "eu": "巴斯克语",
  "btx": "巴塔克卡罗语",
  "bbc": "巴塔克托巴语",
  "bts": "巴塔克西马隆贡语",
  "bci": "巴乌雷语",
  "be": "白俄罗斯语",
  "bm": "班巴拉语",
  "pag": "邦阿西楠语",
  "pam": "邦板牙语",
  "bg": "保加利亚语",
  "nso": "北索托语",
  "bem": "奔巴语",
  "bik": "比科尔语",
  "bal": "俾路支语",
  "is": "冰岛语",
  "pl": "波兰语",
  "bs": "波斯尼亚语",
  "fa": "波斯语",
  "bho": "博杰普尔语",
  "bua": "布里亚特语",
  "br": "布列塔尼语",
  "bo": "藏语",
  "chm": "草原马里语",
  "ch": "查莫罗语",
  "ce": "车臣语",
  "chk": "楚克语",
  "cv": "楚瓦什语",
  "tn": "茨瓦纳语",
  "ts": "聪加语",
  "fa-AF": "达里语",
  "tt": "鞑靼语",
  "da": "丹麦语",
  "shn": "掸语",
  "tet": "德顿语",
  "de": "德语",
  "dv": "迪维希语",
  "dyu": "迪尤拉语",
  "tiv": "蒂夫语",
  "din": "丁卡语",
  "doi": "多格拉语",
  "ru": "俄语",
  "ndc-ZW": "恩道语",
  "nr": "恩德贝莱语（南部）",
  "dov": "恩敦贝语",
  "bm-Nkoo": "恩科字母（西非书面文字）",
  "fo": "法罗语",
  "fr": "法语",
  "sa": "梵语",
  "tl": "菲律宾语",
  "fj": "斐济语",
  "fi": "芬兰语",
  "fon": "丰语",
  "fy": "弗里西语",
  "fur": "弗留利语",
  "ff": "富拉尼语",
  "kg": "刚果语",
  "km": "高棉语",
  "kl": "格陵兰语",
  "ka": "格鲁吉亚语",
  "gom": "贡根语",
  "gu": "古吉拉特语",
  "gn": "瓜拉尼语",
  "cnh": "哈卡钦语",
  "kk": "哈萨克语",
  "ht": "海地克里奥尔语",
  "ko": "韩语",
  "ha": "豪萨语",
  "nl": "荷兰语",
  "hrx": "洪斯吕克语",
  "ky": "吉尔吉斯语",
  "ktu": "吉土巴语",
  "gl": "加利西亚语",
  "ca": "加泰罗尼亚语",
  "gaa": "加语",
  "cs": "捷克语",
  "kac": "景颇语",
  "kn": "卡纳达语",
  "kr": "卡努里语",
  "kha": "卡西语",
  "kek": "凯克其语",
  "kv": "科米语",
  "xh": "科萨语",
  "co": "科西嘉语",
  "crh": "克里米亚鞑靼语",
  "hr": "克罗地亚语",
  "qu": "克丘亚语",
  "ku": "库尔德语（库尔曼吉语）",
  "ckb": "库尔德语（索拉尼）",
  "trp": "廓克博若克语",
  "la": "拉丁语",
  "ltg": "拉特加莱语",
  "lv": "拉脱维亚语",
  "lo": "老挝语",
  "lt": "立陶宛语",
  "lij": "利古里亚语",
  "li": "林堡语",
  "ln": "林加拉语",
  "rn": "隆迪语",
  "luo": "卢奥语",
  "lg": "卢干达语",
  "lb": "卢森堡语",
  "rw": "卢旺达语",
  "lmo": "伦巴第语",
  "ro": "罗马尼亚语",
  "rom": "罗姆语",
  "mad": "马都拉语",
  "gv": "马恩岛语",
  "mg": "马尔加什语",
  "mwr": "马尔瓦迪语",
  "mt": "马耳他语",
  "mr": "马拉地语",
  "ml": "马拉雅拉姆语",
  "ms": "马来语",
  "ms-Arab": "马来语（爪夷文）",
  "mk": "马其顿语",
  "mh": "马绍尔语",
  "mam": "玛姆语",
  "mai": "迈蒂利语",
  "mfe": "毛里裘斯克里奥耳语",
  "mi": "毛利语",
  "mni-Mtei": "梅泰语（曼尼普尔语）",
  "mn": "蒙古语",
  "bn": "孟加拉语",
  "min": "米南语",
  "lus": "米佐语",
  "my": "缅甸语",
  "hmn": "苗语",
  "nhe": "纳瓦特尔语（东部瓦斯特卡）",
  "af": "南非荷兰语",
  "st": "南索托语",
  "ne": "尼泊尔语",
  "new": "尼泊尔语言（尼瓦尔语）",
  "nus": "努尔语",
  "no": "挪威语",
  "pap": "帕皮阿门托语",
  "pa": "旁遮普语（果鲁穆奇文）",
  "pa-Arab": "旁遮普语（沙木基文）",
  "pt": "葡萄牙语（巴西）",
  "pt-PT": "葡萄牙语（葡萄牙）",
  "ps": "普什图语",
  "ny": "齐切瓦语",
  "cgg": "奇加语",
  "ak": "契维语",
  "ja": "日语",
  "sv": "瑞典语",
  "zap": "萨巴特克语",
  "se": "萨米语（北部）",
  "sm": "萨摩亚语",
  "sr": "塞尔维亚语",
  "kri": "塞拉利昂克里奥尔语",
  "crs": "塞舌尔克里奥尔语",
  "sg": "桑戈语",
  "sat-Latn": "桑塔利语",
  "si": "僧伽罗语",
  "eo": "世界语",
  "sk": "斯洛伐克语",
  "sl": "斯洛文尼亚语",
  "ss": "斯瓦特语",
  "sw": "斯瓦希里语",
  "gd": "苏格兰盖尔语",
  "sus": "苏苏语",
  "ceb": "宿务语",
  "so": "索马里语",
  "tg": "塔吉克语",
  "ber": "塔马齐格特语（提非纳文）",
  "ber-Latn": "塔马塞特语",
  "ty": "塔希提语",
  "te": "泰卢固语",
  "ta": "泰米尔语",
  "th": "泰语",
  "to": "汤加语",
  "ti": "提格里尼亚语",
  "tcy": "图鲁语",
  "tum": "图姆布卡语",
  "tyv": "图瓦语",
  "tr": "土耳其语",
  "tk": "土库曼语",
  "war": "瓦瑞语",
  "mak": "望加锡语",
  "cy": "威尔士语",
  "vec": "威尼斯语",
  "ug": "维吾尔语",
  "ve": "文达语",
  "wo": "沃洛夫语",
  "udm": "乌德穆尔特语",
  "ur": "乌尔都语",
  "uk": "乌克兰语",
  "uz": "乌兹别克语",
  "es": "西班牙语",
  "szl": "西里西亚语",
  "scn": "西西里语",
  "iw": "希伯来语",
  "el": "希腊语",
  "hil": "希利盖农语",
  "haw": "夏威夷语",
  "sd": "信德语",
  "hu": "匈牙利语",
  "sn": "修纳语",
  "su": "巽他语",
  "jam": "牙买加土语",
  "sah": "雅库特语",
  "hy": "亚美尼亚语",
  "ace": "亚齐语",
  "iba": "伊班语",
  "ig": "伊博语",
  "ilo": "伊洛卡诺语",
  "it": "意大利语",
  "yi": "意第绪语",
  "hi": "印地语",
  "id": "印尼语",
  "en": "英语",
  "yua": "尤卡坦玛雅语",
  "yo": "约鲁巴语",
  "yue": "粤语",
  "vi": "越南语",
  "jw": "爪哇语",
  "zh-CN": "中文",
  "dz": "宗卡语",
  "zu": "祖鲁语"
}
```

</p>
</details>

<details><summary>支持的目标语言，共 243 种</summary>
<p>

```json
 {
  "ab": "阿布哈兹语",
  "sq": "阿尔巴尼亚语",
  "aa": "阿法尔语",
  "ar": "阿拉伯语",
  "alz": "阿卢尔语",
  "am": "阿姆哈拉语",
  "ach": "阿乔利语",
  "as": "阿萨姆语",
  "az": "阿塞拜疆语",
  "awa": "阿瓦德语",
  "av": "阿瓦尔语",
  "ee": "埃维语",
  "ay": "艾马拉语",
  "ga": "爱尔兰语",
  "et": "爱沙尼亚语",
  "oc": "奥克语",
  "or": "奥利亚语",
  "om": "奥罗莫语",
  "os": "奥塞梯语",
  "tpi": "巴布亚皮钦语",
  "bew": "巴达维语",
  "ban": "巴厘语",
  "ba": "巴什基尔语",
  "eu": "巴斯克语",
  "btx": "巴塔克卡罗语",
  "bbc": "巴塔克托巴语",
  "bts": "巴塔克西马隆贡语",
  "bci": "巴乌雷语",
  "be": "白俄罗斯语",
  "bm": "班巴拉语",
  "pag": "邦阿西楠语",
  "pam": "邦板牙语",
  "bg": "保加利亚语",
  "nso": "北索托语",
  "bem": "奔巴语",
  "bik": "比科尔语",
  "bal": "俾路支语",
  "is": "冰岛语",
  "pl": "波兰语",
  "bs": "波斯尼亚语",
  "fa": "波斯语",
  "bho": "博杰普尔语",
  "bua": "布里亚特语",
  "br": "布列塔尼语",
  "bo": "藏语",
  "chm": "草原马里语",
  "ch": "查莫罗语",
  "ce": "车臣语",
  "chk": "楚克语",
  "cv": "楚瓦什语",
  "tn": "茨瓦纳语",
  "ts": "聪加语",
  "fa-AF": "达里语",
  "tt": "鞑靼语",
  "da": "丹麦语",
  "shn": "掸语",
  "tet": "德顿语",
  "de": "德语",
  "dv": "迪维希语",
  "dyu": "迪尤拉语",
  "tiv": "蒂夫语",
  "din": "丁卡语",
  "doi": "多格拉语",
  "ru": "俄语",
  "ndc-ZW": "恩道语",
  "nr": "恩德贝莱语（南部）",
  "dov": "恩敦贝语",
  "bm-Nkoo": "恩科字母（西非书面文字）",
  "fo": "法罗语",
  "fr": "法语",
  "sa": "梵语",
  "tl": "菲律宾语",
  "fj": "斐济语",
  "fi": "芬兰语",
  "fon": "丰语",
  "fy": "弗里西语",
  "fur": "弗留利语",
  "ff": "富拉尼语",
  "kg": "刚果语",
  "km": "高棉语",
  "kl": "格陵兰语",
  "ka": "格鲁吉亚语",
  "gom": "贡根语",
  "gu": "古吉拉特语",
  "gn": "瓜拉尼语",
  "cnh": "哈卡钦语",
  "kk": "哈萨克语",
  "ht": "海地克里奥尔语",
  "ko": "韩语",
  "ha": "豪萨语",
  "nl": "荷兰语",
  "hrx": "洪斯吕克语",
  "ky": "吉尔吉斯语",
  "ktu": "吉土巴语",
  "gl": "加利西亚语",
  "ca": "加泰罗尼亚语",
  "gaa": "加语",
  "cs": "捷克语",
  "kac": "景颇语",
  "kn": "卡纳达语",
  "kr": "卡努里语",
  "kha": "卡西语",
  "kek": "凯克其语",
  "kv": "科米语",
  "xh": "科萨语",
  "co": "科西嘉语",
  "crh": "克里米亚鞑靼语",
  "hr": "克罗地亚语",
  "qu": "克丘亚语",
  "ku": "库尔德语（库尔曼吉语）",
  "ckb": "库尔德语（索拉尼）",
  "trp": "廓克博若克语",
  "la": "拉丁语",
  "ltg": "拉特加莱语",
  "lv": "拉脱维亚语",
  "lo": "老挝语",
  "lt": "立陶宛语",
  "lij": "利古里亚语",
  "li": "林堡语",
  "ln": "林加拉语",
  "rn": "隆迪语",
  "luo": "卢奥语",
  "lg": "卢干达语",
  "lb": "卢森堡语",
  "rw": "卢旺达语",
  "lmo": "伦巴第语",
  "ro": "罗马尼亚语",
  "rom": "罗姆语",
  "mad": "马都拉语",
  "gv": "马恩岛语",
  "mg": "马尔加什语",
  "mwr": "马尔瓦迪语",
  "mt": "马耳他语",
  "mr": "马拉地语",
  "ml": "马拉雅拉姆语",
  "ms": "马来语",
  "ms-Arab": "马来语（爪夷文）",
  "mk": "马其顿语",
  "mh": "马绍尔语",
  "mam": "玛姆语",
  "mai": "迈蒂利语",
  "mfe": "毛里裘斯克里奥耳语",
  "mi": "毛利语",
  "mni-Mtei": "梅泰语（曼尼普尔语）",
  "mn": "蒙古语",
  "bn": "孟加拉语",
  "min": "米南语",
  "lus": "米佐语",
  "my": "缅甸语",
  "hmn": "苗语",
  "nhe": "纳瓦特尔语（东部瓦斯特卡）",
  "af": "南非荷兰语",
  "st": "南索托语",
  "ne": "尼泊尔语",
  "new": "尼泊尔语言（尼瓦尔语）",
  "nus": "努尔语",
  "no": "挪威语",
  "pap": "帕皮阿门托语",
  "pa": "旁遮普语（果鲁穆奇文）",
  "pa-Arab": "旁遮普语（沙木基文）",
  "pt": "葡萄牙语（巴西）",
  "pt-PT": "葡萄牙语（葡萄牙）",
  "ps": "普什图语",
  "ny": "齐切瓦语",
  "cgg": "奇加语",
  "ak": "契维语",
  "ja": "日语",
  "sv": "瑞典语",
  "zap": "萨巴特克语",
  "se": "萨米语（北部）",
  "sm": "萨摩亚语",
  "sr": "塞尔维亚语",
  "kri": "塞拉利昂克里奥尔语",
  "crs": "塞舌尔克里奥尔语",
  "sg": "桑戈语",
  "sat-Latn": "桑塔利语",
  "si": "僧伽罗语",
  "eo": "世界语",
  "sk": "斯洛伐克语",
  "sl": "斯洛文尼亚语",
  "ss": "斯瓦特语",
  "sw": "斯瓦希里语",
  "gd": "苏格兰盖尔语",
  "sus": "苏苏语",
  "ceb": "宿务语",
  "so": "索马里语",
  "tg": "塔吉克语",
  "ber": "塔马齐格特语（提非纳文）",
  "ber-Latn": "塔马塞特语",
  "ty": "塔希提语",
  "te": "泰卢固语",
  "ta": "泰米尔语",
  "th": "泰语",
  "to": "汤加语",
  "ti": "提格里尼亚语",
  "tcy": "图鲁语",
  "tum": "图姆布卡语",
  "tyv": "图瓦语",
  "tr": "土耳其语",
  "tk": "土库曼语",
  "war": "瓦瑞语",
  "mak": "望加锡语",
  "cy": "威尔士语",
  "vec": "威尼斯语",
  "ug": "维吾尔语",
  "ve": "文达语",
  "wo": "沃洛夫语",
  "udm": "乌德穆尔特语",
  "ur": "乌尔都语",
  "uk": "乌克兰语",
  "uz": "乌兹别克语",
  "es": "西班牙语",
  "szl": "西里西亚语",
  "scn": "西西里语",
  "iw": "希伯来语",
  "el": "希腊语",
  "hil": "希利盖农语",
  "haw": "夏威夷语",
  "sd": "信德语",
  "hu": "匈牙利语",
  "sn": "修纳语",
  "su": "巽他语",
  "jam": "牙买加土语",
  "sah": "雅库特语",
  "hy": "亚美尼亚语",
  "ace": "亚齐语",
  "iba": "伊班语",
  "ig": "伊博语",
  "ilo": "伊洛卡诺语",
  "it": "意大利语",
  "yi": "意第绪语",
  "hi": "印地语",
  "id": "印尼语",
  "en": "英语",
  "yua": "尤卡坦玛雅语",
  "yo": "约鲁巴语",
  "yue": "粤语",
  "vi": "越南语",
  "jw": "爪哇语",
  "zh-TW": "中文（繁体）",
  "zh-CN": "中文（简体）",
  "dz": "宗卡语",
  "zu": "祖鲁语"
}
```

</p>
</details>

在库中访问

```python
from pygtrans import SOURCE_LANGUAGES, TARGET_LANGUAGES

print('支持的源语言:')
for code, lang in SOURCE_LANGUAGES.items():
    print(code, lang)

print('支持的目标语言:')
for code, lang in TARGET_LANGUAGES.items():
    print(code, lang)

```

## 必看说明

1. `pygtrans`中包含两个翻译模块
    1. `Translate`:
        - 完全免费，支持批量
        - 从2021年9月15日开始, 需要科学上网才能使用, 具体参考 [#8](https://github.com/foyoux/pygtrans/issues/8)
    2. `ApiKeyTranslate`: 需要有效的谷歌翻译 **API KEY**，[谷歌提供免费试用](https://cloud.google.com/translate/docs/quickstarts)
2. `Translate`的最佳实践:
    1. `http` 代理：`Translate(proxies={"https": "http://localhost:10809"})`
    2. `socks5` 代理: `Translate(proxies={"https": "socks5://localhost:10808"})`
    3. **重要**：尽量一次性多翻译，减少请求次数，参考 [#13](https://github.com/foyoux/pygtrans/issues/13)，比如一次性翻译
       2000 / 5000 / 10000，甚至一次性 100000 条
3. 如果 `429`, 可尝试切换 domain, 具体参考 [#37](https://github.com/foyoux/pygtrans/issues/37)