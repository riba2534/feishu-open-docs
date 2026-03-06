---
title: "获取流程表单数据"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/get"
updateTime: "1714122838000"
---

# 获取流程表单数据

根据流程实例 id（process_id）获取流程表单字段数据，包括表单里的业务字段和自定义字段。仅支持飞书人事、假勤相关业务流程。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v1&resource=process.form_variable_data&method=get)

:::html
<md-alert type="error">

</md-alert>
:::

:::html
<md-alert type="warn">

</md-alert>
:::

:::html
<md-alert type="tip">
建议使用新版本 API 文档。详情参见[获取流程表单数据](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-form_variable_data/get)。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v1/processes/:process_id/form_variable_data</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[100 次/分钟](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="corehr:corehr:readonly" desc="获取核心人事信息" support_app_types="custom,isv" tags="">获取核心人事信息</md-perm>
            <md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv" tags="">获取流程数据</md-perm>
            <md-perm name="corehr:corehr" desc="更新核心人事信息" support_app_types="custom" tags="">更新核心人事信息</md-perm>
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
	<md-text type="field-name" >process_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	流程实例 ID

**示例值**："123456987"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
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
	<md-text type="field-name" >field_variable_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	流程变量
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >variable_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	变量api名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >variable_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bpm_dataengine_i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	变量名称的i18n描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >variable_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_variable_value_info</md-text>
	</md-dt-td>
	<md-dt-td>
	变量值的对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >text_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_text_value</md-text>
	</md-dt-td>
	<md-dt-td>
	文本变量对象
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
	文本类型变量的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >number_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_number_value</md-text>
	</md-dt-td>
	<md-dt-td>
	数值变量对象
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
	数值类型变量的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >date_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_date_value</md-text>
	</md-dt-td>
	<md-dt-td>
	日期变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	日期变量的值，从1970起的天数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >employment_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_employment_value</md-text>
	</md-dt-td>
	<md-dt-td>
	员工变量对象
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
	employmentID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	员工ID 如3158117
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >date_time_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_datetime_value</md-text>
	</md-dt-td>
	<md-dt-td>
	日期时间变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	毫秒的时间戳。注：此字段数据类型为 int64
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >zone</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	时区，+08:00
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >enum_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_enum_value</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举变量对象
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
	枚举值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bpm_dataengine_i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举的名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >desc</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bpm_dataengine_i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举的描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >null_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_null_value</md-text>
	</md-dt-td>
	<md-dt-td>
	空变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >bool_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_bool_value</md-text>
	</md-dt-td>
	<md-dt-td>
	布尔变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	布尔变量的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >department_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_department_value</md-text>
	</md-dt-td>
	<md-dt-td>
	部门变量对象
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
	部门ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >file_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_file_value</md-text>
	</md-dt-td>
	<md-dt-td>
	文件变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >source_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	文件源类型（1BPM; 2主数据）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >file_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文件id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >file_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文件名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >length</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	文件长度
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >mime_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	扩展类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >i18n_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_i18n_value</md-text>
	</md-dt-td>
	<md-dt-td>
	i18n变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bpm_dataengine_i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	i18n值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	对象变量
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
	对象ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >wk_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	主数据apiName
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >list_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_list_value</md-text>
	</md-dt-td>
	<md-dt-td>
	列表对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_list_object\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	列表值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >text_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_text_value</md-text>
	</md-dt-td>
	<md-dt-td>
	文本变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文本类型变量的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >number_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_number_value</md-text>
	</md-dt-td>
	<md-dt-td>
	数值变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	数值类型变量的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >date_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_date_value</md-text>
	</md-dt-td>
	<md-dt-td>
	日期变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	日期变量的值，从1970起的天数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >employment_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_employment_value</md-text>
	</md-dt-td>
	<md-dt-td>
	员工变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	employmentID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	员工ID 如3158117
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >date_time_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_datetime_value</md-text>
	</md-dt-td>
	<md-dt-td>
	日期时间变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	毫秒的时间戳。注：此字段数据类型为 int64
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >zone</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	时区，+08:00
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >enum_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_enum_value</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bpm_dataengine_i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举的名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >desc</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bpm_dataengine_i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举的描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >null_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_null_value</md-text>
	</md-dt-td>
	<md-dt-td>
	空变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >bool_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_bool_value</md-text>
	</md-dt-td>
	<md-dt-td>
	布尔变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	布尔变量的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >department_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_department_value</md-text>
	</md-dt-td>
	<md-dt-td>
	部门变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	部门ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >file_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_file_value</md-text>
	</md-dt-td>
	<md-dt-td>
	文件变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >source_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	文件源类型（1BPM; 2主数据）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >file_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文件id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >file_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文件名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >length</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	文件长度
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >mime_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	扩展类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >i18n_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_i18n_value</md-text>
	</md-dt-td>
	<md-dt-td>
	i18n变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bpm_dataengine_i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	i18n值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为zh_cn，但在实际返回的 JSON Key 中展示为 zh-CN）i18n类型字段，中文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	（基于系统兼容性，该参数名称在文档中展示为en_us，但在实际返回的 JSON Key 中展示为 en-US）i18n类型字段，英文值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	对象变量
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	对象ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >wk_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	主数据apiName
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >record_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_record_value</md-text>
	</md-dt-td>
	<md-dt-td>
	记录对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_record_value_example</md-text>
	</md-dt-td>
	<md-dt-td>
	注：该参数实际为 Map 数据类型，Key 是变量唯一标识，Value 是变量值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >country_region</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_variable_value_info_example</md-text>
	</md-dt-td>
	<md-dt-td>
	这个属性名称是map的key的示例，属性值是map的value的示例，值和外层的variable_value是的一样的结构。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	文本变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	对象ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >wk_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	主数据apiName
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >record_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_record_value</md-text>
	</md-dt-td>
	<md-dt-td>
	记录对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_record_value_example</md-text>
	</md-dt-td>
	<md-dt-td>
	注：该参数实际为 Map 数据类型，Key 是变量唯一标识，Value 是变量值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >country_region</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_variable_value_info_example</md-text>
	</md-dt-td>
	<md-dt-td>
	这个属性名称是map的key的示例，属性值是map的value的示例，值和外层的variable_value是的一样的结构。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >form_field_variable_object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	文本变量对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	对象ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >wk_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	主数据apiName
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
    "data":
    {
        "field_variable_values":
        [
            {
                "variable_api_name": "reason",
                "variable_name":
                {
                    "en-US": "Reason",
                    "zh-CN": "离职原因"
                },
                "variable_value":
                {
                    "enum_value":
                    {
                        "desc": null,
                        "enum_source_id": 123,
                        "enum_source_type": 2,
                        "name":
                        {
                            "en-US": "",
                            "zh-CN": "测试"
                        },
                        "value": "reason_for_offboarding_option96",
                        "wk_api_name": "reason_for_offboarding"
                    }
                }
            },
            {
                "variable_api_name": "offboarding_date",
                "variable_name":
                {
                    "en-US": "Offboarding date",
                    "zh-CN": "离职日期"
                },
                "variable_value":
                {
                    "date_value":
                    {
                        "value": 19265
                    }
                }
            },
            {
                "variable_api_name": "employment",
                "variable_name":
                {
                    "en-US": "Employment",
                    "zh-CN": "员工"
                },
                "variable_value":
                {
                    "employment_value":
                    {
                        "user_id": "123321",
                        "value": "123321"
                    }
                }
            }
        ],
        "process_id": "123321"
    },
    "msg": "",
    "success": true
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
  <md-td>400</md-td>
  <md-td>1160100</md-td>
  <md-td>审批流程不存在</md-td>
  <md-td>确认审批流程ID是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160500</md-td>
  <md-td>服务端内部错误</md-td>
  <md-td>内部错误，建议联系飞书开发平台技术支持</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




