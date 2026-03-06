---
title: "删除Doc"
fullPath: "/ukTMukTMukTM/uATM2UjLwEjN14CMxYTN"
updateTime: "1651916140000"
---

# 删除 Doc


该接口用于根据 docToken 删除对应的 Docs 文档。


> **Error**: 为了更好地提升该接口的安全性，我们对其进行了升级，请尽快迁移至
>   [新版本>>](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/delete)


> **Warning**: 文档只能被文档所有者删除，文档被删除后将会放到回收站里

:::note
该接口不支持并发调用，且调用频率上限为5QPS
:::

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/drive/explorer/v2/file/docs/:docToken |
| HTTP Method | DELETE |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `docs:doc` 查看、评论、编辑和管理文档 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token`            **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560"             [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


::: note
::: html
使用 `tenant_access_token` 前，请确保该应用是文档的所有者，否则会报无权限错误。

:::
<br>

### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `docToken` | `string` | doc 的 token，获取方式见 [概述](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction) |


## 响应
### 响应体
|参数|说明|
|--|--|
|id|doc 的 id「字符串类型」|
|result|删除结果|


### 响应体示例
```json
{
    "code":0,
    "msg":"success",
    "data":
    {
        "id":"id string",
        "result":true
    }
}
```
### 错误码


| 错误码 | 说明 | 排查建议 |
| --- | --- | --- |
| 91201 | FAILED | 处理失败，稍后重试。 |
| 91202 | PARAMERR | 参数错误，检查参数是否正确，如：`type`、`fileToken`、`dstFolderToken`。 |
| 91203 | NOTEXIST | 请检查请求参数是否正确，如：`type`跟`fileToken`是否匹配。 |
| 91204 | FORBIDDEN | 检查当前账户对文档、文件夹的权限。参考[接入流程授权](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/docs-overview#6d744fe3) |
| 91205 | DELETED | 来源文件已被删除，检查是否还存在。 |
| 91206 | OUT_OF_LIMIT | 超过限制。 |
| 91207 | DUPLICATE | 重复记录。 |
| 91208 | REVIEW | 内容审查不通过。 |


具体可参考：[服务端错误码说明](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)
