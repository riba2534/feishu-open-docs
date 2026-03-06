---
title: "启停用岗位"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/active"
updateTime: "1760409246000"
---

# 启用或停用岗位

对岗位进行启用或停用操作{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=position&method=active)

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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/positions/active</md-td>
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
            <md-perm name="corehr:position:write" desc="读写岗位信息" support_app_types="custom,isv" tags="">读写岗位信息</md-perm>
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
	<md-text type="field-name" >position_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	岗位ID，详细信息可通过[查询岗位信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/query)接口获得

**示例值**："6862995757234914823"
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
	可选值：true（启用）、false（停用）

**示例值**：true
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
	生效时间

**示例值**："2020-01-01"

**数据校验规则**：

- 长度范围：`10` ～ `10` 字符
- 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$`
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "position_id": "6862995757234914823",
    "active": true,
    "effective_time": "2020-01-01"
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
  <md-td>1160285</md-td>
  <md-td>Failed to disable as it still has active employees after the deactivation effective time.</md-td>
  <md-td>在停用生效日期后，此岗位仍有在职人员，请检查该岗位在停用生效日期后的在职人员列表，移除或调整相关人员后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160267</md-td>
  <md-td>Activation date cannot be earlier than the effective date of the last deactivated version</md-td>
  <md-td>启用生效日期不可早于最后一个版本生效日期，请检查最后一个版本的生效日期，并确保当前设置的启用生效日期不早于该日期后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160104</md-td>
  <md-td>Record doesn't exist</md-td>
  <md-td>记录不存在，请检查传入的记录ID是否正确或确认记录是否存在</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160281</md-td>
  <md-td>Failed to disable as 1 or more members of it are in a job status change process after the current deactivation date</md-td>
  <md-td>停用失败。在停用生效日期后，此岗位仍有在途的异动，请检查该岗位在停用生效日期后的在途异动列表，处理完毕后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160269</md-td>
  <md-td>Effective date can't be later than the year 9999</md-td>
  <md-td>生效日期不能晚于9999年，请修改生效日期为9999年12月31日或之前</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160353</md-td>
  <md-td>Effective Date cannot earlier than 1900</md-td>
  <md-td>生效日期不能早于1900年，请修改生效日期为1900年1月1日或之后</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160501</md-td>
  <md-td>Failed to disable as it still has sub position(s) after the deactivation effective time.</md-td>
  <md-td>停用失败。在停用生效日期后，此岗位仍有生效的下级岗位，请检查该岗位在停用生效日期后的下级岗位列表，移除或调整相关岗位后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160508</md-td>
  <md-td>Failed to disable. As the position still has pre-hires after the deactivation effective time.</md-td>
  <md-td>停用失败。在停用生效日期后，此岗位仍有人员将入职，请检查该岗位在停用生效日期后的预入职人员列表，处理完毕后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160268</md-td>
  <md-td>Effective date for disabling the position can't be earlier than the effective date of the last version</md-td>
  <md-td>停用生效日期不可早于最后一个版本生效日期，请检查最后一个版本的生效日期并调整停用生效日期</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161200</md-td>
  <md-td>There are still enabled subordinates on the current deactivation date</md-td>
  <md-td>停用失败。在停用生效日期后，此岗位仍有在职员工，请检查该岗位在停用生效日期后的在职员工列表，移除或调整相关员工后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160266</md-td>
  <md-td>Effective date must be later than the first effective date</md-td>
  <md-td>生效日期必须晚于第一个版本的生效日期，请检查第一个版本的生效日期，并调整当前生效日期至其之后重试</md-td>
</md-tr>


<md-tr>
  <md-td>429</md-td>
  <md-td>1161604</md-td>
  <md-td>QPS over limit</md-td>
  <md-td>QPS 超出限制，请降低请求频率重试，必要时请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




