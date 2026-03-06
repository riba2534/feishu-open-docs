---
title: "查询成本分摊报表汇总数据"
fullPath: "/uAjLw4CM/ukTMukTMukTM/payroll-v1/cost_allocation_report/list"
updateTime: "1765505834000"
---

# 查询成本分摊报表汇总数据

根据算薪期间和成本分摊方案id获取成本分摊汇总数据。调用接口前，需在payroll 系统中打开「财务过账」开关，并且完成发布成本分摊报表。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=payroll&version=v1&resource=cost_allocation_report&method=list)

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
      <md-td>https://open.feishu.cn/open-apis/payroll/v1/cost_allocation_reports</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[5 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="payroll:cost_allocation_report:read" desc="获取成本分摊报表汇总数据" support_app_types="custom,isv" tags="">获取成本分摊报表汇总数据</md-perm>
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



### 查询参数
:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 15%;" filters="是,否" >必填</md-dt-th>
      <md-dt-th style="width: 37%;" >描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >page_size</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	分页大小

**示例值**：50

**数据校验规则**：

- 取值范围：`1` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >page_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果

**示例值**：6823630319749592415
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >cost_allocation_plan_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	成本分摊方案ID，通过[批量查询成本分摊方案](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/cost_allocation_plan/list)获取

**示例值**：6823630319749580304
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >pay_period</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	期间，成本分摊数据对应的年月，格式 为yyyy-MM

**示例值**：2023-11
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >report_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	报表类型

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="0" >默认，表示没有开通计提和实发功能时的报表类型，开通计提和实发之后，该类型报表将无法发布。</md-enum-item>
<md-enum-item key="1" >计提</md-enum-item>
<md-enum-item key="2" >实发</md-enum-item>
</md-enum>
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
	<md-text type="field-name" >pay_period</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	期间，成本分摊报表对应的年月
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >page_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >has_more</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否还有更多项
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >cost_allocation_report_names</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	报表名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语种
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
	语种对应的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >cost_allocation_report_datas</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cost_allocation_report_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	汇总数据
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >data_summary_dimensions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >data_summary_dimension\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	数据维度汇总
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >dimension_level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	层级
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >dimension_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	类型：

公司主体 - 1

成本中心 - 2

部门 - 3

薪资组 - 4

人员类型 - 5

雇佣状态 - 6

转正状态 - 7

职务 - 8

序列 - 9

职级 - 10

工时制度 - 11

合同类型 - 12

算薪项 - 13

自定义维度 - 100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >dimension_value_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	维度ID，需要根据dimension_type再次转换，如：当dimension_type为1时，该值表示公司主体的ID。

对应的接口映射如下：

dimension_type = 1 [公司主体](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)

dimension_type = 2 [成本中心](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)

dimension_type = 3 [部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)

dimension_type = 4 [薪资组](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/paygroup/list)

dimension_type = 5 [人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)

dimension_type = 8 [职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)

dimension_type = 9 [序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)

dimension_type = 10 [职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)

dimension_type = 11 [工时制度](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >enum_dimension</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >enum_object</md-text>
	</md-dt-td>
	<md-dt-td>
	算薪项汇总维度时，当算薪项是特定枚举值，会使用该字段返回枚举值ID以及枚举值Key，业务需要获取枚举对象的详情信息，可根据ID去对应的对象中查找，其中枚举对象的映射如下：

 workCalendar [工作日历](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/work_calendar)

 location [地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/location/batch_get)

company [公司主体](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)

costCenter  [成本中心](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)

department [部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)

employeeType [人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)

job [职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)

jobFamily [序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)

jobLevel [职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)

workingHoursType [工时制度](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >enum_value_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举对象ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >enum_key</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举对象
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >dimension_value_lookup_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dimension_value_lookup_info</md-text>
	</md-dt-td>
	<md-dt-td>
	维度引用对象的基础信息，当维度为引用类型字段才会有值，目前支持的引用对象类型见type
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	引用对象类型，类型对应的对象映射包括不仅限：

type = company [公司主体](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)

type = cost_center [成本中心](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)

type = department [部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)

type = pay_group [薪资组](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/paygroup/list)

type = employee_type [人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)

type = job [职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)

type = job_family [序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)

type = job_level [职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)

type = working_hours_type [工时制度](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	引用对象的id，可根据相关API查询到对象的完整信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	引用对象的code，目前下面的对象会有code：

type = company [公司主体](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)

type = cost_center [成本中心](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)

type = department [部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)

type = job [职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)

type = job_family [序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)

type = job_level [职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)

type = location [地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/location/batch_get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >dimension_names</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	维度名称，算薪项、自定义维度使用
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语种
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
	语种对应的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >dimension_titles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	数据维度表头，算薪项、自定义维度使用
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语种
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
	语种对应的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	名称对应的实体id

需要根据dimension_type再次转换，如：当dimension_type为13时，该值表示算薪项的ID。

对应的接口映射如下：

dimension_type = 13 [算薪项](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/acct_item/list)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >compensation_cost_item</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >compensation_cost_item</md-text>
	</md-dt-td>
	<md-dt-td>
	成本项数据
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >number_of_individuals_for_payment</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	发薪人数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >compensation_costs</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >compensation_cost\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	成本项数据
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >compensation_cost_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	成本项值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >i18n_names</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	成本项名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语种
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语种对应的值
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
        "pay_period": "2023-11",
        "page_token": "6823630319749580302",
        "has_more": true,
        "cost_allocation_report_names": [
            {
                "locale": "zh_cn",
                "value": "名称"
            }
        ],
        "cost_allocation_report_datas": [
            {
                "data_summary_dimensions": [
                    {
                        "dimension_level": 1,
                        "dimension_type": 1,
                        "dimension_value_id": "6823630319749580306",
                        "enum_dimension": {
                            "enum_value_id": "7188920315914207276",
                            "enum_key": "company"
                        },
                        "dimension_value_lookup_info": {
                            "type": "work_calendar",
                            "id": "6961286846093788621",
                            "code": "D1230011115"
                        },
                        "dimension_names": [
                            {
                                "locale": "zh_cn",
                                "value": "名称"
                            }
                        ],
                        "dimension_titles": [
                            {
                                "locale": "zh_cn",
                                "value": "名称",
                                "id": "723123123123123213"
                            }
                        ]
                    }
                ],
                "compensation_cost_item": {
                    "number_of_individuals_for_payment": 100,
                    "compensation_costs": [
                        {
                            "compensation_cost_value": "123456.78",
                            "i18n_names": [
                                {
                                    "locale": "zh_cn",
                                    "value": "名称"
                                }
                            ]
                        }
                    ]
                }
            }
        ]
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
  <md-td>2500001</md-td>
  <md-td>unknown error</md-td>
  <md-td>未知错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2500002</md-td>
  <md-td>param is invalid</md-td>
  <md-td>参数错误，请检查参数</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>2500003</md-td>
  <md-td>rpc fail</md-td>
  <md-td>请求调用出错，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>2500004</md-td>
  <md-td>get plan version fail</md-td>
  <md-td>获取成本分摊方案版本出错，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500005</md-td>
  <md-td>report has changed, please fetch again</md-td>
  <md-td>报表已变更，请重新获取。一般为报表拉取过程中新发布了报表。需要不传page_token参数，重新从头拉取</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500006</md-td>
  <md-td>report not found or unpublished</md-td>
  <md-td>报表不存在或者未发布，请检查参数并且联系报表管理员确认发布报表后再尝试</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>2500007</md-td>
  <md-td>report fetch fail</md-td>
  <md-td>获取报表数据失败，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




