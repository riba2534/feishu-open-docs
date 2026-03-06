---
title: "创建 / 更新外部算薪数据"
fullPath: "/uAjLw4CM/ukTMukTMukTM/payroll-v1/datasource_record/save"
updateTime: "1747821596000"
---

# 创建 / 更新外部算薪数据

参照数据源配置字段格式，批量保存（创建或更新）数据记录。
1. 记录的唯一标志通过业务主键判断（employment_id + payroll_period）
2. 若不存在数据记录，则本次保存会插入1条记录。
3. 若已存在数据记录，则本次保存会覆盖更新已有记录（只更新传入字段的值，未传入字段值不更新），如果传入的数据记录没有任何变化，则不更新。
4. 若更新或者插入成功，会返回产生数据变更的记录条数。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=payroll&version=v1&resource=datasource_record&method=save)

:::html
<md-alert type="tip">


</md-alert>
:::

:::html
<md-alert type="warn">
1. 除了接口自身的限流外，还会限制单个数据源只能串行批量写入（防止批量更新同一批数据导致底层性能或者死锁风险），需调用端做好并发控制
2. 本接口如果发生报错，调用方可认为全部保存失败，不会存在部分保存失败部分成功场景。
3. 请确保写入的数据记录的数据源及字段都是被启用的。
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
      <md-td>https://open.feishu.cn/open-apis/payroll/v1/datasource_records/save</md-td>
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
            <md-perm name="payroll:external_datasource_record:write" desc="Payroll外部数据记录写入权限" support_app_types="custom,isv" tags="">Payroll外部数据记录写入权限</md-perm>
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
	数据源code。可从[获取外部数据源配置信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/payroll-v1/datasource/list)
或者 「飞书人事后台-设置-算薪数据设置-外部数据源配置」页面 获取

**示例值**："test__c"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >records</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >datasource_record\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	需保存的记录列表

**数据校验规则**：

- 长度范围：`1` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >active_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	记录的启停用状态。说明：数据记录被停用后，依旧可以被API保存、查询，但无法被算薪使用。

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="1" >已启用</md-enum-item>
<md-enum-item key="2" >已停用</md-enum-item>
</md-enum>

**数据校验规则**：

- 取值范围：`1` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >field_values</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >datasource_record_field\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	需创建或者更新记录的具体字段值列表：
- 必传字段：
 根据记录的数据源的数据写入维度属性，有不同的必传字段：
1. 算薪期间维度。“payroll_period”、“employment_id”字段必传，payroll_period格式：“2024-01”。
2. 数据发生日期维度（灰度中）。“occur_day”、“employment_id”字段必传。occur_day格式：“2024-01-02”。
3. 自定义数据周期维度（灰度中）。“custom_start”、“custom_end”、“employment_id”字段必传。custom_start、custom_end格式：“2024-01-02”。

employment_id为飞书人事中员工的基本信息id，可通过[搜索员工信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/employee/search)获取
- 其他自定字段按照诉求可选传入，需保证写入的字段在配置中存在且启用。字段code不得重复传入，且字段的值需符合类型对应的约束。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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
	数据源字段编码，请确保字段存在且是启用的。可从「查询外部数据源设置」API 或者 「飞书人事后台-设置-算薪数据设置-外部数据源配置」页面 获取

**示例值**："test__c"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
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
	字段值 通过string传输，不允许输入空字符串，请确保字段的值符合类型的约束。  

**示例值**："123"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	1. 不需要传入此字段，这里只做文档说明用。
2. 字段类型可从「查询外部数据源设置」的返回值中的datasources.fields. field_type中获取
3. value的传值的格式需符合类型的约束：
- field_type=1：金额。eg: "12.23"。目前仅支持人民币¥元，超过设置的精度会被四舍五入；
- field_type=2：数值。eg: "12.23"。超过设置的精度会被四舍五入。
- field_type=3：文本。 eg: "我是一段文本"。文本字符个数不允许超过500，一条记录的文本总的字符个数不允许超过3000.
- field_type=4：日期。除系统预置的payroll_period字段外的所有自定义字段，日期格式均为“yyyy-mm-dd”，示例：“2024-01-01”。但payroll_period代表算薪期间，精确到月，格式“yyyy-mm”，示例：“2024-01”。
- field_type=5：百分比。百分比 "10" 代表10%，最多保留两位小数，超过后四舍五入

**示例值**：1

**数据校验规则**：

- 取值范围：`1` ～ `100`
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
    "records": [
        {
            "active_status": 1, // 启停状态
            "field_values": [
                {
                    "field_code": "employment_id", // 必传字段，员工ID
                    "value": "6993242233201853965" // 员工ID获取方式见文档
                },
                {
                    "field_code": "payroll_period", // 必传字段，算薪期间
                    "value": "2024-10" // 算薪期间，精确到月
                },
                {
                    "field_code": "yache41_8680__c", // 自定义字段1
                    "value": "2024-10-01"
                },
                {
                    "field_code": "yache11_8680__c", // 自定义字段2
                    "value": "我是一段文本"
                },
                {
                    "field_code": "yache22_8680__c", // 自定义字段3
                    "value": "123"
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


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >affect_counts</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	变更的记录条数，变更包含新建或者更新记录两种操作。（该字段为数字类型）
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
        "affect_counts": "120"
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
  <md-td>系统未知异常，可联系[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
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
  <md-td>2500008</md-td>
  <md-td>datasource_code:{field_code} not active</md-td>
  <md-td>数据源未启用，请在设置中检查启停用状态</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500009</md-td>
  <md-td>field_code:{field_code} not active</md-td>
  <md-td>字段未启用，请在设置中检查启停用状态</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500010</md-td>
  <md-td>{field_code} format not valid</md-td>
  <md-td>字段传入的值的格式不正确，请按照字段类型传入正确格式的值</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500011</md-td>
  <md-td>{field_code} text length more than 500</md-td>
  <md-td>字段传入的文本长度超过500，请缩短后再传入</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500012</md-td>
  <md-td>record{records_index} text total length more than 3000</md-td>
  <md-td>第x条记录（x指数组下标），的文本总长超过3000，请缩短后再传入</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500013</md-td>
  <md-td>records{records_index} lack required field: {field_codes}</md-td>
  <md-td>第x条记录（x指数组下标）缺少必传的字段，请检查emploment_id、payroll_period是否都传了。</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500014</md-td>
  <md-td>records{records_index} lark data auth</md-td>
  <md-td>应用没有第x条记录（x指数组下标）的数据权限，请检查权限配置</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500015</md-td>
  <md-td>records{records_index} data entity {ID} not exists</md-td>
  <md-td>第x条记录（x指数组下标）的实体ID不存在，请检查传入的employment_id是否存在</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500016</md-td>
  <md-td>the  payroll period cannot be earlier than 1970-01</md-td>
  <md-td>传入的  payroll period 不能早于1970-01</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500017</md-td>
  <md-td>records{records_index} duplicated</md-td>
  <md-td>传入的数据记录重复</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500018</md-td>
  <md-td>record field_code:{field_codes} duplicated</md-td>
  <md-td>字段重复</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500020</md-td>
  <md-td>data capacity limit exceeded</md-td>
  <md-td>写入过多的数据，超过容量限制，请联系对应实施</md-td>
</md-tr>


<md-tr>
  <md-td>200</md-td>
  <md-td>2500021</md-td>
  <md-td>The data source is writing data, acquiring lock failed</md-td>
  <md-td>当前数据源正在写数据，每个数据源只允许串行写入数据，请做好并发控制，不要1个数据源并发保存数据</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




