---
title: "获取 Offer 申请表信息"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/get"
updateTime: "1751544666000"
---

# 获取 Offer 申请表信息

根据 Offer 申请表 ID 获取 Offer 申请表信息，可获取到的信息包括申请表名称、申请表模块、申请表字段等。


## Offer 申请表产品示意图
![whiteboard_exported_image (7).png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/945f549ba9d2ad3e9e70474c576189ff_n7LaFh6hLs.png?maxWidth=500px)


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/offer_application_forms/:offer_application_form_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:offer_schema:readonly` 获取 offer 申请表信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `offer_application_form_id` | `string` | Offer 申请表 ID，可通过[获取 Offer 申请表列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/list)接口获取<br>**示例值**："7680792645903286275" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `offer_apply_form` | `offer_apply_form_info` | Offer 申请表详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | Offer 申请表 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | Offer 申请表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `schema` | `offer_apply_form_schema` | schema 信息，用于描述申请表单结构的元数据定义，即对申请表内容的描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | schema ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `module_list` | `offer_apply_form_module_info\[\]` | 模块列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 模块名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否为自定义模块： - true：自定义模块 - false：系统预置模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 模块启用状态<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hint` | `i18n` | 模块填写提示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文提示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文提示 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_list` | `offer_apply_form_object_info\[\]` | 字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 字段描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `module_id` | `string` | 所属模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否为自定义字段： - true：自定义字段 - false：系统预置字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填： - true：必填 - false：非必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 字段启用状态<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `need_approve` | `boolean` | 修改后是否需要审批： - true：需要审批 - false：不需要审批 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_sensitive` | `boolean` | 是否敏感字段（敏感字段会在发起 Offer 审批时隐藏） - true：敏感字段 - false：非敏感字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型（废弃）<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 数字 - `9`: 金额 - `10`: 公式 - `11`: 默认字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type_v2` | `string` | 字段类型枚举<br>**可选值有**：<br>- `text`: 单行文本 - `long_text`: 多行文本 - `select`: 单选 - `multi_select`: 多选 - `date_select`: 日期选择 - `month_select`: 月份选择 - `year_select`: 年份选择 - `number`: 数字 - `amount`: 金额 - `formula`: 公式 - `boolean`: 布尔值 - `file`: 附件 - `personnel_select`: 人员单选 - `personnel_multi_select`: 人员多选 - `city_single_select`: 城市单选 - `corehr_text`: 单行文本（引用自人事） - `corehr_long_text`: 多行文本（引用自人事） - `corehr_select`: 单选（引用自人事） - `corehr_multi_select`: 多选（引用自人事） - `corehr_date_select`: 日期选择（引用自人事） - `corehr_number`: 数字（引用自人事） - `corehr_boolean`: 布尔值（引用自人事） - `corehr_attachment`: 附件（引用自人事） - `corehr_personnel_select`: 人员单选（引用自人事） - `corehr_personnel_multi_select`: 人员多选（引用自人事） - `default`: 默认字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `offer_apply_form_object_config_info` | 字段配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `offer_apply_form_config_option_info\[\]` | 选项信息，仅在在字段类型object_type_v2为单选、多选时有值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formula` | `offer_apply_form_config_formula_info` | 公式信息，仅在在字段类型object_type_v2为公式时有值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 计算公式。由薪资字段ID、运算符组成，薪资字段来源于offer申请表-薪资信息模块，公式中包含的薪资字段具体信息通过同级字段extra_map获取。示例："( [6872592813776914699] * 12 + 20 / 2 ) / [6872592813776914699] + 2000"，其中6872592813776914699为薪资字段ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `result` | `int` | 计算结果显示格式<br>**可选值有**：<br>- `1`: 金额 - `2`: 数字 - `3`: 百分比 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `extra_map` | `offer_apply_form_formula_extra_map_info\[\]` | 公式字段信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 公式字段 ID，字段来源于Offer申请表 - 薪资信息模块。如value示例中的：6872592813776914699 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `i18n` | 公式字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称。如：基本工资 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称。如：Basic salary |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_display_config` | `offer_apply_form_object_display_config_info` | 字段显示条件配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_condition` | `int` | 显示条件类型<br>**可选值有**：<br>- `1`: 全部满足 - `2`: 任一满足 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pre_object_config_list` | `offer_apply_form_pre_object_config_info\[\]` | 条件列表。由字段 ID、运算符、字段值组合成一个条件。如：   - 招聘类型（字段 ID 对应的字段）--等于--社招   - 入职部门（字段 ID 对应的字段）--包含--人事部 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 字段 ID，字段来源于offer申请表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `int` | 运算符<br>**可选值有**：<br>- `1`: 等于 - `2`: 不等于 - `3`: 包含 - `4`: 不包含 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string\[\]` | 字段值 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "offer_apply_form": {
            "id": "7190465990618843431",
            "name": {
                "zh_cn": "校招 Offer 申请表",
                "en_us": "campus offer application form"
            },
            "schema": {
                "id": "7080465990618843430",
                "module_list": [
                    {
                        "id": "7230465990618843432",
                        "name": {
                            "zh_cn": "基础信息模块",
                            "en_us": "basic info module"
                        },
                        "is_customized": false,
                        "active_status": 1,
                        "hint": {
                            "zh_cn": "用于填写基础信息",
                            "en_us": "use for basic info"
                        },
                        "object_list": [
                            {
                                "id": "7260465990618843426",
                                "name": {
                                    "zh_cn": "薪资总包字段",
                                    "en_us": "salary total package field"
                                },
                                "description": {
                                    "zh_cn": "用于计算薪资总包",
                                    "en_us": "use for calculate salary total package"
                                },
                                "module_id": "7230465990618843432",
                                "is_customized": true,
                                "is_required": true,
                                "active_status": 1,
                                "need_approve": true,
                                "is_sensitive": false,
                                "object_type": 3,
                                "object_type_v2":"select",
                                "config": {
                                    "options": [
                                        {
                                            "id": "7551465990618843435",
                                            "name": {
                                                "zh_cn": "全年薪资选项",
                                                "en_us": "annual salary option"
                                            },
                                            "description": {
                                                "zh_cn": "计算全年薪资",
                                                "en_us": "calculate annual salary"
                                            }
                                        }
                                    ],
                                    "object_display_config": {
                                        "display_condition": 1,
                                        "pre_object_config_list": [
                                            {
                                                "id": "7560465990618843426",
                                                "operator": 1,
                                                "value": [
                                                    "1"
                                                ]
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


