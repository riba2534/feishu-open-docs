---
title: "查询编制规划明细信息（支持自定义组织）"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/workforce_plan_detail/batch_v2"
updateTime: "1748953010000"
---

# 查询编制规划明细信息（支持自定义组织）

查询编制规划明细，包括维度信息、编制数、预估在职人数、在职人数和预增/预减人数。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=workforce_plan_detail&method=batch_v2)

:::html
<md-alert type="tip">
- 本接口可查询编制规划或集中填报明细信息。
- 请求体入参如果没有特殊说明，不填写默认为空，不参与筛选。
- 所有筛选项可一起使用，之间为 AND 关系。如部门 + 人员类型，则返回同时满足部门及人员类型的编制规划明细数据。
- 本接口支持自定义组织（自定义组织功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)）。
</md-alert>
:::

:::html
<md-alert type="warn">
延迟说明：搜索同步延迟 10s 以内，即：直接创建编制明细后 10s 内调用此接口可能查询不到数据。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/workforce_plan_details/batch_v2</md-td>
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
      <md-app-support types="custom"></md-app-support>
      </md-td>
    </md-tr>
    <md-tr>
      <md-th>
            权限要求
            <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
            
      </md-th>
      <md-td>
            <md-perm name="corehr:workforce_detail:read" desc="查看编制规划明细信息" support_app_types="custom" tags="">查看编制规划明细信息</md-perm>
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

**示例值**：["123456"]
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
	否
	</md-dt-td>
	<md-dt-td>
	分页大小

**示例值**：100

**默认值**：`100`

**数据校验规则**：

- 取值范围：`1` ～ `100`
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
	<md-text type="field-name" >workforce_plan_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	编制规划方案ID，ID及详细信息可通过[获取编制规划方案列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/workforce_plan/list)接口查询获得。查询编制规划明细信息时，编制规划方案ID必填，是否为集中填报项目设置为false，不填写集中填报项目ID（是否填写不影响返回结果）

**示例值**："781234834512"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >is_centralized_reporting_project</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否为集中填报项目。如果租户未使用集中填报功能，将此参数置空即可。如果查询集中填报明细，将此参数设置为true。

**字段权限要求**：获取编制规划集中填报明细信息(corehr:workforce_plan_centralized_reporting_project_detail:read)

**示例值**：false

**默认值**：`false`
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
	否
	</md-dt-td>
	<md-dt-td>
	编制规划集中填报项目ID，ID可通过访问集中填报页面，从URL中提取report_id参数。如果租户未使用集中填报功能，将此参数置空即可。查询集中填报信息时，集中填报项目ID必填，是否为集中填报项目设置为true，不填写编制规划方案ID（是否填写不影响返回结果）

**字段权限要求**：获取编制规划集中填报明细信息(corehr:workforce_plan_centralized_reporting_project_detail:read)

**示例值**："7140964208476371111"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >dimension_id_in_datas</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dimension_id_in_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	维度筛选

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >dimension_key</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
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


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >dimension_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
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
- position_id：岗位，功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_01_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_02_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_03_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_04_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_05_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)

**示例值**：["7210266650427033132"]

**数据校验规则**：

- 长度范围：`0` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >include_missing_dimension_rows</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否包含缺维度的明细行数据，true为包含缺维度明细行数据，false为仅获取所有维度都有值的明细行数据，默认为 false

**示例值**：false
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >filter_all_zero_value_rows</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否过滤在职、预增/预减人员、编制数、预估在职人数都为0的明细行，true为过滤在职、预增/预减人员、编制数、预估在职人数都为0的明细行，false为不过滤在职、预增/预减人员、编制数、预估在职人数都为0的明细行，默认为 false

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
    "workforce_plan_id": "781234834512",
    "is_centralized_reporting_project": false,
    "centralized_reporting_project_id": "7140964208476371111",
    "dimension_id_in_datas": [
        {
            "dimension_key": "department",
            "dimension_ids": [
                "7210266650427033132"
            ]
        }
    ],
    "include_missing_dimension_rows": false,
    "filter_all_zero_value_rows": false
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
	<md-text type="field-name" >workforce_plan_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	编制规划方案 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >centralized_reporting_project_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	集中填报项目 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >items</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >workforce_plan_detail_v2\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	编制规划明细信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >workforce_plan_detail_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	编制规划明细 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >dimension_info_datas</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dimension_info_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	维度信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >dimension_key</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	维度 key
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
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >dimension_info</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >dimension_info</md-text>
	</md-dt-td>
	<md-dt-td>
	维度信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	维度id
- department_id：可从[查询部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get)获得。
- location_id：可从[查询地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/list)获得。
- cost_center_id：可从[查询成本中心](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)获得。
- job_id：可从[查询职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/list)获得。
- job_level_id：可从[查询职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/list)获得。
- job_family_id：可从[查询序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/list)获得。
- employee_type_id：可从[查询人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/list)获得。
- position_id：岗位，功能灰度中，如有需求请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_01_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_02_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_03_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_04_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
- custom_org_05_id：自定义组织，功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	维度名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	语言编码（IETF BCP 47）
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
	文本内容
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
	编制规划值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >active_individuals</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	在职人数
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
	预增员数量
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
	预减员数量
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >estimated_active_individuals_details</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >workforce_plan_eai_detail\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	预估在职人数明细
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	预估月份
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >estimated_active_individuals</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	预估在职人数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >multi_period_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >workforce_plan_multi_period_value\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	自然周期的编制规划信息。功能灰度中，有需要请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >period_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自然周期的最后一天
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >workforce_plan</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	对应自然周期的编制规划值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >individuals_to_be_added</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	对应自然周期的预增员数量
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >individuals_to_be_removed</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	对应自然周期的预减员数量
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_missing_dimension</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否为缺维度的明细行，true为缺维度明细行，false为非缺维度明细行
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_all_zero_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否在职、预增/预减人员、编制数、预估在职人数都为0的明细行，true代表在职、预增/预减人员、编制数、预估在职人数都为0的明细行，false代表在职、预增/预减人员、编制数、预估在职人数不全为0的明细行
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


  </md-dt-tbody>
</md-dt-table>
:::



### 响应体示例
:::html
<md-code-json>
{"code":0,
"msg":"success",
"data":{"workforce_plan_id":"7128319234123",
"centralized_reporting_project_id":"7128319234123",
"items":[{"workforce_plan_detail_id":""123456"",
"dimension_info_datas":[{"dimension_key":""department"",
"dimension_info":{"id":"“123456”",
"name":[{
    "lang": "zh-CN",
    "value": "中文示例"
}]}}],
"workforce_plan":"10.00",
"active_individuals":"10.00",
"individuals_to_be_added":"10.00",
"individuals_to_be_removed":"10.00",
"estimated_active_individuals_details":[{
    "date": "“2020-10-31”",
    "estimated_active_individuals": "“10.00”"
}],
"multi_period_values":[{
    "period_date": "2022-10-31",
    "workforce_plan": "12.00",
    "individuals_to_be_added": "10.00",
    "individuals_to_be_removed": "10.00"
}],
"is_missing_dimension":false,
"is_all_zero_value":false}],
"page_token":"34523459",
"has_more":true}}
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
  <md-td>503</md-td>
  <md-td>1161204</md-td>
  <md-td>Requset timeout</md-td>
  <md-td>请求超时，请稍后重试。如无法解决可[飞书开放平台技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>429</md-td>
  <md-td>1161604</md-td>
  <md-td>QPS over limit</md-td>
  <md-td>请求量过大，请稍后访问。如无法解决可联系 [飞书开放平台技术支持](https://applink.feishu.cn/TLJpeNdW) 。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160109</md-td>
  <md-td>param is invalid</md-td>
  <md-td>请检查是否传入了无效参数。如无法解决可联系[飞书开放平台技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161009</md-td>
  <md-td>programme not found</md-td>
  <md-td>请检查是否传入了无效编制规划方案信息。如无法解决可联系[飞书开放平台技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>403</md-td>
  <md-td>1160100</md-td>
  <md-td>no permission</md-td>
  <md-td>请检查是否申请对应权限。如无法解决可联系[飞书开放平台技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161008</md-td>
  <md-td>lack APP ID</md-td>
  <md-td>系统错误。如无法解决可联系 [飞书开放平台技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




