---
title: "查询角色成员信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/apaas-v1/application-role-member/get"
updateTime: "1727087227000"
---

# 获取角色成员详情

获取角色成员详情


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/apaas/v1/applications/:namespace/roles/:role_api_name/member |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `app_engine:role:read` 查询角色配置信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `namespace` | `string` | 应用命名空间<br>**示例值**："package_test__c"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| `role_api_name` | `string` | 角色 API 名称<br>**示例值**："adminRole"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `need_display_name` | `boolean` | 否 | 是否需要公式的展示名称，便于前端展示<br>**示例值**：false |
| `use_api_id` | `boolean` | 否 | 是否使用 API ID字段作为出入参，默认值为 false<br>**示例值**：false<br>**默认值**：`false` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `role_member` | `role_member` | 角色成员 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `role_api_id` | `string` | 角色唯一 ID，系统自动生成 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `role_api_name` | `string` | 角色 API 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `users` | `string\[\]` | 授权用户 ID 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `departments` | `string\[\]` | 授权部门 ID 列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_filter` | `criterion` | 自定义授权用户规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `conditions` | `condition\[\]` | 查询条件 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `index` | `string` | 序号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `left` | `condition_value` | 左值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `settings` | `string` | 设置值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_names` | `string\[\]` | 左值/右值的展示名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `right` | `condition_value` | 右值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `settings` | `string` | 设置值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_names` | `string\[\]` | 左值/右值的展示名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operator` | `string` | 操作符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `logic_expression` | `string` | 逻辑关系 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_display_infos` | `permission_name_info\[\]` | 授权用户姓名列表，入参 need_display_name = true时返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_display_infos` | `permission_name_info\[\]` | 授权部门名称列表，入参 need_display_name = true时返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 角色成员模式<br>**可选值有**：<br>- `all`: 全部用户 - `custom`: 自定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_by` | `string` | 更新人 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_at` | `int` | 更新时间，单位：毫秒时间戳 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "role_member": {
            "role_api_id": "role_api_id",
            "role_api_name": "adminRole",
            "users": [
                "1802412778084426"
            ],
            "departments": [
                "1802412778084426"
            ],
            "user_filter": {
                "conditions": [
                    {
                        "index": "1",
                        "left": {
                            "type": "metadataVariable",
                            "settings": "{\"fieldPath\":[{\"fieldApiName\": \"_id\",\"objectApiName\": \"_user\"}]}",
                            "display_names": [
                                "用户.ID"
                            ]
                        },
                        "right": {
                            "type": "metadataVariable",
                            "settings": "{\"fieldPath\":[{\"fieldApiName\": \"_id\",\"objectApiName\": \"_user\"}]}",
                            "display_names": [
                                "用户.ID"
                            ]
                        },
                        "operator": "equal"
                    }
                ],
                "logic_expression": "1 and 2"
            },
            "user_display_infos": [
                {
                    "id": "1802412778084426",
                    "name": "张三"
                }
            ],
            "department_display_infos": [
                {
                    "id": "1802412778084426",
                    "name": "张三"
                }
            ],
            "type": "custom",
            "updated_by": "1802412778084426",
            "updated_at": 1702546522477
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2320001 | param is invalid | 请检查输入参数 |


