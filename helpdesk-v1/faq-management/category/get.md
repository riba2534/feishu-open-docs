---
title: "获取知识库分类"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/category/get"
updateTime: "1692084863000"
---

# 获取知识库分类

该接口用于获取知识库分类。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/helpdesk/v1/categories/:id |
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
| `id` | `string` | 知识库分类ID<br>**示例值**："6948728206392295444" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `category` | \- |
| &nbsp;&nbsp;└ `category_id` | `string` | 知识库分类ID |
| &nbsp;&nbsp;└ `id` | `string` | 知识库分类ID，（旧版，请使用category_id） |
| &nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;└ `helpdesk_id` | `string` | 服务台ID |
| &nbsp;&nbsp;└ `language` | `string` | 语言 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "category_id": "6948728206392295444",
        "id": "6948728206392295444",
        "name": "创建团队和邀请成员",
        "helpdesk_id": "6939771743531696147",
        "language": "zh_cn"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 401 | 154001 | Unauthorized, please check you have the correct access | 检查Authorization 和 X-Lark-Helpdesk-Authorization 是否正确，应用和服务台属于同一租户 |
| 404 | 154004 | Resource not found | 资源不存在，请检查ID值 |
| 500 | 155000 | Internal error | 内部错误，请联系我们 |


