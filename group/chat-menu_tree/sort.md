---
title: "排序群菜单"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat-menu_tree/sort"
updateTime: "1748248143000"
---

# 排序群菜单

调整指定群组内的群菜单排列顺序，成功调用后接口会返回群组内所有群菜单信息。


## 前提条件

- 应用需要开启[机器人能力](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-enable-bot-ability)。
- 调用当前接口的机器人必须在对应的群组内。

## 使用限制

- 该接口仅支持群模式为 `group` 的群组，你可以调用[获取群信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat/get)接口，在返回结果中查看 `chat_mode` 参数取值是否为 `group`。
- 仅支持调整群组内一级菜单的排序。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/im/v1/chats/:chat_id/menu_tree/sort |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `im:chat` 获取与更新群组信息 `im:chat.menu_tree:write_only` 操作群菜单 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `chat_id` | `string` | 群 ID。获取方式：<br>- [创建群](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat/create)，从返回结果中获取该群的 chat_id。 - 调用[获取用户或机器人所在的群列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat/list)接口，可以查询用户或机器人所在群的 chat_id。 - 调用[搜索对用户或机器人可见的群列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat/search)，可搜索用户或机器人所在的群、对用户或机器人公开的群的 chat_id。<br>**注意**：仅支持群模式为 **群组（group）** 的群组 ID。你可以调用[获取群信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat/get)接口，在返回结果中查看 `chat_mode` 参数取值是否为 `group`。<br>**示例值**："oc_a0553eda9014c201e6969b478895c230" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `chat_menu_top_level_ids` | `string\[\]` | 是 | 通过一级菜单的 ID 进行排序。数组内的元素排序对应群组内一级菜单从左往右的排序。ID 可通过 [获取群菜单](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat-menu_tree/get) 接口获取。<br>**说明**：进行排序的 ID 列表需要跟群内存在的一级菜单 ID 列表对齐。<br>**示例值**：["6936075528890826780"] |


### 请求体示例

```json
{
    "chat_menu_top_level_ids": [
        "6936075528890826780"
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `menu_tree` | `chat.menu_tree` | 排序后，群菜单信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `chat_menu_top_levels` | `chat_menu_top_level\[\]` | 一级菜单列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `chat_menu_top_level_id` | `string` | 一级菜单 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `chat_menu_item` | `chat_menu_item` | 一级菜单信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `action_type` | `string` | 菜单类型<br>**可选值有**：<br>- `NONE`: 无分类，当一级菜单下有二级菜单时，类型取值为 NONE。 - `REDIRECT_LINK`: 跳转链接类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `redirect_link` | `chat_menu_item_redirect_link` | 跳转链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `common_url` | `string` | 公用跳转链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ios_url` | `string` | iOS 端跳转链接，当该字段不设置时，iOS 端默认使用 `common_url` 值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `android_url` | `string` | Android 端跳转链接，当该字段不设置时，Android 端默认使用 `common_url` 值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_url` | `string` | PC 端跳转链接，当该字段不设置时，PC 端默认使用 `common_url` 值。<br>**说明**：以 `https://applink.feishu.cn/client/web_url/open?mode=sidebar-semi&url=` 开头的链接表示在飞书侧边栏展开。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_url` | `string` | Web 端跳转链接，当该字段不设置时，Web 端默认使用 `common_url` 值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `image_key` | `string` | 图标的 key 值。通过[下载图片](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/get)接口可将图标下载到本地（只能下载由当前机器人上传的图片）。<br>**注意**：一级菜单下存在二级菜单时不能设置图标。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 菜单名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_names` | `i18n_names` | 菜单国际化名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `children` | `chat_menu_second_level\[\]` | 二级菜单列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `chat_menu_second_level_id` | `string` | 二级菜单 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `chat_menu_item` | `chat_menu_item` | 二级菜单 ID，后续删除、修改、排序等群菜单管理操作均需要使用菜单 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `action_type` | `string` | 菜单类型<br>**可选值有**：<br>- `NONE`: 无类型 - `REDIRECT_LINK`: 跳转链接类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `redirect_link` | `chat_menu_item_redirect_link` | 跳转链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `common_url` | `string` | 公用跳转链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ios_url` | `string` | iOS 端跳转链接，当该字段不设置时，iOS 端默认使用 `common_url` 值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `android_url` | `string` | Android 端跳转链接，当该字段不设置时，Android 端默认使用 `common_url` 值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_url` | `string` | PC 端跳转链接，当该字段不设置时，PC 端默认使用 `common_url` 值。<br>**说明**：以 `https://applink.feishu.cn/client/web_url/open?mode=sidebar-semi&url=` 开头的链接表示在飞书侧边栏展开。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `web_url` | `string` | Web 端跳转链接，当该字段不设置时，Web 端默认使用 `common_url` 值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `image_key` | `string` | 图标的 key 值。通过[下载图片](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/get)接口可将图标下载到本地（只能下载由当前机器人上传的图片）。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 菜单名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_names` | `i18n_names` | 菜单国际化名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文名 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "menu_tree": {
            "chat_menu_top_levels": [
                {
                    "chat_menu_top_level_id": "7117116451961487361",
                    "chat_menu_item": {
                        "action_type": "NONE",
                        "redirect_link": {
                            "common_url": "https://open.feishu.cn/",
                            "ios_url": "https://open.feishu.cn/",
                            "android_url": "https://open.feishu.cn/",
                            "pc_url": "https://open.feishu.cn/",
                            "web_url": "https://open.feishu.cn/"
                        },
                        "image_key": "img_v2_b0fbe905-7988-4282-b882-82edd010336j",
                        "name": "菜单",
                        "i18n_names": {
                            "zh_cn": "菜单",
                            "en_us": "Menu",
                            "ja_jp": "メニュー"
                        }
                    },
                    "children": [
                        {
                            "chat_menu_second_level_id": "7039638308221468675",
                            "chat_menu_item": {
                                "action_type": "REDIRECT_LINK",
                                "redirect_link": {
                                    "common_url": "https://open.feishu.cn/",
                                    "ios_url": "https://open.feishu.cn/",
                                    "android_url": "https://open.feishu.cn/",
                                    "pc_url": "https://open.feishu.cn/",
                                    "web_url": "https://open.feishu.cn/"
                                },
                                "image_key": "img_v2_b0fbe905-7988-4282-b882-82edd010336j",
                                "name": "报名",
                                "i18n_names": {
                                    "zh_cn": "报名",
                                    "en_us": "Sign up",
                                    "ja_jp": "サインアップ"
                                }
                            }
                        }
                    ]
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 232001 | Your request contains an invalid request parameter. | 参数错误，参考接口文档提供的参数描述，检查输入参数是否有误。 |
| 400 | 232009 | Your request specifies a chat which has already been dissolved. | 群组已被解散，无法操作。 |
| 400 | 232011 | Operator can NOT be out of the chat. | 操作者不在群组中。你需要将当前调用 API 的应用或用户[加入待操作的群组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat-members/create)后重试。 |
| 400 | 232014 | The token used in the request does NOT have the permissions necessary to complete the request. | 操作者没有权限进行该操作，请检查是否已开通调用接口所需要的权限。 |
| 400 | 232024 | Users do not have the visibility of the app, or the operator does not have collaboration permissions with the target users. | 机器人对用户没有可见性，或操作者与用户间没有协作权限。 - 如果是机器人对用户没有可见性，需要在[开发者后台](https://open.feishu.cn/app) > **应用详情页** > **应用发布** > **版本管理与发布** 编辑应用对用户的可见性并发布应用。具体操作参考[配置应用可用范围](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/availability)。 - 如果是操作者与用户之间没有协作权限，请检查是否与目标用户有协作权限，如屏蔽、未添加为联系人等。 |
| 400 | 232025 | Bot ability is not activated. | 应用未启用机器人能力。你需要登录[开发者后台](https://open.feishu.cn/app)，在应用详情页的 **应用能力** > **添加应用能力** 页面内，添加 **机器人** 能力，并发布应用使配置生效。具体操作参见[机器人能力](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-enable-bot-ability)。 |
| 400 | 232033 | The operator or invited bots does NOT have the authority to manage external chats without the scope. | 当前被操作的群为外部群，暂不支持操作外部群。只有开启对外共享能力的机器人支持外部群，详情参见[机器人支持外部群和外部用户单聊](https://open.larkoffice.com/document/uAjLw4CM/ukzMukzMukzM/develop-robots/add-bot-to-external-group)。 |
| 400 | 232034 | The app is unavailable or inactivated by the tenant. | 应用在本租户下未安装或未启用。需要先安装应用，再使用应用调用接口。 |
| 400 | 232055 | The operator does not have chat tab, chat menu, chat widget manage permission | 没有会话标签页、会话菜单和小组件的管理权限。如果在飞书客户端群设置中 **谁可以管理标签页、小组件和会话菜单** 选择了 **仅群主和管理员**，则只允许群主或者管理员进行操作。 |
| 400 | 232072 | Sort chat_menu_top_level's param is invalid. | 传入的一级菜单 ID 列表跟群内目前存在的一级菜单 ID 列表不一致。请检查参数传值是否有误。 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


