---
title: "新建文件"
fullPath: "/ukTMukTMukTM/uQTNzUjL0UzM14CN1MTN"
updateTime: "1733230641000"
---

# 新建文件

该接口用于在云空间指定文件夹中创建电子表格或者多维表格。
:::html
<md-alert type="tip">
该接口为历史版本，已不推荐使用。推荐你使用[创建表格](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet/create)或[创建多维表格](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/create)接口，能力和权限拆分力度更细。
  
</md-alert>
:::

## 使用限制

-   云空间中根目录或文件夹的单层节点上限为 1500 个。超过此限制时，接口将返回 1062507 错误码。可通过将文件新建到不同文件夹中解决。
- 云空间中所有层级的节点总和的上限为 40 万个。
- 该接口不支持并发调用，且调用频率上限为 5QPS 且 10000次/天。否则会返回 1061045 错误码，可通过稍后重试解决。
- 该接口不支持创建[文档](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-overview)（文档类型为 `docx`），如需创建文档，请调用[创建文档](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document/create)接口。


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
      <md-td>https://open.feishu.cn/open-apis/drive/explorer/v2/file/:folderToken</md-td>
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
        	<md-perm name="docs:doc" desc="查看、评论、编辑和管理文档" support_app_types="custom,isv" tags="">查看、评论、编辑和管理文档</md-perm>
            <md-perm name="sheets:spreadsheet" desc="查看、评论、编辑和管理电子表格" support_app_types="custom,isv" tags="">查看、评论、编辑和管理电子表格</md-perm>
      </md-td>
      </md-tr>
  </md-tbody>
</md-table>
:::

:::html
<md-alert type="tip">
了解更多权限相关信息，参考[云文档常见问题](/ssl:ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)。
</md-alert>
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
  通过访问凭证（access_token）对调用者身份进行鉴权。可选值：
- <md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag>：	租户授权凭证。应用代表租户（即企业或团队）执行对应操作。示例值："Bearer t-7f1bcd13fc57d46bac21793aabcef"
          
- <md-tag mode="inline" type="token-user">user_access_token</md-tag>：用户授权凭证。应用代表用户执行对应操作。示例值："Bearer u-7f1bcd13fc57d46bac21793aabcef"
了解更多，参考[获取访问凭证](/ssl:ttdoc/ukTMukTMukTM/uMTNz4yM1MjLzUzM)。

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

<br>

### 路径参数
:::html
<md-table>
  <md-thead>
      <tr>
      <md-th style="width: 15%;">名称</md-th>
      <md-th style="width: 15%;">类型</md-th>
      <md-th >描述</md-th>
      </tr>
  </md-thead>
  <md-tbody>

<md-tr>
	<md-td>
	<md-text type="field-name" >folderToken</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>

	<md-td>
	指定新建文件所属的文件夹或云空间根目录的 token。了解如何获取文件夹 token，参考[文件夹概述](/ssl:ttdoc/ukTMukTMukTM/ugTNzUjL4UzM14CO1MTN/folder-overview)。
	</md-td>
</md-tr>

  </md-tbody>
</md-table>
:::

### 请求体
:::html
<md-table>
  <md-thead>
    <md-tr>
      <md-th style="width: 15%;">参数</md-th>
      <md-th style="width: 15%;">类型</md-th>
      <md-th style="width: 10%;">必填</md-th>
      <md-th>说明</md-th>
    </md-tr>
  </md-thead>
  <md-tbody>
    <md-tr>
      <md-td>title</md-td>
      <md-td>string</md-td>
      <md-td>是</md-td>
      <md-td>
        创建的文件的标题。
      </md-td>
    </md-tr>
    <md-tr>
      <md-td>type</md-td>
      <md-td>string</md-td>
      <md-td>是</md-td>
      <md-td>
        需要创建的文件的类型，可选值：

- sheet：电子表格
- bitable：多维表格
      </md-td>
    </md-tr>
  </md-tbody>
</md-table>
:::

### 请求体示例
```json
{
   "title":"测试表格",
   "type":"sheet"
}
```

## 响应
### 响应体
|参数|类型|说明|
|--|--|--|
|url|string|新创建文件的访问链接|
|token|string|新创建文件的 token|
|revision|int|新创建文件的版本号|


### 响应体示例
```json
{
   "code":0,
   "msg":"Success",
   "data":{
      "url":"https://example.feishu.cn/sheets/shtcnOko1Ad0HU48HH8KHabcef",
      "token":"shtcnOko1Ad0HU48HH8KHabcef",
      "revision":0
   }
}
```
### 错误码
以下为本接口相关错误码。了解更多通用错误码，参考[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)。

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
      <md-td>请检查请求参数是否正确。</md-td> 
	</md-tr>
     <md-tr> 
      <md-td>91204</md-td>  
      <md-td>FORBIDDEN</md-td>  
      <md-td>检查当前应用对文档、文件夹的权限。参考[云文档常见问题](/ssl:ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)。</md-td> 
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
     <md-tr> 
      <md-td>91210</md-td>  
      <md-td>doc type is deprecated, please use docx.</md-td>  
      <md-td>旧版文档创建能力已下线，详情参考 [旧版文档（Docs 1.0）创建能力下线说明](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/breaking-change/docs-create-ability-offline)。</md-td> 
	</md-tr>
        <md-tr> 
      <md-td>1062507</md-td>  
      <md-td>parent node out of sibling num.</md-td>  
      <md-td>云空间目录下挂载数量超过限制（单层1500限制 ）。</md-td> 
	</md-tr>
        <md-tr> 
      <md-td>1061045</md-td>  
      <md-td>resource contention occurred, please retry.</md-td>  
      <md-td>发生资源争用，请稍后重试。</md-td> 
	</md-tr>
  </md-tbody> 
</md-table>
:::
