---
title: "获取人才字段"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query"
updateTime: "1747361704000"
---

# 获取人才字段

获取全部人才字段详细信息，包含字段名称、字段描述、字段类型、启用状态等信息。


## 概念说明
在「飞书招聘」-「设置」-「候选人字段管理」中，人才中的字段按照模块进行组织，一个模块下可以包含多个字段，对应人才字段类型中`模块`类型，如下图所示。

![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/ef34f907d66c16101567d67d48b08b06_NDaFV3Wupm.png?maxWidth=500)


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/talent_objects/query |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:talent:readonly` 获取人才信息 `hire:talent` 更新人才信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `common_schema\[\]` | 模块列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 模块名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 模块中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 模块英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 模块描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 模块中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 模块英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `setting` | `common_schema_setting` | 模块信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**注意**：模块级别的字段类型只能取值 `11` 模块<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `common_schema_config` | 模块配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `common_schema_option\[\]` | 选项信息，模块下该字段不会有值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 选项是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否是自定义模块 - `true` 为自定义模块 - `false` 为系统预置模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 模块是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `children_list` | `common_schema_child\[\]` | 字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 字段描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 字段中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 字段英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `setting` | `common_schema_setting` | 字段配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型<br>**注意**：字段级别的字段类型不能取值 `11` 模块<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `12`: 日期 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `common_schema_config` | 配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `common_schema_option\[\]` | 选项信息，当字段类型为 `单选` 或 `多选` 时该字段有值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 选项中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 选项英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 选项是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 所属模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否是自定义字段 - `true` 为自定义字段 - `false` 为系统预置字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 字段是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "items": [
            {
                "id": "6949805467799537964",
                "name": {
                    "zh_cn": "教育经历",
                    "en_us": "Education"
                },
                "description": {
                    "zh_cn": "人才的教育经历信息",
                    "en_us": "The education infos of talent"
                },
                "setting": {
                    "object_type": 11,
                    "config": {
                        "options": [
                            {
                                "key": "1",
                                "name": {
                                    "zh_cn": "选项一",
                                    "en_us": "Option 1"
                                },
                                "description": {
                                    "zh_cn": "这是第一个选项",
                                    "en_us": "This is the option 1"
                                },
                                "active_status": 1
                            }
                        ]
                    }
                },
                "is_customized": true,
                "is_required": false,
                "active_status": 1,
                "children_list": [
                    {
                        "id": "6949805467799537964",
                        "name": {
                            "zh_cn": "学历",
                            "en_us": "Degree"
                        },
                        "description": {
                            "zh_cn": "人才的学历是什么",
                            "en_us": "What is the degree of talent"
                        },
                        "setting": {
                            "object_type": 3,
                            "config": {
                                "options": [
                                    {
                                        "key": "1",
                                        "name": {
                                            "zh_cn": "选项一",
                                            "en_us": "Option 1"
                                        },
                                        "description": {
                                            "zh_cn": "这是第一个选项",
                                            "en_us": "This is option 1"
                                        },
                                        "active_status": 1
                                    }
                                ]
                            }
                        },
                        "parent_id": "6949805467799537964",
                        "is_customized": true,
                        "is_required": false,
                        "active_status": 1
                    }
                ]
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


