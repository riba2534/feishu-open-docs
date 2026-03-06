---
title: "查询复盘信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/review/query"
updateTime: "1712650627000"
---

# 查询复盘信息

根据周期和用户查询复盘信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/okr/v1/reviews/query |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `okr:okr:readonly` 获取 OKR 信息 `okr:okr` 更新 OKR 信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_admin_id`: 以people_admin_id来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `user_ids` | `string\[\]` | 是 | 目标用户id列表，最多5个<br>**示例值**：ou-asdasdasdasdasd<br>**数据校验规则**：<br>- 最大长度：`5` |
| `period_ids` | `string\[\]` | 是 | period_id列表，最多5个<br>**示例值**：6951461264858777132<br>**数据校验规则**：<br>- 最大长度：`5` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `review_list` | `okr_review\[\]` | OKR复盘 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `okr_objective_aligned_objective_owner` | 复盘的用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user_id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `review_period_list` | `okr_review_period\[\]` | 用户对应的OKR复盘列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `period_id` | `string` | 周期ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cycle_review_list` | `okr_review_period_url\[\]` | 复盘文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 文档链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间 毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `progress_report_list` | `okr_review_period_url\[\]` | 进展报告 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 文档链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建时间 毫秒 |


### 响应体示例

```json
{
    "code": 0,
    "data": {
        "review_list": [
            {
                "review_period_list": [
                    {
                        "cycle_review_list": [
                            {
                                "create_time": "1646902033525",
                                "url": "https://okr-boe1.feishu-boe.cn/docs/docbcZ4PTuEDd2MBJ9k2W4rOeY1"
                            }
                        ],
                        "period_id": "7067724095781142548",
                        "progress_report_list": [
                            {
                                "create_time": "1646904637251",
                                "url": "https://okr-boe1.feishu-boe.cn/docs/docbcthFL8qo5ENgYW5k3iTLZWf"
                            },
                            {
                                "create_time": "1646902091512",
                                "url": "https://okr-boe1.feishu-boe.cn/docs/docbcRS2NbVRcPfm77W9H4031qb"
                            }
                        ]
                    }
                ],
                "user_id": {
                    "open_id": "ou_e6139117c300506837def50545420c6a",
                    "user_id": "6969855501744834092"
                }
            }
        ]
    },
    "msg": "success"
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1009999 | Unknown error. Please contact Feishu Assistant or your customer success manager. | 内部错误，请联系飞书助手或您的客户成功经理 |
| 500 | 1009998 | system exception | 系统异常 |
| 400 | 1001001 | Invalid parameters. Please check document and modify accordingly. | 无效的参数，请对照文档检查输入的参数 |
| 400 | 1001002 | No permission. | 您无权访问该接口，请确认您的登录凭证 |
| 400 | 1001003 | User not found. | 用户不存在 |
| 400 | 1001004 | OKR data not found. | 对应ID的数据不存在 |


