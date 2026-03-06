---
title: "更新岗位信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/patch"
updateTime: "1765434885000"
---

# 更新岗位信息

更新岗位的版本信息，例如岗位关联的职务、职级、序列，以及岗位描述等{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=position&method=patch)

:::html
<md-alert type="tip">
- 非必填字段，不传时即不做变更
- 如果传入生效时间当天不存在版本则会自动生成一个版本。
- 如果传入生效时间当天存在版本则会修改该版本。
</md-alert>
:::

:::html
<md-alert type="warn">
岗位在关联人员、异动、入职对象信息及建立自身上下级关系后，不允许更新部门
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/positions/:position_id</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>PATCH</md-td>
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



### 路径参数
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
	<md-text type="field-name" >position_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	岗位 ID 列表，详细信息可通过[查询岗位信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/query)接口获得

**示例值**："6862995757234914824"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
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
	<md-text type="field-name" >department_id_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	此次调用中使用的部门 ID 类型，三种类型的 ID 都可通过飞书人事的[批量查询部门（ V2）](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/department/batch_get) 来获取

**示例值**：people_corehr_department_id

**可选值有**：
<md-enum>
<md-enum-item key="open_department_id" >以 open_department_id 来标识部门</md-enum-item>
<md-enum-item key="department_id" >以 department_id 来标识部门</md-enum-item>
<md-enum-item key="people_corehr_department_id" >以 people_corehr_department_id 来标识部门</md-enum-item>
</md-enum>

**默认值**：`people_corehr_department_id`
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
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	编码 (不能与其他记录的编码重复)
- 如果开启了岗位自动编码，此字段传入不生效

**示例值**："A01234"
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
	否
	</md-dt-td>
	<md-dt-td>
	名称

**数据校验规则**：

- 长度范围：`0` ～ `2`
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
	名称信息的语言，支持中文和英文。中文用zh-CN；英文用en-US

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
	- 支持 zh-CN 和 en-US，最大长度为 255 字符
- 名称不能包含「/」「；」「;」「\」「'」字符

**示例值**："张三"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >descriptions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	描述

**数据校验规则**：

- 长度范围：`0` ～ `2`
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
	语言

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
	支持 zh-CN 和 en-US，最大长度为 255 字符

**示例值**："张三"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_family_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	序列 ID 列表，详细信息可通过[查询单个序列](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_family/get)接口获得

**示例值**：["4719519211875096301"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >cost_center_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	成本中心 ID，可以通过[搜索成本中心信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)接口获取对应的成本中心信息

**示例值**："4719519211875096301"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	职务，可通过[【查询单个职务】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job/get)获取详细信息

**示例值**："4719519211875096301"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_level_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	职级 ID 列表，可通过[【查询单个职级】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/job_level/get)获取详细信息

**示例值**：["4719519211875096301"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >employee_type_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	人员类型 ID 列表，可通过文档[查询人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)获得详细信息

**示例值**：["4719519211875096301"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_grade_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	职等 ID 列表，可通过 [【查询职等】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_grade/query)获取详细信息

**示例值**：["4719519211875096301"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >work_location_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工作地点 ID 列表，详细信息可通过[查询单个地点](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/location/get)接口获得

**示例值**：["4719519211875096301"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >working_hours_type_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工时制度 ID 列表，可通过[【查询单个工时制度】](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get)查询详细信息

**示例值**："4719519211875096301"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >department_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	部门 ID，详细信息可通过[查询单个部门](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)接口获得
- 类型与 department_id_type 一致

**示例值**："4719519211875096301"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >direct_leader_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	直属上级岗位ID，详细信息可通过[查询岗位信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/query)接口获得

**示例值**："4719519211875096301"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >dotted_line_leader_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	虚线上级岗位ID，详细信息可通过[查询岗位信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/position/query)接口获得

**示例值**："4719519211875096301"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >is_key_position</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否关键岗位

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
	生效日期

**示例值**："2020-05-01"

**数据校验规则**：

- 正则校验：`^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))$`
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
	自定义字段

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
	自定义字段 apiname，即自定义字段的唯一标识

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
	字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同（如 123, 123.23, "true", ["id1","id2"], "2006-01-02 15:04:05"）

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
    "code": "A01234",
    "names": [
        {
            "lang": "zh-CN",
            "value": "张三"
        }
    ],
    "descriptions": [
        {
            "lang": "zh-CN",
            "value": "张三"
        }
    ],
    "job_family_ids": [
        "4719519211875096301"
    ],
    "cost_center_id": "4719519211875096301",
    "job_id": "4719519211875096301",
    "job_level_ids": [
        "4719519211875096301"
    ],
    "employee_type_ids": [
        "4719519211875096301"
    ],
    "job_grade_ids": [
        "4719519211875096301"
    ],
    "work_location_ids": [
        "4719519211875096301"
    ],
    "working_hours_type_id": "4719519211875096301",
    "department_id": "4719519211875096301",
    "direct_leader_id": "4719519211875096301",
    "dotted_line_leader_id": "4719519211875096301",
    "is_key_position": true,
    "effective_time": "2020-05-01",
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
  <md-td>1160263</md-td>
  <md-td>Name or code already exists</md-td>
  <md-td>名称或编码已存在，请检查名称或编码是否与现有记录重复后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160903</md-td>
  <md-td>Name already exists</md-td>
  <md-td>名称已存在，请检查名称是否与现有记录重复后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160259</md-td>
  <md-td>Individual is offboarded on the effecitve date</md-td>
  <md-td>传入的人员类型字段的人员在生效日期当天已离职，请检查人员类型字段的人员在生效日期当天的在职状态后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160572</md-td>
  <md-td>URL is illegal</md-td>
  <md-td>链接类型字段非法，请检查链接格式是否符合要求后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160253</md-td>
  <md-td>\"Name can't include "/" or ";"</md-td>
  <md-td>名称包含禁止的字符（如"/"、";"），请检查名称后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160266</md-td>
  <md-td>Effective date must be later than the first effective date</md-td>
  <md-td>传入的生效日期必须晚于第一个版本的生效日期，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160251</md-td>
  <md-td>Required field(s) is empty</md-td>
  <md-td>必填字段不能为空，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160701</md-td>
  <md-td>The job doesn't exist on the effective date.</md-td>
  <md-td>传入的职务在生效日期当天不存在，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160702</md-td>
  <md-td>The job will be deactivated on or after the effective date.</md-td>
  <md-td>传入的职务在生效日期当天或未来停用，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160703</md-td>
  <md-td>The job family doesn't exist on the effective date.</md-td>
  <md-td>传入的序列在生效日期不存在，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160269</md-td>
  <md-td>Effective date can't be later than the year 9999</md-td>
  <md-td>生效日期不能晚于9999</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160353</md-td>
  <md-td>Effective Date cannot earlier than 1900</md-td>
  <md-td>生效日期不能早于1900</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160704</md-td>
  <md-td>传入的序列在生效日期当天或未来停用，请检查后重试</md-td>
  <md-td>The job family will be deactivated on or after the effective date</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160705</md-td>
  <md-td>The job level doesn't exist</md-td>
  <md-td>传入的职级不存在，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160707</md-td>
  <md-td>The job grade doesn't exist</md-td>
  <md-td>传入的职等不存在，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160709</md-td>
  <md-td>The job and job family doesn't match</md-td>
  <md-td>传入的职务和序列不匹配，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160710</md-td>
  <md-td>The job and job level doesn't match</md-td>
  <md-td>传入的职务和职级不匹配，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160711</md-td>
  <md-td>The job level and job family doesn't match</md-td>
  <md-td>传入的职级和序列不匹配，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160712</md-td>
  <md-td>the job level and job grade doesn't match</md-td>
  <md-td>传入的职级和职等不匹配，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160714</md-td>
  <md-td>The position doesn't exist on the effective date.</md-td>
  <md-td>岗位在传入的生效日期当天未生效，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160104</md-td>
  <md-td>Record doesn't exist</md-td>
  <md-td>岗位记录不存在，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160715</md-td>
  <md-td>The position will be deactivated on or after the effective date</md-td>
  <md-td>岗位在生效日期当天或未来停用，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160515</md-td>
  <md-td>Effective date must be later than the first effective date</md-td>
  <md-td>生效日期必须晚于第一个版本的生效日期，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160255</md-td>
  <md-td>Parent position hasn't taken effect on effective date</md-td>
  <md-td>上级岗位在传入的生效日期当天尚未生效，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160256</md-td>
  <md-td>Parent position will be deactivated on or after this effective date</md-td>
  <md-td>上级岗位在传入的生效日期当天或未来停用，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160264</md-td>
  <md-td>This operation will make the relationship between the superior and the subordinate into a ring</md-td>
  <md-td>更新后，会出现岗位上下级关系成环，请修改上级后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161603</md-td>
  <md-td>Name already exists</md-td>
  <md-td>岗位名称重复，请修改名称后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160271</md-td>
  <md-td>Unable to submit as no changes have been made</md-td>
  <md-td>数据无变更，请检查后重试</md-td>
</md-tr>


<md-tr>
  <md-td>503</md-td>
  <md-td>1161204</md-td>
  <md-td>Requset timeout</md-td>
  <md-td>接口超时，请重试。必要时请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
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




