---
title: "批量新增部门"
fullPath: "/ukTMukTMukTM/uMDOwUjLzgDM14yM4ATN"
updateTime: "1626181320000"
---

# 批量新增部门

该接口用于向通讯录中批量新增多个部门。<br>


:::html
<md-alert type="warn">
调用该接口需要具有所有新增部门父部门的授权范围。<br>
应用商店应用无权限调用此接口。<br>
调用该接口需要申请 `更新通讯录` 以及 `以应用身份访问通讯录` 权限。<br>
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
      <md-td>https://open.feishu.cn/open-apis/contact/v2/department/batch_add</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    
    
    <md-tr>
      <md-th>
权限要求
 <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
<div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
</md-th>
      <md-td>
        <md-perm href="/ssl:ttdoc/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN"> 更新通讯录 </md-perm>
             <md-perm href="/ssl:ttdoc/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN">以应用身份访问通讯录（历史版本）</md-perm>
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
参数 | 类型 | 必填 / 选填 | 说明
-- | -- | -- | --
departments | array | 必填 | 所有要新增部门的集合。
&emsp;∟id | string | 选填 | 自定义部门 ID，企业内必须唯一。只能在创建部门时指定，不支持更新。<br>若不填该参数，将自动生成。<br>不区分大小写，长度为 1 ~ 64 个字符。只能由数字、字母和“_”、“-”、“@”、“.”四种特殊字符组成，且第一个字符必须是数字或字母。
&emsp;∟name | string | 必填 | 部门名称。
&emsp;∟parent_id | string | 必填 | 父部门 ID。<br>当被添加的部门为企业一级部门时，此字段填写“0”。
&emsp;∟leader_user_id<br>&emsp;∟leader_open_id | string | 选填 | 部门负责人 ID，支持通过 user_id 或 open_id 进行设置。<br>请求同时传递两个字段时只使用 leader_user_id，忽略 leader_open_id。
&emsp;∟create_group_chat | bool | 选填 | 是否同时创建部门群，默认为 false，不创建部门群。
### 请求体示例
```json
{
    "departments": [
        {
            "id": "custom_1",
            "name": "custom_1",
            "parent_id": "custom_2",
            "leader_user_id": "id_zhangsan",
            "leader_open_id": "ou_123456787999b8329abcdef00f7ce93c",
            "create_group_chat": true
        },
        {
            "id": "custom_2",
            "name": "custom_2",
            "parent_id": "0"
        }
    ]
}
```
## 响应
### 响应体
参数 | 说明
-- | --
code | 返回码，非 0 表示失败。
msg | 对返回码的文本描述。
data | -
&emsp;∟task_id | 生成的异步任务 ID，参见 [查询批量任务执行状态](/ssl:ttdoc/ukTMukTMukTM/uUDOwUjL1gDM14SN4ATN) 接口。
### 响应体示例
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "task_id": "123456784b68a7c89abcdef092dc09ea"
    }
}
```
### 错误码

具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)

