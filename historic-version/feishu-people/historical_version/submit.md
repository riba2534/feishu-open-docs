---
title: "操作员工离职"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/submit"
updateTime: "1729821899000"
---

# 操作员工离职

该接口用于发起员工离职。若发起成功，会生成一条员工的离职数据，同时产生相应的事件。参考[离职申请状态变更](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/offboarding/events/status_updated){尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v1&resource=offboarding&method=submit)

:::html
<md-alert type="error">

</md-alert>
:::

:::html
<md-alert type="warn">
该接口暂不支持员工数据鉴权，拥有接口权限即可操作对应租户所有员工的离职，使用时请注意数据安全。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v1/offboardings/submit</md-td>
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

**示例值**：people_corehr_id

**可选值有**：
<md-enum>
<md-enum-item key="open_id" >标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)</md-enum-item>
<md-enum-item key="union_id" >标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)</md-enum-item>
<md-enum-item key="user_id" >标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)</md-enum-item>
<md-enum-item key="people_corehr_id" >以飞书人事的 ID 来识别用户</md-enum-item>
</md-enum>

**默认值**：`people_corehr_id`

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
	<md-text type="field-name" >offboarding_mode</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	离职方式，目前只支持直接离职

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="1" >直接离职</md-enum-item>
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
	离职员工 ID。ID类型与查询参数 user_id_type取值一致：

1、当user_id_type取值为open_id时，ID获取方式参考[如何获取自己的Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)。

2、当user_id_type取值为user_id时，ID获取方式参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)。

3、当user_id_type取值为union_id时，ID获取方式参考[如何获取自己的 Union ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)。

4、当user_id_type取值为people_corehr_id时，先参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。v1/common_data-id/convert)获取

**示例值**："6982509313466189342"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offboarding_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	离职日期，入参格式应为YYYY-MM-DD

**示例值**："2022-05-18"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offboarding_reason_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	离职原因，可通过接口
[【查询员工离职原因列表】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/query)获取

**示例值**："reason_for_offboarding_option8"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offboarding_reason_explanation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职原因说明，长度限制6000个字符，该字段允许为空

**示例值**："离职原因说明"
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
	操作发起人 ID。ID类型与查询参数 user_id_type取值一致：

1、当user_id_type取值为open_id时，ID获取方式参考[如何获取自己的Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)。

2、当user_id_type取值为user_id时，ID获取方式参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)。

3、当user_id_type取值为union_id时，ID获取方式参考[如何获取自己的 Union ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)。

4、当user_id_type取值为people_corehr_id时，先参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。

注意：

1.只有操作发起人可以撤销流程

2.为空时，默认系统发起人

**示例值**："6982509313466189341"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >add_block_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否加入离职屏蔽名单

注意：

1.取值为true时，屏蔽原因（block_reason）为必填。

2.取值为false时，不允许填写屏蔽原因（block_reason）和屏蔽原因说明（block_reason_explanation）。

3.取值为空时，不允许填写屏蔽原因（block_reason）和屏蔽原因说明（block_reason_explanation）。

4.操作离职时如果选择加入屏蔽名单，只有当员工离职生效后才会进入到屏蔽名单。

**示例值**：false
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >block_reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	屏蔽原因

注意：

1.该字段取值于 [人员档案配置](https://people.feishu.cn/people/hr-settings/profile) > 信息配置 > 离职信息 的屏蔽原因字段选项集。

2.枚举字段值也可通过[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)获取，参考接口返回的 字段详情 > 字段类型配置信息 > 选项配置信息 > 选项信息 > 枚举常量集 API name

3.该字段是否必填取决于是否加入离职屏蔽名单(add_block_list)

**示例值**："红线"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >block_reason_explanation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	屏蔽原因说明，该字段允许为空

**示例值**："xx 年 xx 月 xx 日因 xx 原因红线"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职自定义字段。

注意：可填写的字段范围参考[人员档案配置](https://people.feishu.cn/people/hr-settings/profile) > 信息配置 > 离职信息 中的自定义字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段唯一标识

注意：

1.该字段取值于[人员档案配置](https://people.feishu.cn/people/hr-settings/profile) > 信息配置 > 离职信息 中各字段的字段编码

2.该字段也可以通过[获取自定义字段列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query)获取

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
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
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(如123, 123.23, "true", [\"id1\",\"id2\"], "2006-01-02 15:04:05")。

注意：

1.枚举字段的枚举值取值于[人员档案配置](https://people.feishu.cn/people/hr-settings/profile) > 信息配置 > 离职信息 对应字段选项集的选项编码。

2.枚举字段值也可通过[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)获取，参考接口返回的 字段详情 > 字段类型配置信息 > 选项配置信息 > 选项信息 > 枚举常量集 API name

3.人员字段目前只支持传入员工的雇佣ID。先参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。

4.暂不支持填写附件类型字段。

**示例值**："\"Sandy\""
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "offboarding_mode": 1,
    "employment_id": "6982509313466189342",
    "offboarding_date": "2022-05-18",
    "offboarding_reason_unique_identifier": "reason_for_offboarding_option8",
    "offboarding_reason_explanation": "离职原因说明",
    "initiator_id": "6982509313466189341",
    "add_block_list": false,
    "block_reason": "红线",
    "block_reason_explanation": "xx 年 xx 月 xx 日因 xx 原因红线",
    "custom_fields": [
        {
            "field_name": "name",
            "value": "\"Sandy\""
        }
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
	<md-text type="field-name" >offboarding_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职记录 id
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
	雇员 id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >offboarding_reason_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因，可通过接口
[【查询员工离职原因列表】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/query)获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
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


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >offboarding_reason_explanation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因说明
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >add_block_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否加入离职屏蔽名单
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >block_reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	屏蔽原因
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >block_reason_explanation</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	屏蔽原因说明
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
	创建时间
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
        "offboarding_id": "7095671727698478604",
        "employment_id": "6982509313466189342",
        "offboarding_reason_unique_identifier": "reason_for_offboarding_option8",
        "offboarding_date": "2022-05-18",
        "offboarding_reason_explanation": "离职原因说明",
        "add_block_list": false,
        "block_reason": "红线",
        "block_reason_explanation": "xx 年 xx 月 xx 日因 xx 原因红线",
        "created_time": "2022-05-09 17:50:17"
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
  <md-td>1160103</md-td>
  <md-td>general internal server error code</md-td>
  <md-td>系统出现问题，如需帮助，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160201</md-td>
  <md-td>has approving offboarding</md-td>
  <md-td>存在「审批中」或「待生效」的离职申请，请先撤销后再申请</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160203</md-td>
  <md-td>no current contract</md-td>
  <md-td>所选离职日期无生效中的合同，请确认合同信息后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160204</md-td>
  <md-td>has future contract</md-td>
  <md-td>存在晚于离职日期生效的合同，请确认合同信息后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160205</md-td>
  <md-td>contract has actual end date</md-td>
  <md-td>离职日期时的合同已存在实际结束日期，请确认合同信息后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160210</md-td>
  <md-td>has offboarding record</md-td>
  <md-td>存在「审批中」或「待生效」的离职申请，请先撤销后再申请</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160602</md-td>
  <md-td>offboarding is earlier than probation</md-td>
  <md-td>存在晚于离职日期的转正记录，请重新选择离职日期或先撤销试用期转正申请</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160603</md-td>
  <md-td>offboarding is earlier than transform</md-td>
  <md-td>存在晚于离职日期的异动记录，请重新选择离职日期或先撤销异动申请</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160604</md-td>
  <md-td>reason explanation length exceed maximum</md-td>
  <md-td>离职原因说明长度超过最大限制(6000)，请确认长度后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160616</md-td>
  <md-td>no valid job data</md-td>
  <md-td>该员工没有合法的任职记录，请确认任职记录后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1161000</md-td>
  <md-td>unknown error</md-td>
  <md-td>调用上下游系统错误，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160710</md-td>
  <md-td>invalid block list</md-td>
  <md-td>若是否加入屏蔽名单取值为true时，则屏蔽原因为必填，若取值为false时，不允许填写屏蔽原因和屏蔽原因说明。请检查屏蔽名单格式是否正确再重新提交。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160200</md-td>
  <md-td>has approving transform</md-td>
  <md-td>存在审批中的异动流程，请先撤销或完成异动流程的审批</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160601</md-td>
  <md-td>offboarding is earlier than onboarding</md-td>
  <md-td>离职日期不可早于入职日期，请确认员工入职日期后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160617</md-td>
  <md-td>hyperlink field format is illegal</md-td>
  <md-td>超链接字段输入格式不合法，请检查填写的超链接字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160618</md-td>
  <md-td>text field exceeds maximum limit</md-td>
  <md-td>单行文本字段字段长度不允许超过255个字符，多行文本字段长度不允许超过6000个字符，请检查填写的文本字段长度后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160619</md-td>
  <md-td>enum value of the enum field is invalid</md-td>
  <md-td>填写自定义枚举字段的枚举值不存在，请检查枚举值是否在字段的选项编码后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160621</md-td>
  <md-td>offboarding reason is required</md-td>
  <md-td>离职原因必填，请填写离职原因</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160622</md-td>
  <md-td>offboarding date is required</md-td>
  <md-td>离职日期必填，请填写离职日期</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160631</md-td>
  <md-td>employee is not exist or has offboarded</md-td>
  <md-td>填写的员工ID不存在，请检查填写的员工ID在飞书人事有对应的员工，其中雇员ID必须在职。</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




