---
title: "通讯录权限范围变更"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/scope/events/updated"
updateTime: "1743142527000"
---

# 通讯录权限范围变更

当应用订阅该事件后，如果应用的通讯录权限范围发生变更，则会触发该事件。{使用示例}(url=/api/tools/api_explore/api_explore_config?project=contact&version=v3&resource=scope&event=updated)


## 前提条件

你需要在应用中配置事件订阅，这样才可以在事件触发时接收到事件数据。了解事件订阅可参见[事件订阅概述](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)。

## 事件

| 项目 | 值 |
| --- | --- |
| 事件类型 | contact.scope.updated_v3 |
| 支持的应用类型 | custom,isv |
| 权限要求             订阅该事件所需的权限，开启其中任意一项权限即可订阅 开启任一权限即可 | `contact:contact.base:readonly` 获取通讯录基本信息 `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:contact:access_as_app` 以应用身份访问通讯录 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:user.assign_info:read` 查询用户席位信息 `contact:user.base:readonly` 获取用户基本信息 `contact:user.department:readonly` 获取用户组织架构信息 `contact:user.department_path:readonly` 获取成员所在部门路径 `contact:user.employee:readonly` 获取用户受雇信息 `contact:user.employee_number:read` 查看成员工号 `contact:user.gender:readonly` 获取用户性别 `contact:user.subscription_ids:write` 分配用户席位 `contact:user.employee_id:readonly` 获取用户 user ID `contact:user.phone:readonly` 获取用户手机号 `contact:user.email:readonly` 获取用户邮箱信息 `contact:user.job_family:readonly` 查询用户所属的工作序列 `contact:user.job_level:readonly` 查询用户职级 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| 推送方式 | `Webhook` |


### 事件体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `schema` | `string` | 事件模式 |
| `header` | `event_header` | 事件头 |
| &nbsp;&nbsp;└ `event_id` | `string` | 事件 ID |
| &nbsp;&nbsp;└ `event_type` | `string` | 事件类型 |
| &nbsp;&nbsp;└ `create_time` | `string` | 事件创建时间戳（单位：毫秒） |
| &nbsp;&nbsp;└ `token` | `string` | 事件 Token |
| &nbsp;&nbsp;└ `app_id` | `string` | 应用 ID |
| &nbsp;&nbsp;└ `tenant_key` | `string` | 租户 Key |
| `event` | `\-` | \- |
| &nbsp;&nbsp;└ `added` | `scope` | 当通讯录权限范围变更时，新增的对象信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `departments` | `department\[\]` | 部门对象信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 部门名称。<br>**数据校验规则**：<br>- 最小长度：`1` 字符<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `department_i18n_name` | 国际化的部门名称。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 部门的中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 部门的日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 部门的英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_department_id` | `string` | 父部门的 ID。取值为 0 表示当前部门的父部门为根部门。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 当前部门的自定义部门 ID。<br>**数据校验规则**：<br>- 最大长度：`64` 字符<br>- 正则校验：`^[a-zA-Z0-9][a-zA-Z0-9_\-@.]{0,63}$`<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_department_id` | `string` | 部门的 open_department_id。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leader_user_id` | `string` | 部门主管的 open_id。关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `chat_id` | `string` | 部门群 ID。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `order` | `string` | 部门的排序，即部门在其同级部门的展示顺序。取值越小排序越靠前。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `unit_ids` | `string\[\]` | 部门单位的自定义 ID 列表。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `member_count` | `int` | 部门下用户的个数。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `department_status` | 部门状态。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_deleted` | `boolean` | 是否被删除。<br>**可能值：**<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leaders` | `departmentLeader\[\]` | 部门负责人信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leaderType` | `int` | 负责人类型。<br>**可选值有**：<br>- `1`: 主负责人。 - `2`: 副负责人。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leaderID` | `string` | 负责人的用户 open_id。了解用户 ID 可参见[用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `group_chat_employee_types` | `int\[\]` | 部门群雇员类型限制。当该字段列表为空时，表示为无任何雇员类型。类型字段可包含以下值：<br>- 1：正式员工 - 2：实习生 - 3：外包 - 4：劳务 - 5：顾问 - 6：其他自定义类型字段。你可以调用[获取人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)接口，获取到该租户的自定义员工类型的名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `primary_member_count` | `int` | 部门下主属用户的个数。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `users` | `user\[\]` | 用户对象信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union_id，应用开发商发布的不同应用中同一用户的标识。关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user_id，租户内用户的唯一标识。关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open_id，应用内用户的唯一标识。关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名。<br>**数据校验规则**：<br>- 最小长度：`1` 字符<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `nickname` | `string` | 别名。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱。<br>**字段权限要求**： `contact:user.email:readonly` 获取用户邮箱信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号。<br>**字段权限要求**： `contact:user.phone:readonly` 获取用户手机号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `int` | 性别。<br>**可选值有**：<br>- `0`: 保密。 - `1`: 男。 - `2`: 女。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.gender:readonly` 获取用户性别 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar` | `avatar_info` | 用户头像信息。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_72` | `string` | 72*72 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_240` | `string` | 240*240 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_640` | `string` | 640*640 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_origin` | `string` | 原始头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `user_status` | 用户状态。通过 is_frozen、is_resigned、is_activated、is_exited 布尔值类型参数进行展示。<br>用户状态的转关逻辑可参见[用户资源介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/field-overview#4302b5a1)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_frozen` | `boolean` | 是否为暂停状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_resigned` | `boolean` | 是否为离职状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_activated` | `boolean` | 是否为激活状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_exited` | `boolean` | 是否为主动退出状态。主动退出一段时间后用户状态会自动转为已离职。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_unjoin` | `boolean` | 是否为未加入状态，需要用户自主确认才能加入企业或团队。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leader_user_id` | `string` | 用户的直接主管的 open_id。<br>关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.department:readonly` 获取用户组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 工作城市。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家或地区 Code 缩写。具体格式可参见 [国家/地区码表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/country-code-description)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_station` | `string` | 工位。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `join_time` | `int` | 入职时间。秒级时间戳格式，表示从 1970 年 1 月 1 日开始所经过的秒数。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_no` | `string` | 工号。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:user.employee_number:read` 查看成员工号 `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type` | `int` | 员工类型。<br>**可能值有：** - `1`：正式员工 - `2`：实习生 - `3`：外包 - `4`：劳务 - `5`：顾问   <br>同时可读取到自定义员工类型的 int 值，通过 int 值调用[获取人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)接口，进而获取到该租户的自定义员工类型的名称。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_attrs` | `user_custom_attr\[\]` | 自定义字段。如果企业管理员已在管理后台 > 组织架构 > 成员字段管理 > 自定义字段管理 > 全局设置中开启了 **允许开放平台 API 调用**，则该字段生效。<br>更多信息可参见[用户接口相关问题](https://open.larkoffice.com/document/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN#77061525)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 自定义字段类型。<br>**可能值有：** - `TEXT`：文本 - `HREF`：网页 - `ENUMERATION`：枚举 - `PICTURE_ENUM`：图片 - `GENERIC_USER`：用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 自定义字段 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `user_custom_attr_value` | 自定义字段取值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | - 字段类型为 TEXT 时，该参数返回定义的字段值。 - 字段类型为 HREF 时，该参数返回定义的网页标题。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 字段类型为 HREF 时，该参数返回定义的默认 URL。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_url` | `string` | 字段类型为 HREF 时，如果为 PC 端设置了 URL，则该参数返回定义的 PC 端 URL。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_id` | `string` | 字段类型为 `ENUMERATION` 或 `PICTURE_ENUM` 时，该参数返回定义的选项 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_value` | `string` | 选项类型的值，即用户详情或自定义字段中选中的选项值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 选项类型为图片时，图片的名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `picture_url` | `string` | 选项类型为图片时，图片的链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `generic_user` | `custom_attr_generic_user` | 字段类型为 `GENERIC_USER` 时，该参数返回定义的引用人员信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 引用人员的 user_id。关于用户 ID 的具体说明可参见[用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 用户类型。目前固定取值为 1，表示用户。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enterprise_email` | `string` | 企业邮箱。如果企业管理员已在管理后台启用飞书邮箱服务，则会返回该值。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_title` | `string` | 职务。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_frozen` | `boolean` | 是否为暂停状态的用户。<br>**可能值有：**<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID。<br>**字段权限要求**： `contact:user.job_level:readonly` 查询用户职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID。<br>**字段权限要求**： `contact:user.job_family:readonly` 查询用户所属的工作序列 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `subscription_ids` | `string\[\]` | 分配给用户的席位 ID 列表。需开通 **分配用户席位** 权限。<br>**字段权限要求**： `contact:user.subscription_ids:write` 分配用户席位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assign_info` | `user_assign_info\[\]` | 用户席位列表。<br>**字段权限要求**： `contact:user.assign_info:read` 查询用户席位信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `subscription_id` | `string` | 席位 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `license_plan_key` | `string` | 席位的许可证（license plan key）。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `product_name` | `string` | 席位名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `product_i18n_name` | 国际化名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 席位中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 席位日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 席位英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 席位起始时间。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 席位结束时间。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_path` | `department_detail\[\]` | 部门路径。<br>**字段权限要求**： `contact:user.department_path:readonly` 获取成员所在部门路径 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_name` | `department_path_name` | 部门名称信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 部门名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `department_i18n_name` | 部门国际化名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 部门的中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 部门的日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 部门的英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_path` | `department_path` | 部门路径。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 部门路径 ID 列表。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_path_name` | `department_path_name` | 部门路径名字。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 部门名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `department_i18n_name` | 部门国际化名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 部门的中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 部门的日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 部门的英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_groups` | `user_group\[\]` | 用户组对象。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_group_id` | `string` | 用户组的自定义 ID。<br>**数据校验规则**：<br>- 长度范围：`1` ～ `64` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户组的名称。<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 用户组的类型。<br>**可选值有**：<br>- `1`: 普通用户组。 - `2`: 动态用户组。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `member_count` | `int` | 成员数量。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 用户组状态。<br>**可选值有**：<br>- `0`: 未知。 - `1`: 计算完毕。 - `2`: 计算中。 - `3`: 计算失败。 |
| &nbsp;&nbsp;└ `removed` | `scope` | 当通讯录权限范围发生变更时，移除的对象信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `departments` | `department\[\]` | 部门对象信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 部门名称。<br>**数据校验规则**：<br>- 最小长度：`1` 字符<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `department_i18n_name` | 国际化的部门名称。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 部门的中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 部门的日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 部门的英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_department_id` | `string` | 父部门的 ID。取值为 0 表示当前部门的父部门为根部门。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 当前部门的自定义部门 ID。<br>**数据校验规则**：<br>- 最大长度：`64` 字符<br>- 正则校验：`^[a-zA-Z0-9][a-zA-Z0-9_\-@.]{0,63}$`<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_department_id` | `string` | 部门的 open_department_id。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leader_user_id` | `string` | 部门主管的 open_id。关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `chat_id` | `string` | 部门群 ID。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `order` | `string` | 部门的排序，即部门在其同级部门的展示顺序。取值越小排序越靠前。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `unit_ids` | `string\[\]` | 部门单位的自定义 ID 列表。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `member_count` | `int` | 部门下用户的个数。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `department_status` | 部门状态。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.base:readonly` 获取部门基础信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_deleted` | `boolean` | 是否被删除。<br>**可能值：**<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leaders` | `departmentLeader\[\]` | 部门负责人信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leaderType` | `int` | 负责人类型。<br>**可选值有**：<br>- `1`: 主负责人。 - `2`: 副负责人。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leaderID` | `string` | 负责人的用户 open_id。了解用户 ID 可参见[用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `group_chat_employee_types` | `int\[\]` | 部门群雇员类型限制。当该字段列表为空时，表示为无任何雇员类型。类型字段可包含以下值：<br>- 1：正式员工 - 2：实习生 - 3：外包 - 4：劳务 - 5：顾问 - 6：其他自定义类型字段。你可以调用[获取人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)接口，获取到该租户的自定义员工类型的名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `primary_member_count` | `int` | 部门下主属用户的个数。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:department.organize:readonly` 获取通讯录部门组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `users` | `user\[\]` | 用户对象信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union_id，应用开发商发布的不同应用中同一用户的标识。关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user_id，租户内用户的唯一标识。关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open_id，应用内用户的唯一标识。关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名。<br>**数据校验规则**：<br>- 最小长度：`1` 字符<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `nickname` | `string` | 别名。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱。<br>**字段权限要求**： `contact:user.email:readonly` 获取用户邮箱信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号。<br>**字段权限要求**： `contact:user.phone:readonly` 获取用户手机号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `int` | 性别。<br>**可选值有**：<br>- `0`: 保密。 - `1`: 男。 - `2`: 女。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.gender:readonly` 获取用户性别 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar` | `avatar_info` | 用户头像信息。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_72` | `string` | 72*72 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_240` | `string` | 240*240 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_640` | `string` | 640*640 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_origin` | `string` | 原始头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `user_status` | 用户状态。通过 is_frozen、is_resigned、is_activated、is_exited 布尔值类型参数进行展示。<br>用户状态的转关逻辑可参见[用户资源介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/field-overview#4302b5a1)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_frozen` | `boolean` | 是否为暂停状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_resigned` | `boolean` | 是否为离职状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_activated` | `boolean` | 是否为激活状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_exited` | `boolean` | 是否为主动退出状态。主动退出一段时间后用户状态会自动转为已离职。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_unjoin` | `boolean` | 是否为未加入状态，需要用户自主确认才能加入企业或团队。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `leader_user_id` | `string` | 用户的直接主管的 open_id。<br>关于用户 ID 的说明可参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.department:readonly` 获取用户组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 工作城市。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家或地区 Code 缩写。具体格式可参见 [国家/地区码表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/country-code-description)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_station` | `string` | 工位。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `join_time` | `int` | 入职时间。秒级时间戳格式，表示从 1970 年 1 月 1 日开始所经过的秒数。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_no` | `string` | 工号。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:user.employee_number:read` 查看成员工号 `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type` | `int` | 员工类型。<br>**可能值有：** - `1`：正式员工 - `2`：实习生 - `3`：外包 - `4`：劳务 - `5`：顾问   <br>同时可读取到自定义员工类型的 int 值，通过 int 值调用[获取人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)接口，进而获取到该租户的自定义员工类型的名称。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_attrs` | `user_custom_attr\[\]` | 自定义字段。如果企业管理员已在管理后台 > 组织架构 > 成员字段管理 > 自定义字段管理 > 全局设置中开启了 **允许开放平台 API 调用**，则该字段生效。<br>更多信息可参见[用户接口相关问题](https://open.larkoffice.com/document/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN#77061525)。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 自定义字段类型。<br>**可能值有：** - `TEXT`：文本 - `HREF`：网页 - `ENUMERATION`：枚举 - `PICTURE_ENUM`：图片 - `GENERIC_USER`：用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 自定义字段 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `user_custom_attr_value` | 自定义字段取值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | - 字段类型为 TEXT 时，该参数返回定义的字段值。 - 字段类型为 HREF 时，该参数返回定义的网页标题。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 字段类型为 HREF 时，该参数返回定义的默认 URL。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_url` | `string` | 字段类型为 HREF 时，如果为 PC 端设置了 URL，则该参数返回定义的 PC 端 URL。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_id` | `string` | 字段类型为 `ENUMERATION` 或 `PICTURE_ENUM` 时，该参数返回定义的选项 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_value` | `string` | 选项类型的值，即用户详情或自定义字段中选中的选项值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 选项类型为图片时，图片的名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `picture_url` | `string` | 选项类型为图片时，图片的链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `generic_user` | `custom_attr_generic_user` | 字段类型为 `GENERIC_USER` 时，该参数返回定义的引用人员信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 引用人员的 user_id。关于用户 ID 的具体说明可参见[用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 用户类型。目前固定取值为 1，表示用户。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enterprise_email` | `string` | 企业邮箱。如果企业管理员已在管理后台启用飞书邮箱服务，则会返回该值。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_title` | `string` | 职务。<br>**字段权限要求（满足任一）**： `contact:contact:readonly_as_app` 以应用身份读取通讯录 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_frozen` | `boolean` | 是否为暂停状态的用户。<br>**可能值有：**<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID。<br>**字段权限要求**： `contact:user.job_level:readonly` 查询用户职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID。<br>**字段权限要求**： `contact:user.job_family:readonly` 查询用户所属的工作序列 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `subscription_ids` | `string\[\]` | 分配给用户的席位 ID 列表。需开通 **分配用户席位** 权限。<br>**字段权限要求**： `contact:user.subscription_ids:write` 分配用户席位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `assign_info` | `user_assign_info\[\]` | 用户席位列表。<br>**字段权限要求**： `contact:user.assign_info:read` 查询用户席位信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `subscription_id` | `string` | 席位 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `license_plan_key` | `string` | 席位的许可证（license plan key）。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `product_name` | `string` | 席位名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `product_i18n_name` | 国际化名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 席位中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 席位日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 席位英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 席位起始时间。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 席位结束时间。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_path` | `department_detail\[\]` | 部门路径。<br>**字段权限要求**： `contact:user.department_path:readonly` 获取成员所在部门路径 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_name` | `department_path_name` | 部门名称信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 部门名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `department_i18n_name` | 部门国际化名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 部门的中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 部门的日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 部门的英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_path` | `department_path` | 部门路径。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 部门路径 ID 列表。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_path_name` | `department_path_name` | 部门路径名字。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 部门名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `department_i18n_name` | 部门国际化名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 部门的中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 部门的日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 部门的英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_groups` | `user_group\[\]` | 用户组对象。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_group_id` | `string` | 用户组的自定义 ID。<br>**数据校验规则**：<br>- 长度范围：`1` ～ `64` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户组的名称。<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 用户组的类型。<br>**可选值有**：<br>- `1`: 普通用户组。 - `2`: 动态用户组。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `member_count` | `int` | 成员数量。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 用户组状态。<br>**可选值有**：<br>- `0`: 未知。 - `1`: 计算完毕。 - `2`: 计算中。 - `3`: 计算失败。 |


### 事件体示例

```json
{
    "schema": "2.0",
    "header": {
        "event_id": "5e3702a84e847582be8db7fb73283c02",
        "event_type": "contact.scope.updated_v3",
        "create_time": "1608725989000",
        "token": "rvaYgkND1GOiu5MM0E1rncYC6PLtF7JV",
        "app_id": "cli_9f5343c580712544",
        "tenant_key": "2ca1d211f64f6438"
    },
    "event": {
        "added": {
            "departments": [
                {
                    "name": "DemoName",
                    "i18n_name": {
                        "zh_cn": "Demo名称",
                        "ja_jp": "デモ名",
                        "en_us": "Demo Name"
                    },
                    "parent_department_id": "D067",
                    "department_id": "D096",
                    "open_department_id": "od-4e6ac4d14bcd5071a37a39de902c7141",
                    "leader_user_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
                    "chat_id": "oc_5ad11d72b830411d72b836c20",
                    "order": "100",
                    "unit_ids": [
                        "custom_unit_id"
                    ],
                    "member_count": 100,
                    "status": {
                        "is_deleted": false
                    },
                    "leaders": [
                        {
                            "leaderType": 1,
                            "leaderID": "ou_7dab8a3d3cdcc9da365777c7ad535d62"
                        }
                    ],
                    "group_chat_employee_types": [
                        1,2,3
                    ],
                    "primary_member_count": 100
                }
            ],
            "users": [
                {
                    "union_id": "on_94a1ee5551019f18cd73d9f111898cf2",
                    "user_id": "3e3cf96b",
                    "open_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
                    "name": "张三",
                    "en_name": "San Zhang",
                    "nickname": "Alex Zhang",
                    "email": "zhangsan@gmail.com",
                    "mobile": "130xxxx1111",
                    "gender": 1,
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
                    "leader_user_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
                    "city": "杭州",
                    "country": "CN",
                    "work_station": "北楼-H34",
                    "join_time": 2147483647,
                    "employee_no": "1",
                    "employee_type": 1,
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
                    "is_frozen": false,
                    "job_level_id": "mga5oa8ayjlp9rb",
                    "job_family_id": "mga5oa8ayjlp9rb",
                    "subscription_ids": [
                        "7179609168571645971"
                    ],
                    "assign_info": [
                        {
                            "subscription_id": "7079609167680782300",
                            "license_plan_key": "suite_enterprise_e5",
                            "product_name": "旗舰版 E5",
                            "i18n_name": {
                                "zh_cn": "zh_cn_name",
                                "ja_jp": "ja_jp_name",
                                "en_us": "en_name"
                            },
                            "start_time": "1674981000",
                            "end_time": "1674991000"
                        }
                    ],
                    "department_path": [
                        {
                            "department_id": "od-4e6ac4d14bcd5071a37a39de902c7141",
                            "department_name": {
                                "name": "测试部门名1",
                                "i18n_name": {
                                    "zh_cn": "Demo名称",
                                    "ja_jp": "デモ名",
                                    "en_us": "Demo Name"
                                }
                            },
                            "department_path": {
                                "department_ids": [
                                    "od-4e6ac4d14bcd5071a37a39de902c7141"
                                ],
                                "department_path_name": {
                                    "name": "测试部门名1",
                                    "i18n_name": {
                                        "zh_cn": "Demo名称",
                                        "ja_jp": "デモ名",
                                        "en_us": "Demo Name"
                                    }
                                }
                            }
                        }
                    ]
                }
            ],
            "user_groups": [
                {
                    "user_group_id": "test",
                    "name": "userGroupName",
                    "type": 1,
                    "member_count": 10,
                    "status": 1
                }
            ]
        },
        "removed": {
            "departments": [
                {
                    "name": "DemoName",
                    "i18n_name": {
                        "zh_cn": "Demo名称",
                        "ja_jp": "デモ名",
                        "en_us": "Demo Name"
                    },
                    "parent_department_id": "D067",
                    "department_id": "D096",
                    "open_department_id": "od-4e6ac4d14bcd5071a37a39de902c7141",
                    "leader_user_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
                    "chat_id": "oc_5ad11d72b830411d72b836c20",
                    "order": "100",
                    "unit_ids": [
                        "custom_unit_id"
                    ],
                    "member_count": 100,
                    "status": {
                        "is_deleted": false
                    },
                    "leaders": [
                        {
                            "leaderType": 1,
                            "leaderID": "ou_7dab8a3d3cdcc9da365777c7ad535d62"
                        }
                    ],
                    "group_chat_employee_types": [
                        1,2,3
                    ],
                    "primary_member_count": 100
                }
            ],
            "users": [
                {
                    "union_id": "on_94a1ee5551019f18cd73d9f111898cf2",
                    "user_id": "3e3cf96b",
                    "open_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
                    "name": "张三",
                    "en_name": "San Zhang",
                    "nickname": "Alex Zhang",
                    "email": "zhangsan@gmail.com",
                    "mobile": "130xxxx1111",
                    "gender": 1,
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
                    "leader_user_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
                    "city": "杭州",
                    "country": "CN",
                    "work_station": "北楼-H34",
                    "join_time": 2147483647,
                    "employee_no": "1",
                    "employee_type": 1,
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
                    "is_frozen": false,
                    "job_level_id": "mga5oa8ayjlp9rb",
                    "job_family_id": "mga5oa8ayjlp9rb",
                    "subscription_ids": [
                        "7179609168571645971"
                    ],
                    "assign_info": [
                        {
                            "subscription_id": "7079609167680782300",
                            "license_plan_key": "suite_enterprise_e5",
                            "product_name": "旗舰版 E5",
                            "i18n_name": {
                                "zh_cn": "zh_cn_name",
                                "ja_jp": "ja_jp_name",
                                "en_us": "en_name"
                            },
                            "start_time": "1674981000",
                            "end_time": "1674991000"
                        }
                    ],
                    "department_path": [
                        {
                            "department_id": "od-4e6ac4d14bcd5071a37a39de902c7141",
                            "department_name": {
                                "name": "测试部门名1",
                                "i18n_name": {
                                    "zh_cn": "Demo名称",
                                    "ja_jp": "デモ名",
                                    "en_us": "Demo Name"
                                }
                            },
                            "department_path": {
                                "department_ids": [
                                    "od-4e6ac4d14bcd5071a37a39de902c7141"
                                ],
                                "department_path_name": {
                                    "name": "测试部门名1",
                                    "i18n_name": {
                                        "zh_cn": "Demo名称",
                                        "ja_jp": "デモ名",
                                        "en_us": "Demo Name"
                                    }
                                }
                            }
                        }
                    ]
                }
            ],
            "user_groups": [
                {
                    "user_group_id": "test",
                    "name": "userGroupName",
                    "type": 1,
                    "member_count": 10,
                    "status": 1
                }
            ]
        }
    }
}
```


### 事件订阅示例代码

事件订阅流程可参考：[事件订阅概述](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)，新手入门可参考：[教程](https://open.larkoffice.com/document/uAjLw4CM/uMzNwEjLzcDMx4yM3ATM/develop-an-echo-bot/introduction)


`订阅方式`


长连接方式（推荐）：无需发布到公网地址，在本地开发环境中即可接收事件回调，且无需处理加解密逻辑。
发送至开发者服务器：需要提供服务器公网地址。


```
package main

import (
	"context"
	"fmt"

	larkcore "github.com/larksuite/oapi-sdk-go/v3/core"
	larkevent "github.com/larksuite/oapi-sdk-go/v3/event"
	"github.com/larksuite/oapi-sdk-go/v3/event/dispatcher"
	"github.com/larksuite/oapi-sdk-go/v3/service/contact/v3"
	larkws "github.com/larksuite/oapi-sdk-go/v3/ws"
)

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/golang-sdk-guide/preparations
func main() {
	// 注册事件 Register event
	eventHandler := dispatcher.NewEventDispatcher("", "").
		OnP2ScopeUpdatedV3(func(ctx context.Context, event *larkcontact.P2ScopeUpdatedV3) error {
			fmt.Printf("[ OnP2ScopeUpdatedV3 access ], data: %s\n", larkcore.Prettify(event))
			return nil
		})

	// 构建 client Build client
	cli := larkws.NewClient("YOUR_APP_ID", "YOUR_APP_SECRET",
		larkws.WithEventHandler(eventHandler),
		larkws.WithLogLevel(larkcore.LogLevelDebug),
	)

	// 建立长连接 Establish persistent connection
	err := cli.Start(context.Background())

	if err != nil {
		panic(err)
	}
}
```


```
# SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/python--sdk/preparations-before-development
import lark_oapi as lark


def do_p2_contact_scope_updated_v3(data: lark.contact.v3.P2ContactScopeUpdatedV3) -> None:
    print(f'[ do_p2_contact_scope_updated_v3 access ], data: {lark.JSON.marshal(data, indent=4)}')

# 注册事件 Register event
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_contact_scope_updated_v3(do_p2_contact_scope_updated_v3) \
    .build()


def main():
    # 构建 client Build client
    cli = lark.ws.Client("APP_ID", "APP_SECRET",
                        event_handler=event_handler, log_level=lark.LogLevel.DEBUG)
    # 建立长连接 Establish persistent connection
    cli.start()

if __name__ == "__main__":
    main()
```


```
package com.example.sample;

import com.lark.oapi.core.utils.Jsons;
import com.lark.oapi.service.contact.ContactService;
import com.lark.oapi.service.contact.v3.model.P2ScopeUpdatedV3;
import com.lark.oapi.event.EventDispatcher;
import com.lark.oapi.ws.Client;

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/java-sdk-guide/preparations
public class Sample {
    // 注册事件 Register event
    private static final EventDispatcher EVENT_HANDLER = EventDispatcher.newBuilder("", "")
            .onP2ScopeUpdatedV3(new ContactService.P2ScopeUpdatedV3Handler() {
                @Override
                public void handle(P2ScopeUpdatedV3 event) throws Exception {
                    System.out.printf("[ onP2ScopeUpdatedV3 access ], data: %s\n", Jsons.DEFAULT.toJson(event.getEvent()));
                }
            })
            .build();

    public static void main(String[] args) {
        // 构建 client Build client
        Client client = new Client.Builder("APP_ID", "APP_SECRET")
                .eventHandler(EVENT_HANDLER)
                .build();
        // 建立长连接 Establish persistent connection
        client.start();
    }
}
```


```
// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/nodejs-sdk/preparation-before-development
import * as Lark from '@larksuiteoapi/node-sdk';
const baseConfig = {
    appId: 'APP_ID',
    appSecret: 'APP_SECRET'
}
// 构建 client Build client
const wsClient = new Lark.WSClient(baseConfig);
// 建立长连接 Establish persistent connection
wsClient.start({
    // 注册事件 Register event
    eventDispatcher: new Lark.EventDispatcher({}).register({
        'contact.scope.updated_v3': async (data) => {
            console.log(data);
        }
    })
});
```


```
package main

import (
	"context"
	"fmt"
	"net/http"

	larkcore "github.com/larksuite/oapi-sdk-go/v3/core"
	"github.com/larksuite/oapi-sdk-go/v3/core/httpserverext"
	larkevent "github.com/larksuite/oapi-sdk-go/v3/event"
	"github.com/larksuite/oapi-sdk-go/v3/event/dispatcher"
	"github.com/larksuite/oapi-sdk-go/v3/service/contact/v3"
)

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/golang-sdk-guide/preparations
func main() {
	// 注册事件 Register event
	eventHandler := dispatcher.NewEventDispatcher("", "").
		OnP2ScopeUpdatedV3(func(ctx context.Context, event *larkcontact.P2ScopeUpdatedV3) error {
			fmt.Printf("[ OnP2ScopeUpdatedV3 access ], data: %s\n", larkcore.Prettify(event))
			return nil
		})

	// 创建路由处理器 Create route handler
	http.HandleFunc("/webhook/event", httpserverext.NewEventHandlerFunc(handler, larkevent.WithLogLevel(larkcore.LogLevelDebug)))

	err := http.ListenAndServe(":7777", nil)

	if err != nil {
		panic(err)
	}
}
```


```
# SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/python--sdk/preparations-before-development
from flask import Flask
from lark_oapi.adapter.flask import *
import lark_oapi as lark

app = Flask(__name__)


def do_p2_contact_scope_updated_v3(data: lark.contact.v3.P2ContactScopeUpdatedV3) -> None:
    print(f'[ do_p2_contact_scope_updated_v3 access ], data: {lark.JSON.marshal(data, indent=4)}')

# 注册事件 Register event
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_contact_scope_updated_v3(do_p2_contact_scope_updated_v3) \
    .build()


# 创建路由处理器 Create route handler
@app.route("/webhook/event", methods=["POST"])
def event():
    resp = event_handler.do(parse_req())
    return parse_resp(resp)

if __name__ == "__main__":
    app.run(port=7777)
```


```
package com.lark.oapi.sample.event;

import com.lark.oapi.core.utils.Jsons;
import com.lark.oapi.service.contact.ContactService;
import com.lark.oapi.service.contact.v3.model.P2ScopeUpdatedV3;
import com.lark.oapi.sdk.servlet.ext.ServletAdapter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/java-sdk-guide/preparations
@RestController
public class EventController {

    // 注册事件 Register event
    private static final EventDispatcher EVENT_HANDLER = EventDispatcher.newBuilder("verificationToken", "encryptKey")
            .onP2ScopeUpdatedV3(new ContactService.P2ScopeUpdatedV3Handler() {
                @Override
                public void handle(P2ScopeUpdatedV3 event) throws Exception {
                    System.out.printf("[ onP2ScopeUpdatedV3 access ], data: %s\n", Jsons.DEFAULT.toJson(event.getEvent()));
                }
            })
            .build();

    // 注入 ServletAdapter 实例 Inject ServletAdapter instance
    @Autowired
    private ServletAdapter servletAdapter;

    // 创建路由处理器 Create route handler
    @RequestMapping("/webhook/event")
    public void event(HttpServletRequest request, HttpServletResponse response)
            throws Throwable {
        // 回调扩展包提供的事件回调处理器 Callback handler provided by the extension package
        servletAdapter.handleEvent(request, response, EVENT_DISPATCHER);
    }
}
```


```
// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/nodejs-sdk/preparation-before-development
import http from 'http';
import * as lark from '@larksuiteoapi/node-sdk';

// 注册事件 Register event
const eventDispatcher = new lark.EventDispatcher({
    encryptKey: '',
    verificationToken: '',
}).register({
    'contact.scope.updated_v3': async (data) => {
        console.log(data);
        return 'success';
    },
});

const server = http.createServer();
// 创建路由处理器 Create route handler
server.on('request', lark.adaptDefault('/webhook/event', eventDispatcher));
server.listen(3000);
```

