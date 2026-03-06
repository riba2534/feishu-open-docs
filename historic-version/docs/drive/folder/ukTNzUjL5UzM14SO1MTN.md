---
title: "新建文件夹"
fullPath: "/ukTMukTMukTM/ukTNzUjL5UzM14SO1MTN"
updateTime: "1651916127000"
---

# 新建文件夹

该接口用于根据 folderToken 在该 folder 下创建文件夹。

:::html

<md-alert type="error">

为了更好地提升该接口的安全性，我们对其进行了升级，请尽快迁移至
  [新版本>>](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/create_folder)

</md-alert>

<md-alert type="warn">
该接口不支持并发创建，且调用频率上限为 5QPS 以及 10000次/天
</md-alert>
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
      <md-td>https://open.feishu.cn/open-apis/drive/explorer/v2/folder/:folderToken</md-td>
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
</md-th>
   <md-td>
<md-perm name="drive:drive" desc="查看、评论、编辑和管理云空间中所有文件" support_app_types="custom,isv" tags="">查看、评论、编辑和管理云空间中所有文件</md-perm>
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
or
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
关于云文档接口的 AccessToken 调用说明详见 [云文档接口快速入门](/ssl:ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)
:::

### 路径参数
|参数|类型|必须|说明|
|--|-----|--|----|
|folderToken|string|是|文件夹的 token，获取方式见 [概述](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction)| 

### 请求体
|参数|类型|必须|说明|
|--|-----|--|----|
|title|string|是|文件夹标题| 

### 请求体示例
```json
{
	"title": "string"
}
```
### 响应

### 响应体
|参数|说明|
|--|--|
|url|新创建文件夹的 url|
|revision|新创建文件夹的版本号|
|token|新创建文件夹的 token|

### 响应体示例

```json
{
	"code": 0,
	"msg": "Success",
	"data": {
		"url": "string",
    	"revision": 0,
    	"token": "string"
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

