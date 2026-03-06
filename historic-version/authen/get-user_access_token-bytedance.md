---
title: "获取 user_access_token（仅字节）"
fullPath: "/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user_access_token-bytedance"
updateTime: "1750920552000"
---

# 获取 user_access_token（仅字节）
:::html
<md-alert type="error">
本接口已成为历史版本，不推荐使用。请使用最新版本：[获取 user_access_token ](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token)
</md-alert>。
:::

根据[登录预授权码](/ssl:ttdoc/common-capabilities/sso/api/obtain-oauth-code) 返回 code 获取 `user_access_token`。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=authen&version=v1&resource=oidc.access_token&method=create)

:::html
<md-alert type="tip">

</md-alert>
:::

:::html
<md-alert type="warn">
- 2024年9月23日起，字节内新创建的企业自建应用将**默认无法通过「获取 user_access_token」接口获取 refresh_token**，需在应用开发者后台安全设置中开启「刷新 user_access_token」开关后方可正常获取和刷新。9月19日前创建的企业自建应用暂不受影响，可通过原接口直接获取和刷新。
  
- 为了让流程更加规范，本接口不再返回用户信息，只返回token相关的字段。如需用户信息，请通过 [获取用户信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/authen-v1/user_info/get)接口获取数据
</md-alert>
:::

:::html
<md-alert type="error">

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
      <md-td>https://open.feishu.cn/open-apis/authen/v1/oidc/access_token</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[1000 次/分钟、50 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
      <md-th style="width: 35%;">名称</md-th>
      <md-th style="width: 13%;">类型</md-th>
       <md-th style="width: 15%;" filters="是,否" >必填</md-th>
      <md-th  style="width: 37%;">描述</md-th>
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

**示例值**："Bearer a-7f1bcd13fc57d46bac21793a18e560"

[了解更多：如何选择与获取 access token](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

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

:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 15%;" filters="是,否" >必填</md-dt-th>
      <md-dt-th style="width: 37%;">描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>

<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >grant_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	授权类型，**固定值**

**示例值**："authorization_code"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	登录预授权码，调用[登录预授权码](/ssl:ttdoc/common-capabilities/sso/api/obtain-oauth-code) 获取code

**示例值**："xMSldislSkdK"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "grant_type": "authorization_code",
    "code": "xMSldislSkdK"
}
</md-code-json>
:::



## 响应





### 响应体
:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 52%;">描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>

<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	错误码，非 0 表示失败
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >message</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	错误描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >token_info</md-text>
	</md-dt-td>
	<md-dt-td>
	\-
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >access_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	字段`access_token`即user_access_token，用于获取用户资源和访问某些open api
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >refresh_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	刷新user_access_token时使用的 refresh_token
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >token_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	token 类型，固定值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >expires_in</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	user_access_token有效期，单位: 秒，有效时间两个小时左右，需要以返回结果为准
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >refresh_expires_in</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	refresh_token有效期，单位: 秒，一般是30天左右，需要以返回结果为准
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >scope</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户授予app的权限全集
	</md-dt-td>
</md-dt-tr>


  </md-dt-tbody>
</md-dt-table>
:::



### 响应体示例
:::html
<md-code-json>
{
    "code": 0,
    "message": "success",
    "data": {
        "access_token": "u-5Dak9ZAxJ9tFUn8MaTD_BFM51FNdg5xzO0y010000HWb",
        "refresh_token": "ur-6EyFQZyplb9URrOx5NtT_HM53zrJg59HXwy040400G.e",
        "token_type": "Bearer",
        "expires_in": 7199,
        "refresh_expires_in": 2591999,
        "scope": "auth:user.id:read bitable:app"
    }
}
</md-code-json>
:::



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
  <md-td>20001</md-td>
  <md-td>Invalid request. Please check request param</md-td>
  <md-td>请检查请求参数</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20002</md-td>
  <md-td>The app_id or app_secret passed is incorrect. Please check the value</md-td>
  <md-td>检查app_id和密钥是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20003</md-td>
  <md-td>The code passed is invalid. Please note that the code could only be used once</md-td>
  <md-td>登录预授权码的有效期是 5 分钟，且只能被使用一次。请检查登录预授权码是否被重复使用或过期</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20004</md-td>
  <md-td>The code passed has expired. Please generate a new one</md-td>
  <md-td>过期code，请重新生成</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20007</md-td>
  <md-td>Failed to generate a user access token. Please try again</md-td>
  <md-td>请检查参数是否有效，重试</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20008</md-td>
  <md-td>User not exist</md-td>
  <md-td>用户不存在，换有效帐号</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20013</md-td>
  <md-td>The tenant access token passed is invalid. Please check the value</md-td>
  <md-td>检查tenant_access_token是否有效</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20014</md-td>
  <md-td>The app access token passed is invalid. Please check the value</md-td>
  <md-td>检查app_access_token是否有效</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20021</md-td>
  <md-td>User resigned</md-td>
  <md-td>用户离职，请使用有效帐号</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20022</md-td>
  <md-td>User frozen</md-td>
  <md-td>用户冻结，请使用有效帐号</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20023</md-td>
  <md-td>User not registered</md-td>
  <md-td>用户未注册，请使用有效帐号</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20024</md-td>
  <md-td>App id in user_access_token or refresh_token diff with app id in app_access_token or tenant_access_token. Please keep the app id consistent</md-td>
  <md-td>请检查生成两个token的app是否为同一个</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20025</md-td>
  <md-td>Lack of app_id or app_secret in request</md-td>
  <md-td>缺失app_id或app_secret，请检查参数</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20028</md-td>
  <md-td>Invalid app id</md-td>
  <md-td>无效app_id，请检查参数</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20029</md-td>
  <md-td>Invalid redirect uri</md-td>
  <md-td>redirect_uri 无效。排查方案：

1. 确保 Authorization 取值正确。
2. 确保[获取登录授权码 code](/ssl:ttdoc/common-capabilities/sso/api/obtain-oauth-code) 时，设置的回调地址 redirect_uri 参数，已配置到开发者后台 > 应用详情页 > 安全设置 > 重定向 URL。

关于该报错的详细解决方案，参见[如何解决授权免登页面 20029 错误](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-resolve-the-authorization-page-20029-error)。</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20035</md-td>
  <md-td>The app_id or app_secret passed is incorrect. Please check the value</md-td>
  <md-td>无效app_id 或 app_secret，请检查参数</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20036</md-td>
  <md-td>The grant_type passed is not supported</md-td>
  <md-td>无效grant_type，请与接口要求保持一致</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20039</md-td>
  <md-td>The user access token is not found. Please check the value</md-td>
  <md-td>查询不到user_access_token，请传有效参数</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20042</md-td>
  <md-td>App disabled</md-td>
  <md-td>app不可用，请检查app状态</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>20046</md-td>
  <md-td>Brand inconsistency</md-td>
  <md-td>应用品牌和域名品牌不一致，请保证feishu应用在feishu域名下使用，lark类似</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




