---
title: "获取活跃会议"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/reserve/get_active_meeting"
updateTime: "1725888875000"
---

# 获取活跃会议

获取一个预约的当前活跃会议。


> **Warning**: 只能获取归属于自己的预约的活跃会议（一个预约最多有一个正在进行中的会议）


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/vc/v1/reserves/:reserve_id/get_active_meeting |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `vc:reserve:readonly` 获取会议预约信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `reserve_id` | `string` | 预约ID（预约的唯一标识）<br>**示例值**："6911188411932033028" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `with_participants` | `boolean` | 否 | 是否需要参会人列表，默认为false<br>**示例值**：false |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `meeting` | `meeting` | 会议数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 会议ID（视频会议的唯一标识，视频会议开始后才会产生） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `topic` | `string` | 会议主题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 会议链接（飞书用户可通过点击会议链接快捷入会） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_no` | `string` | 会议号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `password` | `string` | 会议密码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 会议创建时间（unix时间，单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 会议开始时间（unix时间，单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 会议结束时间（unix时间，单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `host_user` | `meeting_user` | 主持人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_type` | `int` | 用户类型<br>**可选值有**：<br>- `1`: 飞书用户 - `2`: rooms用户 - `3`: 文档用户 - `4`: neo单品用户 - `5`: neo单品游客用户 - `6`: pstn用户 - `7`: sip用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_connect` | `boolean` | 该会议是否支持互通（注：该字段内测中） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 会议状态<br>**可选值有**：<br>- `1`: 会议呼叫中 - `2`: 会议进行中 - `3`: 会议已结束 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `participant_count` | `string` | 参会峰值人数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `participant_count_accumulated` | `string` | 累计参会人数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `participants` | `meeting_participant\[\]` | 参会人列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `first_join_time` | `string` | 首次入会时间，秒级Unix时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `final_leave_time` | `string` | 最终离会时间，秒级Unix时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `in_meeting_duration` | `string` | 累计在会中时间，时间单位：秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_type` | `int` | 用户类型<br>**可选值有**：<br>- `1`: 飞书用户 - `2`: rooms用户 - `3`: 文档用户 - `4`: neo单品用户 - `5`: neo单品游客用户 - `6`: pstn用户 - `7`: sip用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_host` | `boolean` | 是否为主持人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_cohost` | `boolean` | 是否为联席主持人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_external` | `boolean` | 是否为外部参会人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 参会人状态<br>**可选值有**：<br>- `1`: 呼叫中 - `2`: 在会中 - `3`: 正在响铃 - `4`: 不在会中或已经离开会议 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ability` | `meeting_ability` | 会中使用的能力 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_video` | `boolean` | 是否使用视频 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_audio` | `boolean` | 是否使用音频 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_share_screen` | `boolean` | 是否使用共享屏幕 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_follow_screen` | `boolean` | 是否使用妙享（magic share） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_recording` | `boolean` | 是否使用录制 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_pstn` | `boolean` | 是否使用PSTN |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "meeting": {
            "id": "6911188411934433028",
            "topic": "my meeting",
            "url": "https://vc.feishu.cn/j/337736498",
            "meeting_no": "123456789",
            "password": "971024",
            "create_time": "1608885566",
            "start_time": "1608883322",
            "end_time": "1608888867",
            "host_user": {
                "id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b",
                "user_type": 1
            },
            "meeting_connect": true,
            "status": 2,
            "participant_count": "10",
            "participant_count_accumulated": "10",
            "participants": [
                {
                    "id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b",
                    "first_join_time": "1624438144",
                    "final_leave_time": "1624438144",
                    "in_meeting_duration": "123",
                    "user_type": 1,
                    "is_host": true,
                    "is_cohost": false,
                    "is_external": false,
                    "status": 2
                }
            ],
            "ability": {
                "use_video": true,
                "use_audio": true,
                "use_share_screen": true,
                "use_follow_screen": true,
                "use_recording": true,
                "use_pstn": true
            }
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 121001 | internal error | 服务器内部错误，如果重试无效可联系管理员 |
| 400 | 121002 | not support | 暂不支持该功能 |
| 400 | 121003 | param error | 参数错误，检查参数的取值范围（请按照上面字段说明自查） |
| 404 | 121004 | data not exist | 请求的数据不存在 |
| 403 | 121005 | no permission | 无权限进行该操作，建议检查token类型、操作者身份以及资源的归属 |


