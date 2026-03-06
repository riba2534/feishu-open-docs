---
title: "资源介绍"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/meeting-overview"
updateTime: "1679916444000"
---

#  资源介绍
##  资源定义
用户可以在会议中进行邀请参会成员、移除参会成员和设置主持人等操作。其中，方法包括：[获取会议详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/get)、[获取与会议号相关联的会议列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/list_by_no)、[邀请参会人](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/invite)、[移除参会人](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/kickout)、[设置主持人](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/set_host)、[结束会议](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/end)。事件包括：[会议开始](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/meeting_started)、[会议结束](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/meeting_ended)、[加入会议](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/join_meeting)、[离开会议](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/leave_meeting)、[录制开始](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/recording_started)、[录制停止](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/recording_ended)、[录制完成](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/recording_ready)、[屏幕共享开始](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/share_started)、[屏幕共享结束](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/share_ended)。

##  字段说明

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `data` | `-` | `-` |
| ∟ `meeting` | `meeting` | 会议数据 |
| ∟ `id` | `string` | 会议ID（视频会议的唯一标识，视频会议开始后才会产生） |
| ∟ `topic` | `string` | 会议主题 |
| ∟ `url` | `string` | 会议链接（飞书用户可通过点击会议链接快捷入会） |
| ∟ `create_time` | `string` | 会议创建时间（unix时间，单位sec） |
| ∟ `start_time` | `string` | 会议开始时间（unix时间，单位sec） |
| ∟ `end_time` | `string` | 会议结束时间（unix时间，单位sec） |
| ∟ `host_user` | `meeting_user` | 主持人 |
| ∟ `id` | `string` | 用户 ID |
| ∟ `user_type` | `int` | 用户类型            **可选值有**： - `1`：lark用户 - `2`：rooms用户 - `3`：文档用户 - `4`：neo单品用户 - `5`：neo单品游客用户 - `6`：pstn用户 - `7`：sip用户 |
| ∟ `status` | `int` | 会议状态            **可选值有**： - `1`：会议呼叫中 - `2`：会议进行中 - `3`：会议已结束 |
| ∟ `participant_count` | `string` | 参会人数 |
| ∟ `participants` | `meeting_participant[]` | 参会人列表 |
| ∟ `id` | `string` | 用户ID |
| ∟ `user_type` | `int` | 用户类型            **可选值有**： - `1`：lark用户 - `2`：rooms用户 - `3`：文档用户 - `4`：neo单品用户 - `5`：neo单品游客用户 - `6`：pstn用户 - `7`：sip用户 |
| ∟ `is_host` | `boolean` | 是否为主持人 |
| ∟ `is_cohost` | `boolean` | 是否为联席主持人 |
| ∟ `is_external` | `boolean` | 是否为外部参会人 |
| ∟ `status` | `int` | 参会人状态            **可选值有**： - `1`：呼叫中 - `2`：在会中 - `3`：正在响铃 - `4`：不在会中或已经离开会议 |
| ∟ `ability` | `meeting_ability` | 会中使用的能力 |
| ∟ ` use_video` | `boolean` | 是否使用视频 |
| ∟ `use_audio` | `boolean` | 是否使用音频 |
| ∟ `use_share_screen` | `boolean` | 是否使用共享屏幕 |
| ∟ `use_follow_screen` | `boolean` | 是否使用妙享（magic share） |
| ∟ `use_recording` | `boolean` | 是否使用录制 |
| ∟ `use_pstn` | `boolean` | 是否使用PSTN |

###  数据示例
```json
{
    "data": {
        "meeting": {
            "id": "6911188411934433028",
            "topic": "my meeting",
            "url": "https://vc.feishu.cn/j/337736498",
            "create_time": "1608885566",
            "start_time": "1608883322",
            "end_time": "1608888867",
            "host_user": {
                "id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b",
                "user_type": 1
            },
            "status": 2,
            "participant_count": "10",
            "participants": [
                {
                    "id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b",
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
