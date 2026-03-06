---
title: "查询帖子信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/moments-v1/post/get"
updateTime: "1732608437000"
---

# 查询帖子信息

通过 ID 查询帖子实体数据信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/moments/v1/posts/:post_id |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `moments:moments:readonly` 查询公司圈内容、板块 `moments:moments:access_all` 允许管理租户公司圈全部数据 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `post_id` | `string` | 帖子的ID，可从发布帖子接口返回数据或发布帖子事件中获取<br>**示例值**："6934510454161014804" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `post` | `post` | 帖子实体 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 发帖用户ID（类型为请求中传入的类型，仅实名下有值） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 帖子内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `image_key_list` | `string\[\]` | 图片的 key列表（暂不支持下载） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `media_file_token` | `string` | 媒体文件的 token（暂未使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `comment_count` | `int` | 评论数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `reaction_set` | `reaction_set` | 帖子的 reaction及其数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `reactions` | `reaction_list\[\]` | reaction列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | reaction的类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `count` | `int` | 该类型 reaction的数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `total_count` | `int` | 所有 reaction的数量 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 帖子ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `string` | 帖子创建时间，格式 rfc3339， e.g. "2006-01-02T15:04:05Z07:00" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `media_cover_image_key` | `string` | 视频封面图片（暂未使用） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `category_ids` | `string\[\]` | 帖子所属板块 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `string` | 帖子链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_type` | `int` | 发帖人类型<br>**可选值有**：<br>- `1`: 实名 - `2`: 花名 - `3`: 匿名 - `4`: 官方号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dislike_count` | `int` | 点踩数量 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "post": {
            "user_id": "ou_xxxxx",
            "content": "[[{\"tag\":\"text\",\"text\":\"豪华中型车…………\"},{\"tag\":\"a\",\"text\":\"查看原文\",\"href\":\"https://www.autohome.com.cn/advice/202204/1244455.html\"}]]",
            "image_key_list": [
                "暂不支持下载图片"
            ],
            "media_file_token": "该字段暂不支持使用",
            "comment_count": 1,
            "reaction_set": {
                "reactions": [
                    {
                        "type": "OK",
                        "count": 12
                    }
                ],
                "total_count": 12
            },
            "id": "6934510454161014804",
            "create_time": "2022-05-23T00:00:00+08:00",
            "media_cover_image_key": "该字段暂不支持使用",
            "category_ids": [
                "71123"
            ],
            "link": "https://applink.feishu.cn/client/moments/detail?postId=6934510454161014804",
            "user_type": 1,
            "dislike_count": 0
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1420001 | invalid args | 排查post_id格式是否正确 |
| 403 | 1420002 | permission denied | 排查是否有权限查询帖子 |
| 404 | 1420004 | post not found | 排查帖子id是否正确或是否已删除 |
| 429 | 1420003 | triggers the frequency limit | 请降低请求频率，稍后重试 |


