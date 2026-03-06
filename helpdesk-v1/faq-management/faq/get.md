---
title: "获取指定知识库详情"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/faq/get"
updateTime: "1692084862000"
---

# 获取指定知识库详情

该接口用于获取服务台知识库详情。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/helpdesk/v1/faqs/:id |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `helpdesk:all:readonly` 获取服务台资源详情 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


> **Tip**: 服务台请求Header中还需添加“服务台token”参数：
>   
>   Key: X-Lark-Helpdesk-Authorization
>   
>   Value: base64(helpdesk_id:helpdesk_token)，通过base64加密将helpdesk_id和helpdesk_token用':'连接而成的字符串。
>   
>   [了解更多：获取与使用服务台token](https://open.larkoffice.com/document/ukTMukTMukTM/ugDOyYjL4gjM24CO4IjN)


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `id` | `string` | 知识库ID<br>**示例值**："6856395634652479491" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `faq` | `faq` | 知识库详情 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `faq_id` | `string` | 知识库ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 知识库旧版ID，请使用faq_id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `helpdesk_id` | `string` | 服务台ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `question` | `string` | 问题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `answer` | `string` | 答案 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `answer_richtext` | `richtext\[\]` | 富文本答案 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `int` | 修改时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `categories` | `category\[\]` | 分类 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `category_id` | `string` | 知识库分类ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 知识库分类ID，（旧版，请使用category_id） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_id` | `string` | 父知识库分类ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `helpdesk_id` | `string` | 服务台ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `language` | `string` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tags` | `string\[\]` | 相似问题列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `expire_time` | `int` | 失效时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `update_user` | `ticket_user` | 更新用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_user` | `ticket_user` | 创建用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "faq": {
            "faq_id": "6936004780707807231",
            "id": "6936004780707807231",
            "helpdesk_id": "6936004780707807251",
            "question": "问题",
            "answer": "答案",
            "answer_richtext": [
                {
                    "content": "我的答案",
                    "type": "text"
                }
            ],
            "create_time": 1596379008,
            "update_time": 1596379008,
            "categories": [
                {
                    "category_id": "6948728206392295444",
                    "id": "6948728206392295444",
                    "name": "创建团队和邀请成员",
                    "parent_id": "0",
                    "helpdesk_id": "6939771743531696147",
                    "language": "zh_cn"
                }
            ],
            "tags": [
                "问",
                "题"
            ],
            "expire_time": 1596379008,
            "update_user": {
                "id": "ou_37019b7c830210acd88fdce886e25c71",
                "avatar_url": "https://xxxx",
                "name": "abc",
                "department": "用户部门名称(有权限才展示)",
                "city": "城市",
                "country": "国家"
            },
            "create_user": {
                "id": "ou_37019b7c830210acd88fdce886e25c71",
                "avatar_url": "https://xxxx",
                "name": "abc",
                "department": "用户部门名称(有权限才展示)",
                "city": "城市",
                "country": "国家"
            }
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 404 | 154004 | Resource not found | 资源不存在，请检查ID值 |
| 500 | 155000 | Internal error | 内部错误，请联系我们 |


