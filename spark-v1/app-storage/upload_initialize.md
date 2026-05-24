---
title: "分片上传文件 - 创建上传请求"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/upload_initialize"
updateTime: "1776914156000"
---

# 分片上传文件 - 创建上传请求

发送初始化请求，以获取上传请求 ID和分片策略，为上传分片做准备。获取结果后可调用`上传分片`接口完成文件分片上传。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/storage/upload/initialize |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app.storage:write` 获取与上传文件资源 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 妙搭应用 id，可从妙搭应用 URL 中获取，如 https://miaoda.feishu.cn/app/app_4jcn5n11bpf5v 中的 app_4jcn5n11bpf5v 即为 app_id<br>**示例值**："app_4jcn5n11bpf5v" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_name` | `string` | 是 | 文件的名称，建议最大长度不超过100<br>**示例值**："测试文本文件.txt" |
| `file_size` | `int` | 是 | 文件的大小，单位为字节。<br>**示例值**：104857600<br>**数据校验规则**：<br>- 取值范围：`1` ～ `2147483648` |
| `mime_type` | `string` | 否 | 文件 MIME 类型<br>**示例值**："text/plain; charset=utf-8" |


### 请求体示例

```json
{
    "file_name": "测试文本文件.txt",
    "file_size": 104857600,
    "mime_type": "text/plain; charset=utf-8"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `upload_id` | `string` | 上传请求 ID，有效期 24h |
| &nbsp;&nbsp;└ `chunk_size` | `int` | 建议的分片大小（字节） |
| &nbsp;&nbsp;└ `chunk_numbers` | `int` | 预估的总分片数 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "upload_id": "upload_abc123xyz456",
        "chunk_size": 4194304,
        "chunk_numbers": 25
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


