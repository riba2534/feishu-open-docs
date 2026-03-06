---
title: "群成员概述"
fullPath: "/uAjLw4CM/ukTMukTMukTM/im-v1/chat/chat-member/intro"
updateTime: "1730257094000"
---

# 群成员概述

群成员包括用户和机器人。在飞书群组内，支持添加用户或者机器人作为群成员，同时支持将用户或者机器人设置为群管理员。开放平台提供了管理群成员的相关接口与事件：

- 指定群管理员、邀请成员入群、将成员移出群以及获取群成员列表等接口
- 用户进群、用户出群、机器人进群、机器人被移出群以及用户与机器人发起会话等事件


## 字段说明

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `items` | `list_member\[\]` | 群成员列表 |
| ∟ `member_id_type` | `string` | 成员的用户 ID 类型，ID 类型包括 `open_id`、`user_id`、`union_id`。了解更多参见[用户身份概述](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)。 |
| ∟ `member_id` | `string` | 成员的用户 ID，ID 类型与 member_id_type 取值一致。 |
| ∟ `name` | `string` | 群成员的名字 |


### 数据示例
```json
{
  "items": [
    {
      "member_id_type": "user_id",
      "member_id": "4d7a3c6g",
      "name": "李健"
    }
  ]
}
```
