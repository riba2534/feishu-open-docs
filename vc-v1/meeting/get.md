---
title: "获取会议详情"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/get"
updateTime: "1774528229000"
---

# 获取会议详情

根据会议 ID 获取指定会议的详细信息，包括会议主题、链接、主持人、参会人员、状态、时间信息及关联纪要 ID。


> **Warning**: 只能获取归属于自己的会议，支持查询最近90天内的会议


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/vc/v1/meetings/:meeting_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `vc:meeting.meetingevent:read` 获取会议信息 `vc:meeting:readonly` 获取会议信息 |
| 字段权限要求 | &gt; **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID `vc:meeting.artifact.note:read` 获取智能纪要信息 `vc:meeting.artifact.verbatim:read` 获取逐字稿信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `meeting_id` | `string` | 会议ID（视频会议的唯一标识，视频会议开始后才会产生）可通过调用[获取与会议号关联的会议列表](https://open.larkoffice.com/document/server-docs/vc-v1/meeting/list_by_no)获取<br>**示例值**："6911188411932033028" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `with_participants` | `boolean` | 否 | 是否返回参会人列表，默认值为 false，不返回参会人列表；设为 true 时返回参会人列表。当 user_id_type 为 user_id 时，参会人列表仅能获取 Lark 用户。<br>**示例值**：false |
| `with_meeting_ability` | `boolean` | 否 | 是否返回会中使用能力统计，默认值为 false，不返回能力统计；设为 true 时返回会中使用能力统计（仅限tenant_access_token）<br>**示例值**：false |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `query_mode` | `int` | 否 | 此次查询的查询模式，不传，或传0，只查询会议信息；传1，只查询会议产物<br>**示例值**：0<br>**可选值有**：<br>- `0`: 只查询会议信息（默认） - `1`: 只查询会议产物（纪要、逐字稿） |


注意：使用user_id作为user_id_type时，参会人列表中仅能获取lark用户，rooms/pstn/sip等用户将被过滤。如需获取此类用户，请使用open_id


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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_connect` | `boolean` | 该会议是否支持互通 |
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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ability` | `meeting_ability` | 会中使用的能力<br>**注意**：仅当使用应用身份（tenant_access_token）调用该接口，且查询参数 with_meeting_ability 取值为 true 时，该参数会有返回值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_video` | `boolean` | 是否使用视频 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_audio` | `boolean` | 是否使用音频 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_share_screen` | `boolean` | 是否使用共享屏幕 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_follow_screen` | `boolean` | 是否使用妙享（magic share） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_recording` | `boolean` | 是否使用录制 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `use_pstn` | `boolean` | 是否使用PSTN |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `note_id` | `string` | 纪要ID |
| &nbsp;&nbsp;└ `related_artifacts` | `meeting_related_artifacts` | 会议产物相关信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `note_doc_token` | `string` | 智能纪要的 doc_token - 文档一旦生成，就可以查到对应 token - 无字段权限时，该 key 不会出现在 related_artifacts 结构当中 - 有字段权限而无内容时，related_artifacts 结构中会包含该 key，同时其值为空字符串<br>**字段权限要求**： `vc:meeting.artifact.note:read` 获取智能纪要信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `verbatim_doc_token` | `string` | 逐字稿的 doc_token - 文档一旦生成，就可以查到对应 token - 无字段权限时，该 key 不会出现在 related_artifacts 结构当中 - 有字段权限而无内容时，related_artifacts 结构中会包含该 key，同时其值为空字符串<br>**字段权限要求**： `vc:meeting.artifact.verbatim:read` 获取逐字稿信息 |


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
| 500 | 121001 | internal error | 服务器内部错误，如果重试无效可联系[技术支持](https://applink.larkoffice.com/TLJpeNdW) |
| 400 | 121002 | not support | 暂不支持该功能，有疑问可联系[技术支持](https://applink.larkoffice.com/TLJpeNdW) |
| 400 | 121003 | param error | 参数错误，检查参数的取值范围（请按照上面字段说明自查） |
| 404 | 121004 | data not exist | 请求的数据不存在，请确保传入了正确的会议ID（meeting_id），如何获取会议ID，可参考[获取与会议号关联的会议列表](https://open.larkoffice.com/document/server-docs/vc-v1/meeting/list_by_no) |
| 403 | 121005 | no permission | 无权限进行该操作，建议检查token类型、操作者身份以及资源的归属 |


