---
title: "创建建筑物"
fullPath: "/ukTMukTMukTM/uATNwYjLwUDM24CM1AjN"
updateTime: "1658308224000"
---

# 创建建筑物

该接口对应管理后台的添加建筑，添加楼层的功能，可用于创建建筑物和建筑物的楼层信息。
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
      <md-td>https://open.feishu.cn/open-apis/meeting_room/building/create</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>

   <md-tr>
     <md-th>支持的应用类型</md-th>
      <md-td>
	  <md-app-support types="custom"></md-app-support>
      </md-td>
   </md-tr>


    
    
    <md-tr>
      <md-th>
 权限要求
 <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
</md-th>
      <md-td>
<md-perm name="calendar:room" desc="管理会议室信息" support_app_types="custom" tags="">管理会议室信息</md-perm>
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

| 参数       | 参数类型 | 必须 | 说明                                                         |
| ---------- | -------- | ---- | ------------------------------------------------------------ |
| name  | string      | 是   | 建筑名称 |
| floors | string[]   | 是   | 楼层列表 |
| country_id   | string   | 是   | 国家/地区ID |
| district_id     | string   | 是   | 城市ID |
| custom_building_id     | string   | 否   | 租户自定义建筑ID |
### 请求体示例

```json
{
    "name":"测试建筑",
    "floors":[
        "F1",
        "F2",
        "F3",
        "F4"
    ],
    "country_id":"1814991",
    "district_id":"2034437",
    "custom_building_id":"test_building_01"
}
```

## 响应
### 响应体

| 参数         | 说明                                                 |
| ------------ | ---------------------------------------------------- |
| code         | 返回码，非 0 表示失败                                |
| msg          | 返回码的描述，"success" 表示成功，其他为错误提示信息 |
| data         | 返回业务信息                                         |
| ∟building_id  | 成功创建的建筑ID                          |

### 响应体示例


```json
{
    "code":0,
    "msg":"success",
    "data":{
        "building_id":"omb_8ec170b937536a5d87c23b418b83f9bb",
    }
}
```

### 错误码

具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)