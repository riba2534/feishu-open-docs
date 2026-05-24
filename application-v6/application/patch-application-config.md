---
title: "更新应用开发配置"
fullPath: "/uAjLw4CM/ukTMukTMukTM/application-v7/application-v7/application-config/patch"
updateTime: "1779344705000"
---

# 更新应用开发配置

通过该接口可更新自建应用的应用的开发配置（通讯录、安全、可见性等），不传入的参数则保持不变，仅针对传入的参数则进行更新。如果应用正在审核中，则无法更新配置


> **Tip**: - 若用 user_access_token 代表某个终端用户操作API，则需确保该用户为应用的所有者、管理员、开发者，否则无法操作成功
> 
> - 若用 tenant_access_token 代表应用操作API，则仅可以操作自身


> **Warning**: - 仅支持更新[开发者后台](https://open.feishu.cn/app)创建的自建应用，不包含通过机器人助手等其他渠道创建的自建应用
> - 免审权限、事件订阅服务器地址、重定向URL、IP白名单、H5可信域名、协议名白名单修改后立即生效，其他应用配置修改后需要[提交发布](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/application-v7/application-v7/application-publish/create)，并审核通过后才会在线上生效。为确保所有配置均能在线上生效，建议修改后提交应用发布。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/application/v7/applications/:app_id/config |
| HTTP Method | PATCH |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `application:application:patch` 修改应用信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 应用的app_id [如何获取应用的 App ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-app-id)<br>**示例值**："cli_a306c5476fb8d00c" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_id_type` | `string` | 否 | 部门id 类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 以open_department_id标识部门 - `department_id`: 以department_id标识部门<br>**默认值**：`open_department_id` |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `scope` | `app_config_scope` | 否 | 权限配置[API 权限列表](https://open.larkoffice.com/document/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list) |
| &nbsp;&nbsp;└ `add_scopes` | `app_config_scope_item\[\]` | 否 | 新增权限<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scope_name` | `string` | 是 | 权限名称<br>**示例值**："im:message" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `token_type` | `string` | 是 | 身份类型<br>**示例值**："tenant"<br>**可选值有**：<br>- `user`: 以用户身份申请, 调用API时使用user_access_token - `tenant`: 以应用身份申请, 调用API时使用tenant_access_token |
| &nbsp;&nbsp;└ `remove_scopes` | `app_config_scope_item\[\]` | 否 | 删除权限<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scope_name` | `string` | 是 | 权限名称<br>**示例值**："im:message" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `token_type` | `string` | 是 | 身份类型<br>**示例值**："tenant"<br>**可选值有**：<br>- `user`: 以用户身份申请, 调用API时使用user_access_token - `tenant`: 以应用身份申请, 调用API时使用tenant_access_token |
| `event` | `app_config_event` | 否 | 事件配置 |
| &nbsp;&nbsp;└ `subscription_type` | `string` | 是 | 订阅方式<br>**示例值**："webhook"<br>**可选值有**：<br>- `webhook`: 将事件发送至开发者服务器 - `websocket`: 将事件发送至websocket长链接 |
| &nbsp;&nbsp;└ `request_url` | `string` | 否 | 接收事件的服务器地址，当subscription_type为webhook需要填写<br>**示例值**："https://open.feishu.cn/" |
| &nbsp;&nbsp;└ `add_events` | `string\[\]` | 否 | 添加事件列表<br>**示例值**：["im.chat.updated_v1"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` |
| &nbsp;&nbsp;└ `remove_events` | `string\[\]` | 否 | 删除事件列表<br>**示例值**：["im.chat.updated_v1"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` |
| `security` | `app_config_security` | 否 | 安全配置 |
| &nbsp;&nbsp;└ `add` | `app_config_security_item` | 否 | 新增项 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `redirect_urls` | `string\[\]` | 否 | 重定向URL<br>**示例值**：["https://open.feishu.com/"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allowed_ips` | `string\[\]` | 否 | IP白名单 IP需要填写调用方出口公网IP地址<br>**示例值**：["114.251.196.102"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `h5_trusted_domains` | `string\[\]` | 否 | H5可信域名仅可信域名内的 H5 可以访问 JSAPI，部分需要鉴权的 JSAPI 必填。<br>**示例值**：["https://open.feishu.com"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `web_view_trusted_domains` | `string\[\]` | 否 | Web-View 可信域名<br>**示例值**：["https://open.feishu.com"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allowed_schemas` | `string\[\]` | 否 | 小程序协议名白名单<br>**示例值**：["https://applink.feishu.cn"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allowed_server_domains` | `string\[\]` | 否 | 服务器可信域名<br>**示例值**：["https://open.feishu.com"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;└ `remove` | `app_config_security_item` | 否 | 删除列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `redirect_urls` | `string\[\]` | 否 | 重定向URL<br>**示例值**：["https://open.feishu.com/"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allowed_ips` | `string\[\]` | 否 | IP白名单 IP需要填写调用方出口公网IP地址<br>**示例值**：["114.251.196.102"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `h5_trusted_domains` | `string\[\]` | 否 | H5可信域名仅可信域名内的 H5 可以访问 JSAPI，部分需要鉴权的 JSAPI 必填。<br>**示例值**：["https://open.feishu.com"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `web_view_trusted_domains` | `string\[\]` | 否 | Web-View 可信域名<br>**示例值**：["https://open.feishu.com"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allowed_schemas` | `string\[\]` | 否 | 小程序协议名白名单<br>**示例值**：["https://applink.feishu.cn"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allowed_server_domains` | `string\[\]` | 否 | 服务器可信域名<br>**示例值**：["https://open.feishu.com"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `300` |
| &nbsp;&nbsp;└ `allow_refresh_token` | `boolean` | 否 | 是否允许刷新 user_access_token<br>**示例值**：false |
| `visibility` | `app_config_visibility` | 否 | 可见性范围配置 |
| &nbsp;&nbsp;└ `is_visible_to_all` | `boolean` | 是 | 是否全员可见,false:否;true:是;不填:继续当前状态不改变.如果可见范围为全员后添加的可用人员则无效,禁用人员仍然有效<br>**示例值**：false |
| &nbsp;&nbsp;└ `visible_list` | `app_visibility_id_list` | 否 | 可用人员列表，当is_visible_to_all为true时，visible_list中的参数无效 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_ids` | `string\[\]` | 否 | 成员id列表(open_id/union_id/user_id)<br>**示例值**：["ou_84aad35d084aa403a838cf73ee18467"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 否 | 部门id列表(自定义部门id/open_department_id)<br>**示例值**：["od-4e6ac4d14bcd5071a37a39de902c7141"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` |
| `contacts` | `app_config_contacts_range` | 否 | 通讯录权限范围配置 |
| &nbsp;&nbsp;└ `contacts_range_type` | `string` | 是 | 更新范围方式<br>**示例值**："some"<br>**可选值有**：<br>- `equal_to_availability`: 和可见性保持一致 - `some`: 部分成员 - `all`: 全部成员范围 |
| &nbsp;&nbsp;└ `visible_list` | `app_contacts_range_id_list` | 否 | 通讯录可用人员列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_ids` | `string\[\]` | 否 | 成员id列表<br>**示例值**：["ou_7dab8a3d3cdcc9da365777c7ad535d62"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 否 | 部门id列表<br>**示例值**：["od-4e6ac4d14bcd5071a37a39de902c7141"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` |
| `event_and_callback_encrypt_strategy` | `event_and_callback_encrypt_strategy` | 否 | 事件与回调加密策略 |
| &nbsp;&nbsp;└ `encryption_key` | `string` | 否 | 加密key, 配置 Encrypt Key 后，开放平台将向请求地址推送加密后的事件<br>**示例值**："xE4k2SkQgtbC8jZEviGRxxxxxxxx"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `32` 字符 |
| &nbsp;&nbsp;└ `verification_token` | `string` | 否 | 开放平台向应用推送的事件中都带有此 Token，应用可以据此 Token 验证推送的事件是否属于该应用。<br>**示例值**："lVEjWtBAu6kVIgSLMV3C4fxxxx"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `32` 字符 |
| `callback` | `app_config_callback` | 否 | 回调配置 |
| &nbsp;&nbsp;└ `callback_type` | `string` | 是 | 回调类型<br>**示例值**："webhook"<br>**可选值有**：<br>- `webhook`: webhook - `websocket`: websocket |
| &nbsp;&nbsp;└ `request_url` | `string` | 否 | 如果回调是 webhook，webhook 的请求地址<br>**示例值**："https://open.feishu.cn/callback" |
| &nbsp;&nbsp;└ `add_callbacks` | `string\[\]` | 否 | 添加哪些回调<br>**示例值**：["url.preview.get"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `50` |
| &nbsp;&nbsp;└ `remove_callbacks` | `string\[\]` | 否 | 移除哪些回调<br>**示例值**：["url.preview.get"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `50` |


### 请求体示例

```json
{
    "scope": {
        "add_scopes": [
            {
                "scope_name": "im:message",
                "token_type": "tenant"
            }
        ],
        "remove_scopes": [
            {
                "scope_name": "im:message",
                "token_type": "tenant"
            }
        ]
    },
    "event": {
        "subscription_type": "webhook",
        "request_url": "https://open.feishu.cn/",
        "add_events": [
            "im.chat.updated_v1"
        ],
        "remove_events": [
            "im.chat.updated_v1"
        ]
    },
    "security": {
        "add": {
            "redirect_urls": [
                "https://open.feishu.com/"
            ],
            "allowed_ips": [
                "114.251.196.102"
            ],
            "h5_trusted_domains": [
                "https://open.feishu.com"
            ],
            "web_view_trusted_domains": [
                "https://open.feishu.com"
            ],
            "allowed_schemas": [
                "https://applink.feishu.cn"
            ],
            "allowed_server_domains": [
                "https://open.feishu.com"
            ]
        },
        "remove": {
            "redirect_urls": [
                "https://open.feishu.com/"
            ],
            "allowed_ips": [
                "114.251.196.102"
            ],
            "h5_trusted_domains": [
                "https://open.feishu.com"
            ],
            "web_view_trusted_domains": [
                "https://open.feishu.com"
            ],
            "allowed_schemas": [
                "https://applink.feishu.cn"
            ],
            "allowed_server_domains": [
                "https://open.feishu.com"
            ]
        },
        "allow_refresh_token": false
    },
    "visibility": {
        "is_visible_to_all": false,
        "visible_list": {
            "user_ids": [
                "ou_84aad35d084aa403a838cf73ee18467"
            ],
            "department_ids": [
                "od-4e6ac4d14bcd5071a37a39de902c7141"
            ]
        }
    },
    "contacts": {
        "contacts_range_type": "some",
        "visible_list": {
            "user_ids": [
                "ou_7dab8a3d3cdcc9da365777c7ad535d62"
            ],
            "department_ids": [
                "od-4e6ac4d14bcd5071a37a39de902c7141"
            ]
        }
    },
    "event_and_callback_encrypt_strategy": {
        "encryption_key": "xE4k2SkQgtbC8jZEviGRxxxxxxxx",
        "verification_token": "lVEjWtBAu6kVIgSLMV3C4fxxxx"
    },
    "callback": {
        "callback_type": "webhook",
        "request_url": "https://open.feishu.cn/callback",
        "add_callbacks": [
            "url.preview.get"
        ],
        "remove_callbacks": [
            "url.preview.get"
        ]
    }
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 210031 | Param is invalid | 根据错误提示信息，检查参数是否符合要求 |
| 404 | 210032 | The specified application does not exist | 指定的应用不存在，请检查传入的app_id参数是否正确 |
| 500 | 210033 | Internal server error | 服务内部错误，请稍候重试或联系技术支持(https://applink.feishu.cn/TLJpeNdW) |
| 400 | 210034 | This API only does not support to update ISV App, only support to update Self-Built App | 仅支持更新自建应用，请检查更新的应用是否为自建应用 |
| 403 | 210035 | As the app was created via Base, it cannot be updated using this API. | 仅可以操作开发者后台创建的应用，请使用开发者后台创建的应用调用该API |
| 403 | 210036 | Lack of permission to update other app. | 应用身份调用仅允许更新自身，不允许更新其它应用，请使用应用自身的身份调用该API |
| 403 | 210037 | The current user has no permission to modify the app configurations | 用户无权限操作，用户需要是应用所有者 或者是应用的管理员以及开发者 |
| 403 | 210040 | Unable to update configurations, as the app is currently under review. | 应用正在审核中，不能进行该操作，请等待审核通过后再尝试 |
| 400 | 210041 | The scope that parameter indicated needs robot ability to be enable first. | 需要先开启机器人能力，请在应用配置中开启机器人能力后再调用该 API |
| 400 | 210042 | The validation for event.request_url failed. | 事件回调地址验证失败，请按照文档配置正确的 request_url：[将回调发送至开发者服务器](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/event-subscription-guide/callback-subscription/step-1-choose-a-subscription-mode/send-callbacks-to-developers-server) |
| 403 | 210043 | The specified application is not created via developer platform, can not modify by this API | 仅可以操作开发者后台创建的应用，请使用开发者后台创建的应用调用该API |


