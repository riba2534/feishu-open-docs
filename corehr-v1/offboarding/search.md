---
title: "搜索离职信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/search"
updateTime: "1758704092000"
---

# 搜索离职信息

该接口支持根据员工ID、离职审批发起时间和离职日期等字段搜索离职信息，可获取包括离职日期、离职原因、离职状态和流程审批状态等信息。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v1&resource=offboarding&method=search)

:::html
<md-alert type="tip">
注意：该接口会按照应用拥有的「员工数据」的权限范围返回数据，请确定在「开发者后台 - 权限管理 - 数据权限-飞书人事（企业版）数据权限」中申请了「员工资源」权限范围。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v1/offboardings/search</md-td>
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
            <md-perm name="corehr:offboarding:read" desc="获取员工离职信息" support_app_types="custom,isv" tags="">获取员工离职信息</md-perm>
            <md-perm name="corehr:offboarding:write" desc="读写员工离职信息" support_app_types="custom" tags="">读写员工离职信息</md-perm>
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
        <md-perm name="corehr:employment.offboarding_reason:read" desc="获取员工离职原因" support_app_types="custom,isv" tags="">获取员工离职原因</md-perm>
        <md-perm name="corehr:offboarding.custom_field:read" desc="获取离职信息自定义字段信息" support_app_types="custom,isv" tags="">获取离职信息自定义字段信息</md-perm>
        <md-perm name="corehr:offboarding.block_list:read" desc="获取离职屏蔽名单" support_app_types="custom" tags="">获取离职屏蔽名单</md-perm>
        <md-perm name="corehr:offboarding.block_list:write" desc="读写离职屏蔽名单" support_app_types="custom" tags="">读写离职屏蔽名单</md-perm>
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
        <md-perm name="corehr:offboarding.last_attendance_date:read" desc="获取离职申请的最后出勤日" support_app_types="custom" tags="">获取离职申请的最后出勤日</md-perm>
        <md-perm name="corehr:offboarding.noncompete_agreement:read" desc="获取离职申请的竞业信息" support_app_types="custom" tags="">获取离职申请的竞业信息</md-perm>
        <md-perm name="corehr:offboarding.retain_account:read" desc="获取离职后是否保留账号字段" support_app_types="custom" tags="">获取离职后是否保留账号字段</md-perm>
        <md-perm name="corehr:offboarding.retain_account:write" desc="读写离职后是否保留账号字段" support_app_types="custom" tags="">读写离职后是否保留账号字段</md-perm>
        <md-perm name="corehr:offboarding.signature:read" desc="获取离职申请的电子签相关字段" support_app_types="custom" tags="">获取离职申请的电子签相关字段</md-perm>
        <md-perm name="corehr:offboarding.social_insurance:read" desc="获取离职申请的社保信息" support_app_types="custom" tags="">获取离职申请的社保信息</md-perm>
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
	雇佣 ID 列表，ID类型与查询参数 user_id_type取值一致：

- 当user_id_type取值为open_id时，ID获取方式参考[如何获取自己的Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)。

- 当user_id_type取值为user_id时，ID获取方式参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)。

- 当user_id_type取值为union_id时，ID获取方式参考[如何获取自己的 Union ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)。

- 当user_id_type取值为people_corehr_id时，先参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。

**示例值**：["7140964208476371111"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >apply_initiating_time_start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职审批发起时间（搜索的起始范围），请按照秒级时间戳格式传入。该字段非必填，需要与离职审批发起时间（搜索的结束范围）一同使用。

**示例值**："1672578336"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >apply_initiating_time_end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职审批发起时间（搜索的结束范围），请按照秒级时间戳格式传入。该字段非必填，需要与离职审批发起时间（搜索的起始范围）一同使用。

**示例值**："1674133537"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >apply_finished_time_start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职审批结束时间（搜索的起始范围），请按照秒级时间戳格式传入。该字段非必填，需要与离职审批结束时间（搜索的结束范围）一同使用。

**示例值**："1641007353"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >apply_finished_time_end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职审批结束时间 （搜索的结束范围），请按照秒级时间戳格式传入。该字段非必填，需要与离职审批结束时间（搜索的起始范围）一同使用。

**示例值**："1641007353"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >expected_offboarding_date_start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	期望离职日期（搜索的起始范围），请按日期格式传入。该字段非必填，需要与期望离职日期（搜索的结束范围）一同使用

**示例值**："2022-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >expected_offboarding_date_end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	期望离职日期（搜索的结束范围），请按日期格式传入。该字段非必填，需要与期望离职日期（搜索的起始范围）一同使用。

**示例值**："2022-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offboarding_date_start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职日期（搜索的起始范围），请按日期格式传入。该字段非必填，需要与离职日期（搜索的结束范围）一同使用。

**示例值**："2022-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offboarding_date_end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职日期（搜索的结束范围），该字段非必填，需要与离职日期（搜索的起始范围）一同使用。

**示例值**："2022-01-01"
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
	离职状态，多个状态之间为「或」的关系。为空时默认搜索所有状态的离职信息。

**示例值**：["Approving"]

**可选值有**：
<md-enum>
<md-enum-item key="Approving" >审批中</md-enum-item>
<md-enum-item key="Approved" >审批通过</md-enum-item>
<md-enum-item key="Offboarded" >已离职</md-enum-item>
<md-enum-item key="Rejected" >已拒绝</md-enum-item>
<md-enum-item key="Withdrawn" >已撤销</md-enum-item>
<md-enum-item key="NoNeedApproval" >无需审批</md-enum-item>
</md-enum>

**数据校验规则**：

- 最大长度：`10`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >reasons</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职原因列表 , 可以通过[【查询员工离职原因列表】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/query)接口获取 ，查询时不返回下级原因相关的离职信息。为空时默认搜索所有离职数据。

<br><b>字段权限要求：</b><br>
<md-perm name="corehr:employment.offboarding_reason.search:read" desc="按照离职原因搜索" support_app_types="custom,isv" tags="">按照离职原因搜索</md-perm>corehr:employment.offboarding_reason.search:read，确认已开通该权限。

**示例值**：["voluntary"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >employee_reasons</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职原因（员工）列表 , 可以通过[【查询员工离职原因列表】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/query)接口获取，查询时不返回下级原因相关的离职信息。为空时默认搜索所有离职数据。

<br><b>字段权限要求：</b><br>
<md-perm name="corehr:employment.offboarding_reason.search:read" desc="按照离职原因搜索" support_app_types="custom,isv" tags="">按照离职原因搜索</md-perm>

**示例值**：["voluntary"]
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
        "7140964208476371111"
    ],
    "apply_initiating_time_start": "1672578336",
    "apply_initiating_time_end": "1674133537",
    "apply_finished_time_start": "1641007353",
    "apply_finished_time_end": "1641007353",
    "expected_offboarding_date_start": "2022-01-01",
    "expected_offboarding_date_end": "2022-01-01",
    "offboarding_date_start": "2022-01-01",
    "offboarding_date_end": "2022-01-01",
    "statuses": [
        "Approving"
    ],
    "reasons": [
        "voluntary"
    ],
    "employee_reasons": [
        "voluntary"
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
	<md-text type="field-type" >offboarding\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	查询的员工离职信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >initiating_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职发起类型，可选项包括：

-offboarding_initiated_by_self：员工申请离职

-offboarding_initiated_by_others：代发起离职申请

-offboarding_directly：直接离职
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
	离职状态

**可选值有**：
<md-enum>
<md-enum-item key="Approving" >审批中</md-enum-item>
<md-enum-item key="Approved" >审批通过</md-enum-item>
<md-enum-item key="Offboarded" >已离职</md-enum-item>
<md-enum-item key="Rejected" >已拒绝</md-enum-item>
<md-enum-item key="Withdrawn" >已撤销</md-enum-item>
<md-enum-item key="NoNeedApproval" >无需审批</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >application_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >application_info</md-text>
	</md-dt-td>
	<md-dt-td>
	离职审批信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >apply_initiator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职审批发起人的雇佣 ID。ID 类型与查询参数 user_id_type 的取值一致。例如，当user_id_type为user_id时，该字段取员工的user_id，若user_id_type为people_corehr_id时，则取该员工的人事雇佣ID。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >apply_initiating_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职申请流程发起时间
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >apply_finish_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职申请流程结束时间
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >process_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	流程 ID。可用于[查询流程相关信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/list)，例如：作为[获取单个流程详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/list)的process_id查询流程详情。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >offboarding_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >offboarding_info</md-text>
	</md-dt-td>
	<md-dt-td>
	员工离职信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >employment_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职员工的雇佣 ID，ID类型与查询参数 user_id_type取值一致：

1、当user_id_type取值为open_id时，ID获取方式参考[如何获取自己的Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)。

2、当user_id_type取值为user_id时，ID获取方式参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)。

3、当user_id_type取值为union_id时，ID获取方式参考[如何获取自己的 Union ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)。

4、当user_id_type取值为people_corehr_id时，先参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >hrbp_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	员工的 hrbp 列表，ID类型与查询参数 user_id_type取值一致：

1、当user_id_type取值为open_id时，ID获取方式参考[如何获取自己的Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)。

2、当user_id_type取值为user_id时，ID获取方式参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)。

3、当user_id_type取值为union_id时，ID获取方式参考[如何获取自己的 Union ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)。

4、当user_id_type取值为people_corehr_id时，先参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >expected_offboarding_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	期望离职日期
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >offboarding_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职日期
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >enum</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因

**字段权限要求**：
<md-perm name="corehr:employment.offboarding_reason:read" desc="获取员工离职原因" support_app_types="custom,isv" tags="">获取员工离职原因</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >enum_name</md-text>
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
	<md-text type="field-name" >display</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举多语展示
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语言
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
	内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >reason_explanation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因说明

**字段权限要求**：
<md-perm name="corehr:employment.offboarding_reason:read" desc="获取员工离职原因" support_app_types="custom,isv" tags="">获取员工离职原因</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >employee_reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >enum</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因（员工）

**字段权限要求**：
<md-perm name="corehr:employment.offboarding_reason:read" desc="获取员工离职原因" support_app_types="custom,isv" tags="">获取员工离职原因</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >enum_name</md-text>
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
	<md-text type="field-name" >display</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举多语展示
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语言
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
	内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >employee_reason_explanation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因说明（员工）

**字段权限要求**：
<md-perm name="corehr:employment.offboarding_reason:read" desc="获取员工离职原因" support_app_types="custom,isv" tags="">获取员工离职原因</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >add_block_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是否加入离职屏蔽名单。注意：该字段为字符类型。可选值有：

-true：是

-false：否

**字段权限要求（满足任一）**：
<md-perm name="corehr:offboarding.block_list:read" desc="获取离职屏蔽名单" support_app_types="custom" tags="">获取离职屏蔽名单</md-perm>
<md-perm name="corehr:offboarding.block_list:write" desc="读写离职屏蔽名单" support_app_types="custom" tags="">读写离职屏蔽名单</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >block_reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >enum</md-text>
	</md-dt-td>
	<md-dt-td>
	屏蔽原因，枚举值可查询
[【获取字段详情】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取,按如下参数查
询即可:

object_api_name= "offboarding_info"

custom_api_name= "block_reason"

**字段权限要求（满足任一）**：
<md-perm name="corehr:offboarding.block_list:read" desc="获取离职屏蔽名单" support_app_types="custom" tags="">获取离职屏蔽名单</md-perm>
<md-perm name="corehr:offboarding.block_list:write" desc="读写离职屏蔽名单" support_app_types="custom" tags="">读写离职屏蔽名单</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >enum_name</md-text>
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
	<md-text type="field-name" >display</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举多语展示
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语言
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
	内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >block_reason_explanation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	屏蔽原因说明

**字段权限要求（满足任一）**：
<md-perm name="corehr:offboarding.block_list:read" desc="获取离职屏蔽名单" support_app_types="custom" tags="">获取离职屏蔽名单</md-perm>
<md-perm name="corehr:offboarding.block_list:write" desc="读写离职屏蔽名单" support_app_types="custom" tags="">读写离职屏蔽名单</md-perm>
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
<md-perm name="corehr:offboarding.custom_field:read" desc="获取离职信息自定义字段信息" support_app_types="custom,isv" tags="">获取离职信息自定义字段信息</md-perm>
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
	自定义字段的唯一标识
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
	自定义字段类型。可选值有：

-1：文本类型，包括超链接字段

-2：布尔类型

-3：数字类型

-4：枚举类型

-5：Lookup类型，如离职人员、竞业公司等

-8：时间类型

-9：附件类型

注意：不支持的字段类型未给出说明。
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


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >retain_account</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	离职是否保留飞书账号

**字段权限要求（满足任一）**：
<md-perm name="corehr:offboarding.retain_account:read" desc="获取离职后是否保留账号字段" support_app_types="custom" tags="">获取离职后是否保留账号字段</md-perm>
<md-perm name="corehr:offboarding.retain_account:write" desc="读写离职后是否保留账号字段" support_app_types="custom" tags="">读写离职后是否保留账号字段</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >social_insurance_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	社保停保年月，按YYYY-MM的日期格式返回

**字段权限要求**：
<md-perm name="corehr:offboarding.social_insurance:read" desc="获取离职申请的社保信息" support_app_types="custom" tags="">获取离职申请的社保信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >provident_fund_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	公积金截止年月，按YYYY-MM的日期格式返回

**字段权限要求**：
<md-perm name="corehr:offboarding.social_insurance:read" desc="获取离职申请的社保信息" support_app_types="custom" tags="">获取离职申请的社保信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >enforce_noncompete_agreement</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否启动竞业

**字段权限要求**：
<md-perm name="corehr:offboarding.noncompete_agreement:read" desc="获取离职申请的竞业信息" support_app_types="custom" tags="">获取离职申请的竞业信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >noncompete_agreement_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	竞业合同ID，可以通过[查询单个合同](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/contract/get)获取详细的合同信息

**字段权限要求**：
<md-perm name="corehr:offboarding.noncompete_agreement:read" desc="获取离职申请的竞业信息" support_app_types="custom" tags="">获取离职申请的竞业信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >noncompete_agreement_company</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	竞业公司ID，可以通过[查询单个公司](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/get)获取详细的公司信息

**字段权限要求**：
<md-perm name="corehr:offboarding.noncompete_agreement:read" desc="获取离职申请的竞业信息" support_app_types="custom" tags="">获取离职申请的竞业信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >noncompete_agreement_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	竞业开始日期

**字段权限要求**：
<md-perm name="corehr:offboarding.noncompete_agreement:read" desc="获取离职申请的竞业信息" support_app_types="custom" tags="">获取离职申请的竞业信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >noncompete_agreement_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	竞业结束日期

**字段权限要求**：
<md-perm name="corehr:offboarding.noncompete_agreement:read" desc="获取离职申请的竞业信息" support_app_types="custom" tags="">获取离职申请的竞业信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >sign_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >enum</md-text>
	</md-dt-td>
	<md-dt-td>
	签署方式，枚举值可查询
[【获取字段详情】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)接口获取,按如下参数查
询即可:

object_api_name= "offboarding_info"

custom_api_name= "sign_type"

**字段权限要求**：
<md-perm name="corehr:offboarding.signature:read" desc="获取离职申请的电子签相关字段" support_app_types="custom" tags="">获取离职申请的电子签相关字段</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >enum_name</md-text>
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
	<md-text type="field-name" >display</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	枚举多语展示
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语言
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
	内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >signature_file</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	签署文件ID列表

**字段权限要求**：
<md-perm name="corehr:offboarding.signature:read" desc="获取离职申请的电子签相关字段" support_app_types="custom" tags="">获取离职申请的电子签相关字段</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >last_attendance_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最后出勤日

**字段权限要求**：
<md-perm name="corehr:offboarding.last_attendance_date:read" desc="获取离职申请的最后出勤日" support_app_types="custom" tags="">获取离职申请的最后出勤日</md-perm>
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
	是否带编转移
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >offboarding_checklist</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >offboarding_checklist</md-text>
	</md-dt-td>
	<md-dt-td>
	离职办理流程信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >checklist_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职流转状态，可选值有：
- AntiBegin：未发起
- Approving：进行中
- Finished：已完成
- Rejected：已拒绝
- Withdrawn：已撤销
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >checklist_start_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职流转开始时间
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >checklist_finish_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职流转结束时间
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >checklist_process_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职流转流程实例 ID。可用于[查询流程相关信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/list)，例如：作为[获取单个流程详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/list)的process_id查询流程详情。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >offboarding_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职唯一标识
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
  "data": {
    "has_more": false,
    "items": [
      {
        "application_info": {
          "apply_finish_time": "2022-02-03 11:22:33",
          "apply_initiating_time": "2022-02-03 11:22:33",
          "apply_initiator_id": "6838119494196871234",
          "process_id": "6838119494196871234"
        },
        "initiating_type": "offboarding_directly",
        "offboarding_checklist": {
          "checklist_finish_time": "2022-02-03 11:22:33",
          "checklist_process_id": "6838119494196871234",
          "checklist_start_time": "2022-02-03 11:22:33",
          "checklist_status": "AntiBegin"
        },
        "offboarding_id": "7298499290417251879",
        "offboarding_info": {
          "add_block_list": "false",
          "block_reason": {
            "display": [
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              },
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              }
            ],
            "enum_name": "phone_type"
          },
          "block_reason_explanation": "xx 年 xx 月 xx 日因 xx 原因红线",
          "custom_fields": [
            {
              "custom_api_name": "name",
              "name": {
                "en_us": "Custom Name",
                "zh_cn": "自定义姓名"
              },
              "type": 1,
              "value": "\"231\""
            },
            {
              "custom_api_name": "name",
              "name": {
                "en_us": "Custom Name",
                "zh_cn": "自定义姓名"
              },
              "type": 1,
              "value": "\"231\""
            }
          ],
          "employee_reason": {
            "display": [
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              },
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              }
            ],
            "enum_name": "phone_type"
          },
          "employee_reason_explanation": "升学",
          "employment_id": "6893014062142064135",
          "enforce_noncompete_agreement": false,
          "expected_offboarding_date": "2022-02-08",
          "hrbp_id": [
            "6893014062142064135",
            "6893014062142064135"
          ],
          "is_transfer_with_workforce": false,
          "last_attendance_date": "2022-02-08",
          "noncompete_agreement_company": "123",
          "noncompete_agreement_end_date": "2022-02-08",
          "noncompete_agreement_id": "123",
          "noncompete_agreement_start_date": "2022-02-08",
          "offboarding_date": "2022-02-08",
          "provident_fund_end_date": "2022-02",
          "reason": {
            "display": [
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              },
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              }
            ],
            "enum_name": "phone_type"
          },
          "reason_explanation": "升学",
          "retain_account": false,
          "sign_type": {
            "display": [
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              },
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              }
            ],
            "enum_name": "phone_type"
          },
          "signature_file": "[\"123\",\"456\"]",
          "social_insurance_end_date": "2022-02"
        },
        "status": "Approving"
      },
      {
        "application_info": {
          "apply_finish_time": "2022-02-03 11:22:33",
          "apply_initiating_time": "2022-02-03 11:22:33",
          "apply_initiator_id": "6838119494196871234",
          "process_id": "6838119494196871234"
        },
        "initiating_type": "offboarding_directly",
        "offboarding_checklist": {
          "checklist_finish_time": "2022-02-03 11:22:33",
          "checklist_process_id": "6838119494196871234",
          "checklist_start_time": "2022-02-03 11:22:33",
          "checklist_status": "AntiBegin"
        },
        "offboarding_id": "7298499290417251879",
        "offboarding_info": {
          "add_block_list": "false",
          "block_reason": {
            "display": [
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              },
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              }
            ],
            "enum_name": "phone_type"
          },
          "block_reason_explanation": "xx 年 xx 月 xx 日因 xx 原因红线",
          "custom_fields": [
            {
              "custom_api_name": "name",
              "name": {
                "en_us": "Custom Name",
                "zh_cn": "自定义姓名"
              },
              "type": 1,
              "value": "\"231\""
            },
            {
              "custom_api_name": "name",
              "name": {
                "en_us": "Custom Name",
                "zh_cn": "自定义姓名"
              },
              "type": 1,
              "value": "\"231\""
            }
          ],
          "employee_reason": {
            "display": [
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              },
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              }
            ],
            "enum_name": "phone_type"
          },
          "employee_reason_explanation": "升学",
          "employment_id": "6893014062142064135",
          "enforce_noncompete_agreement": false,
          "expected_offboarding_date": "2022-02-08",
          "hrbp_id": [
            "6893014062142064135",
            "6893014062142064135"
          ],
          "is_transfer_with_workforce": false,
          "last_attendance_date": "2022-02-08",
          "noncompete_agreement_company": "123",
          "noncompete_agreement_end_date": "2022-02-08",
          "noncompete_agreement_id": "123",
          "noncompete_agreement_start_date": "2022-02-08",
          "offboarding_date": "2022-02-08",
          "provident_fund_end_date": "2022-02",
          "reason": {
            "display": [
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              },
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              }
            ],
            "enum_name": "phone_type"
          },
          "reason_explanation": "升学",
          "retain_account": false,
          "sign_type": {
            "display": [
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              },
              {
                "lang": "zh-CN",
                "value": "刘梓新"
              }
            ],
            "enum_name": "phone_type"
          },
          "signature_file": "[\"123\",\"456\"]",
          "social_insurance_end_date": "2022-02"
        },
        "status": "Approving"
      }
    ],
    "page_token": ""
  },
  "msg": "success"
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
  <md-td>1160102</md-td>
  <md-td>Param is invalid</md-td>
  <md-td>请检查分页大小、分页标记和离职审批发起时间的时间戳格式后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160103</md-td>
  <md-td>No permission on param</md-td>
  <md-td>无权限使用离职原因或离职原因（员工）进行筛选，请确认应用申请按照离职原因搜索(corehr:employment.offboarding_reason.search:read)后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160104</md-td>
  <md-td>Missing query parametert</md-td>
  <md-td>请确保离职审批发起时间、期望离职日期和离职日期的结束开始时间都传入后请求</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160999</md-td>
  <md-td>general internal server error code</md-td>
  <md-td>系统出现问题，如需帮助，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




