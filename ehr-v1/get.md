---
title: "下载人员的附件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/ehr/ehr-v1/attachment/get"
updateTime: "1671763327000"
---

# 下载人员的附件

根据文件 token 下载文件。

调用 「批量获取员工花名册信息」接口的返回值中，「文件」类型的字段 id，即是文件 token


> **Tip**: ![image.png](https://sf1-ttcdn-tos.pstatp.com/obj/open-platform-opendoc/bed391d2a8ce6ed2d5985ea69bf92850_9GY1mnuDXP.png)


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/ehr/v1/attachments/:token |
| HTTP Method | GET |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `ehr:attachment:readonly` 获取飞书人事（标准版）应用中的附件数据 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `token` | `string` | 文件 token<br>**示例值**："09bf7b924f9a4a69875788891b5970d8" |


## 响应


HTTP状态码为 200 时，表示成功

返回文件二进制流


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1241001 | 服务器内部错误 | 重试或联系飞书人事（标准版）客服 |
| 400 | 1241002 | 请求参数错误 | 检查查询参数 |
| 404 | 1241003 | Token 不存在或者已过期 | 重新获取 Token |
| 400 | 1241004 | 你的企业尚未开通飞书人事（标准版）。如需开通，请前往「飞书管理后台」启用飞书人事（标准版） | 前往「飞书管理后台」启用飞书人事（标准版） |


