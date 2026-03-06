---
title: "获取绩效详情数据"
fullPath: "/uAjLw4CM/ukTMukTMukTM/performance-v2/review_data/query"
updateTime: "1758627919000"
---

# 获取绩效详情数据

获取被评估人各环节的绩效评估详情（不包含校准环节），如环节评估数据、环节提交状态等{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=performance&version=v2&resource=review_data&method=query)

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
      <md-td>https://open.feishu.cn/open-apis/performance/v2/review_datas/query</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[20 次/分钟](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="performance:performance" desc="管理绩效数据" support_app_types="custom,isv" tags="">管理绩效数据</md-perm>
            <md-perm name="performance:performance:readonly" desc="查看绩效数据" support_app_types="custom,isv" tags="">查看绩效数据</md-perm>
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
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
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
	<md-text type="field-name" >semester_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	评估周期 ID 列表，semester_id 可通过[【获取周期】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list)获得

**示例值**：["6992035450862224940"]

**数据校验规则**：

- 长度范围：`0` ～ `10`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >reviewee_user_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	被评估人 ID 列表，ID 类型与user_id_type 的取值一致

**示例值**：["ou_3245842393d09e9428ad4655da6e30b3"]

**数据校验规则**：

- 长度范围：`0` ～ `10`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >stage_types</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	环节类型，如果同时传了环节 ID 和环节类型，优先返回环节 ID 对应的绩效数据。
stage_types 和 stage_ids 至少要传一个，不传默认不返回任何环节评估数据。如果返回数据为空，可以检查模板对应环节是否有内容。

**示例值**：["leader_review"]

**可选值有**：
<md-enum>
<md-enum-item key="summarize_key_outputs" >工作总结环节</md-enum-item>
<md-enum-item key="review" >评估型环节</md-enum-item>
<md-enum-item key="communication_and_open_result" >结果沟通环节</md-enum-item>
<md-enum-item key="view_result" >绩效结果查看环节</md-enum-item>
<md-enum-item key="reconsideration" >结果复议环节</md-enum-item>
<md-enum-item key="leader_review" >终评环节（特指最终的绩效结果数据）</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >review_stage_roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	评估型环节的执行人角色，当传入的环节类型中有评估型环节时，该参数才生效，返回指定执行人角色的评估型环节数据，不传默认包含所有的执行人角色。

**示例值**：["reviewee"]

**可选值有**：
<md-enum>
<md-enum-item key="reviewee" >被评估人</md-enum-item>
<md-enum-item key="invited_reviewer" >360°评估人</md-enum-item>
<md-enum-item key="solid_line_leader" >实线上级</md-enum-item>
<md-enum-item key="dotted_line_leader" >虚线上级</md-enum-item>
<md-enum-item key="secondary_solid_line_leader" >第二实线上级</md-enum-item>
<md-enum-item key="direct_project_leader" >合作项目中的直属上级</md-enum-item>
<md-enum-item key="custom_review_role" >自定义评估角色</md-enum-item>
<md-enum-item key="metric_reviewer" >指标评价人</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >stage_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	环节 ID，如果同时传了环节 ID 和环节类型，优先返回环节 ID 对应的绩效数据。
stage_types 和 stage_ids 至少要传一个，不传默认不返回任何环节评估数据。

可在事件[绩效结果开通](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/stage_task/events/open_result)、[绩效详情变更](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/review_data/events/changed)获得，用于接收事件后按环节查询评估数据场景

**示例值**：["7343513161666707459"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >need_leader_review_data_source</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	当要获取的绩效数据的环节类型包含终评环节时，可指定是否需要返回绩效终评数据的具体环节来源。不传则默认不返回。

    可选值有：
- true: 返回绩效终评数据的具体环节来源
- false: 不返回绩效终评数据的具体环节来源

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >updated_later_than</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	可筛选出在此时间之后，有内容提交的环节数据，毫秒级时间戳。不传默认返回所有时间提交的环节数据，包括未提交的环节数据

**示例值**："1630425599999"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >stage_progresses</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	环节状态，不传默认包含所有状态。各类型的环节分别有以下环节状态：
  
  查看绩效结果环节状态

    可选值有：
  - `0`：已开通，绩效结果已开通，未发起复议也无需确认结果
  - `1`：待确认，绩效结果已开通但被评估人还未确认结果，确认的截止时间还未到达
  - `2`：已截止，绩效结果已开通但被评估人还未确认结果，确认的截止时间已到达
  - `3`：已确认，绩效结果已开通，被评估人已确认结果
  - `4`：已复议，绩效结果已开通，且被评估人已发起复议
  
  绩效结果复议环节状态

    可选值有：
  - `1`：待完成，任务未完成
  - `2`：已截止，任务的截止时间已到达，且任务未完成
  - `3`：已完成，任务已完成
  
  除上述类型外的其他环节类型状态

    可选值有：
  - `0`：未开始，任务的开始时间未到达
  - `1`：待完成，任务的开始时间到达而截止时间未到达，且任务未完成
  - `2`：已截止，任务的截止时间已到达，且任务未完成
  - `3`: 已完成，任务已完成

**示例值**：[1]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "semester_ids": [
        "6992035450862224940"
    ],
    "reviewee_user_ids": [
        "ou_3245842393d09e9428ad4655da6e30b3"
    ],
    "stage_types": [
        "leader_review"
    ],
    "review_stage_roles": [
        "reviewee"
    ],
    "stage_ids": [
        "7343513161666707459"
    ],
    "need_leader_review_data_source": true,
    "updated_later_than": "1630425599999",
    "stage_progresses": [
        1
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
	<md-text type="field-name" >datas</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >review_profile\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估数据列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >open_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的 open_id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的 user_id，ID 类型与user_id_type 的取值一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >semester_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效评估周期 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >activity_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效评估项目 ID，详细信息请参考[获取项目配置](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/activity/query)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >review_template_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人在该周期对应的后台评估模板 ID，详细信息请参考[获取评估模板配置](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/review_template/query)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >stages</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >review_stage\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	本周期内各环节内容
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
	环节 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >stage_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	环节类型

**可选值有**：
<md-enum>
<md-enum-item key="summarize_key_outputs" >工作总结环节</md-enum-item>
<md-enum-item key="review" >评估型环节</md-enum-item>
<md-enum-item key="communication_and_open_result" >结果沟通环节</md-enum-item>
<md-enum-item key="view_result" >绩效结果查看环节</md-enum-item>
<md-enum-item key="reconsideration" >结果复议环节</md-enum-item>
<md-enum-item key="leader_review" >终评环节（特指最终的绩效结果数据）</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >template_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	该环节对应的环节模板的 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >records</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >review_record\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估内容记录。多人评估的环节有多份记录，比如 360 评估环节。如果开启了 360 匿名评估，并且是对全部查看者匿名，则评估记录数低于匿名下限，则不返回 360 评估记录
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >progress</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人的环节状态。各类型的环节分别有以下环节状态：
  
  查看绩效结果环节状态

    可选值有：
  - `0`：已开通，绩效结果已开通，未发起复议也无需确认结果
  - `1`：待确认，绩效结果已开通但被评估人还未确认结果，确认的截止时间还未到达
  - `2`：已截止，绩效结果已开通但被评估人还未确认结果，确认的截止时间已到达
  - `3`：已确认，绩效结果已开通，被评估人已确认结果
  - `4`：已复议，绩效结果已开通，且被评估人已发起复议
    
    终评环节/结果沟通环节状态（不传默认包含所有的状态）
  
  绩效结果复议环节状态

    可选值有：
  - `1`：待完成，任务未完成
  - `2`：已截止，任务的截止时间已到达，且任务未完成
  - `3`：已完成，任务已完成
  
  除上述类型外的其他环节类型状态

    可选值有：
  - `0`：未开始，任务的开始时间未到达
  - `1`：待完成，任务的开始时间到达而截止时间未到达，且任务未完成
  - `2`：已截止，任务的截止时间已到达，且任务未完成
  - `3`: 已完成，任务已完成
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >units</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >review_unit\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估记录中的评估内容明细
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >unit_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估内容 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >is_unknown</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否为不了解。当评估人选不了解时，会返回为 true，其他时候不返回。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >review_detail\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估题列表，指评估内容中的每个题，可能是评估项或者填写项
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >field_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估题 ID，指评估内容中的每个评估项或填写项
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >reviewer_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人 ID。如果开启了 360 匿名评估，并且是对全部查看者匿名，则不返回该值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >open_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的 open_id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的 user_id，ID 类型与user_id_type 的取值一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >submit_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	该评估题的最后提交时间，毫秒级时间戳
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >indicator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项 ID（不包含子评估项），option_id 或 score 有值的时候有值，详细信息请参考[获取评估项列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/indicator/query)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >option_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估等级 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评分
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	填写项填写的文本
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >tag_based_question_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	标签填写题 ID，详细信息请参考[获取标签填写题配置](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/question/query)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >tag_text_item_data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >tag_text\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	标签填写项的内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >tag_text_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	标签 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >tag_text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人在该标签下填写的文本
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >tag_richtext</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	富文本格式的填写内容，解析方式见 [editor](https://open.larkoffice.com/document/client-docs/gadget/component-component/basic-component/form/editor#51af2f4f)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >perf_coefficient_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效系数值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >sub_indicator_data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >sub_indicator\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	子评估项内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >field_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	子评估题 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >indicator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	子评估项 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >option_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	子评估项的评估等级 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	子评估项的评分
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	子评估项填写的文本
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >richtext</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	富文本格式的填写内容，解析方式见 [editor](https://open.larkoffice.com/document/client-docs/gadget/component-component/basic-component/form/editor#51af2f4f)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >objective_data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >objective_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估的目标数据，当评估内容是对目标（O）或关键举措（KR）评估时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >objective_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	目标 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	目标的评分
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人在该填写项填写的文本
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >keyresult_data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >keyresult_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估的关键举措，当评估内容是对关键举措（KR）评估时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >keyresult_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	关键举措 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	关键举措的评分
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	该关键举措的填写项内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >richtext</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	富文本格式的填写内容，解析方式见 [editor](https://open.larkoffice.com/document/client-docs/gadget/component-component/basic-component/form/editor#51af2f4f)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >richtext</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	富文本格式的填写内容，解析方式见 [editor](https://open.larkoffice.com/document/client-docs/gadget/component-component/basic-component/form/editor#51af2f4f)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >metric_data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >metric_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估的指标，当评估内容是对指标评估时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	指标 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	指标评分
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >leader_review_data_source</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	终评环节填写内容的来源（仅终评环节的数据有值）

**可选值有**：
<md-enum>
<md-enum-item key="review" >产生终评结果的评估型环节</md-enum-item>
<md-enum-item key="calibaration" >校准环节</md-enum-item>
<md-enum-item key="reconsideration" >结果复议环节</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >multi_texts</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	工作/总结类型的文本内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >richtext</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	富文本格式的填写内容，解析方式见 [editor](https://open.larkoffice.com/document/client-docs/gadget/component-component/basic-component/form/editor#51af2f4f)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >multi_richtexts</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	富文本格式的填写内容，解析方式见 [editor](https://open.larkoffice.com/document/client-docs/gadget/component-component/basic-component/form/editor#51af2f4f)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >is_principal_review_item</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	该评估题是否是首要评估项
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >invited_review_record_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >invited_review_record_info</md-text>
	</md-dt-td>
	<md-dt-td>
	360 ° 评估记录的信息。如果开启了 360 匿名评估，并且是对全部查看者匿名，则不返回评估人的部分信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >reviewer_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人 ID。如果开启了 360 匿名评估，并且是对全部查看者匿名，则不返回该值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >open_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的 open_id
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
	用户的 user_id，ID 类型与user_id_type 的取值一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >is_rejected</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否拒绝
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >rejected_reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	360° 评估人拒绝评估的理由，当 360° 评估环节被评估人拒绝时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >distribute_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	360° 评估人的评估尺度标签

**可选值有**：
<md-enum>
<md-enum-item key="1" >严格</md-enum-item>
<md-enum-item key="2" >适中</md-enum-item>
<md-enum-item key="3" >宽松</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >avg_diff</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	360° 评估人的评估尺度数值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >relationship_with_reviewee</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	360° 评估人的与被评估人关系。如果开启了 360 匿名评估，并且是对全部查看者匿名，且配置隐藏描述信息则不返回该值

**可选值有**：
<md-enum>
<md-enum-item key="direct_report" >直属下级</md-enum-item>
<md-enum-item key="skiplevel_report" >隔级下级</md-enum-item>
<md-enum-item key="former_direct_manager" >原直属上级</md-enum-item>
<md-enum-item key="skiplevel_manager" >隔级上级</md-enum-item>
<md-enum-item key="teammate" >相同上级同事</md-enum-item>
<md-enum-item key="crossteam_colleague" >不同上级同事</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >invitedby</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	360° 评估人的邀请人类型。如果开启了 360 匿名评估，并且是对全部查看者匿名，且配置隐藏描述信息则不返回该值

**可选值有**：
<md-enum>
<md-enum-item key="system_default" >系统默认</md-enum-item>
<md-enum-item key="reviewee" >被评估人本人</md-enum-item>
<md-enum-item key="manager" >上级</md-enum-item>
<md-enum-item key="hrbp_or_others" >HRBP或其他人</md-enum-item>
<md-enum-item key="voluntary" >自愿评估</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >direct_project_leader_record_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >direct_project_leader_record_info</md-text>
	</md-dt-td>
	<md-dt-td>
	合作项目中上级的评估记录信息，仅在「项目直属上级环节」有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >reviewer_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >open_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的 open_id
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
	用户的 user_id，ID 类型与user_id_type 的取值一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >cooperation_projects</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_project\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人作为直属项目上级所在的项目
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
	合作项目 ID
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
	合作项目的名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	合作项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >reviewer_role</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人在合作项目中的角色。在未配置合作项目角色情况下，该字段为空值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	合作项目角色 ID
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
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >reviewee_role</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人在合作项目中的项目角色。在未配置合作项目角色情况下，该字段为空值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	合作项目角色 ID
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
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >user_roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >underling_roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >review_depend_projects</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_project\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估依据的项目
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
	合作项目 ID
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
	合作项目的名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >reviewer_role</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人的项目角色。在未配置项目角色情况下，该字段为空值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
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
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >reviewee_role</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人的项目角色。在未配置项目角色情况下，该字段为空值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
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
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >user_roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >underling_roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >participated_projects</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_project\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	共同参与的项目
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
	合作项目 ID
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
	合作项目的名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >reviewer_role</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人的项目角色。在未配置项目角色情况下，该字段为空值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
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
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >reviewee_role</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人的项目角色。在未配置项目角色情况下，该字段为空值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
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
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >user_roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >underling_roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cooperation_user_role\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人项目角色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	名称
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
	中文
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
	英文
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >record_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估记录 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >review_stage_role</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估型环节的执行人角色

**可选值有**：
<md-enum>
<md-enum-item key="reviewee" >被评估人</md-enum-item>
<md-enum-item key="invited_reviewer" >360°评估人</md-enum-item>
<md-enum-item key="solid_line_leader" >实线上级</md-enum-item>
<md-enum-item key="dotted_line_leader" >虚线上级</md-enum-item>
<md-enum-item key="secondary_solid_line_leader" >第二实线上级</md-enum-item>
<md-enum-item key="direct_project_leader" >项目直属上级</md-enum-item>
<md-enum-item key="custom_review_role" >自定义评估角色</md-enum-item>
<md-enum-item key="metric_reviewer" >指标评价人角色</md-enum-item>
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
        "datas": [
            {
                "user_id": {
                    "open_id": "od-asd2dasdasd",
                    "user_id": "ou-ux987dsf6x"
                },
                "semester_id": "7343513161666707459",
                "activity_id": "7343513161666707459",
                "review_template_id": "7343513161666707459",
                "stages": [
                    {
                        "stage_id": "7343513161666707459",
                        "stage_type": "review",
                        "template_id": "7343513161666707459",
                        "records": [
                            {
                                "progress": 1,
                                "units": [
                                    {
                                        "unit_id": "7343513161666707459",
                                        "data": [
                                            {
                                                "field_id": "7343513161666707459",
                                                "reviewer_user_id": {
                                                    "open_id": "od-asd2dasdasd",
                                                    "user_id": "ou-ux987dsf6x"
                                                },
                                                "submit_time": "7343513161666707459",
                                                "indicator_id": "7343513161666707459",
                                                "option_id": "7343513161666707459",
                                                "score": "1.1",
                                                "text": "qwert",
                                                "tag_based_question_id": "7343513161666707459",
                                                "tag_text_item_data": [
                                                    {
                                                        "tag_text_id": "7343513161666707459",
                                                        "tag_text": "qwertyu",
                                                        "tag_richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"qwerty\"}]}"
                                                    }
                                                ],
                                                "perf_coefficient_value": "1.1",
                                                "sub_indicator_data": [
                                                    {
                                                        "field_id": "7343513161666707459",
                                                        "indicator_id": "7343513161666707459",
                                                        "option_id": "7343513161666707459",
                                                        "score": "1.1",
                                                        "text": "qwertyuiop",
                                                        "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"qwerty\"}]}"
                                                    }
                                                ],
                                                "objective_data": [
                                                    {
                                                        "objective_id": "7343513161666707459",
                                                        "score": "1.1",
                                                        "text": "qwertyu",
                                                        "keyresult_data": [
                                                            {
                                                                "keyresult_id": "7343513161666707459",
                                                                "score": "1.1",
                                                                "text": "qwerty",
                                                                "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"qwerty\"}]}"
                                                            }
                                                        ],
                                                        "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"qwerty\"}]}"
                                                    }
                                                ],
                                                "metric_data": [
                                                    {
                                                        "id": "7343513161666707459",
                                                        "score": "1.1"
                                                    }
                                                ],
                                                "leader_review_data_source": "review",
                                                "multi_texts": [
                                                    "qwerty"
                                                ],
                                                "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"qwerty\"}]}",
                                                "multi_richtexts": [
                                                    "{\"ops\":[{\"name\":\"insert\",\"text\":\"qwerty\"}]}"
                                                ],
                                                "is_principal_review_item": true
                                            }
                                        ]
                                    }
                                ],
                                "invited_review_record_info": {
                                    "reviewer_id": {
                                        "open_id": "od-asd2dasdasd",
                                        "user_id": "ou-ux987dsf6x"
                                    },
                                    "is_rejected": false,
                                    "rejected_reason": "test",
                                    "distribute_type": 1,
                                    "avg_diff": "1.23",
                                    "relationship_with_reviewee": "direct_report",
                                    "invitedby": "system_default"
                                },
                                "direct_project_leader_record_info": {
                                    "reviewer_id": {
                                        "open_id": "od-asd2dasdasd",
                                        "user_id": "ou-ux987dsf6x"
                                    },
                                    "cooperation_projects": [
                                        {
                                            "id": "7309457114076807188",
                                            "name": {
                                                "zh_cn": "体验",
                                                "en_us": "Interactive experience"
                                            },
                                            "roles": [
                                                {
                                                    "reviewer_role": {
                                                        "role_id": "7213434603057807379",
                                                        "name": {
                                                            "zh_cn": "体验",
                                                            "en_us": "Interactive experience"
                                                        }
                                                    },
                                                    "reviewee_role": {
                                                        "role_id": "7213434603057807379",
                                                        "name": {
                                                            "zh_cn": "体验",
                                                            "en_us": "Interactive experience"
                                                        }
                                                    }
                                                }
                                            ],
                                            "user_roles": [
                                                {
                                                    "role_id": "7213434603057807379",
                                                    "name": {
                                                        "zh_cn": "体验",
                                                        "en_us": "Interactive experience"
                                                    }
                                                }
                                            ],
                                            "underling_roles": [
                                                {
                                                    "role_id": "7213434603057807379",
                                                    "name": {
                                                        "zh_cn": "体验",
                                                        "en_us": "Interactive experience"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "review_depend_projects": [
                                        {
                                            "id": "7309457114076807188",
                                            "name": {
                                                "zh_cn": "体验",
                                                "en_us": "Interactive experience"
                                            },
                                            "roles": [
                                                {
                                                    "reviewer_role": {
                                                        "role_id": "7213434603057807379",
                                                        "name": {
                                                            "zh_cn": "体验",
                                                            "en_us": "Interactive experience"
                                                        }
                                                    },
                                                    "reviewee_role": {
                                                        "role_id": "7213434603057807379",
                                                        "name": {
                                                            "zh_cn": "体验",
                                                            "en_us": "Interactive experience"
                                                        }
                                                    }
                                                }
                                            ],
                                            "user_roles": [
                                                {
                                                    "role_id": "7213434603057807379",
                                                    "name": {
                                                        "zh_cn": "体验",
                                                        "en_us": "Interactive experience"
                                                    }
                                                }
                                            ],
                                            "underling_roles": [
                                                {
                                                    "role_id": "7213434603057807379",
                                                    "name": {
                                                        "zh_cn": "体验",
                                                        "en_us": "Interactive experience"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "participated_projects": [
                                        {
                                            "id": "7309457114076807188",
                                            "name": {
                                                "zh_cn": "体验",
                                                "en_us": "Interactive experience"
                                            },
                                            "roles": [
                                                {
                                                    "reviewer_role": {
                                                        "role_id": "7213434603057807379",
                                                        "name": {
                                                            "zh_cn": "体验",
                                                            "en_us": "Interactive experience"
                                                        }
                                                    },
                                                    "reviewee_role": {
                                                        "role_id": "7213434603057807379",
                                                        "name": {
                                                            "zh_cn": "体验",
                                                            "en_us": "Interactive experience"
                                                        }
                                                    }
                                                }
                                            ],
                                            "user_roles": [
                                                {
                                                    "role_id": "7213434603057807379",
                                                    "name": {
                                                        "zh_cn": "体验",
                                                        "en_us": "Interactive experience"
                                                    }
                                                }
                                            ],
                                            "underling_roles": [
                                                {
                                                    "role_id": "7213434603057807379",
                                                    "name": {
                                                        "zh_cn": "体验",
                                                        "en_us": "Interactive experience"
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                },
                                "record_id": "7385000219907457024-7385000219907457025"
                            }
                        ],
                        "review_stage_role": "reviewee"
                    }
                ]
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
  <md-td>400</md-td>
  <md-td>1580102</md-td>
  <md-td>param is invalid</md-td>
  <md-td>检查传入的参数</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1580101</md-td>
  <md-td>internal error</md-td>
  <md-td>内部错误，请稍后重试，仍然出现可以[咨询客服](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952&extra=%7B%22channel%22%3A14%2C%22created_at%22%3A1614493146%2C%22scenario_id%22%3A6885151765134622721%2C%22signature%22%3A%22ca94c408b966dc1de2083e5bbcd418294c146e98%22%7D)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580901</md-td>
  <md-td>tenant no licnese</md-td>
  <md-td>租户无绩效席位，请联系租户管理员开通绩效席位</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




