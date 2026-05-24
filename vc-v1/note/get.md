---
title: "获取纪要详情"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/note/get"
updateTime: "1774580763000"
---

# 获取纪要详情

获取一篇纪要的详细数据。


> **Warning**: 只能获取自己可见纪要文档，以及相关联的产物、关联引用信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/vc/v1/notes/:note_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `vc:note:read` 获取智能纪要 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `note_id` | `string` | 纪要ID<br>**示例值**："6943848821689040898" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `note` | `note` | 纪要信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator_id` | `string` | 纪要创建者 User ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 纪要创建时间（unix时间，单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `artifacts` | `note_artifact_info\[\]` | 纪要产物 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `artifact_type` | `int` | 纪要产物类型<br>**可选值有**：<br>- `0`: 保留值（正常业务流程中服务端不会返回） - `1`: 纪要文档 - `2`: 逐字稿文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 产物创建时间（unix时间，单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `doc_token` | `string` | 产物的doc token |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `references` | `note_reference_info\[\]` | 关联引用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reference_type` | `int` | 关联引用类型<br>**可选值有**：<br>- `0`: 保留值（正常业务流程中服务端不会返回） - `1`: 会中共享文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `doc_token` | `string` | 关联引用的doc token |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "note": {
            "creator_id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b",
            "create_time": "1773922587",
            "artifacts": [
                {
                    "artifact_type": 1,
                    "create_time": "1773922587",
                    "doc_token": "BkX1wpU0gi6WP4klwRGchoqZntv"
                }
            ],
            "references": [
                {
                    "reference_type": 1,
                    "doc_token": "fqF1wpU0gi6WP4klwRGchoqqweA"
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 121001 | internal error | 服务器内部错误，如果重试无效可联系管理员 |
| 400 | 121002 | not support | 暂不支持该功能 |
| 400 | 121003 | param error | 传入参数校验错误，检查参数传入格式 |
| 404 | 121004 | data not exist | 请求的数据不存在，请检查传入的ID是否正确或是否存在该数据 |
| 403 | 121005 | no permission | 无权限进行该操作，建议检查操作者身份以及纪要的可见性 |


