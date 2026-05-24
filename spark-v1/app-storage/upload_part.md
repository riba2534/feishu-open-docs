---
title: "分片上传文件 - 上传分片"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/upload_part"
updateTime: "1776914176000"
---

# 分片上传文件 - 上传分片

根据`创建上传请求`接口返回的上传请求 ID 和分片策略上传对应的文件分片。全部上传完成后可调用`完成上传`接口完成文件分片上传。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/storage/upload/part |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
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
| `upload_id` | `string` | 是 | 上传请求 ID，可通过`分片上传文件 - 创建上传请求`获取。<br>**示例值**："upload_abc123xyz456" |
| `chunk_index` | `int` | 是 | 分片编号从 1 开始<br>**示例值**：1<br>**数据校验规则**：<br>- 取值范围：`1` ～ `10000` |
| `file` | `file` | 是 | 对应分片文件的二进制内容，不限制文件格式，需要与`创建上传请求`接口中的文件 MIME 类型一致。<br>**示例值**：file binary |
| `chunk_check_sum` | `string` | 否 | 对应分片文件的 md5<br>**示例值**："ef176a6c424f954fa42d4cde03949897" |


### 请求体示例

```HTTP
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="upload_id";

upload_abc123xyz456
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="chunk_index";

1
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file";
Content-Type: application/octet-stream


---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="chunk_check_sum";

ef176a6c424f954fa42d4cde03949897
---7MA4YWxkTrZu0gW
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
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


