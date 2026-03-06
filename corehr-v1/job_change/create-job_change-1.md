---
title: "发起员工异动(不推荐)"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_change/create"
updateTime: "1734431976000"
---

# 发起员工异动（不推荐）

该接口用于发起员工异动（变更员工雇佣信息），若发起成功，会生成一条员工的异动数据，同时产生相应的事件：[异动状态变更事件](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_change/events/updated){尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v1&resource=job_change&method=create)

:::html
<md-alert type="error">
本事件不再推荐使用，请使用新版本[发起员工异动](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_change/create)
</md-alert>
:::

:::html
<md-alert type="warn">

</md-alert>
:::

:::html
<md-alert type="tip">

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
      <md-td>https://open.feishu.cn/open-apis/corehr/v1/job_changes</md-td>
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
      <md-app-support types="custom"></md-app-support>
      </md-td>
    </md-tr>
    <md-tr>
      <md-th>
            权限要求
            <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
            
            <div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
            
      </md-th>
      <md-td>
            <md-perm name="corehr:corehr" desc="更新核心人事信息" support_app_types="custom" tags="">更新核心人事信息</md-perm>
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
        <md-perm name="corehr:job_change.employment_custom_field:read" desc="获取异动工作信息自定义字段" support_app_types="custom,isv" tags="">获取异动工作信息自定义字段</md-perm>
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
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
<md-enum-item key="people_admin_id" >以people_admin_id来识别用户</md-enum-item>
<md-enum-item key="people_corehr_id" >以飞书人事的ID来识别用户</md-enum-item>
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

**示例值**：people_corehr_department_id

**可选值有**：
<md-enum>
<md-enum-item key="open_department_id" >以 open_department_id 来标识部门</md-enum-item>
<md-enum-item key="department_id" >以 department_id 来标识部门</md-enum-item>
<md-enum-item key="people_corehr_department_id" >以 people_corehr_department_id 来标识部门</md-enum-item>
</md-enum>

**默认值**：`people_corehr_department_id`
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
	<md-text type="field-name" >transfer_mode</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	异动方式

**示例值**：2

**可选值有**：
<md-enum>
<md-enum-item key="1" >直接异动（无审批）</md-enum-item>
<md-enum-item key="2" >正常异动（完整流程）</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >employment_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	雇员ID，ID 类型与查询参数 user_id_type 的取值一致。
- 当user_id_type=user_id时，该字段取员工的user_id，取值参考user_id_type部分。
- 当user_id_type=people_corehr_id时，则取该员工的人事雇佣ID，可从[雇佣ID](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取。

**示例值**："ou_a294793e8fa21529f2a60e3e9de45520"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >transfer_type_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	异动类型唯一标识，不支持仅在特殊场景使用的异动类型，如组织架构调整、职责转交和试用期转正。可通过接口[获取异动类型列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/transfer_type/query)获取

**示例值**："internal_transfer"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >flow_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	关联流程唯一标识符，可通过接口[获取异动类型列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/transfer_type/query)获取

注意：当异动方式为2时，该字段为必填

**示例值**："people_6963913041981490725_6983885526583627531"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >effective_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	生效日期，格式："YYYY-MM-DD"

**示例值**："2022-03-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >transfer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >transfer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	异动详细信息，以下参数如不传，无默认值，代表对应数据无异动
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >remark</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	备注

**示例值**："异动详情"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >offer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	offer信息

注：本字段仅会存储到数据库，前端表单不支持直接显示。

**示例值**："offer info"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_dotted_manager_clean</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否撤销虚线上级

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >probation_exist</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否有试用期

**示例值**：false
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_department</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原部门ID，可通过[【批量查询部门】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口获取

**示例值**："6966236933198579208"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_department</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新部门ID，可通过[【批量查询部门】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)接口获取

**示例值**："6966236933198579208"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_work_location</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原工作地点，可通过[【批量查询地点】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获取

**示例值**："6967271100992587295"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_work_location</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新工作地点，可通过[【批量查询地点】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)接口获取

**示例值**："6967271100992587295"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_direct_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原直属上级，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取

**示例值**："6974641477444060708"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_direct_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新直属上级，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取

**示例值**："7013619729281713671"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_dotted_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原虚线上级，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取

**示例值**："6974648866876573198"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_dotted_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新虚线上级，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取

**示例值**："7013328578351842852"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_job</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原职务，
可通过[【批量查询职务】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口获取

**示例值**："6969469398088287751"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_job</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新职务，
可通过[【批量查询职务】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口获取

**示例值**："6969469557836760606"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_job_family</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原序列ID，可通过[【批量查询序列】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)接口获取

**示例值**："6967287547462419975"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_job_family</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新序列ID，可通过[【批量查询序列】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)接口获取

**示例值**："6967287547462419975"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_job_level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原职级ID，
可通过[【批量查询职级】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)接口获取

**示例值**："6972085707674355214"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_job_level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新职级ID，
可通过[【批量查询职级】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)接口获取

**示例值**："6972085707674355214"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_workforce_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原人员类型，可通过[【批量查询人员类型】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)接口获取

**示例值**："6968386026792289828"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_workforce_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新人员类型，可通过[【批量查询人员类型】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)接口获取

**示例值**："7036268995372303885"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_employee_subtype</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原人员子类型

**示例值**："6968386026792289828"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_employee_subtype</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新人员子类型

**示例值**："7036268995372303885"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得

**示例值**："6974659700705068581"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得

**示例值**："6974659700705068581"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_contract_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原合同编号，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息

**示例值**："55332"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_contract_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新合同编号，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息

**示例值**："55333"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_contract_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原合同类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息

**示例值**："labor_contract"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_contract_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新合同类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息

**示例值**："labor_contract"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_duration_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原期限类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息

**示例值**："fixed_term"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_duration_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新期限类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息

**示例值**："fixed_term"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_signing_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原签订类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息

**示例值**："new"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_signing_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新签订类型，可通过[【批量查询合同】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/list)接口获取详细信息

**示例值**："new"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_contract_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原合同开始日期，格式："YYYY-MM-DD"

**示例值**："2021-07-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_contract_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新合同开始日期，格式："YYYY-MM-DD"

**示例值**："2021-07-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_contract_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原合同结束日期，格式："YYYY-MM-DD"

**示例值**："2024-07-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_contract_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新合同结束日期，格式："YYYY-MM-DD"

**示例值**："2024-07-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_working_hours_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原工时制度，可通过[【批量查询工时制度】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口获取

**示例值**："6969087376740206087"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_working_hours_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新工时制度，可通过[【批量查询工时制度】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口获取

**示例值**："6969087376740206087"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_working_calendar</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原工作日历，请开通休假服务后联系管理员获取工作日历数据

**示例值**："6969087376740236087"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_working_calendar</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新工作日历，请开通休假服务后联系管理员获取工作日历数据

**示例值**："6969087376740236087"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_probation_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原试用期预计结束日期，格式："YYYY-MM-DD"

**示例值**："2021-11-17"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_probation_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新试用期预计结束日期，格式："YYYY-MM-DD"

**示例值**："2021-11-17"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_weekly_working_hours</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原周工作时长

**示例值**："162"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_weekly_working_hours</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新周工作时长

**示例值**："160"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_work_shift</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原排班

**示例值**："work_shift"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_work_shift</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新排班

**示例值**："non_work_shift"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_cost_center_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >support_cost_center_item\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原成本中心分摊信息
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
	支持的成本中心id，详细信息可通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得

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
	分摊比例

**示例值**：100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_cost_center_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >support_cost_center_item\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新成本中心分摊信息
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
	支持的成本中心id，详细信息可通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得

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
	分摊比例

**示例值**：100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_employment_change</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >tranfer_employment_info</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原工作信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >regular_employee_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	转正式员工日期，格式："YYYY-MM-DD"

**示例值**："2023-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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
	司龄起算日期，格式："YYYY-MM-DD"

**示例值**："2023-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employee_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	员工编号，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取

**示例值**："1111111"
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
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
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
	是
	</md-dt-td>
	<md-dt-td>
	自定义字段 apiname，即自定义字段的唯一标识。可以通过[获取自定义字段列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query)获取

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
	字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"）

注意：

1.枚举字段值可通过[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)获取，参考接口返回的 字段详情 > 字段类型配置信息 > 选项配置信息 > 选项信息 > 枚举常量集 API name

**示例值**："231"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_employment_change</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >tranfer_employment_info</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新工作信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >regular_employee_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	转正式员工日期，格式："YYYY-MM-DD"

**示例值**："2023-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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
	司龄起算日期，格式："YYYY-MM-DD"

**示例值**："2023-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employee_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	员工编号，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取

**示例值**："1111111"
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
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段
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
	是
	</md-dt-td>
	<md-dt-td>
	自定义字段 apiname，即自定义字段的唯一标识。可以通过[获取自定义字段列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query)获取

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
	字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"）

注意：

1.枚举字段值可通过[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)获取，参考接口返回的 字段详情 > 字段类型配置信息 > 选项配置信息 > 选项信息 > 枚举常量集 API name

**示例值**："231"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_job_grade</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原职等，可通过[【查询职等】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口获取

**示例值**："7289005963599693366"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_job_grade</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新职等，可通过[【查询职等】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口获取

**示例值**："7289005963599693366"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_compensation_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原薪资类型

**示例值**："hourly"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_compensation_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新薪资类型

**示例值**："salary"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_service_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原任职公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得

**示例值**："7289005963599693367"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_service_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新任职公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得

**示例值**："7289005963599693367"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >original_position</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	原岗位

**示例值**："7289005963599693367"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >target_position</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	新岗位

**示例值**："7289005963599693367"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >transfer_key</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	发起异动幂等标志，发起失败可以重新用此标志继续请求

**示例值**："transfer_3627531"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >initiator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	异动发起人 ID，可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取

**示例值**："ou_a294793e8fa21529f2a60e3e9de45520"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "transfer_mode": 2,
    "employment_id": "ou_a294793e8fa21529f2a60e3e9de45520",
    "transfer_type_unique_identifier": "internal_transfer",
    "flow_id": "people_6963913041981490725_6983885526583627531",
    "effective_date": "2022-03-01",
    "transfer_info": {
        "remark": "异动详情",
        "offer_info": "offer info",
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
        "target_position": "7289005963599693367"
    },
    "transfer_key": "transfer_3627531",
    "initiator_id": "ou_a294793e8fa21529f2a60e3e9de45520"
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
	<md-text type="field-type" >job_change</md-text>
	</md-dt-td>
	<md-dt-td>
	\-
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
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


<md-dt-tr level="1">
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


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	异动状态

**可选值有**：
<md-enum>
<md-enum-item key="0" >Approving  审批中</md-enum-item>
<md-enum-item key="1" >Approved  审批通过</md-enum-item>
<md-enum-item key="2" >Transformed  已异动</md-enum-item>
<md-enum-item key="3" >Rejected  已拒绝</md-enum-item>
<md-enum-item key="4" >Cancelled  已撤销</md-enum-item>
<md-enum-item key="5" >NoNeedApproval  无需审批</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >transfer_type_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动类型唯一标识，，可通过接口
[获取异动类型列表
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/transfer_type/query)获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >transfer_reason_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动原因唯一标识，可通过接口
[获取异动原因列表
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/transfer_reason/query)获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >process_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动发起后审批流程 id，可通过【流程-获取单个流程列表】获取详细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >effective_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	异动生效日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >created_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	创建时间，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >remark</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	备注
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >offer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	offer信息（数据仅会存储到系统，不支持页面上显示）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_job</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原职务，
可通过[【批量查询职务】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_job</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新职务，
可通过[【批量查询职务】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_job_level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原级别，
可通过[【批量查询职级】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_job_level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新职级，
可通过[【批量查询职级】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新公司，详细信息可通过[【批量查询公司】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)接口查询获得
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_contract_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原合同开始日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_contract_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新合同开始日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_contract_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原合同结束日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_contract_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新合同结束日期，格式："YYYY-MM-DD"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_working_hours_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原工时制度，可通过[【批量查询工时制度】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/list)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_working_calendar</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原工作日历，请开通休假服务后联系管理员获取工作日历数据
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_working_calendar</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新工作日历，请开通休假服务后联系管理员获取工作日历数据
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_cost_center_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >support_cost_center_item\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	原成本中心分摊信息
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
	支持的成本中心id，详细信息可通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得
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
	分摊比例
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_cost_center_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >support_cost_center_item\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	新成本中心分摊信息
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
	支持的成本中心id，详细信息可通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口查询获得
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
	分摊比例
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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


<md-dt-tr level="3">
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


<md-dt-tr level="3">
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


<md-dt-tr level="3">
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


<md-dt-tr level="3">
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


<md-dt-tr level="4">
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


<md-dt-tr level="4">
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


<md-dt-tr level="5">
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


<md-dt-tr level="5">
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


<md-dt-tr level="4">
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


<md-dt-tr level="4">
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


<md-dt-tr level="2">
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


<md-dt-tr level="3">
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


<md-dt-tr level="3">
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


<md-dt-tr level="3">
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


<md-dt-tr level="3">
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


<md-dt-tr level="4">
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


<md-dt-tr level="4">
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


<md-dt-tr level="5">
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


<md-dt-tr level="5">
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


<md-dt-tr level="4">
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


<md-dt-tr level="4">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_job_grade</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原职等，可通过[【查询职等】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_job_grade</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新职等，可通过[【查询职等】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_compensation_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原薪资类型，请开通薪酬服务后联系管理员获取

**字段权限要求**：
<md-perm name="corehr:job_data.compensation_type:read" desc="获取薪资类型" support_app_types="custom" tags="">获取薪资类型</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_compensation_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新薪资类型，请开通薪酬服务后联系管理员获取

**字段权限要求**：
<md-perm name="corehr:job_data.compensation_type:read" desc="获取薪资类型" support_app_types="custom" tags="">获取薪资类型</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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


<md-dt-tr level="2">
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


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >original_position</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原岗位
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >target_position</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新岗位
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
        "job_change_id": "6991776076699549697",
        "employment_id": "ou_a294793e8fa21529f2a60e3e9de45520",
        "status": 4,
        "transfer_type_unique_identifier": "direct_leader_change",
        "transfer_reason_unique_identifier": "involuntary_transfer",
        "process_id": "6991776078461142564",
        "effective_date": "2022-03-01",
        "created_time": "1627899724000",
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
            "target_position": "7289005963599693367"
        }
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
  <md-td>400</md-td>
  <md-td>1160100</md-td>
  <md-td>The transaction type can't be empty</md-td>
  <md-td>异动类型为必填，请填写异动类型</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160200</md-td>
  <md-td>Please check employment_id</md-td>
  <md-td>异动员工ID为必填，请填写异动员工ID</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160201</md-td>
  <md-td>Has pending offboarding</md-td>
  <md-td>存在「审批中」或「待生效」的离职申请，请先撤销后再申请</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160202</md-td>
  <md-td>has a job status change which effective date is later</md-td>
  <md-td>存在晚于生效日期的异动记录，请撤销后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160300</md-td>
  <md-td>Please check department  effective date</md-td>
  <md-td>异动生效日期部门不存在或者已停用，请检查部门ID的部门后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160301</md-td>
  <md-td>Please check work city effective date</md-td>
  <md-td>异动生效日期工作地点不存在或者已停用，请检查工作地点后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160302</md-td>
  <md-td>Please check job effective date</md-td>
  <md-td>异动生效日期职务不存在或者已停用，请检查职务后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160303</md-td>
  <md-td>Please check job family effective date</md-td>
  <md-td>异动生效日期序列不存在或者已停用，请检查序列后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160306</md-td>
  <md-td>Please check work_hour_type</md-td>
  <md-td>请确认工时制度是否存在后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160307</md-td>
  <md-td>Please check job level</md-td>
  <md-td>请确认职级是否存在后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160308</md-td>
  <md-td>Please check work force type</md-td>
  <md-td>请确认人员类型是否存在后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160400</md-td>
  <md-td>Please check leader</md-td>
  <md-td>直属汇报线成环，请确认直属上级链路是否成环后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160401</md-td>
  <md-td>Please check virtual leader</md-td>
  <md-td>虚线汇报线成环，请确认虚线上级链路是否成环后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160500</md-td>
  <md-td>system error</md-td>
  <md-td>调用上下游系统错误，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160501</md-td>
  <md-td>transform effective date early than onboarding</md-td>
  <md-td>异动生效日期早于入职日期，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160502</md-td>
  <md-td>transform effective date later than offbaording</md-td>
  <md-td>异动生效日期晚于离职日期，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160600</md-td>
  <md-td>At least fill in one field in transform information for job status change</md-td>
  <md-td>请至变更一个异动信息字段后再发起员工异动</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160601</md-td>
  <md-td>At least fill in one field in transform information for job status change</md-td>
  <md-td>请至变更一个异动信息字段后再发起员工异动</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160700</md-td>
  <md-td>check whether the selected members or job status change information are correct</md-td>
  <md-td>请确认原异动信息的字段与异动员工当前的信息一致后再发起</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1162002</md-td>
  <md-td>Has a job data which effective date is later</md-td>
  <md-td>存在一条晚于当前异动生效日期的任职记录</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163000</md-td>
  <md-td>Please check department  effective date</md-td>
  <md-td>异动生效日期部门不存在或者已停用，请检查部门ID的部门后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163001</md-td>
  <md-td>Please check work city effective date</md-td>
  <md-td>异动生效日期工作地点不存在或者已停用，请检查工作地点后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163002</md-td>
  <md-td>Please check job effective date</md-td>
  <md-td>异动生效日期职务不存在或者已停用，请检查职务后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163003</md-td>
  <md-td>Please check job family effective date</md-td>
  <md-td>异动生效日期序列不存在或者已停用，请检查序列后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163004</md-td>
  <md-td>The job doesn't match the job family or job level</md-td>
  <md-td>职务与职级或序列不匹配，请修改职务序列职级后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163005</md-td>
  <md-td>The job doesn't match the job family or job level</md-td>
  <md-td>职务与职级或序列不匹配，请修改职务序列职级后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163010</md-td>
  <md-td>The job family doesn't match job level</md-td>
  <md-td>请检查职级与序列是否匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163012</md-td>
  <md-td>Insufficient headcount</md-td>
  <md-td>请检查是否还有head count后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163015</md-td>
  <md-td>The weekly working hours value is out of range</md-td>
  <md-td>周工作时间值超出限定范围，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163016</md-td>
  <md-td>In the work location field, you can only select a location whose purpose is work city</md-td>
  <md-td>工作地点字段只能选择用途为工作城市的地点，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163017</md-td>
  <md-td>In the social security city field, you can only select a location whose purpose is social security city</md-td>
  <md-td>社保城市字段只能选择用途为社保城市的地点，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163018</md-td>
  <md-td>The number of allocation proportion must be an integer from 1 to 100</md-td>
  <md-td>成本中心的比例值只能限定在1-100范围内，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163019</md-td>
  <md-td>Duplicate cost center rate</md-td>
  <md-td>多个成本中心比例总和必须等于100，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163020</md-td>
  <md-td>Cost center is non-effective on the effective date of job status change</md-td>
  <md-td>异动生效日期当天成本中心还未生效，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163021</md-td>
  <md-td>The number of allocation proportion must be an integer from 1 to 100</md-td>
  <md-td>成本中心的比例值只能限定在1-100范围内，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163022</md-td>
  <md-td>Please fill in both cost center and allocation proportion</md-td>
  <md-td>请同时填写成本中心id和对应比例</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163023</md-td>
  <md-td>Please enter the sub-level cost center</md-td>
  <md-td>请输入下级成本中心</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163024</md-td>
  <md-td>Illegal data format of cost center</md-td>
  <md-td>成本中心数据格式不合法，请检查成本中心填写格式后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163025</md-td>
  <md-td>No cost centers found</md-td>
  <md-td>填写的成本中心不存在，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1163026</md-td>
  <md-td>Cost center is non-effective at a future date</md-td>
  <md-td>异动生效日期成本中心还未生效，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1164000</md-td>
  <md-td>Direct manager wasn't onboarded</md-td>
  <md-td>部门负责人还未入职，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1164001</md-td>
  <md-td>Direct manager was offboarded</md-td>
  <md-td>直属上级已离职，请重新填写后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1164002</md-td>
  <md-td>Dotted manager wasn't onboarded</md-td>
  <md-td>直属上级未入职，请重新填写后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1164003</md-td>
  <md-td>The effective date of the change is later than the offboarding date</md-td>
  <md-td>员工异动日期晚于离职日期，请重新填写后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1165000</md-td>
  <md-td>Dotted manager was offboarded</md-td>
  <md-td>虚线上级已离职，请重新填写后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1165001</md-td>
  <md-td>Contract start date is later than the original contract end date</md-td>
  <md-td>合同开始日期晚于原合同结束日期，请重新填写后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1165002</md-td>
  <md-td>Expected probation end date must be later than the effective date of job status change</md-td>
  <md-td>期望试用期结束日期必须晚于等于异动生效日期,请重新填写后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1165005</md-td>
  <md-td>Contract end date must be later than the effective date of job status change</md-td>
  <md-td>合同结束日期必须晚于等于异动生效日期，请重新填写后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1165006</md-td>
  <md-td>Contract end date can't be earlier than contract start date</md-td>
  <md-td>合同结束日期不能晚于原合同开始日期，请重新填写后重新提交</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




