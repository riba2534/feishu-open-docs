---
title: "查询发薪活动明细列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/payroll-v1/payment_activity_detail/list"
updateTime: "1741609527000"
---

# 查询发薪活动明细列表

根据「发薪活动 ID 」和「分页参数」查询发薪活动明细列表和关联的算薪明细分段数据。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=payroll&version=v1&resource=payment_activity_detail&method=list)

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

## 使用场景

> 当前接口仅支持查询某个发薪活动下的所有发薪明细数据，若需要查询某些员工在特定范围内的发薪明细，请使用[批量查询发薪明细](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/payment_detail/query)接口。

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
      <md-td>https://open.feishu.cn/open-apis/payroll/v1/payment_activity_details</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[5 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="payroll:payment_activity_details:read" desc="获取发薪明细数据" support_app_types="custom,isv" tags="">获取发薪明细数据</md-perm>
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

**数据校验规则**：

- 取值范围：`1` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >activity_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	发薪活动 ID，调用[查询发薪活动列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/payment_activity/list)接口后，可以从返回结果中获取到发薪活动 ID。

**示例值**：7202076988667019308
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

**示例值**：7202076988667019333

**数据校验规则**：

- 长度范围：`0` ～ `100`
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
	<md-text type="field-name" >payment_activity_details</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >payment_activity_detail\[\]</md-text>
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
	<md-text type="field-name" >payment_details</md-text>
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
        "payment_activity_details": [
            {
                "employee_id": "7202076988667019308",
                "payment_details": [
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
  <md-td>500</md-td>
  <md-td>2500003</md-td>
  <md-td>rpc fail</md-td>
  <md-td>请求调用出错，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500004</md-td>
  <md-td>current payment activity is not exist or deleted</md-td>
  <md-td>当前发薪活动不存在或已被删除。</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




