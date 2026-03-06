---
title: "获取应用版本列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/application-v6/application-app_version/list"
updateTime: "1739867977000"
---

# 获取应用版本列表

根据 app_id 获取对应应用版本列表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/application/v6/applications/:app_id/app_versions |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `application:application:self_manage` 管理应用自身资源 `application:application.app_version:readonly` 获取应用版本信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 应用的 app_id，需要查询其他应用版本信息时，必须申请[获取应用版本信息](https://open.larkoffice.com/document/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN)权限，仅查询本应用版本信息时，可填入 "me" 或者应用自身 app_id<br>**示例值**："cli_9b445f5258795107" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `lang` | `string` | 是 | 应用信息的语言版本<br>**示例值**：zh_cn<br>**可选值有**：<br>- `zh_cn`: 中文 - `en_us`: 英文 - `ja_jp`: 日文<br>**数据校验规则**：<br>- 最小长度：`1` 字符 |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：10<br>**默认值**：`20`<br>**数据校验规则**：<br>- 取值范围：`1` ～ `50` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：new-e3c5a0627cdf0c2e057da7257b90376a |
| `order` | `int` | 否 | 0：按照时间倒序 1：按照时间正序<br>**示例值**：0<br>**默认值**：`0` |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `application.app_version\[\]` | 应用版本列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_id` | `string` | 应用 id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `version` | `string` | 在开发者后台填入的应用版本号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `version_id` | `string` | 唯一标识应用版本的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_name` | `string` | 应用默认名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 应用头像 url |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 应用默认描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scopes` | `app_scope\[\]` | 应用权限列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `scope` | `string` | 应用权限 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 应用权限的国际化描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `int` | 权限等级描述<br>**可选值有**：<br>- `1`: 普通权限 - `2`: 高级权限 - `3`: 超敏感权限 - `0`: 未知等级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token_types` | `string\[\]` | 返回用户身份类型user、应用身份类型tenant。如果两种类型都支持，则同时返回两个。<br>**可选值有**：<br>- `tenant`: 应用身份类型 - `user`: 用户身份类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `back_home_url` | `string` | 后台主页地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n` | `app_i18n_info\[\]` | 应用的国际化信息列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_key` | `string` | 国际化语言的 key<br>**可选值有**：<br>- `zh_cn`: 中文 - `en_us`: 英文 - `ja_jp`: 日文 - `zh_hk`: 繁体中文(中国香港) - `zh_tw`: 繁体中文(中国台湾) - `id_id`: 印度尼西亚语 - `ms_my`: 马来语 - `de_de`: 德语 - `es_es`: 西班牙语 - `fr_fr`: 法语 - `it_it`: 意大利语 - `pt_br`: 葡萄牙语(巴西) - `vi_vn`: 越南语 - `ru_ru`: 俄语 - `th_th`: 泰语 - `ko_kr`: 韩语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 应用国际化名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 应用国际化描述（副标题） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `help_use` | `string` | 国际化帮助文档链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `common_categories` | `string\[\]` | 应用分类的国际化描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `events` | `string\[\]` | 应用已订阅开放平台事件列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 版本状态<br>**可选值有**：<br>- `0`: 未知状态 - `1`: 审核通过 - `2`: 审核拒绝 - `3`: 审核中 - `4`: 未提交审核 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 版本创建时间（单位：s） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `publish_time` | `string` | 版本发布时间（单位：s） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ability` | `app_ability` | 当前版本下应用开启的能力 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gadget` | `gadget` | 小程序能力 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enable_pc_mode` | `int` | pc 支持的小程序模式，bit 位表示<br>**可选值有**：<br>- `1`: sidebar 模式 - `2`: pc 模式 - `4`: 主导航模式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `schema_urls` | `string\[\]` | schema url 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_use_mobile_pkg` | `boolean` | pc 端是否使用小程序版本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_version` | `string` | pc 的小程序版本号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_version` | `string` | 移动端小程序版本号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_min_lark_version` | `string` | 移动端兼容的最低飞书版本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_min_lark_version` | `string` | pc 端兼容的最低飞书版本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_app` | `web_app` | 网页能力 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_url` | `string` | pc 端 url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_url` | `string` | 移动端 url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bot` | `bot` | 机器人能力 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `card_request_url` | `string` | 消息卡片回调地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `workplace_widgets` | `workplace_widget\[\]` | 小组件能力 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `min_lark_version` | `string` | 最低兼容飞书版本号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `navigate` | `navigate` | 主导航小程序 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc` | `navigate_meta` | pc 端主导航信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `version` | `string` | 主导航小程序版本号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `image_url` | `string` | 默认图片 url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hover_image_url` | `string` | 选中态图片 url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `navigate_meta` | 移动端主导航信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `version` | `string` | 主导航小程序版本号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `image_url` | `string` | 默认图片 url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hover_image_url` | `string` | 选中态图片 url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cloud_doc` | `cloud_doc` | 云文档应用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `space_url` | `string` | 云空间重定向 url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n` | `cloud_doc_i18n_info\[\]` | 国际化信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_key` | `string` | 国际化语言的 key<br>**可选值有**：<br>- `zh_cn`: 中文 - `en_us`: 英文 - `ja_jp`: 日文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 云文档国际化名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `read_description` | `string` | 云文档国际化读权限说明 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `write_description` | `string` | 云文档国际化写权限说明 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `icon_url` | `string` | 图标链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mode` | `int` | 云文档支持模式<br>**可选值有**：<br>- `0`: 未知 - `1`: 移动端 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `docs_blocks` | `docs_block\[\]` | 云文档小组件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `block_type_id` | `string` | BlockTypeID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n` | `block_i18n_info\[\]` | block 的国际化信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_key` | `string` | 国际化语言的 key<br>**可选值有**：<br>- `zh_cn`: 中文 - `en_us`: 英文 - `ja_jp`: 日文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_icon_url` | `string` | 移动端 icon 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_icon_url` | `string` | pc 端口 icon 链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `message_action` | `message_action` | 消息快捷操作 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_app_link` | `string` | pc 端链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_app_link` | `string` | 移动端链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n` | `message_action_i18n_info\[\]` | 国际化信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_key` | `string` | 国际化语言的 key<br>**可选值有**：<br>- `zh_cn`: 中文 - `en_us`: 英文 - `ja_jp`: 日文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 国际化名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `plus_menu` | `plus_menu` | 加号菜单 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_app_link` | `string` | pc 端链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_app_link` | `string` | 移动端链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `remark` | `app_version_remark` | 跟随应用版本的信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `remark` | `string` | 备注说明 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `update_remark` | `string` | 更新说明 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `visibility` | `app_visibility` | 应用当前版本开发者编辑的可见性建议，若开发者未编辑可见性建议，则该字段无内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_all` | `boolean` | 是否全员可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `visible_list` | `app_visible_list` | 可见名单 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_ids` | `string\[\]` | 可见性成员 open_id 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 可见性部门的 id 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `group_ids` | `string\[\]` | 可见性成员 group_id 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `invisible_list` | `app_visible_list` | 不可见名单 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_ids` | `string\[\]` | 不可见性成员 open_id 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 不可见性部门的 id 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `group_ids` | `string\[\]` | 不可见性成员 group_id 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `event_infos` | `event\[\]` | 应用已订阅事件详情列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `event_type` | `string` | 事件类型，事件唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `event_name` | `string` | 事件名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `event_description` | `string` | 事件描述 |
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
                "app_id": "cli_9f3ca975326b501b",
                "version": "1.0.0",
                "version_id": "oav_d317f090b7258ad0372aa53963cda70d",
                "app_name": "应用名称",
                "avatar_url": "https://www.example.com",
                "description": "应用描述",
                "scopes": [
                    {
                        "scope": "contact:user.base",
                        "description": "获取应用信息",
                        "level": 1,
                        "token_types": [
                            "user"
                        ]
                    }
                ],
                "back_home_url": "https://www.example.com",
                "i18n": [
                    {
                        "i18n_key": "zh_cn",
                        "name": "应用名称",
                        "description": "应用描述",
                        "help_use": "https://www.example.com"
                    }
                ],
                "common_categories": [
                    "分析工具"
                ],
                "events": [
                    "contacts.open_platform.depart"
                ],
                "status": 1,
                "create_time": "1610462759",
                "publish_time": "1610462759",
                "ability": {
                    "gadget": {
                        "enable_pc_mode": 1,
                        "schema_urls": [
                            "https://www.example.com"
                        ],
                        "pc_use_mobile_pkg": false,
                        "pc_version": "1.0.0",
                        "mobile_version": "1.0.0",
                        "mobile_min_lark_version": "2.0",
                        "pc_min_lark_version": "2.0"
                    },
                    "web_app": {
                        "pc_url": "https://www.example.com",
                        "mobile_url": "https://www.example.com"
                    },
                    "bot": {
                        "card_request_url": "https://www.example.com"
                    },
                    "workplace_widgets": [
                        {
                            "min_lark_version": "1.0.0"
                        }
                    ],
                    "navigate": {
                        "pc": {
                            "version": "1.0.0",
                            "image_url": "https://www.example.com",
                            "hover_image_url": "https://www.example.com"
                        },
                        "mobile": {
                            "version": "1.0.0",
                            "image_url": "https://www.example.com",
                            "hover_image_url": "https://www.example.com"
                        }
                    },
                    "cloud_doc": {
                        "space_url": "https://www.example.com",
                        "i18n": [
                            {
                                "i18n_key": "zh_cn",
                                "name": "名称",
                                "read_description": "读权限说明",
                                "write_description": "写权限说明"
                            }
                        ],
                        "icon_url": "https://www.example.com",
                        "mode": 1
                    },
                    "docs_blocks": [
                        {
                            "block_type_id": "blk_4fb61568435880110854c1d0",
                            "i18n": [
                                {
                                    "i18n_key": "zh_cn",
                                    "name": "名称"
                                }
                            ],
                            "mobile_icon_url": "https://www.example.com",
                            "pc_icon_url": "https://www.example.com"
                        }
                    ],
                    "message_action": {
                        "pc_app_link": "https://www.example.com",
                        "mobile_app_link": "https://www.example.com",
                        "i18n": [
                            {
                                "i18n_key": "zh_cn",
                                "name": "名称"
                            }
                        ]
                    },
                    "plus_menu": {
                        "pc_app_link": "https://www.example.com",
                        "mobile_app_link": "https://www.example.com"
                    }
                },
                "remark": {
                    "remark": "备注说明",
                    "update_remark": "更新说明",
                    "visibility": {
                        "is_all": false,
                        "visible_list": {
                            "open_ids": [
                                "ou_4065981088f8ef67a504ba8bd6b24d85"
                            ],
                            "department_ids": [
                                "od-4b4a6907ad726ea07b27b0d2882b7c65"
                            ],
                            "group_ids": [
                                "b6d1g5dd6fd26186"
                            ]
                        },
                        "invisible_list": {
                            "open_ids": [
                                "ou_4065981088f8ef67a504ba8bd6b24d85"
                            ],
                            "department_ids": [
                                "od-4b4a6907ad726ea07b27b0d2882b7c65"
                            ],
                            "group_ids": [
                                "b6d1g5dd6fd26186"
                            ]
                        }
                    }
                },
                "event_infos": [
                    {
                        "event_type": "im.chat.updated_v1",
                        "event_name": "群配置修改事件",
                        "event_description": "群聊名称、头像、描述以及群编辑权限、群分享权限等被修改时推送事件"
                    }
                ]
            }
        ],
        "page_token": "new-e3c5a0627cdf0c2e057da7257b90376a",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 210500 | page_token does not exist or has expired | 请检查 page_token 是否合法，page_token 过期时间为 2h，若超过 2h 请重新获取 |
| 400 | 210501 | invalid page_token | page_token 在应用间不互通，请检查该 page_token 是否由调用接口的应用获取到 |
| 400 | 210503 | invalid app_id | 请检查请求路径中的 app_id 是否合法 |
| 400 | 210504 | no such app in tenant | 请检查被查询应用与当前调用接口应用是否在同一企业内 |
| 400 | 210505 | target app not a custom app | 请检查被查询应用是否是自建应用 |
| 400 | 210506 | no such app | 请检查请求路径中的 app_id 是否存在 |
| 400 | 210508 | insufficient permission level | 请检查应用已申请权限与被查询 app_id，当被查询 app_id 非本应用且未申请[获取应用版本信息](https://open.larkoffice.com/document/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN)权限时，返回该错误码 |
| 400 | 210514 | invalid order | 请检查 order 范围是否在 [0, 1] 范围内 |


