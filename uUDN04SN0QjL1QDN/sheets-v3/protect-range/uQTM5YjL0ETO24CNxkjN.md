---
title: "获取保护范围"
fullPath: "/ukTMukTMukTM/uQTM5YjL0ETO24CNxkjN"
updateTime: "1723618710000"
---

# 获取保护范围

获取电子表格工作表中指定保护范围的信息，包括保护的行列索引、支持编辑的用户 ID、保护范围的备注等。

## 使用限制

- 单次调用该接口，最多支持获取 5 个保护范围的信息。
- 不支持获取包含多个区域的保护范围。即如果一个保护范围中添加了多个区域，例如 B22:B26 和 C26:C28，则不支持调用该接口获取。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/protected_range_batch_get |
| HTTP Method | GET |
| 接口频率限制 | [100 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求  调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `sheets:spreadsheet` 查看、评论、编辑和管理电子表格 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | 通过访问凭证（access_token）对调用者身份进行鉴权。可选值： - `tenant_access_token`：        租户授权凭证。应用代表租户（即企业或团队）执行对应操作。示例值："Bearer t-7f1bcd13fc57d46bac21793aabcef"            - `user_access_token`：用户授权凭证。应用代表用户执行对应操作。示例值："Bearer u-7f1bcd13fc57d46bac21793aabcef" 了解更多，参考[获取访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)。 |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| spreadsheetToken | string | 电子表格的 token。可通过以下两种方式获取。了解更多，参考[电子表格概述](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)。 -  电子表格的 URL：https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef== - 调用[获取文件夹中的文件清单](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)        **示例值**："Iow7sNNEphp3WbtnbCscPqabcef" |


### 查询参数


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `protectIds` | `string` | 是 | 保护范围的 ID，可通过[获取表格元数据](https://open.larkoffice.com/document/ukTMukTMukTM/uETMzUjLxEzM14SMxMTN)接口获取。多个 ID 之间用逗号分隔。最多可传入 5 个 ID。    **示例值**："7379738014546812456,7379738014546812456" |
| `memberType` | `string` | 否 | 返回的用户 ID 的类型。默认为 `userId`，建议选择 `openId`。了解更多，参考[用户身份概述](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。可选值：<br>- `userId`：即 `lark_id`，为全局 ID，标识用户的物理用户身份。<br>- `openId`：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。了解更多：[如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- `unionId`：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。了解更多：[如何获取 Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) |

### cURL 请求示例
```bash
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/protected_range_batch_get?protectIds=6946456074476339204,6947648349520592923,6947942538267541505&memberType=userId' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
```

## 响应  
### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `protectedRanges` | `array<interface>` | 保护范围的信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `protectId` | `string` | 保护范围的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dimension` | `` | 保护范围的维度信息。为空表示保护整个工作表。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `sheetId` | `string` | 工作表的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `startIndex` | `int` | 开始的行或列的索引。从 1 开始计数。若 `startIndex` 为 3，则从第 3 行或列开始保护。包含第 3 行或列。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `endIndex` | `int` | 结束的行或列的索引。从 1 开始计数。若 `endIndex` 为 7，则保护到第 7 行或列。包含第 7 行或列。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `majorDimension` | `string` | 保护范围的维度。可选值： - ROWS：行 - COLUMNS：列 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sheetId` | `string` | 工作表的 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `lockInfo` | `string` | 保护范围的备注信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `editors` | `` | 允许编辑保护范围的用户信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `users` | `array<interface>` | 用户信息的列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `memberType` | `string` | 用户 ID 的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `memberId` | `string` | 用户的 ID |

### 响应体示例

```json
{
  "code": 0,
  "data": {
    "protectedRanges": [
      {
        "dimension": {
          "endIndex": 13,
          "majorDimension": "COLUMNS",
          "sheetId": "aIVj4J",
          "startIndex": 10
        },
        "editors": {
          "users": [
            {
              "memberId": "7307457169426112456",
              "memberType": "userId"
            }
          ]
        },
        "lockInfo": "你能编辑",
        "protectId": "7379738014546821122",
        "sheetId": "aIVj4J"
      },
      {
        "dimension": {
          "endIndex": 14,
          "majorDimension": "COLUMNS",
          "sheetId": "aIVj4J",
          "startIndex": 13
        },
        "editors": {
          "users": [
            {
              "memberId": "7307457169426112456",
              "memberType": "userId"
            }
          ]
        },
        "lockInfo": "你能编辑",
        "protectId": "7379831455515639836",
        "sheetId": "aIVj4J"
      }
    ]
  },
  "msg": "success"
}
```

### 错误码

具体可参考：[服务端错误码说明](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)