---
title: "获取申请表模板列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/portal_apply_schema/list"
updateTime: "1755250026000"
---

# 获取申请表模板列表

获取招聘官网申请表模板列表，在官网申请职位时，申请表需按照官网申请表模板的格式进行填写。


> **Tip**: 该功能尚在灰度阶段，如需使用请联系客户经理申请灰度


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/portal_apply_schemas |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:site:readonly` 获取官网信息 `hire:site` 更新官网信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：20<br>**默认值**：`10`<br>**数据校验规则**：<br>- 最大值：`50` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6930815272790114324 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `registration_schema\[\]` | 申请表模板列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 申请表模板 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 申请表模板名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scenarios` | `int\[\]` | 申请表模板适用场景<br>**可选值有**：<br>- `5`: 面试登记表 - `6`: 入职登记表 - `14`: 信息更新登记表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `objects` | `common_schema\[\]` | 模块列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 模块名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 模块描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `setting` | `common_schema_setting` | 模块信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `common_schema_config` | 配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `common_schema_option\[\]` | 选项信息，当字段类型为单选/多选时会返回该信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否是自定义模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_visible` | `boolean` | 是否可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `children_list` | `common_schema_child\[\]` | 字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 字段描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `setting` | `common_schema_setting` | 字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `common_schema_config` | 配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `common_schema_option\[\]` | 选项信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 所属模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否是自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_visible` | `boolean` | 是否可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "items": [
            {
                "id": "7044739584859326764",
                "name": "默认官网申请表",
                "scenarios": [
                    14
                ],
                "objects": [
                    {
                        "id": "6949805467799537964",
                        "name": {
                            "zh_cn": "基本信息",
                            "en_us": "Basic Information"
                        },
                        "description": {
                            "zh_cn": "候选人的基本信息",
                            "en_us": "The basic information of the candidate"
                        },
                        "setting": {
                            "object_type": 1,
                            "config": {
                                "options": [
                                    {
                                        "key": "Option1",
                                        "name": {
                                            "zh_cn": "选项一",
                                            "en_us": "Option1"
                                        },
                                        "description": {
                                            "zh_cn": "第一个选项",
                                            "en_us": "First Option"
                                        },
                                        "active_status": 1
                                    }
                                ]
                            }
                        },
                        "is_customized": true,
                        "is_required": false,
                        "is_visible": true,
                        "active_status": 1,
                        "children_list": [
                            {
                                "id": "6949805467799537964",
                                "name": {
                                    "zh_cn": "自定义字段",
                                    "en_us": "Custom Field"
                                },
                                "description": {
                                    "zh_cn": "第一个自定义字段",
                                    "en_us": "First Custom Field"
                                },
                                "setting": {
                                    "object_type": 1,
                                    "config": {
                                        "options": [
                                            {
                                                "key": "Option1",
                                                "name": {
                                                    "zh_cn": "选项一",
                                                    "en_us": "Option1"
                                                },
                                                "description": {
                                                    "zh_cn": "第一个选项",
                                                    "en_us": "First Option"
                                                },
                                                "active_status": 1
                                            }
                                        ]
                                    }
                                },
                                "parent_id": "6949805467799537964",
                                "is_customized": true,
                                "is_required": false,
                                "is_visible": true,
                                "active_status": 1
                            }
                        ]
                    }
                ]
            }
        ],
        "page_token": "6930815272790114324",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | system error | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | param illegal | 检查参数是否正确，例如类型，大小 |


