---
title: "批量查询外部算薪数据记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/payroll-v1/datasource_record/query"
updateTime: "1747821608000"
---

# 批量查询外部算薪数据记录

1. 支持通过payroll_period（必传）、employment_id（可选）这两个预置字段，批量查询指定数据源下的数据记录列表。
2. 数据源配置信息可从[获取外部数据源配置信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/datasource/list)或者 「飞书人事后台-设置-算薪数据设置-外部数据源配置」页面 获取{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=payroll&version=v1&resource=datasource_record&method=query)

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
      <md-td>https://open.feishu.cn/open-apis/payroll/v1/datasource_records/query</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[10 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="payroll:external_datasource_record:read" desc="Payroll外部数据记录查询权限" support_app_types="custom,isv" tags="">Payroll外部数据记录查询权限</md-perm>
            <md-alert type="tip" icon="none">
              本接口支持行数据鉴权，请确保应用拥有写入员工所在薪资组的数据授权。（如果是用户身份访问，请在飞书人事后台-角色配置中赋予「外部数据源 - 数据明细」的权限）
            </md-alert>
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
	<md-text type="field-name" >page_size</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	

**示例值**：10

**数据校验规则**：

- 取值范围：`1` ～ `100`
	</md-dt-td>
</md-dt-tr>


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

**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=
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
	<md-text type="field-name" >source_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	数据源code

**示例值**："test__c"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >selected_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	指定查询的数据源字段code。
1. 如不传入此字段，默认返回所有数据源字段
2. 如果传入，除了返回指定字段外，系统会默认返回emplyment_id、payroll_period字段的值。

**示例值**：["test__c"]

**数据校验规则**：

- 长度范围：`1` ～ `200`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >field_filters</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >datasource_record_field_filter\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	查询条件列表，多个条件之间为And关系，支持的查询条件如下：
1. employment_id
- 非必传，最多传入100个，field_type=3（文本类型）。
- 该id为飞书人事中员工的基本信息id，可通过[搜索员工信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)获取.
- 查询操作符只支持IsAnyOf（包含）
2. 时间范围条件必传，根据数据源的不同数据写入维度，支持的时间范围查询条件如下：
- 算薪期间维度。payroll_period字段，格式：2024-01，
    查询方式：IsAnyOf操作符枚举需要查的月份，最多可查2个月。
- 数据发生日期维度（灰度中）。occur_day字段，格式2024-01-02，
    查询方式：通过InDateRange操作符查询（日期范围查询），occur_day的时间范围不允许超过90天，
- 自定义数据周期维度（灰度中）。custom_start、custom_end字段，格式：2024-01-02。查询方式：两者都必传，通过InDateRange操作符查询（日期范围查询），时间范围不允许超过90天。

**数据校验规则**：

- 最大长度：`100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >field_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	字段编码

**示例值**："employment_id"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >field_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	包含的字段值列表。

**示例值**：["123"]

**数据校验规则**：

- 长度范围：`1` ～ `500`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >operator</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	查询操作符，不传默认为IsAnyOf 包含查询。

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="1" >IsAnyOf 包含查询，被查询记录的字段值被field_values列表包含即可。</md-enum-item>
<md-enum-item key="2" >InDateRange 日期范围查询。field_values长度必须为2，类似[startDate,endDate]，前后都是闭区间；其中日期格式为“2024-01-02”，仅occur_day、custom_start、custom_end字段支持此查询方式，且时间范围不超过90天。</md-enum-item>
</md-enum>

**数据校验规则**：

- 取值范围：`1` ～ `2`
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "source_code": "yache19_8680__c",
    "selected_fields": [
        "yache41_8680__c"  // 需查的字段
    ],
    "field_filters": [
        {
            "field_code": "employment_id", // 可选查询条件
            "field_values": [
                "6993242233201853965",
                "7163264720525592101"
            ]
        },
        {
            "field_code": "payroll_period", // 算薪期间，必要的查询条件
            "field_values": [
                "2024-10"
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


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >records</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >datasource_record\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	数据记录列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >active_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	记录的启停用状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >已启用</md-enum-item>
<md-enum-item key="2" >已停用</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >datasource_record_field\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	记录的字段值列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >field_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	数据源字段编码
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
	字段值 通过string传输，值为API写入的值。 
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >field_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	字段类型。可从「查询外部数据源设置」API 或者 「飞书人事后台-设置-算薪数据设置-外部数据源配置」页面 获取。
1. 金额
2. 数值
3. 文本
4. 日期
5. 百分比
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
        "page_token": "7413047003142619148",
        "has_more": true,
        "records": [
            {
                "active_status": 1,
                "field_values": [
                    {
                        "field_code": "yache41_8680__c",
                        "value": "2024-12-01",
                        "field_type": 1
                    }
                ]
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
  <md-td>2500001</md-td>
  <md-td>unknown error</md-td>
  <md-td>未知错误，联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2500002</md-td>
  <md-td>param invalid</md-td>
  <md-td>参数异常，请检查入参</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500004</md-td>
  <md-td>datasource_code:{field_code} not exist</md-td>
  <md-td>数据源编码不存在，请检查编码是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500005</md-td>
  <md-td>field_code:{field_code} not exist</md-td>
  <md-td>字段编码不存在，请检查编码是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500006</md-td>
  <md-td>lack required field_filter : {field_code}</md-td>
  <md-td>缺少必传的查询条件</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500007</md-td>
  <md-td>field_filter: {field code} values size is not valid</md-td>
  <md-td>查询条件传入的值过多</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500019</md-td>
  <md-td>{field_code} format not valid</md-td>
  <md-td>字段传入的值的格式不正确，请按照字段类型传入正确格式的值</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500010</md-td>
  <md-td>filter field_code:{field_code} duplicated</md-td>
  <md-td>字段重复</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




