---
title: "获取客户端设备认证信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/security_and_compliance-v2/device_record/mine"
updateTime: "1761028215000"
---

# 获取设备认证信息

通过客户端授权信息获取对应设备认证信息，包含设备归属、可信状态等{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=security_and_compliance&version=v2&resource=device_record&method=mine)

:::html
<md-alert type="tip">

</md-alert>
:::

:::html
<md-alert type="warn">

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
      <md-td>https://open.feishu.cn/open-apis/security_and_compliance/v2/device_records/mine</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[50 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="security_and_compliance:device_record:read" desc="获取设备信息" support_app_types="custom,isv" tags="">获取设备信息</md-perm>
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
<md-tag mode="inline" type="token-user">user_access_token</md-tag>

**值格式**："Bearer `access_token`"

**示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560"

[了解更多：如何选择与获取 access token](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

</md-td>
</md-tr>
</md-tbody>
</md-table>
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
	<md-text type="field-name" >msg</md-text>
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
	<md-text type="field-type" >\-</md-text>
	</md-dt-td>
	<md-dt-td>
	\-
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >device_record_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	设备认证编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >device_ownership</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	设备归属

**可选值有**：
<md-enum>
<md-enum-item key="0" >未知设备</md-enum-item>
<md-enum-item key="1" >个人设备</md-enum-item>
<md-enum-item key="2" >企业设备</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >device_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	可信状态

**可选值有**：
<md-enum>
<md-enum-item key="0" >未知状态</md-enum-item>
<md-enum-item key="1" >信任设备</md-enum-item>
<md-enum-item key="2" >非信任设备</md-enum-item>
</md-enum>
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
    "msg": "success",
    "data": {
        "device_record_id": "7089353870308032531",
        "device_ownership": 0,
        "device_status": 0
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
  <md-td>500</md-td>
  <md-td>1780001</md-td>
  <md-td>Internal server error.</md-td>
  <md-td>内部接口处理失败。若无法解决，请通过【飞书客服入口】寻求帮助，https://applink.larkoffice.com/TLJpeNdW</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1780101</md-td>
  <md-td>Request param error.</md-td>
  <md-td>检查参数是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1780102</md-td>
  <md-td>The API is in beta testing. Please contact customer support to request beta access.</md-td>
  <md-td>请联系服务提供方排查，https://applink.larkoffice.com/TLJpeNdW</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1785011</md-td>
  <md-td>The current user identity has not completed device authentication.</md-td>
  <md-td>客户端未完成设备认证，建议提示用户重新登录或升级客户端至7.42及以上后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1785012</md-td>
  <md-td>The third-party device integration is not enabled.</md-td>
  <md-td>未开启允许三方应用获取客户端设备认证信息，请联系管理员前往 【飞书管理后台-安全-终端安全-设备管理-设备集成配置】进行配置</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




