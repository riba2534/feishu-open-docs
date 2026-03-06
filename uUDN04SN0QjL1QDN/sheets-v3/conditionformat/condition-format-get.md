---
title: "批量获取条件格式"
fullPath: "/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-get"
updateTime: "1723186034000"
---

# 获取条件格式

根据工作表 ID 获取详细的条件格式信息，最多支持同时查询 10 个工作表的条件格式。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheet_token/condition_formats |
| HTTP Method | GET |
| 接口频率限制 | [100 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求  调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `drive:drive:readonly` 查看、评论和下载云空间中所有文件 `sheets:spreadsheet` 查看、评论、编辑和管理电子表格 `sheets:spreadsheet:readonly` 查看、评论和导出电子表格 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | 通过访问凭证（access_token）对调用者身份进行鉴权。可选值： - `tenant_access_token`：	租户授权凭证。应用代表租户（即企业或团队）执行对应操作。示例值："Bearer t-7f1bcd13fc57d46bac21793aabcef" - `user_access_token`：用户授权凭证。应用代表用户执行对应操作。示例值："Bearer u-7f1bcd13fc57d46bac21793aabcef" 了解更多，参考[获取访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)。 |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |

### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| spreadsheet_token | string | 电子表格的 token。可通过以下两种方式获取。了解更多，参考[电子表格概述](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)。 -  电子表格的 URL：https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef== - 调用[获取文件夹中的文件清单](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list) |
 
### 查询参数


| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `sheet_ids` | `array<string>` | 是 | 电子表格工作表的 ID。调用[获取工作表](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query)获取 ID。多个 ID 使用逗号分隔。       **示例值**：`xxxID1,xxxID2` |
  

###  cURL 请求示例
```bash
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/condition_formats?sheet_ids=Q7PlXT' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
```
## 响应  
### 响应体


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `sheet_condition_formats` | `array<interface>` | 表格的条件格式信息 |
| &nbsp;&nbsp;└ `sheet_id` | `string` | 电子表格工作表的 ID |
| &nbsp;&nbsp;└ `condition_format` | / | 条件格式的详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cf_id` | `string` | 条件格式的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ranges` | `array<string>` | 条件格式应用的范围，支持以下枚举值，了解更多，参考[条件格式指南](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-guide)。<br>- `sheetId`：填写工作表 ID，表示将条件格式应用于整表 - `sheetId!{开始行索引}:{结束行索引}`：填写工作表 ID 和行数区间，表示将条件格式应用于整行 - `sheetId!{开始列索引}:{结束列索引}`：填写工作表 ID 和列的区间，表示将条件格式应用于整列 - `sheetId!{开始单元格}:{结束单元格}`：填写工作表 ID 和单元格区间，表示将条件格式应用于单元格选定的区域中 - `sheetId!{开始单元格}:{结束列索引}`：填写工作表 ID、起始单元格和结束列，表示省略结束行，使用表格的最后行作为结束行    **示例值**：["40a7b0!C3:C3"] |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rule_type` | `string` | 创建条件时的规则类型。枚举值： - containsBlanks：为空 - notContainsBlanks：不为空 - duplicateValues：重复值 - uniqueValues：唯一值 - cellIs：限定值范围 - containsText：包含内容 - timePeriod：日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `attrs` | `array<object>` | `rule_type` 参数对应的具体属性信息。了解更多，参考[条件格式指南](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-guide)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `string` | 操作方法。了解更多，参考[条件格式指南](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-guide)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `time_period` | `string` | 时间范围。当 `rule_type` 为 `timePeriod` 时，返回该参数，且 `operator` 参数仅支持 `is`。枚举值：    - yesterday：昨天 - today：今天 - tomorrow：明天 - last7Days：最近 7 天 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `formula` | `array<string>` | 公式。当 `rule_type` 为 `cellIs` 时，返回该参数。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 文本。当 `rule_type` 为 `containsText` 时，返回该参数。值为用户自定义。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `style` | / | 条件格式的样式。支持设置字体样式、文本装饰、字体颜色和背景颜色。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `font` | / | 符合条件的数据的字体样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `bool` | 字体是否加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `bool` | 字体是否为斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text_decoration` | `int` | 文本装饰。为文本设置下划线或删除线。可选值： - 0：无下划线和删除线 - 1：下划线 - 2：删除线 - 3：同时设置下划线和删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fore_color` | `string` | 字体颜色的十六进制代码。如 #faf1d1。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `back_color` | `string` | 背景颜色的十六进制代码。如 #faf1d1。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "sheet_condition_formats": [
            {
                "condition_format": {
                    "cf_id": "r9sYuhgAl6",
                    "ranges": [
                        "uEnW3A!C4:C4"
                    ],
                    "rule_type": "timePeriod",
                    "attrs": [
                        {
                            "operator": "is",
                            "time_period": "today"
                        }
                    ],
                    "style": {
                        "back_color": "#d9f5d6",
                        "font": {
                            "bold": true,
                            "italic": false
                        },
                        "fore_color": "#faf1d1",
                        "text_decoration": 3
                    }
                },
                "sheet_id": "uEnW3A"
            }
        ]
    }
}
```
### 错误码

具体可参考：[服务端错误码说明](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)