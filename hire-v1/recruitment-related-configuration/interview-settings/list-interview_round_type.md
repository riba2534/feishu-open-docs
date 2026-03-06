---
title: "获取面试轮次类型列表"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_round_type/list"
updateTime: "1721631011000"
---

# 获取面试轮次类型列表

根据职位流程查询面试轮次类型列表，可以查询到的信息包括：面试轮次类型名称、启用状态、关联的面试评价表信息。可应用于更新职位设置场景：[更新职位设置](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/update_config)


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/interview_round_types |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:interview:readonly` 获取面试信息 `hire:interview` 更新面试信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `process_type` | `int` | 否 | 职位流程类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 社招流程 - `2`: 校招流程 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `active_status` | `int` | 面试轮次类型启用状态<br>**可选值有**：<br>- `1`: 已启用 - `2`: 未启用 |
| &nbsp;&nbsp;└ `items` | `interview_round_type\[\]` | 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 面试轮次类型 ID。在面试轮次类型更新时，类型 ID 也会更新 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `biz_id` | `string` | 面试轮次类型对应的业务 ID。在面试轮次类型更新时，业务 ID 保持不变 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 面试轮次类型名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试轮次类型中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试轮次类型英文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `process_type` | `int` | 职位流程类型<br>**可选值有**：<br>- `1`: 社招流程 - `2`: 校招流程 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active_status` | `int` | 启用状态<br>**可选值有**：<br>- `1`: 启用 - `2`: 未启用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `interview_assessment_template_info` | `interview_round_type_assessment_template` | 面试评价表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 面试评价表 ID。在面试评价表更新时，评价表 ID 也会更新 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `biz_id` | `string` | 面试评价表对应的业务 ID。在面试评价表更新时，业务 ID 保持不变 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n` | 面试评价表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 面试评价表中文名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 面试评价表英文名称 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "active_status": 1,
        "items": [
            {
                "id": "7012129842917869868",
                "biz_id": "7012129842917869868",
                "name": {
                    "zh_cn": "默认面试轮次类型",
                    "en_us": "default interview round type"
                },
                "process_type": 1,
                "active_status": 1,
                "interview_assessment_template_info": {
                    "id": "7012129842917869868",
                    "biz_id": "7012129842917869868",
                    "name": {
                        "zh_cn": "默认面试评价表",
                        "en_us": "default interview assessment template"
                    }
                }
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


