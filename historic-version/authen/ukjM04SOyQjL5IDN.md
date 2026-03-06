---
title: "获取 user_access_token（小程序）"
fullPath: "/uYjL24iN/ukjM04SOyQjL5IDN"
updateTime: "1687769386000"
---

# 获取 user_access_token（小程序）

通过 [login](/ssl:ttdoc/uYjL24iN/uYzMuYzMuYzM)接口获取到登录凭证`code`后，开发者可以通过服务器发送请求的方式获取 session_key 和 用户凭证信息。

:::note

本接口适用于 [小程序登录](/ssl:ttdoc/uYjL24iN/uETO5QjLxkTO04SM5kDN) 及[小组件登录](/ssl:ttdoc/uAjLw4CM/uYjL24iN/block/guide/open-ability/block-login)。
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
      <md-td>https://open.feishu.cn/open-apis/mina/v2/tokenLoginValidate</md-td>
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
            无
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
      <md-td>是</md-td>
      	<md-td>
<md-tag mode="inline" type="token-app">app_access_token</md-tag>

**值格式**："Bearer `access_token`"

**示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560"

[了解更多：获取与使用access_token](/ssl:ttdoc/ukTMukTMukTM/uMTNz4yM1MjLzUzM)

</md-td>
</md-tr>
<md-tr>
<md-td>Content-Type</md-td>
<md-td>string</md-td>
<md-td>是</md-td>
<md-td>**固定值**："application/json; charset=utf-8"</md-td>
</md-tr>
</md-tbody>
</md-table>
:::

### 请求体
参数 | 类型 | 必填 | 说明 
-- | -- | -- | -- 
code | string | 是 | [登录](/ssl:ttdoc/uYjL24iN/uYzMuYzMuYzM)时获取的 code

### 请求体示例
```json
{
     "code": "2ef0bb04e272d274"
}
```

## 响应
### 响应体

:::html
<md-table>
  <md-thead>
      <md-tr>
      <md-th style="width: 30%;">名称</md-th>
      <md-th style="width: 18%;">类型</md-th>
      <md-th >描述</md-th>
      </md-tr>
  </md-thead>
  <md-tbody>

<md-tr>
	<md-td>
	<md-text type="field-name" >code</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >int</md-text>
	</md-td>
	<md-td>
	错误码，非 0 表示失败
	</md-td>
</md-tr>


<md-tr>
	<md-td>
	<md-text type="field-name" >msg</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	错误描述
	</md-td>
</md-tr>


<md-tr>
	<md-td>
	<md-text type="field-name" >data</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >\-</md-text>
	</md-td>
	<md-td>
	\-
	</md-td>
</md-tr>
    
    <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >open_id</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	用户的[Open ID](/ssl:ttdoc/home/user-identity-introduction/open-id)，用于在同一个应用中对用户进行标识 
	</md-td>
</md-tr>
    
    <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >employee_id</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	用户的[User ID](/ssl:ttdoc/home/user-identity-introduction/user-id)，在职员工在企业内的唯一标识 

**仅当开通以下权限后 返回该字段**：
<md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
	</md-td>
</md-tr>
    
    <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >session_key</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	会话密钥
	</md-td>
</md-tr>
    
    <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >tenant_key</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	用户所在企业唯一标识
	</md-td>
</md-tr>
    
    

    
    <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >access_token</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	[user_access_token](/ssl:ttdoc/ukTMukTMukTM/uMTNz4yM1MjLzUzM)，用户身份访问凭证
	</md-td>
</md-tr>
    
    <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >expires_in</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >int</md-text>
	</md-td>
	<md-td>
	[user_access_token](/ssl:ttdoc/ukTMukTMukTM/uMTNz4yM1MjLzUzM)过期时间戳
	</md-td>
</md-tr>
    
    <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >refresh_token</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	刷新用户 access_token 时使用的 token，过期时间为30天。刷新access_token 接口说明请查看[文档](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/authen-v1/authen/refresh_access_token)
	</md-td>
</md-tr>

    
      </md-tbody>
</md-table>
:::

### 响应体示例
```json
{
    "code": 0,
    "msg": "success",
    "data": {
    	"open_id": "ou_194fcfc5e4b78db556a040ff5e42c0",
    	"employee_id":"6c486g",
    	"session_key": "e3aeb7df000c835365c630dac91bcf",
    	"tenant_key":"2c5914ac018f97",
    	"access_token":"u-tpwcnx2XzIcq8yHyJ6KL",
    	"expires_in":1565512680,
    	"refresh_token":"ur-W9dGvBJyVtwZmrwh0vBn"
    }
}
```

### 错误码
:::html
<md-table>
    <md-thead>
        <md-tr>
            <md-th style="width: 15%;">HTTP状态码</md-th>
            <md-th style="width: 15%;">错误码</md-th>
            <md-th style="width: 30%;">描述</md-th>
            <md-th style="width: 30%;">排查建议</md-th>
        </md-tr>
    </md-thead>
  <md-tbody>
    
    <md-tr>
      <md-td>200</md-td>
      <md-td>10202</md-td>
      <md-td>access token invalid</md-td>
      <md-td>检查 access_token 是否过期</md-td>
    </md-tr>
    <md-tr>
      <md-td>200</md-td>
      <md-td>10213</md-td>
      <md-td>code appid not match</md-td>
<md-td>
1. 获取code的应用与该接口的应用必须是同一个应用，请确认是否跨应用调用
2. code 仅能使用一次，请确认是否重复使用或者过期</md-td>
    </md-tr>
    <md-tr>
      <md-td>200</md-td>
      <md-td>10226</md-td>
      <md-td>invalid code</md-td>
      <md-td>code不合法，请检查code是否合法或者过期</md-td>
    </md-tr>
    <md-tr>
      <md-td>200</md-td>
      <md-td>10228</md-td>
      <md-td>user to app has no visibility</md-td>
      <md-td>当前用户没有可见性</md-td>
    </md-tr>
  </md-tbody>
</md-table>

:::



## 已知问题
返回的data中会包含一个union_id，该参数已废弃，与开放平台中常用的[Union ID](/ssl:ttdoc/home/user-identity-introduction/union-id)不是一个概念，请勿使用；如需要使用[Union ID](/ssl:ttdoc/home/user-identity-introduction/union-id)，可通过[获取单个用户信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/get)获取
:::html
