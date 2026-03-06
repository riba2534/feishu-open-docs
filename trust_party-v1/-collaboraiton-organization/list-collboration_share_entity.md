---
title: "获取关联组织双方共享成员范围"
fullPath: "/uAjLw4CM/ukTMukTMukTM/directory-v1/collboration_share_entity/list"
updateTime: "1745918518000"
---

# 获取关联组织双方共享成员范围

在创建规则时，需要获取本组织以及对方组织人员、部门和用户组的ID，且这些实体都应该在关联组织的共享范围内。本接口可获取关联组织双方的共享范围下的人员、部门和用户组。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/directory/v1/share_entities |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `trust_party:collaboration_rule:read` 获取关联组织协作规则 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `target_tenant_key` | `string` | 是 | 对方组织的tenant key，可通过[管理员获取所有关联组织列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/directory-v1/collaboration_tenant/list)获取<br>**示例值**：test_key |
| `target_department_id` | `string` | 否 | 不填写该参数时，查询整个组织的分享范围，可填写该字段继续下钻查看指定部门下的子部门+成员。填写0分为两种情况，若组织分享的为全员则展示一级部门，否则展示分享的部门+成员；可以递归使用该接口实现整个分享范围的下钻查询<br>**示例值**：test_key |
| `target_group_id` | `string` | 否 | 获取用户组下的成员，填写该值后忽略target_department_id；可以通过本接口参数返回的用户组ID继续本接口查询<br>**示例值**：test_key |
| `is_select_subject` | `boolean` | 否 | 是否主体组织分享范围，默认是客体组织的分享范围<br>**示例值**：true |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0= |
| `page_size` | `int` | 否 | 分页大小<br>**示例值**：10<br>**默认值**：`100`<br>**数据校验规则**：<br>- 取值范围：`0` ～ `100` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `share_departments` | `share_department\[\]` | 分享的部门信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `open_department_id` | `string` | 部门open ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n_text` | i18n文本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 默认值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值 |
| &nbsp;&nbsp;└ `share_groups` | `share_group\[\]` | 分享的用户组信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `open_group_id` | `string` | 用户组的open_id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n_text` | i18n文本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 默认值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值 |
| &nbsp;&nbsp;└ `share_users` | `share_user\[\]` | 分享的用户信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `open_user_id` | `string` | user open ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n_text` | i18n文本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 默认值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `avatar` | `image_link` | 用户的头像 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_72` | `string` | 72*72像素头像链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_240` | `string` | 240*240像素头像链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_640` | `string` | 640*640像素头像链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_origin` | `string` | 原始头像链接 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "has_more": true,
        "share_departments": [
            {
                "open_department_id": "ou-12121xxxx",
                "name": {
                    "default_value": "张三",
                    "i18n_value": {
                        "en_us": "test"
                    }
                }
            }
        ],
        "share_groups": [
            {
                "open_group_id": "ou-12121212",
                "name": {
                    "default_value": "张三",
                    "i18n_value": {
                        "en_us": "test"
                    }
                }
            }
        ],
        "share_users": [
            {
                "open_user_id": "ou-12121212",
                "name": {
                    "default_value": "张三",
                    "i18n_value": {
                        "en_us": "test"
                    }
                },
                "avatar": {
                    "avatar_72": "http://qwed.com",
                    "avatar_240": "http://wssd.com",
                    "avatar_640": "http://wssd.com",
                    "avatar_origin": "https:inernal-api/image"
                }
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2223109 | page_token is invalid | 请填写有效的page token |
| 400 | 2224001 | No permission to operate | 需要有关联组织管理员的权限，请联系本租户超管将你配置为关联组织管理员 |


