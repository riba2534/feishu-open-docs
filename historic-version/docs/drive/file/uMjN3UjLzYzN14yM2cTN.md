---
title: "获取元数据"
fullPath: "/ukTMukTMukTM/uMjN3UjLzYzN14yM2cTN"
updateTime: "1658126122000"
---

# 获取元数据


该接口用于根据 token 获取各类文件的元数据。

:::note
请求用户需要拥有该文件的访问（读）权限
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
      <md-td>https://open.feishu.cn/open-apis/suite/docs-api/meta</md-td>
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
<md-perm name="drive:drive.metadata:readonly" desc="查看云空间中文件元数据" support_app_types="custom,isv" tags="">查看云空间中文件元数据</md-perm>
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
<md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag> 或 
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

### 请求体
|参数|类型|必须|说明|
|--|-----|--|----|
|request_docs||是|请求文档，一次不超过200个|
|&ensp;∟docs_token|string|是|文件的 token，获取方式见[概述](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction)|
|&ensp;∟docs_type|string|是|文件类型  <br>1) "doc": 飞书文档<br>2) "sheet": 飞书电子表格 <br>3) "bitable": 飞书多维表格<br>4) "mindnote": 飞书思维笔记 <br>5) "file": 飞书文件 <br>6) "docx": 飞书新版文档|
### 请求体示例
```json
{
    "request_docs": [
        {
            "docs_token": "12345",
            "docs_type": "doc"
        },  
        {
            "docs_token": "12345",
            "docs_type": "sheet"
        }
    ]
}
```

## 响应
### 响应体
|参数|说明|
|--|--|
|docs_metas|文件元数据|
|&ensp;∟docs_token|文件token|
|&ensp;∟docs_type|文件类型|
|&ensp;∟title|标题|
|&ensp;∟owner_id|文件拥有者|
|&ensp;∟create_time|创建时间（Unix时间戳）|
|&ensp;∟latest_modify_user|最后编辑者|
|&ensp;∟latest_modify_time|最后编辑时间（Unix时间戳）|

### 响应体示例
```json
{
    "code": 0, 
    "msg": "Success",
    "data": { 
        "docs_metas": [ { 
                "docs_token": "doc22222",
                "docs_type": "doc",
                "title": "abc", 
                "owner_id": "12345", 
                "create_time": 123456, 
                "latest_modify_user": "12345", 
                "latest_modify_time": 123456
            }
        ]
    }
}
```
### 错误码

具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)
