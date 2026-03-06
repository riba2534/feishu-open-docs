---
title: "获取电子签模板列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/signature_template_info_with_thumbnail/list"
updateTime: "1764324084000"
---

# 获取电子签模板列表

该接口用于批量获取电子签模板信息，包括模板类别、用途、适用区域等。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/signature_template_info_with_thumbnails |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:signature_template:read` 获取电子签模板信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小；如果不填，默认为10<br>**示例值**：10 |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：0 |
| `name` | `string` | 否 | 模版名<br>**示例值**：入职模板 |
| `category_apiname` | `string` | 否 | 模版类别，多个类别之间请使用英文逗号分隔； 枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板类别（signature_template_category）枚举定义部分获得<br>**示例值**：contract_agreement,certificate |
| `usage_apiname` | `string` | 否 | 模板用途，多个用途之间使用英文逗号分隔； 枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板用途（signature_template_usage）枚举定义部分获得<br>**示例值**：dispatch,general |
| `active` | `boolean` | 否 | 是否停用<br>**示例值**：false |
| `applicability_apinames` | `string\[\]` | 否 | 电子签模板适用范围，多个用途之间使用英文逗号分隔； 枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板适用范围（signature_template_applicability）枚举定义部分获得<br>**示例值**：document_print, 文件打印<br>**数据校验规则**：<br>- 长度范围：`0` ～ `4294967296` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `signature_template_info_with_thumbnail\[\]` | 电子签模板列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 名称 支持多语 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `category` | `enum` | 模版类别， 枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板类别（signature_template_category）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `usage` | `enum` | 模版用途； 枚举值可通过文档[【飞书人事枚举常量】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)电子签模板类别（signature_template_category）枚举定义部分获得 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 创建日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `modify_time` | `string` | 修改日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_by` | `signature_user_info` | 创建人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 雇佣ID，[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_by` | `signature_user_info` | 修改人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 雇佣ID，[【搜索员工信息】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `thumbnail_url` | `string` | 缩略图url |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `signatory_labels` | `signature_signatory_label\[\]` | 模版签署人标签 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `template_signatory_type` | `enum` | 电子签模板签订人类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_name` | `string` | 枚举值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display` | `i18n\[\]` | 枚举多语展示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 中英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `apiname` | `string` | 主数据apiname |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `template_code` | `string` | 模板编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `template_desc` | `string` | 模板描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `template_region_info` | `signature_template_region_info` | 模板适用区域 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_global_scope` | `string` | 是否全球适用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `meta_infos` | `signature_meta_info\[\]` | 适用区域名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | 元数据api_name |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `wk_id` | `string` | wukong id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `i18n\[\]` | 多语描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `lang` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 内容 |
| &nbsp;&nbsp;└ `page_token` | `int` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `count` | `int` | 数据总数 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": "1",
                "label": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "category": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "张三"
                        }
                    ]
                },
                "usage": {
                    "enum_name": "phone_type",
                    "display": [
                        {
                            "lang": "zh-CN",
                            "value": "张三"
                        }
                    ]
                },
                "create_time": "2021-12-21",
                "modify_time": "2021-12-21",
                "created_by": {
                    "id": "7300476612163913260"
                },
                "updated_by": {
                    "id": "7300476612163913260"
                },
                "thumbnail_url": "1",
                "signatory_labels": [
                    {
                        "template_signatory_type": {
                            "enum_name": "phone_type",
                            "display": [
                                {
                                    "lang": "zh-CN",
                                    "value": "张三"
                                }
                            ]
                        },
                        "label": [
                            {
                                "lang": "zh-CN",
                                "value": "张三"
                            }
                        ],
                        "apiname": "status"
                    }
                ],
                "template_code": "1234",
                "template_desc": "desc",
                "template_region_info": {
                    "is_global_scope": "global",
                    "meta_infos": [
                        {
                            "api_name": "status",
                            "wk_id": "123124124124123",
                            "label": [
                                {
                                    "lang": "zh-CN",
                                    "value": "张三"
                                }
                            ]
                        }
                    ]
                }
            }
        ],
        "page_token": 1000,
        "count": 1000
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1160100 | param is invalid | 参数无效。请检查请求参数的类型、格式或值是否符合接口要求（如参数是否缺失、类型是否与文档一致）或联系相关[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 403 | 1160101 | illegal user | 非法用户。请验证用户ID是否正确、用户是否存在或是否具备访问该接口的权限，或者联系相关[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1160102 | template not found | 模板未找到。请检查模板ID是否正确、模板是否已创建或未被删除，或联系相关[技术支持](https://applink.feishu.cn/TLJpeNdW) |


