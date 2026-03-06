---
title: "批量设置单元格样式 "
fullPath: "/ukTMukTMukTM/uAzMzUjLwMzM14CMzMTN"
updateTime: "1723618587000"
---

# 批量设置单元格样式

批量设置单元格中数据的样式。支持设置字体、背景、边框等样式。

## 使用限制
- 单次设置的范围不可超过 5,000 行 100 列。
- 在设置边框样式时，单次更新的单元格数量不可超过 30,000 个。

## 注意事项

在批量设置单元格时，当单元格在多个范围中时，单元格将应用请求体的最后一个样式。例如，对 A1:B2、B2:C3 分别设置样式，B2 单元格将应用 B2:C3 区域的样式。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/styles_batch_update |
| HTTP Method | PUT |
| 接口频率限制 | [100 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求  调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `sheets:spreadsheet` 查看、评论、编辑和管理电子表格 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | 通过访问凭证（access_token）对调用者身份进行鉴权。可选值： - `tenant_access_token`：        租户授权凭证。应用代表租户（即企业或团队）执行对应操作。示例值："Bearer t-7f1bcd13fc57d46bac21793aabcef" - `user_access_token`：用户授权凭证。应用代表用户执行对应操作。示例值："Bearer u-7f1bcd13fc57d46bac21793aabcef" 了解更多，参考[获取访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)。 |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| spreadsheetToken | string | 是 | 电子表格的 token。可通过以下两种方式获取。了解更多，参考[电子表格概述](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)。 - 电子表格的 URL：https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef== - 调用[获取文件夹中的文件清单](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list) |

### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `data` | `array` | 是 | 指定样式与范围，支持传入多对 `ranges` 和 `style` 参数。 |
| &nbsp;&nbsp;└ `ranges` | `array` | 是 | ⁣指定多个范围。单个范围的格式为 `!<开始位置>:<结束位置>`。其中：<br>- `sheetId` 为工作表 ID，通过[获取工作表](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query) 获取。 - `<开始位置>:<结束位置>` 为工作表中单元格的范围，数字表示行索引，字母表示列索引。如 `A2:B2` 表示该工作表第 2 行的 A 列到 B 列。`range`支持四种写法，详情参考[电子表格概述](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)。 |
| &nbsp;&nbsp;└ `style` | `object` | 是 | 需要更新的样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `font` | `object` | 否 | 字体相关样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `bool` | 否 | 是否加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `italic` | `bool` | 否 | 是否斜体 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fontSize` | `string` | 否 | 字体大小，如 10pt/1.5。其中 10pt 表示字号，取值范围为[9,36]pt。1.5 为行距，固定为 1.5px。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `clean` | `bool` | 否 | 是否清除字体格式，默认为 false。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `textDecoration` | `int` | 否 | 文本的其它样式，可选值： - 0：默认 - 1：下划线 - 2：删除线 - 3： 下划线和删除线 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `formatter` | `string` | 否 | 数字格式，详见[电子表格支持的数字格式类型](https://open.larkoffice.com/document/ukTMukTMukTM/uMjM2UjLzIjN14yMyYTN)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `hAlign` | `int` | 否 | 水平对齐方式。可选值： - 0：左对齐 - 1：中对齐 - 2：右对齐 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `vAlign` | `int` | 否 | 垂直对齐方式。可选值： - 0：上对齐 - 1：中对齐 - 2：下对齐 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `foreColor` | `string` | 否 | 字体颜色，用十六进制颜色代码表示。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `backColor` | `string` | 否 | 背景颜色，用十六进制颜色代码表示。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `borderType` | `string` | 否 | 边框类型，可选值： - FULL_BORDER：全边框，即四周都有边框 - OUTER_BORDER：外边框，只有外侧有边框 - INNER_BORDER：内边框，只有内部有边框 - NO_BORDER：无边框，即没有任何边框 - LEFT_BORDER：左边框，只有左侧有边框 - RIGHT_BORDER：右边框，只有右侧有边框 - TOP_BORDER：上边框，只有顶部有边框 - BOTTOM_BORDER：下边框，只有底部有边框 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `borderColor` | `string` | 否 | 边框颜色，用十六进制颜色代码表示。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `clean` | `bool` | 否 | 是否清除所有格式。默认值为 false。 |


### 请求体示例
```json
{
    "data":[
        {
            "ranges":[
                "6e5ed3!A3:C4",
                "Q7PlXT!A2:B6"
            ],
            "style":{
                "font":{
                    "bold":true,
                    "italic":true,
                    "fontSize":"10pt/1.5",
                    "clean":false
                },
                "textDecoration":0,
                "formatter":"",
                "hAlign":0,
                "vAlign":0,
                "foreColor":"#000000",
                "backColor":"#21d11f",
                "borderType":"FULL_BORDER",
                "borderColor":"#ff0000",
                "clean":false
            }
        },
        {
            "ranges":[
                "Q7PlXT!A2:B6"
            ],
            "style":{
              ...
            }
        }
    ]
}
```
  
###  cURL 请求示例
```bash
curl --location --request PUT 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/GQJHsEgcoh2qDHtSxeKcJCabcef/styles_batch_update' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data":[
        {
            "ranges":[
                "Q7PlXT!C7:E12",
                "Q7PlXT!I20:K27"
            ],
            "style":{
                "font":{
                    "bold":true,
                    "italic":true,
                    "fontSize":"10pt/1.5",
                    "clean":false
                },
                "textDecoration":0,
                "formatter":"",
                "hAlign":0,
                "vAlign":0,
                "foreColor":"#000000",
                "backColor":"#21d11f",
                "borderType":"FULL_BORDER",
                "borderColor":"#ff0000",
                "clean":false
            }
        },
        {
            "ranges":[
                "BzY8T5!A1:C2"
            ],
            "style":{
                "font":{
                    "bold":true,
                    "italic":true,
                    "fontSize":"10pt/1.5",
                    "clean":false
                },
                "textDecoration":0,
                "formatter":"",
                "hAlign":0,
                "vAlign":0,
                "foreColor":"#000000",
                "backColor":"#21d11f",
                "borderType":"FULL_BORDER",
                "borderColor":"#ff0000",
                "clean":false
            }
        }
    ]
}
'
```
  
## 响应
### 响应体


| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `spreadsheetToken` | `string` | 电子表格的 token |
| &nbsp;&nbsp;└ `totalUpdatedRows` | `int` | 设置样式的总行数 |
| &nbsp;&nbsp;└ `totalUpdatedColumns` | `int` | 设置样式的总列数 |
| &nbsp;&nbsp;└ `totalUpdatedCells` | `int` | 设置样式的单元格总数 |
| &nbsp;&nbsp;└ `revision` | `int` | 工作表的版本号。从 0 开始计数，更新一次版本号加一。 |
| &nbsp;&nbsp;└ `responses` | `/` | 各个范围的设置单元格样式的范围、行列数等 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `spreadsheetToken` | `string` | 电子表格的 token |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updatedRange` | `string` | 设置样式的范围 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updatedRows` | `int` | 设置样式的行数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updatedColumns` | `int` | 设置样式的列数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updatedCells` | `int` | 设置样式的单元格总数 |

### 响应体示例
```json
{
    "code": 0,
    "data": {
        "responses": [
            {
                "spreadsheetToken": "GQJHsEgcoh2qDHtSxeKcJCabcef",
                "updatedCells": 18,
                "updatedColumns": 3,
                "updatedRange": "6e5ed3!C7:E12",
                "updatedRows": 6
            },
            {
                "spreadsheetToken": "GQJHsEgcoh2qDHtSxeKcJCabcef",
                "updatedCells": 24,
                "updatedColumns": 3,
                "updatedRange": "4FRjKE!I20:K27",
                "updatedRows": 8
            },
            {
                "spreadsheetToken": "GQJHsEgcoh2qDHtSxeKcJCabcef",
                "updatedCells": 6,
                "updatedColumns": 3,
                "updatedRange": "9ZFgm1!A1:C2",
                "updatedRows": 2
            }
        ],
        "revision": 90,
        "spreadsheetToken": "GQJHsEgcoh2qDHtSxeKcJCabcef",
        "totalUpdatedCells": 51,
        "totalUpdatedColumns": 9,
        "totalUpdatedRows": 16
    },
    "msg": "success"
}
```
### 错误码

具体可参考：[服务端错误码说明](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)
