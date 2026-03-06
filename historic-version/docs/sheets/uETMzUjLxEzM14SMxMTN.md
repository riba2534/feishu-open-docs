---
title: "获取表格元数据"
fullPath: "/ukTMukTMukTM/uETMzUjLxEzM14SMxMTN"
updateTime: "1722417363000"
---

# 获取表格元数据

该接口用于根据 spreadsheetToken 获取表格元数据。

## 请求

:::html
<md-table>
  <md-thead>
    <tr>
      <md-th>基本</md-th>
      <md-th></md-th>
    </tr>
  </md-thead>
  <md-tbody>
    <md-tr>
      <md-th>HTTP URL</md-th>
      <md-td>https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/metainfo</md-td></md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td></md-tr>
   <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[100 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
    </md-tr>
   <md-tr>
     
     <md-th>支持的应用类型</md-th>
      <md-td>
	  <md-app-support types="custom,isv"></md-app-support>
      </md-td>
   </md-tr>


    <md-tr>
      <md-th>
权限要求
 <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
<div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
</md-th>
      <md-td>
<md-perm name="drive:drive" desc="查看、评论、编辑和管理云空间中所有文件" support_app_types="custom,isv" tags="">查看、评论、编辑和管理云空间中所有文件</md-perm>
<md-perm name="drive:drive:readonly" desc="查看、评论和下载云空间中所有文件" support_app_types="custom,isv" tags="">查看、评论和下载云空间中所有文件</md-perm>
<md-perm name="sheets:spreadsheet" desc="查看、评论、编辑和管理电子表格" support_app_types="custom,isv" tags="">查看、评论、编辑和管理电子表格</md-perm>
<md-perm name="sheets:spreadsheet:readonly" desc="查看、评论和导出电子表格" support_app_types="custom,isv" tags="">查看、评论和导出电子表格</md-perm>
</md-td>
      

    </md-tr>

  </md-tbody>
</md-table>
:::

### 请求头

:::html
<md-table> 
  <md-thead> 
    <md-tr> 
      <md-th style="width: 18%;">名称</md-th>  
      <md-th style="width: 15%;">类型</md-th>  
       <md-th style="width: 15%;">必填</md-th>  
      <md-th>描述</md-th> 
    </md-tr> 
  </md-thead>  
  <md-tbody> 
    <md-tr> 
      <md-td>Authorization</md-td>  
      <md-td>string</md-td>  
      <md-td> 是 </md-td> 
      	<md-td>
<md-tag mode="inline" type="token-user">user_access_token</md-tag> 或 <md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag> 

**值格式**："Bearer `access_token`"

**示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560"
          
 [了解更多：如何选择与获取 access token](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
	</md-td>
</md-tr>
     <md-tr> 
      <md-td>Content-Type</md-td>  
      <md-td>string</md-td>  
      <md-td> 是 </md-td> 
     <md-td>**固定值**："application/json; charset=utf-8"</md-td>
</md-tr>

  </md-tbody> 
</md-table>
:::


### 路径参数

:::html
<md-table>
  <md-thead>
  <md-tr>
      <md-th>参数</md-th>
      <md-th>类型</md-th>
      <md-th>描述</md-th>
  </md-tr>
      </md-thead>
  <md-tbody>
    <md-tr>
      <md-td>spreadsheetToken</md-td>
       <md-td>string</md-td>
       <md-td>spreadsheet 的 token；获取方式见[在线表格开发指南](/ssl:ttdoc/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)</md-td>
      </md-tr>
</md-tbody>
</md-table>
::: 


### 查询参数
:::html

:::
:::html
<md-table>
  <md-thead>
  <md-tr>
      <md-th>参数</md-th>
      <md-th>类型</md-th>
      <md-th>必须</md-th>
	  <md-th>说明</md-th>
  </md-tr>
      </md-thead>
  <md-tbody>
    <md-tr>
      <md-td>extFields</md-td>
       <md-td>string</md-td>
       <md-td>否</md-td>
      <md-td>额外返回的字段，extFields=protectedRange时返回保护行列信息</md-td>
      </md-tr>
    <md-tr>
      <md-td>user_id_type</md-td>
       <md-td>string</md-td>
       <md-td>否</md-td>
      <md-td>返回的用户id类型，可选open_id,union_id</md-td>
      </md-tr>
</md-tbody>
</md-table>
::: 

### cURL 请求示例

```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/metainfo?extFields=protectedRange&user_id_type=open_id' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e'
```

## 响应

### 响应体
:::html

:::

| 参数                              | 类型             | 说明                                                         |
| --------------------------------- | ---------------- | ------------------------------------------------------------ |
| spreadsheetToken                  | string           | spreadsheet 的 token                                         |
| properties                        |                  | spreadsheet 的属性                                           |
| &emsp;∟title                      | string           | spreadsheet 的标题                                           |
| &emsp;∟ownerUser                  | int64              | 所有者的 id，仅user_id_type为空时返回该值                                                  |
| &emsp;∟ownerUserID                  | string              | 所有者的 id，取决于user_id_type的值，仅user_id_type不为空时返回该值                                                  |
| &emsp;∟sheetCount                 | int              | spreadsheet 下的 sheet 数                                    |
| &emsp;∟revision                   | int              | 该 sheet 的版本                                              |
| sheets                            | array<interface> | spreadsheet 下的sheet列表                                    |
| &emsp;∟sheetId                    | string           | sheet 的 id                                                  |
| &emsp;∟title                      | string           | sheet 的标题                                                 |
| &emsp;∟index                      | int              | sheet 的位置                                                 |
| &emsp;∟rowCount                   | int              | sheet 的最大行数                                             |
| &emsp;∟columnCount                | int              | sheet 的最大列数                                             |
| &emsp;∟frozenRowCount             | int              | 该 sheet 的冻结行数，小于等于 sheet 的最大行数，0表示未设置冻结 |
| &emsp;∟frozenColCount             | int              | 该 sheet 的冻结列数，小于等于 sheet 的最大列数，0表示未设置冻结 |
| &emsp;∟merges                     | array<interface> | 该 sheet 中合并单元格的范围                                  |
| &emsp;&emsp;∟startRowIndex        | int              | 合并单元格范围的开始行下标，index 从 0 开始                  |
| &emsp;&emsp;∟startColumnIndex     | int              | 合并单元格范围的开始列下标，index 从 0 开始                  |
| &emsp;&emsp;∟rowCount             | int              | 合并单元格范围的行数量                                       |
| &emsp;&emsp;∟columnCount          | int              | 合并单元格范围的列数量                                       |
| &emsp;∟protectedRange             | array<interface> | 该 sheet 中保护范围                                          |
| &emsp;&emsp;∟dimension            |                  | 保护行列的信息，如果为保护工作表，则该字段为空               |
| &emsp;&emsp;&emsp;∟startIndex     | int              | 保护行列的起始位置，位置从1开始                              |
| &emsp;&emsp;&emsp;∟endIndex       | int              | 保护行列的结束位置，位置从1开始                              |
| &emsp;&emsp;&emsp;∟majorDimension | string           | 若为ROWS，则为保护行；为COLUMNS，则为保护列                  |
| &emsp;&emsp;&emsp;∟sheetId        | string           | 保护范围所在工作表 ID                                        |
| &emsp;&emsp;∟protectId            | string           | 保护范围ID                                                   |
| &emsp;&emsp;∟lockInfo             | string           | 保护说明                                                     |
| &emsp;&emsp;∟sheetId              | string           | 保护工作表 ID                                                |
| &emsp;∟blockInfo                  |                  | 若含有该字段，则此工作表不为表格                             |
| &emsp;&emsp;∟blockToken           | string           | block的token                                                 |
| &emsp;&emsp;∟blockType            | string           | block的类型                                                  |

### 响应体示例

```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "properties": {
            "title": "",
            "ownerUser": 0,
            "sheetCount": 0,
            "revision": 0
        },
        "sheets": [
            {
                "sheetId": "***",
                "title": "***",
                "index": 0,
                "rowCount": 0,
                "columnCount": 0,
                "frozenColCount": 0,
                "frozenRowCount": 0,
                "merges": [
                    {
                        "columnCount": 0,
                        "rowCount": 0,
                        "startColumnIndex": 0,
                        "startRowIndex": 0
                    }
                ],
                "protectedRange": [
                    {
                        "dimension": {
                            "endIndex": 0,
                            "majorDimension": "ROWS",
                            "sheetId": "***",
                            "startIndex": 0
                        },
                        "protectId": "***",
                        "sheetId": "***",
                        "lockInfo": "***"
                    }
                ]
            },
            {
                "blockInfo": {
                    "blockToken": "***",
                    "blockType": "***"
                },
                "columnCount": 0,
                "frozenColCount": 0,
                "frozenRowCount": 0,
                "index": 0,
                "rowCount": 0,
                "sheetId": "***",
                "title": "*** "
            }
        ],
        "spreadsheetToken": "***"
    }
}
```

### 错误码

具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)