---
title: "上传文件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/upload"
updateTime: "1775707376000"
---

# 上传文件

用于上传 20MB（含） 以内的文件


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/storage/upload |
| HTTP Method | POST |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app.storage:write` 获取与上传文件资源 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **示例值**："multipart/form-data; boundary=---7MA4YWxkTrZu0gW" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 妙搭应用 id，可从妙搭应用 URL 中获取，如 https://miaoda.feishu.cn/app/app_4jcn5n11bpf5v 中的 app_4jcn5n11bpf5v 即为 app_id<br>**示例值**："app_4jcn5n11bpf5v" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_name` | `string` | 是 | 文件名称<br>**示例值**："file_name" |
| `check_sum` | `string` | 否 | 文件的十六进制 SHA-256 值，用于文件一致性校验。如果传入此值，服务端会在上传完成后对比接收到文件的 SHA-256 值，如果不一致，会返回上传失败。<br>**示例值**："f8d80a7f68b820d99f5612b952140319991d6599d95f29699d076684b0977f99" |
| `file` | `file` | 是 | 文件二进制<br>**示例值**：file binary |


### 请求体示例

```HTTP
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file_name";

file_name
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="check_sum";

f8d80a7f68b820d99f5612b952140319991d6599d95f29699d076684b0977f99
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file";
Content-Type: application/octet-stream


---7MA4YWxkTrZu0gW
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `file_key` | `string` | 文件 ID |
| &nbsp;&nbsp;└ `file_url` | `string` | 文件 URL，相对路径 |
| &nbsp;&nbsp;└ `file_name` | `string` | 文件名称 |
| &nbsp;&nbsp;└ `file_size` | `int` | 文件大小，单位字节 |
| &nbsp;&nbsp;└ `mime_type` | `string` | 文件 MIME 类型 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "file_key": "1859988692091946",
        "file_url": "/app/app_4jmwuym484u90/runtime/api/v1/storage/object/bucket_aadju74v6daba/1859988692091946",
        "file_name": "文件名称",
        "file_size": 33,
        "mime_type": "binary/octet-stream"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


