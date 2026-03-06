---
title: "更新用户所有信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/update"
updateTime: "1723606526000"
---

# 更新用户所有信息

该接口用于更新通讯录中用户的字段。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=contact&version=v3&resource=user&method=update)

:::html
<md-alert type="error">

</md-alert>
:::

:::html
<md-alert type="warn">
本接口已为历史版本，不再维护更新，不推荐使用。推荐你使用[修改用户部分信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/patch)接口。
</md-alert>
:::

:::html
<md-alert type="tip">
应用需要拥有待更新用户的通讯录授权，如果涉及到用户部门变更，还需要同时拥有变更前、后所有新部门的通讯录授权。
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
      <md-td>https://open.feishu.cn/open-apis/contact/v3/users/:user_id</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>PUT</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[1000 次/分钟、50 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="contact:contact" desc="更新通讯录" support_app_types="custom" tags="">更新通讯录</md-perm>
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
        <md-perm name="contact:user.gender:readonly" desc="获取用户性别" support_app_types="custom,isv" tags="">获取用户性别</md-perm>
        <md-perm name="contact:user.base:readonly" desc="获取用户基本信息" support_app_types="custom,isv" tags="">获取用户基本信息</md-perm>
        <md-perm name="contact:user.department:readonly" desc="获取用户组织架构信息" support_app_types="custom,isv" tags="">获取用户组织架构信息</md-perm>
        <md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
        <md-perm name="contact:user.phone:readonly" desc="获取用户手机号" support_app_types="custom" tags="">获取用户手机号</md-perm>
        <md-perm name="contact:user.email:readonly" desc="获取用户邮箱信息" support_app_types="custom" tags="">获取用户邮箱信息</md-perm>
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
        <md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
        <md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
        <md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
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
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户ID，需要与查询参数中的user_id_type类型保持一致。

**示例值**："ou_7dab8a3d3cdcc9da365777c7ad535d62"
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
</md-enum>

**默认值**：`open_id`

**当值为 `user_id`，字段权限要求**：
<md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
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
	此次调用中使用的部门ID的类型

**示例值**：open_department_id

**可选值有**：
<md-enum>
<md-enum-item key="department_id" >以自定义department_id来标识部门</md-enum-item>
<md-enum-item key="open_department_id" >以open_department_id来标识部门</md-enum-item>
</md-enum>

**默认值**：`open_department_id`
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
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	用户名

**示例值**："张三"

**数据校验规则**：

- 最小长度：`1` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >en_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	英文名

**示例值**："San Zhang"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >nickname</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	别名

**示例值**："Alex Zhang"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >email</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	邮箱

注意：
1. 非中国大陆手机号成员必须同时添加邮箱
2. 邮箱不可重复

**示例值**："zhangsan@gmail.com"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >mobile</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	手机号

注意：
1. 在本企业内不可重复
2. 未认证企业仅支持添加中国大陆手机号，通过飞书认证的企业允许添加海外手机号
3. 国际电话区号前缀中必须包含加号 +
4. 该 mobile 字段在海外版飞书非必填

**示例值**："13011111111 (其他例子，中国大陆手机号: 13011111111 或 +8613011111111, 非中国大陆手机号:  +41446681800)"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >mobile_visible</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	手机号码可见性，true 为可见，false 为不可见，目前默认为 true。不可见时，组织员工将无法查看该员工的手机号码

**示例值**：false
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >gender</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	性别

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="0" >保密</md-enum-item>
<md-enum-item key="1" >男</md-enum-item>
<md-enum-item key="2" >女</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >avatar_key</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	头像的文件Key，可通过“消息与群组/消息/图片信息”中的“上传图片”接口上传并获取头像文件 Key

“上传图片”功能参见[上传图片](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/create)

**示例值**："2500c7a9-5fff-4d9a-a2de-3d59614ae28g"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >department_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	用户所属部门的ID列表，一个用户可属于多个部门。

ID值的类型与查询参数中的department_id_type 对应。

不同 ID 的说明与department_id的获取方式参见 [部门ID说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0)

**示例值**：["od-4e6ac4d14bcd5071a37a39de902c7141"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >leader_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户的直接主管的用户ID，ID值与查询参数中的user_id_type 对应。

不同 ID 的说明参见 [用户相关的 ID 概念](/ssl:ttdoc/home/user-identity-introduction/introduction)

获取方式参见[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)

**示例值**："ou_7dab8a3d3cdcc9da365777c7ad535d62"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >city</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工作城市

**示例值**："杭州"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >country</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	国家或地区Code缩写，具体写入格式请参考 [国家/地区码表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/country-code-description)

**示例值**："CN"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >work_station</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工位

**示例值**："北楼-H34"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >join_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	入职时间，时间戳格式，表示从1970年1月1日开始所经过的秒数

**示例值**：2147483647
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >employee_no</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	工号

**示例值**："1"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >employee_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	员工类型，可选值有：
- `1`：正式员工
- `2`：实习生
- `3`：外包
- `4`：劳务
- `5`：顾问   
同时可读取到自定义员工类型的 int 值，可通过下方接口获取到该租户的自定义员工类型的名称，参见[获取人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)

**示例值**：1
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >orders</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user_order\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户排序信息。

用于标记通讯录下组织架构的人员顺序，人员可能存在多个部门中，且有不同的排序。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
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
	排序信息对应的部门ID， ID值与查询参数中的department_id_type 对应。

表示用户所在的、且需要排序的部门。

不同 ID 的说明参见及获取方式参见 [部门ID说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview)

**示例值**："od-4e6ac4d14bcd5071a37a39de902c7141"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >user_order</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户在其直属部门内的排序，数值越大，排序越靠前

**示例值**：100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >department_order</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户所属的多个部门间的排序，数值越大，排序越靠前

**示例值**：100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >is_primary_dept</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	标识用户的唯一主部门，主部门为用户所属部门中排序第一的部门(department_order最大)

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >custom_attrs</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user_custom_attr\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段，请确保你的组织管理员已在管理后台/组织架构/成员字段管理/自定义字段管理/全局设置中开启了“允许开放平台 API 调用“，否则该字段不会生效/返回。

更多详情参见[用户接口相关问题](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN#77061525)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段类型   
- `TEXT`：文本
- `HREF`：网页
- `ENUMERATION`：枚举
- `PICTURE_ENUM`：图片
- `GENERIC_USER`：用户

具体说明参见常见问题的[用户接口相关问题](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN#77061525)

**示例值**："TEXT"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段ID

**示例值**："DemoId"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user_custom_attr_value</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义字段取值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	字段类型为`TEXT`时该参数定义字段值，必填；字段类型为`HREF`时该参数定义网页标题，必填

**示例值**："DemoText"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	字段类型为 HREF 时，该参数定义默认 URL，例如手机端跳转小程序，PC端跳转网页

**示例值**："http://www.fs.cn"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >pc_url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	字段类型为 HREF 时，该参数定义PC端 URL

**示例值**："http://www.fs.cn"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >option_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	字段类型为 ENUMERATION 或 PICTURE_ENUM 时，该参数定义选项值

**示例值**："edcvfrtg"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >generic_user</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_attr_generic_user</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	字段类型为 GENERIC_USER 时，该参数定义引用人员
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	用户的user_id ，具体参见[用户相关的 ID 概念](/ssl:ttdoc/home/user-identity-introduction/introduction)

**示例值**："9b2fabg5"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	用户类型:  
1：用户

目前固定为1，表示用户类型

**示例值**：1
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >enterprise_email</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	企业邮箱，请先确保已在管理后台启用飞书邮箱服务

创建用户时，企业邮箱的使用方式参见[用户接口相关问题](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN#77061525)

**示例值**："demo@mail.com"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	职务

**示例值**："xxxxx"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >is_frozen</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否暂停用户

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
    "name": "张三",
    "en_name": "San Zhang",
    "nickname": "Alex Zhang",
    "email": "zhangsan@gmail.com",
    "mobile": "13011111111 (其他例子，中国大陆手机号: 13011111111 或 +8613011111111, 非中国大陆手机号:  +41446681800)",
    "mobile_visible": false,
    "gender": 1,
    "avatar_key": "2500c7a9-5fff-4d9a-a2de-3d59614ae28g",
    "department_ids": [
        "od-4e6ac4d14bcd5071a37a39de902c7141"
    ],
    "leader_user_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
    "city": "杭州",
    "country": "CN",
    "work_station": "北楼-H34",
    "join_time": 2147483647,
    "employee_no": "1",
    "employee_type": 1,
    "orders": [
        {
            "department_id": "od-4e6ac4d14bcd5071a37a39de902c7141",
            "user_order": 100,
            "department_order": 100,
            "is_primary_dept": true
        }
    ],
    "custom_attrs": [
        {
            "type": "TEXT",
            "id": "DemoId",
            "value": {
                "text": "DemoText",
                "url": "http://www.fs.cn",
                "pc_url": "http://www.fs.cn",
                "option_id": "edcvfrtg",
                "generic_user": {
                    "id": "9b2fabg5",
                    "type": 1
                }
            }
        }
    ],
    "enterprise_email": "demo@mail.com",
    "job_title": "xxxxx",
    "is_frozen": false
}
</md-code-json>
:::

**Go 请求示例**
```go
import (
	"context"

	"github.com/larksuite/oapi-sdk-go/v3"
	"github.com/larksuite/oapi-sdk-go/v3/service/contact/v3"
)

func main() {
	// 创建 Client
	client := lark.NewClient("appID", "appSecret")

	// 创建请求对象
	req := larkcontact.NewUpdateUserReqBuilder().
		UserId(`ou_7dab8a3d3cdcc9da365777c7ad535d62`).
		User(larkcontact.NewUserBuilder().
			Name(`张三`).
			Mobile(`13011111111`).
			DepartmentIds([]string{`od-4e6ac4d14bcd5071a37a39de902c7141`}).
			EmployeeType(1).
			Build()).
		Build()

	// 发起请求
	resp, err := client.Contact.User.Update(context.Background(), req)
}
```

**Java 请求示例**
```java
import com.lark.oapi.Client;
import com.lark.oapi.core.request.RequestOptions;
import com.lark.oapi.service.contact.v3.model.UpdateUserReq;
import com.lark.oapi.service.contact.v3.model.UpdateUserResp;
import com.lark.oapi.service.contact.v3.model.User;

public class Main {

    public static void main(String arg[]) throws Exception {
        // 构建client
        Client client = Client.newBuilder("appId", "appSecret").build();

        // 创建请求对象
        UpdateUserReq req = UpdateUserReq.newBuilder()
                .userId("ou_7dab8a3d3cdcc9da365777c7ad535d62")
                .user(User.newBuilder()
                        .name("张三")
                        .mobile("13011111111")
                        .departmentIds(new String[]{"od-4e6ac4d14bcd5071a37a39de902c7141"})
                        .employeeType(1)
                        .build())
                .build();

        // 发起请求
        UpdateUserResp resp = client.contact().user().update(req, RequestOptions.newBuilder().build());
    }
}
```

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
	<md-text type="field-name" >user</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user</md-text>
	</md-dt-td>
	<md-dt-td>
	用户信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >union_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的union_id，应用开发商发布的不同应用中同一用户的标识，不同ID的说明参见 [用户相关的 ID 概念](/ssl:ttdoc/home/user-identity-introduction/introduction)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的user_id，租户内用户的唯一标识，不同ID的说明参见 [用户相关的 ID 概念](/ssl:ttdoc/home/user-identity-introduction/introduction)

**字段权限要求**：
<md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >open_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的open_id，应用内用户的唯一标识，不同ID的说明参见 [用户相关的 ID 概念](/ssl:ttdoc/home/user-identity-introduction/introduction)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户名

**字段权限要求（满足任一）**：
<md-perm name="contact:user.base:readonly" desc="获取用户基本信息" support_app_types="custom,isv" tags="">获取用户基本信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >en_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	英文名

**字段权限要求（满足任一）**：
<md-perm name="contact:user.base:readonly" desc="获取用户基本信息" support_app_types="custom,isv" tags="">获取用户基本信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >nickname</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	别名

**字段权限要求（满足任一）**：
<md-perm name="contact:user.base:readonly" desc="获取用户基本信息" support_app_types="custom,isv" tags="">获取用户基本信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >email</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	邮箱

注意：
1. 非中国大陆手机号成员必须同时添加邮箱
2. 邮箱不可重复

**字段权限要求**：
<md-perm name="contact:user.email:readonly" desc="获取用户邮箱信息" support_app_types="custom" tags="">获取用户邮箱信息</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >mobile</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	手机号

注意：
1. 在本企业内不可重复
2. 未认证企业仅支持添加中国大陆手机号，通过飞书认证的企业允许添加海外手机号
3. 国际电话区号前缀中必须包含加号 +
4. 该 mobile 字段在海外版飞书非必填

**字段权限要求**：
<md-perm name="contact:user.phone:readonly" desc="获取用户手机号" support_app_types="custom" tags="">获取用户手机号</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >mobile_visible</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	手机号码可见性，true 为可见，false 为不可见，目前默认为 true。不可见时，组织员工将无法查看该员工的手机号码
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >gender</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	性别

**可选值有**：
<md-enum>
<md-enum-item key="0" >保密</md-enum-item>
<md-enum-item key="1" >男</md-enum-item>
<md-enum-item key="2" >女</md-enum-item>
</md-enum>

**字段权限要求（满足任一）**：
<md-perm name="contact:user.gender:readonly" desc="获取用户性别" support_app_types="custom,isv" tags="">获取用户性别</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >avatar_key</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	头像的文件Key，可通过“消息与群组/消息/图片信息”中的“上传图片”接口上传并获取头像文件 Key

“上传图片”功能参见[上传图片](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/create)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >avatar</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >avatar_info</md-text>
	</md-dt-td>
	<md-dt-td>
	用户头像信息

**字段权限要求（满足任一）**：
<md-perm name="contact:user.base:readonly" desc="获取用户基本信息" support_app_types="custom,isv" tags="">获取用户基本信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >avatar_72</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	72*72像素头像链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >avatar_240</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	240*240像素头像链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >avatar_640</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	640*640像素头像链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >avatar_origin</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	原始头像链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user_status</md-text>
	</md-dt-td>
	<md-dt-td>
	用户状态，枚举类型，包括is_frozen、is_resigned、is_activated、is_exited 。

用户状态转移参见：[用户状态图](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/field-overview#4302b5a1)

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_frozen</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否暂停
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_resigned</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否离职
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_activated</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否激活
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_exited</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否主动退出，主动退出一段时间后用户会自动转为已离职
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_unjoin</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否未加入，需要用户自主确认才能加入团队
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
	用户所属部门的ID列表，一个用户可属于多个部门。

ID值的类型与查询参数中的department_id_type 对应。

不同 ID 的说明与department_id的获取方式参见 [部门ID说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0)

**字段权限要求（满足任一）**：
<md-perm name="contact:user.department:readonly" desc="获取用户组织架构信息" support_app_types="custom,isv" tags="">获取用户组织架构信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >leader_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的直接主管的用户ID，ID值与查询参数中的user_id_type 对应。

不同 ID 的说明参见 [用户相关的 ID 概念](/ssl:ttdoc/home/user-identity-introduction/introduction)

获取方式参见[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)

**字段权限要求（满足任一）**：
<md-perm name="contact:user.department:readonly" desc="获取用户组织架构信息" support_app_types="custom,isv" tags="">获取用户组织架构信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >city</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	工作城市

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >country</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	国家或地区Code缩写，具体写入格式请参考 [国家/地区码表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/country-code-description)

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >work_station</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	工位

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >join_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	入职时间，时间戳格式，表示从1970年1月1日开始所经过的秒数

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_tenant_manager</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否是租户超级管理员

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employee_no</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	工号

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >employee_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	员工类型，可选值有：
- `1`：正式员工
- `2`：实习生
- `3`：外包
- `4`：劳务
- `5`：顾问   
同时可读取到自定义员工类型的 int 值，可通过下方接口获取到该租户的自定义员工类型的名称，参见[获取人员类型](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >orders</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user_order\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	用户排序信息。

用于标记通讯录下组织架构的人员顺序，人员可能存在多个部门中，且有不同的排序。

**字段权限要求（满足任一）**：
<md-perm name="contact:user.department:readonly" desc="获取用户组织架构信息" support_app_types="custom,isv" tags="">获取用户组织架构信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >department_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	排序信息对应的部门ID， ID值与查询参数中的department_id_type 对应。

表示用户所在的、且需要排序的部门。

不同 ID 的说明参见及获取方式参见 [部门ID说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >user_order</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	用户在其直属部门内的排序，数值越大，排序越靠前
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >department_order</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	用户所属的多个部门间的排序，数值越大，排序越靠前
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_primary_dept</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	标识用户的唯一主部门，主部门为用户所属部门中排序第一的部门(department_order最大)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom_attrs</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user_custom_attr\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段，请确保你的组织管理员已在管理后台/组织架构/成员字段管理/自定义字段管理/全局设置中开启了“允许开放平台 API 调用“，否则该字段不会生效/返回。

更多详情参见[用户接口相关问题](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN#77061525)

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段类型   
- `TEXT`：文本
- `HREF`：网页
- `ENUMERATION`：枚举
- `PICTURE_ENUM`：图片
- `GENERIC_USER`：用户

具体说明参见常见问题的[用户接口相关问题](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN#77061525)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >user_custom_attr_value</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义字段取值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	字段类型为`TEXT`时该参数定义字段值，必填；字段类型为`HREF`时该参数定义网页标题，必填
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	字段类型为 HREF 时，该参数定义默认 URL，例如手机端跳转小程序，PC端跳转网页
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >pc_url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	字段类型为 HREF 时，该参数定义PC端 URL
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >option_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	字段类型为 ENUMERATION 或 PICTURE_ENUM 时，该参数定义选项值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >option_value</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	选项类型的值。

表示 成员详情/自定义字段 中选项选中的值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	选项类型为图片时，表示图片的名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >picture_url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	图片链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >generic_user</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >custom_attr_generic_user</md-text>
	</md-dt-td>
	<md-dt-td>
	字段类型为 GENERIC_USER 时，该参数定义引用人员
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	用户的user_id ，具体参见[用户相关的 ID 概念](/ssl:ttdoc/home/user-identity-introduction/introduction)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	用户类型:  
1：用户

目前固定为1，表示用户类型
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >enterprise_email</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	企业邮箱，请先确保已在管理后台启用飞书邮箱服务

创建用户时，企业邮箱的使用方式参见[用户接口相关问题](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN#77061525)

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >job_title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	职务

**字段权限要求（满足任一）**：
<md-perm name="contact:user.employee:readonly" desc="获取用户受雇信息" support_app_types="custom,isv" tags="">获取用户受雇信息</md-perm>
<md-perm name="contact:contact:access_as_app" desc="以应用身份访问通讯录" support_app_types="custom,isv" tags="history,offline">以应用身份访问通讯录</md-perm>
<md-perm name="contact:contact:readonly" desc="读取通讯录" support_app_types="custom,isv" tags="history,offline">读取通讯录</md-perm>
<md-perm name="contact:contact:readonly_as_app" desc="以应用身份读取通讯录" support_app_types="custom,isv" tags="history">以应用身份读取通讯录</md-perm>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_frozen</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否暂停用户
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
        "user": {
            "union_id": "on_94a1ee5551019f18cd73d9f111898cf2",
            "user_id": "3e3cf96b",
            "open_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
            "name": "张三",
            "en_name": "San Zhang",
            "nickname": "Alex Zhang",
            "email": "zhangsan@gmail.com",
            "mobile": "13011111111 (其他例子，中国大陆手机号: 13011111111 或 +8613011111111, 非中国大陆手机号:  +41446681800)",
            "mobile_visible": false,
            "gender": 1,
            "avatar_key": "2500c7a9-5fff-4d9a-a2de-3d59614ae28g",
            "avatar": {
                "avatar_72": "https://foo.icon.com/xxxx",
                "avatar_240": "https://foo.icon.com/xxxx",
                "avatar_640": "https://foo.icon.com/xxxx",
                "avatar_origin": "https://foo.icon.com/xxxx"
            },
            "status": {
                "is_frozen": false,
                "is_resigned": false,
                "is_activated": true,
                "is_exited": false,
                "is_unjoin": false
            },
            "department_ids": [
                "od-4e6ac4d14bcd5071a37a39de902c7141"
            ],
            "leader_user_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
            "city": "杭州",
            "country": "CN",
            "work_station": "北楼-H34",
            "join_time": 2147483647,
            "is_tenant_manager": false,
            "employee_no": "1",
            "employee_type": 1,
            "orders": [
                {
                    "department_id": "od-4e6ac4d14bcd5071a37a39de902c7141",
                    "user_order": 100,
                    "department_order": 100,
                    "is_primary_dept": true
                }
            ],
            "custom_attrs": [
                {
                    "type": "TEXT",
                    "id": "DemoId",
                    "value": {
                        "text": "DemoText",
                        "url": "http://www.fs.cn",
                        "pc_url": "http://www.fs.cn",
                        "option_id": "edcvfrtg",
                        "option_value": "option",
                        "name": "name",
                        "picture_url": "https://xxxxxxxxxxxxxxxxxx",
                        "generic_user": {
                            "id": "9b2fabg5",
                            "type": 1
                        }
                    }
                }
            ],
            "enterprise_email": "demo@mail.com",
            "job_title": "xxxxx",
            "is_frozen": false
        }
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
  <md-td>40001</md-td>
  <md-td>param error</md-td>
  <md-td>参数错误。你可以自行检查输入参数是否设置有误。如果问题无法解决可联系开放平台[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>40016</md-td>
  <md-td>dept name can not be nul error</md-td>
  <md-td>部门名不能为空。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41001</md-td>
  <md-td>mobile has already exist error</md-td>
  <md-td>手机号已存在</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41002</md-td>
  <md-td>email has already exist error</md-td>
  <md-td>邮箱已存在</md-td>
</md-tr>


<md-tr>
  <md-td>409</md-td>
  <md-td>41003</md-td>
  <md-td>user account conflict error</md-td>
  <md-td>用户的联系方式属于两个不同的飞书账号，添加失败。建议用户换其它的手机号或邮箱，或是先注销手机号或邮箱对应的帐号，然后再创建或更新，具体注销的流程见[帮助中心](https://www.feishu.cn/hc/zh-CN/articles/360049067831)

有关这个错误的详细介绍请参考[通用错误码](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN#74588198)中的介绍</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41004</md-td>
  <md-td>mobile is invalid error</md-td>
  <md-td>手机号不合法，请检查是否是正确的手机号格式</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41005</md-td>
  <md-td>email is invalid error</md-td>
  <md-td>不是合法邮箱的邮箱地址，请检查邮箱地址的有效性</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41006</md-td>
  <md-td>no user name error</md-td>
  <md-td>没有设置user的name</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41009</md-td>
  <md-td>no email or mobile error</md-td>
  <md-td>电子邮箱和手机号不能都为空。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41011</md-td>
  <md-td>user id already exist error</md-td>
  <md-td>user_id是企业内用户的唯一ID，不能重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41010</md-td>
  <md-td>no mobile error</md-td>
  <md-td>手机号不能为空。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41014</md-td>
  <md-td> user name sensitive error</md-td>
  <md-td>name中包含敏感信息，如有疑问，请联系客服</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41013</md-td>
  <md-td>exceed user id update limit error</md-td>
  <md-td>用户ID更新次数超过限制。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41015</md-td>
  <md-td>idp type invalid error error</md-td>
  <md-td>登录类型无效。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41016</md-td>
  <md-td>department has too many users  error</md-td>
  <md-td>一个部门中有过多的用户，用户数量超过了500</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41017</md-td>
  <md-td>department is required error</md-td>
  <md-td>部门信息不能为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41018</md-td>
  <md-td>position info is invalid error</md-td>
  <md-td>岗位信息无效</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41019</md-td>
  <md-td>position department is invalid error</md-td>
  <md-td>岗位部门无效</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41020</md-td>
  <md-td>position code has already exist  error</md-td>
  <md-td>岗位code无效</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41021</md-td>
  <md-td>position multiple main count error</md-td>
  <md-td>一个用户至多只能有设置一个主岗</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41022</md-td>
  <md-td>user tenant not match error</md-td>
  <md-td>检查是否使用其他企业的凭证访问当前企业的资源</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41023</md-td>
  <md-td>update department conflict position department error</md-td>
  <md-td>用户的岗位部门必须与用户的部门一致，更新用户部门需要同时更新相应的岗位部门，否则阻断更新操作</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41024</md-td>
  <md-td>update position department conflict department error</md-td>
  <md-td>用户的岗位部门必须与用户的部门一致，用户的新岗位部门也必须是用户的部门之一，否则阻断更新操作</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41025</md-td>
  <md-td>order department invalid error</md-td>
  <md-td>请求的用户排序信息中的部门ID必须是用户的部门ID之一</md-td>
</md-tr>


<md-tr>
  <md-td>405</md-td>
  <md-td>41028</md-td>
  <md-td>user multi department need upgrade visibility error</md-td>
  <md-td>请在企业管理后台更新“组织架构可见范围”的补充规则</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41029</md-td>
  <md-td>create or update user multi department error</md-td>
  <md-td>当前企业不支持用户同时加入多个部门，如有疑问，请联系客服</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41030</md-td>
  <md-td>set leader to oneself error</md-td>
  <md-td>请检查用户的直属上级参数值</md-td>
</md-tr>


<md-tr>
  <md-td>504</md-td>
  <md-td>41031</md-td>
  <md-td>position feature not enable error</md-td>
  <md-td>当前企业不支持设置用户岗位信息，如有疑问，请联系客服</md-td>
</md-tr>


<md-tr>
  <md-td>504</md-td>
  <md-td>41032</md-td>
  <md-td>user multi department feature not enable error</md-td>
  <md-td>当前企业不支持用户同时加入多个部门，如有疑问，请联系客服</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41033</md-td>
  <md-td>user in too many departments  error</md-td>
  <md-td>不支持用户同时属于50个以上的部门，请检查</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41034</md-td>
  <md-td>email prefix already exist error</md-td>
  <md-td>email的前缀已经存在</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41035</md-td>
  <md-td>email prefix is invalid error</md-td>
  <md-td>email的前缀不合法，请检查拼写</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41036</md-td>
  <md-td>avatar key is invalid error</md-td>
  <md-td>头像key无效</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41037</md-td>
  <md-td>avatar key is sensitive error</md-td>
  <md-td>头像key存在敏感信息</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41038</md-td>
  <md-td>gender is invalid error</md-td>
  <md-td>性别不合法，请检查</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41040</md-td>
  <md-td>user name is null error</md-td>
  <md-td>用户名不能为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41041</md-td>
  <md-td>department id is not assigned  error</md-td>
  <md-td>用户所属的部门不能为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41042</md-td>
  <md-td>join time is invalid error</md-td>
  <md-td>用户加入时间不能为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41043</md-td>
  <md-td>employee id is invalid error</md-td>
  <md-td>无效的user id。 大小位于1-64个字节之间</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41044</md-td>
  <md-td>Custom attribute is not set error</md-td>
  <md-td>设置用户自定义字段，必须指明设定的字段ID，字段ID可以通过获取企业自定义字段接口查询</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41045</md-td>
  <md-td>Custom attribute id is not exist error</md-td>
  <md-td>自定义字段ID不存在，请确认自定义字段ID来源，自定义字段ID可以通过获取企业自定义字段接口查询</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41046</md-td>
  <md-td>Custom attribute value is not set error</md-td>
  <md-td>设置自定义字段，需要传入字段value字段</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41047</md-td>
  <md-td>Custom attribute href text  is null error</md-td>
  <md-td>设置HREF类型自定义字段，text字段为必填字段</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41048</md-td>
  <md-td>Custom attribute href url  is null error</md-td>
  <md-td>设置HREF类型自定义字段，url字段为必填字段</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41050</md-td>
  <md-td>no user authority error</md-td>
  <md-td>操作的用户需在通讯录权限范围中，[了解更多](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41051</md-td>
  <md-td>user id info not provide error</md-td>
  <md-td>用户ID没有填写</md-td>
</md-tr>


<md-tr>
  <md-td>403</md-td>
  <md-td>40004</md-td>
  <md-td>no dept authority error</md-td>
  <md-td>操作的部门需在通讯录权限范围中，[了解更多](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41059</md-td>
  <md-td>invalid employee type error</md-td>
  <md-td>用户的雇员类型错误，请填写1-5之间的数字，1 正式员工 2 实习生 3 外包 4 劳务 5 顾问</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41060</md-td>
  <md-td>inactive employee type error</md-td>
  <md-td>雇员类型企业未使用，请咨询管理员</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41063</md-td>
  <md-td>job_title length exceed 100 character</md-td>
  <md-td>职务的设置长度超过100字符，请检查字段长度</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41068</md-td>
  <md-td>Number of email aliases exceeds the upper limit</md-td>
  <md-td>企业邮箱账户已经达到上线，请咨询企业管理员</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41069</md-td>
  <md-td>Business email is in the recycle bin</md-td>
  <md-td>企业邮正在回收中，不可使用</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41070</md-td>
  <md-td>name length exceed 64 character</md-td>
  <md-td>姓名长度超过64个字符</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41071</md-td>
  <md-td>en_name length exceed 64 character</md-td>
  <md-td>英文名长度超过64个字符</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41072</md-td>
  <md-td>nickname length exceed 64 character</md-td>
  <md-td>别名长度超过64个字符</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44001</md-td>
  <md-td>business email domain not available error</md-td>
  <md-td>企业无对应的企业邮域名，咨询企业管理员</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44002</md-td>
  <md-td>update order must update department together</md-td>
  <md-td>修改用户部门排序时，请求必须同时带上部门ID列表</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44006</md-td>
  <md-td>name length exceed 64 character</md-td>
  <md-td>姓名超过64个字符</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44007</md-td>
  <md-td>en_name length exceed 64 character</md-td>
  <md-td>英文名超过64个字符</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44008</md-td>
  <md-td>nickname length exceed 64 character</md-td>
  <md-td>别名超过64个字符</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44010</md-td>
  <md-td>unJoined user not allow to update</md-td>
  <md-td>未加入状态用户禁止更新</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44011</md-td>
  <md-td>existed user not allow to update</md-td>
  <md-td>已激活用户禁止更新</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>42006</md-td>
  <md-td>user has resigned error</md-td>
  <md-td>用户已经离职。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44013</md-td>
  <md-td>User enterprise Email password is not valid</md-td>
  <md-td>--</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44014</md-td>
  <md-td>Can not update inactive user email when email equal enterprise</md-td>
  <md-td>-</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44015</md-td>
  <md-td>can not update password when user already have password</md-td>
  <md-td>-</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44016</md-td>
  <md-td>can not set enterprise email password</md-td>
  <md-td>--</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44017</md-td>
  <md-td>Suite_Admin_Common_UnableToEditUpper</md-td>
  <md-td>-</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44018</md-td>
  <md-td>lark not support +86 mobile</md-td>
  <md-td>--</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44019</md-td>
  <md-td>feishu only support +86 mobile</md-td>
  <md-td>未认证企业仅支持添加中国大陆+86 手机号，添加非 +86 手机号请先完成飞书认证，完成认证后次日可添加。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44020</md-td>
  <md-td>mobile and email need together exist</md-td>
  <md-td>已认证企业，添加非 +86 手机号成员时必须同时添加邮箱</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44024</md-td>
  <md-td>User enterprise email has already been registered as a member's account</md-td>
  <md-td>企业邮箱已注册</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44025</md-td>
  <md-td>update user lock error,wait some seconds and retry</md-td>
  <md-td>并发更新User受限，请等待一段时间重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44035</md-td>
  <md-td>departmentID is invaild</md-td>
  <md-td>部门ID是无效的</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44036</md-td>
  <md-td>freeze tenant founder is forbidden</md-td>
  <md-td>禁止冻结租户创始人</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>44038</md-td>
  <md-td>this user can not been update by security issues</md-td>
  <md-td>此用户因安全问题无法更新</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>41410</md-td>
  <md-td>user primary dept must be the first department in the order</md-td>
  <md-td>主部门必须为用户所属部门中排序第一的部门(department_order最大)</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




