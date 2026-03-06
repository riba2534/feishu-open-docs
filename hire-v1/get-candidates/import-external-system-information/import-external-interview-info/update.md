---
title: "更新外部面试"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/external_interview/update"
updateTime: "1733205907000"
---

# 更新外部面试

更新外部面试信息。


## 注意事项
该接口会对原面试以及面试评价内容进行全量覆盖更新。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/external_interviews/:external_interview_id |
| HTTP Method | PUT |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:external_application` 更新外部投递 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `external_interview_id` | `string` | 外部面试 ID，可通过[查询外部面试列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/external_interview/batch_query)接口获取<br>**示例值**："6960663240925956660" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `external_application_id` | `string` | 是 | 外部投递 ID，可通过[查询外部投递列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/external_application/list)接口获取<br>**示例值**："6960663240925956437" |
| `participate_status` | `int` | 否 | 参与状态<br>**示例值**：1<br>**可选值有**：<br>- `1`: 未参与 - `2`: 参与 - `3`: 爽约 |
| `begin_time` | `int` | 否 | 开始时间，毫秒时间戳（字段类型为：int64）<br>**示例值**：1618500278638 |
| `end_time` | `int` | 否 | 结束时间，毫秒时间戳（字段类型为：int64）<br>**示例值**：1618500278639 |
| `interview_assessments` | `external_interview_assessment\[\]` | 否 | 面试评价列表 |
| &nbsp;&nbsp;└ `username` | `string` | 否 | 面试官姓名<br>**示例值**："张三" |
| &nbsp;&nbsp;└ `conclusion` | `int` | 否 | 面试结果<br>**示例值**：1<br>**可选值有**：<br>- `1`: 不通过 - `2`: 通过 - `3`: 待定 |
| &nbsp;&nbsp;└ `assessment_dimension_list` | `external_interview_assessment_dimension\[\]` | 否 | 评价维度列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `score` | `int` | 否 | 打分题分数（当维度类型为「打分题」时使用）<br>**示例值**：99 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `string` | 否 | 单选选项（当维度类型为「单选题」时使用）<br>**示例值**："选项1" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `string\[\]` | 否 | 多选选项（当维度类型为「多选题」时使用）<br>**示例值**：["选项1"] |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 否 | 描述内容（当维度类型为「描述题」时使用）<br>**示例值**："测试内容" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assessment_type` | `int` | 否 | 维度类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 打分题 - `2`: 单选题 - `3`: 描述题 - `4`: 多选题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 维度标题<br>**示例值**："心理测试" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 否 | 维度描述<br>**示例值**："心理测试描述" |
| &nbsp;&nbsp;└ `content` | `string` | 否 | 综合评价<br>**示例值**："面试内容结果补充" |


### 请求体示例

```json
{
    "external_application_id": "6960663240925956437",
    "participate_status": 1,
    "begin_time": 1618500278638,
    "end_time": 1618500278639,
    "interview_assessments": [
        {
            "username": "张三",
            "conclusion": 1,
            "assessment_dimension_list": [
                {
                    "score": 99,
                    "option": "选项1",
                    "options": [
                        "选项1"
                    ],
                    "content": "测试内容",
                    "assessment_type": 1,
                    "title": "心理测试",
                    "description": "心理测试描述"
                }
            ],
            "content": "面试内容结果补充"
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
| &nbsp;&nbsp;└ `external_interview` | `external_interview` | 外部面试 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `external_application_id` | `string` | 外部投递 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 外部面试 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `participate_status` | `int` | 参与状态<br>**可选值有**：<br>- `1`: 未参与 - `2`: 参与 - `3`: 爽约 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `begin_time` | `int` | 开始时间，毫秒时间戳（字段类型为：int64） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `int` | 结束时间，毫秒时间戳（字段类型为：int64） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_assessments` | `external_interview_assessment\[\]` | 面试评价列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 外部面评 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `username` | `string` | 面试官姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `conclusion` | `int` | 面试结果<br>**可选值有**：<br>- `1`: 不通过 - `2`: 通过 - `3`: 待定 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assessment_dimension_list` | `external_interview_assessment_dimension\[\]` | 评价维度列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `score` | `int` | 打分题分数（当维度类型为「打分题」时使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option` | `string` | 单选选项（当维度类型为「单选题」时使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `string\[\]` | 多选选项（当维度类型为「多选题」时使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 描述内容（当维度类型为「描述题」时使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assessment_type` | `int` | 维度类型<br>**可选值有**：<br>- `1`: 打分题 - `2`: 单选题 - `3`: 描述题 - `4`: 多选题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 维度标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 维度描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 综合评价 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "external_interview": {
            "external_application_id": "6960663240925956437",
            "id": "6960663240925956436",
            "participate_status": 1,
            "begin_time": 1618500278638,
            "end_time": 1618500278639,
            "interview_assessments": [
                {
                    "id": "6989181065243969836",
                    "username": "张三",
                    "conclusion": 1,
                    "assessment_dimension_list": [
                        {
                            "score": 99,
                            "option": "选项1",
                            "options": [
                                "选项1"
                            ],
                            "content": "面试内容结果补充",
                            "assessment_type": 1,
                            "title": "心理测试",
                            "description": "心理测试描述"
                        }
                    ],
                    "content": "面试内容结果补充"
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统异常 | 请根据实际报错信息定位问题或联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


