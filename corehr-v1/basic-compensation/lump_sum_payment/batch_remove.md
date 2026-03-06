---
title: "批量删除一次性支付记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/compensation-v1/lump_sum_payment/batch_remove"
updateTime: "1755603246000"
---

# 批量删除一次性支付记录

传入一次性支付记录ID，删除ID对应的一次性支付记录{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=compensation&version=v1&resource=lump_sum_payment&method=batch_remove)

:::html
<md-alert type="tip">
一次性支付记录被删除后，通过查询一次性支付授予明细接口或者查询一次性支付授予记录接口将查不到该数据
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
      <md-td>https://open.feishu.cn/open-apis/compensation/v1/lump_sum_payment/batch_remove</md-td>
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
	<md-text type="field-name" >record_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	要删除的一次性支付记录id（通过[【查询一次性支付记录】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/compensation-v1/lump_sum_payment/query) 接口进行查询）

**示例值**：["7337149697626801708"]

**数据校验规则**：

- 长度范围：`0` ～ `500`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	因重复提交删除

**示例值**："删除原因实例"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "record_ids": [
        "7337149697626801708"
    ],
    "reason": "删除原因实例"
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
<md-enum-item key="21270211" >"The bonus details amount format is incorrect" 奖金明细金额格式不正</md-enum-item>
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




