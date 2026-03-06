---
title: "批量导入补充信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/performance-v2/additional_information/import"
updateTime: "1751526502000"
---

# 批量导入补充信息

批量导入被评估人的补充信息作为绩效评估的参考，如补充信息的事项、时间以及具体描述等。该接口支持创建和更新补充信息。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=performance&version=v2&resource=additional_information&method=import)

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

## 注意事项
该接口执行创建或者更新的判断逻辑如下（按顺序判断）：

1. 若请求参数 `additional_informations` 中 `item_ids` 传入系统中已有的补充信息 ID 时，将更新对应的补充消息数据。
2. 若请求参数 `additional_informations` 中 `external_ids` 传入系统中已有的外部系统补充信息 ID 时，将更新对应的补充消息数据。
3. 若请求参数 `additional_informations` 中 `reviewee_user_id`、`item `、`time `、`detailed_description` 的参数组合在系统中已存在内容一致的补充消息时，将更新对应的补充消息数据。
4. 以上情况都不符合时，创建新的补充消息数据。


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
      <md-td>https://open.feishu.cn/open-apis/performance/v2/additional_informations/import</md-td>
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
            
            <div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
            
      </md-th>
      <md-td>
            <md-perm name="performance:performance" desc="管理绩效数据" support_app_types="custom,isv" tags="">管理绩效数据</md-perm>
            <md-perm name="performance:semester_activity:write" desc="管理周期与项目配置信息" support_app_types="custom,isv" tags="">管理周期与项目配置信息</md-perm>
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
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom,isv" tags="">获取用户 user ID</md-perm>
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
	根据 `client_token` 是否一致来判断是否为同一请求，同一请求多次调用将被拦截

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
	评估周期 ID，可通过[获取周期列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v1/semester/list)接口获取

**示例值**："7348736302176534547"

**数据校验规则**：

- 长度范围：`1` ～ `100` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >additional_informations</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >additional_information\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	补充信息列表

**数据校验规则**：

- 长度范围：`1` ～ `1000`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >item_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	补充信息 ID
<br>

**注意**：若传入系统中已有的补充信息 ID 时，将更新对应的补充消息数据

**示例值**："7350194523185610771"

**数据校验规则**：

- 长度范围：`1` ～ `100` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >external_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	外部系统补充信息 ID，用于系统间的数据映射。
<br>

**注意**：若传入系统中已有的外部系统补充信息 ID 时，将更新对应的补充消息数据

**示例值**："6789523104723558912"

**数据校验规则**：

- 长度范围：`0` ～ `100` 字符
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
	被评估人 ID 列表，与入参 `user_id_type` 类型一致，可通过[获取被评估人信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/performance-v2/reviewee/query)接口获取
<br>

**注意**：若 `reviewee_user_id`、`item `、`time `、`detailed_description` 的参数组合在系统中已存在内容一致的补充消息时，将更新对应的补充消息数据

**示例值**："ou_3245842393d09e9428ad4655da6e30b3"

**数据校验规则**：

- 长度范围：`1` ～ `9999` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >item</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	事项
<br>

**注意**：若 `reviewee_user_id`、`item `、`time `、`detailed_description` 的参数组合在系统中已存在内容一致的补充消息时，将更新对应的补充消息数据

**示例值**："业绩补充说明"

**数据校验规则**：

- 长度范围：`1` ～ `1000` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	时间
<br>

**说明**：文本内容，无格式校验
<br>

**注意**：若 `reviewee_user_id`、`item `、`time `、`detailed_description` 的参数组合在系统中已存在内容一致的补充消息时，将更新对应的补充消息数据

**示例值**："2024-03-12"

**数据校验规则**：

- 长度范围：`1` ～ `100` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >detailed_description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	具体描述
<br>

**注意**：若 `reviewee_user_id`、`item `、`time `、`detailed_description` 的参数组合在系统中已存在内容一致的补充消息时，将更新对应的补充消息数据

**示例值**："销售额增长目标超额完成"

**数据校验规则**：

- 长度范围：`1` ～ `5000` 字符
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
	补充信息导入记录名称，管理员可在补充信息管理的导入记录中查看。
<br>

**默认值**："API导入"

**示例值**："人工导入"

**数据校验规则**：

- 长度范围：`0` ～ `200` 字符
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "semester_id": "7348736302176534547",
    "additional_informations": [
        {
            "item_id": "7350194523185610771",
            "external_id": "6789523104723558912",
            "reviewee_user_id": "ou_3245842393d09e9428ad4655da6e30b3",
            "item": "业绩补充说明",
            "time": "2024-03-12",
            "detailed_description": "销售额增长目标超额完成"
        }
    ],
    "import_record_name": "人工导入"
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


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >additional_informations</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >additional_information\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	成功导入后的补充信息列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >item_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	补充信息 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >external_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	外部系统补充信息 ID

**说明**：若导入时没有提供，则返回为空
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >reviewee_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	被评估人 ID 列表，与入参 `user_id_type` 类型一致
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >item</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	事项
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	时间
<br>

**说明**：文本内容，无格式校验
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >detailed_description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	具体描述
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
        "import_record_id": "7350194523185610771",
        "additional_informations": [
            {
                "item_id": "7350195758357807123",
                "external_id": "6789523104723558912",
                "reviewee_user_id": "ou_3245842393d09e9428ad4655da6e30b3",
                "item": "业绩补充说明",
                "time": "2024-03-12",
                "detailed_description": "销售额增长目标超额完成"
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
  <md-td>1580101</md-td>
  <md-td>internal error</md-td>
  <md-td>请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580105</md-td>
  <md-td>semester_id is invalid</md-td>
  <md-td>周期 ID 不合法，请检查入参 `semester_id` 是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580111</md-td>
  <md-td>invalid user ID</md-td>
  <md-td>被评估人 ID 不合法，请检查入参 `additional_informations` 中的 `reviewee_user_id` 是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580110</md-td>
  <md-td>request ID repeat</md-td>
  <md-td>Client Token 重复，请检查入参 `client_token` 是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580112</md-td>
  <md-td>permission denied</md-td>
  <md-td>操作无权限的被评估人数据，请检查当前应用申请的被评估人数据范围</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580202</md-td>
  <md-td>external ID repeat</md-td>
  <md-td>External ID 重复，请检查入参 `additional_informations` 中是否有重复的 `external_id`</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580203</md-td>
  <md-td>item ID repeat</md-td>
  <md-td>Item ID 重复，请检查入参 `additional_informations` 中是否有重复的 `item_id`</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580201</md-td>
  <md-td>item ID not found</md-td>
  <md-td>Item ID 不合法，请检查入参 `additional_informations` 中的 `item_id`是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1580204</md-td>
  <md-td>external ID is not unique</md-td>
  <md-td>External ID 已绑定在本周期其它补充信息，请检查入参 `additional_informations` 中的 `external_id`是否正确</md-td>
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


