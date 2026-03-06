---
title: "创建外部面评"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/external_interview_assessment/create"
updateTime: "1725853641000"
---

# 创建外部面评

导入来自其他系统的面评信息，创建为外部面评。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/external_interview_assessments |
| HTTP Method | POST |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:external_application` 更新外部投递 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `external_id` | `string` | 否 | 外部系统面评主键（仅用于幂等）<br>**示例值**："123" |
| `username` | `string` | 否 | 面试官姓名<br>**示例值**："shaojiale" |
| `conclusion` | `int` | 否 | 面试结果<br>**示例值**：1<br>**可选值有**：<br>- `1`: 不通过 - `2`: 通过 - `3`: 待定 |
| `assessment_dimension_list` | `external_interview_assessment_dimension\[\]` | 否 | 评价维度列表 |
| &nbsp;&nbsp;└ `score` | `int` | 否 | 打分题分数（当题目类型为「打分题」时使用）<br>**示例值**：99 |
| &nbsp;&nbsp;└ `option` | `string` | 否 | 单选选项（当题目类型为「单选题」时使用）<br>**示例值**："opt" |
| &nbsp;&nbsp;└ `options` | `string\[\]` | 否 | 多选选项（当题目类型为「多选题」时使用）<br>**示例值**：["opt"] |
| &nbsp;&nbsp;└ `content` | `string` | 否 | 描述内容（当题目类型为「描述题」时使用）<br>**示例值**："content" |
| &nbsp;&nbsp;└ `assessment_type` | `int` | 否 | 题目类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 打分题 - `2`: 单选题 - `3`: 描述题 - `4`: 多选题 |
| &nbsp;&nbsp;└ `title` | `string` | 否 | 题目标题<br>**示例值**："title" |
| &nbsp;&nbsp;└ `description` | `string` | 否 | 题目描述<br>**示例值**："desc" |
| `content` | `string` | 否 | 综合记录<br>**示例值**："hello world" |
| `external_interview_id` | `string` | 是 | 外部面试 ID<br>**示例值**："6986199832494934316" |


### 请求体示例

```json
{
    "external_id": "123",
    "username": "shaojiale",
    "conclusion": 1,
    "assessment_dimension_list": [
        {
            "score": 99,
            "option": "opt",
            "options": [
                "opt"
            ],
            "content": "content",
            "assessment_type": 1,
            "title": "title",
            "description": "desc"
        }
    ],
    "content": "hello world",
    "external_interview_id": "6986199832494934316"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `external_interview_assessment` | `external_interview_assessment` | 外部面评信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 外部面评 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `username` | `string` | 面试官姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `conclusion` | `int` | 面试结果<br>**可选值有**：<br>- `1`: 不通过 - `2`: 通过 - `3`: 待定 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assessment_dimension_list` | `external_interview_assessment_dimension\[\]` | 评价维度列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `score` | `int` | 打分题分数（当题目类型为「打分题」时使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `string` | 单选选项（当题目类型为「单选题」时使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `string\[\]` | 多选选项（当题目类型为「多选题」时使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 描述内容（当题目类型为「描述题」时使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assessment_type` | `int` | 题目类型<br>**可选值有**：<br>- `1`: 打分题 - `2`: 单选题 - `3`: 描述题 - `4`: 多选题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 题目标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 题目描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 综合记录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `external_interview_id` | `string` | 外部面试 ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "external_interview_assessment": {
            "id": "6989181065243969836",
            "username": "shaojiale",
            "conclusion": 1,
            "assessment_dimension_list": [
                {
                    "score": 99,
                    "option": "opt",
                    "options": [
                        "opt"
                    ],
                    "content": "content",
                    "assessment_type": 1,
                    "title": "title",
                    "description": "desc"
                }
            ],
            "content": "hello world",
            "external_interview_id": "6986199832494934316"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请联系研发排查 |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


