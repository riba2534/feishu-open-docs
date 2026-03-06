---
title: "获取系统状态"
fullPath: "/uAjLw4CM/ukTMukTMukTM/personal_settings-v1/system_status/list"
updateTime: "1689134249000"
---

# 获取系统状态

获取租户下所有系统状态。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/personal_settings/v1/system_statuses |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `personal_settings:status:system_status_update` 获取与更新系统状态 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：50<br>**默认值**：`50`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `50` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：GxmvlNRvP0NdQZpa7yIqf_Lv_QuBwTQ8tXkX7w-irAghVD_TvuYd1aoJ1LQph86O-XImC4X9j9FhUPhXQDvtrQ== |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `system_status\[\]` | 租户系统状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `system_status_id` | `string` | 系统状态ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 系统状态名称，名称字符数要在1到20范围内。不同系统状态的title不能重复。<br> **注意：**  - 1中文=2英文=2其他语言字符=2字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_title` | `system_status_i18n_name` | 系统状态国际化名称，名称字符数要在1到20范围内。不同系统状态之间i18n_title中任何一种title都不能重复。<br> **注意：**  - 1中文=2英文=2其他语言字符=2字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `icon_key` | `string` | 图标<br>[**了解icon_key可选值**](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/personal_settings-v1/system_status/overview)<br>**可选值有**：<br>- `GeneralDoNotDisturb`: GeneralDoNotDisturb - `GeneralInMeetingBusy`: GeneralInMeetingBusy - `Coffee`: Coffee - `GeneralBusinessTrip`: GeneralBusinessTrip - `GeneralWorkFromHome`: GeneralWorkFromHome - `StatusEnjoyLife`: StatusEnjoyLife - `GeneralTravellingCar`: GeneralTravellingCar - `StatusBus`: StatusBus - `StatusInFlight`: StatusInFlight - `Typing`: Typing - `EatingFood`: EatingFood - `SICK`: SICK - `GeneralSun`: GeneralSun - `GeneralMoonRest`: GeneralMoonRest - `StatusReading`: StatusReading - `Status_PrivateMessage`: Status_PrivateMessage - `StatusFlashOfInspiration`: StatusFlashOfInspiration - `GeneralVacation`: GeneralVacation |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `color` | `string` | 颜色<br>**可选值有**：<br>- `BLUE`: 蓝色 - `GRAY`: 灰色 - `INDIGO`: 靛青色 - `WATHET`: 浅蓝色 - `GREEN`: 绿色 - `TURQUOISE`: 绿松石色 - `YELLOW`: 黄色 - `LIME`: 酸橙色 - `RED`: 红色 - `ORANGE`: 橙色 - `PURPLE`: 紫色 - `VIOLET`: 紫罗兰色 - `CARMINE`: 胭脂红色 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `priority` | `int` | 优先级，数值越小，客户端展示的优先级越高。不同系统状态的优先级不能一样。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sync_setting` | `system_status_sync_setting` | 同步设置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_open_by_default` | `boolean` | 是否默认开启 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 同步设置名称，名称字符数要在1到30范围内。<br>**注意：**  - 1中文=2英文=2其他语言字符=2字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_title` | `system_status_sync_i18n_name` | 同步设置国际化名称，名称字符数要在1到30范围内。<br>**注意：**  - 1中文=2英文=2其他语言字符=2字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `explain` | `string` | 同步设置解释文案，解释字符数要在1到60范围内。<br>**注意：**  - 1中文=2英文=2其他语言字符=2字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_explain` | `system_status_sync_i18n_explain` | 同步设置国际化解释文案，解释字符数要在1到60范围内。<br>**注意：**  - 1中文=2英文=2其他语言字符=2字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "system_status_id": "7101214603622940633",
                "title": "出差",
                "i18n_title": {
                    "zh_cn": "出差",
                    "en_us": "On business trip",
                    "ja_jp": "出張中"
                },
                "icon_key": "GeneralBusinessTrip",
                "color": "BLUE",
                "priority": 1,
                "sync_setting": {
                    "is_open_by_default": true,
                    "title": "出差期间自动开启",
                    "i18n_title": {
                        "zh_cn": "出差期间自动开启",
                        "en_us": "Auto display Business Trip",
                        "ja_jp": "出張中に自動的にオンにする"
                    },
                    "explain": "出差审批通过后，将自动开启并优先展示该状态。",
                    "i18n_explain": {
                        "zh_cn": "出差审批通过后，该状态将自动开启并优先展示",
                        "en_us": "Auto-display after travel request is approved.",
                        "ja_jp": "申請が承認されると、このステータスが優先的に表示されます"
                    }
                }
            }
        ],
        "page_token": "GxmvlNRvP0NdQZpa7yIqf_Lv_QuBwTQ8tXkX7w-irAghVD_TvuYd1aoJ1LQph86O-XImC4X9j9FhUPhXQDvtrQ==",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2005001 | Your request contains an invalid request parameter. | 参数错误，请根据接口返回的错误信息并参考文档检查输入参数。 |
| 400 | 2005007 | Tenant does not have permission to api. | 租户没有访问api权限。 |


