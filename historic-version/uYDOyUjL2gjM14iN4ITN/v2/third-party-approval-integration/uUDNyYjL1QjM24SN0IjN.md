---
title: "三方审批实例校验"
fullPath: "/ukTMukTMukTM/uUDNyYjL1QjM24SN0IjN"
updateTime: "1657280240000"
---

# 三方审批实例校验
:::html
<md-alert type="error">
为了更好地提升接口文档的的易理解性，我们对文档进行了升级，请尽快迁移至[新版本>>](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/approval-v4/external_instance/check)
</md-alert>
:::
校验三方审批实例数据，用于判断服务端数据是否为最新的。用户提交实例最新更新时间，如果服务端不存在该实例，或者服务端实例更新时间不是最新的，则返回对应实例 id。

例如，用户可以每隔5分钟，将最近5分钟产生的实例使用该接口进行对比。

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
      <md-td>https://www.feishu.cn/approval/openapi/v3/external/instance/check</md-td>
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
<md-perm name="approval:approval:readonly" desc="访问审批应用" support_app_types="custom,isv" tags="">访问审批应用</md-perm>
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
 
**值格式**："Bearer `access_token`"

**示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560"
          
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
|-|-|-|-|
|update_times|list|是|实例信息|
|∟instance_id|String|是|审批实例 id|
|∟update_time|int|是|审批实例最近更新时间|
|∟tasks|list|是|任务信息|
|&emsp;∟task_id|String|是|任务 id|
|&emsp;∟update_time|int|是|任务最近更新时间|

### 请求体示例

```json
{
    "update_times": [
        {
            "instance_id": "1234234234242423",
            "update_time": 1591603040000,
            "tasks": [
                {
                    "task_id": "112253",
                    "update_time": 1591603040000
                },
                {
                    "task_id": "112255",
                    "update_time": 1591603040000
                }
            ]
        }
    ]
}
```

## 响应

### 响应体
|参数|类型|必须|说明|
|-|-|-|-|
|code|int|是|错误码，非0表示失败|
|msg|String|是|返回码的描述|
|data|map|是|返回业务信息|
|&emsp;diff_times|list|否|实例信息|
|&emsp;&emsp;∟instance_id|String|是|审批实例 id|
|&emsp;&emsp;∟update_time|int|否|审批实例最近更新时间|
|&emsp;&emsp;∟tasks|list|否|任务信息|
|&emsp;&emsp;&emsp;∟task_id|String|是|任务 id|
|&emsp;&emsp;&emsp;∟update_time|int|否|任务最近更新时间|
### 响应体示例

```json
{
    "code":0,
    "msg": "success",
    "data":{
      "diff_times": [
              {
                  "instance_id": "1234234234242423",
                  "update_time": 1591603040000,
                  "tasks": [
                      {
                          "task_id": "112255",
                          "update_time": 0
                      }
                  ]
              }
          ]
      }
}
```
