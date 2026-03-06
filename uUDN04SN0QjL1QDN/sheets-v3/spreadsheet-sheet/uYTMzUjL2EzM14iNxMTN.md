---
title: "操作工作表"
fullPath: "/ukTMukTMukTM/uYTMzUjL2EzM14iNxMTN"
updateTime: "1732796955000"
---

# 操作工作表


根据电子表格的 token 对工作表进行操作，包括增加工作表、复制工作表、删除工作表。
::: note
该接口和 [更新工作表属性](https://open.larkoffice.com/document/ukTMukTMukTM/ugjMzUjL4IzM14COyMTN) 的请求地址相同，但参数不同，调用前请仔细阅读文档。
:::

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheet_token/sheets_batch_update |
| HTTP Method | POST |
| 接口频率限制 | [100 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求  调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `sheets:spreadsheet` 查看、评论、编辑和管理电子表格 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | 应用调用 API 时，需要通过访问凭证（access_token）进行身份鉴权，参考[选择并获取访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM#5aa2e490)。 **值格式**："Bearer `access_token`"            可选值如下： - `tenant_access_token`：            	以应用身份调用 API，可读写的数据范围由应用自身的[数据权限范围](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/configure-app-data-permissions)决定。参考[自建应用获取 tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal)或[商店应用获取 tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token)。**示例值**："Bearer t-g1044qeGEDXTB6NDJOGV4JQCYDGHRBARFTGT1234"            - `user_access_token`：                以用户身份调用 API，可读写的数据范围由用户的的数据权限范围决定。参考[获取 user_access_token](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token)。。**示例值**："Bearer u-cjz1eKCEx289x1TXEiQJqAh5171B4gDHPq00l0GE1234" |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| spreadsheet_token | string | 电子表格的 token。可通过以下两种方式获取。了解更多，参考[电子表格概述](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)。 -  电子表格的 URL：https://sample.feishu.cn/sheets/==Ios7sNNEphp3WbtnbCscPqabcef== - 调用[获取文件夹中的文件清单](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list) |
 


### 请求体   


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `requests` | `/` | 是 | 支持增加、复制、和删除工作表。一次请求可以同时进行多个操作。 |
| &nbsp;&nbsp;└ `addSheet` | `/` | 否 | 增加工作表。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `properties` | `/` | 是 | 工作表属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 是 | 新增工作表的标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `index` | `int` | 否 | 新增工作表的位置。不填默认在工作表的第 0 索引位置增加工作表。 |
| &nbsp;&nbsp;└ `copySheet` | `/` | 否 | 复制工作表。复制的新工作表位于源工作表索引位置之后。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `source` | `/` | 是 | 需要复制的工作表资源 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sheetId` | `string` | 是 | 源工作表的 ID。调用[获取工作表](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query)获取 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `destination` | `/` | 是 | 新工作表的属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 新工作表名称。不填默认为“源工作表名称”+“(副本_源工作表的 `index` 值)”，如 “Sheet1(副本_0)”。 |
| &nbsp;&nbsp;└ `deleteSheet` | `/` | 否 | 删除工作表。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sheetId` | `string` | 是 | 要删除的工作表的 ID。调用[获取工作表](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query)获取 ID。 |


### 请求体示例  
```json
{
  "requests": [
    {
      "addSheet": {
        "properties": {
          "title": "new_sheet",
          "index": 1
        }
      }
    },
    {
      "copySheet": {
        "source": {
          "sheetId": "2jm6f7"
        },
        "destination": {
          "title": "sheet_copy"
        }
      }
    },
    {
      "deleteSheet": {
        "sheetId": "l8Gdub"
      }
    }
  ]
}

```
### cURL 请求示例
```bash
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/Ios7sNNEphp3WbtnbCscPqabcef/sheets_batch_update' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
  "requests": [
    {
      "addSheet": {
        "properties": {
          "title": "new_sheet",
          "index": 1
        }
      }
    },
    {
      "copySheet": {
        "source": {
          "sheetId": "2jm6f7"
        },
        "destination": {
          "title": "sheet_copy"
        }
      }
    },
    {
      "deleteSheet": {
        "sheetId": "l8Gdub"
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
| `replies` | `/` | 本次操作工作表的结果 |
| &nbsp;&nbsp;└ `addSheet` | `/` | 增加工作表的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `properties` | `/` | 新增工作表的属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sheetId` | `string` | 新增工作表的 `sheetId` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 新增工作表的标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `index` | `int` | 新增工作表的位置 |
| &nbsp;&nbsp;└ `copySheet` | `/` | 复制工作表的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `properties` | `/` | 复制的工作表的属性 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sheetId` | `string` | 复制工作表的 `sheetId` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 复制工作表的标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `index` | `int` | 复制的工作表的位置 |
| &nbsp;&nbsp;└ `deleteSheet` | `/` | 删除工作表的结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `result` | `bool` | 删除工作表是否成功 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sheetId` | `string` | 被删除的工作表的 ID |


### 响应体示例  
```json
{
  "code": 0,
  "msg": "Success",
  "data": {
    "replies": [
      {
        "addSheet": {
          "properties": {
            "sheetId": "l8Gddg",
            "title": "new_sheet",
            "index": 1
          }
        },
        "copySheet": {
          "properties": {
            "sheetId": "dso4jn",
            "title": "sheet_copy",
            "index": 0
          }
        },
        "deleteSheet": {
          "result": true,
          "sheetId": "l8Gdub"
        }
      }
    ]
  }
}
```
### 错误码

具体可参考：[服务端错误码说明](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)  


