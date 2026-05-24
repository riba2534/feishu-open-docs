---
title: "添加/取消表情回应"
fullPath: "/ukTMukTMukTM/uIzNzUjLyczM14iM3MTN/drive-v2/comment_reaction/update_reaction"
updateTime: "1775723478000"
---

# 添加/取消表情回应

使用该接口可对云文档中的某条评论进行emoji表情回应或取消emoji表情回应。适用于用户需要对云文档评论进行emoji表情互动的场景。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/drive/v2/files/:file_token/comments/reaction |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `docs:document.comment:create` 添加、回复云文档中的评论 `docs:document.comment:write_only` 回复、修改、删除云文档中的评论 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `file_token` | `string` | 文件的唯一标识令牌，用于定位目标文件。可通过调用「获取文件元信息」或「文件上传」接口获取。<br>**示例值**："ppHV2Xepq2BQk3K79FTB"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_type` | `string` | 是 | 文件类型，用于区分不同类型的云文档，可选值需参考[开放平台文件类型枚举](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)<br>**示例值**：docx<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `action` | `string` | 是 | 操作类型<br>**示例值**："add"<br>**可选值有**：<br>- `add`: 添加表情回复 - `delete`: 删除添加的reaction<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |
| `reply_id` | `string` | 是 | 回复 ID<br>可通过调用 添加回复、获取回复信息 接口获取<br>**示例值**："1234567890"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |
| `reaction_type` | `string` | 是 | reaction 类型<br>可选值：ANGRY, APPLAUSE, ATTENTION, AWESOME, BEAR, BEER, BETRAYED, BIGKISS, BLACKFACE, BLUBBER, BLUSH, BOMB, CAKE, CHUCKLE, CLAP, CLEAVER, COMFORT, CRAZY, CRY, CUCUMBER, DETERGENT, DIZZY, DONE, DONNOTGO, DROOL, DROWSY, DULL, DULLSTARE, EATING, EMBARRASSED, ENOUGH, ERROR, EYESCLOSED, FACEPALM, FINGERHEART, FISTBUMP, FOLLOWME, FROWN, GIFT, GLANCE, GOODJOB, HAMMER, HAUGHTY, HEADSET, HEART, HEARTBROKEN, HIGHFIVE, HUG, HUSKY, INNOCENTSMILE, JIAYI, JOYFUL, KISS, LAUGH, LIPS, LOL, LOOKDOWN, LOVE, MONEY, MUSCLE, NOSEPICK, OBSESSED, OK, PARTY, PETRIFIED, POOP, PRAISE, PROUD, PUKE, RAINBOWPUKE, ROSE, SALUTE, SCOWL, SHAKE, SHHH, SHOCKED, SHOWOFF, SHY, SICK, SILENT, SKULL, SLAP, SLEEP, SLIGHT, SMART, SMILE, SMIRK, SMOOCH, SMUG, SOB, SPEECHLESS, SPITBLOOD, STRIVE, SWEAT, TEARS, TEASE, TERROR, THANKS, THINKING, THUMBSUP, TOASTED, TONGUE, TRICK, UPPERLEFT, WAIL, WAVE, WELLDONE, WHAT, WHIMPER, WINK, WITTY, WOW, WRONGED, XBLUSH, YAWN, YEAH, FIREWORKS, BULL, CALF, AWESOMEN, 2021, CANDIEDHAWS, REDPACKET, FORTUNE, LUCK, FIRECRACKER, Yes, No, Get, LGTM, Lemon, EatingFood, Hundred, MinusOne, ThumbsDown, Fire, OKR, Drumstick, BubbleTea, Loudspeaker, Pin, Coffee, Alarm, Trophy, Music, Typing, Pepper, CheckMark, CrossMark.<br>**示例值**："ANGRY"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |


### 请求体示例

```json
{
    "action": "add",
    "reply_id": "1234567890",
    "reaction_type": "ANGRY"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1061001 | server internal error | 服务内部错误，请稍后重试，若仍报错请联系[技术支持](https://applink.feishu.cn/client/helpdesk) |
| 400 | 1061002 | invalid params | 检查请求参数是否规范 |
| 401 | 1061004 | no permission | 由于权限不足，访问被拒绝。请确认应用已申请该接口所需权限，具体操作参考权限申请文档 |
| 404 | 1061003 | docs had been deleted | 检查待回复云文档是否已被删除 |


