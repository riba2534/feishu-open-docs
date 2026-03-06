---
title: "更新自定义分组"
fullPath: "/uAjLw4CM/ukTMukTMukTM/task-v2/section/patch"
updateTime: "1751462775000"
---

# 更新自定义分组

更新自定义分组，可以更新自定义分组的名称和位置。

更新时，将`update_fields`字段中填写所有要修改的字段名，同时在`section`字段中填写要修改的字段的新值即可。调用约定详情见[功能概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/task-v2/overview)中的“ 关于资源的更新”章节。

目前支持更新的字段包括：
* `name` - 自定义字段名字;
* `insert_before` - 要让当前自定义分组放到某个自定义分组前面的secion_guid，用于改变当前自定义分组的位置;
* `insert_after` - 要让当前自定义分组放到某个自定义分组后面的secion_guid，用于改变当前自定义分组的位置。

`insert_before`和`insert_after`如果填写，必须是同一个资源的合法section_guid。注意不能同时设置`insert_before`和`insert_after`。


> **Tip**: 需要自定义分组所在资源的编辑权限。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/task/v2/sections/:section_guid |
| HTTP Method | PATCH |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `task:section:write` 查看、创建、更新、删除自定义分组 `task:section:writeonly` 创建、更新自定义分组 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `section_guid` | `string` | 要更新的自定义分组GUID<br>**示例值**："9842501a-9f47-4ff5-a622-d319eeecb97f"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**默认值**：`open_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `section` | `input_section` | 是 | 要更新的自定义分组的数据。 |
| &nbsp;&nbsp;└ `name` | `string` | 否 | 自定义分组名。如更新，不允许设为空，支持最大100个utf8字符。<br>**示例值**："已经审核过的任务" |
| &nbsp;&nbsp;└ `insert_before` | `string` | 否 | 要将新分组插入到自定义分分组的前面的目标分组的guid。<br>**示例值**："e6e37dcc-f75a-5936-f589-12fb4b5c80c2"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |
| &nbsp;&nbsp;└ `insert_after` | `string` | 否 | 要将新分组插入到自定义分分组的后面的目标分组的guid。<br>**示例值**："e6e37dcc-f75a-5936-f589-12fb4b5c80c2"<br>**数据校验规则**：<br>- 最大长度：`100` 字符 |
| `update_fields` | `string\[\]` | 是 | 要更新的字段名，支持： * `name` - 自定义字段名字 * `insert_before` - 要让当前自定义分组放到某个自定义分组前面的secion_guid，用于改变当前自定义分组的位置。 * `insert_after` - 要让当前自定义分组放到某个自定义分组后面的secion_guid，用于改变当前自定义分组的位置。<br>**示例值**：["name"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `10` |


### 请求体示例

```json
{
    "section": {
        "name": "已经审核过的任务",
        "insert_before": "e6e37dcc-f75a-5936-f589-12fb4b5c80c2",
        "insert_after": "e6e37dcc-f75a-5936-f589-12fb4b5c80c2"
    },
    "update_fields": [
        "name"
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `section` | `section` | 更新后的自定义分组 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `guid` | `string` | 自定义分组的guid |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 自定义分组的名字 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resource_type` | `string` | 资源类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_default` | `boolean` | 分组是否为默认自定义分组 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `member` | 自定义分组的创建者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 表示member的id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 成员的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `role` | `string` | 成员角色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 成员名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tasklist` | `tasklist_summary` | 如果该分组归属于清单，展示清单的简要信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `guid` | `string` | 清单的全局唯一ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 清单名字 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `string` | 自定义分组创建时间戳(ms) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `string` | 自定义分组最近一次更新时间戳(ms) |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "section": {
            "guid": "e6e37dcc-f75a-5936-f589-12fb4b5c80c2",
            "name": "已经评审过的任务",
            "resource_type": "tasklist",
            "is_default": true,
            "creator": {
                "id": "ou_2cefb2f014f8d0c6c2d2eb7bafb0e54f",
                "type": "user",
                "role": "editor",
                "name": "张明德（明德）"
            },
            "tasklist": {
                "guid": "cc371766-6584-cf50-a222-c22cd9055004",
                "name": "活动分工任务列表"
            },
            "created_at": "1675742789470",
            "updated_at": "1675742789470"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1470400 | 请求参数错误，比如在`update_fields`里设置了不支持变更的字段名。 | 错误原因见返回的msg提示的信息。 |
| 404 | 1470404 | 要更新的自定义分组不存在或已删除。 | 确认要更新的自定义分组不存在或已删除。 |
| 500 | 1470500 | 服务器错误。 | 尝试重试调用。如持续失败，请联系支持人员进行反馈。 |
| 403 | 1470403 | 缺少更新自定义分组的权限。 | 确认调用身份拥有可以编辑自定义分组的权限。 |


