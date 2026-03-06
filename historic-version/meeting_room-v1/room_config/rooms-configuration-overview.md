---
title: "会议室配置概述"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/room_config/rooms-configuration-overview"
updateTime: "1639995191000"
---

#  会议室配置概述
##  资源定义
会议室配置用于对飞书会议室的背景设置、资源管理等进行配置，包括：[查询会议室配置](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/room_config/query)、[设置会议室配置](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/room_config/set)。

##  字段说明

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `scope` | `int` | 查询节点范围 **示例值**："5"            **可选值有**： - `1`：租户 - `2`：国家/地区 - `3`：城市 - `4`：建筑 - `5`：楼层 - `6`：会议室 |
| `country_id` | `string` | 国家/地区ID scope为2，3时需要此参数 **示例值**："086" |
| `district_id` | `string` | 城市ID scope为3时需要此参数 **示例值**："001" |
| `building_id` | `string` | 建筑ID scope为4，5时需要此参数 **示例值**："22" |
| `floor_name` | `string` | 楼层 scope为5时需要此参数 **示例值**："4" |
| `room_id` | `string` | 会议室ID scope为6时需要此参数 **示例值**："6383786266263" |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `room_config` | `-` |
| ∟ `room_background` | `string` | 飞书会议室背景图 |
| ∟ `display_background` | `string` | 飞书签到板背景图 |
| ∟ `digital_signage` | `room_digital_signage` | 飞书会议室数字标牌 |
| ∟ `enable` | `boolean` | 是否开启数字标牌功能 |
| ∟ `mute` | `boolean` | 是否静音播放 |
| ∟ `start_display` | `int` | 日程会议开始前n分钟结束播放 |
| ∟ `stop_display` | `int` | 会议结束后n分钟开始播放 |
| ∟ `materials` | `room_digital_signage_material[]` | 素材列表 |
| ∟ `id` | `string` | 素材ID |
| ∟ `name` | `string` | 素材名称 |
| ∟ `material_type` | `int` | 素材类型            **可选值有**： - `1`：图片 - `2`：视频 - `3`：GIF |
| ∟ `url` | `string` | 素材url |
| ∟ `duration` | `int` | 播放时长（单位sec） |
| ∟ `cover` | `string` | 素材封面url |
| ∟ `md5` | `string` | 素材文件md5 |

###  数据示例
```json
{
    "scope":5,
    "country_id":"086",
    "district_id":"001",
    "building_id":"22",
    "floor_name":"4",
    "room_id":"6383786266263",
    "code":0,
    "msg":"success",
    "data": {
        "room_background": "https://lf1-ttcdn-tos.pstatp.com/obj/xxx",
        "display_background": "https://lf1-ttcdn-tos.pstatp.com/obj/xxx",
        "digital_signage": {
            "enable": true,
            "mute": true,
            "start_display": 3,
            "stop_display": 3,
            "materials": [
                {
                    "id": "7847784676276",
                    "name": "name",
                    "material_type": 0,
                    "url": "url",
                    "duration": 15,
                    "cover": "url",
                    "md5": "md5"
                }
            ]
        }
    }
}
```