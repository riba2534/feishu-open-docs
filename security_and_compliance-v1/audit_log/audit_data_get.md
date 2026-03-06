---
title: "获取行为审计日志数据"
fullPath: "/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/audit_data_get"
updateTime: "1760680617000"
---

# 获取行为审计日志数据
{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=admin&version=v1&resource=audit_info&method=list)

该接口用于查询成员的操作行为日志。行为审计日志中记录了成员进行操作的时间、地点、操作对象等信息。通过查询成员行为日志，管理员可以发现成员是否有违规操作，以保护企业数据和信息安全。
-  性能说明：查询时请适当缩短查询时间范围和适当控制查询频次（避免重复的无效查询等情况）

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
      <md-td>https://open.feishu.cn/open-apis/admin/v1/audit_infos</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[100 次/分钟](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            
            <div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
            
      </md-th>
      <md-td>
            <md-perm name="admin:audit_info:readonly" desc="获取行为审计日志" support_app_types="custom" tags="">获取行为审计日志</md-perm>
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

**示例值**：user_id

**可选值有**：
<md-enum>
<md-enum-item key="open_id" >标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)</md-enum-item>
<md-enum-item key="union_id" >标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)</md-enum-item>
<md-enum-item key="user_id" >标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)</md-enum-item>
</md-enum>

**默认值**：`user_id`

**当值为 `user_id`，字段权限要求**：
<md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >latest</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	日志时间范围： 结束时间。格式： 秒级时间戳。默认值： 此刻。起止日期之间相差不能超过30天

**示例值**：1668700799
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >oldest</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	日志时间范围： 起始时间。格式： 秒级时间戳。默认值：30日前此刻。起止日期之间相差不能超过30天

**示例值**：1668528000
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >event_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	行为审计的事件名称，可选事件名称见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)

**示例值**：space_create_doc
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >operator_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	过滤操作者: 操作者类型。 与 operator_value 配合使用，当填写operator_value时，此项必填

**示例值**：user

**可选值有**：
<md-enum>
<md-enum-item key="user" >用户</md-enum-item>
<md-enum-item key="bot" >[当前未开放] 以bot_id来识别用户</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >operator_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	操作者值

**示例值**：55ed16fe
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >event_module</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	行为审计的事件模块，可选事件模块见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)

**示例值**：1
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

**示例值**：LC39/f1%2B/Sz9Uv39Gf39/ew/cd5WY0gfGYFdixOW9cVk4bC79ituO/gx0qpPn1bYf92nz/kI0nNJOG3wCwDJKoNU%2BtyaXbpI8pV/9UNDMZT0BNeyanFH17Wv711Qh9anR3l2GjQfc2fUqXtxg1YPp63XyhYY4iRMv54ySRG7r%2BI89iS3zAoPzFuuU1MUJKsf
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

**示例值**：20

**默认值**：`20`

**数据校验规则**：

- 取值范围：`1` ～ `200`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >user_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户类型。此选项为空时，默认查询「组织内成员」。当填写此选项时，operator_type值必须为user。

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="0" >互联网上的任何人</md-enum-item>
<md-enum-item key="1" >组织内成员</md-enum-item>
<md-enum-item key="2" >组织外成员</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >object_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	过滤操作对象: 操作对象类型. 与object_value配合使用

**示例值**：1
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	过滤操作对象: 操作对象ID. 与object_type配合使用

**示例值**：55ed16fe
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
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
	<md-text type="field-name" >items</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_info\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	返回的具体数据内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >event_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	事件ID，不唯一，可用作聚合
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >unique_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	事件唯一ID，可以用于去重，倾向使用该字段识别用户的行为
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >event_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	事件名称，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >department_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	用户所属部门的ID列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >event_module</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	事件模块，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >operator_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	操作人类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >组织内成员</md-enum-item>
<md-enum-item key="12" >机器人</md-enum-item>
<md-enum-item key="1001" >组织外成员</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >operator_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	操作人id，当operator_type是1001时，该项为脱敏后的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >objects</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_object_entity\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	操作对象列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >object_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	操作对象类型，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >object_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	操作对象值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >object_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	操作对象名称，当前针对文档、会话、应用类型开放，如会话名、文档名等
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >object_owner</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	操作对象所有者，当前针对文档类型开放
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >object_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_object_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	操作对象扩展字段，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >recipients</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_recipient_entity\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	接收者对象列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >recipient_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	接收者对象类型，1代表用户，2代表部门，4代表会话
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >recipient_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	接收者对象值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >recipient_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_recipient_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	接收者对象扩展字段
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >event_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	事件时间
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >ip</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	ip信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >operator_app</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	第三方isvID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >audit_context</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_context</md-text>
	</md-dt-td>
	<md-dt-td>
	环境信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >terminal_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	终端类型

**可选值有**：
<md-enum>
<md-enum-item key="0" >ios</md-enum-item>
<md-enum-item key="1" >安卓</md-enum-item>
<md-enum-item key="2" >pc端</md-enum-item>
<md-enum-item key="3" >web端</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >ios_context</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_ios_context</md-text>
	</md-dt-td>
	<md-dt-td>
	返回ios的环境信息，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >pc_context</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_pc_context</md-text>
	</md-dt-td>
	<md-dt-td>
	返回pc的环境信息，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>



<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >web_context</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_web_context</md-text>
	</md-dt-td>
	<md-dt-td>
	返回web的环境信息，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >android_context</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_android_context</md-text>
	</md-dt-td>
	<md-dt-td>
	返回android的环境信息，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >extend</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_event_extend</md-text>
	</md-dt-td>
	<md-dt-td>
	事件扩展字段，参考common_drawers中的信息即可
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >operator_app_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	第三方isv名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >common_drawers</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >api_audit_common_drawers</md-text>
	</md-dt-td>
	<md-dt-td>
	事件扩展字段，字段详情见[枚举值列表](/ssl:ttdoc/ukTMukTMukTM/uQjM5YjL0ITO24CNykjN/audit_log/appendix)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >audit_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >audit_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	设备信息：<br>city：ip位置，城市名称；<br>device_model：设备型号；<br>mc：Mac地址；<br>os：操作系统；
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >operator_tenant</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	操作人所在企业编号
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
        "has_more": false,
        "items": [
            {
  				"event_id": "7254062411181719572",
				"unique_id": "7254062413199179796",
                "event_module": 1,
                "event_name": "space_edit_doc",
		  		"operator_type": 1,
                "operator_value": "4a3b8541",
                "operator_tenant": "F686619755",
                "event_time": 1688968015,
                "audit_context": {
                    "terminal_type": 3,
                    "web_context": {
                        "IP": "fdbd:dc02:ff:1:1:174:246:126",
                        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                    }
                },
                "audit_detail": {
                    "city": "",
                    "device_model": "",
                    "mc": "",
                    "os": ""
                },
                "common_drawers": {
                    "common_draw_info_list": [
                        {
                            "info_key": "CCM_op_status",
                            "info_val": "success",
                            "key_i18n_key": "SuiteAdmin_DrawerKeyspaceeditdoc_Kccmopstatus",
                            "val_i18n_key": "SuiteAdmin_DrawerValspaceeditdoc_Kccmopstatusvsuccess",
                            "val_type": "1"
                        },
                        {
                            "info_key": "ccm_edit_part",
                            "info_val": "0",
                            "key_i18n_key": "SuiteAdmin_DrawerKeyspaceeditdoc_Kccmeditpart",
                            "val_i18n_key": "SuiteAdmin_DrawerValspaceeditdoc_Kccmeditpartv0",
                            "val_type": "1"
                        },
                        {
                            "info_key": "ccm_folder_id",
                            "info_val": "nodbcMQRCwBJ5aWEWxQsWsTA5zg",
                            "key_i18n_key": "SuiteAdmin_DrawerKeyspaceeditdoc_Kccmfolderid",
                            "val_i18n_key": "SuiteAdmin_DrawerValspaceeditdoc_Kccmfolderidvnodbcmqrcwbj5awewxqswsta5zg",
                            "val_type": "1"
                        },
                        {
                            "info_key": "ccm_folder_name",
                            "info_val": "",
                            "key_i18n_key": "SuiteAdmin_DrawerKeyspaceeditdoc_Kccmfoldername",
                            "val_i18n_key": "SuiteAdmin_DrawerValspaceeditdoc_Kccmfoldernamev",
                            "val_type": "1"
                        },
                        {
                            "info_key": "ccm",
                            "info_val": "[{\"key\":\"title\",\"keyName\":\"文件名称\",\"value\":\"\",\"valueType\":\"1\",\"valueExtInfo\":null,\"eventFieldInfoList\":null},{\"key\":\"owner\",\"keyName\":\"文件所有者\",\"value\":\"\",\"valueType\":\"3\",\"valueExtInfo\":\"{\\\"type\\\":3,\\\"id\\\":\\\"0\\\",\\\"name\\\":\\\"\\\",\\\"avatar\\\":\\\"\\\",\\\"employee_id\\\":\\\"\\\"}\",\"eventFieldInfoList\":null},{\"key\":\"create_time\",\"keyName\":\"创建时间\",\"value\":\"\",\"valueType\":\"8\",\"valueExtInfo\":null,\"eventFieldInfoList\":null},{\"key\":\"sec_label\",\"keyName\":\"密级标签\",\"value\":\"\",\"valueType\":\"1\",\"valueExtInfo\":null,\"eventFieldInfoList\":null},{\"key\":\"doc_belong_tenant\",\"keyName\":\"是否属于本组织\",\"value\":\"否\",\"valueType\":\"1\",\"valueExtInfo\":null,\"eventFieldInfoList\":null}]",
                            "key_i18n_key": "文件 ID",
                            "val_type": "Lwd1smp3nl01AndDEMzbsfqacBb"
                        },
                        {
                            "info_key": "ccm_type",
                            "info_val": "-",
                            "key_i18n_key": "文件类型"
                        }
                    ]
                },
                "department_ids": [
                    "0",
                    "od-ab89476fbcf901c3e5ccd78f788f85bf"
                ],
                
                "extend": {},
                "ip": "fdbd:dc02:ff:1:1:174:246:126",
                "objects": [
                    {
                        "object_detail": {},
                        "object_name": "",
                        "object_owner": "",
                        "object_type": "106",
                        "object_value": "Lwd1smp3nl01AndDEMzbsfqacBb"
                    }
                ],
                "operator_app": "",
                "operator_app_name": "",
                "recipients": [
  					{
                        "recipient_type": "",
                        "recipient_value": "",
                        "recipient_detail": {
                            "permission_action_type": ""
                        }
                    }
  				]
            }
        ],
        "page_token": "LC39/f1%2B/Sz9Uv39Gf39/ew/cd5WY0gfGYFdixOW9cW8qPuyh59mg7cXBJKifnqatoP8P2g8URSUi2/4fj5NPJh8VxaPH3yTCnbSZeXzNs4mpQYaUVbp7lTIy1YfIsZ1i0UPASt4qAPObiCewWErhlEG6Qg%2B/6zX7JFBCRsatVcctGTHeL9bb8ssmfdt0Yag"
    }
}
</md-code-json>
:::
注：审计环境信息有可能由于客户端版本不同、用户使用终端不同等原因导致缺失，我们会尽量保障环境信息完整获取，如发现缺失，您也可以随时报告给飞书

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
  <md-td>1050001</md-td>
  <md-td>TIME_CHECK_NOT_VALID</md-td>
  <md-td>检查请求参数latest和oldest</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1050002</md-td>
  <md-td>ErrCode_DATABASE_ERR</md-td>
  <md-td>系统错误，请重试或联系相关人员</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1050004</md-td>
  <md-td>Error_Param_Error</md-td>
  <md-td>检查请求参数</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1050005</md-td>
  <md-td>Error_Page_Size_Invalid</md-td>
  <md-td>检查请求参数page_size</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1050006</md-td>
  <md-td>Error_Page_Token_Invalid</md-td>
  <md-td>检查请求参数page_token</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1050007</md-td>
  <md-td>Error_Event_Name_Not_Found</md-td>
  <md-td>检查请求参数event_name</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1050008</md-td>
  <md-td>Error_Open_Platform_RPC</md-td>
  <md-td>系统错误，请重试或联系相关人员</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1050009</md-td>
  <md-td>Error_Lark_ID_Not_Found</md-td>
  <md-td>检查请求参数operator_value</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::











