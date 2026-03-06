---
title: "创建自定义组织"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/custom_org/create"
updateTime: "1765434816000"
---

# 创建自定义组织

使用指定信息创建自定义组织，接口内会做相关规则校验。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=custom_org&method=create)

:::html
<md-alert type="tip">
- 每种自定义组织都可以通过此接口创建，不同种自定义组织通过不同 object_api_name 区分。
- 非必填字段，不传时默认为空。
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/custom_orgs</md-td>
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
	<md-text type="field-name" >client_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	根据client_token是否一致来判断是否为同一请求

**示例值**：1245464678

**数据校验规则**：

- 长度范围：`0` ～ `128` 字符
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

**数据校验规则**：

- 长度范围：`0` ～ `64` 字符

**当值为 `user_id`，字段权限要求**：
<md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
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

**数据校验规则**：

- 长度范围：`1` ～ `128` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >names</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	自定义组织的名称
- 相同上级的自定义组织中英文名称不允许重复。
- 名称不能包含「/」「；」「;」「\」「'」字符。

**数据校验规则**：

- 长度范围：`0` ～ `5`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	名称信息的语言，中文用 zh-CN，英文用 en-US

**示例值**："zh-CN"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	名称信息的内容。

**示例值**："飞书人事"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义组织编码 (不能与其他记录的编码重复)
- 开启自动编码时，如果不传值会自动生成编码，否则以传入值为准
- 未开启自动编码时，不传值不会自动生成编码

**示例值**："000001（格式和配置的匹配规则相关）"

**数据校验规则**：

- 长度范围：`0` ～ `128` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >parent_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	上级自定义组织 ID
- 上级自定义组织的状态必须是启用的。
- 可从 [批量查询自定义组织](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/custom_org/query)的 org_id 字段中获取。

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >manager_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	负责人 ID 列表。
- 详细信息可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search) 或 [【批量查询员工】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get) 接口获取，ID 为返回值中的 ==employment_id==

**示例值**：["6862995757234914824"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义组织描述

**数据校验规则**：

- 长度范围：`0` ～ `5`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >lang</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	语言, 中文用 zh-CN ，英文用 en-US

**示例值**："zh-CN"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	文本内容

**示例值**："中文示例"
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
	自定义组织生效时间
- 填写格式： YYYY-MM-DD
- 系统默认为填写日期当天的 00:00:00 生效 
- 该接口只支持到最小单位为日
- 日期范围要求:1900-01-01 ～ 9999-12-31

**示例值**："2020-01-01"

**数据校验规则**：

- 长度范围：`10` ～ `10` 字符
- 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >org_roles</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >org_role_update\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自动给「按自定义组织授权的角色」授权

**数据校验规则**：

- 长度范围：`0` ～ `64`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	角色key
 - api_name、security_group_id必须填一个
 - 可以通过页面「飞书人事-设置-组织配置」选择对应自定义组织，「字段配置-字段编码」获取

**示例值**："hcm_corehr_xxxxxx"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >security_group_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	角色ID
 - api_name、security_group_id必须填一个
 - 可以通过[批量获取角色列表](https://open.larkoffice.com/document/server-docs/corehr-v1/authorization/list) 获取，数据为返回数据中的 data.items.id 值。筛选条件data.items.group_type == 3（组织角色），data.items.org_truncation 关联的组织有且仅有一个，data.items.org_truncation.org_key 等于当前查询自定义组织 object_api_name

**示例值**："7034393015968122400"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >employment_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	被授权的员工 ID 列表
- 详细信息可通过[【搜索员工信息】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search) 或 [【批量查询员工】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/batch_get) 接口获取

**示例值**：["6862995757234914824"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
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


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >custom_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_field_data\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段类型，详细见[获取自定义字段列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom_field/query) 

**数据校验规则**：

- 长度范围：`0` ～ `200`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >custom_api_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	自定义字段 API Name，即自定义字段的唯一标识

**示例值**："name"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段值，为 JSON 转义后的字符串。

**注意：具体传值方式参见**[获取自定义字段的元数据](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/custom-fields-guide)

**示例值**："\"231\""
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
    "names": [
        {
            "lang": "zh-CN",
            "value": "飞书人事"
        }
    ],
    "code": "000001（格式和配置的匹配规则相关）",
    "parent_id": "6862995757234914824",
    "manager_ids": [
        "6862995757234914824"
    ],
    "description": [
        {
            "lang": "zh-CN",
            "value": "中文示例"
        }
    ],
    "effective_time": "2020-01-01",
    "org_roles": [
        {
            "api_name": "hcm_corehr_xxxxxx",
            "security_group_id": "7034393015968122400",
            "employment_ids": [
                "6862995757234914824"
            ]
        }
    ],
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
    ],
    "custom_fields": [
        {
            "custom_api_name": "name",
            "value": "\"231\""
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


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >org_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义组织的 ID
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
        "org_id": "6862995757234914824"
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
  <md-td>1160263</md-td>
  <md-td>The code already exists</md-td>
  <md-td>检查编码是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160255</md-td>
  <md-td>Parent organization hasn't taken effect on effective date</md-td>
  <md-td>检查上级组织是否生效</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160256</md-td>
  <md-td>Parent organization will be deactivated on or after this effective date</md-td>
  <md-td>检查上级是否即将停用</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160264</md-td>
  <md-td>This operation will make the relationship between the superior and the subordinate into a ring</md-td>
  <md-td>检查检查上下级之间是否成环</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161603</md-td>
  <md-td>Name already exists</md-td>
  <md-td>检查名称是否与相同上级组织下的其他同级组织重名</md-td>
</md-tr>


<md-tr>
  <md-td>503</md-td>
  <md-td>1161204</md-td>
  <md-td>Requset timeout</md-td>
  <md-td>联系飞书人事 Oncall 获取[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>429</md-td>
  <md-td>1161604</md-td>
  <md-td>QPS over limit</md-td>
  <md-td>联系飞书人事 Oncall 获取[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




