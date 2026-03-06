---
title: "更新免审词条"
fullPath: "/uAjLw4CM/ukTMukTMukTM/lingo-v1/entity/update"
updateTime: "1713496255000"
---

# 更新免审词条

通过此接口更新已有的词条，无需经过词典管理员审核，直接写入词库。因此，调用该接口时应当慎重操作。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/lingo/v1/entities/:entity_id |
| HTTP Method | PUT |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `baike:entity:exempt_review` 创建、更新词典免审词条 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `entity_id` | `string` | 词条 ID<br>**示例值**："enterprise_40217521" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `main_keys` | `term\[\]` | 是 | 词条名<br>**数据校验规则**：<br>- 最大长度：`1` |
| &nbsp;&nbsp;└ `key` | `string` | 是 | 名称<br>**示例值**："企业百科" |
| &nbsp;&nbsp;└ `display_status` | `display_status` | 是 | 展示状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allow_highlight` | `boolean` | 是 | 是否允许在 IM 和 Doc 等场景进行高亮提示<br>**示例值**：true |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allow_search` | `boolean` | 是 | 是否允许在飞书中被搜索到<br>**示例值**：true |
| `aliases` | `term\[\]` | 否 | 别名<br>**数据校验规则**：<br>- 最大长度：`10` |
| &nbsp;&nbsp;└ `key` | `string` | 是 | 名称<br>**示例值**："飞书词典" |
| &nbsp;&nbsp;└ `display_status` | `display_status` | 是 | 展示状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allow_highlight` | `boolean` | 是 | 是否允许在 IM 和 Doc 等场景进行高亮提示<br>**示例值**：true |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allow_search` | `boolean` | 是 | 是否允许在飞书中被搜索到<br>**示例值**：true |
| `description` | `string` | 否 | 详情描述<br>**示例值**："词典是飞书提供的一款知识管理工具，通过飞书词典可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通"<br>**数据校验规则**：<br>- 最大长度：`5000` 字符 |
| `related_meta` | `related_meta` | 否 | 相关数据 |
| &nbsp;&nbsp;└ `users` | `referer\[\]` | 否 | 关联用户信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 是 | 对应相关信息 ID<br>**示例值**："格式请看请求体示例" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 标题<br>**示例值**："飞书官网" |
| &nbsp;&nbsp;└ `chats` | `referer\[\]` | 否 | 相关服务中的相关公开群 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 是 | 对应相关信息 ID<br>**示例值**："格式请看请求体示例" |
| &nbsp;&nbsp;└ `docs` | `referer\[\]` | 否 | 关联文档信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 标题<br>**示例值**："飞书官网" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 链接地址<br>**示例值**："https://www.feishu.cn/hc/zh-CN"<br>**数据校验规则**：<br>- 正则校验：`(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]` |
| &nbsp;&nbsp;└ `oncalls` | `referer\[\]` | 否 | 相关服务中的相关值班号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 是 | 对应相关信息 ID<br>**示例值**："相关服务中的相关公开群" |
| &nbsp;&nbsp;└ `links` | `referer\[\]` | 否 | 相关链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 标题<br>**示例值**："飞书官网" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 链接地址<br>**示例值**："https://www.feishu.cn/hc/zh-CN"<br>**数据校验规则**：<br>- 正则校验：`(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]` |
| &nbsp;&nbsp;└ `abbreviations` | `abbreviation\[\]` | 否 | 相关词条信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 否 | 相关其他词条 id<br>**示例值**："enterprise_51587960" |
| &nbsp;&nbsp;└ `classifications` | `classification\[\]` | 否 | 当前词条所属分类 词条只能属于二级分类，且每个一级分类下只能选择一个二级分类。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 是 | 二级分类 ID<br>**示例值**："7049606926****37761" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `father_id` | `string` | 否 | 对应一级分类 ID<br>**示例值**："7049606926****37777" |
| &nbsp;&nbsp;└ `images` | `baike_image\[\]` | 否 | 上传的相关图片<br>**数据校验规则**：<br>- 最大长度：`10` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 是 | 通过文件接口上传后的图片 token<br>**示例值**："boxbcEcmKiDia3evgqWTpvdc7jc" |
| `outer_info` | `outer_info` | 否 | 外部 id 关联数据 |
| &nbsp;&nbsp;└ `provider` | `string` | 是 | 数据提供方（不能包含中横线 "-"）<br>**示例值**："星云"<br>**数据校验规则**：<br>- 长度范围：`2` ～ `32` 字符 |
| &nbsp;&nbsp;└ `outer_id` | `string` | 是 | 唯一标识，可用来和其他平台的内容进行绑定。需保证和百科词条唯一对应（不能包含中横线 "-"）<br>**示例值**："12345abc"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `64` 字符 |
| `rich_text` | `string` | 否 | 富文本格式（当填写富文本内容时，description字段将会失效可不填写），支持的格式参考[飞书词典指南](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/baike-v1/overview)中的释义部分<br>**示例值**："<b>加粗</b><i>斜体</i><p><a href=\"https://feishu.cn\">链接</a></p><p><span>词典是飞书提供的一款知识管理工具，通过飞书词典可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通</span></p>"<br>**数据校验规则**：<br>- 最大长度：`5000` 字符 |
| `i18n_descs` | `i18n_entry_desc\[\]` | 否 | 国际化的词条释义<br>**数据校验规则**：<br>- 最大长度：`3` |
| &nbsp;&nbsp;└ `language` | `int` | 是 | 语言类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 中文 - `2`: 英文 - `3`: 日文 |
| &nbsp;&nbsp;└ `description` | `string` | 否 | 纯文本释义<br>**示例值**："词典是飞书提供的一款知识管理工具，通过飞书词典可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `5000` 字符 |
| &nbsp;&nbsp;└ `rich_text` | `string` | 否 | 富文本描述<br>**示例值**："词典是飞书提供的一款知识管理工具，通过飞书词典可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `5000` 字符 |


### 请求体示例

```json
{
    "main_keys": [
        {
            "key": "飞书词典",
            "display_status": {
                "allow_highlight": true,
                "allow_search": true
            }
        }
    ],
    "aliases": [
        {
            "key": "词典",
            "display_status": {
                "allow_highlight": true,
                "allow_search": true
            }
        }
    ],
    "description": "词典是飞书提供的一款知识管理工具，通过飞书词典可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通",
    "rich_text": "词典是飞书提供的一款知识管理工具，通过飞书词典可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通",
    "i18n_descs": [
        {
            "language": 1,
            "description": "国际化中文释义",
            "rich_text": "国际化中文释义"
        }
    ],
    "related_meta": {
        "users": [
            {
                "id": "ou_30b07b6****ea46518789914dac63d36",
                "title": "负责人"
            },
            {
                "id": "ou_b292c0****c14754639fa4501e80c36a",
                "title": ""
            }
        ],
        "chats": [
            {
                "id": "oc_c13831833e****92c52befa759ea4806"
            },
            {
                "id": "oc_c8161c910****a24127e73b10233b295"
            }
        ],
        "docs": [
            {
                "title": "猜你想问 / FAQs",
                "url": "https://example.feishu.cn/wiki/wikcnZ8Lq4f9DMCDOtdcIzCUjAh"
            },
            {
                "title": "快速了解飞书文档 | Introducing Feishu Docs",
                "url": "https://example.feishu.cn/docs/doccnxlVCCFjMsJE15I7PLAjIWc"
            }
        ],
        "links": [
            {
                "title": "飞书官网",
                "url": "https://feishu.cn"
            }
        ],
        "oncalls": [
            {
                "id": "702368904****548034"
            },
            {
                "id": "70240637****0910850"
            }
        ],
        "abbreviations": [
            {
                "id": "enterprise_44***90"
            },
            {
                "id": "enterprise_70348****374354564"
            },
            {
                "id": "enterprise_70365****3106796547"
            }
        ],
        "classifications": [
            {
                "id": "7049606926****37761",
                "father_id": "7049606926****37777"
            }
        ],
        "images": [
            {
                "token": "boxbcEcmKiD3SGHvgqWTpvdc7jc"
            }
        ]
    },
    "outer_info": {
        "provider": "星云",
        "outer_id": "client_653****98d"
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
| &nbsp;&nbsp;└ `entity` | `entity` | 词条信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 词条 ID （需要更新某个词条时填写，若是创建新词条可不填写） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `main_keys` | `term\[\]` | 词条名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_status` | `display_status` | 展示状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `allow_highlight` | `boolean` | 是否允许在 IM 和 Doc 等场景进行高亮提示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `allow_search` | `boolean` | 是否允许在飞书中被搜索到 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `aliases` | `term\[\]` | 别名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_status` | `display_status` | 展示状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `allow_highlight` | `boolean` | 是否允许在 IM 和 Doc 等场景进行高亮提示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `allow_search` | `boolean` | 是否允许在飞书中被搜索到 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 纯文本格式词条释义。注：description 和 rich_text 至少有一个，否则会报错：1540001 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `string` | 创建者 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 词条创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updater` | `string` | 最近一次更新者 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `string` | 词条最近更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `related_meta` | `related_meta` | 更多相关信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `users` | `referer\[\]` | 相关联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 对应相关信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 对应相关信息的描述，如相关联系人的描述、相关链接的标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `chats` | `referer\[\]` | 相关服务中的相关公开群 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 对应相关信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 对应相关信息的描述，如相关联系人的描述、相关链接的标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `docs` | `referer\[\]` | 相关云文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `oncalls` | `referer\[\]` | 相关服务中的相关值班号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 对应相关信息 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `links` | `referer\[\]` | 关联链接信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `abbreviations` | `abbreviation\[\]` | 相关词条信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 相关词条 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `classifications` | `classification\[\]` | 当前词条所属分类 词条只能属于二级分类，且每个一级分类下只能选择一个二级分类。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 二级分类 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `father_id` | `string` | 对应一级分类 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `images` | `baike_image\[\]` | 上传的相关图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 通过文件接口上传后的图片 token |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `statistics` | `statistics` | 当前词条收到的反馈数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `like_count` | `int` | 点赞数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dislike_count` | `int` | 当前词条版本收到的负反馈数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `outer_info` | `outer_info` | 外部 id 关联数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `provider` | `string` | 外部系统（不能包含中横线 "-"） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `outer_id` | `string` | 唯一标识，可用来和其他平台的内容进行绑定。需保证和词典词条唯一对应（不能包含中横线 "-"） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rich_text` | `string` | 富文本格式（当填写富文本内容时，description字段将会失效可不填写），支持的格式参考[飞书词典指南](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/baike-v1/overview)中的释义部分 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `source` | `int` | 词条的创建来源，1：用户主动创建，2：批量导入，3：官方词，4：OpenAPI 创建 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_descs` | `i18n_entry_desc\[\]` | 国际化的词条释义 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `int` | 语言类型<br>**可选值有**：<br>- `1`: 中文 - `2`: 英文 - `3`: 日文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 纯文本释义 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rich_text` | `string` | 富文本描述 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "entity": {
            "id": "enterprise_402***21",
            "main_keys": [
                {
                    "key": "飞书词典",
                    "display_status": {
                        "allow_highlight": true,
                        "allow_search": true
                    }
                }
            ],
            "aliases": [
                {
                    "key": "词典",
                    "display_status": {
                        "allow_highlight": true,
                        "allow_search": true
                    }
                }
            ],
            "description": "词典是飞书提供的一款知识管理工具，通过飞书词典可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通",
            "rich_text": "词典是飞书提供的一款知识管理工具，通过飞书词典可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通",
            "i18n_descs": [
                {
                    "language": 1,
                    "description": "国际化中文释义",
                    "rich_text": "国际化中文释义"
                }
            ],
            "related_meta": {
                "users": [
                    {
                        "id": "ou_30b07b63089e***18789914dac63d36",
                        "title": "负责人"
                    },
                    {
                        "id": "ou_b292c0d285c1***639fa4501e80c36a",
                        "title": ""
                    }
                ],
                "chats": [
                    {
                        "id": "oc_c13831833eaa8c92***cfa759ea4806"
                    },
                    {
                        "id": "oc_c8161c9109966a24***e73b10233b295"
                    }
                ],
                "docs": [
                    {
                        "title": "猜你想问 / FAQs",
                        "url": "https://example.feishu.cn/wiki/wikcnZ8Lq4***CDOtdcIzCUjAh"
                    },
                    {
                        "title": "快速了解飞书文档 | Introducing Feishu Docs",
                        "url": "https://example.feishu.cn/docs/doccnxlVCs***sJE15I7PLAjIWc"
                    }
                ],
                "links": [
                    {
                        "title": "飞书官网",
                        "url": "https://feishu.cn"
                    }
                ],
                "oncalls": [
                    {
                        "id": "70236890***45548034"
                    },
                    {
                        "id": "70240637***60910850"
                    }
                ],
                "abbreviations": [
                    {
                        "id": "enterprise_4450***890"
                    },
                    {
                        "id": "enterprise_703481***74354564"
                    },
                    {
                        "id": "enterprise_703659***06796547"
                    }
                ],
                "classifications": [
                    {
                        "id": "70496069***2837761",
                        "father_id": "70496069***02837777"
                    }
                ],
                "images": [
                    {
                        "token": "boxbcEcmKiD***vgqWTpvdc7jc"
                    }
                ]
            },
            "statistics": {
                "like_count": 100,
                "dislike_count": 20
            },
            "outer_info": {
                "provider": "星云",
                "outer_id": "client_6539***498d"
            },
            "create_time": "1627540853",
            "update_time": "1627541853"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2250001 | invalid param | 参数错误，参考文档检查输入参数 |
| 500 | 2250002 | network anomaly, please try again | 多数请求是服务超时，请重新请求，少数是服务异常请[咨询客服](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952&extra=%7B%22channel%22:14,%22created_at%22:1614493146,%22scenario_id%22:6885151765134622721,%22signature%22:%22ca94c408b966dc1de2083e5bbcd418294c146e98%22%7D) |


