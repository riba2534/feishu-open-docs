---
title: "导入表格"
fullPath: "/ukTMukTMukTM/uATO2YjLwkjN24CM5YjN"
updateTime: "1646321582000"
---

# 导入表格
>  为了更好地提升该接口的安全性，我们对其进行了升级，请尽快迁移至[新版本](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/import_task/import-user-guide)


该接口用于将本地表格导入到云空间上。
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
      <md-td>https://open.feishu.cn/open-apis/sheets/v2/import</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
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
<md-perm name="sheets:spreadsheet" desc="查看、评论、编辑和管理电子表格" support_app_types="custom,isv" tags="">查看、评论、编辑和管理电子表格</md-perm>
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

### 请求体
| 参数          | 类型       | 必须 | 说明                                                         |
| ------------- | ---------- | ---- | ------------------------------------------------------------ |
| file          | array<byte> | 是   | 需要导入的文件数据，转换成字节数组的形式，支持"xlsx","csv"格式，最大不超过20M  |
| name          | string     | 是   | 文件名，带上文件拓展名，如"hello.csv"、"hello.xlsx"。导入后sheet的标题将去除文件拓展名，如"hello.xlsx"导入后标题为"hello"。           |
| folderToken   | string     | 否   | 导入的文件夹token，默认导入到根目录下                        |
### 请求体示例

```json
{
    "file": [80,75,3,......],
    "name": "name.xlsx",
    "folderToken": "fldxxxxx"
}
```
### cURL 请求示例
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/import' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "file": [49,44,51,44,52,53,44,50,51,50,44,49,10,53,44,53,50,54,44,49,50,44,53,44,51,54,50,51,44,52,10,49,50,51,50,44,53,49,52,44,53,44,50,54,44,51,50,44,50,44,49,51,49,50],
    "name": "test.csv",
    "folderToken": "fldcncFpcEKOpsQhFpZD2VV6kXf"
}'
```
## 响应
### 响应体
| 参数   |类型| 说明                                             |
| ------ |-----| ------------------------------------------------ |
| ticket |string| 与导入文件一一对应的凭证，用于查询文件导入的进度，详见[查询导入结果的接口](/ssl:ttdoc/ukTMukTMukTM/uETO2YjLxkjN24SM5YjN)  |
### 响应体示例

```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "ticket": "6891610400000000"
    }
}
```
### 错误码

具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)


