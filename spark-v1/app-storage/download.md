---
title: "下载文件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/download"
updateTime: "1775707386000"
---

# 下载文件

用于下传 20MB（含） 以内的文件


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/storage |
| HTTP Method | GET |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app.storage:write` 获取与上传文件资源 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Range | string | 否 | 在 HTTP 请求头中，通过指定 Range 来下载文件的部分内容，单位是字节（byte）。该参数的格式为 Range: bytes=start-end，示例值为 Range: bytes=0-1024，表示下载第 0 个字节到第 1024 个字节之间的数据。 **示例值**："Range: bytes=0-1024" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 妙搭应用 id，可从妙搭应用 URL 中获取，如 https://miaoda.feishu.cn/app/app_4jcn5n11bpf5v 中的 app_4jcn5n11bpf5v 即为 app_id<br>**示例值**："app_4jcn5n11bpf5v" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_key` | `string` | 否 | 文件 ID，ID 和 URL 不能同时为空，都提供的情况下，使用 file_key<br>**示例值**：1859988692091946 |
| `file_url` | `string` | 否 | 文件 URL，ID 和 URL 不能同时为空<br>**示例值**：/app/app_4jmwuym484u90/runtime/api/v1/storage/object/bucket_aadju74v6daba/1859988692091946 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `content_type` | `string` | 文件的MIME |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "content_type": "image/jpeg"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


