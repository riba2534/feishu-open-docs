---
title: "批量创建一次性支付记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/compensation-v1/lump_sum_payment/batch_create"
updateTime: "1755603208000"
---

# 批量创建一次性支付记录

通过传入的一次性支付记录数据，校验并创建一次性支付记录，并返回创建失败原因或创建成功数据的ID{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=compensation&version=v1&resource=lump_sum_payment&method=batch_create)

:::html
<md-alert type="tip">
本接口支持部分成功，失败部分详细报错信息参考 `data.operate_results.code`。
- 当 `data.operate_results.code` 存在非 0 时，响应体 code 仍可能返回 0
- 仅当出现非预期异常时，响应体 code 才会为非 0
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
      <md-td>https://open.feishu.cn/open-apis/compensation/v1/lump_sum_payment/batch_create</md-td>
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
            <md-perm name="corehr:compensation.lump_sum_payment:write" desc="一次性支付写权限" support_app_types="custom" tags="">一次性支付写权限</md-perm>
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
	<md-text type="field-name" >records</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >lump_sum_payment_for_create\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	要创建的一次性支付信息

**数据校验规则**：

- 长度范围：`0` ～ `500`
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
	是
	</md-dt-td>
	<md-dt-td>
	外部幂等id，由上游业务决定

**示例值**："7402510801304718380_7309316347007764012_7402523725868058156_1726070400000_10000"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
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

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >total_amount</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	总金额，字符串表达的数字，单位为入参中 currency_id 给定的币种

**示例值**："2000.00"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >binding_period</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	绑定期，单位为月

**示例值**：2

**数据校验规则**：

- 取值范围：`0` ～ `2147483647`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
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
	币种 id（通过[【查询币种】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-currency/search)) 接口进行查询）

**示例值**："6863329932261459464"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >issuance_frequency</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	发放次数，必须与 details 的长度一致

**示例值**：3

**数据校验规则**：

- 取值范围：`0` ～ `2147483647`
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
	薪酬项 id（通过[【查询薪酬项】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/compensation-v1/item/list)) 接口进行查询）

**示例值**："7411039006180312620"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >reference_period_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	所属期开始日期

**示例值**："2024-08-01"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >reference_period_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	所属期结束日期

**示例值**："2024-08-01"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >details</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >lump_sum_payment_detail_for_create\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	发放明细列表

**数据校验规则**：

- 长度范围：`0` ～ `2147483647`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >issuance_amount</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	一次性支付明细发放金额，可转数字的字符串，单位为入参中 currency_id 给定的币种

**示例值**："2000.00"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >issuance_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	发放状态

**示例值**："to_be_issued"

**可选值有**：
<md-enum>
<md-enum-item key="to_be_issued" >应发放</md-enum-item>
<md-enum-item key="not_issued" >不发放</md-enum-item>
</md-enum>

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >issuance_way</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	发放方式

**示例值**："with_salary"

**可选值有**：
<md-enum>
<md-enum-item key="with_salary" >随工资发放</md-enum-item>
<md-enum-item key="with_cash" >现金发放</md-enum-item>
<md-enum-item key="with_year_end_bonus" >随年终奖发放</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >issuance_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	发放时间

**示例值**："2024-08-01"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >belong_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	申请发放日期

**示例值**："2025-01-20"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >issuance_country_region_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	发放国家ID（可通过[查询国家/地区信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/basic_info-country_region/search)进行查询）

**示例值**："6862995757234914824"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >issuance_pay_group_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	发放薪资组ID（可通过[获取薪资组基本信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/paygroup/list)
进行查询）

**示例值**："6862995757234914824"

**数据校验规则**：

- 长度范围：`0` ～ `255` 字符
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

**示例值**："该员工表现优异，为其发放一笔奖金"

**数据校验规则**：

- 长度范围：`0` ～ `3000` 字符
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "records": [
        {
            "unique_id": "7402510801304718380_7309316347007764012_7402523725868058156_1726070400000_10000",
            "user_id": "7337149697626801708",
            "total_amount": "2000.00",
            "binding_period": 2,
            "currency_id": "6863329932261459464",
            "issuance_frequency": 3,
            "item_id": "7411039006180312620",
            "reference_period_start_date": "2024-08-01",
            "reference_period_end_date": "2024-08-01",
            "details": [
                {
                    "issuance_amount": "2000.00",
                    "issuance_status": "to_be_issued",
                    "issuance_way": "with_salary",
                    "issuance_time": "2024-08-01",
                    "belong_time": "2025-01-20",
                    "issuance_country_region_id": "6862995757234914824",
                    "issuance_pay_group_id": "6862995757234914824"
                }
            ],
            "remark": "该员工表现优异，为其发放一笔奖金"
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
	<md-text type="field-name" >operate_results</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >lump_sum_payment_operate_result\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	每条记录的操作结果。对于创建成功的记录，会返回创建后的一次性支付记录id
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
	操作的记录的 id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >unique_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	操作的记录的 unique_id
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	操作结果状态码

**可选值有**：
<md-enum>
<md-enum-item key="0" >"Success" 操作成功</md-enum-item>
<md-enum-item key="21270201" >"The bonus to be changed does not exist" 要更改的奖金不存在</md-enum-item>
<md-enum-item key="21270202" >"Idempotent ID conflict" 幂等id冲突</md-enum-item>
<md-enum-item key="21270203" >"The total amount format is incorrect" 总金额格式不正确</md-enum-item>
<md-enum-item key="21270205" >"Only use the number of decimal places specified in the bonus item rules" 仅限使用奖金项规则中规定的小数位数</md-enum-item>
<md-enum-item key="21270206" >"The sum of the bonus details does not equal the total amount" 奖金明细金额之和不等于总金额</md-enum-item>
<md-enum-item key="21270207" >"issuance frequency not equal to size of details" 奖金明细总数不等于发放次数</md-enum-item>
<md-enum-item key="21270208" >"The number of issuances is less than or equal to 0" 发放次数小于等于0</md-enum-item>
<md-enum-item key="21270209" >"The currency is empty or does not exist" 币种为空或不存在</md-enum-item>
<md-enum-item key="21270210" >"Notes are too long" 备注超长</md-enum-item>
<md-enum-item key="21270211" >"The bonus details amount format is incorrect" 奖金明细金额格式不正确</md-enum-item>
<md-enum-item key="21270213" >"The bonus details payment time format is incorrect" 奖金明细的发放时间格式不正确</md-enum-item>
<md-enum-item key="21270214" >"The bonus details are issued in an illegal manner" 奖金明细的发放方式不合法</md-enum-item>
<md-enum-item key="21270215" >"The bonus details are not in a valid payment status" 奖金明细的发放状态不合法</md-enum-item>
<md-enum-item key="21270217" >"Employees are not covered by the bonus rules" 员工不在奖金项规则适用范围之内</md-enum-item>
<md-enum-item key="21270218" >"The method of awarding bonus details is not covered by the bonus item rules" 奖金明细的发放方式不在奖金项规则适用范围之内</md-enum-item>
<md-enum-item key="21270219" >"Bonus item rules do not support configuration of binding period" 奖金项规则不支持配置绑定期</md-enum-item>
<md-enum-item key="21270220" >"The bonus details payment status is "paid", and cannot be modified" 奖金明细发放状态为「已发放」，不支持修改</md-enum-item>
<md-enum-item key="21270221" >"The bonus item rules already include the currency, and other currencies cannot be specified" 奖金项规则已包含币种，不支持指定其他币种</md-enum-item>
<md-enum-item key="21270222" >"The salary item does not exist" 薪酬项不存在</md-enum-item>
<md-enum-item key="21270223" >"Employee does not exist" 员工不存在</md-enum-item>
<md-enum-item key="21270224" >"The bonus details payment status is "paid", and deletion is not supported" 奖金明细发放状态为「已发放」，不支持删除</md-enum-item>
<md-enum-item key="21270225" >"Bonus rules do not allow multiple awards" 奖金项规则不允许多次发放</md-enum-item>
<md-enum-item key="21270226" >"No data permission" 无数据权限</md-enum-item>
<md-enum-item key="21270227" >"Only positive integers are allowed for the binding period" 绑定期只允许正整数</md-enum-item>
<md-enum-item key="21270228" >"This bonus does not currently support custom binding periods. Please configure and write according to the rules for the binding period of the salary item" 该奖金暂不支持自定义绑定期，请按照薪酬项绑定期规则配置写入</md-enum-item>
<md-enum-item key="21270229" >"The application issuance date must not be later than the issuance date" 申请发放日期不得晚于发放日期</md-enum-item>
<md-enum-item key="21270230" >"The application payment date format of the bonus details is incorrect" 奖金明细的申请发放日期格式不正确</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >message</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	操作结果描述
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
        "operate_results": [
            {
                "id": "7390583861280556588",
                "unique_id": "7390583861280556588",
                "code": 21270202,
                "message": "uqniue id conflict"
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
  <md-td>2290001</md-td>
  <md-td>param is invalid</md-td>
  <md-td>参数异常，请检查入参</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>2290002</md-td>
  <md-td>server error</md-td>
  <md-td>服务端异常，请稍后重试</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




