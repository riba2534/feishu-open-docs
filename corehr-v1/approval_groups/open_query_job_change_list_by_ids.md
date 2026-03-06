---
title: "批量查询人员调整内容"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/approval_groups/open_query_job_change_list_by_ids"
updateTime: "1763528835000"
---

# 批量查询人员调整内容

根据人员异动记录 ID 批量查询人员调整内容{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=approval_groups&method=open_query_job_change_list_by_ids)

:::html
<md-alert type="tip">

</md-alert>
:::

:::html
<md-alert type="warn">
- 用户使用该接口前需提前获取 组织架构调整流程信息 权限
- 延迟说明：数据库主从延迟2s以内，即：用户接收到流程状态变更消息后2s内调用此接口可能查询不到数据。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/approval_groups/open_query_job_change_list_by_ids</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
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
            <md-perm name="corehr:approval_groups.orgdraft_job_change:read" desc="获取组织架构调整人员调整内容" support_app_types="custom,isv" tags="">获取组织架构调整人员调整内容</md-perm>
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
        <md-perm name="corehr:employment.job:read" desc="获取员工的职务信息" support_app_types="custom,isv" tags="">获取员工的职务信息</md-perm>
        <md-perm name="corehr:employment.job_level:read" desc="获取职务级别信息" support_app_types="custom,isv" tags="">获取职务级别信息</md-perm>
        <md-perm name="corehr:employment.job_grade:read" desc="获取职等信息" support_app_types="custom" tags="">获取职等信息</md-perm>
        <md-perm name="corehr:employment.job_grade:write" desc="读写职等信息" support_app_types="custom" tags="">读写职等信息</md-perm>
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
        <md-perm name="corehr:employment.job_level:write" desc="读写员工的职务级别信息" support_app_types="custom" tags="">读写员工的职务级别信息</md-perm>
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
	<md-text type="field-name" >process_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	组织架构调整流程 ID， 用户通过『飞书人事-我的团队-组织架构』或『飞书 人事-人员管理-组织架构』 发起一个组织架构调整，并提交审批后，系统会根据管理员在审批流程中配置的规则，生成 一个或多个审批单据。

**示例值**：6991776076699549697
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
	<md-text type="field-name" >job_change_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	人员异动记录 ID List,  在组织架构调整发起后，会为调整涉及的员工生成一个 员工异动记录， 对应的记录 ID 即为 job_change_id。  调整记录可通过[【根据流程 ID 查询组织架构调整记录】](ssl://ttdocs/uAjLw4CM/ukTMukTMukTM/corehr-v2/approval_groups/get) 获取。 
- 必须是查询参数process_id对应的流程下的人员调整记录ID。
- 未设置时查询到的人员调整记录为空。

**示例值**：["6991776076699549697"]

**数据校验规则**：

- 长度范围：`1` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >need_department_path</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否返回部门全路径

**示例值**：false

**默认值**：`false`
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "job_change_ids": [
        "6991776076699549697"
    ],
    "need_department_path": false
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
	<md-text type="field-name" >job_changes</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >job_change\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	人员异动记录信息列表
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
	异动记录 id, 在组织架构调整发起后，会为调整涉及的员工生成一个 员工异动记录， 对应的记录 ID 即为 job_change_id
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
	雇员 id, 详细信息可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
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
	<md-text type="field-name" >original_department</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原部门，可通过[查询单个部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)获取详情，ID 类型需要为 ==people_corehr_department_id==。
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
	新部门, 如果是一个已存在的部门， 则会使用其飞书人事部门 ID 作为调整记录 ID，可通过[查询单个部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)获取详情，ID 类型需要为==people_corehr_id==
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_draft_department</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新部门，为避免一个没有经过审批的组织架构调整影响正在运行的系统，如果是在组织架构调整中新生成的『部门』生成临时的 ID， 格式 "td_
xxx"
可通过[批量查询部门调整内容](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/approval_groups/open_query_department_change_list_by_ids)获取详情，ID 类型需要为 ==people_corehr_department_id==。



	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_department_id_path</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >orgdraft_department_id\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	原部门全路径，从根部门开始自上而下返回部门 ID 列表, 主要用于 API 场景， 没有审批完成前获取部门路径用于计算。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >department_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	部门 ID ，对于在本次调整中新建的部门，在调整未生效时将返回为空。支持根据部门 ID 类型转换。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >draft_department_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	调整过程部门 ID ，固定返回people_corehr_department_id，不会根据部门 ID 类型进行转换。对于在本次调整中新建的部门，在调整未生效前会返回格式为 td_xxx 的过程部门 ID，生效后将返回正式的people_corehr_department_id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_department_id_path</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >orgdraft_department_id\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	新部门全路径，从根部门开始自上而下返回部门 ID 列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >department_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	部门 ID ，对于在本次调整中新建的部门，在调整未生效时将返回为空。支持根据部门 ID 类型转换
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >draft_department_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	调整过程部门 ID ，固定返回people_corehr_department_id，不会根据部门 ID 类型进行转换。对于在本次调整中新建的部门，在调整未生效前会返回格式为 td_xxx 的临时部门 ID，生效后将返回正式的people_corehr_department_id
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
	原直属上级， 详细信息可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
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
	新直属上级， 详细信息可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口获取
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
	原职务， 可通过[查询单个职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get)获取详情。

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
	新职务，可通过[查询单个职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get)获取详情。

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
	原序列， 可通过[查询单个序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)获取详情。
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
	新序列， 可通过[查询单个序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)获取详情。
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
	原职级，可通过[查询单个职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)获取详情。

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
	新职级，可通过[查询单个职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)获取详情。

**字段权限要求（满足任一）**：
<md-perm name="corehr:employment.job_level:read" desc="获取职务级别信息" support_app_types="custom,isv" tags="">获取职务级别信息</md-perm>
<md-perm name="corehr:employment.job_level:write" desc="读写员工的职务级别信息" support_app_types="custom" tags="">读写员工的职务级别信息</md-perm>
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
	成本中心 ID，可以通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息
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
	分摊比例(整数) 成本分摊百分比的整数部分，实际值为小数时向下取整（比如：12.99→ 12），如需小数请使用分摊比例字段。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >new_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	分摊比例 成本分摊百分比，可能包含小数位。

- 功能灰度中，成本分摊功能灰度开放前无值。
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
	成本中心 ID，可以通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息
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
	分摊比例(整数) 成本分摊百分比的整数部分，实际值为小数时向下取整（比如：12.99→ 12），如需小数请使用分摊比例字段。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >new_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	分摊比例 成本分摊百分比，可能包含小数位。

- 功能灰度中，成本分摊功能灰度开放前无值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_allocation_expiration_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新分摊失效时间
- 时间格式：YYYY-MM-DD HH:MM:SS
- 功能灰度中，成本分摊功能灰度开放前无值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_allocation_expiration_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原分摊失效时间
- 时间格式：YYYY-MM-DD HH:MM:SS
- 功能灰度中，成本分摊功能灰度开放前无值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_allocation_effective_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新分摊生效时间
- 时间格式：YYYY-MM-DD HH:MM:SS
- 功能灰度中，成本分摊功能灰度开放前无值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_allocation_effective_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原分摊生效时间
- 时间格式：YYYY-MM-DD HH:MM:SS
- 功能灰度中，成本分摊功能灰度开放前无值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_default_cost_center</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原默认成本中心 原默认成本中心的ID，可以通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息。
原默认成本中心是否继承字段为true，或者员工原岗位、原部门均无默认成本中心时无值。

- 功能灰度中，成本分摊功能灰度开放前无值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_default_cost_center</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新默认成本中心 新默认成本中心的ID，可以通过[【搜索成本中心信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息。
新默认成本中心是否继承字段为true，或者员工新岗位、新部门均无默认成本中心时无值。

- 功能灰度中，成本分摊功能灰度开放前无值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >original_is_default_cost_center_inherited</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	原默认成本中心是否继承 默认成本中心继承逻辑优先取生效日期对应的岗位的默认成本中心，其次取部门的默认成本中心。

- 功能灰度中，成本分摊功能灰度开放前无值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_is_default_cost_center_inherited</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	新默认成本中心是否继承 默认成本中心继承逻辑优先取生效日期对应的岗位的默认成本中心，其次取部门的默认成本中心。

- 功能灰度中，成本分摊功能灰度开放前无值。
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
	原职等， 可通过[查询单个职等](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)获取详情。

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
	新职等，  可通过[查询单个职等](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)获取详情。

**字段权限要求（满足任一）**：
<md-perm name="corehr:employment.job_grade:read" desc="获取职等信息" support_app_types="custom" tags="">获取职等信息</md-perm>
<md-perm name="corehr:employment.job_grade:write" desc="读写职等信息" support_app_types="custom" tags="">读写职等信息</md-perm>
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
	原岗位
- 功能灰度中，开通岗位功能后可通过接口【查询岗位信息】获取详情。
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
	新岗位
- 功能灰度中，如果是一个已存在的岗位，开通岗位功能后可通过接口【查询岗位信息】获取详情。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >target_draft_position</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	新岗位(调整过程岗位 ID )
- 对于在本次调整中新建的岗位，在调整未生效前会返回格式为 td_xxx 的过程岗位 ID，生效后将返回正式的岗位ID
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
        "job_changes": [
            {
                "job_change_id": "6991776076699549697",
                "employment_id": "ou_a294793e8fa21529f2a60e3e9de45520",
                "transfer_info": {
                    "original_department": "6966236933198579208",
                    "target_department": "6966236933198579208",
                    "target_draft_department": "td_704442734715974602312",
                    "original_department_id_path": [
                        {
                            "department_id": "6974659700705068581",
                            "draft_department_id": "6974659700705068581"
                        }
                    ],
                    "target_department_id_path": [
                        {
                            "department_id": "6974659700705068581",
                            "draft_department_id": "6974659700705068581"
                        }
                    ],
                    "original_direct_manager": "6974641477444060708",
                    "target_direct_manager": "7013619729281713671",
                    "original_job": "6969469398088287751",
                    "target_job": "6969469557836760606",
                    "original_job_family": "6967287547462419975",
                    "target_job_family": "6967287547462419975",
                    "original_job_level": "6972085707674355214",
                    "target_job_level": "6972085707674355214",
                    "original_cost_center_rate": [
                        {
                            "cost_center_id": "6950635856373745165",
                            "rate": 100,
                            "new_rate": 50.2
                        }
                    ],
                    "target_cost_center_rate": [
                        {
                            "cost_center_id": "6950635856373745165",
                            "rate": 100,
                            "new_rate": 50.2
                        }
                    ],
                    "target_allocation_expiration_time": "2022-03-01 00:00:00",
                    "original_allocation_expiration_time": "2022-03-01 00:00:00",
                    "target_allocation_effective_time": "2022-03-01 00:00:00",
                    "original_allocation_effective_time": "2022-03-01 00:00:00",
                    "original_default_cost_center": "7380264299728602661",
                    "target_default_cost_center": "7380264299728602661",
                    "original_is_default_cost_center_inherited": true,
                    "target_is_default_cost_center_inherited": false,
                    "original_job_grade": "7289005963599693366",
                    "target_job_grade": "7289005963599693366",
                    "original_position": "7289005963599693367",
                    "target_position": "7289005963599693367",
                    "target_draft_position": "td_7289005963599693367"
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
  <md-td>200</md-td>
  <md-td>1162001</md-td>
  <md-td>Approval process not found</md-td>
  <md-td>请检查审批流 ID 是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>1161000</md-td>
  <md-td>Adjustment draft not found</md-td>
  <md-td>请检查人员异动记录 ID 是否正确</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




