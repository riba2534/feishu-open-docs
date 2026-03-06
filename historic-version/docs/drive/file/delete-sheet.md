---
title: "删除Sheet"
fullPath: "/ukTMukTMukTM/uUTNzUjL1UzM14SN1MTN/delete-sheet"
updateTime: "1658126137000"
---

# 删除 Sheet


该接口用于根据 spreadsheetToken 删除对应的 sheet 文档。

:::html

<md-alert type="error">

为了更好地提升该接口的安全性，我们对其进行了升级，请尽快迁移至
  [新版本>>](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/delete)

</md-alert>

<md-alert type="warn">

文档只能被文档所有者删除，文档被删除后将会放到回收站里
</md-alert>

:::

:::note
该接口不支持并发调用，且调用频率上限为5QPS
:::

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
      <md-td>https://open.feishu.cn/open-apis/drive/explorer/v2/file/spreadsheets/:spreadsheetToken</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>DELETE</md-td>
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
<md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag>
或
<md-tag mode="inline" type="token-user">user_access_token</md-tag>
          
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

::: note
::: html
使用 <md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag> 前，请确保该应用是文档的所有者，否则会报无权限错误。
</md-td>
:::
<br>

### 路径参数
:::html
<md-table>
  <md-thead>
      <tr>
      <md-th style="width: 30%;">名称</md-th>
      <md-th style="width: 15%;">类型</md-th>
      <md-th >描述</md-th>
      </tr>
  </md-thead>
  <md-tbody>

<md-tr>
	<md-td>
	<md-text type="field-name" >spreadsheetToken</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	spreadsheet 的 token，获取方式见 [概述](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction)
	</md-td>
</md-tr>

  </md-tbody>
</md-table>
:::


## 响应
### 响应体
|参数|说明|
|--|--|
|id|sheet 的 id 「字符串类型」|
|result|删除结果|


### 响应体示例
```json
{
    "code":0,
    "msg":"Success",
    "data":
    {
        "id":"id string",
        "result":true
    }
}
```
### 错误码

:::html
<md-table> 
  <md-thead> 
    <md-tr> 
      <md-th style="width: 15%;">错误码</md-th>  
      <md-th style="width: 25%;">说明</md-th>  
      <md-th style="width: 60%;">排查建议</md-th>  
    </md-tr> 
  </md-thead>  
  <md-tbody> 
     <md-tr> 
      <md-td>91201</md-td>  
      <md-td>FAILED</md-td>  
      <md-td>处理失败，稍后重试。</md-td> 
	</md-tr>
     <md-tr> 
      <md-td>91202</md-td>  
      <md-td>PARAMERR</md-td>  
      <md-td>参数错误，检查参数是否正确，如：`type`、`fileToken`、`dstFolderToken`。</md-td> 
	</md-tr>
     <md-tr> 
      <md-td>91203</md-td>  
      <md-td>NOTEXIST</md-td>  
      <md-td>请检查请求参数是否正确，如：`type`跟`fileToken`是否匹配。</md-td> 
	</md-tr>
     <md-tr> 
      <md-td>91204</md-td>  
      <md-td>FORBIDDEN</md-td>  
      <md-td>检查当前账户对文档、文件夹的权限。参考[接入流程授权](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/docs-overview#6d744fe3)</md-td> 
	</md-tr>
     <md-tr> 
      <md-td>91205</md-td>  
      <md-td>DELETED</md-td>  
      <md-td>来源文件已被删除，检查是否还存在。</md-td> 
	</md-tr>
     <md-tr> 
      <md-td>91206</md-td>  
      <md-td>OUT_OF_LIMIT</md-td>  
      <md-td>超过限制。</md-td> 
	</md-tr>
     <md-tr> 
      <md-td>91207</md-td>  
      <md-td>DUPLICATE</md-td>  
      <md-td>重复记录。</md-td> 
	</md-tr>
     <md-tr> 
      <md-td>91208</md-td>  
      <md-td>REVIEW</md-td>  
      <md-td>内容审查不通过。</md-td> 
	</md-tr>
  </md-tbody> 
</md-table>
:::

具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)
