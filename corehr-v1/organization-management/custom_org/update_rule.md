---
title: "更新自定义组织的匹配规则"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/custom_org/update_rule"
updateTime: "1747710056000"
---

# 更新自定义组织的匹配规则

更新自定义组织的匹配规则。仅开启了「为组织设置自动匹配规则」的自定义组织类型可用。如需更新自定义组织基本信息可使用[更新自定义组织](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/custom_org/patch)
{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=custom_org&method=update_rule)

:::html
<md-alert type="tip">
- 自定义组织规则无生效时间概念，规则变更不会生成相应版本。
- 自定义组织规则变更后不会自动生效，需要在「飞书人事-组织管理-对应自定义组织」页面右上角点击「立即计算匹配规则」按钮才会生效。或者每天 0 点自动生效。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/custom_orgs/update_rule</md-td>
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
            <md-perm name="corehr:custom_org:write" desc="读写自定义组织信息" support_app_types="custom,isv" tags="">读写自定义组织信息</md-perm>
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
	<md-text type="field-name" >object_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	组织类型编码，可在「飞书人事-设置-组织设置」中相应的自定义组织目录下查看

**示例值**："custom_org_01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >org_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	自定义组织 ID
- 可从 [批量查询自定义组织](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/custom_org/query)的 org_id 字段中获取。

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >match_rule_groups</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >match_rules\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自动匹配的规则组。
- 需要在「飞书人事-设置-组织设置」中打开对应组织类型的自动匹配开关后，才可以使用匹配规则组字段。
- 各个==match_rule_groups==之间是并集关系
- 各个==match_rules==之间是交集关系

**数据校验规则**：

- 长度范围：`0` ～ `16`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >match_rules</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >match_rule\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	匹配规则列表，组内是交集关系

**数据校验规则**：

- 长度范围：`0` ～ `64`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >left_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	左值

**示例值**："department"

**可选值有**：
<md-enum>
<md-enum-item key="department" >部门</md-enum-item>
<md-enum-item key="department_hierarchy" >部门（含下级）</md-enum-item>
<md-enum-item key="work_location" >工作地点</md-enum-item>
<md-enum-item key="work_location_hierarchy" >工作地点（含下级）</md-enum-item>
<md-enum-item key="cost_center" >成本中心</md-enum-item>
<md-enum-item key="cost_center_hierarchy" >成本中心（含下级）</md-enum-item>
<md-enum-item key="job" >职务</md-enum-item>
<md-enum-item key="job_level" >职级</md-enum-item>
<md-enum-item key="job_family" >序列</md-enum-item>
<md-enum-item key="job_family_hierarchy" >序列（含下级）</md-enum-item>
<md-enum-item key="employee_type" >人员类型</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >operator</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	操作符

**示例值**："contains"

**可选值有**：
<md-enum>
<md-enum-item key="contains" >包含</md-enum-item>
<md-enum-item key="notContains" >不包含</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >right_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	右值，填写左值对应的 ID 列表。
- ==department==和==department_hierarchy==：详细 ID 可通过[查询单个部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)接口获得，ID 类型需要为 ==people_corehr_department_id==。
- ==work_location==和==work_location_hierarchy==：详细 ID 可通过[查询单个地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/get)接口获得。
- ==cost_center==和==cost_center_hierarchy==：详细 ID 可通过[搜索成本中心信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获得。
- ==job==：详细 ID 可通过[查询单个职务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get)接口获得。
- ==job_level==：详细 ID 可通过[查询单个职级](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)接口获得。
- ==job_family==和==job_family_hierarchy==：详细 ID 可通过[查询单个序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)接口获得。
- ==employee_type==：详细 ID 可通过[查询人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)接口获得。

**示例值**：["6862995757234914824"]

**数据校验规则**：

- 长度范围：`0` ～ `10000`
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "object_api_name": "custom_org_01",
    "org_id": "6862995757234914824",
    "match_rule_groups": [
        {
            "match_rules": [
                {
                    "left_value": "department",
                    "operator": "contains",
                    "right_values": [
                        "6862995757234914824"
                    ]
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
  <md-td>联系飞书人事 [Oncall](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>429</md-td>
  <md-td>1161604</md-td>
  <md-td>QPS over limit</md-td>
  <md-td>联系飞书人事 [Oncall](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




