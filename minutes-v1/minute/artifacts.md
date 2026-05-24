---
title: "获取妙记AI产物"
fullPath: "/uAjLw4CM/ukTMukTMukTM/minutes-v1/minute/artifacts"
updateTime: "1774523641000"
---

# 获取妙记AI产物

通过妙记唯一标识minute_token获取AI产物


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/minutes/v1/minutes/:minute_token/artifacts |
| HTTP Method | GET |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `minutes:minutes.artifacts:read` 获取妙记 AI 产物 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `minute_token` | `string` | 妙记唯一标识。可从妙记的 URL 链接中获取，一般为最后一串字符：https://sample.feishu.cn/minutes/obcnq3b9jl72l83w4f14xxxx<br>**示例值**："obcnq3b9jl72l83w4f149w9c"<br>**数据校验规则**：<br>- 长度范围：`24` ～ `24` 字符 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `summary` | `string` | 妙记总结 |
| &nbsp;&nbsp;└ `minute_chapters` | `minute_chapter\[\]` | 妙记章节 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 章节标题，用于区分纪要内不同的讨论模块，需简洁明确概括章节核心内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_ms` | `string` | 章节对应的讨论内容开始时间戳，单位为毫秒，用于定位会议录像或录音的对应片段。需与stop_ms配合使用，且数值需小于stop_ms。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `stop_ms` | `string` | 章节对应的讨论内容结束时间戳，单位为毫秒，用于定位会议录像或录音的对应片段。需与start_ms配合使用，且数值需大于start_ms。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `summary_content` | `string` | 章节的核心讨论内容摘要，需准确提炼该章节的决策结果、行动项、待跟进事项等关键信息。支持富文本格式，最大长度限制为10000字符。 |
| &nbsp;&nbsp;└ `minute_todos` | `minute_todo\[\]` | 妙记待办 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 待办内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assignees` | `string\[\]` | 负责人 |


### 响应体示例

```json
{"code":0,
"msg":"success",
"data":{"summary":"妙记总结",
"minute_chapters":[{"title":"项目进度回顾与风险评估",
"start_ms":"31000",
"stop_ms":"33000",
"summary_content":"1. 确认Q3项目交付节点为9月30日，延迟交付将触发合同违约条款；
2. 指派张三负责协调供应商资源，需在7月15日前提交资源保障方案；
3. 风险预警：核心组件供应链可能存在断供风险，需启动备选供应商评估流程。"}],
"minute_todos":[{
    "content": "提交资源保障方案",
    "assignees": [
        "张三"
    ]
}]}}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2091001 | param is invalid | 检查请求参数的类型或格式是否与接口要求一致 |
| 404 | 2091002 | resource not found | 请求的资源不存在，请检查输入的 minute_token 是否正确 |
| 400 | 2091003 | minute not ready, try later | 资源生成中，请稍后重试 |
| 400 | 2091004 | resource deleted | 资源已删除，无法访问，请确认输入的minute_token对应的资源是否存在 |
| 403 | 2091005 | permission deny | 权限校验不通过，请检查应用是否具备访问该资源的权限 |


