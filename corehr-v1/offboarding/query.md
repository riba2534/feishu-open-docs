---
title: "查询员工离职原因列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/query"
updateTime: "1721042513000"
---

# 查询员工离职原因列表

该接口用于查询[离职配置](https://people.feishu.cn/people/hr-settings/dimission/setting)> 离职原因的选项信息，包括离职原因选项的唯一标识、名称和启用状态等信息。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v1&resource=offboarding&method=query)

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
      <md-td>https://open.feishu.cn/open-apis/corehr/v1/offboardings/query</md-td>
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
            <md-perm name="corehr:common_data.preset_data:read" desc="获取预置数据信息" support_app_types="custom,isv" tags="">获取预置数据信息</md-perm>
            <md-perm name="corehr:corehr:readonly" desc="获取核心人事信息" support_app_types="custom,isv" tags="">获取核心人事信息</md-perm>
            <md-perm name="corehr:corehr" desc="更新核心人事信息" support_app_types="custom" tags="">更新核心人事信息</md-perm>
            <md-perm name="corehr:common_data.preset_data:write" desc="更新预置数据信息" support_app_types="custom" tags="">更新预置数据信息</md-perm>
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
	<md-text type="field-name" >active</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职原因状态，为空时默认搜索所有状态的离职原因。可选项有:

-true: 启用

-false: 停用

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offboarding_reason_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	离职原因唯一标识列表，用于过滤离职原因，为空时默认搜索所有离职原因，最多支持20个

**示例值**：["offboarding_reason_unique_identifier"]
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "active": true,
    "offboarding_reason_unique_identifier": [
        "offboarding_reason_unique_identifier"
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
	<md-text type="field-name" >items</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >offboarding_reason\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >offboarding_reason_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	离职原因唯一标识，可用于开放平台[操作员工离职](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/submit)、[搜索离职信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/offboarding/search)等接口入参中的离职原因。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	名称
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
	<md-text type="field-name" >active</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否启用，可选项有：

- true
- false
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >parent_offboarding_reason_unique_identifier</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	当前离职原因的父级原因唯一标识
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >created_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	创建时间，格式："YYYY-MM-DD HH-mm-ss"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >updated_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	更新时间，格式："YYYY-MM-DD HH-mm-ss"
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
        "items": [
            {
                "offboarding_reason_unique_identifier": "reason_for_offboarding_option8",
                "name": [
                    {
                        "lang": "zh-CN",
                        "value": "张三"
                    }
                ],
                "active": true,
                "parent_offboarding_reason_unique_identifier": "offboarding_reason_1",
                "created_time": "2021-08-20 20:28:23",
                "updated_time": "2022-01-07 17:21:06"
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
  <md-td>500</md-td>
  <md-td>1160103</md-td>
  <md-td>general internal server error code</md-td>
  <md-td>调用上下游系统错误，重试后仍报错，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
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
  <md-td>离职原因说明长度超过最大限制(6000)</md-td>
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
  <md-td>调用上下游系统错误，重试后仍报错，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




