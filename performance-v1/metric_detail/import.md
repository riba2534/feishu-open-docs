---
title: "录入被评估人关键指标数据"
fullPath: "/uAjLw4CM/ukTMukTMukTM/performance-v2/metric_detail/import"
updateTime: "1750859223000"
---

# 录入被评估人关键指标数据

批量录入指定周期中被评估人的关键指标数据。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=performance&version=v2&resource=metric_detail&method=import)

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
      <md-td>https://open.feishu.cn/open-apis/performance/v2/metric_details/import</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[10 次/分钟](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="performance:metric:write" desc="管理关键指标数据" support_app_types="custom,isv" tags="">管理关键指标数据</md-perm>
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
	是
	</md-dt-td>
	<md-dt-td>
	根据 client_token 是否一致来判断是否为同一请求

**示例值**：12454646

**数据校验规则**：

- 长度范围：`0` ～ `64` 字符
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

**示例值**：open_id

**可选值有**：
<md-enum>
<md-enum-item key="open_id" >标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)</md-enum-item>
<md-enum-item key="union_id" >标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)</md-enum-item>
<md-enum-item key="user_id" >标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)</md-enum-item>
<md-enum-item key="people_admin_id" >以people_admin_id来识别用户</md-enum-item>
</md-enum>

**默认值**：`open_id`

**数据校验规则**：

- 长度范围：`0` ～ `999999999` 字符

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
	<md-text type="field-name" >semester_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	周期 ID，可通过[获取周期](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list)接口获取

**示例值**："7293040702907514899"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >import_record_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	数据源录入人，在录入记录页面可以查看该记录名称。

**示例值**："API录入"

**默认值**：`API录入`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >imported_metrics</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >imported_metric\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	指标明细列表

**数据校验规则**：

- 长度范围：`1` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >reviewee_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	被评估人 ID，与入参 `user_id_type` 类型一致

**示例值**："ou_3245842393d09e9428ad4655da6e30b3"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >metric_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	指标 ID，可通过[获取指标列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/metric_lib/query)接口获取

**示例值**："7272580325522276372"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >imported_metric_field\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	指标字段信息

**数据校验规则**：

- 长度范围：`1` ～ `99`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	指标字段 ID，可通过[获取指标字段列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/metric_field/query)接口获取

**示例值**："7283776005142675476"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	字段值

**示例值**："100"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >field_value_person</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	字段值，当字段为人员信息时必填，与入参 `user_id_type` 类型一致

**示例值**："ou_3245842393d09e9428ad4655da6e30b3"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "semester_id": "7293040702907514899",
    "import_record_name": "API录入",
    "imported_metrics": [
        {
            "reviewee_user_id": "ou_3245842393d09e9428ad4655da6e30b3",
            "metric_id": "7272580325522276372",
            "fields": [
                {
                    "field_id": "7283776005142675476",
                    "field_value": "100",
                    "field_value_person": "ou_3245842393d09e9428ad4655da6e30b3"
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
	<md-text type="field-name" >import_record_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	导入记录 ID
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
        "import_record_id": "7241404194141224979"
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
  <md-td>1580101</md-td>
  <md-td>internal error</md-td>
  <md-td>请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580102</md-td>
  <md-td>param is invalid</md-td>
  <md-td>检查参数是否正确，例如类型，大小</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580105</md-td>
  <md-td>invalid semester ID</md-td>
  <md-td>周期 ID 不存在，请检查 `semester_id` 入参是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580110</md-td>
  <md-td>request ID repeat</md-td>
  <md-td>client_token 重复，请检查 `client_token` 入参是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580112</md-td>
  <md-td>permission denied</md-td>
  <md-td>操作无权限的被评估人数据，请检查当前应用申请的被评估人数据范围</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580301</md-td>
  <md-td>field value type is invalid</md-td>
  <md-td>字段值类型不合法</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580302</md-td>
  <md-td>field_value is null</md-td>
  <md-td>必填字段的字段值不能为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580303</md-td>
  <md-td>field value length exceeds the limit</md-td>
  <md-td>字段值内容长度超出限制，检查字段值长度</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580304</md-td>
  <md-td>sum of weights for metrics exceeds 100%</md-td>
  <md-td>指标的权重之和超出 100% 限制</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580305</md-td>
  <md-td>filed id not found in the metric</md-td>
  <md-td>请求的指标字段 ID 不存在于对应指标中</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580306</md-td>
  <md-td>reviewee not found</md-td>
  <md-td>请求的用户未参与评估或者所在项目未启动</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580307</md-td>
  <md-td>duplicate metric for the same reviewee in request</md-td>
  <md-td>检查传入的内容中是否有重复，同一个被评估人不允许传入重复的指标</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580308</md-td>
  <md-td>duplicate field for the same metric in request</md-td>
  <md-td>检查传入的内容中是否有重复，被评估人的指标的一个字段只允许传入唯一的字段值</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580309</md-td>
  <md-td>input is not allowed after the deadline</md-td>
  <md-td>已经超过了录入截止时间</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580310</md-td>
  <md-td>old vision metrics can't be input</md-td>
  <md-td>不支持录入老版本的关键指标数据</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580311</md-td>
  <md-td>data input by admins can't be overwritten</md-td>
  <md-td>不支持录入管理员已填写的字段值</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580312</md-td>
  <md-td>reviewee's metrics not found</md-td>
  <md-td>检查用户录入的指标ID是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580901</md-td>
  <md-td>tenant no licnese</md-td>
  <md-td>租户无绩效席位，请联系租户管理员开通绩效席位</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::

更多错误码信息，参见[通用错误码](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)。


