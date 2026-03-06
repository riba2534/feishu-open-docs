---
title: "获取绩效结果"
fullPath: "/uAjLw4CM/ukTMukTMukTM/performance-v1/review_data/query"
updateTime: "1741090280000"
---

# 获取绩效结果

获取被评估人在指定周期、指定项目中各个环节的评估结果信息，包含绩效所在的周期、项目、评估项、评估模版以及各环节评估数据等信息。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=performance&version=v1&resource=review_data&method=query)

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
若采用 `tenant_access_token` 的鉴权模式，推荐使用[获取绩效详情数据](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/review_data/query)
接口获取更丰富的返回数据。
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
      <md-td>https://open.feishu.cn/open-apis/performance/v1/review_datas/query</md-td>
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
或
<md-tag mode="inline" type="token-user">user_access_token</md-tag>

**值格式**："Bearer `access_token`"

**示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560"

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
<md-enum-item key="people_admin_id" >以 people_admin_id 来识别用户</md-enum-item>
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
	<md-text type="field-name" >start_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	周期开始时间最小值，毫秒时间戳，小于该时间开始的周期会被过滤掉
<br>

**注意**：当填写了 `semester_id_list` 参数时，此参数无效

**示例值**："1430425599999"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >end_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	周期结束时间最大值，毫秒时间戳，大于该时间结束的周期会被过滤掉
<br>

**注意**：当填写了 `semester_id_list` 参数时，此参数无效

**示例值**："1630425599999"
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
	是
	</md-dt-td>
	<md-dt-td>
	环节类型，目前仅支持终评环节、结果沟通环节、查看绩效结果环节（不传默认包含所有的环节）

**示例值**：["leader_review"]

**可选值有**：
<md-enum>
<md-enum-item key="leader_review" >终评环节</md-enum-item>
<md-enum-item key="communication_and_open_result" >结果沟通环节</md-enum-item>
<md-enum-item key="view_result" >查看绩效结果环节</md-enum-item>
</md-enum>

**数据校验规则**：

- 最大长度：`50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >stage_progress</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	环节状态，填写时按照指定状态获取绩效结果，不填查询所有状态的绩效结果

**示例值**：[1]

**可选值有**：
<md-enum>
<md-enum-item key="0" >未开始，任务的开始时间未到达</md-enum-item>
<md-enum-item key="1" >待完成，任务的开始时间到达而截止时间未到达，且任务未完成</md-enum-item>
<md-enum-item key="2" >已截止，任务的截止时间已到达，且任务未完成</md-enum-item>
<md-enum-item key="3" >已完成，任务已完成</md-enum-item>
<md-enum-item key="4" >已复议</md-enum-item>
</md-enum>

**数据校验规则**：

- 最大长度：`50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >semester_id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	评估周期 ID 列表，可通过[获取周期](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list)接口获取

**示例值**：["6992035450862224940"]

**数据校验规则**：

- 最大长度：`50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >reviewee_user_id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	被评估人 ID 列表，与入参 `user_id_type` 类型一致

**示例值**：["ou_838b193464e10df19f1e1b3853698cca"]

**数据校验规则**：

- 最大长度：`50`
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
	环节更新时间最早时间，毫秒时间戳，可筛选出在此时间之后，有内容提交的环节数据

**示例值**："1630425599999"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
	"reviewee_user_id_list":["ou_3245842393d09e9428ad4655da6e30b3"],
	"start_time":"1430425599999",
	"end_time":"1630425599999",
	"stage_types":["leader_review","communication_and_open_result"],
	"semester_id_list":["6992035450862224940"],
	"stage_progress":[0,1,2,3],
	"updated_later_than":"1430425599999"
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
	<md-text type="field-type" >review_data</md-text>
	</md-dt-td>
	<md-dt-td>
	\-
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >semesters</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >semester\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	周期列表
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
	周期 ID，详情可查看：[获取周期列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list)
<!--

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >year</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	周期年份
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >type_group</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	周期类型分组
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	周期类型-->
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	周期名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh-CN</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	周期中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en-US</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	周期英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >progress</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效评估周期 状态

**可选值有**：
<md-enum>
<md-enum-item key="initiating" >初始化</md-enum-item>
<md-enum-item key="enabled" >已启动</md-enum-item>
</md-enum>
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
	周期开始时间，毫秒时间戳
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
	周期结束时间，毫秒时间戳
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	周期创建时间，毫秒时间戳
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >modify_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效评估周期 更新时间
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >create_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效评估周期 创建人 ID，与入参 user_id_type 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >modify_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效评估周期 更新人 ID，与入参 user_id_type 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >activities</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >activity\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效评估项目列表
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
	项目 ID，可通过[获取项目列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/activity/query)接口获取

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	项目名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh-CN</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	项目中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en-US</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	项目英文名称
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
	周期 ID，详情可查看：[获取周期列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >indicators</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >indicator\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项列表
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
	评估项 ID，详情可查看：[获取评估项列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/indicator/query)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh-CN</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en-US</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >options</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >indicator_option\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项等级列表
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
	等级 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	等级名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >zh-CN</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	等级中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >en-US</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	等级英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >label</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	等级代号
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >templates</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >template\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估模板列表
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
	评估模板 ID，详情可查看：[获取评估模板](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/review_template/query)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	环节名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh-CN</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	环节中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en-US</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	环节英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >stage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	环节类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >units</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >unit\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估内容列表
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
	评估内容 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	评估内容名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh-CN</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估内容中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en-US</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估内容英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >field\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	评估字段列表
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
	评估字段 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	评估字段名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh-CN</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估字段中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en-US</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估字段英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >indicator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项 ID，详情可查看：[获取评估项列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/indicator/query)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >parent_field_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	父级评估字段 ID
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
	被评估人 ID，ID 类型请参考：[用户资源介绍](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/field-overview)
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
	用户的 user_id，与入参 `user_id_type` 类型一致
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
	周期 ID，详情可查看：[获取周期列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list)

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
	项目 ID，详情可查看：[获取项目列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/activity/query)

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
	环节信息
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
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >progress</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	环节状态

**可选值有**：
<md-enum>
<md-enum-item key="0" >未开始，任务的开始时间未到达</md-enum-item>
<md-enum-item key="1" >待完成，任务的开始时间到达而截止时间未到达，且任务未完成</md-enum-item>
<md-enum-item key="2" >已截止，任务的截止时间已到达，且任务未完成</md-enum-item>
<md-enum-item key="3" >已完成，任务已完成</md-enum-item>
<md-enum-item key="4" >已复议，绩效结果已开通，且被评估人已发起复议</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >review_detail\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	环节填写内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >template_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估模板 ID，详情可查看：[获取评估模板](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/review_template/query)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
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


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >field_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估字段 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >reviewer_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user</md-text>
	</md-dt-td>
	<md-dt-td>
	评估人 ID，ID 类型请参考：[用户资源介绍](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/field-overview)

	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
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


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的 user_id，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >submit_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最后提交时间，毫秒时间戳
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >indicator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项 ID，详情可查看：[获取评估项列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/indicator/query)
 <br>

**说明**：当 option_id 或 score 有值的时候有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >option_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评估项结果等级 ID
 <br>

**说明**：当前评估项是评级型评估项数据时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >score</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	评分型评估项填写内容
 <br>

**说明**：当前评估项是评分型评估项数据时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	填写项填写内容 
<br>

**说明**：当前评估项是填写项数据时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >perf_coefficient_result</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	绩效系数值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
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


  </md-dt-tbody>
</md-dt-table>
:::



### 响应体示例
:::html
<md-code-json>
{
  "code": 0,
  "data": {
    "activities": [
      {
        "id": "6992035450862323244",
        "name": {
          "en-US": "",
          "zh-CN": "rino"
        },
        "semester_id": "6992035450862224940"
      }
    ],
    "datas": [
      {
        "activity_id": "6992035450862323244",
        "semester_id": "6992035450862224940",
        "stages": [
          {
            "data": [
              {
                "field_id": "6982759009698137641",
                "reviewer_user_id": {
                  "open_id": "ou_f0ff33850fc47236e34360d5eed99405",
                  "user_id": "6924863940618878996"
                },
                "submit_time": "1627977114000",
                "template_id": "6982759008972326447",
                "text": "干得不错",
                "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"干得不错\"}]}",
                "unit_id": "6982759008973882926"
              }
            ],
            "progress": 3,
            "stage_type": "communication_and_open_result"
          },
          {
            "data": [
              {
                "field_id": "6982759006887888417",
                "indicator_id": "6966127279593784876",
                "option_id": "6966127279593653804",
                "reviewer_user_id": {
                  "open_id": "ou_f0ff33850fc47236e34360d5eed99405",
                  "user_id": "6924863940618878996"
                },
                "submit_time": "1627977100000",
                "template_id": "6982759008789366313",
                "unit_id": "6982759009396508196"
              },
              {
                "field_id": "6982759010081818159",
                "reviewer_user_id": {
                  "open_id": "ou_f0ff33850fc47236e34360d5eed99405",
                  "user_id": "6924863940618878996"
                },
                "submit_time": "1627977100000",
                "template_id": "6982759008789366313",
                "text": "nice",
                "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"nice\"}]}",
                "unit_id": "6982759009396508196"
              },
              {
                "field_id": "6982759007539463717",
                "reviewer_user_id": {
                  "open_id": "ou_f0ff33850fc47236e34360d5eed99405",
                  "user_id": "6924863940618878996"
                },
                "submit_time": "1627977100000",
                "template_id": "6982759008789366313",
                "text": "bad",
                "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"bad\"}]}",
                "unit_id": "6982759009396508196"
              },
              {
                "field_id": "6982759008811615782",
                "indicator_id": "6966168074268280364",
                "option_id": "6966127279593686572",
                "reviewer_user_id": {
                  "open_id": "ou_f0ff33850fc47236e34360d5eed99405",
                  "user_id": "6924863940618878996"
                },
                "submit_time": "1627977100000",
                "template_id": "6982759008789366313",
                "unit_id": "6982759008043877922"
              },
              {
                "field_id": "6982759010112800295",
                "reviewer_user_id": {
                  "open_id": "ou_f0ff33850fc47236e34360d5eed99405",
                  "user_id": "6924863940618878996"
                },
                "submit_time": "1627977100000",
                "template_id": "6982759008789366313",
                "text": "字节范不错",
                "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"字节范不错\"}]}",
                "unit_id": "6982759008043877922"
              },
              {
                "field_id": "6982759009719158315",
                "indicator_id": "6966164187820820012",
                "option_id": "6966127279593621036",
                "reviewer_user_id": {
                  "open_id": "ou_f0ff33850fc47236e34360d5eed99405",
                  "user_id": "6924863940618878996"
                },
                "submit_time": "1627977100000",
                "template_id": "6982759008789366313",
                "unit_id": "6982759010462647852"
              },
              {
                "field_id": "6982759006797776417",
                "reviewer_user_id": {
                  "open_id": "ou_f0ff33850fc47236e34360d5eed99405",
                  "user_id": "6924863940618878996"
                },
                "submit_time": "1627977100000",
                "template_id": "6982759008789366313",
                "text": "与公司共同发展",
                "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"与公司共同发展\"}]}",
                "unit_id": "6982759010462647852"
              },
              {
                "field_id": "7374030018090418179",
                "indicator_id": "",
                "option_id": "",
                "perf_coefficient_result": "4.00",
                "reviewer_user_id": {
                  "open_id": "ou_4cced6778e381ff987855095d546be82",
                  "user_id": "7312059639540072452"
                },
                "score": "",
                "submit_time": "1716900660000",
                "template_id": "7374030018090106883",
                "text": "",
                "richtext": "{\"ops\":[{\"name\":\"insert\",\"text\":\"\"}]}",
                "unit_id": "7374030018090336259"
              }
            ],
            "progress": 3,
            "stage_type": "leader_review"
          }
        ],
        "user_id": {
          "open_id": "ou_3245842393d09e9428ad4655da6e30b3",
          "user_id": "6932009399175086099"
        }
      }
    ],
    "fields": [
      {
        "id": "6982759008811615782",
        "name": {
          "en-US": "",
          "zh-CN": "价值观"
        }
      },
      {
        "id": "6982759010112800295",
        "name": {
          "en-US": "",
          "zh-CN": "价值观评语"
        }
      },
      {
        "id": "6982759008504284709",
        "name": {
          "en-US": "",
          "zh-CN": ""
        }
      },
      {
        "id": "6982759009698137641",
        "name": {
          "en-US": "",
          "zh-CN": "最终反馈"
        }
      },
      {
        "id": "6982759006887888417",
        "name": {
          "en-US": "",
          "zh-CN": "业绩"
        }
      },
      {
        "id": "6982759010081818159",
        "name": {
          "en-US": "",
          "zh-CN": "做得好的"
        }
      },
      {
        "id": "6982759007539463717",
        "name": {
          "en-US": "",
          "zh-CN": "待改进的"
        }
      },
      {
        "id": "6982759009072072239",
        "name": {
          "en-US": "",
          "zh-CN": "留言"
        }
      },
      {
        "id": "6982759009719158315",
        "name": {
          "en-US": "",
          "zh-CN": "投入度"
        }
      },
      {
        "id": "6982759006797776417",
        "name": {
          "en-US": "",
          "zh-CN": "投入度评语"
        }
      }
    ],
    "indicators": [
      {
        "id": "6966127279593784876",
        "name": {
          "en-US": "",
          "zh-CN": "业绩"
        },
        "options": [
          {
            "id": "6966127279593588268",
            "label": "D",
            "name": {
              "en-US": "",
              "zh-CN": "不符预期"
            }
          },
          {
            "id": "6966127279593621036",
            "label": "C",
            "name": {
              "en-US": "",
              "zh-CN": "略低预期"
            }
          },
          {
            "id": "6966127279593653804",
            "label": "B",
            "name": {
              "en-US": "",
              "zh-CN": "符合预期"
            }
          },
          {
            "id": "6966127279593686572",
            "label": "A",
            "name": {
              "en-US": "",
              "zh-CN": "略超预期"
            }
          },
          {
            "id": "6966127279593719340",
            "label": "S",
            "name": {
              "en-US": "",
              "zh-CN": "远超预期"
            }
          }
        ]
      },
      {
        "id": "6966164187820820012",
        "name": {
          "en-US": "",
          "zh-CN": "投入度"
        },
        "options": [
          {
            "id": "6966127279593588268",
            "label": "D",
            "name": {
              "en-US": "",
              "zh-CN": "不符预期"
            }
          },
          {
            "id": "6966127279593621036",
            "label": "C",
            "name": {
              "en-US": "",
              "zh-CN": "略低预期"
            }
          },
          {
            "id": "6966127279593653804",
            "label": "B",
            "name": {
              "en-US": "",
              "zh-CN": "符合预期"
            }
          },
          {
            "id": "6966127279593686572",
            "label": "A",
            "name": {
              "en-US": "",
              "zh-CN": "略超预期"
            }
          },
          {
            "id": "6966127279593719340",
            "label": "S",
            "name": {
              "en-US": "",
              "zh-CN": "远超预期"
            }
          }
        ]
      },
      {
        "id": "6966168074268280364",
        "name": {
          "en-US": "",
          "zh-CN": "价值观"
        },
        "options": [
          {
            "id": "6966127279593588268",
            "label": "D",
            "name": {
              "en-US": "",
              "zh-CN": "不符预期"
            }
          },
          {
            "id": "6966127279593621036",
            "label": "C",
            "name": {
              "en-US": "",
              "zh-CN": "略低预期"
            }
          },
          {
            "id": "6966127279593653804",
            "label": "B",
            "name": {
              "en-US": "",
              "zh-CN": "符合预期"
            }
          },
          {
            "id": "6966127279593686572",
            "label": "A",
            "name": {
              "en-US": "",
              "zh-CN": "略超预期"
            }
          },
          {
            "id": "6966127279593719340",
            "label": "S",
            "name": {
              "en-US": "",
              "zh-CN": "远超预期"
            }
          }
        ]
      }
    ],
    "semesters": [
      {
        "end_time": "1640966399999",
        "id": "6992035450862224940",
        "name": {
          "en-US": "",
          "zh-CN": "sr"
        },
        "start_time": "1625068800000"
      }
    ],
    "templates": [
      {
        "id": "6982759007063000610",
        "name": {
          "en-US": "Release and Communicate Performance Review with Direct Reports",
          "zh-CN": "进行直属下级绩效沟通并开通结果"
        },
        "stage": "communication_and_open_result"
      },
      {
        "id": "6982759008113116716",
        "name": {
          "en-US": "Manager Review",
          "zh-CN": "上级评估"
        },
        "stage": "leader_review"
      },
      {
        "id": "6982759008537495079",
        "name": {
          "en-US": "Release and Communicate Performance Review with Direct Reports",
          "zh-CN": "进行直属下级绩效沟通并开通结果"
        },
        "stage": "communication_and_open_result"
      },
      {
        "id": "6982759008789366313",
        "name": {
          "en-US": "Manager Review",
          "zh-CN": "上级评估"
        },
        "stage": "leader_review"
      },
      {
        "id": "6982759008959153708",
        "name": {
          "en-US": "Release and Communicate Performance Review with Direct Reports",
          "zh-CN": "进行直属下级绩效沟通并开通结果"
        },
        "stage": "communication_and_open_result"
      },
      {
        "id": "6982759008972326447",
        "name": {
          "en-US": "Release and Communicate Performance Review with Direct Reports",
          "zh-CN": "进行直属下级绩效沟通并开通结果"
        },
        "stage": "communication_and_open_result"
      },
      {
        "id": "6982759010376304165",
        "name": {
          "en-US": "Manager Review",
          "zh-CN": "上级评估"
        },
        "stage": "leader_review"
      },
      {
        "id": "6982759010524038691",
        "name": {
          "en-US": "Manager Review",
          "zh-CN": "上级评估"
        },
        "stage": "leader_review"
      },
      {
        "id": "6982759010669463083",
        "name": {
          "en-US": "Release and Communicate Performance Review with Direct Reports",
          "zh-CN": "进行直属下级绩效沟通并开通结果"
        },
        "stage": "communication_and_open_result"
      }
    ],
    "units": [
      {
        "id": "6982759008043877922",
        "name": {
          "en-US": "",
          "zh-CN": "价值观"
        }
      },
      {
        "id": "6982759008607602222",
        "name": {
          "en-US": "",
          "zh-CN": "重点工作"
        }
      },
      {
        "id": "6982759008973882926",
        "name": {
          "en-US": "",
          "zh-CN": "最终反馈"
        }
      },
      {
        "id": "6982759009396508196",
        "name": {
          "en-US": "",
          "zh-CN": "业绩"
        }
      },
      {
        "id": "6982759010063910445",
        "name": {
          "en-US": "",
          "zh-CN": "留言"
        }
      },
      {
        "id": "6982759010462647852",
        "name": {
          "en-US": "",
          "zh-CN": "投入度"
        }
      }
    ]
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
  <md-td>500</md-td>
  <md-td>1580101</md-td>
  <md-td>internal error</md-td>
  <md-td>请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580102</md-td>
  <md-td>param is invalid</md-td>
  <md-td>检查参数是否正确，例如类型，大小</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580901</md-td>
  <md-td>tenant no license</md-td>
  <md-td>请检查租户是否有席位</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




