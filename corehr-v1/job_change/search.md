---
title: "搜索员工异动信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_change/search"
updateTime: "1757378631000"
---

# 搜索异动信息

搜索异动信息，该接口会按照应用拥有的「员工数据」的权限范围返回数据，请确定在「开发者后台 - 权限管理 - 数据权限」中有申请「员工资源」权限范围{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=job_change&method=search)

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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/job_changes/search</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
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
            <md-perm name="corehr:job_change:read" desc="获取员工异动信息" support_app_types="custom,isv" tags="">获取员工异动信息</md-perm>
            <md-perm name="corehr:job_change:write" desc="读写员工异动信息" support_app_types="custom" tags="">读写员工异动信息</md-perm>
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
        <md-perm name="corehr:contract.company:read" desc="获取合同主体信息" support_app_types="custom,isv" tags="">获取合同主体信息</md-perm>
        <md-perm name="corehr:contract.period:read" desc="获取合同期限信息" support_app_types="custom,isv" tags="">获取合同期限信息</md-perm>
        <md-perm name="corehr:employment.job:read" desc="获取员工的职务信息" support_app_types="custom,isv" tags="">获取员工的职务信息</md-perm>
        <md-perm name="corehr:employment.job_level:read" desc="获取职务级别信息" support_app_types="custom,isv" tags="">获取职务级别信息</md-perm>
        <md-perm name="corehr:job_change.custom_field:read" desc="获取员工异动自定义字段信息" support_app_types="custom,isv" tags="">获取员工异动自定义字段信息</md-perm>
        <md-perm name="corehr:job_change.employment_custom_field:read" desc="获取异动工作信息自定义字段" support_app_types="custom,isv" tags="">获取异动工作信息自定义字段</md-perm>
        <md-perm name="corehr:job_change.pathway:read" desc="读取异动信息中的通道字段信息" support_app_types="custom,isv" tags="">读取异动信息中的通道字段信息</md-perm>
        <md-perm name="corehr:job_change.pathway:write" desc="读写异动信息中的通道字段信息" support_app_types="custom,isv" tags="">读写异动信息中的通道字段信息</md-perm>
        <md-perm name="corehr:job_change.remark:read" desc="获取异动流程备注信息" support_app_types="custom,isv" tags="">获取异动流程备注信息</md-perm>
        <md-perm name="corehr:employment.job_level:write" desc="读写员工的职务级别信息" support_app_types="custom" tags="">读写员工的职务级别信息</md-perm>
        <md-perm name="corehr:contract.period:write" desc="读写合同期限信息" support_app_types="custom" tags="">读写合同期限信息</md-perm>
        <md-perm name="corehr:contract.company:write" desc="读写合同主体信息" support_app_types="custom" tags="">读写合同主体信息</md-perm>
        <md-perm name="corehr:job_change.is_adjust_salary:read" desc="获取异动单据是否调薪字段" support_app_types="custom" tags="">获取异动单据是否调薪字段</md-perm>
        <md-perm name="corehr:employment.job_grade:read" desc="获取职等信息" support_app_types="custom" tags="">获取职等信息</md-perm>
        <md-perm name="corehr:employment.job_grade:write" desc="读写职等信息" support_app_types="custom" tags="">读写职等信息</md-perm>
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
        <md-perm name="corehr:job_change.social_security_city:read" desc="获取异动单据社保字段" support_app_types="custom" tags="">获取异动单据社保字段</md-perm>
        <md-perm name="corehr:job_data.compensation_type:read" desc="获取薪资类型" support_app_types="custom" tags="">获取薪资类型</md-perm>
        <md-perm name="corehr:job_data.service_company:read" desc="获取任职公司" support_app_types="custom" tags="">获取任职公司</md-perm>
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
	分页大小，最大 100

**示例值**：100

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

**示例值**：6891251722631890445
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >user_id_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户 ID 类型

**示例值**：open_id

**可选值有**：
<md-enum>
<md-enum-item key="open_id" >标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)</md-enum-item>
<md-enum-item key="union_id" >标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)</md-enum-item>
<md-enum-item key="user_id" >标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)</md-enum-item>
<md-enum-item key="people_corehr_id" >以飞书人事的 ID 来识别用户</md-enum-item>
</md-enum>

**默认值**：`open_id`

**当值为 `user_id`，字段权限要求**：
<md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >department_id_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	此次调用中使用的部门 ID 类型

**示例值**：open_department_id

**可选值有**：
<md-enum>
<md-enum-item key="open_department_id" >以 open_department_id 来标识部门</md-enum-item>
<md-enum-item key="department_id" >以 department_id 来标识部门</md-enum-item>
<md-enum-item key="people_corehr_department_id" >以 people_corehr_department_id 来标识部门</md-enum-item>
</md-enum>

**默认值**：`open_department_id`
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
	<md-text type="field-name" >employment_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	雇员 ID 列表，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取

**示例值**：["ou_a294793e8fa21529f2a60e3e9de45520"]

**数据校验规则**：

- 最大长度：`30`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_change_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动记录 ID 列表，可通过接口
[搜索异动信息
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_change/search)获取详细信息

**示例值**：["7044427347159746085"]

**数据校验规则**：

- 最大长度：`10`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >statuses</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动状态，多个状态之间为「或」的关系

**示例值**：["Approving"]

**可选值有**：
<md-enum>
<md-enum-item key="Approving" >Approving  审批中</md-enum-item>
<md-enum-item key="Approved" >Approved  审批通过</md-enum-item>
<md-enum-item key="Transformed" >Transformed  已异动</md-enum-item>
<md-enum-item key="Rejected" >Rejected  已拒绝</md-enum-item>
<md-enum-item key="Cancelled" >Cancelled  已撤销</md-enum-item>
<md-enum-item key="NoNeedApproval" >NoNeedApproval  无需审批</md-enum-item>
</md-enum>

**数据校验规则**：

- 最大长度：`10`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >effective_date_start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动生效日期 - 搜索范围开始，需要与effective_date_end（异动生效日期 - 搜索范围结束）一同使用，格式："YYYY-MM-DD"

**示例值**："2022-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >effective_date_end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动生效日期 - 搜索范围结束，需要与effective_date_start（异动生效日期 - 搜索范围开始）一同使用，格式："YYYY-MM-DD"

**示例值**："2022-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >updated_time_start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动更新时间 - 搜索范围开始，需要与updated_time_end（异动更新时间 - 搜索范围结束）一同使用，毫秒时间戳

**示例值**："1704084635000"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >updated_time_end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动更新时间 - 搜索范围结束，需要与updated_time_start（异动更新时间 - 搜索范围结束）一同使用，毫秒时间戳

**示例值**："1704084635000"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >target_department_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新部门 ID 列表

**示例值**：["7269981744640312876"]

**数据校验规则**：

- 最大长度：`30`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >transfer_type_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动类型，可通过接口
[获取异动类型列表
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/transfer_type/query)获取

**示例值**：["assignment_start_reason_option5"]

**数据校验规则**：

- 最大长度：`30`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >transfer_reason_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动原因，可通过接口
[获取异动原因列表
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/transfer_reason/query)获取详细信息

**示例值**：["reason_for_job_change_option_7182520625066475540_7382109467556446228"]

**数据校验规则**：

- 最大长度：`30`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >exception_statuses</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异常处理状态，多个状态之间为「或」的关系

**示例值**：["pending"]

**可选值有**：
<md-enum>
<md-enum-item key="pending" >pending  未处理</md-enum-item>
<md-enum-item key="processed" >processed  已处理</md-enum-item>
</md-enum>

**数据校验规则**：

- 最大长度：`10`
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "employment_ids": [
        "ou_a294793e8fa21529f2a60e3e9de45520"
    ],
    "job_change_ids": [
        "7044427347159746085"
    ],
    "statuses": [
        "Approving"
    ],
    "effective_date_start": "2022-01-01",
    "effective_date_end": "2022-01-01",
    "updated_time_start": "1704084635000",
    "updated_time_end": "1704084635000",
    "target_department_ids": [
        "7269981744640312876"
    ],
    "transfer_type_unique_identifier": [
        "assignment_start_reason_option5"
    ],
    "transfer_reason_unique_identifier": [
        "reason_for_job_change_option_7182520625066475540_7382109467556446228"
    ],
    "exception_statuses": [
        "pending"
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
	<md-text type="field-name" >items</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >job_change\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	员工异动列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >job_change_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动记录 id，可通过接口
[搜索异动信息
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_change/search)获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employment_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	雇员 id，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动状态

**可选值有**：
<md-enum>
<md-enum-item key="Approving" >审批中</md-enum-item>
<md-enum-item key="Approved" >审批通过</md-enum-item>
<md-enum-item key="Transformed" >已异动</md-enum-item>
<md-enum-item key="Rejected" >已拒绝</md-enum-item>
<md-enum-item key="Cancelled" >已撤销</md-enum-item>
<md-enum-item key="NoNeedApproval" >无需审批</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >transfer_type_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动类型，可通过接口
[获取异动类型列表
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/transfer_type/query)获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >transfer_reason_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动原因，可通过接口
[获取异动原因列表
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/transfer_reason/query)获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >process_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动流程 id，可通过【流程-获取单个流程详情】接口获取
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
	生效时间，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >created_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	创建时间，毫秒级时间戳
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >updated_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	更新时间，毫秒级时间戳
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >transfer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >transfer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	异动详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >remark</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	备注

**字段权限要求**：
<md-perm name="corehr:job_change.remark:read" desc="获取异动流程备注信息" support_app_types="custom,isv" tags="">获取异动流程备注信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >offer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	offer信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_dotted_manager_clean</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否撤销虚线上级
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >probation_exist</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否有试用期
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_department</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原部门，可通过[【批量查询部门】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_department</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新部门，可通过[【批量查询部门】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_work_location</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原工作地点，可通过[【批量查询地点】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_work_location</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新工作地点，可通过[【批量查询地点】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_direct_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原直属上级，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_direct_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新直属上级，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_dotted_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原虚线上级，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_dotted_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新虚线上级，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_job</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原职务，
可通过[【批量查询职务】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口获取

**字段权限要求（满足任一）**：
<md-perm name="corehr:employment.job:read" desc="获取员工的职务信息" support_app_types="custom,isv" tags="">获取员工的职务信息</md-perm>
<md-perm name="corehr:employment.job_level:read" desc="获取职务级别信息" support_app_types="custom,isv" tags="">获取职务级别信息</md-perm>
<md-perm name="corehr:employment.job_level:write" desc="读写员工的职务级别信息" support_app_types="custom" tags="">读写员工的职务级别信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_job</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新职务，
可通过[【批量查询职务】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口获取

**字段权限要求（满足任一）**：
<md-perm name="corehr:employment.job:read" desc="获取员工的职务信息" support_app_types="custom,isv" tags="">获取员工的职务信息</md-perm>
<md-perm name="corehr:employment.job_level:read" desc="获取职务级别信息" support_app_types="custom,isv" tags="">获取职务级别信息</md-perm>
<md-perm name="corehr:employment.job_level:write" desc="读写员工的职务级别信息" support_app_types="custom" tags="">读写员工的职务级别信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_job_family</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原序列，可通过[【批量查询序列】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_job_family</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新序列，可通过[【批量查询序列】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_job_level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原职级，
可通过[【批量查询职级】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)接口获取

**字段权限要求（满足任一）**：
<md-perm name="corehr:employment.job_level:read" desc="获取职务级别信息" support_app_types="custom,isv" tags="">获取职务级别信息</md-perm>
<md-perm name="corehr:employment.job_level:write" desc="读写员工的职务级别信息" support_app_types="custom" tags="">读写员工的职务级别信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_job_level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新级别，
可通过[【批量查询职级】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)接口获取

**字段权限要求（满足任一）**：
<md-perm name="corehr:employment.job_level:read" desc="获取职务级别信息" support_app_types="custom,isv" tags="">获取职务级别信息</md-perm>
<md-perm name="corehr:employment.job_level:write" desc="读写员工的职务级别信息" support_app_types="custom" tags="">读写员工的职务级别信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_workforce_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原人员类型，可通过[【批量查询人员类型】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_workforce_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新人员类型，可通过[【批量查询人员类型】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_employee_subtype</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原人员子类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_employee_subtype</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新人员子类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得

**字段权限要求（满足任一）**：
<md-perm name="corehr:contract.company:read" desc="获取合同主体信息" support_app_types="custom,isv" tags="">获取合同主体信息</md-perm>
<md-perm name="corehr:contract.company:write" desc="读写合同主体信息" support_app_types="custom" tags="">读写合同主体信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得

**字段权限要求（满足任一）**：
<md-perm name="corehr:contract.company:read" desc="获取合同主体信息" support_app_types="custom,isv" tags="">获取合同主体信息</md-perm>
<md-perm name="corehr:contract.company:write" desc="读写合同主体信息" support_app_types="custom" tags="">读写合同主体信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_contract_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原合同编号，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_contract_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新合同编号，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_contract_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原合同类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_contract_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新合同类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_duration_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原期限类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_duration_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新期限类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_signing_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原签订类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_signing_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新签订类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_contract_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原合同开始日期，格式："YYYY-MM-DD"

**字段权限要求（满足任一）**：
<md-perm name="corehr:contract.period:read" desc="获取合同期限信息" support_app_types="custom,isv" tags="">获取合同期限信息</md-perm>
<md-perm name="corehr:contract.period:write" desc="读写合同期限信息" support_app_types="custom" tags="">读写合同期限信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_contract_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新合同开始日期，格式："YYYY-MM-DD"

**字段权限要求（满足任一）**：
<md-perm name="corehr:contract.period:read" desc="获取合同期限信息" support_app_types="custom,isv" tags="">获取合同期限信息</md-perm>
<md-perm name="corehr:contract.period:write" desc="读写合同期限信息" support_app_types="custom" tags="">读写合同期限信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_contract_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原合同结束日期，格式："YYYY-MM-DD"

**字段权限要求（满足任一）**：
<md-perm name="corehr:contract.period:read" desc="获取合同期限信息" support_app_types="custom,isv" tags="">获取合同期限信息</md-perm>
<md-perm name="corehr:contract.period:write" desc="读写合同期限信息" support_app_types="custom" tags="">读写合同期限信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_contract_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新合同结束日期，格式："YYYY-MM-DD"

**字段权限要求（满足任一）**：
<md-perm name="corehr:contract.period:read" desc="获取合同期限信息" support_app_types="custom,isv" tags="">获取合同期限信息</md-perm>
<md-perm name="corehr:contract.period:write" desc="读写合同期限信息" support_app_types="custom" tags="">读写合同期限信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_working_hours_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原工时制度可通过[【批量查询工时制度】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_working_hours_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新工时制度，可通过[【批量查询工时制度】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_working_calendar</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原工作日历，开通休假服务后联系管理员获取。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_working_calendar</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新工作日历，开通休假服务后联系管理员获取。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_probation_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原试用期预计结束日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_probation_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新试用期预计结束日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_weekly_working_hours</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原周工作时长
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_weekly_working_hours</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新周工作时长
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_work_shift</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原排班
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_work_shift</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新排班
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_cost_center_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >job_data_cost_center\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	原成本中心分摊方式
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >cost_center_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	成本中心 ID，详细信息可通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	分摊比例(整数)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_cost_center_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >job_data_cost_center\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	新成本中心分摊方式
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >cost_center_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	成本中心 ID，详细信息可通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	分摊比例(整数)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_employment_change</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >tranfer_employment_info</md-text>
	</md-dt-td>
	<md-dt-td>
	原工作信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >regular_employee_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	转正式员工日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >seniority_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	司龄起算日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >employee_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	员工编号，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段

**字段权限要求**：
<md-perm name="corehr:job_change.employment_custom_field:read" desc="获取异动工作信息自定义字段" support_app_types="custom,isv" tags="">获取异动工作信息自定义字段</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >custom_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段 apiname，即自定义字段的唯一标识
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_name</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	中文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段类型
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
	字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_employment_change</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >tranfer_employment_info</md-text>
	</md-dt-td>
	<md-dt-td>
	新工作信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >regular_employee_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	转正式员工日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >seniority_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	司龄起算日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >employee_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	员工编号
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段

**字段权限要求**：
<md-perm name="corehr:job_change.employment_custom_field:read" desc="获取异动工作信息自定义字段" support_app_types="custom,isv" tags="">获取异动工作信息自定义字段</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >custom_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段 apiname，即自定义字段的唯一标识
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_name</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	中文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段类型
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
	字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_job_grade</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原职等，可通过[【查询职等】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口获取

**字段权限要求（满足任一）**：
<md-perm name="corehr:employment.job_grade:read" desc="获取职等信息" support_app_types="custom" tags="">获取职等信息</md-perm>
<md-perm name="corehr:employment.job_grade:write" desc="读写职等信息" support_app_types="custom" tags="">读写职等信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_job_grade</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新职等，可通过[【查询职等】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口获取

**字段权限要求（满足任一）**：
<md-perm name="corehr:employment.job_grade:read" desc="获取职等信息" support_app_types="custom" tags="">获取职等信息</md-perm>
<md-perm name="corehr:employment.job_grade:write" desc="读写职等信息" support_app_types="custom" tags="">读写职等信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_compensation_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原薪资类型

**字段权限要求**：
<md-perm name="corehr:job_data.compensation_type:read" desc="获取薪资类型" support_app_types="custom" tags="">获取薪资类型</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_compensation_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新薪资类型

**字段权限要求**：
<md-perm name="corehr:job_data.compensation_type:read" desc="获取薪资类型" support_app_types="custom" tags="">获取薪资类型</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_service_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原任职公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得

**字段权限要求**：
<md-perm name="corehr:job_data.service_company:read" desc="获取任职公司" support_app_types="custom" tags="">获取任职公司</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_service_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新任职公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得

**字段权限要求**：
<md-perm name="corehr:job_data.service_company:read" desc="获取任职公司" support_app_types="custom" tags="">获取任职公司</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_position</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原岗位，可通过【岗职务管理-岗位】相关API获取（目前仅灰度部分租户，如需要请联系管理员开灰）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_position</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新岗位，可通过【岗职务管理-岗位】相关API获取（目前仅灰度部分租户，如需要请联系管理员开灰）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_social_security_city</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原社保城市

**字段权限要求**：
<md-perm name="corehr:job_change.social_security_city:read" desc="获取异动单据社保字段" support_app_types="custom" tags="">获取异动单据社保字段</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_social_security_city</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新社保城市

**字段权限要求**：
<md-perm name="corehr:job_change.social_security_city:read" desc="获取异动单据社保字段" support_app_types="custom" tags="">获取异动单据社保字段</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_pathway</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原通道

**字段权限要求（满足任一）**：
<md-perm name="corehr:job_change.pathway:read" desc="读取异动信息中的通道字段信息" support_app_types="custom,isv" tags="">读取异动信息中的通道字段信息</md-perm>
<md-perm name="corehr:job_change.pathway:write" desc="读写异动信息中的通道字段信息" support_app_types="custom,isv" tags="">读写异动信息中的通道字段信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_pathway</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新通道

**字段权限要求（满足任一）**：
<md-perm name="corehr:job_change.pathway:read" desc="读取异动信息中的通道字段信息" support_app_types="custom,isv" tags="">读取异动信息中的通道字段信息</md-perm>
<md-perm name="corehr:job_change.pathway:write" desc="读写异动信息中的通道字段信息" support_app_types="custom,isv" tags="">读写异动信息中的通道字段信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_transfer_with_workforce</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	编制随人员一起调整
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_adjust_salary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否调整薪酬

**字段权限要求**：
<md-perm name="corehr:job_change.is_adjust_salary:read" desc="获取异动单据是否调薪字段" support_app_types="custom" tags="">获取异动单据是否调薪字段</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	异动自定义字段

**字段权限要求**：
<md-perm name="corehr:job_change.custom_field:read" desc="获取员工异动自定义字段信息" support_app_types="custom,isv" tags="">获取员工异动自定义字段信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >custom_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段 apiname，即自定义字段的唯一标识
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_name</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	中文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段类型
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
	字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"）
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
	<md-text type="field-name" >page_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
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
                "job_change_id": "6991776076699549697",
                "employment_id": "ou_a294793e8fa21529f2a60e3e9de45520",
                "status": "Approved",
                "transfer_type_unique_identifier": "direct_leader_change",
                "transfer_reason_unique_identifier": "involuntary_transfer",
                "process_id": "6991776078461142564",
                "effective_date": "2022-03-01",
                "created_time": "1627899724000",
                "updated_time": "1647434443000",
                "transfer_info": {
                    "remark": "异动详情",
                    "offer_info": "优质人才，加急处理",
                    "target_dotted_manager_clean": true,
                    "probation_exist": false,
                    "original_department": "6966236933198579208",
                    "target_department": "6966236933198579208",
                    "original_work_location": "6967271100992587295",
                    "target_work_location": "6967271100992587295",
                    "original_direct_manager": "6974641477444060708",
                    "target_direct_manager": "7013619729281713671",
                    "original_dotted_manager": "6974648866876573198",
                    "target_dotted_manager": "7013328578351842852",
                    "original_job": "6969469398088287751",
                    "target_job": "6969469557836760606",
                    "original_job_family": "6967287547462419975",
                    "target_job_family": "6967287547462419975",
                    "original_job_level": "6972085707674355214",
                    "target_job_level": "6972085707674355214",
                    "original_workforce_type": "6968386026792289828",
                    "target_workforce_type": "7036268995372303885",
                    "original_employee_subtype": "6968386026792289828",
                    "target_employee_subtype": "7036268995372303885",
                    "original_company": "6974659700705068581",
                    "target_company": "6974659700705068581",
                    "original_contract_number": "55332",
                    "target_contract_number": "55333",
                    "original_contract_type": "labor_contract",
                    "target_contract_type": "labor_contract",
                    "original_duration_type": "fixed_term",
                    "target_duration_type": "fixed_term",
                    "original_signing_type": "new",
                    "target_signing_type": "new",
                    "original_contract_start_date": "2021-07-01",
                    "target_contract_start_date": "2021-07-01",
                    "original_contract_end_date": "2024-07-01",
                    "target_contract_end_date": "2024-07-01",
                    "original_working_hours_type": "6969087376740206087",
                    "target_working_hours_type": "6969087376740206087",
                    "original_working_calendar": "6969087376740236087",
                    "target_working_calendar": "6969087376740236087",
                    "original_probation_end_date": "2021-11-17",
                    "target_probation_end_date": "2021-11-17",
                    "original_weekly_working_hours": "162",
                    "target_weekly_working_hours": "160",
                    "original_work_shift": "work_shift",
                    "target_work_shift": "non_work_shift",
                    "original_cost_center_rate": [
                        {
                            "cost_center_id": "6950635856373745165",
                            "rate": 100
                        }
                    ],
                    "target_cost_center_rate": [
                        {
                            "cost_center_id": "6950635856373745165",
                            "rate": 100
                        }
                    ],
                    "original_employment_change": {
                        "regular_employee_start_date": "2023-01-01",
                        "seniority_date": "2023-01-01",
                        "employee_number": "1111111",
                        "custom_fields": [
                            {
                                "custom_api_name": "name",
                                "name": {
                                    "zh_cn": "自定义姓名",
                                    "en_us": "Custom Name"
                                },
                                "type": 1,
                                "value": "231"
                            }
                        ]
                    },
                    "target_employment_change": {
                        "regular_employee_start_date": "2023-01-01",
                        "seniority_date": "2023-01-01",
                        "employee_number": "1111111",
                        "custom_fields": [
                            {
                                "custom_api_name": "name",
                                "name": {
                                    "zh_cn": "自定义姓名",
                                    "en_us": "Custom Name"
                                },
                                "type": 1,
                                "value": "231"
                            }
                        ]
                    },
                    "original_job_grade": "7289005963599693366",
                    "target_job_grade": "7289005963599693366",
                    "original_compensation_type": "hourly",
                    "target_compensation_type": "salary",
                    "original_service_company": "7289005963599693367",
                    "target_service_company": "7289005963599693367",
                    "original_position": "7289005963599693367",
                    "target_position": "7289005963599693367",
                    "original_social_security_city": "7289005963599693367",
                    "target_social_security_city": "7289005963599693367",
                    "original_pathway": "7289005963599693367",
                    "target_pathway": "7289005963599693367",
                    "is_transfer_with_workforce": false
                },
                "is_adjust_salary": true,
                "custom_fields": [
                    {
                        "custom_api_name": "name",
                        "name": {
                            "zh_cn": "自定义姓名",
                            "en_us": "Custom Name"
                        },
                        "type": 1,
                        "value": "\"231\""
                    }
                ]
            }
        ],
        "has_more": true,
        "page_token": "6891251722631890445"
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
  <md-td>1160101</md-td>
  <md-td>marshal error</md-td>
  <md-td>please oncall, https://applink.feishu.cn/TLJpeNdW</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160102</md-td>
  <md-td>unmarshal error</md-td>
  <md-td>please oncall, https://applink.feishu.cn/TLJpeNdW</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160103</md-td>
  <md-td>request ID repeat</md-td>
  <md-td>change the request id</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160104</md-td>
  <md-td>custom field format error</md-td>
  <md-td>please oncall, https://applink.feishu.cn/TLJpeNdW</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160105</md-td>
  <md-td>field is required</md-td>
  <md-td>please check the parameter</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160106</md-td>
  <md-td>date format should be 2006-01-02</md-td>
  <md-td>please check the date parameter</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160107</md-td>
  <md-td>param is invalid</md-td>
  <md-td>please check the parameter</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




