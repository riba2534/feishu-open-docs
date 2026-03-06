---
title: "获取信息登记表列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/registration_schema/list"
updateTime: "1755242686000"
---

# 获取信息登记表列表

根据适用场景获取信息登记表列表，可获取到的信息包括登记表名称、登记表模块、登记表字段等


> **Tip**: 信息登记表配置请参考「飞书招聘」-「设置」-「候选人信息管理」- 「信息登记表设置」


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/registration_schemas |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:talent:readonly` 获取人才信息 `hire:talent` 更新人才信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：20<br>**默认值**：`10`<br>**数据校验规则**：<br>- 最大值：`50` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6930815272790114324 |
| `scenario` | `int` | 否 | 登记表适用场景；不填表示获取全部类型信息登记表<br>**示例值**：5<br>**可选值有**：<br>- `5`: 面试登记表 - `6`: 入职登记表 - `14`: 信息更新登记表 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `registration_schema\[\]` | 信息登记表列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 信息登记表 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 信息登记表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scenarios` | `int\[\]` | 登记表适用场景<br>**可选值有**：<br>- `5`: 面试登记表 - `6`: 入职登记表 - `14`: 信息更新登记表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `objects` | `common_schema\[\]` | 模块列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 模块名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 模块描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `setting` | `common_schema_setting` | 模块信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型，在模块信息中该字段将固定返回`11`<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `common_schema_config` | 配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `common_schema_option\[\]` | 选项信息，仅在类型`object_type`为单选、多选时有值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否是自定义模块： - `true`：自定义模块 - `false`：系统预置模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填： - `true`：必填 - `false`：非必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_visible` | `boolean` | 是否可见： - `true`：可见 - `false`：不可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `children_list` | `common_schema_child\[\]` | 字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 字段描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `setting` | `common_schema_setting` | 字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `common_schema_config` | 配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `common_schema_option\[\]` | 选项信息，仅在字段类型object_type为单选、多选时有值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 所属模块 ID，即外层的object.id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否是自定义字段： - `true`：自定义字段 - `false`：系统预置字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填： - `true`：必填 - `false`：非必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_visible` | `boolean` | 是否可见： - `true`：可见 - `false`：不可见 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "SUCCESS",
    "data": {
        "items": [
            {
                "id": "7044739584859326764",
                "name": "默认信息登记表",
                "scenarios": [
                    5
                ],
                "objects": [
                    {
                        "id": "6949805467799537964",
                        "name": {
                            "zh_cn": "简历",
                            "en_us": "Resume"
                        },
                        "description": {
                            "zh_cn": "用于信息登记的模块",
                            "en_us": "module use for info registry"
                        },
                        "setting": {
                            "object_type": 1,
                            "config": {
                                "options": [
                                    {
                                        "key": "1",
                                        "name": {
                                            "zh_cn": "模块选项",
                                            "en_us": "module option"
                                        },
                                        "description": {
                                            "zh_cn": "模块适用的选项",
                                            "en_us": "option use for mudule"
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
                                    "zh_cn": "简历自定义字段",
                                    "en_us": "resume custom field"
                                },
                                "description": {
                                    "zh_cn": "用于简历的字段",
                                    "en_us": "field use for resume"
                                },
                                "setting": {
                                    "object_type": 1,
                                    "config": {
                                        "options": [
                                            {
                                                "key": "1",
                                                "name": {
                                                    "zh_cn": "字段选项",
                                                    "en_us": "option for field"
                                                },
                                                "description": {
                                                    "zh_cn": "用于字段的选项",
                                                    "en_us": "option use for field"
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


