---
title: "修改知识库"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/faq/patch"
updateTime: "1719457048000"
---

# 修改知识库

该接口用于修改知识库。


> **Tip**: 注意事项：
> 	user_access_token 访问，需要操作者是当前服务台的客服、管理员或所有者


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/helpdesk/v1/faqs/:id |
| HTTP Method | PATCH |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `helpdesk:all` 更新服务台资源详情 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


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


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `faq` | `faq_update_info` | 否 | 修改的知识库内容 |
| &nbsp;&nbsp;└ `category_id` | `string` | 否 | 知识库分类ID<br>**示例值**："6836004780707807251" |
| &nbsp;&nbsp;└ `question` | `string` | 是 | 问题<br>**示例值**："问题" |
| &nbsp;&nbsp;└ `answer` | `string` | 否 | 答案<br>**示例值**："答案" |
| &nbsp;&nbsp;└ `answer_richtext` | `richtext\[\]` | 否 | 富文本答案和答案必须有一个必填。Json Array格式，富文本结构请见[了解更多: 富文本](https://open.larkoffice.com/document/ukTMukTMukTM/uITM0YjLyEDN24iMxQjN)<br>**示例值**：[{"content":"答案","type":"text"},{"content":"\n","type":"text"}] |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 否 | 内容<br>**示例值**："这是一个答案" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 否 | 内容类型。可选值：text、hyperlink、img、line break<br>**示例值**："text" |
| &nbsp;&nbsp;└ `tags` | `string\[\]` | 否 | 相似问题<br>**示例值**：["测试","问题"] |


### 请求体示例

```json
{
    "faq": {
        "category_id": "6836004780707807251",
        "question": "问题",
        "answer": "答案",
        "answer_richtext": [
            {
                "content": "这是一个答案",
                "type": "text"
            }
        ],
        "tags": [
            "测试",
            "问题"
        ]
    }
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 154000 | Bad request, please check your request body | 请求不合法，请检查参数 |
| 403 | 154003 | Please check you have the correct access | 检查是否申请正确权限 |
| 404 | 154004 | Resource not found | 资源不存在，请检查ID值 |
| 500 | 155000 | Internal error | 内部错误，请联系我们 |


