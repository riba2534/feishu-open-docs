---
title: "获取预约"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/reserve/get"
updateTime: "1725888875000"
---

# 获取预约

获取一个预约的详情。


> **Warning**: 只能获取归属于自己的预约


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/vc/v1/reserves/:reserve_id |
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
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `reserve` | `reserve` | 预约数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 预约ID（预约的唯一标识，非会议ID，会议ID仅在会议开始后才生成） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_no` | `string` | 9位会议号（飞书用户可通过输入9位会议号快捷入会） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `password` | `string` | 会议密码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 会议链接（飞书用户可通过点击会议链接快捷入会） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_link` | `string` | APPLink用于唤起飞书APP入会。"{?}"为占位符，用于配置入会参数，使用时需替换具体值：0表示关闭，1表示打开。preview为入会前的设置页，mic为麦克风，speaker为扬声器，camera为摄像头 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `live_link` | `string` | 会议转直播链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 预约到期时间（unix时间，单位sec） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expire_status` | `int` | 过期状态<br>**可选值有**：<br>- `1`: 未过期 - `2`: 已过期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reserve_user_id` | `string` | 预约人ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_settings` | `reserve_meeting_setting` | 会议设置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `topic` | `string` | 会议主题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `action_permissions` | `reserve_action_permission\[\]` | 会议权限配置列表，如果存在相同的权限配置项则它们之间为"逻辑或"的关系（即 有一个为true则拥有该权限） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `permission` | `int` | 权限项<br>**可选值有**：<br>- `1`: 是否能成为主持人 - `2`: 是否能邀请参会人 - `3`: 是否能加入会议 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `permission_checkers` | `reserve_permission_checker\[\]` | 权限检查器列表，权限检查器之间为"逻辑或"的关系（即 有一个为true则拥有该权限） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `check_field` | `int` | 检查字段类型<br>**可选值有**：<br>- `1`: 用户ID（check_list填入用户ID） - `2`: 用户类型（check_list可选值有  "1"：飞书用户、 "2"：rooms用户、 "6"：pstn用户、 "7"：sip用户） - `3`: 租户ID（check_list填入租户tenant_key） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `check_mode` | `int` | 检查方式<br>**可选值有**：<br>- `1`: 在check_list中为有权限（白名单） - `2`: 不在check_list中为有权限（黑名单） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `check_list` | `string\[\]` | 检查字段列表（根据check_field的类型填入对应内容） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_initial_type` | `int` | 会议初始类型<br>**可选值有**：<br>- `1`: 多人会议 - `2`: 1v1呼叫 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_connect` | `boolean` | 该会议是否支持互通，不支持更新（注：该字段内测中） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `call_setting` | `reserve_call_setting` | 1v1呼叫相关参数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `callee` | `reserve_callee` | 被呼叫的用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_type` | `int` | 用户类型，当前仅支持用户类型6(pstn用户)<br>**可选值有**：<br>- `1`: 飞书用户 - `2`: rooms用户 - `3`: 文档用户 - `4`: neo单品用户 - `5`: neo单品游客用户 - `6`: pstn用户 - `7`: sip用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pstn_sip_info` | `pstn_sip_info` | pstn/sip信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `nickname` | `string` | 给pstn/sip用户设置的临时昵称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `main_address` | `string` | pstn/sip主机号，格式为：[国际冠字]-[电话区号][电话号码]，当前仅支持国内手机及固定电话号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `auto_record` | `boolean` | 使用飞书视频会议时，是否开启自动录制，默认false |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assign_host_list` | `reserve_assign_host\[\]` | 指定主持人列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_type` | `int` | 用户类型，仅支持设置同租户下的 Lark 用户<br>**可选值有**：<br>- `1`: 飞书用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "reserve": {
            "id": "6911188411934973028",
            "meeting_no": "112000358",
            "password": "971024",
            "url": "https://vc.feishu.cn/j/337736498",
            "app_link": "https://applink.feishu.cn/client/videochat/open?source=openplatform&action=join&idtype=reservationid&id={?}&preview={?}&mic={?}&speaker={?}&camera={?}",
            "live_link": "https://meetings.feishu.cn/s/1gub381l4gglv",
            "end_time": "1608883322",
            "expire_status": 0,
            "reserve_user_id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b",
            "meeting_settings": {
                "topic": "my meeting",
                "action_permissions": [
                    {
                        "permission": 1,
                        "permission_checkers": [
                            {
                                "check_field": 1,
                                "check_mode": 1,
                                "check_list": [
                                    "ou_3ec3f6a28a0d08c45d895276e8e5e19b"
                                ]
                            }
                        ]
                    }
                ],
                "meeting_initial_type": 1,
                "meeting_connect": true,
                "call_setting": {
                    "callee": {
                        "id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b",
                        "user_type": 1,
                        "pstn_sip_info": {
                            "nickname": "dodo",
                            "main_address": "+86-02187654321"
                        }
                    }
                },
                "auto_record": true,
                "assign_host_list": [
                    {
                        "user_type": 1,
                        "id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b"
                    }
                ]
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


