---
title: "获取投递详情"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get_detail"
updateTime: "1764644288000"
---

# 获取投递详情

根据投递 ID 获取投递信息并通过参数按需获取该投递相关的实体信息，如「职位」、「人才」、「评估」、「面试」、「Offer」、「猎头」、「内推」、「官网」等实体的信息。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=hire&version=v1&resource=application&method=get_detail)

:::html
<md-alert type="tip">
目前暂不支持查询被删除的投递详情
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
      <md-td>https://open.feishu.cn/open-apis/hire/v1/applications/:application_id/get_detail</md-td>
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
            <md-perm name="hire:application" desc="更新投递信息" support_app_types="custom,isv" tags="">更新投递信息</md-perm>
            <md-perm name="hire:application:readonly" desc="获取投递信息" support_app_types="custom,isv" tags="">获取投递信息</md-perm>
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
        <md-perm name="hire:agency:readonly" desc="获取招聘猎头信息" support_app_types="custom,isv" tags="">获取招聘猎头信息</md-perm>
        <md-perm name="hire:agency_salary:readonly" desc="获取猎头填写的薪资" support_app_types="custom,isv" tags="">获取猎头填写的薪资</md-perm>
        <md-perm name="hire:employee" desc="更新招聘员工信息" support_app_types="custom,isv" tags="">更新招聘员工信息</md-perm>
        <md-perm name="hire:employee:readonly" desc="获取招聘员工信息" support_app_types="custom,isv" tags="">获取招聘员工信息</md-perm>
        <md-perm name="hire:evaluation:readonly" desc="获取简历评估信息" support_app_types="custom,isv" tags="">获取简历评估信息</md-perm>
        <md-perm name="hire:interview:readonly" desc="获取面试信息" support_app_types="custom,isv" tags="">获取面试信息</md-perm>
        <md-perm name="hire:job:readonly" desc="获取职位信息" support_app_types="custom,isv" tags="">获取职位信息</md-perm>
        <md-perm name="hire:offer:readonly" desc="获取 offer 信息" support_app_types="custom,isv" tags="">获取 offer 信息</md-perm>
        <md-perm name="hire:offer_salary:readonly" desc="获取 Offer 薪酬" support_app_types="custom,isv" tags="">获取 Offer 薪酬</md-perm>
        <md-perm name="hire:referral:readonly" desc="获取内推信息" support_app_types="custom,isv" tags="">获取内推信息</md-perm>
        <md-perm name="hire:site:readonly" desc="获取官网信息" support_app_types="custom,isv" tags="">获取官网信息</md-perm>
        <md-perm name="hire:talent:readonly" desc="获取人才信息" support_app_types="custom,isv" tags="">获取人才信息</md-perm>
        <md-perm name="hire:interview" desc="更新面试信息" support_app_types="custom" tags="">更新面试信息</md-perm>
        <md-perm name="hire:agency" desc="更新招聘猎头信息" support_app_types="custom" tags="">更新招聘猎头信息</md-perm>
        <md-perm name="hire:referral" desc="更新内推信息" support_app_types="custom" tags="">更新内推信息</md-perm>
        <md-perm name="hire:job" desc="更新职位信息" support_app_types="custom" tags="">更新职位信息</md-perm>
        <md-perm name="hire:site" desc="更新官网信息" support_app_types="custom" tags="">更新官网信息</md-perm>
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
        <md-perm name="hire:talent" desc="更新人才信息" support_app_types="custom" tags="">更新人才信息</md-perm>
        <md-perm name="hire:offer" desc="更新 offer 信息" support_app_types="custom" tags="">更新 offer 信息</md-perm>
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
	<md-text type="field-name" >application_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递 ID，可通过[获取投递列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/list)接口获取

**示例值**："6956499586395523359"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
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
<md-enum-item key="people_admin_id" >以people_admin_id来识别用户,即将下线字段,不建议使用</md-enum-item>
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
<md-enum-item key="open_department_id" >以 open_department_id 来标识部门，通过[批量获取部门信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/batch)接口获取</md-enum-item>
<md-enum-item key="department_id" >以 department_id 来标识部门，通过[批量获取部门信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/batch)接口获取</md-enum-item>
</md-enum>

**默认值**：`open_department_id`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_level_id_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	此次调用中使用的「职级 ID」的类型

**示例值**：job_level_id

**可选值有**：
<md-enum>
<md-enum-item key="people_admin_job_level_id" >「人力系统管理后台」适用的职级 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。</md-enum-item>
<md-enum-item key="job_level_id" >「飞书管理后台」适用的职级 ID，通过[获取租户职级列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/list)接口获取</md-enum-item>
</md-enum>

**默认值**：`job_level_id`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_family_id_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	此次调用中使用的「序列 ID」的类型

**示例值**：job_family_id

**可选值有**：
<md-enum>
<md-enum-item key="people_admin_job_category_id" >「人力系统管理后台」适用的序列 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。</md-enum-item>
<md-enum-item key="job_family_id" >「飞书管理后台」适用的序列 ID，通过[获取租户序列列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/list)接口获取</md-enum-item>
</md-enum>

**默认值**：`job_family_id`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >employee_type_id_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	此次调用中使用的「人员类型 ID」的类型

**示例值**：employee_type_enum_id

**可选值有**：
<md-enum>
<md-enum-item key="people_admin_employee_type_id" >「人力系统管理后台」适用的人员类型 ID。人力系统管理后台逐步下线中，建议不继续使用此 ID。</md-enum-item>
<md-enum-item key="employee_type_enum_id" >「飞书管理后台」适用的人员类型 ID，通过[查询人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)接口获取</md-enum-item>
</md-enum>

**默认值**：`employee_type_enum_id`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >options</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	关联实体信息获取参数，用于指定获取哪些关联实体信息，不传时默认只返回投递基本信息（`basic_info`）。如需一次查询多个实体信息，可通过将同一参数名多次传递，并且每次传递不同的参数值。
 <br>

例如：https://{url}?options=with_job&options=with_talent


**示例值**：with_job

**可选值有**：
<md-enum>
<md-enum-item key="with_job" >返回职位实体信息</md-enum-item>
<md-enum-item key="with_talent" >返回人才实体信息</md-enum-item>
<md-enum-item key="with_interview" >返回面试聚合实体信息</md-enum-item>
<md-enum-item key="with_offer" >返回 Offer 实体信息</md-enum-item>
<md-enum-item key="with_evaluation" >返回评估实体信息</md-enum-item>
<md-enum-item key="with_employee" >返回员工实体信息</md-enum-item>
<md-enum-item key="with_agency" >返回猎头实体信息</md-enum-item>
<md-enum-item key="with_referral" >返回内推实体信息</md-enum-item>
<md-enum-item key="with_portal" >返回官网实体信息</md-enum-item>
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
	<md-text type="field-name" >application_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_detail_info</md-text>
	</md-dt-td>
	<md-dt-td>
	投递详情
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >basic_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_detail_basic_info</md-text>
	</md-dt-td>
	<md-dt-td>
	投递基本信息
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
	投递 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >job_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	职位 ID，详情请查看：[获取职位信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >talent_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	人才 ID，详情请查看：[获取人才信息 V1](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >stage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_stage_info</md-text>
	</md-dt-td>
	<md-dt-td>
	投递处于的阶段
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
	投递阶段 ID，详情可查看：[获取招聘流程信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_process/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >zh_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递阶段中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >en_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递阶段英文名称
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
	阶段类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >筛选型</md-enum-item>
<md-enum-item key="2" >评估型</md-enum-item>
<md-enum-item key="3" >笔试型</md-enum-item>
<md-enum-item key="4" >面试型</md-enum-item>
<md-enum-item key="5" >Offer型</md-enum-item>
<md-enum-item key="6" >待入职</md-enum-item>
<md-enum-item key="7" >已入职</md-enum-item>
<md-enum-item key="8" >其它类型</md-enum-item>
<md-enum-item key="255" >系统默认</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >active_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	投递活跃状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >活跃</md-enum-item>
<md-enum-item key="2" >非活跃</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >delivery_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	投递方式

**可选值有**：
<md-enum>
<md-enum-item key="1" >HR寻访</md-enum-item>
<md-enum-item key="2" >候选人主动投递</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >resume_source_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_resume_source</md-text>
	</md-dt-td>
	<md-dt-td>
	投递来源信息
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
	投递来源 ID，详情请查看[获取简历来源列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/resume_source/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	投递来源名称
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
	投递来源中文名称
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
	投递来源英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >resume_source_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	投递来源类型

**可选值有**：
<md-enum>
<md-enum-item key="10000" >内推</md-enum-item>
<md-enum-item key="10001" >猎头</md-enum-item>
<md-enum-item key="10002" >内部来源</md-enum-item>
<md-enum-item key="10003" >第三方招聘网站</md-enum-item>
<md-enum-item key="10004" >社交媒体</md-enum-item>
<md-enum-item key="10005" >线下来源</md-enum-item>
<md-enum-item key="10006" >其他</md-enum-item>
<md-enum-item key="10007" >外部推荐</md-enum-item>
<md-enum-item key="10008" >员工转岗</md-enum-item>
<md-enum-item key="10009" >实习生转正</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >website_resume_source</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_website_resume_source</md-text>
	</md-dt-td>
	<md-dt-td>
	官网投递来源（当从官网进行投递时返回）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >website_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	官网站点 ID，详情请查看：[获取招聘官网列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website/list)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >website_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	官网站点名称
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
	官网站点中文名称
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
	官网站点英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >channel</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_website_channel</md-text>
	</md-dt-td>
	<md-dt-td>
	推广渠道来源
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >channel_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	推广渠道 ID，详情请查看[获取招聘官网推广渠道列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website-channel/list)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >channel_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	推广渠道名称
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
	推广渠道中文名称
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
	推广渠道英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >talent_attachment_resume_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	简历附件 ID，详情请查看 ：[获取附件信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get)，
「备注信息：只有站内创投时上传的简历附件才能关联取值，渠道/官网/内推创投的简历附件不会关联」

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >stage_time_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_stage_time\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	投递阶段变更时间列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >stage_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	阶段 ID，详情请查看：[获取招聘流程信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_process/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >enter_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最近一次进入该阶段的时间（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >exit_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最后一次离开时间（单位：毫秒），如当前在该阶段，则为空
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >onboard_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	投递入职状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >未入职</md-enum-item>
<md-enum-item key="2" >已入职</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >application_preferred_city_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >code_name_object\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	意向投递城市列表
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
	城市编码，详情请参考：[查询地点列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/query)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	城市名称
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
	城市中文名称
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
	城市英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >termination_reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >termination_reason_info</md-text>
	</md-dt-td>
	<md-dt-td>
	投递终止原因
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
	终止原因 ID，详情请查看：[获取终止投递原因](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/termination_reason/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	终止原因名称
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
	终止原因中文名称
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
	终止原因英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >children</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >termination_reason_child_info\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	子级终止原因
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	终止原因 ID，详情请查看：[获取终止投递原因](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/termination_reason/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	终止原因名称
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
	终止原因中文名称
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
	终止原因英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >creator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递创建者 ID，与入参 `user_id_type` 类型一致
<br>

**注意**：
仅当投递创建人为企业内部员工时可获取（如员工手动上传简历 / 加入职位 / 内推），其余情况返回为空（如候选人主动投递。当投递创建者是外部租户，user_id_type默认为lark_id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >owner_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递所有者 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >terminator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递终止者 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	创建时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >modify_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	修改时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >job</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >job_basic_info</md-text>
	</md-dt-td>
	<md-dt-td>
	投递职位信息

**字段权限要求（满足任一）**：
<md-perm name="hire:job:readonly" desc="获取职位信息" support_app_types="custom,isv" tags="">获取职位信息</md-perm>
<md-perm name="hire:job" desc="更新职位信息" support_app_types="custom" tags="">更新职位信息</md-perm>
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
	职位 ID，详情请查看：[获取职位信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	职位名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	职位编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >talent</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >talent_basic_info_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	投递人才信息

**字段权限要求（满足任一）**：
<md-perm name="hire:talent:readonly" desc="获取人才信息" support_app_types="custom,isv" tags="">获取人才信息</md-perm>
<md-perm name="hire:talent" desc="更新人才信息" support_app_types="custom" tags="">更新人才信息</md-perm>
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
	人才 ID，详情请查看：[获取人才信息 V1](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	人才名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >mobile_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	人才手机国家区号
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >mobile_number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	人才手机号
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
	人才邮箱
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >evaluations</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >evaluation\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	投递评估信息

**字段权限要求**：
<md-perm name="hire:evaluation:readonly" desc="获取简历评估信息" support_app_types="custom,isv" tags="">获取简历评估信息</md-perm>
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
	评估 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >application_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递 ID，详情请查看：[获取投递信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >stage_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递阶段 ID，详情请查看：[获取招聘流程信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_process/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >creator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	创建人用户 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >evaluator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人用户 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >commit_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	提交状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >已提交</md-enum-item>
<md-enum-item key="2" >未提交</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >conclusion</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	评估结论

**可选值有**：
<md-enum>
<md-enum-item key="1" >通过</md-enum-item>
<md-enum-item key="2" >未通过</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >content</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估详情
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估创建时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >update_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估最近更新时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >interview_aggregation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >interview_aggregation</md-text>
	</md-dt-td>
	<md-dt-td>
	投递面试信息

**字段权限要求（满足任一）**：
<md-perm name="hire:interview:readonly" desc="获取面试信息" support_app_types="custom,isv" tags="">获取面试信息</md-perm>
<md-perm name="hire:interview" desc="更新面试信息" support_app_types="custom" tags="">更新面试信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >interviews</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >interview_extend_v2\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	面试信息列表
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
	面试 ID，详情请查看：[获取面试信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview/list)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >begin_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试开始时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >end_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试结束时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >round</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	面试轮次（从0开始计数）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >interview_record_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >interview_record_v2\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价 ID，详情请查看：[获取面试评价详细信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/hire-v2/interview_record/get)


	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >feedback_form_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价表 ID，详情请查看：[获取面试评价表列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >commit_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	提交状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >已提交</md-enum-item>
<md-enum-item key="2" >未提交</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >submit_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价提交时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >record_score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >record_score</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价分数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价得分（精确到小数点后两位）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >total_score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价总分（精确到小数点后两位）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >interviewer</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >basic_user_info</md-text>
	</md-dt-td>
	<md-dt-td>
	面试官信息
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
	面试官用户 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	面试官名称
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
	面试官中文名称
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
	面试官英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >attachments</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >interview_attachment\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价附件列表
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
	附件 ID，详情请查看：[获取附件信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get)
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
	附件名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >content_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	附件类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	附件创建时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >module_assessments</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >module_assessment\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	模块评价列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >interview_feedback_form_module_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价表模块 ID，详情请查看：[获取面试评价表列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)
接口中的 module 的 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >module_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	模块名称
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
	模块中文名称
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
	模块英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >module_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	模块类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >系统预置「面试结论」模块</md-enum-item>
<md-enum-item key="2" >自定义模块（无模块名称）</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >module_weight</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	模块权重
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >module_score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	模块打分（精确到小数点后两位）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >dimension_assessments</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dimension_assessment\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	模块评价
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >interview_feedback_form_dimension_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	对应模版中维度 ID，详情请查看：[获取面试评价表列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_feedback_form/list)
接口中的 dimension 的 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >dimension_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	维度名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	维度中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	维度英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >dimension_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	维度类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >单选题</md-enum-item>
<md-enum-item key="2" >多选题</md-enum-item>
<md-enum-item key="3" >描述题</md-enum-item>
<md-enum-item key="5" >职级建议</md-enum-item>
<md-enum-item key="6" >打分题(单选)</md-enum-item>
<md-enum-item key="7" >打分题(填空)</md-enum-item>
<md-enum-item key="10" >系统预置-结论</md-enum-item>
<md-enum-item key="11" >系统预置-得分</md-enum-item>
<md-enum-item key="12" >系统预置-记录</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >weight</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	维度权重
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >dimension_content</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	当维度类型为描述题时，从此取值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >dimension_option</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dimension_option</md-text>
	</md-dt-td>
	<md-dt-td>
	当维度类型为单选题时，从此取值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	选项 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	选项名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	选项中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	选项英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >score_val</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	选项对应的分数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >dimension_options</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dimension_option\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	当维度类型为多选题时，从此取值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	选项 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	选项名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	选项中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	选项英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >score_val</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	选项对应的分数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >dimension_score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	当维度评价方式为「打分题(填空)时」，从此取值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >recommended_job_level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >recommended_job_level</md-text>
	</md-dt-td>
	<md-dt-td>
	当维度为「职级建议」时，从此取值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >lower_limit_job_level_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	最低职级建议
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最低职级中文建议
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最低职级英文建议
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >higher_limit_job_level_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	最高职级建议
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最高职级中文建议
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最高职级英文建议
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >question_assessments</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >question_assessment\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	维度关联面试题
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >question_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	所关联面试题的类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >普通面试题目</md-enum-item>
<md-enum-item key="2" >在线编程题目</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	关联面试题的名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	关联面试题的中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	关联面试题的英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	关联面试题的描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	关联面试题的中文描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	关联面试题的英文描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >content</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试者作答内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >abilities</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >ability\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	能力项列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	能力项 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	能力项名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="10">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	能力项中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="10">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	能力项英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="9">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	能力项描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="10">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	能力项中文描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="10">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	能力项英文描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >feedback_submit_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试评价提交时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >stage_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试关联的投递阶段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >application_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递 ID，详情请查看：[获取投递信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >stage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	阶段信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	阶段 ID，详情请查看：[获取招聘流程信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_process/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	阶段名称
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
	阶段中文名称
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
	阶段英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >creator</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	创建人
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	创建人 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	创建人名称
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
	创建人中文名称
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
	创建人英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	创建时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >update_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	更新时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >interview_round_summary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	面试状态

**可选值有**：
<md-enum>
<md-enum-item key="2" >未开始</md-enum-item>
<md-enum-item key="3" >全部未评价</md-enum-item>
<md-enum-item key="4" >全部通过</md-enum-item>
<md-enum-item key="5" >全部淘汰</md-enum-item>
<md-enum-item key="6" >爽约</md-enum-item>
<md-enum-item key="7" >部分评价且均评价通过</md-enum-item>
<md-enum-item key="8" >部分评价且评价中有通过有淘汰的</md-enum-item>
<md-enum-item key="9" >部分评价且均评价淘汰</md-enum-item>
<md-enum-item key="10" >所有面试官都提交评价且评价中有通过有淘汰的</md-enum-item>
<md-enum-item key="11" >部分评价且评价中有通过和待定的</md-enum-item>
<md-enum-item key="12" >部分评价且评价中有淘汰和待定的</md-enum-item>
<md-enum-item key="13" >部分评级且评价均为待定</md-enum-item>
<md-enum-item key="14" >部分评价且评价中有通过、待定和淘汰的</md-enum-item>
<md-enum-item key="15" >所有面试官都提交评价且评价中有通过和待定的</md-enum-item>
<md-enum-item key="16" >所有面试官都提交评价且评价中有待定和淘汰的</md-enum-item>
<md-enum-item key="17" >所有面试官都提交评价且评价均为待定</md-enum-item>
<md-enum-item key="18" >所有面试官都提交评价且评价中有通过、待定、淘汰的</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >interview_arrangement_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试安排 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >interview_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	面试类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >现场面试</md-enum-item>
<md-enum-item key="2" >电话面试</md-enum-item>
<md-enum-item key="3" >视频面试</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >talent_time_zone</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >code_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	候选人时区
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	时区编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	时区名称
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
	时区中文名称
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
	时区英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >contact_user</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	面试联系人
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试联系人 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	面试联系人名称
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
	面试联系人中文名称
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
	面试联系人英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >contact_mobile</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试联系人电话
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
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


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >address</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_address_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	面试地点
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	地点 ID，详情请查看：[获取地址列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	地点名称
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
	地点中文名称
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
	地点英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >district</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	区域信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	区域名称
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
	区域中文名称
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
	区域英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	区域编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY 国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >city</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	城市信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	城市名称
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
	城市中文名称
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
	城市英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	城市编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY 国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >state</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	省信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	省名称
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
	省中文名称
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
	省英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	省编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY 国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >country</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	国家信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	国家名称
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
	国家中文名称
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
	国家英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	国家编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY 国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >video_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	视频面试工具

**可选值有**：
<md-enum>
<md-enum-item key="1" >Zoom</md-enum-item>
<md-enum-item key="2" >牛客技术类型</md-enum-item>
<md-enum-item key="3" >牛客非技术类型</md-enum-item>
<md-enum-item key="4" >赛码</md-enum-item>
<md-enum-item key="5" >Lark</md-enum-item>
<md-enum-item key="8" >Hackerrank</md-enum-item>
<md-enum-item key="9" >飞书（含代码考核）</md-enum-item>
<md-enum-item key="100" >不使用系统工具</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >arrangement_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	当安排类型为集中面试时，此值表示集中面试的安排状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >未开始</md-enum-item>
<md-enum-item key="2" >进行中</md-enum-item>
<md-enum-item key="3" >已结束</md-enum-item>
<md-enum-item key="4" >已取消</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >arrangement_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	安排类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >社招单面</md-enum-item>
<md-enum-item key="2" >集中面试</md-enum-item>
<md-enum-item key="3" >集体面试</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >arrangement_appointment_kind</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	安排方式（是否使用自助约面）

**可选值有**：
<md-enum>
<md-enum-item key="1" >直接安排</md-enum-item>
<md-enum-item key="2" >自助约面</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >meeting_room_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >interview_meeting_room\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	面试会议室
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >room_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	会议室 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >room_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	会议室名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >building_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	建筑名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >reserved_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	会议室预定状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >预约中</md-enum-item>
<md-enum-item key="2" >预约成功</md-enum-item>
<md-enum-item key="3" >预约失败</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >floor_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	楼层
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >interview_round_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	面试轮次类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	面试轮次类型 ID，详情可查看：[获取面试轮次类型列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/interview_round_type/list)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	面试轮次类型名称
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
	面试轮次类型中文名称
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
	面试轮次类型英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >offer</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >offer_info_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	投递 Offer 信息（正式offer）

**字段权限要求（满足任一）**：
<md-perm name="hire:offer:readonly" desc="获取 offer 信息" support_app_types="custom,isv" tags="">获取 offer 信息</md-perm>
<md-perm name="hire:offer" desc="更新 offer 信息" support_app_types="custom" tags="">更新 offer 信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >offer_basic</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >offer_basic_info_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 基本信息
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
	Offer ID，详情请查看：[获取 Offer 详情](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/get)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >offer_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 状态

**可选值有**：
<md-enum>
<md-enum-item key="10" >Offer 已创建</md-enum-item>
<md-enum-item key="2" >Offer 审批中</md-enum-item>
<md-enum-item key="3" >Offer 审批已撤回</md-enum-item>
<md-enum-item key="4" >Offer 审批通过</md-enum-item>
<md-enum-item key="5" >Offer 审批不通过</md-enum-item>
<md-enum-item key="6" >Offer 已发送</md-enum-item>
<md-enum-item key="7" >Offer 被候选人接受</md-enum-item>
<md-enum-item key="8" >Offer 被候选人拒绝</md-enum-item>
<md-enum-item key="9" >Offer 已失效</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >leader</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >basic_user_info</md-text>
	</md-dt-td>
	<md-dt-td>
	直属上级
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	直属上级名称
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
	直属上级中文名称
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
	直属上级英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >employee_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	人员类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	人员类型 ID，与入参 `employee_type_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	人员类型名称
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
	人员类型中文名称
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
	人员类型英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >department</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >basic_department_info</md-text>
	</md-dt-td>
	<md-dt-td>
	部门
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	部门 ID，与入参 `department_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	部门名称
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
	部门中文名称
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
	部门英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >sequence</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	序列
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	序列 ID，与入参 `job_family_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	序列名称
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
	序列中文名称
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
	序列英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >level</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	级别
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	级别 ID，与入参  `job_level_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	级别名称
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
	级别中文名称
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
	级别英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >company_main_body</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object</md-text>
	</md-dt-td>
	<md-dt-td>
	公司主体
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	公司主体 ID，详情可查看：[查询单个公司](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	公司主体名称
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
	公司主体中文名称
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
	公司主体英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >job_requirement_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	招聘需求 ID，详情请查看：[获取招聘需求信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement/list_by_id)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >probation_month</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	试用期（单位：月）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >contract_period</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >contract_period_info</md-text>
	</md-dt-td>
	<md-dt-td>
	合同期（年/月）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >period_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	合同周期类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >月</md-enum-item>
<md-enum-item key="2" >年</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >period</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	合同时长
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >onboard_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	入职日期，格式为 YYYY-MM-DD
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >owner</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >basic_user_info</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 负责人
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 负责人用户 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 负责人名称
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
	Offer 负责人中文名称
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
	Offer 负责人英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >onboard_address</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_address_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	入职地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	入职地址 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	入职地址名称
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
	入职地址中文名称
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
	入职地址英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >district</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	区域信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	区域名称
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
	区域中文名称
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
	区域英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	区域编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY  国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >city</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	城市信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	城市名称
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
	城市中文名称
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
	城市英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY  国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >state</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	省信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	省名称
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
	省中文名称
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
	省英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	省编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY  国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >country</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	国家信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	国家名称
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
	国家中文名称
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
	国家英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	国家编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY  国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >work_address</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_address_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	工作地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	工作地址 ID，详情请查看：[获取地址列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/location/list)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	工作地址名称
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
	工作地址中文名称
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
	工作地址中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >district</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	区域信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	区域信息名称
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
	区域信息中文名称
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
	区域信息英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	区域编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY  国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >city</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	城市信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	城市信息名称
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
	城市信息中文名称
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
	城市信息英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	城市编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY 国家 </md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >state</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	省信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	省名称
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
	省中文名称
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
	省英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	省编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY 国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >country</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >base_location</md-text>
	</md-dt-td>
	<md-dt-td>
	国家信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	国家信息名称
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
	国家信息中文名称
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
	国家信息英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	国家编码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >location_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	地址类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >COUNTRY 国家</md-enum-item>
<md-enum-item key="2" >STATE 省</md-enum-item>
<md-enum-item key="3" >CITY 市</md-enum-item>
<md-enum-item key="4" >DISTRICT 区</md-enum-item>
<md-enum-item key="5" >ADDRESS 地址</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >remark</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 备注
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >attachment_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >offer_attachment_info\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	附件列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 附件 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 附件名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >size</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 附件大小
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >common_attachment_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 通用附件 ID 列表，可通过[获取附件信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get)接口获取附件的详细信息

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >customize_info_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_offer_custom_value\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 自定义字段数据
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >object_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段 ID，详情可查看：[获取 Offer 申请表信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >customize_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段 Value
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 创建时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >offer_salary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >offer_salary_info_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer 薪酬信息

**字段权限要求**：
<md-perm name="hire:offer_salary:readonly" desc="获取 Offer 薪酬" support_app_types="custom,isv" tags="">获取 Offer 薪酬</md-perm>
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
	薪酬 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >salary_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	薪酬状态

**可选值有**：
<md-enum>
<md-enum-item key="0" >薪酬未创建</md-enum-item>
<md-enum-item key="1" >薪酬已创建</md-enum-item>
<md-enum-item key="2" >薪酬审批中</md-enum-item>
<md-enum-item key="3" >薪酬无需审批</md-enum-item>
<md-enum-item key="4" >薪酬审批已通过</md-enum-item>
<md-enum-item key="5" >薪酬审批已拒绝</md-enum-item>
<md-enum-item key="6" >薪酬已撤回</md-enum-item>
<md-enum-item key="7" >薪酬已删除</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >probation_salary_percentage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	试用期百分比
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >award_salary_multiple</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	年终奖月数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >option_shares</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	期权股数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >quarterly_bonus</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	季度奖金额，单位元、支持小数点后两位
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >half_year_bonus</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	半年奖金额，单位元、支持小数点后两位
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >total_annual_cash</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	年度现金总额（数量，非公式），单位元、支持小数点后两位
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >customize_info_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_offer_custom_value\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	薪酬自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >object_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段 ID，详情可查看：[获取 Offer 申请表信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_application_form/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >customize_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段 Value
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	薪酬创建时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employee</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >employee_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	投递员工入转离信息

**字段权限要求（满足任一）**：
<md-perm name="hire:employee" desc="更新招聘员工信息" support_app_types="custom,isv" tags="">更新招聘员工信息</md-perm>
<md-perm name="hire:employee:readonly" desc="获取招聘员工信息" support_app_types="custom,isv" tags="">获取招聘员工信息</md-perm>
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
	员工 ID，详情请查看：[通过员工 ID 获取入职信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/employee/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >application_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递 ID，详情请查看：[获取投递信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >onboard_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	入职状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >已入职</md-enum-item>
<md-enum-item key="2" >已离职</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >conversion_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	转正状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >未转正</md-enum-item>
<md-enum-item key="2" >已转正</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >onboard_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	实际入职时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >expected_conversion_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	预期转正时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >actual_conversion_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	实际转正时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >overboard_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >overboard_note</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >onboard_city_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	办公地点
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >department_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	入职部门 ID，与入参 `department_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >leader_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	直属上级 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >sequence_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	序列 ID，与入参 `job_family_id_type` 类型一致 
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >level_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	职级 ID，与入参 `job_level_id_type` 类型一致 
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >employee_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	人员类型，与入参 `employee_type_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >job_requirement_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	招聘需求 ID，详情请查看：[获取招聘需求信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_requirement/list_by_id)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >agency</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >agency_info</md-text>
	</md-dt-td>
	<md-dt-td>
	投递猎头推荐信息

**字段权限要求（满足任一）**：
<md-perm name="hire:agency:readonly" desc="获取招聘猎头信息" support_app_types="custom,isv" tags="">获取招聘猎头信息</md-perm>
<md-perm name="hire:agency" desc="更新招聘猎头信息" support_app_types="custom" tags="">更新招聘猎头信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >basic_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >agency_basic_info</md-text>
	</md-dt-td>
	<md-dt-td>
	猎头基本信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >hunter_user_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	猎头用户名
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
	猎头中文用户名
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
	猎头英文用户名
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >hunter_company_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	猎头公司名
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >comment_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >report_custom_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	猎头评价信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	猎头评价信息名称
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
	猎头评价信息中文名称
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
	猎头评价信息英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	猎头评价内容
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
	猎头评价中文内容
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
	猎头评价英文内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	猎头评价信息描述
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
	猎头评价信息中文描述
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
	猎头评价信息英文描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >salary_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >report_custom_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	薪酬信息

**字段权限要求**：
<md-perm name="hire:agency_salary:readonly" desc="获取猎头填写的薪资" support_app_types="custom,isv" tags="">获取猎头填写的薪资</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	薪酬信息名称
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
	薪酬信息中文名称
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
	薪酬信息英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	薪酬信息内容
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
	薪酬信息中文内容
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
	薪酬信息英文内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	薪酬信息描述
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
	薪酬信息中文描述
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
	薪酬信息英文描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >portal</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_detail_portal_info</md-text>
	</md-dt-td>
	<md-dt-td>
	投递官网信息

**字段权限要求（满足任一）**：
<md-perm name="hire:site:readonly" desc="获取官网信息" support_app_types="custom,isv" tags="">获取官网信息</md-perm>
<md-perm name="hire:site" desc="更新官网信息" support_app_types="custom" tags="">更新官网信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >campus_volunteer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >campus_volumnteer_info</md-text>
	</md-dt-td>
	<md-dt-td>
	校招志愿信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >volunteer_seq</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	志愿顺序
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >referral</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >referral_info_v2</md-text>
	</md-dt-td>
	<md-dt-td>
	投递内推信息

**字段权限要求（满足任一）**：
<md-perm name="hire:referral:readonly" desc="获取内推信息" support_app_types="custom,isv" tags="">获取内推信息</md-perm>
<md-perm name="hire:referral" desc="更新内推信息" support_app_types="custom" tags="">更新内推信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >basic_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >referral_basic_info</md-text>
	</md-dt-td>
	<md-dt-td>
	内推基本信息
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
	内推 ID

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >application_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	投递 ID，详情请查看：[获取投递信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >referral_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	内推类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >意向推荐</md-enum-item>
<md-enum-item key="2" >职位推荐</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >user_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >basic_user_info</md-text>
	</md-dt-td>
	<md-dt-td>
	内推人信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户 ID，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	用户名称
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
	用户中文名称
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
	用户英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	内推创建时间戳（单位：毫秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >referral_method</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	内推方法

**可选值有**：
<md-enum>
<md-enum-item key="1" >正常内推</md-enum-item>
<md-enum-item key="2" >内推码</md-enum-item>
<md-enum-item key="3" >特别内推码</md-enum-item>
<md-enum-item key="4" >H5 内推</md-enum-item>
<md-enum-item key="5" >HR 代为内推</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >recommend_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >referral_recommend_info</md-text>
	</md-dt-td>
	<md-dt-td>
	内推关联推荐信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >relationship</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	与内推人关系

**可选值有**：
<md-enum>
<md-enum-item key="0" >无关系</md-enum-item>
<md-enum-item key="1" >直系亲属</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >familiarity</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	熟悉程度

**可选值有**：
<md-enum>
<md-enum-item key="0" >不熟悉</md-enum-item>
<md-enum-item key="1" >熟悉</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >comment</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	推荐语
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >specific_relationship</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >specific_relationship</md-text>
	</md-dt-td>
	<md-dt-td>
	特殊关系
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >relation_with_candidate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	与候选人的关系

**可选值有**：
<md-enum>
<md-enum-item key="1" >前同事</md-enum-item>
<md-enum-item key="2" >朋友</md-enum-item>
<md-enum-item key="3" >其他</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >extra</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	附加信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >work_ability_familiarity</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	工作能力熟悉程度

**可选值有**：
<md-enum>
<md-enum-item key="1" >非常熟悉</md-enum-item>
<md-enum-item key="2" >比较熟悉</md-enum-item>
<md-enum-item key="3" >一般熟悉</md-enum-item>
<md-enum-item key="4" >不熟悉</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >match_degree</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	匹配度

**可选值有**：
<md-enum>
<md-enum-item key="1" >非常匹配</md-enum-item>
<md-enum-item key="2" >比较匹配</md-enum-item>
<md-enum-item key="3" >一般匹配</md-enum-item>
<md-enum-item key="4" >不匹配</md-enum-item>
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
        "application_detail": {
            "basic_info": {
                "id": "6949805467799537964",
                "job_id": "6843547872837273223",
                "talent_id": "6843547872837273223",
                "stage": {
                    "id": "614218419274131",
                    "zh_name": "面试",
                    "en_name": "Interview",
                    "type": 1
                },
                "active_status": 1,
                "delivery_type": 1,
                "resume_source_info": {
                    "id": "614218419274131",
                    "name": {
                        "zh_cn": "内推",
                        "en_us": "Referral"
                    },
                    "resume_source_type": 10002
                },
                "website_resume_source": {
                    "website_id": "614218419274131",
                    "website_name": {
                        "zh_cn": "新希望官网",
                        "en_us": "New hope offical"
                    },
                    "channel": {
                        "channel_id": "777218419274131",
                        "channel_name": {
                            "zh_cn": "领英",
                            "en_us": "LinkedIn"
                        }
                    }
                },
                "talent_attachment_resume_id": "6960663240925956415",
                "stage_time_list": [
                    {
                        "stage_id": "614218419274131",
                        "enter_time": "1632991542615",
                        "exit_time": "1631509574398"
                    }
                ],
                "onboard_status": 1,
                "application_preferred_city_list": [
                    {
                        "code": "CT _1",
                        "name": {
                            "zh_cn": "北京",
                            "en_us": "Beijing"
                        }
                    }
                ],
                "termination_reason": {
                    "id": "6891258038901016846",
                    "name": {
                        "zh_cn": "候选人拒绝",
                        "en_us": "Candidate rejected"
                    },
                    "children": [
                        {
                            "id": "6891258038901016846",
                            "name": {
                                "zh_cn": "对公司业务不感兴趣",
                                "en_us": "Not interested in company business"
                            }
                        }
                    ]
                },
                "creator_id": "ou_ce613028fe74745421f5dc320bb9c709",
                "owner_id": "ou_ce913028fe74123221f5dc320bb9c709",
                "terminator_id": "ou_ce913028fe74123221f5dc320bb9c709",
                "create_time": "1632990774278",
                "modify_time": "1634801678103"
            },
            "job": {
                "id": "6956499586395523359",
                "name": "后端研发工程师",
                "code": "A75256"
            },
            "talent": {
                "id": "6956499586395523359",
                "name": "小明",
                "mobile_code": "+86",
                "mobile_number": "13563350751",
                "email": "xxx@bytedance.com"
            },
            "evaluations": [
                {
                    "id": "6875295756292425998",
                    "application_id": "6875569957036738823",
                    "stage_id": "6784315427607595268",
                    "creator_id": "ou_aaf83d1b2c856ead36aa9a38784b9a5c",
                    "evaluator_id": "ou_aaf83d1b2c856ead36aa9a38784b9a5c",
                    "commit_status": 1,
                    "conclusion": 1,
                    "content": "这位同学很优秀",
                    "create_time": "1600843767338",
                    "update_time": "1600843937733"
                }
            ],
            "interview_aggregation": {
                "interviews": [
                    {
                        "id": "6949805467799537964",
                        "begin_time": "1618899376474",
                        "end_time": "1618999376474",
                        "round": 0,
                        "interview_record_list": [
                            {
                                "id": "7171693733661327361",
                                "feedback_form_id": "71716937336613273612",
                                "commit_status": 1,
                                "submit_time": "1710405457390",
                                "record_score": {
                                    "score": 85.33,
                                    "total_score": 100
                                },
                                "interviewer": {
                                    "id": "6956499586395523359",
                                    "name": {
                                        "zh_cn": "张三",
                                        "en_us": "Tom cruise"
                                    }
                                },
                                "attachments": [
                                    {
                                        "file_id": "7140517838785481004",
                                        "file_name": "1.13测试1的面试记录.pdf",
                                        "content_type": "application/pdf",
                                        "create_time": "1710399930151"
                                    }
                                ],
                                "module_assessments": [
                                    {
                                        "interview_feedback_form_module_id": "7171693733661327361",
                                        "module_name": {
                                            "zh_cn": "模块一",
                                            "en_us": "Module 1"
                                        },
                                        "module_type": 1,
                                        "module_weight": 10,
                                        "module_score": 10,
                                        "dimension_assessments": [
                                            {
                                                "interview_feedback_form_dimension_id": "7171693733661327361",
                                                "dimension_name": {
                                                    "zh_cn": "维度一",
                                                    "en_us": "Dimension 1"
                                                },
                                                "dimension_type": 1,
                                                "weight": 1,
                                                "dimension_content": "描述题作答",
                                                "dimension_option": {
                                                    "id": "7171693733661327361",
                                                    "name": {
                                                        "zh_cn": "选项一",
                                                        "en_us": "Option 1"
                                                    },
                                                    "score_val": 10
                                                },
                                                "dimension_options": [
                                                    {
                                                        "id": "7171693733661327361",
                                                        "name": {
                                                            "zh_cn": "选项一",
                                                            "en_us": "Option 1"
                                                        },
                                                        "score_val": 10
                                                    }
                                                ],
                                                "dimension_score": 10,
                                                "recommended_job_level": {
                                                    "lower_limit_job_level_name": {
                                                        "zh_cn": "多元化、跨国企业，最低职级建议为 6 - 10 级",
                                                        "en_us": "Diversified, multinational companies, the minimum recommended job level is 6 - 10"
                                                    },
                                                    "higher_limit_job_level_name": {
                                                        "zh_cn": "多元化、跨国企业，最高职级建议为 12 - 14 级",
                                                        "en_us": "Diversified, multinational companies, the maximum recommended job level is 12 - 14"
                                                    }
                                                },
                                                "question_assessments": [
                                                    {
                                                        "question_type": 1,
                                                        "title": {
                                                            "zh_cn": "题目一",
                                                            "en_us": "Question 1"
                                                        },
                                                        "description": {
                                                            "zh_cn": "这是一段对面试题的中文描述",
                                                            "en_us": "This is a description of question 1."
                                                        },
                                                        "content": "我对这道题目的作答是...",
                                                        "abilities": [
                                                            {
                                                                "id": "7270798542321666366",
                                                                "name": {
                                                                    "zh_cn": "创新思维",
                                                                    "en_us": "Creative Thinking"
                                                                },
                                                                "description": {
                                                                    "zh_cn": "创新思维",
                                                                    "en_us": "Creative Thinking"
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ],
                        "feedback_submit_time": "1659318415000",
                        "stage_id": "634324253532232",
                        "application_id": "634324253532232",
                        "stage": {
                            "id": "1213213123123",
                            "name": {
                                "zh_cn": "阶段一",
                                "en_us": "Stage 1"
                            }
                        },
                        "creator": {
                            "id": "1213213123123",
                            "name": {
                                "zh_cn": "张三",
                                "en_us": "Bob"
                            }
                        },
                        "create_time": "1618999376474",
                        "update_time": "1618999376474",
                        "interview_round_summary": 2,
                        "interview_arrangement_id": "6888110869563033870",
                        "interview_type": 1,
                        "talent_time_zone": {
                            "code": "Asia/Shanghai",
                            "name": {
                                "zh_cn": "上海",
                                "en_us": "Shanghai"
                            }
                        },
                        "contact_user": {
                            "id": "1213213123123",
                            "name": {
                                "zh_cn": "王五",
                                "en_us": "Alice"
                            }
                        },
                        "contact_mobile": "13333333333",
                        "remark": "这是一条备注",
                        "address": {
                            "id": "6583482347283472832",
                            "name": {
                                "zh_cn": "北京",
                                "en_us": "Beijing"
                            },
                            "district": {
                                "name": {
                                    "zh_cn": "朝阳区",
                                    "en_us": "Chaoyang District"
                                },
                                "code": "400700",
                                "location_type": 1
                            },
                            "city": {
                                "name": {
                                    "zh_cn": "上海",
                                    "en_us": "Shanghai"
                                },
                                "code": "400700",
                                "location_type": 1
                            },
                            "state": {
                                "name": {
                                    "zh_cn": "湖南省",
                                    "en_us": "Hunan  Province"
                                },
                                "code": "400700",
                                "location_type": 1
                            },
                            "country": {
                                "name": {
                                    "zh_cn": "中国",
                                    "en_us": "China"
                                },
                                "code": "400700",
                                "location_type": 1
                            }
                        },
                        "video_type": 1,
                        "arrangement_status": 1,
                        "arrangement_type": 1,
                        "arrangement_appointment_kind": 1,
                        "meeting_room_list": [
                            {
                                "room_id": "6949805467799537964",
                                "room_name": "OCG111",
                                "building_name": "OCG",
                                "reserved_status": 1,
                                "floor_name": "17"
                            }
                        ],
                        "interview_round_type": {
                            "id": "1213213123123",
                            "name": {
                                "zh_cn": "第一轮",
                                "en_us": "First round"
                            }
                        }
                    }
                ]
            },
            "offer": {
                "offer_basic": {
                    "id": "7056641315456469292",
                    "offer_status": 10,
                    "leader": {
                        "id": "6956499586395523359",
                        "name": {
                            "zh_cn": "张三",
                            "en_us": "Bob"
                        }
                    },
                    "employee_type": {
                        "id": "1213213123123",
                        "name": {
                            "zh_cn": "正式",
                            "en_us": "Regular"
                        }
                    },
                    "department": {
                        "id": "6956499586395523359",
                        "name": {
                            "zh_cn": "HR 部门",
                            "en_us": "HR Department"
                        }
                    },
                    "sequence": {
                        "id": "1213213123123",
                        "name": {
                            "zh_cn": "研发",
                            "en_us": "RD"
                        }
                    },
                    "level": {
                        "id": "1213213123123",
                        "name": {
                            "zh_cn": "3-1",
                            "en_us": "3-1"
                        }
                    },
                    "company_main_body": {
                        "id": "1213213123123",
                        "name": {
                            "zh_cn": "顶呱呱公司",
                            "en_us": "Dingguagua"
                        }
                    },
                    "job_requirement_id": "7018398769038182700",
                    "probation_month": 3,
                    "contract_period": {
                        "period_type": 1,
                        "period": 3
                    },
                    "onboard_date": "2023-01-01",
                    "owner": {
                        "id": "6956499586395523359",
                        "name": {
                            "zh_cn": "赵六",
                            "en_us": "Tom"
                        }
                    },
                    "onboard_address": {
                        "id": "6583482347283472832",
                        "name": {
                            "zh_cn": "成都市高新区天府四街",
                            "en_us": "Tianfu 4th street, Gaoxin district, Chengdu"
                        },
                        "district": {
                            "name": {
                                "zh_cn": "高新区",
                                "en_us": "Gaoxin"
                            },
                            "code": "400700",
                            "location_type": 1
                        },
                        "city": {
                            "name": {
                                "zh_cn": "成都",
                                "en_us": "Chengdu"
                            },
                            "code": "400700",
                            "location_type": 1
                        },
                        "state": {
                            "name": {
                                "zh_cn": "四川",
                                "en_us": "Sichuan"
                            },
                            "code": "400700",
                            "location_type": 1
                        },
                        "country": {
                            "name": {
                                "zh_cn": "中国",
                                "en_us": "China"
                            },
                            "code": "400700",
                            "location_type": 1
                        }
                    },
                    "work_address": {
                        "id": "6583482347283472832",
                        "name": {
                            "zh_cn": "成都市高新区天府四街",
                            "en_us": "Tianfu 4th street, Gaoxin district, Chengdu"
                        },
                        "district": {
                            "name": {
                                "zh_cn": "高新",
                                "en_us": "Gaoxin"
                            },
                            "code": "400700",
                            "location_type": 1
                        },
                        "city": {
                            "name": {
                                "zh_cn": "成都",
                                "en_us": "Chengdu"
                            },
                            "code": "400700",
                            "location_type": 1
                        },
                        "state": {
                            "name": {
                                "zh_cn": "四川",
                                "en_us": "Sichuan"
                            },
                            "code": "400700",
                            "location_type": 1
                        },
                        "country": {
                            "name": {
                                "zh_cn": "中国",
                                "en_us": "China"
                            },
                            "code": "400700",
                            "location_type": 1
                        }
                    },
                    "remark": "这个 Offer 需要加急审批",
                    "attachment_list": [
                        {
                            "id": "7018398769038182700",
                            "name": "获奖证书「全套」",
                            "size": 4096,
                            "common_attachment_id": "7118398769038182701"
                        }
                    ],
                    "customize_info_list": [
                        {
                            "object_id": "6930815272790114324",
                            "customize_value": "This is a text type customized data value"
                        }
                    ],
                    "create_time": "1619719298000"
                },
                "offer_salary": {
                    "id": "6956641395189795116",
                    "salary_status": 1,
                    "probation_salary_percentage": "30%",
                    "award_salary_multiple": "3",
                    "option_shares": "100",
                    "quarterly_bonus": "1000",
                    "half_year_bonus": "3000",
                    "total_annual_cash": "200000",
                    "customize_info_list": [
                        {
                            "object_id": "6930815272790114324",
                            "customize_value": "1"
                        }
                    ],
                    "create_time": "1619720918463"
                }
            },
            "employee": {
                "id": "123",
                "application_id": "6990656563279480364",
                "onboard_status": 1,
                "conversion_status": 1,
                "onboard_time": "1637596800000",
                "expected_conversion_time": "1637596800000",
                "actual_conversion_time": "1637596800000",
                "overboard_time": "1637596800000",
                "overboard_note": "职业发展考虑",
                "onboard_city_code": "C20",
                "department_id": "6966123381141866028",
                "leader_id": "ou-xxx",
                "sequence_id": "6501",
                "level_id": "6301",
                "employee_type": "1",
                "job_requirement_id": "123123123213"
            },
            "agency": {
                "basic_info": {
                    "hunter_user_name": {
                        "zh_cn": "猎头一号",
                        "en_us": "Hunter One"
                    },
                    "hunter_company_name": "明天会更好猎头公司"
                },
                "comment_info": [
                    {
                        "name": {
                            "zh_cn": "能力",
                            "en_us": "Ability"
                        },
                        "value": {
                            "zh_cn": "还不错",
                            "en_us": "Not bad"
                        },
                        "description": {
                            "zh_cn": "这是一段中文的猎头评价信息描述",
                            "en_us": "This is a english comment of comment info"
                        }
                    }
                ],
                "salary_info": [
                    {
                        "name": {
                            "zh_cn": "当前薪资",
                            "en_us": "Current salary"
                        },
                        "value": {
                            "zh_cn": "5000",
                            "en_us": "5000"
                        },
                        "description": {
                            "zh_cn": "这是一段测试描述",
                            "en_us": "This is a test description"
                        }
                    }
                ]
            },
            "portal": {
                "campus_volunteer_info": {
                    "volunteer_seq": 1
                }
            },
            "referral": {
                "basic_info": {
                    "id": "6956498101012220204",
                    "application_id": "7051498101012220201",
                    "referral_type": 1,
                    "user_info": {
                        "id": "6956499586395523359",
                        "name": {
                            "zh_cn": "赵六",
                            "en_us": "Tom"
                        }
                    },
                    "create_time": "1619720918791",
                    "referral_method": 1
                },
                "recommend_info": {
                    "relationship": 1,
                    "familiarity": 0,
                    "comment": "该同学十分优秀，经验丰富。",
                    "specific_relationship": {
                        "relation_with_candidate": 1,
                        "extra": "在前公司合作非常愉快～"
                    },
                    "work_ability_familiarity": 1,
                    "match_degree": 1
                }
            }
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
  <md-td>500</md-td>
  <md-td>1002001</md-td>
  <md-td>system error</md-td>
  <md-td>请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002002</md-td>
  <md-td>parameter error</md-td>
  <md-td>检查参数是否正确，例如类型，大小</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002201</md-td>
  <md-td>application does not exist</md-td>
  <md-td>投递 ID 不合法，请检查 `application_id` 入参是否正确</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




