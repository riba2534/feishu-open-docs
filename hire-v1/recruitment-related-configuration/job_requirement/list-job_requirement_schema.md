---
title: "获取招聘需求模板列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement_schema/list"
updateTime: "1725854028000"
---

# 获取招聘需求模板列表

获取招聘需求模板列表，包含需求模板ID，以及模板里的字段定义等。招聘需求模板可参考「飞书招聘」-「设置」-「招聘需求字段管理」。


> **Tip**: [创建招聘需求](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement/create)、
> [更新招聘需求](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement/update)等接口，都需要按照招聘需求模板的定义进行传值。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/job_requirement_schemas |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:job_requirement:readonly` 获取招聘需求信息 `hire:job_requirement` 更新招聘需求信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eyJvZmZzZXQiOjEwLCJ0aW1NTUyMjM2NzIsImlkIjpudWxsfQ |
| `page_size` | `int` | 否 | 分页大小<br>**最大值**：`100`<br>**示例值**：100<br>**默认值**：`10` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `job_requirement_schema\[\]` | 招聘需求模板列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 招聘需求模板 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 招聘需求模板名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `object_list` | `common_schema\[\]` | 招聘需求模板模块列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 模块名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 模块描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `setting` | `common_schema_setting` | 模块信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 模块类型，固定返回`11`<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `common_schema_config` | 配置信息，固定返回空 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `common_schema_option\[\]` | 选项信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否是自定义模块 - true：自定义模块 - false：系统预制模块 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `children_list` | `common_schema_child\[\]` | 模块中的字段列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 字段 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 字段描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `setting` | `common_schema_setting` | 字段配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `object_type` | `int` | 字段类型，可选值为1-10，不会返回为11、13<br>**可选值有**：<br>- `1`: 单行文本 - `2`: 多行文本 - `3`: 单选 - `4`: 多选 - `5`: 日期 - `6`: 月份选择 - `7`: 年份选择 - `8`: 时间段 - `9`: 数字 - `10`: 默认字段 - `11`: 模块 - `13`: 附件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `config` | `common_schema_config` | 配置信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `options` | `common_schema_option\[\]` | 选项信息，仅适用于字段类型为单选（`3`）或多选(`4`) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 选项Key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 选项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `i18n` | 选项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 所属模块 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_customized` | `boolean` | 是否是自定义字段 - true：自定义字段 - false：系统预制字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 是否启用<br>**可选值有**：<br>- `1`: 已启用 - `2`: 已停用 |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |


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
          "zh_cn": "关键职位招聘需求模板",
          "en_us": "Recruitment requirements template for key positions"
        },
        "object_list": [
          {
            "id": "6949805467799537964",
            "name": {
              "zh_cn": "默认模块",
              "en_us": "Default module"
            },
            "description": {
              "zh_cn": "通用模块，包含招聘需求的基础字段",
              "en_us": "Generic modules that contain the basic fields of recruitment requirements"
            },
            "setting": {
              "object_type": 11,
              "config": {},
            },
            "is_customized": true,
            "is_required": false,
            "active_status": 1,
            "children_list": [
              {
                "id": "6949805467799537964",
                "name": {
                  "zh_cn": "工作地点",
                  "en_us": "workplace"
                },
                "description": {
                  "zh_cn": "工作地点",
                  "en_us": "workplace"
                },
                "setting": {
                  "object_type": 1,
                  "config": {
                    "options": [
                      {
                        "key": "Beijing",
                        "name": {
                          "zh_cn": "北京",
                          "en_us": "Beijing"
                        },
                        "description": {
                          "zh_cn": "北京",
                          "en_us": "Beijing"
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
    ],
    "has_more": true,
    "page_token": "eyJvZmZzZXQiOjEwLCJ0aW1NTUyMjM2NzIsImlkIjpudWxsfQ"
  }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


