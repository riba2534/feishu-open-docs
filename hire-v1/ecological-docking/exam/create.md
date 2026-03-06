---
title: "创建试卷列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_exam_paper/create"
updateTime: "1725008225000"
---

# 创建试卷列表

飞书招聘的笔试服务商，在完成[账号绑定](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_account/events/created)后，可通过本接口在客户的笔试帐号下创建试卷列表。若客户的笔试账号为「未激活」、「停用」状态，则试卷创建成功后，客户的账号将变为「正常」状态，可正常安排笔试。


> **Warning**: 本接口为全量更新，多次调用时，将生效最后一次调用传入的试卷列表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/eco_exam_papers |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:exam` 更新笔试信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `account_id` | `string` | 是 | 笔试账号 ID，可通过[账号绑定](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/eco_account/events/created)事件获取<br>**示例值**："7147998241542539527" |
| `paper_list` | `eco_exam_paper_data\[\]` | 是 | 试卷列表 |
| &nbsp;&nbsp;└ `id` | `string` | 是 | 试卷 ID。由调用方自定义 **注意**：试卷 ID 长度应不超过`255`字符，超出部分将被截断<br>**示例值**："7147998241542539527"<br>**数据校验规则**：<br>- 最小长度：`1` 字符 |
| &nbsp;&nbsp;└ `name` | `string` | 是 | 试卷名称 **注意**：试卷名称长度应不超过`255`字符，超出部分将被截断<br>**示例值**："春季测评"<br>**数据校验规则**：<br>- 最小长度：`1` 字符 |
| &nbsp;&nbsp;└ `duration` | `int` | 否 | 考试时长（分钟）<br>**示例值**：30 |
| &nbsp;&nbsp;└ `question_count` | `int` | 否 | 试卷题目数量<br>**示例值**：30 |
| &nbsp;&nbsp;└ `start_time` | `string` | 否 | 笔试开始时间，毫秒时间戳。留空或不传表示不限制开始时间。 **注意**：若传值且`end_time`不为空，则开始时间必须小于结束时间<br>**示例值**："1658676234053" |
| &nbsp;&nbsp;└ `end_time` | `string` | 否 | 笔试结束时间，毫秒时间戳。留空或不传表示不限制结束时间 **注意**：若传值且`start_time `不为空，则结束时间必须大于开始时间<br>**示例值**："1672444800000" |


### 请求体示例

```json
{
    "account_id": "7147998241542539527",
    "paper_list": [
        {
            "id": "7147998241542539527",
            "name": "春季测评",
            "duration": 30,
            "question_count": 30,
            "start_time": "1658676234053",
            "end_time": "1672444800000"
        }
    ]
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
    "msg": "SUCCESS",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位问题或联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


