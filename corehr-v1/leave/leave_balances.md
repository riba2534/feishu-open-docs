---
title: "批量查询员工假期余额"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/leave_balances"
updateTime: "1729671178000"
---

# 批量查询员工假期余额

批量获取员工各个假期的余额数据。对应页面为假勤管理-休假管理-[假期报表](https://example.feishu.cn/people/workforce-management/manage/leave/leave_admin/balance){尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v1&resource=leave&method=leave_balances)

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
仅飞书人事企业版可用
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v1/leaves/leave_balances</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
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
            <md-perm name="corehr:corehr:readonly" desc="获取核心人事信息" support_app_types="custom,isv" tags="">获取核心人事信息</md-perm>
            <md-perm name="corehr:leave:read" desc="获取休假信息" support_app_types="custom,isv" tags="">获取休假信息</md-perm>
            <md-perm name="corehr:corehr" desc="更新核心人事信息" support_app_types="custom" tags="">更新核心人事信息</md-perm>
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

**示例值**：`{"eu_nc":"[\"6994333322503669260\"]"}`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >page_size</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	分页大小

**示例值**：20
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >as_of_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	查询截止日期，即截止到某天余额数据的日期（不传则默认为当天）。格式为yyyy-MM-dd

**示例值**：2022-07-29
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >employment_id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	员工 ID 列表，最大 100 个（不传则默认查询全部员工），对应user_id_type。请注意：此接口为get请求，所以传入数组时需要满足get请求传入数组的规范，例如employment_id_list=6919733291281024522&employment_id_list=6919733291281024523



**示例值**：6919733291281024526
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


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >time_zone</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	查询时区

**示例值**：Asia/Shanghai
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >include_offboard</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否获取离职折算字段，默认值为false

**示例值**：true
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
	<md-text type="field-name" >employment_leave_balance_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >employment_leave_balance\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	员工假期余额信息列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employment_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	雇佣信息ID，对应user_id_type
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employment_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	员工姓名
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	名称信息的语言
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	名称信息的内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >as_of_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	截止日期，即查询截止到某天余额数据的日期。格式为yyyy-MM-dd
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >leave_balance_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >leave_balance\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	假期余额列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >leave_type_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	假期类型ID，可用于
* [创建假期发放记录](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave_granting_record/create)
* [批量查询员工请假记录](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/leave_request_history)
* [通过过期时间获取发放记录](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/leave_employ_expire_record/get)
* [修改发放记录
](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/leave_accrual_record/patch)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >leave_type_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	假期类型名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	名称信息的语言
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
	名称信息的内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >historical_cycles_left</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	历史结转余额
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >this_cycle_total</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	当前周期发放
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >this_cycle_taken</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	已休（归属当前周期）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >leave_balance</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	假期余额
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >leave_duration_unit</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	假期时长单位

可选值有：

- 1: 天

- 2: 小时
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >history_cycle_accrual</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	历史结转发放，当入参include_offboard为true时返回
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >balance_in_current_cycle</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	当前周期余额
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >taken</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	已休时长，当入参include_offboard为true时返回
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >taken_history_cycle</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	历史周期已休时长
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >offboarding_balance</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	余额（离职折算），当入参include_offboard为true时返回
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >taken_current_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	已休时长（截止当日），当入参include_offboard为true时返回
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >offboarding_granted</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	本周期授予时长（离职折算），当入参include_offboard为true时返回
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
        "employment_leave_balance_list": [
            {
                "employment_id": "4718803945687580505",
                "employment_name": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "as_of_date": "2022-07-29",
                "leave_balance_list": [
                    {
                        "leave_type_id": "4718803945687580505",
                        "leave_type_name": [
                            {
                                "lang": "zh-CN",
                                "value": "张三"
                            }
                        ],
                        "historical_cycles_left": "0",
                        "this_cycle_total": "0",
                        "this_cycle_taken": "0",
                        "leave_balance": "0",
                        "leave_duration_unit": 1,
                        "history_cycle_accrual": "0",
                        "balance_in_current_cycle": "0",
                        "taken": "0",
                        "taken_history_cycle": "0",
                        "offboarding_balance": "0",
                        "taken_current_date": "0",
                        "offboarding_granted": "0"
                    }
                ]
            }
        ],
        "has_more": true,
        "page_token": "{\"eu_nc\":\"[\\\"6994333322503669260\\\"]\"}"
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
  <md-td>1160001</md-td>
  <md-td>No tenant ID</md-td>
  <md-td>租户ID为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160002</md-td>
  <md-td>Invalid granting unit</md-td>
  <md-td>授予单位出错</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160003</md-td>
  <md-td>Invalid effective date</md-td>
  <md-td>日期格式必须是类似“2020-01-01”</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160004</md-td>
  <md-td>Invalid granting quantity</md-td>
  <md-td>必须是能解析成数字的字符串，例如“2.5”</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160005</md-td>
  <md-td>Accessed data object not found</md-td>
  <md-td>检查leaveTypeID是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160006</md-td>
  <md-td>Employment not found</md-td>
  <md-td>检查employmentID是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160007</md-td>
  <md-td>Leave plan version not found</md-td>
  <md-td>假期计划版本数据不存在，请检查该类型的假期对应的计划配置是否创建</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160008</md-td>
  <md-td>Error occurred while checking if the employee is eligible for the vacation plan</md-td>
  <md-td>员工不适用于假期计划版本，请检查该假期计划适用人员范围是否和员工信息匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160009</md-td>
  <md-td>Accrual rule not found</md-td>
  <md-td>检查该假期计划版本是否正确创建，是否存在有效的发放规则</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160010</md-td>
  <md-td>Granting record already exists</md-td>
  <md-td>response里会带上已存在的发放记录的信息，用户可以将其取出，不需要再重试请求</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160011</md-td>
  <md-td>Error occurred when getting employment information</md-td>
  <md-td>获取员工信息失败</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160012</md-td>
  <md-td>An exception occurs in the database</md-td>
  <md-td>数据库异常，请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160013</md-td>
  <md-td>Error occurred while checking if the employee is eligible for the scope of application of the vacation plan</md-td>
  <md-td>检查员工是否符合假期计划适用范围时发生错误</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160014</md-td>
  <md-td>Error occurred when calculate accrual record</md-td>
  <md-td>计算授予计划错误</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160024</md-td>
  <md-td>There is a subclass for the leave type, but the subclass ID has not been passed</md-td>
  <md-td>如果假期类型存在子类，那么leaveTypeID必须传子类ID</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160025</md-td>
  <md-td>The granting quantity range is from -9999 to 9999</md-td>
  <md-td>额度范围为-9999～9999</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160026</md-td>
  <md-td>The number of decimal places of the granted quantity cannot exceed 6</md-td>
  <md-td>发放数量最多6位小数</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160027</md-td>
  <md-td>The length of the granting reason cannot exceed 3000</md-td>
  <md-td>授予原因长度最多3000</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160028</md-td>
  <md-td>There is an error in the unit conversion configuration in the granting rule</md-td>
  <md-td>检查假期计划版本的单位转换规则是否配置正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160029</md-td>
  <md-td>The leave type has been deactivated</md-td>
  <md-td>不能往已停用的假期类型写发放记录</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1169999</md-td>
  <md-td>Unknown error</md-td>
  <md-td>未知错误，请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160015</md-td>
  <md-td>Internal error</md-td>
  <md-td>内部错误，请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160016</md-td>
  <md-td>Invalid param</md-td>
  <md-td>对照接口文档的入参排查，是否漏填参数、格式错误等（例如数值参数传了字母、日期格式错误等）</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160017</md-td>
  <md-td>User not found</md-td>
  <md-td>未找到用户信息</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160018</md-td>
  <md-td>Invalid leave balance calculate Conf</md-td>
  <md-td>无效的假期余额计算配置</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160019</md-td>
  <md-td>The calculation result of leave balance is empty</md-td>
  <md-td>假期余额计算为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160020</md-td>
  <md-td>When calculating the leave balance, there is no leave plan version that matches the employee</md-td>
  <md-td>没有与员工匹配的假期计划版本</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160021</md-td>
  <md-td>For the leave type that is not granted according to the cycle, balance calculation is not supported</md-td>
  <md-td>不按周期授予的假期类型，不支持余额计算</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160022</md-td>
  <md-td>The data of the leave plan version is invalid</md-td>
  <md-td>假期计划版本数据不合法</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160023</md-td>
  <md-td>Error occurred when calculating the leave balance</md-td>
  <md-td>假期余额计算出错</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160030</md-td>
  <md-td>The length of the granted unique ID cannot exceed 64</md-td>
  <md-td>授予唯一ID长度不能超过64</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160031</md-td>
  <md-td>This granting record cannot be edited or deleted</md-td>
  <md-td>该授予记录不可编辑或删除</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160032</md-td>
  <md-td>The expiration time of this granting record is invalid</md-td>
  <md-td>该授予记录过期时间不合法</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160033</md-td>
  <md-td>The effective date is after the granting date</md-td>
  <md-td>生效日期在发放日期之后</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160034</md-td>
  <md-td>The expiration date format is incorrect</md-td>
  <md-td>失效日期格式错误</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160035</md-td>
  <md-td>No permission to access the employee data</md-td>
  <md-td>无权访问该员工数据</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




