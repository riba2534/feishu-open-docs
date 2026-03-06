---
title: "批量查询发薪明细"
fullPath: "/uAjLw4CM/ukTMukTMukTM/payroll-v1/payment_detail/query"
updateTime: "1772457976000"
---

# 批量查询发薪明细

根据 __发薪活动 ID 列表__ 、__发薪日起止时间__ 和 __飞书人事雇佣 ID 列表__ 分页查询发薪明细列表和关联的算薪明细分段数据。

{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=payroll&version=v1&resource=payment_detail&method=query)

:::html
<md-alert type="tip">

</md-alert>
:::

:::html
<md-alert type="warn">
当前接口仅支持查询某些员工在特定范围内的发薪明细，若需要查询某个发薪活动下的所有发薪明细数据，请使用[查询发薪活动明细列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/payment_activity_detail/list)接口。
</md-alert>
:::

:::html
<md-alert type="error">

</md-alert>
:::

## 注意事项
1. 批量查询发薪明细接口提供的请求参数中，用户必须填写「__发薪日起止时间__（pay_period_start_date，pay_period_end_date）」或「__发薪活动 ID 列表__」，当传入的三个参数均为空时，开放接口将返回 2500006 错误码。
2. 每一次调用接口时，系统最多会扫描 __50__ 个发薪活动，当用户传入的查询条件命中的发薪活动个数大于 __50__ 时，开放接口将根据查询参数返回 2500003 或 2500008 错误码，请合理使用查询参数。
3. 开放接口中的「员工的飞书人事雇佣 ID 列表（employee_ids）」参数为必填。
4. **批量查询发薪明细接口数据取自发薪活动**，调用前请先创建发薪活动并完成算薪活动关联。

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
      <md-td>https://open.feishu.cn/open-apis/payroll/v1/payment_detail/query</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[1 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="payroll:payment_details:read" desc="获取发薪明细数据V2" support_app_types="custom,isv" tags="">获取发薪明细数据V2</md-perm>
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
	<md-text type="field-name" >page_index</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	页码，第一页从 1 开始

**示例值**：100

**数据校验规则**：

- 取值范围：`1` ～ `100000`
	</md-dt-td>
</md-dt-tr>


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
	每页大小，范围为：[1, 100]

**示例值**：10
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >acct_item_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	算薪项 ID 列表，调用[批量查询算薪项](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/acct_item/list)接口后，可以从返回结果中获取到算薪项 ID。
1. 当前参数传空时，接口会返回发薪明细中所有的算薪项；
2. 当前参数不为空时，接口只返回发薪明细中与 acct_item_ids 存在交集的算薪项。

**示例值**：["7202076988667019333"]

**数据校验规则**：

- 长度范围：`0` ～ `100000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >employee_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	员工的飞书人事雇佣 ID 列表，__该参数为必填__，调用[搜索员工信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口后，可以从返回结果中获取到飞书人事雇佣 ID。

注：调用[搜索员工信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口时，查询入参 user_id_type 应为  people_corehr_id。

**示例值**：["7202076988667019222"]

**数据校验规则**：

- 长度范围：`1` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >pay_period_start_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	发薪日开始时间，格式：YYYY-MM-dd，[pay_period_start_date, pay_period_end_date] 是一个左闭右闭区间。

**示例值**："2024-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >pay_period_end_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	发薪日结束时间，格式：YYYY-MM-dd，[pay_period_start_date, pay_period_end_date] 是一个左闭右闭区间。
1. pay_period_start_date 不得晚于 pay_period_end_date 。
2. [pay_period_start_date, pay_period_end_date] 最大间隔为 12 个月。

**示例值**："2024-01-31"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >activity_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	发薪活动 ID 列表，调用[查询发薪活动列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/payment_activity/list)接口后，可以从返回结果中获取到发薪活动 ID。

**示例值**：["7202076988667019308"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >include_segment_data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否需要查询算薪明细的分段信息，如果不传该参数或传 false ，那么只返回发薪活动明细数据；如果该参数传了 true，那么同时返回发薪明细对应的算薪明细分段数据。

**示例值**：false
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "page_index": 100,
    "page_size": 10,
    "acct_item_ids": [
        "7202076988667019333"
    ],
    "employee_ids": [
        "7202076988667019222"
    ],
    "pay_period_start_date": "2024-01-01",
    "pay_period_end_date": "2024-01-31",
    "activity_ids": [
        "7202076988667019308"
    ],
    "include_segment_data": false
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
	<md-text type="field-name" >payment_details</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >payment_detail\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	发薪明细列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employee_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	员工的飞书人事雇佣 ID，调用[搜索员工信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口后，可以从返回结果中获取到飞书人事雇佣 ID。

注：调用[搜索员工信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)接口时，查询入参 user_id_type 应为  people_corehr_id。
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
	发薪明细所在的发薪活动 ID，调用[查询发薪活动列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/payment_activity/list)接口后，可以从返回结果中获取到发薪活动 ID。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >payment_accounting_items</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >payment_accounting_item\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	发薪明细详情
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
	算薪项 ID，调用[批量查询算薪项](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/acct_item/list)接口后，可以从返回结果中获取到算薪项 ID。

注：明细中返回的部分算薪项可能不存在于[批量查询算薪项](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/acct_item/list)的接口结果中。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >accounting_item_names</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	算薪项名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语种
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
	语种对应的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >accounting_item_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >accounting_item_value</md-text>
	</md-dt-td>
	<md-dt-td>
	算薪项值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >original_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	算薪项数据原始值，当发薪明细的数据来源为「人工导入」时，如果当前算薪项类型为引用类型，那么算薪项原始值可能为空。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >reference_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	引用类型算薪项展示值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语种
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
	语种对应的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >segment_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >segment_value\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	算薪项分段数据
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >start_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	分段开始时间-毫秒级时间戳，[start_time, end_time] 是一个左闭右闭区间。
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
	分段结束时间-毫秒级时间戳，[start_time, end_time] 是一个左闭右闭区间。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >reference_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n_content\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	引用类型算薪项分段展示值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >locale</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语种
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
	语种对应的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >original_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	算薪项分段原始值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >accounting_item_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	算薪项类型，1-文本；2-金额；3-数值；4-百分比；5-日期；6-引用
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >total</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	发薪明细总数
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
        "payment_details": [
            {
                "employee_id": "7202076988667019308",
                "activity_id": "7202076988667019308",
                "payment_accounting_items": [
                    {
                        "id": "7202076988667019308",
                        "accounting_item_names": [
                            {
                                "locale": "zh_cn",
                                "value": "名称"
                            }
                        ],
                        "accounting_item_value": {
                            "original_value": "100",
                            "reference_values": [
                                {
                                    "locale": "zh_cn",
                                    "value": "名称"
                                }
                            ]
                        },
                        "segment_values": [
                            {
                                "start_time": "7220356259681386540",
                                "end_time": "7220356259681386540",
                                "reference_values": [
                                    {
                                        "locale": "zh_cn",
                                        "value": "名称"
                                    }
                                ],
                                "original_value": "10000"
                            }
                        ],
                        "accounting_item_type": 1
                    }
                ]
            }
        ],
        "total": 50000
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
  <md-td>2500001</md-td>
  <md-td>unknown error</md-td>
  <md-td>未知错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2500002</md-td>
  <md-td>param is invalid</md-td>
  <md-td>参数错误，请检查参数。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2500003</md-td>
  <md-td>Too many payment activities. Please reduce the number of "payment activity ID list".</md-td>
  <md-td>发薪活动数量过多，请减少「发薪活动 ID 列表」个数。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2500004</md-td>
  <md-td>Pay date range can't exceed 12 months. Please shorten the pay date range.</md-td>
  <md-td>发薪日时间范围不能超过12个月，请缩短发薪日时间范围。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2500005</md-td>
  <md-td>Employee ID list is too long. Please reduce it to within 100 characters.</md-td>
  <md-td>员工 ID 列表过长，请减少至100个以内。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2500006</md-td>
  <md-td>Pay start and end dates and payment activity ID can't both be empty.</md-td>
  <md-td>发薪起止日、发薪活动 ID 不得均为空。</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>2500007</md-td>
  <md-td>rpc fail</md-td>
  <md-td>请求调用出错，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2500008</md-td>
  <md-td>Too many payment activities. Please shorten the pay date range.</md-td>
  <md-td>发薪活动数量过多，请缩短发薪日时间范围。</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




