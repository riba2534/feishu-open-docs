---
title: "创建薪资档案"
fullPath: "/uAjLw4CM/ukTMukTMukTM/compensation-v1/archive/create"
updateTime: "1757469687000"
---

# 创建薪资档案

- 该接口适用于员工入职定薪、调薪或者更正档案场景，通过创建调薪任务的方式，为员工生成对应薪资档案数据。
- 当员工在调薪生效日期存在档案数据时，则是对该档案进行更正操作。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=compensation&version=v1&resource=archive&method=create)

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
      <md-td>https://open.feishu.cn/open-apis/compensation/v1/archives</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
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
            <md-perm name="corehr:compensation_archive:write" desc="创建定调薪任务" support_app_types="custom" tags="">创建定调薪任务</md-perm>
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
	是
	</md-dt-td>
	<md-dt-td>
	用户 ID 类型

**示例值**：open_id

**可选值有**：
<md-enum>
<md-enum-item key="open_id" >标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)</md-enum-item>
<md-enum-item key="union_id" >标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)</md-enum-item>
<md-enum-item key="user_id" >标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)</md-enum-item>
<md-enum-item key="people_corehr_id" >以people_corehr_id来识别用户</md-enum-item>
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
	<md-text type="field-name" >unique_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	外部幂等id，表示操作的唯一标识，避免重复发起，格式为标准的UUIDV4（32 个十六进制字符 + 4 个连字符）

**示例值**："123e4567-e89b-42d3-a456-426614174000"
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
	操作人ID，具体类型由入参中的 user_id_type 指定，选择应用身份鉴权时，该参数不能为空

**示例值**："7337149697626801708"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	员工id，具体类型由入参中的 user_id_type 指定

**示例值**："7337149697626801708"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >effective_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	生效时间，日期格式为 YYYY-MM-DD，字符长度为10

**示例值**："2024-11-12"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >currency_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	币种ID，通过[查询货币信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search?appId=cli_a63f5fc01866100c)接口可获得

**示例值**："6863329932261459464"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >plan_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	薪资方案ID，通过[批量查询薪资方案](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/compensation-v1/plan/list)接口可获得

**示例值**："7431430313074247212"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >plan_tid</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	薪资方案TID，通过[批量查询薪资方案](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/compensation-v1/plan/list)可获得

**示例值**："7431430313074279980"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >change_reason_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	调薪原因ID，通过[批量查询定调薪原因](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/compensation-v1/change_reason/list)接口可获得

**示例值**："7125907336899888684"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >item_value_lists</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >archive_item_value\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	- 薪资项值集合，所填薪资项信息必须是该方案中的薪资项
- 仅需填写方案中可编辑的薪资项即可，不可编辑的薪资项不能传入，否则会校验报错。 
- 根据参数plan_id，可通过[批量查询薪资方案](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/compensation-v1/plan/list)接口获得对应的具体方案信息

**数据校验规则**：

- 长度范围：`0` ～ `2147483647`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >item_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	薪资项ID，具体值可通过接口查询[批量查询薪资项](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/compensation-v1/item/list)

**示例值**："7244131355509917228"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >item_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	- 薪资项的值，该值的单位取决于入参currency_id对应的币种
- 字符串为数字格式，且长度最大不超过18个字符，最小长度为1个字符，不支持负数，不允许为空

**示例值**："200.00"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >item_value_regular</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	- 员工转正后薪资项的值，该值的单位取决于入参currency_id对应的币种。字符串为数字格式，且长度不超过18个字符，不支持负数
- 当员工处于试用期且入参plan_id对应的薪资方案已开启试用期时，才能填写该值。
- 所有可编辑薪资项的转正值要么都为空，要么都不为空，否则会报错。

**示例值**："600.00"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	调薪说明，长度不超过1000字符

**示例值**："因2024年Q2绩效优秀，对该同学调薪10%"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >edit_remark</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	更正说明，长度不超过1000字符，如果本次操作为更正员工薪资档案时，该字段即为更正调薪的说明。

**示例值**："更正2024年Q2绩效调薪金额"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "unique_id": "123e4567-e89b-42d3-a456-426614174000",
    "operator_id": "7337149697626801708",
    "user_id": "7337149697626801708",
    "effective_time": "2024-11-12",
    "currency_id": "6863329932261459464",
    "plan_id": "7431430313074247212",
    "plan_tid": "7431430313074279980",
    "change_reason_id": "7125907336899888684",
    "item_value_lists": [
        {
            "item_id": "7244131355509917228",
            "item_value": "200.00",
            "item_value_regular": "600.00"
        }
    ],
    "description": "因2024年Q2绩效优秀，对该同学调薪10%",
    "edit_remark": "更正2024年Q2绩效调薪金额"
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
	<md-text type="field-name" >unique_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	定调薪任务创建的唯一ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >archive_tid</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	薪资档案的TID
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
        "unique_id": "123e4567-e89b-42d3-a456-426614174000",
        "archive_tid": "7434007780111336970"
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
  <md-td>2290001</md-td>
  <md-td>param is empty</md-td>
  <md-td>参数为空报错，请排查是否有参数为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290002</md-td>
  <md-td>effective time is invalid, correct example: 2024-01-01</md-td>
  <md-td>生效时间不合法，格式应为：2024-01-01</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290003</md-td>
  <md-td>Invalid user ID, cannot find employment</md-td>
  <md-td>人员id无法查询到对应员工，请确认人员id是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>2290004</md-td>
  <md-td>service error</md-td>
  <md-td>服务内部错误，请稍后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290005</md-td>
  <md-td>No permission to adjust</md-td>
  <md-td>- 没有创建薪资档案的权限，请检查应用身份/用户身份的权限设置。
- 首先进入到应用设置页面，选择权限配置，核对权限配置是否合理</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290006</md-td>
  <md-td>The plan not exist, please check plan_tid</md-td>
  <md-td>薪资方案不存在，检查入参的薪资方案id和tid</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290007</md-td>
  <md-td>the description is too long, limit 1000</md-td>
  <md-td>调薪说明长度过长，长度不能超过1000</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290008</md-td>
  <md-td>the edit remark is too long, limit 1000</md-td>
  <md-td>更正说明过长，不能超过1000</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290009</md-td>
  <md-td>the change reason does not exist</md-td>
  <md-td>调薪原因不存在，请检查参数change_reason_id</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290010</md-td>
  <md-td>the currency not exist, please check currency_id</md-td>
  <md-td>币种不存在，请检查参数currency_id</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290011</md-td>
  <md-td>the currency not match with the plan currency</md-td>
  <md-td>所传币种与方案的币种不一致</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290012</md-td>
  <md-td>Invalid user ID, cannot find employment</md-td>
  <md-td>人员id不存在，请检查人员userID信息</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290013</md-td>
  <md-td>employment id to people id failed,   please check user_id</md-td>
  <md-td>无法通过员工ID找到该人员的people id</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290014</md-td>
  <md-td>effective time is invalid, correct example: 2024-01-01</md-td>
  <md-td>生效时间不合法，格式为2024-01-01</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290015</md-td>
  <md-td>the effective time is range out of limit, limit（1970-01-01, 2038-01-19）</md-td>
  <md-td>生效时间不能超过限制，日期需大于1970-01-01，且小于2038-01-19</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290016</md-td>
  <md-td>archive effective time is not allow before the plan effective time</md-td>
  <md-td>档案生效时间早于方案生效时间，请修改参数的生效时间，或者修改薪资方案的对应生效时间</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290017</md-td>
  <md-td>the plan status is deactivate</md-td>
  <md-td>薪资方案已停用，请先启用方案</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290018</md-td>
  <md-td>the effective time is after employee's last day, please check effective_time</md-td>
  <md-td>生效时间不能超过员工离职日期</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290019</md-td>
  <md-td>the effective time is before employee's hire day, please check effective_time</md-td>
  <md-td>生效时间不能早于员工入职日期</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290020</md-td>
  <md-td>miss required archive items, please check item_value_lists</md-td>
  <md-td>缺少必填的的薪资项，方案中可编辑的薪资项都需要填写。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290021</md-td>
  <md-td>the item not allow to edit  or  the item not in plan, please check item_value_lists

</md-td>
  <md-td>方案中不存在该薪资项，或者存在不可编辑的薪资项，请完整填写方案中允许编辑的薪资项。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290022</md-td>
  <md-td>the item value is invalid, value must be a positive number and cannot be greater than 9223372036854775807</md-td>
  <md-td>薪资项的值需为正数，且不能大于9223372036854775807</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290023</md-td>
  <md-td>the plan is not open probation, the item not allow to have regular value</md-td>
  <md-td>薪资方案未开启试用期，薪资项不允许有转正值</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290024</md-td>
  <md-td>the employee is not in probation, the item not allow to have  regular value</md-td>
  <md-td>人员不在试用期内，不允许填写转正值</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290025</md-td>
  <md-td>under this effective date, employees' adjust items are not allowed to have  regular value</md-td>
  <md-td>在该生效时间下，给用户进行调薪操作，不允许存在转正值</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290026</md-td>
  <md-td>regular item values ​​are either all empty or all null. Values ​​must be positive numbers and cannot be greater than 9223372036854775807</md-td>
  <md-td>薪资项的转正值要么都为空，要么都不为空，且为正数，不能大于9223372036854775807</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290027</md-td>
  <md-td>match standard fail</md-td>
  <md-td>- 匹配薪资标准出错，请排查系统是否尚未配置对应的薪资标准
- 首先进入到飞书人事的薪资标准表设置页面，排查是否存在该员工能匹配上的薪资标准</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290028</md-td>
  <md-td>unique id is exist, please change</md-td>
  <md-td>唯一id已存在并使用，请使用新的唯一id</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290029</md-td>
  <md-td>operator id invalid, If using application identity for authentication, the operator id must be valid</md-td>
  <md-td>- 操作人ID不合法，如果选择应用身份鉴权，则入参operator_id不能为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290030</md-td>
  <md-td>operator id invalid, If using application identity for authentication, the operator id must be valid</md-td>
  <md-td>操作人ID不合法，如果选择应用身份鉴权，则入参operator_id不能为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290031</md-td>
  <md-td>This user already has a duplicate salary adjustment task under the effective date</md-td>
  <md-td>用户在当前生效日期下，已经存在有尚未结束的调薪任务，请先结束该调薪任务后再发起</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290032</md-td>
  <md-td>The user has unfinished salary adjustment tasks and cannot initiate another salary adjustment.</md-td>
  <md-td>用户存在尚未完成的调薪任务，请先完成该调薪任务</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290033</md-td>
  <md-td>effective_time is empty</md-td>
  <md-td>生效时间为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290034</md-td>
  <md-td>plan_id is empty</md-td>
  <md-td>方案id为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290035</md-td>
  <md-td>plan_tid is empty</md-td>
  <md-td>方案tid为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290036</md-td>
  <md-td>currency_id is empty</md-td>
  <md-td>币种id为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290037</md-td>
  <md-td>user_id is empty</md-td>
  <md-td>用户id为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290038</md-td>
  <md-td>unique_id is empty</md-td>
  <md-td>唯一id为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290039</md-td>
  <md-td>change_reason_id is empty</md-td>
  <md-td>调薪原因为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290040</md-td>
  <md-td>There are duplicate items in item_value_lists, please check item_value_lists</md-td>
  <md-td>薪资项不允许重复，请检查是否存在相同id的薪资项</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290041</md-td>
  <md-td>the item value is invalid, value must be a positive number and cannot be greater than 9223372036854775807</md-td>
  <md-td>薪资项的值需为正数，且不能大于9223372036854775807</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2290042</md-td>
  <md-td>regular item values ​​are either all empty or all null. Values ​​must be positive numbers and cannot be greater than 9223372036854775807</md-td>
  <md-td>薪资项的转正值需为正数，且不能大于9223372036854775807</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




