---
title: "获取角色详情"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/role/get"
updateTime: "1730873717000"
---

# 获取角色详情

可通过此接口获取角色详情信息，包括名称、描述、权限列表等{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=hire&version=v1&resource=role&method=get)

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
      <md-td>https://open.feishu.cn/open-apis/hire/v1/roles/:role_id</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>GET</md-td>
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
            
            <div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
            
      </md-th>
      <md-td>
            <md-perm name="hire:auth:readonly" desc="获取招聘权限信息" support_app_types="custom,isv" tags="">获取招聘权限信息</md-perm>
            <md-perm name="hire:auth" desc="更新招聘权限信息" support_app_types="custom" tags="">更新招聘权限信息</md-perm>
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
	<md-text type="field-name" >role_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID，调用 [获取角色列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/role/list)获取。

**示例值**："7350589232462807068"
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
	<md-text type="field-name" >role</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >role_detail</md-text>
	</md-dt-td>
	<md-dt-td>
	角色详情
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	角色名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	角色描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色中文描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	角色英文描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >modify_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	更新时间，毫秒时间戳
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >role_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	角色启用状态

**可选值有**：
<md-enum>
<md-enum-item key="1" >启用</md-enum-item>
<md-enum-item key="2" >停用</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >role_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	角色类型

**可选值有**：
<md-enum>
<md-enum-item key="1" >系统内置角色</md-enum-item>
<md-enum-item key="2" >普通用户</md-enum-item>
<md-enum-item key="5" >自定义角色</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >scope_of_application</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	角色适用范围

**可选值有**：
<md-enum>
<md-enum-item key="1" >社招</md-enum-item>
<md-enum-item key="2" >校招</md-enum-item>
<md-enum-item key="3" >都包含</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >has_business_management_scope</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否在角色上配置业务管理范围
- `true`：配置了业务管理范围
- `false`：未配置业务管理范围
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >socail_permission_collection</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >permission_collection</md-text>
	</md-dt-td>
	<md-dt-td>
	社招权限配置，仅当`scope_of_application`为“社招”或“都包含”时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >feature_permissions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	功能权限
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
	权限点 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >management_permissions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	管理权限
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
	权限点 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >data_permissions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >data_permission\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	数据权限
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
	权限点 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >select_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	数据权限状态

**可选值有**：
<md-enum>
<md-enum-item key="0" >不可见</md-enum-item>
<md-enum-item key="1" >可见</md-enum-item>
<md-enum-item key="2" >可编辑</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >business_management_scopes</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >business_management_scope\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	业务管理范围
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >entity</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >entity_info</md-text>
	</md-dt-td>
	<md-dt-td>
	实体
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	实体code，枚举如下
- `talent`：人才
- `application`：投递
- `interview`：面试
- `interview_appointment_project`：预约面试
- `jobfair`：集中面试
- `exam_session`：集中笔试
- `offer`：Offer
- `job`：职位
- `job_recruitment`：招聘需求
- `reward`：内推奖励
- `info_session`：宣讲会
- `bi`：BI
- `subject`：对应项目
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	实体名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	实体中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	实体英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >permission_groups</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >permission_group_info\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	权限分组
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >permission_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点 ID列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >scope_rule</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >permission_scope_rule</md-text>
	</md-dt-td>
	<md-dt-td>
	管理范围规则
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >rule_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	规则类型

**可选值有**：
<md-enum>
<md-enum-item key="0" >无数据权限</md-enum-item>
<md-enum-item key="1" >全部数据权限</md-enum-item>
<md-enum-item key="2" >按规则指定范围，当前系统暂不支持返回详细规则</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >campus_permission_collection</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >permission_collection</md-text>
	</md-dt-td>
	<md-dt-td>
	校招权限配置，仅当`scope_of_application`为“校招”或“都包含”时有值
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >feature_permissions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	功能权限
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
	权限点 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >management_permissions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >id_name_object\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	管理权限
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
	权限点 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >data_permissions</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >data_permission\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	数据权限
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
	权限点 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >select_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	数据权限状态

**可选值有**：
<md-enum>
<md-enum-item key="0" >不可见</md-enum-item>
<md-enum-item key="1" >可见</md-enum-item>
<md-enum-item key="2" >可编辑</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >business_management_scopes</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >business_management_scope\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	业务管理范围
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >entity</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >entity_info</md-text>
	</md-dt-td>
	<md-dt-td>
	实体
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	实体code，枚举如下
- `talent`：人才
- `application`：投递
- `interview`：面试
- `interview_appointment_project`：预约面试
- `jobfair`：集中面试
- `exam_session`：集中笔试
- `offer`：Offer
- `job`：职位
- `job_recruitment`：招聘需求
- `reward`：内推奖励
- `info_session`：宣讲会
- `bi`：BI
- `subject`：对应项目
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >i18n</md-text>
	</md-dt-td>
	<md-dt-td>
	实体名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >zh_cn</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	实体中文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >en_us</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	实体英文名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >permission_groups</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >permission_group_info\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	权限分组
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >permission_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	权限点 ID列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >scope_rule</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >permission_scope_rule</md-text>
	</md-dt-td>
	<md-dt-td>
	管理范围规则
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >rule_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	规则类型

**可选值有**：
<md-enum>
<md-enum-item key="0" >无数据权限</md-enum-item>
<md-enum-item key="1" >全部数据权限</md-enum-item>
<md-enum-item key="2" >按规则指定范围，当前系统暂不支持返回详细规则</md-enum-item>
</md-enum>
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
    "msg": "SUCCESS",
    "data": {
        "role": {
            "id": "6930815272790114324",
            "name": {
                "zh_cn": "招聘 HRBP",
                "en_us": "Recruitment HRBP"
            },
            "description": {
                "zh_cn": "赋予HRBP的权限",
                "en_us": "Authority given to HRBP"
            },
            "modify_time": "1716535727510",
            "role_status": 1,
            "role_type": 1,
            "scope_of_application": 1,
            "has_business_management_scope": true,
            "socail_permission_collection": {
                "feature_permissions": [
                    {
                        "id": "10101000",
                        "name": {
                            "zh_cn": "查看人才",
                            "en_us": "View talent"
                        }
                    }
                ],
                "management_permissions": [
                    {
                        "id": "20101001",
                        "name": {
                            "zh_cn": "门店管理",
                            "en_us": "Store management"
                        }
                    }
                ],
                "data_permissions": [
                    {
                        "id": "30203005",
                        "name": {
                            "zh_cn": "私密备注",
                            "en_us": "Private notes"
                        },
                        "select_status": 0
                    }
                ],
                "business_management_scopes": [
                    {
                        "entity": {
                            "code": "application",
                            "name": {
                                "zh_cn": "投递",
                                "en_us": "Application"
                            }
                        },
                        "permission_groups": [
                            {
                                "permission_ids": [
                                    "6930815272790114324"
                                ],
                                "scope_rule": {
                                    "rule_type": 1
                                }
                            }
                        ]
                    }
                ]
            },
            "campus_permission_collection": {
                "feature_permissions": [
                    {
                        "id": "10101002",
                        "name": {
                            "zh_cn": "查看投递",
                            "en_us": "View application"
                        }
                    }
                ],
                "management_permissions": [
                    {
                        "id": "20101002",
                        "name": {
                            "zh_cn": "编辑权限",
                            "en_us": "Edit permissions"
                        }
                    }
                ],
                "data_permissions": [
                    {
                        "id": "30103001",
                        "name": {
                            "zh_cn": "操作记录",
                            "en_us": "Action history"
                        },
                        "select_status": 0
                    }
                ],
                "business_management_scopes": [
                    {
                        "entity": {
                            "code": "application",
                            "name": {
                                "zh_cn": "投递",
                                "en_us": "application"
                            }
                        },
                        "permission_groups": [
                            {
                                "permission_ids": [
                                    "6930815272790114324"
                                ],
                                "scope_rule": {
                                    "rule_type": 0
                                }
                            }
                        ]
                    }
                ]
            }
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
  <md-td>500</md-td>
  <md-td>1002001</md-td>
  <md-td>系统错误</md-td>
  <md-td>请根据实际报错信息定位或[联系客服](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952&extra=%7B%22channel%22:14,%22created_at%22:1614493146,%22scenario_id%22:6885151765134622721,%22signature%22:%22ca94c408b966dc1de2083e5bbcd418294c146e98%22%7D)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002002</md-td>
  <md-td>参数错误</md-td>
  <md-td>检查参数是否正确，例如类型、大小</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002352</md-td>
  <md-td>角色不存在</md-td>
  <md-td>请检查入参`role_id`是否正确，role_id可通过接口 [获取角色列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/role/list)获取</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




