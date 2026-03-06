---
title: "获取建筑物列表"
fullPath: "/ukTMukTMukTM/ugzNyUjL4cjM14CO3ITN"
updateTime: "1658308189000"
---

# 获取建筑物列表

该接口用于获取本企业下的建筑物（办公大楼）。

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
      <md-td>https://open.feishu.cn/open-apis/meeting_room/building/list?page_size=1&page_token=0&order_by=name-asc&fields=*</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
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
<md-perm name="calendar:room:readonly" desc="获取会议室信息" support_app_types="custom,isv" tags="">获取会议室信息</md-perm>
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

### 查询参数

| 参数       | 参数类型 | 必须 | 说明                                                         |
| ---------- | -------- | ---- | ------------------------------------------------------------ |
| page_size  | int      | 否   | 请求期望返回的建筑物数量，不足则返回全部，该值默认为 10，最大为 100 |
| page_token | string   | 否   | 用于标记当前请求的分页标记，将返回以当前分页标记开始，往后 page_size 个元素 |
| order_by   | string   | 否   | 提供用于对名称进行升序/降序排序的方式查询，可选项有："name-asc,name-desc"，传入其他字符串不做处理，默认无序 |
| fields     | string   | 否   | 用于指定返回的字段名，每个字段名之间用逗号 "," 分隔，如：“id,name”，"*" 表示返回全部字段，可选字段有："id,name,description,floors"，默认返回所有字段 |


## 响应

### 响应体

| 参数         | 说明                                                 |
| ------------ | ---------------------------------------------------- |
| code         | 返回码，非 0 表示失败                                |
| msg          | 返回码的描述，"success" 表示成功，其他为错误提示信息 |
| data         | 返回业务信息                                         |
| ∟page_token  | 分页标记，存在下一页时返回                           |
| ∟has_more    | 存在下一页时，该值为 true，否则为 false              |
| ∟buildings   | 建筑列表                                             |
| &nbsp;&nbsp;&nbsp;∟building_id | 建筑物 ID                                            |
| &nbsp;&nbsp;&nbsp;∟description | 建筑物的相关描述                                     |
| &nbsp;&nbsp;&nbsp;∟floors      | 属于当前建筑物的所有楼层列表                         |
| &nbsp;&nbsp;&nbsp;∟name        | 建筑物名称                                           |
| &nbsp;&nbsp;&nbsp;∟country_id        | 所属国家 ID                                           |
| &nbsp;&nbsp;&nbsp;∟district_id        | 所属城市 ID                                           |

### 响应体示例

```json
{
    "code":0,
    "msg":"success",
    "data":{
        "page_token":"1",
        "has_more":true,
        "buildings":[
            {
                "building_id":"omb_8ec170b937536a5d87c23b418b83f9bb",
                "description":"Some description",
                "floors":[
                    "F1"
                ],
                "name":"Building name",
                "country_id": "country id",
                "district_id": "district id"
            }
        ]
    }
}
```

### 错误码

具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)
