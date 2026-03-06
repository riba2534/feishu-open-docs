---
title: "批量查询薪资方案"
fullPath: "/uAjLw4CM/ukTMukTMukTM/compensation-v1/plan/list"
updateTime: "1745981687000"
---

# 批量查询薪资方案

- 此接口将返回全部薪资方案信息，包括薪资方案 ID、生效日期、薪资项/薪资统计指标等{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=compensation&version=v1&resource=plan&method=list)

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
      <md-td>https://open.feishu.cn/open-apis/compensation/v1/plans</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[10 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="corehr:compensation_plan:read" desc="获取基础薪酬的薪资方案信息" support_app_types="custom" tags="">获取基础薪酬的薪资方案信息</md-perm>
      </md-td>
    </md-tr>
    <md-tr>
      <md-th>
            字段权限要求
      </md-th>
      <md-td>
        <md-alert type="tip" icon="none">
        该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请
        </md-alert>
        <md-perm name="corehr:compensation_plan_detail.indicators:read" desc="获取薪资方案的关联薪资指标" support_app_types="custom" tags="">获取薪资方案的关联薪资指标</md-perm>
        <md-perm name="corehr:compensation_plan_detail.items:read" desc="获取薪资方案的关联薪资项" support_app_types="custom" tags="">获取薪资方案的关联薪资项</md-perm>
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

**示例值**：100

**默认值**：`100`

**数据校验规则**：

- 取值范围：`1` ～ `500`
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

**示例值**：213432123
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
	<md-text type="field-name" >items</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >plan_detail\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资方案信息列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资方案ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >tid</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资方案版本ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资方案名称
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
	薪资方案描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >effective_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资方案生效时间
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >plan_scope</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >plan_scope</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资方案适用范围
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_all</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否全部范围
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >plan_conditions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >plan_condition\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	方案适用范围条件组
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >left_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	适用范围左值

**可选值有**：
<md-enum>
<md-enum-item key="1" >部门</md-enum-item>
<md-enum-item key="2" >部门（包含下级部门）</md-enum-item>
<md-enum-item key="3" >工作地点</md-enum-item>
<md-enum-item key="4" >工作地点（包含下级地点）</md-enum-item>
<md-enum-item key="5" >公司</md-enum-item>
<md-enum-item key="6" >公司（包含下级公司）</md-enum-item>
<md-enum-item key="7" >序列</md-enum-item>
<md-enum-item key="8" >序列（包含子序列）</md-enum-item>
<md-enum-item key="9" >职务</md-enum-item>
<md-enum-item key="10" >职级</md-enum-item>
<md-enum-item key="11" >人员类型</md-enum-item>
<md-enum-item key="12" >招聘类型</md-enum-item>
<md-enum-item key="13" >国家/地区</md-enum-item>
<md-enum-item key="14" >职等</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >operator</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	适用范围操作

**可选值有**：
<md-enum>
<md-enum-item key="1" >包含</md-enum-item>
<md-enum-item key="2" >不包含</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >right_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	- 适用范围左值为：部门、部门（包含下级部门），返回：部门ID，详细信息可以通过[批量查询部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口查询获得

- 适用范围左值为：工作地点、工作地点（包含下级工作地点），返回：工作地点ID，详细信息可以通过[批量查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口查询获得

- 适用范围左值为：公司、公司（包含下级公司），返回：公司ID，详细信息可以通过[通过公司 ID 批量获取公司信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)接口查询获得

- 适用范围左值为：序列、序列（包含子序列），返回：序列ID，详细信息可以通过[通过序列 ID 批量获取序列信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)接口查询获得

- 适用范围左值为：职务，返回：职务ID，详细信息可以通过[批量查询职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口查询获得

- 适用范围左值为：职级，返回：职级ID，详细信息可以通过[通过职级 ID 批量获取职级信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)接口查询获得

- 适用范围左值为：人员类型，返回：人员类型ID，详细信息可以通过[批量查询人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)接口查询获得

- 适用范围左值为：招聘类型，返回：招聘类型

- 适用范围左值为：国家/地区，返回：国家/地区

- 适用范围左值为：职等，返回：职等ID，详细信息可以通过[查询职等](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口查询获得
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >currency_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	币种ID，可通过接口[【查询货币信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search)获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >probation_salary_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	开启试用期薪酬状态
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >plan_items</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >plan_item\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	方案关联的薪资项

**字段权限要求**：
<md-perm name="corehr:compensation_plan_detail.items:read" desc="获取薪资方案的关联薪资项" support_app_types="custom" tags="">获取薪资方案的关联薪资项</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >adjustment_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	定薪方式

**可选值有**：
<md-enum>
<md-enum-item key="manual" >手动输入</md-enum-item>
<md-enum-item key="formula" >公式计算</md-enum-item>
<md-enum-item key="fixed" >固定值</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >item_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资项ID，详细信息可以通过[批量查询薪资项](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/compensation-v1/item/list)接口查询获得
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >plan_item_logic</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >adjustment_logic</md-text>
	</md-dt-td>
	<md-dt-td>
	方案关联薪资项逻辑配置
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >fixed</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	固定值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >formula</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >formula</md-text>
	</md-dt-td>
	<md-dt-td>
	公式配置
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >expr</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	公式表达式
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >formula_params</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >formula_param\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	公式参数列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >ref_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	引用类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >引用薪资项</md-enum-item>
<md-enum-item key="2" >引用薪资指标</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	引用类型ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >probation_discount_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	试用期薪酬类型

**可选值有**：
<md-enum>
<md-enum-item key="percentum" >百分比</md-enum-item>
<md-enum-item key="manual_input" >手动输入</md-enum-item>
<md-enum-item key="none" >不区分试用期和转正薪酬</md-enum-item>
<md-enum-item key="fixed" >固定值</md-enum-item>
<md-enum-item key="formula" >公式计算</md-enum-item>
<md-enum-item key="not_set" >未设置试用期</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >probation_discount_percentum</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	试用期薪酬百分比
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >plan_indicators</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >plan_indicator\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	方案关联的薪资统计指标

**字段权限要求**：
<md-perm name="corehr:compensation_plan_detail.indicators:read" desc="获取薪资方案的关联薪资指标" support_app_types="custom" tags="">获取薪资方案的关联薪资指标</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >indicator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资统计指标ID，详细信息可以通过[批量查询薪资统计指标](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/compensation-v1/indicator/list)接口查询获得
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >plan_indicator_logic</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >adjustment_logic</md-text>
	</md-dt-td>
	<md-dt-td>
	方案关联薪资统计指标逻辑配置
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >fixed</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	固定值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >formula</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >formula</md-text>
	</md-dt-td>
	<md-dt-td>
	公式配置
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >expr</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	公式表达式
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >formula_params</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >formula_param\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	公式参数列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >ref_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	引用类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >引用薪资项</md-enum-item>
<md-enum-item key="2" >引用薪资指标</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	引用类型ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >i18n_names</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	多语言名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语言版本，例如：“zh-CN”、“en-US”
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
	语言名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >i18n_descriptions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	多语言描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语言版本，例如：“zh-CN”、“en-US”
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
	语言名称
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
        "items": [
            {
                "id": "2134193289",
                "tid": "129738122",
                "name": "基本月薪方案",
                "description": "基本月薪方案描述",
                "effective_date": "2022-10-20",
                "plan_scope": {
                    "is_all": false,
                    "plan_conditions": [
                        {
                            "left_type": 7,
                            "operator": 1,
                            "right_value": [
                                "413431223"
                            ]
                        }
                    ]
                },
                "currency_id": "341324121",
                "probation_salary_status": true,
                "plan_items": [
                    {
                        "adjustment_type": "manual",
                        "item_id": "21341234",
                        "plan_item_logic": {
                            "fixed": "60",
                            "formula": {
                                "expr": "${0} +${1}",
                                "formula_params": [
                                    {
                                        "ref_type": 1,
                                        "id": "23143242"
                                    }
                                ]
                            }
                        },
                        "probation_discount_type": "percentum",
                        "probation_discount_percentum": "80.00"
                    }
                ],
                "plan_indicators": [
                    {
                        "indicator_id": "13243432",
                        "plan_indicator_logic": {
                            "fixed": "60",
                            "formula": {
                                "expr": "${0} +${1}",
                                "formula_params": [
                                    {
                                        "ref_type": 1,
                                        "id": "23143242"
                                    }
                                ]
                            }
                        }
                    }
                ],
                "i18n_names": [
                    {
                        "locale": "zh_cn",
                        "value": "中文名称"
                    }
                ],
                "i18n_descriptions": [
                    {
                        "locale": "zh_cn",
                        "value": "中文名称"
                    }
                ]
            }
        ],
        "page_token": "123412344",
        "has_more": true
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
  <md-td>2290001</md-td>
  <md-td>server error</md-td>
  <md-td>服务端异常，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290002</md-td>
  <md-td>param invalid</md-td>
  <md-td>参数异常，请检查参数</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>2290003</md-td>
  <md-td>rpc fail</md-td>
  <md-td>下游服务调用异常，请重试，如重试后仍失败，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




