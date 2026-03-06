---
title: "更新待入职信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/patch"
updateTime: "1756127395000"
---

# 更新待入职

通过指定系统字段和自定义字段以更新待入职数据{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=pre_hire&method=patch)

:::html
<md-alert type="tip">
该接口会按照应用拥有的「待入职人员」的权限范围返回数据，请提前在「开发者后台 - 权限管理 - 数据权限-飞书人事(企业版)数据权限范围」中申请「待入职人员」权限范围
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/pre_hires/:pre_hire_id</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>PATCH</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[1000 次/分钟、50 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="corehr:pre_hire:update" desc="更新待入职人员信息" support_app_types="custom" tags="">更新待入职人员信息</md-perm>
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



### 路径参数
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
	<md-text type="field-name" >pre_hire_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	待入职ID，可以通过[搜索待入职人员信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/search)接口获得

**示例值**："7345005664477775411"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
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
	<md-text type="field-name" >basic_info_update</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >basic_info_update</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	更新个人（person）信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >names</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >name_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	姓名，该值是一个list，会全量更新。即使只更新 list 中的某一个元素，也需要把其它元素都完整传值，否则将丢失数据。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >full_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	全名

**示例值**："李一一"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >first_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	名

**示例值**："一"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >middle_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	中间名

**示例值**："一"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	姓

**示例值**："李"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_first_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	名 - 本地文字

**示例值**："一"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_middle_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	本地中间名

**示例值**："一"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	姓 - 本地文字

**示例值**："李"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_local_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义姓名（本地文字）

**示例值**："李一一"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_western_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义姓名（西方文字）

**示例值**："YiyiLi"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >country_region</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家/地区，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	姓名类型，枚举值如下：

- legal_name：法定姓名
- preferred_name：常用名
- former_name：曾用名
- additional_name：别名

**示例值**："legal_name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >additional_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	别名

**示例值**："别名"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >phones</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >phone_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	电话，该值是一个list，会全量更新。即使只更新 list 中的某一个元素，也需要把其它元素都完整传值，否则将丢失数据。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >international_area_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	电话区号，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = phone
- custom_api_name = international_area_code

**示例值**："86_china"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >phone_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	电话号码

**示例值**："178xxxx1234"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >device_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	设备类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = phone
- custom_api_name = device_type

**示例值**："mobile_phone"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >phone_usage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	电话用途，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = phone
- custom_api_name = phone_usage

**示例值**："work"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	主要电话，若有多个电话，只能有一个电话的「is_primary」为true

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	公开电话

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >emails</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >email_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	邮箱，该值是一个list，会全量更新。即使只更新 list 中的某一个元素，也需要把其它元素都完整传值，否则将丢失数据。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >email</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	邮箱地址

**示例值**："1234567@bytedance.com"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	是否为主要邮箱,若有多个邮箱，只能有一个邮箱的「is_primary」为true

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	是否为公开邮箱

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >email_usage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	邮箱用途，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = email
- custom_api_name = email_usage

**示例值**："work"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >nationality_v2_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	国籍，可以通过[查询国籍信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-nationality/search)接口获取

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >additional_nationality_id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	其他国籍，可以通过[查询国籍信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-nationality/search)接口获取

**示例值**：["6862995757234914824"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >resident_tax_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >resident_tax_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	纳税身份信息,该值是一个list，会全量更新
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >tax_country_region</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	国家 / 地区ID，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >resident_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	居民身份

**示例值**："tax_residence"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >tax_address</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >address_for_update</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	纳税地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >country_region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家 / 地区，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	主要行政区，可以通过接口[查询省份/行政区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)获得

**示例值**："6863326815667095047"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line1</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 1（非拉丁语系的本地文字）

**示例值**："北京市海淀区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 2（非拉丁语系的本地文字）

**示例值**："上海市杨浦区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line3</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 3（非拉丁语系的本地文字）

**示例值**："北京市房山区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line4</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 4（非拉丁语系的本地文字）

**示例值**："天津滨海高新区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line5</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 5（非拉丁语系的本地文字）

**示例值**："成都市成华区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line6</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 6（非拉丁语系的本地文字）

**示例值**："深圳市南山区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line7</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 7（非拉丁语系的本地文字）

**示例值**："南京市鼓楼区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line8</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 8（非拉丁语系的本地文字）

**示例值**："杭州市滨江区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line9</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 9（非拉丁语系的本地文字）

**示例值**："郑州市中原区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >postal_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	邮政编码

**示例值**："611530"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >address_types</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	地址类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：address
- custom_api_name：address_type

**示例值**：["home_address"]

**数据校验规则**：

- 长度范围：`1` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	主要地址

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	公开地址

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >city_id_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	城市，可以通过接口[查询城市信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-city/search)获取详情

**示例值**："6863333254578046471"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >district_id_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	区/县，可以通过接口[查询区/县信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-district/search)获取详情

**示例值**："6863333516579440141"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >resident_status_specification</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	居民纳税身份说明

**示例值**："文本内容，对纳税身份的补充说明信息"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >year_resident_tax</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	年度

**示例值**："2006-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >born_country_region</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	出生国家/地区，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >is_disabled</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否残疾

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >disable_card_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	残疾证号

**示例值**："身份证号+残疾类型（1-7）+ 残疾程度分级（1-4）+[补发编号]"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >is_old_alone</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否孤老

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >is_martyr_family</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否烈属

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >martyr_card_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	烈属证号

**示例值**："00001"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >dependent_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dependent_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	家庭成员
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >relationship</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	关系，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：dependent
- custom_api_name：relationship_with_dependent

**示例值**："parent"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >gender</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	性别，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：dependent
- custom_api_name：gender

**示例值**："male"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >date_of_birth</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	生日

**示例值**："2020-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >national_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >national_id_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	证件号码

**数据校验规则**：

- 长度范围：`1` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >country_region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家 / 地区，可以通过[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)接口获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >national_id_type_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家证件类型，可以通过[批量查询国家证件类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/national_id_type/list)接口获得

**示例值**："6863330041896371725"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >national_id_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	证件号码

**示例值**："1231131333xxxx222"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >issue_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	证件签发日期

**示例值**："2020-04-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >expiration_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	证件到期日期

**示例值**："2020-05-21"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >issued_by</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	证件签发机构

**示例值**："北京市公安局"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >spouses_working_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	配偶工作状态，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：dependent
- custom_api_name：spouses_working_status

**示例值**："working"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_this_person_covered_by_health_insurance</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	包含家属医疗保险

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_this_person_allowed_for_tax_deduction</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	允许家属抵扣税款

**示例值**：false
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >dependent_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	家庭成员姓名

**示例值**："王冰"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employer</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工作单位

**示例值**："海淀区交警大队"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >job</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	岗位信息描述

**示例值**："保安"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >phone</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >phone_for_update</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	电话
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >international_area_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家区号，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：phone
- custom_api_name：international_area_code

**示例值**："86_china"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >phone_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	电话号码

**示例值**："178xxxx1232"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >device_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	设备类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：phone
- custom_api_name：device_type

**示例值**："mobile_phone"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >phone_usage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	电话用途，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：phone
- custom_api_name：phone_usage

**示例值**："home"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	主要电话，若有多个电话，只能有一个电话的「is_primary」为true

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	公开电话

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >address</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >address_for_update</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	联系地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >country_region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家 / 地区，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	主要行政区，可以通过接口[查询省份/行政区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)获得

**示例值**："6863326815667095047"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line1</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 1（非拉丁语系的本地文字）

**示例值**："北京市海淀区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 2（非拉丁语系的本地文字）

**示例值**："上海市杨浦区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line3</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 3（非拉丁语系的本地文字）

**示例值**："北京市房山区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line4</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 4（非拉丁语系的本地文字）

**示例值**："天津滨海高新区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line5</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 5（非拉丁语系的本地文字）

**示例值**："成都市成华区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line6</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 6（非拉丁语系的本地文字）

**示例值**："深圳市南山区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line7</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 7（非拉丁语系的本地文字）

**示例值**："南京市鼓楼区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line8</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 8（非拉丁语系的本地文字）

**示例值**："杭州市滨江区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line9</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 9（非拉丁语系的本地文字）

**示例值**："郑州市中原区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >postal_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	邮政编码

**示例值**："611530"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >address_types</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	地址类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：address
- custom_api_name：address_type

**示例值**：["home_address"]

**数据校验规则**：

- 长度范围：`1` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	主要地址

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	公开地址

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >city_id_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	城市

**示例值**："6863333254578046471"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >district_id_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	区/县

**示例值**："6863333516579440141"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >religion</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	宗教信仰，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：person
- custom_api_name：religion

**示例值**："buddism"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >bank_account_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bank_account_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	银行账号
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >bank_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	银行名称

**示例值**："中国农业银行"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >branch_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	支行名称

**示例值**："中国农业银行支行"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >bank_account_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	银行账号

**示例值**："6231200xxxx01223"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >account_holder</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	开户人姓名

**示例值**："孟十五"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >country_region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	国家/地区 ID，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995745889322510"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >bank_account_usages</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	银行卡用途，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：bank_account
- custom_api_name：bank_account_usage

**示例值**：["payment"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >bank_account_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	银行卡类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：bank_account
- custom_api_name：bank_account_type

**示例值**："checking"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >national_id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >national_id_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	证件账号
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >country_region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家 / 地区，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >national_id_type_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家证件类型，可以通过[批量查询国家证件类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/national_id_type/list)接口获得

**示例值**："6863330041896371725"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >national_id_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	证件号码

**示例值**："1231131333"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >issue_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	证件签发日期

**示例值**："2020-04-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >expiration_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	证件到期日期

**示例值**："2020-05-21"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >issued_by</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	证件签发机构

**示例值**："北京市公安局"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >personal_profile_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >personal_profile_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	个人资料
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >personal_profile_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	资料类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：personal_profile
- custom_api_name: profile_type

**示例值**："profile_type_1_101_101011"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >files</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >file\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	资料文件列表

**数据校验规则**：

- 长度范围：`0` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文件ID，通过[上传文件](../employee/person/upload.md)接口上传文件后，获取文件ID

**示例值**："6655aa1b2ec326f983b91f9d_f9974583040c4b05ae71f92f5df16bbc"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >emergency_contact_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >emergency_contact_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	紧急联系人
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >legal_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	紧急联系人姓名

**示例值**："王冰"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >relationship</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	紧急联系人与本人亲属关系，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：emergency_contact
- custom_api_name：relationship

**示例值**："parent"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >phones</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >phone_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	电话

**数据校验规则**：

- 长度范围：`0` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >international_area_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家区号，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：phone
- custom_api_name：international_area_code

**示例值**："86_china"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >phone_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	电话号码

**示例值**："178xxxx1232"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >device_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	设备类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：phone
- custom_api_name：device_type

**示例值**："mobile_phone"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >phone_usage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	电话用途，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：phone
- custom_api_name：phone_usage

**示例值**："home"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	主要电话，若有多个电话，只能有一个电话的「is_primary」为true

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	公开电话

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >address</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >address_for_update</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >country_region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家 / 地区，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	主要行政区，可以通过接口[查询省份/行政区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)获得

**示例值**："6863326815667095047"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line1</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 1（非拉丁语系的本地文字）

**示例值**："北京市海淀区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 2（非拉丁语系的本地文字）

**示例值**："上海市杨浦区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line3</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 3（非拉丁语系的本地文字）

**示例值**："北京市房山区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line4</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 4（非拉丁语系的本地文字）

**示例值**："天津滨海高新区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line5</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 5（非拉丁语系的本地文字）

**示例值**："成都市成华区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line6</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 6（非拉丁语系的本地文字）

**示例值**："深圳市南山区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line7</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 7（非拉丁语系的本地文字）

**示例值**："南京市鼓楼区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line8</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 8（非拉丁语系的本地文字）

**示例值**："杭州市滨江区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >local_address_line9</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 9（非拉丁语系的本地文字）

**示例值**："郑州市中原区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >postal_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	邮政编码

**示例值**："611530"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >address_types</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	地址类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：address
- custom_api_name：address_type

**示例值**：["home_address"]

**数据校验规则**：

- 长度范围：`1` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	主要地址

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	公开地址

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >city_id_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	城市

**示例值**："6863333254578046471"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >district_id_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	区/县

**示例值**："6863333516579440141"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >email</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >email_for_update</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	邮箱
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >email</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	邮箱地址

**示例值**："1234567@bytedance.com"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	是否为主要邮箱,若有多个邮箱，只能有一个邮箱的「is_primary」为true

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	是否为公开邮箱

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >email_usage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	邮箱用途，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：email
- custom_api_name：email_usage

**示例值**："work"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	主要联系人,若有多个联系人，只能有一个联系人的「is_primary」为true

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >address_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >address_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	联系地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >country_region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	国家 / 地区，可以通过接口[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	主要行政区，可以通过接口[查询省份/行政区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)获得

**示例值**："6863326815667095047"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line1</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 1（非拉丁语系的本地文字）

**示例值**："北京市海淀区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 2（非拉丁语系的本地文字）

**示例值**："上海市杨浦区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line3</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 3（非拉丁语系的本地文字）

**示例值**："北京市房山区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line4</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 4（非拉丁语系的本地文字）

**示例值**："天津滨海高新区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line5</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 5（非拉丁语系的本地文字）

**示例值**："成都市成华区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line6</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 6（非拉丁语系的本地文字）

**示例值**："深圳市南山区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line7</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 7（非拉丁语系的本地文字）

**示例值**："南京市鼓楼区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line8</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 8（非拉丁语系的本地文字）

**示例值**："杭州市滨江区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >local_address_line9</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	地址行 9（非拉丁语系的本地文字）

**示例值**："郑州市中原区"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >postal_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	邮政编码

**示例值**："611530"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >address_types</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	地址类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：address
- custom_api_name：address_type

**示例值**：["home_address"]

**数据校验规则**：

- 长度范围：`1` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	主要地址

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	公开地址

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >city_id_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	城市

**示例值**："6863333254578046471"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >district_id_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	区/县

**示例值**："6863333516579440141"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >marital_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	婚姻状况，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：person
- custom_api_name：marital_status

**示例值**："single"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >ethnicity_race</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	民族 / 种族，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：person
- custom_api_name：ethnicity_race

**示例值**："han"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05)

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >native_region</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	籍贯，可以通过[查询省份/行政区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region_subdivision/search)接口获取

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >hukou_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	户口类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：person_info_chn
- custom_api_name：hukou_type

**示例值**："local_urban_residence"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >hukou_location</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	户口所在地

**示例值**："北京市海淀区北三环西路"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >gender_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	性别，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：dependent
- custom_api_name：gender

**示例值**："male"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >date_of_birth</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	生日

**示例值**："2011-99-99"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >date_entered_workforce</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	参加工作日期

**示例值**："2100-09-09"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >expected_graduate_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	预计毕业日期

**示例值**："2023-01-10"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >citizenship_status_id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	公民身份

**示例值**：["6862995757234914824"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >work_experience</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >work_experience_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工作履历
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >company_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	公司名称

**示例值**："猎豹"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >start_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	开始时间

**示例值**："2015-02-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >end_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	结束时间

**示例值**："2017-02-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >job_title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	岗位

**示例值**："产品经理"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工作描述

**示例值**："app"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >department</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	部门

**示例值**："部门名称"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >education_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >education_info_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	教育经历
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >school_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	学校名称

**示例值**："长安大学"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >education</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	学历，枚举值可通过文档[枚举常量介绍](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/feishu-people-enum-constant)学历（level_of_education）枚举定义获得

**示例值**："phd"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >start_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	开始时间

**示例值**："2017-04-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >end_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	结束时间

**示例值**："2018-04-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_of_study</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	专业

**示例值**："医学影像技术"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offer_info_update</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >offer_info_update</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	更新待入职（prehire）信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >onboarding_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	入职日期

**示例值**："2022-10-08"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >ats_application_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	招聘应用 ID，仅支持飞书招聘 ID，可以通过[获取投递列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/list)接口获取

**示例值**："7140946969586010376"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >onboarding_location_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	入职地点ID，可以通过[批量查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获得

**示例值**："6977976687350924832"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >onboarding_address_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	入职地址ID，可以通过[批量查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获得

**示例值**："6977976687350924832"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >office_location_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	办公地点ID，可以通过[批量查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获得

**示例值**："6977976687350924833"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >office_address_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	办公地址ID，可以通过[批量查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获得

**示例值**："6977976687350924832"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >employment_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	雇佣类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = pre_hire
- custom_api_name = employment_type

**示例值**："employee"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >onboarding_method</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	入职方式，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = pre_hire
- custom_api_name = onboarding_method

**示例值**："onsite"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >work_emails</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >email_for_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工作邮箱，该值是一个list，会全量更新。即使只更新 list 中的某一个元素，也需要把其它元素都完整传值，否则将丢失数据。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >email</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	邮箱地址

**示例值**："1234567@bytedance.com"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_primary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	是否为主要邮箱,若有多个邮箱，只能有一个邮箱的「is_primary」为true

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_public</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	是否为公开邮箱

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >email_usage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	邮箱用途，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = email
- custom_api_name = email_usage

**示例值**："work"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >cost_center_rates</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >job_data_cost_center\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	成本中心分摊信息
- 待废弃，建议使用cost_allocation
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >cost_center_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	成本中心 ID，可以通过[搜索成本中心信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获得

**示例值**："6950635856373745165"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分摊比例，大于0小于等于100的正整数

**示例值**：100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >new_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分摊比例

**示例值**：50.2
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，该值是一个 string list 经转义后的字符串，具体参考请求体示例

**示例值**："[\"Sandy\"]"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >position_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	岗位id，如需获取具体值，请联系人员档案管理员

**示例值**："697797668735092768"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >probation_period</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	试用期时长

**示例值**：6
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >probation_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	试用期开始日期，格式："YYYY-MM-DD"

**示例值**："2022-07-29"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >probation_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	试用期结束日期，格式："YYYY-MM-DD"

**示例值**："2023-04-07"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >contract_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	合同开始日期，格式："YYYY-MM-DD"

**示例值**："2022-10-08"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >contract_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	合同结束日期，格式："YYYY-MM-DD"

**示例值**："2025-10-07"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >contract_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	合同类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：pre_hire
- custom_api_name：contract_type

**示例值**："internship_agreement"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >duration_type_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	期限类型， 枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：pre_hire
- custom_api_name：duration_type

**示例值**："fixed_term"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >signing_type_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	签订类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：pre_hire
- custom_api_name：signing_type

**示例值**："new"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >worker_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工号

**示例值**："DDD00001"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >check_in_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	签到日期，格式："YYYY-MM-DD"

**示例值**："2024-12-31"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >check_in_method</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	签到方式，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可：
- object_api_name：pre_hire
- custom_api_name：onboarding_method

**示例值**："onsite"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	公司主体，可以通过[批量查询公司](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询

**示例值**："6738317738688661772"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >work_shift</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	排班，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = pre_hire
- custom_api_name = work_shift

**示例值**："work_shift"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >recruitment_type_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	招聘类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = pre_hire
- custom_api_name = recruitment_type

**示例值**："experienced_professionals"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >compensation_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	薪资类型，枚举值可查询[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取，按如下参数查询即可： 
- object_api_name = pre_hire
- custom_api_name = compensation_type

**示例值**："hourly"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >pay_group_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	薪资组，如需获取具体值，请联系人员档案管理员

**示例值**："6977976687350924833"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >offer_hr_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Offer HR 雇佣ID，可以通过[批量查询员工信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口获取

**示例值**："7032210902531327521"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >job_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	职务 ID，可以通过[批量查询职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口获取

**示例值**："6977976735715378724"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >job_family_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	序列 ID，可以通过[批量查询序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)接口获取

**示例值**："6977972856625939999"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >job_level_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	职级 ID，可以通过[批量查询职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)接口获取

**示例值**："6977971894960145950"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >job_grade_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	职等ID，可以通过[查询职等](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口获取

**示例值**："6738317738688661772"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >employee_type_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	人员类型 ID，可以通过接口[批量查询人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)获取

**示例值**："6977973225846343171"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >employee_subtype_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	人员子类型

**示例值**："xxx"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >direct_leader_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	直属上级，可以通过[批量查询员工信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get)接口获取

**示例值**："7032210902531327521"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >dotted_line_manager_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	虚线上级，可以通过[搜索员工信息](https://open.feishu.cn/document/server-docs/corehr-v1/employee/search)接口获取详情
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)

**示例值**："xxx"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >department_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	部门 ID，可以通过[批量查询部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口获取

**示例值**："7147562782945478177"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >social_security_city</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	社保城市ID，可以通过[批量查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获得

**示例值**："6977976687350924833"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >work_location_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工作地点ID，可以通过[批量查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获得

**示例值**："6977976687350924833"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >working_calendar</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工作日历，可以通过[查询日历信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query)接口获得

**示例值**："6890452208593372141"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >working_hours_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工时制度，可以通过[批量查询工时制度](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口获得

**示例值**："6890452208593372679"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >seniority_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	司龄起算日期

**示例值**："2022-10-08"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >seniority_adjust_information_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >prehire_seniority_adjust_information_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	司龄调整信息
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >seniority_adjustment</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	调整值
- 精确度：两位小数
- 单位：年
- 自动计算逻辑：如果这个值为空，司龄调整的开始日期和结束日期均不为空，会自动计算出调整值

**示例值**：0.5

**数据校验规则**：

- 取值范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >seniority_adjustment_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	调整类型
- 可通过[【获取字段详情】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口查询，查询参数如下：
  - object_api_name：seniority_adjust_information
  - custom_api_name：seniority_adjustment_type

**示例值**："增加"

**可选值有**：
<md-enum>
<md-enum-item key="decrease" >减少</md-enum-item>
<md-enum-item key="increase" >增加</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >reasons_for_seniority_adjustment</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	司龄调整原因

**示例值**："工厂停产需要减去半年工龄"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	开始日期
- 格式： yyyy-mm-dd

**示例值**："2024-05-19"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	结束日期
- 格式： yyyy-mm-dd

**示例值**："2024-11-18"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段名

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >notice_period_probation_voluntary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >notice_period_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	试用期内通知期（主动离职)
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)

**示例值**：xxx
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >wk_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	ID

**示例值**："4698019107896524633"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	数值

**示例值**：1

**数据校验规则**：

- 取值范围：`1` ～ `65535`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value_unit</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	单位

**示例值**："月"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >notice_period_probation_involuntary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >notice_period_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	试用期内通知期（被动离职）
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)

**示例值**：xxx
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >wk_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	ID

**示例值**："4698019107896524633"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	数值

**示例值**：1

**数据校验规则**：

- 取值范围：`1` ～ `65535`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value_unit</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	单位

**示例值**："月"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >notice_period_positive_voluntary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >notice_period_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	转正后通知期（主动离职）
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)

**示例值**：xxx
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >wk_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	ID

**示例值**："4698019107896524633"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	数值

**示例值**：1

**数据校验规则**：

- 取值范围：`1` ～ `65535`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value_unit</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	单位

**示例值**："月"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >notice_period_positive_involuntary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >notice_period_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	转正后通知期（被动离职）
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)

**示例值**：xxx
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >wk_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	ID

**示例值**："4698019107896524633"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	数值

**示例值**：1

**数据校验规则**：

- 取值范围：`1` ～ `65535`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >value_unit</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	单位

**示例值**："月"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >condition_worker</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否外部人员

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >company_sponsored_visa</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	需要公司办理签证

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >weekly_working_hours_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	周工作时长（单位：小时）

**示例值**：8.5
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >work_station</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工位

**示例值**："5-1-2"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >service_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任职公司，可以通过[批量查询公司](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询

**示例值**："6738317738688661772"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >non_compete_covenant</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否包含竞业条款

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >pathway</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	通道

**示例值**："7460865381179115052"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >default_cost_center</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >prehire_default_cost_center_update</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	默认成本中心
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >cost_center_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	成本中心 ID，可以通过[搜索成本中心信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获得

**示例值**："6950635856373745165"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_herit</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	是否继承岗位/部门的默认成本中心

**示例值**：false
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >cost_allocation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cost_allocation</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	成本分摊
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >effective_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分摊生效日期

**示例值**："2025-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >expiration_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分摊失效日期

**示例值**："2025-02-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >cost_center_rates</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >job_data_cost_center\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	成本分摊信息

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >cost_center_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	成本中心 ID，可以通过[搜索成本中心信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获得

**示例值**："6950635856373745165"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分摊比例(整数)

**示例值**：100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >new_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分摊比例

**示例值**：50.2
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >reuse_feishu_account</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否复用飞书账号，支持传入“reuse”或者“not_resue”，当字段为“reuse”时，需要传入reused_feishu_account_id
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)

**示例值**："reuse"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >reused_feishu_account_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	复用的飞书账号，仅支持Lark Union ID，可以通过[搜索员工信息
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/directory-v1/employee/search)接口获取
- 功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)

**示例值**："on_773dd2c4d14c5c980a4d89a2da5c86d3"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >standard_update_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	指定需要更新的系统字段，只支持最多下钻一层，格式如下：
 - basic_info_update字段：basic_info_update.names（对name整体进行覆盖更新）；basic_info_update.emails（对邮箱整体进行更新）
 - offer_info_update字段：offer_info_update.onboarding_method

注意，如果指定了要更新的系统字段但是没有在结构体中传对应的值，那么就会清空该字段的值

**示例值**：["basic_info_update.names"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >custom_update_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	指定需要更新的pre_hire对象上的自定义字段，可以通过[获取自定义字段列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query)接口获得

注意：如果指定了要更新的自定义字段但是没有在结构体中传对应的值，那么就会清空该字段的值

**示例值**：["custom_field1__c"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >person_custom_update_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	指定需要更新的person对象上的自定义字段，可以通过[获取自定义字段列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query)接口获得

注意：如果指定了要更新的自定义字段但是没有在结构体中传对应的值，那么就会清空该字段的值

**示例值**：["custom_field1__c"]
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "basic_info_update": {
        "names": [
            {
                "full_name": "李一一",
                "first_name": "一",
                "middle_name": "一",
                "name_primary": "李",
                "local_first_name": "一",
                "local_middle_name": "一",
                "local_primary": "李",
                "custom_local_name": "李一一",
                "custom_western_name": "YiyiLi",
                "country_region": "6862995757234914824",
                "name_type": "legal_name",
                "additional_name": "别名"
            }
        ],
        "phones": [
            {
                "international_area_code": "86_china",
                "phone_number": "178xxxx1234",
                "device_type": "mobile_phone",
                "phone_usage": "work",
                "is_primary": true,
                "is_public": true
            }
        ],
        "emails": [
            {
                "email": "1234567@bytedance.com",
                "is_primary": true,
                "is_public": true,
                "email_usage": "work"
            }
        ],
        "nationality_v2_id": "6862995757234914824",
        "additional_nationality_id_list": [
            "6862995757234914824"
        ],
        "resident_tax_list": [
            {
                "tax_country_region": "6862995757234914824",
                "resident_status": "tax_residence",
                "tax_address": {
                    "country_region_id": "6862995757234914824",
                    "region_id": "6863326815667095047",
                    "local_address_line1": "北京市海淀区",
                    "local_address_line2": "上海市杨浦区",
                    "local_address_line3": "北京市房山区",
                    "local_address_line4": "天津滨海高新区",
                    "local_address_line5": "成都市成华区",
                    "local_address_line6": "深圳市南山区",
                    "local_address_line7": "南京市鼓楼区",
                    "local_address_line8": "杭州市滨江区",
                    "local_address_line9": "郑州市中原区",
                    "postal_code": "611530",
                    "address_types": [
                        "home_address"
                    ],
                    "is_primary": true,
                    "is_public": true,
                    "city_id_v2": "6863333254578046471",
                    "district_id_v2": "6863333516579440141"
                },
                "resident_status_specification": "文本内容，对纳税身份的补充说明信息",
                "year_resident_tax": "2006-01-01",
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "Sandy"
                    }
                ]
            }
        ],
        "born_country_region": "6862995757234914824",
        "is_disabled": true,
        "disable_card_number": "身份证号+残疾类型（1-7）+ 残疾程度分级（1-4）+[补发编号]",
        "is_old_alone": true,
        "is_martyr_family": true,
        "martyr_card_number": "00001",
        "dependent_list": [
            {
                "relationship": "parent",
                "gender": "male",
                "date_of_birth": "2020-01-01",
                "national_ids": [
                    {
                        "country_region_id": "6862995757234914824",
                        "national_id_type_id": "6863330041896371725",
                        "national_id_number": "1231131333xxxx222",
                        "issue_date": "2020-04-01",
                        "expiration_date": "2020-05-21",
                        "issued_by": "北京市公安局",
                        "custom_fields": [
                            {
                                "field_name": "name",
                                "value": "Sandy"
                            }
                        ]
                    }
                ],
                "spouses_working_status": "working",
                "is_this_person_covered_by_health_insurance": true,
                "is_this_person_allowed_for_tax_deduction": false,
                "dependent_name": "王冰",
                "employer": "海淀区交警大队",
                "job": "保安",
                "phone": {
                    "international_area_code": "86_china",
                    "phone_number": "178xxxx1232",
                    "device_type": "mobile_phone",
                    "phone_usage": "home",
                    "is_primary": true,
                    "is_public": true
                },
                "address": {
                    "country_region_id": "6862995757234914824",
                    "region_id": "6863326815667095047",
                    "local_address_line1": "北京市海淀区",
                    "local_address_line2": "上海市杨浦区",
                    "local_address_line3": "北京市房山区",
                    "local_address_line4": "天津滨海高新区",
                    "local_address_line5": "成都市成华区",
                    "local_address_line6": "深圳市南山区",
                    "local_address_line7": "南京市鼓楼区",
                    "local_address_line8": "杭州市滨江区",
                    "local_address_line9": "郑州市中原区",
                    "postal_code": "611530",
                    "address_types": [
                        "home_address"
                    ],
                    "is_primary": true,
                    "is_public": true,
                    "city_id_v2": "6863333254578046471",
                    "district_id_v2": "6863333516579440141"
                },
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "Sandy"
                    }
                ]
            }
        ],
        "religion": "buddism",
        "bank_account_list": [
            {
                "bank_name": "中国农业银行",
                "branch_name": "中国农业银行支行",
                "bank_account_number": "6231200xxxx01223",
                "account_holder": "孟十五",
                "country_region_id": "6862995745889322510",
                "bank_account_usages": [
                    "payment"
                ],
                "bank_account_type": "checking",
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "Sandy"
                    }
                ]
            }
        ],
        "national_id_list": [
            {
                "country_region_id": "6862995757234914824",
                "national_id_type_id": "6863330041896371725",
                "national_id_number": "1231131333",
                "issue_date": "2020-04-01",
                "expiration_date": "2020-05-21",
                "issued_by": "北京市公安局",
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "Sandy"
                    }
                ]
            }
        ],
        "personal_profile_list": [
            {
                "personal_profile_type": "profile_type_1_101_101011",
                "files": [
                    {
                        "id": "6655aa1b2ec326f983b91f9d_f9974583040c4b05ae71f92f5df16bbc"
                    }
                ]
            }
        ],
        "emergency_contact_list": [
            {
                "legal_name": "王冰",
                "relationship": "parent",
                "phones": [
                    {
                        "international_area_code": "86_china",
                        "phone_number": "178xxxx1232",
                        "device_type": "mobile_phone",
                        "phone_usage": "home",
                        "is_primary": true,
                        "is_public": true
                    }
                ],
                "address": {
                    "country_region_id": "6862995757234914824",
                    "region_id": "6863326815667095047",
                    "local_address_line1": "北京市海淀区",
                    "local_address_line2": "上海市杨浦区",
                    "local_address_line3": "北京市房山区",
                    "local_address_line4": "天津滨海高新区",
                    "local_address_line5": "成都市成华区",
                    "local_address_line6": "深圳市南山区",
                    "local_address_line7": "南京市鼓楼区",
                    "local_address_line8": "杭州市滨江区",
                    "local_address_line9": "郑州市中原区",
                    "postal_code": "611530",
                    "address_types": [
                        "home_address"
                    ],
                    "is_primary": true,
                    "is_public": true,
                    "city_id_v2": "6863333254578046471",
                    "district_id_v2": "6863333516579440141"
                },
                "email": {
                    "email": "1234567@bytedance.com",
                    "is_primary": true,
                    "is_public": true,
                    "email_usage": "work"
                },
                "is_primary": true,
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "Sandy"
                    }
                ]
            }
        ],
        "address_list": [
            {
                "country_region_id": "6862995757234914824",
                "region_id": "6863326815667095047",
                "local_address_line1": "北京市海淀区",
                "local_address_line2": "上海市杨浦区",
                "local_address_line3": "北京市房山区",
                "local_address_line4": "天津滨海高新区",
                "local_address_line5": "成都市成华区",
                "local_address_line6": "深圳市南山区",
                "local_address_line7": "南京市鼓楼区",
                "local_address_line8": "杭州市滨江区",
                "local_address_line9": "郑州市中原区",
                "postal_code": "611530",
                "address_types": [
                    "home_address"
                ],
                "is_primary": true,
                "is_public": true,
                "city_id_v2": "6863333254578046471",
                "district_id_v2": "6863333516579440141"
            }
        ],
        "marital_status": "single",
        "ethnicity_race": "han",
        "custom_fields": [
            {
                "field_name": "name",
                "value": "Sandy"
            }
        ],
        "native_region": "6862995757234914824",
        "hukou_type": "local_urban_residence",
        "hukou_location": "北京市海淀区北三环西路",
        "gender_id": "male",
        "date_of_birth": "2011-99-99",
        "date_entered_workforce": "2100-09-09",
        "expected_graduate_date": "2023-01-10",
        "citizenship_status_id_list": [
            "6862995757234914824"
        ],
        "work_experience": [
            {
                "company_name": "猎豹",
                "start_time": "2015-02-01",
                "end_time": "2017-02-01",
                "job_title": "产品经理",
                "description": "app",
                "department": "部门名称"
            }
        ],
        "education_info": [
            {
                "school_name": "长安大学",
                "education": "phd",
                "start_time": "2017-04-01",
                "end_time": "2018-04-01",
                "field_of_study": "医学影像技术"
            }
        ]
    },
    "offer_info_update": {
        "onboarding_date": "2022-10-08",
        "ats_application_id": "7140946969586010376",
        "onboarding_location_id": "6977976687350924832",
        "onboarding_address_id": "6977976687350924832",
        "office_location_id": "6977976687350924833",
        "office_address_id": "6977976687350924832",
        "employment_type": "employee",
        "onboarding_method": "onsite",
        "work_emails": [
            {
                "email": "1234567@bytedance.com",
                "is_primary": true,
                "is_public": true,
                "email_usage": "work"
            }
        ],
        "cost_center_rates": [
            {
                "cost_center_id": "6950635856373745165",
                "rate": 100,
                "new_rate": 50.2
            }
        ],
        "custom_fields": [
            {
                "field_name": "name",
                "value": "[\"Sandy\"]"
            }
        ],
        "position_id": "697797668735092768",
        "probation_period": 6,
        "probation_start_date": "2022-07-29",
        "probation_end_date": "2023-04-07",
        "contract_start_date": "2022-10-08",
        "contract_end_date": "2025-10-07",
        "contract_type": "internship_agreement",
        "duration_type_id": "fixed_term",
        "signing_type_id": "new",
        "worker_id": "DDD00001",
        "check_in_time": "2024-12-31",
        "check_in_method": "onsite",
        "company": "6738317738688661772",
        "work_shift": "work_shift",
        "recruitment_type_id": "experienced_professionals",
        "compensation_type": "hourly",
        "pay_group_id": "6977976687350924833",
        "offer_hr_id": "7032210902531327521",
        "job_id": "6977976735715378724",
        "job_family_id": "6977972856625939999",
        "job_level_id": "6977971894960145950",
        "job_grade_id": "6738317738688661772",
        "employee_type_id": "6977973225846343171",
        "employee_subtype_id": "xxx",
        "direct_leader_id": "7032210902531327521",
        "dotted_line_manager_id": "xxx",
        "department_id": "7147562782945478177",
        "social_security_city": "6977976687350924833",
        "work_location_id": "6977976687350924833",
        "working_calendar": "6890452208593372141",
        "working_hours_type": "6890452208593372679",
        "seniority_date": "2022-10-08",
        "seniority_adjust_information_list": [
            {
                "seniority_adjustment": 0.5,
                "seniority_adjustment_type": "增加",
                "reasons_for_seniority_adjustment": "工厂停产需要减去半年工龄",
                "start_date": "2024-05-19",
                "end_date": "2024-11-18",
                "custom_fields": [
                    {
                        "field_name": "name",
                        "value": "Sandy"
                    }
                ]
            }
        ],
        "notice_period_probation_voluntary": {
            "wk_id": "4698019107896524633",
            "value": 1,
            "value_unit": "月"
        },
        "notice_period_probation_involuntary": {
            "wk_id": "4698019107896524633",
            "value": 1,
            "value_unit": "月"
        },
        "notice_period_positive_voluntary": {
            "wk_id": "4698019107896524633",
            "value": 1,
            "value_unit": "月"
        },
        "notice_period_positive_involuntary": {
            "wk_id": "4698019107896524633",
            "value": 1,
            "value_unit": "月"
        },
        "condition_worker": true,
        "company_sponsored_visa": true,
        "weekly_working_hours_v2": 8.5,
        "work_station": "5-1-2",
        "service_company": "6738317738688661772",
        "non_compete_covenant": true,
        "pathway": "7460865381179115052",
        "default_cost_center": {
            "cost_center_id": "6950635856373745165",
            "is_herit": false
        },
        "cost_allocation": {
            "effective_time": "2025-01-01",
            "expiration_time": "2025-02-01",
            "cost_center_rates": [
                {
                    "cost_center_id": "6950635856373745165",
                    "rate": 100,
                    "new_rate": 50.2
                }
            ]
        },
        "reuse_feishu_account": "reuse",
        "reused_feishu_account_id": "on_773dd2c4d14c5c980a4d89a2da5c86d3"
    },
    "standard_update_fields": [
        "basic_info_update.names"
    ],
    "custom_update_fields": [
        "custom_field1__c"
    ],
    "person_custom_update_fields": [
        "custom_field1__c"
    ]
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
	<md-text type="field-name" >pre_hire_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	待入职ID
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
        "pre_hire_id": "7345005664477775407"
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
  <md-td>1161000</md-td>
  <md-td>系统错误</md-td>
  <md-td>系统出现问题，如需帮助，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161001</md-td>
  <md-td>职级无效</md-td>
  <md-td>请填写有效的职级</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161002</md-td>
  <md-td>序列无效</md-td>
  <md-td>请填写有效的序列</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161003</md-td>
  <md-td>职务无效</md-td>
  <md-td>请填写有效的职务</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161004</md-td>
  <md-td>Offer HR 无效</md-td>
  <md-td>请填写有效的 Offer HR</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161005</md-td>
  <md-td>直属上级无效</md-td>
  <md-td>请填写有效的直属上级</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161006</md-td>
  <md-td>入职地点无效</md-td>
  <md-td>请填写有效的入职地点</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161007</md-td>
  <md-td>办公地点无效</md-td>
  <md-td>请填写有效的办公地点</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161008</md-td>
  <md-td>招聘类型无效</md-td>
  <md-td>请填写有效的招聘类型</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161009</md-td>
  <md-td>人员类型无效</md-td>
  <md-td>请填写有效的人员类型</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161010</md-td>
  <md-td>雇佣类型无效</md-td>
  <md-td>请填写有效的雇佣类型</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161011</md-td>
  <md-td>期限类型无效</md-td>
  <md-td>请填写有效的期限类型</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161012</md-td>
  <md-td>签订类型无效</md-td>
  <md-td>请填写有效的签订类型</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161013</md-td>
  <md-td>社保城市无效</md-td>
  <md-td>请填写有效的社保城市</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161014</md-td>
  <md-td>公司主体无效</md-td>
  <md-td>请填写有效的公司主体</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161015</md-td>
  <md-td>部门无效</md-td>
  <md-td>请填写有效的部门</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161016</md-td>
  <md-td>证件号码和在职人员重复</md-td>
  <md-td>请检查证件号码是否和在职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161018</md-td>
  <md-td>合同类型无效</md-td>
  <md-td>请填写有效的合同类型</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1167037</md-td>
  <md-td>个人电话和在职人员重复</md-td>
  <md-td>请检查个人电话是否和在职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161019</md-td>
  <md-td>成本中心内容重复</md-td>
  <md-td>请检查成本中心</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161020</md-td>
  <md-td>成本中心分摊比例必须大于0小于等于100</md-td>
  <md-td>请检查成本中心分摊比例</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161021</md-td>
  <md-td>成本中心数据不完整</md-td>
  <md-td>请填写完整的成本中心数据</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161022</md-td>
  <md-td>成本中心无效</md-td>
  <md-td>请确认填写的是有效的成本中心</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161023</md-td>
  <md-td>成本中心的分摊比例之和需等于 100%</md-td>
  <md-td>成本中心的分摊比例之和需等于 100%</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161024</md-td>
  <md-td>成本中心被停用</md-td>
  <md-td>成本中心被停用</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161025</md-td>
  <md-td>成本中心将被停用</md-td>
  <md-td>成本中心将被停用</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161026</md-td>
  <md-td>个人邮箱和在职人员重复</md-td>
  <md-td>请检查个人邮箱是否和在职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161027</md-td>
  <md-td>个人邮箱和待入职人员重复</md-td>
  <md-td>请检查个人邮箱是否和待入职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161028</md-td>
  <md-td>手机号和在职人员重复</md-td>
  <md-td>请检查个人电话是否和在职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161029</md-td>
  <md-td>手机号和待入职人员重复</md-td>
  <md-td>请检查个人电话是否和待入职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161030</md-td>
  <md-td>Offer id 不存在</md-td>
  <md-td>请检查 Offer id</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161031</md-td>
  <md-td>证件号码和待入职人员重复</md-td>
  <md-td>请检查证件号码是否和待入职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161032</md-td>
  <md-td>国际区号无效</md-td>
  <md-td>请填写有效的国际区号</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161033</md-td>
  <md-td>手机号格式有误</md-td>
  <md-td>请检查手机号</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161034</md-td>
  <md-td>工作邮箱格式有误</md-td>
  <md-td>请检查工作邮箱</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161035</md-td>
  <md-td>工作邮箱域名有误</md-td>
  <md-td>请检查工作邮箱域名</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161036</md-td>
  <md-td>工作邮箱和在职人员重复</md-td>
  <md-td>请检查工作邮箱是否和在职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161037</md-td>
  <md-td>工作邮箱和待入职人员重复</md-td>
  <md-td>请检查工作邮箱是否和待入职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161038</md-td>
  <md-td>工作邮箱和离职人员重复</md-td>
  <md-td>请检查工作邮箱是否和离职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161039</md-td>
  <md-td>地点用途有误</md-td>
  <md-td>请检查填写地点的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161040</md-td>
  <md-td>入职地址的用途有误</md-td>
  <md-td>请检查入职地址的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161041</md-td>
  <md-td>入职地点的用途错误</md-td>
  <md-td>请检查入职地点的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161042</md-td>
  <md-td>办公地址的用途有误</md-td>
  <md-td>请检查办公地址的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161043</md-td>
  <md-td>办公地点的用途有误</md-td>
  <md-td>请检查办公地点的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161044</md-td>
  <md-td>工作地点的用途有误</md-td>
  <md-td>请检查工作地点的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161045</md-td>
  <md-td>社保城市用途错误</md-td>
  <md-td>请检查社保城市的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161046</md-td>
  <md-td>社保城市用途错误</md-td>
  <md-td>请检查社保城市的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161047</md-td>
  <md-td>公积金缴纳地地点用途错误</md-td>
  <md-td>请检查公积金缴纳地的用途</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161048</md-td>
  <md-td>工号和待入职人员重复</md-td>
  <md-td>请检查工号是否和待入职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161049</md-td>
  <md-td>工号格式错误</md-td>
  <md-td>请检查工号</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161050</md-td>
  <md-td>自动编码规则已启用，无法填写工号</md-td>
  <md-td>自动编码规则已启用，无法填写工号</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161051</md-td>
  <md-td>入职地址和入职地点没有关联关系</md-td>
  <md-td>输入的入职地址和入职地点之间不存在层级关系，请前往「组织管理-地点」中确认后并重新填写信息</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161052</md-td>
  <md-td>办公地址和办公地点没有关联关系</md-td>
  <md-td>输入的办公地址和办公地点之间不存在层级关系，请前往「组织管理-地点」中确认后并重新填写信息</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161053</md-td>
  <md-td>办公地址和工作地点没有关联关系</md-td>
  <md-td>输入的办公地址和工作地点之间不存在层级关系，请前往「组织管理-地点」中确认后并重新填写信息</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161054</md-td>
  <md-td>办公地点和工作地点没有关联关系</md-td>
  <md-td>输入的办公地点和工作地点之间不存在层级关系，请前往「组织管理-地点」中确认后并重新填写信息</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161055</md-td>
  <md-td>办公地址、办公地点和工作地点没有关联关系</md-td>
  <md-td>输入的办公地址、办公地点和工作地点之间不存在层级关系，请前往「组织管理-地点」中确认后并重新填写信息</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161056</md-td>
  <md-td>部门使用职务，职务需必填</md-td>
  <md-td>部门使用职务，职务需必填</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161057</md-td>
  <md-td>部门无需使用职务，职务需为空值</md-td>
  <md-td>部门无需使用职务，职务需为空值</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161063</md-td>
  <md-td>编制规划超编</md-td>
  <md-td>编制规划超编</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161064</md-td>
  <md-td>根据当前的自动编码规则，无法生成工号。请前往「设置-人事设置-自动编码设置」中修改规则</md-td>
  <md-td>根据当前的自动编码规则，无法生成工号。请前往「设置-人事设置-自动编码设置」中修改规则</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161065</md-td>
  <md-td>工号生成失败，请重试或者联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
  <md-td>工号生成失败，请重试或者联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161066</md-td>
  <md-td>公司和人员类型为空，无法根据自动编码生成工号</md-td>
  <md-td>公司和人员类型为空，无法根据自动编码生成工号</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161068</md-td>
  <md-td>职务失效</md-td>
  <md-td>请填写有效的职务</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161069</md-td>
  <md-td>序列失效</md-td>
  <md-td>请填写有效的序列</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161070</md-td>
  <md-td>职级失效</md-td>
  <md-td>请填写有效的职级</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161071</md-td>
  <md-td>职务和序列不匹配</md-td>
  <md-td>职务和序列不匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161072</md-td>
  <md-td>职务和职级不匹配</md-td>
  <md-td>职务和职级不匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161073</md-td>
  <md-td>职务、序列和职级不匹配</md-td>
  <md-td>职务、序列和职级不匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161074</md-td>
  <md-td>序列和职级不匹配</md-td>
  <md-td>序列和职级不匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161075</md-td>
  <md-td>合同结束日期、合同开始日期和合同时长不一致</md-td>
  <md-td>合同结束日期、合同开始日期和合同时长不一致</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161076</md-td>
  <md-td>其他国籍包含主国籍</md-td>
  <md-td>其他国籍包含主国籍</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161077</md-td>
  <md-td>其他国籍内容重复</md-td>
  <md-td>其他国籍内容重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161078</md-td>
  <md-td>公民身份内容重复</md-td>
  <md-td>公民身份内容重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161079</md-td>
  <md-td>其他国籍无效</md-td>
  <md-td>请填写有效的其他国籍</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161080</md-td>
  <md-td>公民身份无效</md-td>
  <md-td>请填写有效的公民身份</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161092</md-td>
  <md-td>异常信息检查失败</md-td>
  <md-td>异常信息检查失败</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161097</md-td>
  <md-td>权限被拒绝，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
  <md-td>权限被拒绝，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161108</md-td>
  <md-td>待入职人员已完成入职，无法更新信息</md-td>
  <md-td>待入职人员已完成入职，无法更新信息</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161109</md-td>
  <md-td>职等失效</md-td>
  <md-td>请填写有效的职等</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161112</md-td>
  <md-td>部门使用岗位，岗位需必填</md-td>
  <md-td>部门使用岗位，岗位需必填</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161113</md-td>
  <md-td>岗位不匹配</md-td>
  <md-td>「部门、直属上级、虚线上级、职务、序列、职级、职等、工作地点、工时制度、人员类型」中存在与所选岗位不匹配的信息，请重新选择</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161114</md-td>
  <md-td>岗位在入职日期及其之后不存在</md-td>
  <md-td>岗位在入职日期及其之后不存在</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161115</md-td>
  <md-td>岗位在入职日期及其之后存在停用版本</md-td>
  <md-td>岗位在入职日期及其之后存在停用版本</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161116</md-td>
  <md-td>更新待入职获取锁失败</md-td>
  <md-td>重试更新待入职</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161142</md-td>
  <md-td>通知期信息不合法</md-td>
  <md-td>通知期信息不合法</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161143</md-td>
  <md-td>通知期信息无效，不可编辑</md-td>
  <md-td>通知期信息无效，不可编辑</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161144</md-td>
  <md-td>通知期规则不匹配</md-td>
  <md-td>通知期规则不匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161145</md-td>
  <md-td>你已填写默认成本中心（手动选择），“是否继承岗位/部门的默认成本中心”必须为空或者“否”</md-td>
  <md-td>你已填写默认成本中心（手动选择），“是否继承岗位/部门的默认成本中心”必须为空或者“否”</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161146</md-td>
  <md-td>是否继承岗位/部门的默认成本中心”填写为否，请补充默认成本中心（手动选择）</md-td>
  <md-td>是否继承岗位/部门的默认成本中心”填写为否，请补充默认成本中心（手动选择）</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161147</md-td>
  <md-td>入职日期缺失，无法补充默认成本中心或者成本分摊的生效日期</md-td>
  <md-td>入职日期缺失，无法补充默认成本中心或者成本分摊的生效日期</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161148</md-td>
  <md-td>部门/岗位上的默认成本中心为空，无法继承</md-td>
  <md-td>部门/岗位上的默认成本中心为空，无法继承</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161149</md-td>
  <md-td>成本分摊中的成本中心和分摊比例需填写完整</md-td>
  <md-td>成本分摊中的成本中心和分摊比例需填写完整</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




