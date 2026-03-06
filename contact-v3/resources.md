---
title: "通讯录概述"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/resources"
updateTime: "1721359947000"
---

# 通讯录概述

你可以将通讯录理解为企业组织架构，包含了企业部门信息、企业人员信息等。开放平台针对飞书通讯录提供了一系列安全可靠的接口（API），便于你管理通讯录数据。例如使用通讯录 API 可实现的操作有：

- 查看企业的组织架构
- 为企业创建新的用户
- 修改企业中已有用户的基本属性
- 维护用户和部门的关联关系
- 维护用户和用户组的关联关系

## 典型案例

开放平台提供了包含通讯录业务的集成方案，详情参见[HR 系统集成飞书，“入转调离”管理更轻松](https://open.feishu.cn/solutions/detail/hr)。

##  接入流程

通讯录 API 的基本接入流程如下图所示，如需了解详细的 API 接入流程，参见[流程概述](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)。

![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/7e2c712313cbc2da9b298804cbcf94e2_yZOtP0cS3V.png?height=214&lazyload=true&maxWidth=700&width=2276)

## 开发教程

体验场景化示例教程，了解如何运用通讯录 API 管理企业组织架构。详情参见[将企业组织架构同步到飞书](https://open.larkoffice.com/document/home/synchronize-corporate-organizational-structure-to-feishu/synchronize-corporate-organizational-structure-to-feishu)。

![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/316b9cb34d7c2b8d8e2c4037e211ecc0_Z0ZQpT2PZY.png?height=400&lazyload=true&maxWidth=600&width=752)

## 资源介绍

通讯录业务域以资源为中心进行开发。通讯录聚合了用户、用户组、部门、角色以及人员类型等多种资源，资源关系图如下所示。

![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/c0654fda770a895506dbdbd66356cacb_wtYdEdJ7qO.png?height=1260&lazyload=true&maxWidth=600&width=2098)

通讯录业务域包含的资源以及资源定义如下表：


| 资源 | 定义 |
| --- | --- |
| [用户](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/field-overview) | 用户即企业内的一个成员。通讯录的用户资源包含唯一标识（ID）、名称、性别和邮箱等基本信息，还包含用户所属的部门、自定义字段等信息。 |
| [部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview) | 部门是指企业组织架构树上的某一个节点。在部门内部，可添加用户作为部门成员，可添加新的部门建立父子层级关系。 |
| [用户组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/overview) | 用户组是部门资源之外的一种用户圈定方式。你可以通过用户组关联用户或部门，并在各类业务权限管控中引用用户组，从而实现高效便捷的成员权限管控。 |
| [用户组成员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/overview) | 用户组成员是指用户组内包含的用户、部门。 |
| [单位](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/overview) | 单位用于代表大型企业中的子公司、分支机构的实体。目前单位资源的主要作用是，在单个租户内的部分用户权限上实现“子公司”级别的权限隔离。 |
| [角色](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role/resource-introduction) | 角色用于设置用户的类型，例如人事、行政、法务、IT 等。目前通讯录的角色主要用于审批场景，企业在设计审批流程时，可以指定某种角色作为审批人。 |
| [角色成员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role-member/resource-introduction) | 角色成员是指同一角色内的用户列表以及管理范围。 |
| [人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/overview) | 人员类型是一种特殊的用户属性字段，用于标记用户的身份类型。例如正式、实习、外包、劳务、顾问。 |
| [自定义用户字段](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/custom_attr/overview) | 自定义用户字段的作用是方便企业基于自身的管理诉求，灵活设计用户信息。使用通讯录 API，你可以获取企业所有的自定义字段信息。 |
| [权限范围](https://open.larkoffice.com/document/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority) | 这里的权限范围是指应用的通讯录权限范围，即应用通过通讯录接口可以操作的组织架构数据范围。使用通讯录 API，你可以获取应用的通讯录权限范围。 |
| [职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/create) | 职位等级是用户属性字段。企业可根据组织架构实际情况来自定义管理职级信息。 |
| [序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/create) | 序列是用户属性字段。企业可根据组织架构实际情况来自定义管理序列信息。 |
| [职务](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_title/get) | 用户属性字段。通讯录业务域提供了职务相关的查询接口。 |
| [工作城市](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/work_city/get) | 用户属性字段。通讯录业务域进提供了工作城市相关的查询接口。 |


## 方法列表

以下提供了通讯录业务域内所有资源的 API 和事件列表。

:::note
文中表格涉及的 **商店** 是指商店应用，**自建** 是指企业自建应用。应用类型说明参见[应用类型简介](https://open.larkoffice.com/document/home/app-types-introduction/overview)。
:::

### 用户

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [创建用户](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/create) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [删除用户](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/delete) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [恢复已删除用户](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/resurrect) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [修改用户部分信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/patch) | `contact:contact` 更新通讯录 `contact:user.base` 更新用户基本信息 | `tenant_access_token` `user_access_token` | **X** | **✓** |
| [获取单个用户信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/get) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [批量获取用户信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch) | `contact:contact.base:readonly` 获取通讯录基本信息 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [获取部门直属用户列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/find_by_department) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [通过手机号或邮箱获取用户ID](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch_get_id) | `contact:user.id:readonly` 通过手机号或邮箱获取用户 ID | `tenant_access_token` | **✓** | **✓** |
| [搜索用户](https://open.larkoffice.com/document/ukTMukTMukTM/uMTM4UjLzEDO14yMxgTN) | `contact:user:search` 搜索用户 | `user_access_token` | **✓** | **✓** |
| [更新用户ID](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/update_user_id) | `contact:contact:update_user_id` 更新用户 ID | `tenant_access_token` | **X** | **✓** |


#### 事件列表


| **[事件 (Event)](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)** | 权限要求（满足任一） | 事件类型 | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [员工入职](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/events/created) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.user.created_v3 | **✓** | **✓** |
| [员工离职](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/events/deleted) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.user.deleted_v3 | **✓** | **✓** |
| [员工信息被修改](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/events/updated) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.user.updated_v3 | **✓** | **✓** |


### 部门

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [创建部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/create) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [删除部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/delete) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [修改部门部分信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/patch) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [更新部门所有信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/update) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [部门群转为普通群](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/unbind_department_chat) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [获取单个部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/get) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [批量获取部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/batch) | `contact:contact.base:readonly` 获取通讯录基本信息 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [获取子部门列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/children) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [获取父部门信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/parent) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [搜索部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/search) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `user_access_token` | **✓** | **✓** |
| [更新部门ID](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/update_department_id) | `contact:contact:update_department_id` 更新部门 ID | `tenant_access_token` | **X** | **✓** |


#### 事件列表


| **[事件 (Event)](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)** | 权限要求（满足任一） | 事件类型 | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [部门信息被修改](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/events/updated) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.department.updated_v3 | **✓** | **✓** |
| [部门被创建](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/events/created) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.department.created_v3 | **✓** | **✓** |
| [部门被删除](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/events/deleted) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.department.deleted_v3 | **✓** | **✓** |


### 用户组

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [创建用户组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/create) | `contact:group` 更新用户组信息 | `tenant_access_token` | **X** | **✓** |
| [更新用户组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/patch) | `contact:group` 更新用户组信息 | `tenant_access_token` | **X** | **✓** |
| [删除用户组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/delete) | `contact:group` 更新用户组信息 | `tenant_access_token` | **X** | **✓** |
| [查询指定用户组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/get) | `contact:group:readonly` 获取用户组信息 | `tenant_access_token` | **✓** | **✓** |
| [查询用户组列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/simplelist) | `contact:group:readonly` 获取用户组信息 | `tenant_access_token` | **✓** | **✓** |
| [查询用户所属用户组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/member_belong) | `contact:group:readonly` 获取用户组信息 | `tenant_access_token` | **✓** | **✓** |


### 用户组成员

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [添加用户组成员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/add) | `contact:group` 更新用户组信息 | `tenant_access_token` | **X** | **✓** |
| [批量添加用户组成员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/batch_add) | `contact:group` 更新用户组信息 | `tenant_access_token` | **X** | **✓** |
| [移除用户组成员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/remove) | `contact:group` 更新用户组信息 | `tenant_access_token` | **X** | **✓** |
| [批量移除用户组成员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/batch_remove) | `contact:group` 更新用户组信息 | `tenant_access_token` | **X** | **✓** |
| [查询用户组成员列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/simplelist) | `contact:group:readonly` 获取用户组信息 | `tenant_access_token` | **✓** | **✓** |


### 单位

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [创建单位](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/create) | `contact:unit` 更新单位信息 | `tenant_access_token` | **X** | **✓** |
| [修改单位信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/patch) | `contact:unit` 更新单位信息 | `tenant_access_token` | **X** | **✓** |
| [删除单位](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/delete) | `contact:unit` 更新单位信息 | `tenant_access_token` | **X** | **✓** |
| [获取单位信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/get) | `contact:unit:readonly` 获取单位信息 | `tenant_access_token` | **X** | **✓** |
| [批量获取单位列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/list) | `contact:unit:readonly` 获取单位信息 | `tenant_access_token` | **X** | **✓** |
| [建立部门与单位的绑定关系](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/bind_department) | `contact:unit` 更新单位信息 | `tenant_access_token` | **X** | **✓** |
| [解除部门与单位的绑定关系](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/unbind_department) | `contact:unit` 更新单位信息 | `tenant_access_token` | **X** | **✓** |
| [获取单位绑定的部门列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/list_department) | `contact:unit:readonly` 获取单位信息 | `tenant_access_token` | **X** | **✓** |


### 角色

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [创建角色](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role/create) | `contact:functional_role` 查看、创建、修改、删除角色及角色成员 | `tenant_access_token` | **X** | **✓** |
| [删除角色](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role/delete) | `contact:functional_role` 查看、创建、修改、删除角色及角色成员 | `tenant_access_token` | **X** | **✓** |
| [修改角色名称](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role/update) | `contact:functional_role` 查看、创建、修改、删除角色及角色成员 | `tenant_access_token` | **X** | **✓** |


### 角色成员

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [批量添加角色成员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role-member/batch_create) | `contact:functional_role` 查看、创建、修改、删除角色及角色成员 | `tenant_access_token` | **X** | **✓** |
| [删除角色下的成员](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role-member/batch_delete) | `contact:functional_role` 查看、创建、修改、删除角色及角色成员 | `tenant_access_token` | **X** | **✓** |
| [批量设置角色成员管理范围](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role-member/scopes) | `contact:functional_role` 查看、创建、修改、删除角色及角色成员 | `tenant_access_token` | **X** | **✓** |
| [查询角色下某个成员的管理范围](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role-member/get) | `contact:functional_role` 查看、创建、修改、删除角色及角色成员 `contact:functional_role:readonly` 查询角色信息、角色下的成员信息 | `tenant_access_token` | **X** | **✓** |
| [查询角色下的所有成员信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/functional_role-member/list) | `contact:functional_role` 查看、创建、修改、删除角色及角色成员 `contact:functional_role:readonly` 查询角色信息、角色下的成员信息 | `tenant_access_token` | **X** | **✓** |


### 人员类型

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [新增人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/create) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [查询人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` | **✓** | **✓** |
| [更新人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/update) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |
| [删除人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/delete) | `contact:contact` 更新通讯录 | `tenant_access_token` | **X** | **✓** |


#### 事件列表


| **[事件 (Event)](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)** | 权限要求（满足任一） | 事件类型 | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [新建人员类型事件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/events/created) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.employee_type_enum.created_v3 | **✓** | **✓** |
| [启用人员类型事件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/events/actived) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.employee_type_enum.actived_v3 | **✓** | **✓** |
| [停用人员类型事件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/events/deactivated) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.employee_type_enum.deactivated_v3 | **✓** | **✓** |
| [修改人员类型名称事件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/events/updated) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.employee_type_enum.updated_v3 | **✓** | **✓** |
| [删除人员类型事件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/events/deleted) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.employee_type_enum.deleted_v3 | **✓** | **✓** |


### 自定义用户字段


#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [获取企业自定义用户字段](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/custom_attr/list) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` | **✓** | **✓** |


#### 事件列表


| **[事件 (Event)](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)** | 权限要求（满足任一） | 事件类型 | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [成员字段变更](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/custom_attr_event/events/updated) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.custom_attr_event.updated_v3 | **✓** | **✓** |


### 通讯录权限范围

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [获取通讯录授权范围](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/custom_attr_event/events/updated) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` | **✓** | **✓** |


#### 事件列表


| **[事件 (Event)](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)** | 权限要求（满足任一） | 事件类型 | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [通讯录范围权限被变更](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/scope/events/updated) | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | contact.scope.updated_v3 | **✓** | **✓** |


### 职级

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [创建职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/create) | `contact:contact` 更新通讯录 `contact:job_level` 创建、删除、更新职级 | `tenant_access_token` | **X** | **✓** |
| [删除职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/delete) | `contact:contact` 更新通讯录 `contact:job_level` 创建、删除、更新职级 | `tenant_access_token` | **X** | **✓** |
| [更新职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/update) | `contact:contact` 更新通讯录 `contact:job_level` 创建、删除、更新职级 | `tenant_access_token` | **X** | **✓** |
| [获取单个职级信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/get) | `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:job_level` 创建、删除、更新职级 `contact:job_level:readonly` 查询职级列表 | `tenant_access_token` | **✓** | **✓** |
| [获取租户职级列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_level/list) | `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:job_level` 创建、删除、更新职级 `contact:job_level:readonly` 查询职级列表 | `tenant_access_token` | **✓** | **✓** |


### 序列

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [创建序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/create) | `contact:contact` 更新通讯录 `contact:job_family` 创建、删除、更新租户的工作序列 | `tenant_access_token` | **X** | **✓** |
| [删除序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/delete) | `contact:contact` 更新通讯录 `contact:job_family` 创建、删除、更新租户的工作序列 | `tenant_access_token` | **X** | **✓** |
| [更新序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/update) | `contact:contact` 更新通讯录 `contact:job_family` 创建、删除、更新租户的工作序列 | `tenant_access_token` | **X** | **✓** |
| [获取单个序列信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/get) | `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:job_family` 创建、删除、更新租户的工作序列 `contact:job_family:readonly` 查询租户下工作序列的详细信息 | `tenant_access_token` | **✓** | **✓** |
| [获取租户序列列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_family/list) | `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:job_family` 创建、删除、更新租户的工作序列 `contact:job_family:readonly` 查询租户下工作序列的详细信息 | `tenant_access_token` | **✓** | **✓** |


### 职务

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [获取单个职务信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_title/get) | `contact:job_title:readonly` 获取职务列表 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [获取租户职务列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/job_title/list) | `contact:job_title:readonly` 获取职务列表 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` `user_access_token` | **✓** | **✓** |


### 工作城市

#### API 列表


| **[方法 (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | 权限要求（满足任一） | **[访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)（选择其一）** | 商店 | 自建 |
| --- | --- | --- | --- | --- |
| [获取单个工作城市信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/work_city/get) | `contact:work_city:readonly` 获取工作城市列表 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` `user_access_token` | **✓** | **✓** |
| [获取租户工作城市列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/work_city/list) | `contact:work_city:readonly` 获取工作城市列表 `contact:contact:readonly_as_app` 以应用身份读取通讯录 | `tenant_access_token` `user_access_token` | **✓** | **✓** |

