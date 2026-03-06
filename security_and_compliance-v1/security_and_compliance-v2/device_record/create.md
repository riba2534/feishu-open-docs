---
title: "新增设备"
fullPath: "/uAjLw4CM/ukTMukTMukTM/security_and_compliance-v2/device_record/create"
updateTime: "1761026626000"
---

# 新增设备

使用该接口在设备管理中新增一台设备。新增设备的类型为管理员导入{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=security_and_compliance&version=v2&resource=device_record&method=create)

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
      <md-td>https://open.feishu.cn/open-apis/security_and_compliance/v2/device_records</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[10 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="security_and_compliance:device_record:write" desc="新增、更新、删除设备" support_app_types="custom,isv" tags="">新增、更新、删除设备</md-perm>
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
<md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag>

**值格式**："Bearer `access_token`"

**示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560"

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
	<md-text type="field-name" >device_system</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	操作系统

**示例值**：0

**可选值有**：
<md-enum>
<md-enum-item key="1" >Windows</md-enum-item>
<md-enum-item key="2" >macOS</md-enum-item>
<md-enum-item key="3" >Linux</md-enum-item>
<md-enum-item key="4" >Android</md-enum-item>
<md-enum-item key="5" >iOS</md-enum-item>
<md-enum-item key="6" >OpenHarmony</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >serial_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	生产序列号

**示例值**："C02DTHRMML7H"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >disk_serial_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	硬盘序列号

**示例值**："CC344362-5990-5A68-8DDD-64A23C99FA0C"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >uuid</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	主板UUID

**示例值**："621CDFF0-13D0-5AB1-9ADC-5F560095F6ED"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >mac_address</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	MAC地址

**示例值**："ac:de:48:00:11:21"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >android_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Android标识符

**示例值**："02a11ac4a83b918e"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >idfv</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	iOS供应商标识符

**示例值**："968F0E5C-C297-4122-ACB6-102494DEFD9A"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >aaid</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Harmony供应商标识符

**示例值**："ff3c2237-cd76-4331-9d72-0a4470854567"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >device_ownership</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	设备归属

**示例值**：0

**可选值有**：
<md-enum>
<md-enum-item key="0" >未知设备</md-enum-item>
<md-enum-item key="1" >个人设备</md-enum-item>
<md-enum-item key="2" >企业设备</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >device_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	可信状态

**示例值**：0

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





### 请求体示例
:::html
<md-code-json>
// Windows / macOS / Linux
{
    "device_system": 1 / 2 / 3,
    "serial_number": "C02DTHRMML7H",
    "disk_serial_number": "CC344362-5990-5A68-8DDD-64A23C99FA0C",
    "uuid": "621CDFF0-13D0-5AB1-9ADC-5F560095F6ED",
    "device_ownership": 0,
    "device_status": 0
}

// Android
{
    "device_system": 4,
    "android_id": "02a11ac4a83b918e",
    "device_ownership": 0,
    "device_status": 0
}

// iOS
{
    "device_system": 5,
    "idfv": "968F0E5C-C297-4122-ACB6-102494DEFD9A",
    "device_ownership": 0,
    "device_status": 0
}

// OpenHarmony
{
    "device_system": 6,
    "aaid": "ff3c2237-cd76-4331-9d72-0a4470854567",
    "device_ownership": 0,
    "device_status": 0
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
        "device_record_id": "7089353870308032531"
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
  <md-td>内部接口处理失败。若无法解决请寻求客服帮助</md-td>
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
  <md-td>联系服务提供方排查</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1785005</md-td>
  <md-td>The device information corresponding to the operating system is invalid. Please check the device information in the request.</md-td>
  <md-td>检查参数中设备特征是否与操作系统匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1785007</md-td>
  <md-td>The parameter device_system is invalid.</md-td>
  <md-td>检查参数中操作系统字段是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1785010</md-td>
  <md-td>The device already exists.</md-td>
  <md-td>系统中符合该设备特征的设备已存在</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




