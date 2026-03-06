---
title: "启用/停用公司"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/active"
updateTime: "1730174761000"
---

# 启用/停用公司

对公司进行启用或停用操作{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=company&method=active)

:::html
<md-alert type="tip">
停用公司时请确认有无在职员工、异动单据、待入职单据关联此公司，如有会导致停用失败。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/companies/active</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
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
            <md-perm name="corehr:company:write" desc="查看、创建、更新、删除公司信息" support_app_types="custom,isv" tags="">查看、创建、更新、删除公司信息</md-perm>
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
	<md-text type="field-name" >company_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	公司 ID
- 可从 [批量查询公司](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/company/list)的 id 字段中获取。

**示例值**："1616161616"
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
	公司启用/停用生效时间
- 填写格式： YYYY-MM-DD
- 系统默认为填写日期当天的 00:00:00 生效 
- 该接口只支持到最小单位为日
- 日期范围要求:1900-01-01 ～ 9999-12-31

**示例值**："2020-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >active</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	启用/停用状态。
- active 传 true 代表启用
- active 传 false 代表停用

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >operation_reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	操作原因

**示例值**："业务操作"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "company_id": "1616161616",
    "effective_time": "2020-01-01",
    "active": true,
    "operation_reason": "业务操作"
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


  </md-dt-tbody>
</md-dt-table>
:::



### 响应体示例
:::html
<md-code-json>
{
    "code": 0,
    "msg": "success",
    "data": {}
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
  <md-td>1160402</md-td>
  <md-td>param is invalid</md-td>
  <md-td>检查传参是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160267</md-td>
  <md-td>Activation date cannot be earlier than the effeective date of the last deactivated version</md-td>
  <md-td>启用日期不能早于最新的停用日期</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160268</md-td>
  <md-td>Effective date for disabling can't be earlier than theeffective date of the last version</md-td>
  <md-td>停用日期不能早于最新的启用日期</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160350</md-td>
  <md-td>Failed to enable. Its parent has been deactivated on</md-td>
  <md-td>启用失败，上级公司已停用</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160501</md-td>
  <md-td>Failed to disable this as it still has sub after the deactivation effective time</md-td>
  <md-td>停用日期下仍有启用的下级</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160072</md-td>
  <md-td>Unable to deactivate, because there are still active contracts or employees or pre-hires in it since effective time</md-td>
  <md-td>停用失败，停用日期仍有关联此公司的合同记录、在职员工和待入职员工</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160281</md-td>
  <md-td>Failed to disable as 1 or more members of it are in a job status change process after the current deactcivation date</md-td>
  <md-td>停用失败，停用日期仍有关联此公司的异动记录</md-td>
</md-tr>


<md-tr>
  <md-td>503</md-td>
  <md-td>1161204</md-td>
  <md-td>Requset timeout</md-td>
  <md-td>请求超时，请稍后重试。必要时请联系飞书人事 [Oncall](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>429</md-td>
  <md-td>1161604</md-td>
  <md-td>QPS over limit</md-td>
  <md-td>请求频率过高，请稍后重试。必要时请联系飞书人事 [Oncall](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




