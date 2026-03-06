---
title: "获取用户维度的用户活跃和功能使用数据"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/admin-v1/admin_user_stat/list"
updateTime: "1732772232000"
---

# 获取用户维度的用户活跃和功能使用数据

用于获取用户维度的用户活跃和功能使用数据，即IM（即时通讯）、日历、云文档、音视频会议、邮箱功能的使用数据。


> **Warning**: - 只有企业自建应用才有权限调用此接口
> 
> - 当天的数据会在第二天的早上九点半产出（CN时区: UTC+8，非CN时区: UTC+0）
> 
> - 数据权限范围配置：目前只支持给每个应用配置部门级别数据权限范围，默认包含子部门


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/admin/v1/admin_user_stats |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `admin:admin_user_stat:readonly` 获取用户维度的用户活跃和功能使用数据 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `department_id_type` | `string` | 否 | 部门ID类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `department_id`: 部门的 ID - `open_department_id`: 部门的 Open ID |
| `start_date` | `string` | 是 | 起始日期（包含），格式是YYYY-mm-dd<br>**示例值**：2020-02-15 |
| `end_date` | `string` | 是 | 终止日期（包含），格式是YYYY-mm-dd。起止日期之间相差不能超过31天（包含31天）<br>**示例值**：2020-02-15 |
| `department_id` | `string` | 否 | 部门的 ID，取决于department_id_type<br>**示例值**：od-382e2793cfc9471f892e8a672987654c |
| `user_id` | `string` | 否 | 用户的open_id，user_id或者union_id，取决于user_id_type<br>**示例值**：ou_7dab8a3d3cdcc9da365777c7ad535d62 |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：10<br>**数据校验规则**：<br>- 取值范围：`1` ～ `60` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：2 |
| `target_geo` | `string` | 否 | 需跨域访问的Geo数据，每个Geo仅包含本Geo数据，不传默认查本地数据，调用前需要先开通FG（cn、us、sg、jp），每次只能查一个Geo数据<br>**示例值**：cn |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `items` | `admin_user_stat\[\]` | 数据报表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `date` | `string` | 日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_name` | `string` | 部门名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_path` | `string` | 部门路径 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 账号创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_active_flag` | `int` | 用户激活状态<br>**可选值有**：<br>- `0`: 未激活 - `1`: 已激活 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `register_time` | `string` | 激活时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `suite_active_flag` | `int` | 用户活跃状态，用户在飞书套件任意应用登陆，即为活跃。包括飞书即时消息，文档，日历，会议，开放平台等<br>**可选值有**：<br>- `0`: 无活跃 - `1`: 活跃 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `last_active_time` | `string` | 最近活跃时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `im_active_flag` | `int` | 用户消息活跃状态，发生过如下事件，则认为该用户消息活跃： 发送消息、回复消息、reaction、转发消息、阅读消息、查看会话、发送表情消息等<br>**可选值有**：<br>- `0`: 无活跃 - `1`: 活跃 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `send_messenger_num` | `int` | 发送消息数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `docs_active_flag` | `int` | 用户云文档活跃状态，"发生过如下事件，则认为该用户云文档活跃：  事件1：文档/文件打开 事件2：进入docs相关页面：如文档详情页，space的各个页面"<br>**可选值有**：<br>- `0`: 无活跃 - `1`: 活跃 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_docs_num` | `int` | 创建文件数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `cal_active_flag` | `int` | 用户日历活跃状态，发生过如下事件，则认为用户日历活跃，包含进入日历、创建日程、收到日程邀请等<br>**可选值有**：<br>- `0`: 无活跃 - `1`: 活跃 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_cal_num` | `int` | 创建日程数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `vc_active_flag` | `int` | 用户音视频会议活跃状态，用户进入会中状态（不包含妙记和直播）即为活跃<br>**可选值有**：<br>- `0`: 无活跃 - `1`: 活跃 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `vc_duration` | `int` | 会议时长（分钟，不包含会议室的时长） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `active_os` | `string` | 活跃设备 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_task_num` | `int` | 创建任务数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `vc_num` | `int` | 会议数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `app_package_type` | `string` | 飞书的应用类型名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `os_name` | `string` | 操作系统名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_send_count` | `string` | 邮件总发件量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_receive_count` | `string` | 邮件总收件量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_send_ext_count` | `string` | 对外发件数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_receive_ext_count` | `string` | 来自外部收件数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_send_in_count` | `string` | 对内发件数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email_receive_in_count` | `string` | 来自内部收件数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `search_active_flag` | `int` | 是否使用了大搜（0：未使用，1：有使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `total_search_count` | `string` | 总搜索次数（在飞书主端搜索框发起过搜索请求的会话数） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `quick_search_count` | `string` | 综搜次数（在飞书主端搜索框的综合搜索发起过搜索请求的会话数） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tab_search_count` | `string` | 垂搜次数（在飞书主端搜索框的垂类搜索tab（例如消息tab、云文档tab）发起过搜索请求的会话数） |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "has_more": true,
        "page_token": "3",
        "items": [
            {
                "date": "2020-02-15",
                "user_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62",
                "user_name": "Zhang San",
                "department_name": "testcqlbfaaasdasdasd",
                "department_path": "testkkk/testcqlbfaaasdasdasd",
                "create_time": "2020-09-04 11:17:55",
                "user_active_flag": 1,
                "register_time": "2020-09-04 11:18:32",
                "suite_active_flag": 1,
                "last_active_time": "2020-12-21 22:21:28",
                "im_active_flag": 1,
                "send_messenger_num": 0,
                "docs_active_flag": 1,
                "create_docs_num": 1,
                "cal_active_flag": 1,
                "create_cal_num": 0,
                "vc_active_flag": 1,
                "vc_duration": 0,
                "active_os": "'ios 14.2,-','ios 14.2,feishu 3.40.0-alpha'",
                "create_task_num": 0,
                "vc_num": 0,
                "app_package_type": "Feishu，Lark",
                "os_name": "iOS,Andorid,Windows",
                "email_send_count": "2",
                "email_receive_count": "3",
                "email_send_ext_count": "4",
                "email_receive_ext_count": "5",
                "email_send_in_count": "6",
                "email_receive_in_count": "7",
                "search_active_flag": 1,
                "total_search_count": "7",
                "quick_search_count": "7",
                "tab_search_count": "7"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1051001 | request contain invalid param | 请求中包含非法参数 |
| 400 | 1051002 | request to exceed authority | 请求发生越权 |


