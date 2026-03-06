---
title: "批量获取用户信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch"
updateTime: "1752559901000"
---

# 批量获取用户信息

调用该接口获取通讯录内一个或多个用户的信息，包括用户 ID、名称、邮箱、手机号、状态以及所属部门等信息。


## 注意事项

该查询接口目前不返回用户的席位（assign_info）和部门路径信息（department_path）。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/contact/v3/users/batch |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `contact:contact.base:readonly` 获取通讯录基本信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.assign_info:read` 查询用户席位信息 `contact:user.base:readonly` 获取用户基本信息 `contact:user.department:readonly` 获取用户组织架构信息 `contact:user.department_path:readonly` 获取成员所在部门路径 `contact:user.dotted_line_leader_info.read` 查看成员的虚线上级 ID `contact:user.employee:readonly` 获取用户受雇信息 `contact:user.employee_id:readonly` 获取用户 user ID `contact:user.employee_number:read` 查看成员工号 `contact:user.gender:readonly` 获取用户性别 `contact:user.user_geo` 查看成员数据驻留地 `contact:user.phone:readonly` 获取用户手机号 `contact:user.subscription_ids:write` 分配用户席位 `contact:user.email:readonly` 获取用户邮箱信息 `contact:user.job_family:readonly` 查询用户所属的工作序列 `contact:user.job_level:readonly` 查询用户职级 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_ids` | `string\[\]` | 是 | 用户ID。ID 类型与查询参数 `user_id_type` 保持一致。<br>如需一次查询多个用户ID，可多次传递同一参数名，并且每次传递不同的参数值。例如： `https://{url}?user_ids={user_id1}&user_ids={user_id2}`。<br>**说明**： - 单次最大请求可设置的用户 ID 数量上限为 50。 - 如上例子中的 `user_ids`是参数名，可以多次传递。`{user_id1}`和`{user_id2}`是每次传入的参数值。<br>**示例值**：7be5fg |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 指定查询结果中的部门 ID 类型。关于部门 ID 的详细介绍，可参见[部门 ID 说明](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0)。<br>**示例值**：open_department_id<br>**可选值有**：<br>- `open_department_id`: 由系统自动生成的部门 ID，ID 前缀固定为 `od-`，在租户内全局唯一。 - `department_id`: 支持用户自定义配置的部门 ID。自定义配置时可复用已删除的 department_id，因此在未删除的部门范围内 department_id 具有唯一性。<br>**默认值**：`open_department_id` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `user\[\]` | 查询到的用户信息。<br>**说明**：如有不在应用通讯录权限范围内的用户，则不会返回相应的信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union_id，是应用开发商发布的不同应用中同一用户的标识。不同用户 ID 的说明参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user_id，租户内用户的唯一标识。不同用户 ID 的说明参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open_id，应用内用户的唯一标识。不同用户 ID 的说明参见 [用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名。<br>**字段权限要求（满足任一）**： `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名。<br>**字段权限要求（满足任一）**： `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `nickname` | `string` | 别名。<br>**字段权限要求（满足任一）**： `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱。<br>**字段权限要求**： `contact:user.email:readonly` 获取用户邮箱信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号。<br>**字段权限要求**： `contact:user.phone:readonly` 获取用户手机号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_visible` | `boolean` | 手机号码是否可见。<br>**可能值有**：<br>- true：可见。 - false：不可见。不可见时，企业内的员工将无法查看该用户的手机号码。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `int` | 性别。<br>**可选值有**：<br>- `0`: 保密 - `1`: 男 - `2`: 女 - `3`: 其他<br>**字段权限要求（满足任一）**： `contact:user.gender:readonly` 获取用户性别 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_key` | `string` | 头像的文件 Key。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `avatar` | `avatar_info` | 用户头像信息。<br>**字段权限要求（满足任一）**： `contact:user.base:readonly` 获取用户基本信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_72` | `string` | 72*72 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_240` | `string` | 240*240 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_640` | `string` | 640*640 像素头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_origin` | `string` | 原始头像链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `user_status` | 用户状态。通过 is_frozen、is_resigned、is_activated、is_exited 布尔值类型参数进行展示。<br>用户状态的转关逻辑可参见[用户资源介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/field-overview#4302b5a1)。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_frozen` | `boolean` | 是否为暂停状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_resigned` | `boolean` | 是否为离职状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_activated` | `boolean` | 是否为激活状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_exited` | `boolean` | 是否为主动退出状态。主动退出一段时间后用户状态会自动转为已离职。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_unjoin` | `boolean` | 是否为未加入状态，需要用户自主确认才能加入企业或团队。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 用户所属部门的 ID 列表，一个用户可属于多个部门。ID 类型与查询参数 department_id_type 的取值保持一致。<br>**字段权限要求（满足任一）**： `contact:user.department:readonly` 获取用户组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `leader_user_id` | `string` | 用户的直接主管的用户ID。ID 类型与查询参数 user_id_type 的取值保持一致。<br>**字段权限要求（满足任一）**： `contact:user.department:readonly` 获取用户组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家或地区 Code 缩写，具体格式参考 [国家/地区 Code 参照表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/country-code-description)。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_station` | `string` | 工位。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `join_time` | `int` | 入职时间。秒级时间戳格式，表示从 1970 年 1 月 1 日开始所经过的秒数。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_tenant_manager` | `boolean` | 用户是否为租户超级管理员。<br>**可能值有**：<br>- true：是 - false：否<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_no` | `string` | 工号。<br>**字段权限要求（满足任一）**： `contact:user.employee_number:read` 查看成员工号 `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type` | `int` | 员工类型。<br>**可能值有**：<br>- 1：正式员工 - 2：实习生 - 3：外包 - 4：劳务 - 5：顾问   <br>同时支持自定义员工类型的 int 值。你可通过[获取人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)接口获取到当前租户内自定义员工类型的名称。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `orders` | `user_order\[\]` | 用户排序信息。用于标记通讯录下组织架构的人员顺序，人员可能存在多个部门中，且有不同的排序。<br>**字段权限要求（满足任一）**： `contact:user.department:readonly` 获取用户组织架构信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 排序信息对应的部门 ID，表示用户所在的、且需要排序的部门。ID 值的类型与查询参数 department_id_type 的取值保持一致。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_order` | `int` | 用户在其直属部门内的排序。数值越大，排序越靠前。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_order` | `int` | 用户所属的多个部门间的排序。数值越大，排序越靠前。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `is_primary_dept` | `boolean` | 标识是否为用户的唯一主部门。主部门为用户所属部门中排序第一的部门(department_order 最大)。<br>**可能值有**： - true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_attrs` | `user_custom_attr\[\]` | 自定义字段。了解自定义字段可参见[自定义字段资源介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/custom_attr/overview)。<br>**注意事项**：当企业管理员在管理后台配置了自定义字段，且开启了 **允许开放平台 API 调用** 功能后，该字段才会生效。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 自定义字段类型。<br>**可能值有**： - TEXT：文本 - HREF：网页 - ENUMERATION：枚举 - PICTURE_ENUM：图片 - GENERIC_USER：用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 自定义字段 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `user_custom_attr_value` | 自定义属性取值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | - 字段类型为 TEXT 时，该参数返回定义的字段值。 - 字段类型为 HREF 时，该参数返回定义的网页标题。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 字段类型为 HREF 时，该参数返回定义的默认 URL。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pc_url` | `string` | 字段类型为 HREF 时，该参数返回定义的 PC 端 URL。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_id` | `string` | 枚举类型中选项的选项 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `option_value` | `string` | 枚举类型中选项的选项值。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 图片类型中图片选项的名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `picture_url` | `string` | 图片类型中图片选项的链接。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `generic_user` | `custom_attr_generic_user` | 字段类型为 GENERIC_USER 时，该参数返回定义的引用人员。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 引用人员的用户 ID。ID 类型与查询参数 user_id_type 的取值保持一致。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 用户类型。目前固定为 1，表示用户类型。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enterprise_email` | `string` | 企业邮箱。        **注意事项**：企业管理员在管理后台启用飞书邮箱服务后，才会生效该参数。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_title` | `string` | 职务。<br>**字段权限要求（满足任一）**： `contact:user.employee:readonly` 获取用户受雇信息 `contact:contact:access_as_app` 以应用身份访问通讯录 `contact:contact:readonly` 读取通讯录 `contact:contact:readonly_as_app` 以应用身份读取通讯录 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_frozen` | `boolean` | 是否为暂停状态。<br>**可能值有**：<br>- true：是 - false：否 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `geo` | `string` | 数据驻留地。<br>**字段权限要求**： `contact:user.user_geo` 查看成员数据驻留地 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_level_id` | `string` | 职级 ID。<br>**字段权限要求**： `contact:user.job_level:readonly` 查询用户职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_family_id` | `string` | 序列 ID。<br>**字段权限要求**： `contact:user.job_family:readonly` 查询用户所属的工作序列 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subscription_ids` | `string\[\]` | 分配给用户的席位 ID 列表。<br>**注意** ：当前接口暂不会返回席位相关的数据。<br>**字段权限要求**： `contact:user.subscription_ids:write` 分配用户席位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assign_info` | `user_assign_info\[\]` | 用户席位列表。<br>**注意**：当前接口暂不会返回席位相关的数据。<br>**字段权限要求**： `contact:user.assign_info:read` 查询用户席位信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `subscription_id` | `string` | 席位 ID。<br>**注意**：当前接口暂不会返回席位相关的数据。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `license_plan_key` | `string` | 席位许可（License Plan Key）。<br>**注意**：当前接口暂不会返回席位相关的数据。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `product_name` | `string` | 席位名称。<br>**注意**：当前接口暂不会返回席位相关的数据。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `product_i18n_name` | 国际化名称。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 席位中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 席位日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 席位英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 席位起始时间。秒级时间戳格式。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 席位结束时间。秒级时间戳格式。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_path` | `department_detail\[\]` | 部门路径。<br>**注意**：当前接口暂不会返回部门路径数据。<br>**字段权限要求**： `contact:user.department_path:readonly` 获取成员所在部门路径 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门 ID。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_name` | `department_path_name` | 部门名称信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 部门名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `department_i18n_name` | 部门国际化名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 部门的中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 部门的日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 部门的英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_path` | `department_path` | 部门路径。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_ids` | `string\[\]` | 部门路径 ID 列表。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_path_name` | `department_path_name` | 部门路径名字信息。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 部门名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `department_i18n_name` | 部门国际化名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 部门的中文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 部门的日文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 部门的英文名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dotted_line_leader_user_ids` | `string\[\]` | 虚线上级的用户 ID。ID 类型与查询参数 user_id_type 的取值保持一致。<br>**字段权限要求**： `contact:user.dotted_line_leader_info.read` 查看成员的虚线上级 ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "union_id": "on_94a1ee5551019f18cd73d9f111898cf2",
                "user_id": "3e3cf96b",
                "open_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
                "name": "张三",
                "en_name": "San Zhang",
                "nickname": "Alex Zhang",
                "email": "zhangsan@gmail.com",
                "mobile": "13011111111",
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
                            "option_id": "option",
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
                "geo": "cn",
                "job_level_id": "mga5oa8ayjlp9rb",
                "job_family_id": "mga5oa8ayjlp9rb",
                "subscription_ids": [
                    "23213213213123123"
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
                                "zh_cn": "测试部门名1",
                                "ja_jp": "試験部署名 1",
                                "en_us": "Testing department name 1"
                            }
                        },
                        "department_path": {
                            "department_ids": [
                                "od-4e6ac4d14bcd5071a37a39de902c7141"
                            ],
                            "department_path_name": {
                                "name": "测试部门名1",
                                "i18n_name": {
                                    "zh_cn": "测试部门名1",
                                    "ja_jp": "試験部署名 1",
                                    "en_us": "Testing department name 1"
                                }
                            }
                        }
                    }
                ],
                "dotted_line_leader_user_ids": [
                    "ou_7dab8a3d3cdcc9da365777c7ad535d62"
                ]
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 40001 | invalid parameter | 参数错误。你需要检查输入参数是否有问题，如果仍然无法解决，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 400 | 41050 | no user authority | 无用户权限。当前操作的用户需在应用的通讯录权限范围内。通讯录权限范围的介绍与设置方式，参见[权限范围资源介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。 |
| 403 | 40004 | no dept. authority | 无部门权限。当前操作的部门需在应用的通讯录权限范围内。通讯录权限范围的介绍与设置方式，参见[权限范围资源介绍](https://open.larkoffice.com/document/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


