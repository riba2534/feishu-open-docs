---
title: "新建文件夹"
fullPath: "/ukTMukTMukTM/ukTNzUjL5UzM14SO1MTN"
updateTime: "1651916127000"
---

# 新建文件夹

该接口用于根据 folderToken 在该 folder 下创建文件夹。


> **Error**: 为了更好地提升该接口的安全性，我们对其进行了升级，请尽快迁移至
>   [新版本>>](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/create_folder)


> **Warning**: 该接口不支持并发创建，且调用频率上限为 5QPS 以及 10000次/天


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/drive/explorer/v2/folder/:folderToken |
| HTTP Method | POST |
| 支持的应用类型 | custom,isv |
| 权限要求  调用该 API 所需的权限。开启其中任意一项权限即可调用 | `drive:drive` 查看、评论、编辑和管理云空间中所有文件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` or `user_access_token`   **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560"             [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


::: note
关于云文档接口的 AccessToken 调用说明详见 [云文档接口快速入门](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)
:::

### 路径参数
|参数|类型|必须|说明|
|--|-----|--|----|
|folderToken|string|是|文件夹的 token，获取方式见 [概述](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction)| 

### 请求体
|参数|类型|必须|说明|
|--|-----|--|----|
|title|string|是|文件夹标题| 

### 请求体示例
```json
{
	"title": "string"
}
```
### 响应

### 响应体
|参数|说明|
|--|--|
|url|新创建文件夹的 url|
|revision|新创建文件夹的版本号|
|token|新创建文件夹的 token|

### 响应体示例

```json
{
	"code": 0,
	"msg": "Success",
	"data": {
		"url": "string",
    	"revision": 0,
    	"token": "string"
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

