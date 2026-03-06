---
title: "编辑离职信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/offboarding/edit"
updateTime: "1767755095000"
---

# 编辑离职信息

该接口用于编辑飞书人事的[离职信息](https://people.feishu.cn/people/members/dimission/management)，支持的字段包括离职日期、离职原因、离职申请发起时间和离职申请审批通过时间等等，同时也支持编辑离职的自定义字段（附件字段除外）。当接口成功提交后，会产生对应的[离职信息变更](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/offboarding/events/updated)事件。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=offboarding&method=edit)

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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/offboardings/edit</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[20 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="corehr:offboarding.update:write" desc="编辑离职信息" support_app_types="custom,isv" tags="">编辑离职信息</md-perm>
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
	<md-text type="field-name" >offboarding_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	离职记录ID，不允许为空。可以通过[搜索离职信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/search)获取，取值于接口返回的data > items > offboarding_id

**示例值**："7095671727698478604"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >operator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	操作人雇佣 ID（employment_id），ID类型与查询参数 user_id_type取值一致：

1、当user_id_type取值为open_id时，ID获取方式参考[如何获取自己的Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)。

2、当user_id_type取值为user_id时，ID获取方式参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)。

3、当user_id_type取值为union_id时，ID获取方式参考[如何获取自己的 Union ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)。

4、当user_id_type取值为people_corehr_id时，先参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。

注意：为空时，默认系统操作人

**示例值**："6982509313466189341"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >update_data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	编辑字段数据信息，不允许为空。

**数据校验规则**：

- 长度范围：`0` ～ `10000`
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
（api_name）

注意：

1.该字段取值于[人员档案配置](https://people.feishu.cn/people/hr-settings/profile) > 信息配置 > 离职信息 中各字段的字段编码

2.自定义字段也可以通过[获取自定义字段列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query)获取

3.不可编辑的字段api_name
范围：

-wk_id

-wk_tenant_id

-employment

-process_id

-flow_id

-node_id

-initiator_id

-status

-checklist_status

-checklist_process_id

-type,hrbp_ids

-hrbp_list

-probation_id

-wk_created_at

-wk_created_by

-wk_updated_at

-wk_updated_by

-wk_deleted_at

-wk_is_deleted

-noncompete_agreement_id

-social_insurance_end_date

-provident_fund_end_date

-sign_type

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
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同，例如：

-文本类型（1）:"文本"

-布尔类型（2）:"true"

-数字类型（3）:"123"

-单值枚举类型（4）:"option_1"

-多值枚举类型（4）："[\"option_1\",\"option_2\"]"

-日期类型（7）:"2024-06-30"


注意：

1.枚举字段的枚举值取值于[人员档案配置](https://people.feishu.cn/people/hr-settings/profile) > 信息配置 > 离职信息 对应字段选项集的选项编码。

2.枚举字段值也可通过[获取字段详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/get_by_param)获取，参考接口返回的 字段详情 > 字段类型配置信息 > 选项配置信息 > 选项信息 > 枚举常量集 API name

3.人员字段目前只支持传入员工的雇佣ID。先参考[如何获取自己的 User ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。

4.暂不支持填写附件类型字段。

**示例值**："Sandy"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "offboarding_id": "7095671727698478604",
    "operator_id": "6982509313466189341",
    "update_data": [
        {
            "field_name": "name",
            "value": "Sandy"
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
	<md-text type="field-name" >data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >object_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	编辑字段数据信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	字段名
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
	字段值，是json转义后的字符串，根据元数据定义不同，字段格式不同(123, 123.23, true, [\"id1\",\"id2\], 2006-01-02 15:04:05])
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
        "data": [
            {
                "field_name": "name",
                "value": "Sandy"
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
  <md-td>1160103</md-td>
  <md-td>general internal server error code</md-td>
  <md-td>系统出现问题，如需帮助，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160102</md-td>
  <md-td>parameter is illegal</md-td>
  <md-td>入参不合法，请检查offboarding_id和update_data参数后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160203</md-td>
  <md-td>no current contract</md-td>
  <md-td>离职日期当天无有效的合同，请检查员工合同数据后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160204</md-td>
  <md-td>has future contract</md-td>
  <md-td>存在未来生效的合同，请检查员工合同数据后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160205</md-td>
  <md-td>contract has actual end date</md-td>
  <md-td>合同已存在实际结束日期，请检查员工合同数据后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160602</md-td>
  <md-td>offboarding is earlier than probation</md-td>
  <md-td>离职日期早于试用期开始日期，请检查员工试用期开始日期和离职日期后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160603</md-td>
  <md-td>offboarding is earlier than transform</md-td>
  <md-td>离职日期早于异动生效日期，请检查员工最后一条异动生效日期和离职日期后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160604</md-td>
  <md-td>reason explanation length exceed maximum</md-td>
  <md-td>离职原因说明或离职原因说明（员工）长度超过6000个字符，请检查长度后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160607</md-td>
  <md-td>offboarding is earlier than contract start date</md-td>
  <md-td>离职日期早于合同开始日期，请检查员工合同数据后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160608</md-td>
  <md-td>offboarding is later than contract end date</md-td>
  <md-td>离职日期晚于合同结束日期，请检查员工合同数据后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160610</md-td>
  <md-td>has no permission to edit this offboarding</md-td>
  <md-td>无权限编辑该离职，请检查应用的飞书人事（企业版）数据权限范围后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160710</md-td>
  <md-td>invalid block list</md-td>
  <md-td>屏蔽名单相关字段不合法，请检查屏蔽名单相关字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160200</md-td>
  <md-td>has approving transform</md-td>
  <md-td>存在审批中的异动，请撤销后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160601</md-td>
  <md-td>offboarding is earlier than onboarding</md-td>
  <md-td>离职日期早于入职日期，请检查离职日期后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160617</md-td>
  <md-td>hyperlink field format is illegal</md-td>
  <md-td>超链接字段格式不合法，请检查编辑字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160618</md-td>
  <md-td>text field exceeds maximum limit</md-td>
  <md-td>文本字段超过长度限制，单行文本不应超过255个字符，多行文本不应超过6000个字符,请检查编辑字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160619</md-td>
  <md-td>enum value of the enum field is invalid</md-td>
  <md-td>枚举字段值无效，请确认是否存在该枚举值后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160623</md-td>
  <md-td>not allowed to edit this offboarding</md-td>
  <md-td>不允许编辑，请确认离职流程审批通过且编辑字段在允许的范围内后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160624</md-td>
  <md-td>operator does not exist</md-td>
  <md-td>操作人ID不存在，请确认操作人是否存在后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160625</md-td>
  <md-td>offboarding does not exist</md-td>
  <md-td>离职ID不存在，请检查离职是否存在后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160631</md-td>
  <md-td>employee is not exist or has offboarded</md-td>
  <md-td>员工已离职或不存在，请检查离职员工是否存在后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160636</md-td>
  <md-td>custom employment does not exist</md-td>
  <md-td>自定义人员字段ID不存在，请检查填写的员工是否存在后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160637</md-td>
  <md-td>not support edit attachment</md-td>
  <md-td>不支持编辑附件类型字段，请检查提交数据是否包含附件类型字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160638</md-td>
  <md-td>invalid date time value</md-td>
  <md-td>日期类型字段值不合法，请检查提交数据中的日期类型字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160639</md-td>
  <md-td>invalid bool value</md-td>
  <md-td>布尔类型字段值不合法，请检查提交数据中的布尔类型字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160700</md-td>
  <md-td>non compete agreement field value is illegal</md-td>
  <md-td>竞业相关字段不合法，请确认竞业信息字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160304</md-td>
  <md-td>company id not found</md-td>
  <md-td>公司ID不存在，请检查填写的公司是否存在后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160300</md-td>
  <md-td>the department has been disable on the date of offboarding</md-td>
  <md-td>离职日期当天部门已停用，请检查离职日期后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160630</md-td>
  <md-td>invalid number value</md-td>
  <md-td>数字类型字段格式不合法，请检查提交数据中的数字类型字段后重新提交</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161000</md-td>
  <md-td>unknown error</md-td>
  <md-td>系统出现问题，如需帮助，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161001</md-td>
  <md-td>The current offboarding record is under modification approval; it cannot be edited.</md-td>
  <md-td>当前离职记录正在进行变更审批，不可编辑，请检查离职信息最新的状态</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161002</md-td>
  <md-td>The current offboarding record is under withdrawal approval; it cannot be edited.</md-td>
  <md-td>当前离职记录正在进行撤销审批，不可编辑，请检查离职信息最新的状态</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




