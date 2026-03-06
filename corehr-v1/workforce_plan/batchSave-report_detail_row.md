---
title: "批量创建/更新填报行"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/report_detail_row/batchSave"
updateTime: "1762844368000"
---

# 批量创建/更新填报行

批量创建/更新填报行后，可在【设置-编制规划设置-编制规划XXX-集中填报-查看数据】进行查看。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=report_detail_row&method=batchSave)

:::html
<md-alert type="tip">

</md-alert>
:::

:::html
<md-alert type="warn">
批量创建/更新填报行说明：同批次操作场景下，禁止创建/更新重复行，与此同时，创建时若填报行已存在于系统中，则会在底层自动触发更新机制；建议不要录入编制规划值和预估在职人数均为零值的填报行，系统会对全0填报行进行过滤，从而在页面上不显示该行，可能会导致用户误以为填报行不存在。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/report_detail_row/batchSave</md-td>
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
            <md-perm name="corehr:workforce_plan_centralized_reporting_project_detail:write" desc="写入编制规划集中填报明细信息" support_app_types="custom,isv" tags="">写入编制规划集中填报明细信息</md-perm>
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
	<md-text type="field-name" >workforce_plan_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	编制规划id，可在「设置-编制规划设置-编制规划XXX-页面URL」中解析到。

**示例值**："7430330781544564268"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >centralized_reporting_project_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	集中填报id，可在「设置-编制规划设置-编制规划XXX-集中填报XXX-查看数据-页面URL」中解析report_id。

**示例值**："7430470688844023340"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >items</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >workforce_plan_detail_row\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	集中填报的填报行数量应介于 1 至 5 个之间。

**数据校验规则**：

- 长度范围：`1` ～ `5`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >dimensions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dimension_entity\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	集中填报的维度信息要和用户创建的维度匹配，即传入除自动匹配维度外的所有维度，不多不少。

通过「设置-编制规划设置-编制规划XXX」查看该编制规划有哪些维度。

自定义组织暂时不支持【为组织设置自动匹配规则】，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)了解如何判断该字段是否为自动匹配字段。

**数据校验规则**：

- 长度范围：`1` ～ `20`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >dimension_key</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	维度key，可从下面列表中进行选择：
- "department"：部门。
- "employee_type" ：人员类型。
- "location"：地点。
- "position" ：岗位。
- "cost_center" ：成本中心/业务线。
- "job_family" ：序列。
- "job_level" ：职级。
- "job" ：职务。

自定义组织：
- "custom_org_01" 
- "custom_org_02"
- "custom_org_03"
- "custom_org_04" 
- "custom_org_05"

**示例值**："department"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >dimension_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	维度value。
- department_id：可从[查询部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)获得。
- location_id：可从[查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)获得。
- cost_center_id：可从[查询成本中心](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)获得。
- job_id：可从[查询职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)获得。
- job_level_id：可从[查询职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)获得。
- job_family_id：可从[查询序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)获得。
- employee_type_id：可从[查询人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)获得。
- position_id：岗位，功能灰度中，如有需求请联系技术支持
- custom_org_01_id：自定义组织，功能灰度中，有需要请联系技术支持
- custom_org_02_id：自定义组织，功能灰度中，有需要请联系技术支持
- custom_org_03_id：自定义组织，功能灰度中，有需要请联系技术支持
- custom_org_04_id：自定义组织，功能灰度中，有需要请联系技术支持
- custom_org_05_id：自定义组织，功能灰度中，有需要请联系技术支持

**示例值**："7322790168290739756"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >eai_details</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >workforce_plan_eai_detail\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	预估在职人数相关信息。可从「设置-编制规划设置-编制规划XXX-集中填报」查看预估在职人数的时间，如果不存在该字段说明用户创建时即没有允许填写该字段，批量创建/更新填报行时则无需给该字段，如果存在，用户需要查看预估在职人数的日期，使用示例值格式进行传参。

**数据校验规则**：

- 长度范围：`0` ～ `15`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	预估在职人数的日期，和集中填报页面上显示的预估在职人数的日期一致，且格式要依照示例给定，若二者不匹配，则无法完成识别更新。

**示例值**："2020-10-31"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >estimated_active_individuals</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	预估在职人数应与创建编制规划时指定的小数位数相匹配，若不匹配，则无法更新。小数位查看方式：「设置-编制规划-编制规划XXX」查看预估在职人数的小数位数。

**示例值**："10"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >plan_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	编制规划值。需与创建编制规划时指定的小数位数相匹配，若不匹配，则无法更新。小数位查看方式：「设置-编制规划-编制规划XXX」查看编制规划的小数位数。注意当编制规划方案是按自然周期选择时，该值必须为空，需要设置自然周期的编制规划信息multi_period_values。

**示例值**："12"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >multi_period_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >workforce_plan_multi_period_value\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自然周期的编制规划信息。当编制规划方案是按自然周期选择时，设置该字段。

**数据校验规则**：

- 长度范围：`0` ～ `15`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >period_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	周期的最后一天。注意需要在填报选择的周期范围内。

**示例值**："2022-10-31"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >workforce_plan</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	对应自然周期的编制规划值。编制规划值需与创建编制规划时指定的小数位数相匹配，若不匹配，则无法更新。小数位查看方式：「设置-编制规划-编制规划XXX」查看编制规划的小数位数。

**示例值**："12.00"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >individuals_to_be_added</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	对应自然周期预增员数量。批量创建更新时，无需写入此字段。

**示例值**："10.00"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >individuals_to_be_removed</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	对应自然周期预减员数量。批量创建更新时，无需写入此字段。

**示例值**："10.00"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "workforce_plan_id": "7435976673130317356",
    "centralized_reporting_project_id": "7436723164333753900",
    "items": [
        {
            "dimensions": [
                {
                    "dimension_key": "department",
                    "dimension_value": "7371716294248908332"
                },
                {
                    "dimension_key": "location",
                    "dimension_value": "7312702817660487212"
                },
                {
                    "dimension_key": "cost_center",
                    "dimension_value": "7212847939319219756"
                },
                {
                    "dimension_key": "job_family",
                    "dimension_value": "7210959705752192556"
                },
                {
                    "dimension_key": "employee_type",
                    "dimension_value": "7210608964277601836"
                }
            ],
            "plan_value": "919",
            "eai_details": [
                {
                    "date": "2029-01-31",
                    "estimated_active_individuals": "9"
                },
                {
                    "date": "2029-02-28",
                    "estimated_active_individuals": "99"
                }
            ]
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

下面是错误码的简单示例，详细描述可通过下面的链接查看。

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
  <md-td>param is invalid</md-td>
  <md-td>请先参考全量错误码详细描述进行错误排查，如问题始终无法解决请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::

其他错误码参考: [全量错误码详细描述](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/workforce_plan/the-full-set-of-error-codes)


