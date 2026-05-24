---
title: "上传 HTML 代码并发布"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app/upload_html_code_and_release"
updateTime: "1779366565000"
---

# 上传 HTML 代码并发布


上传 HTML 代码并发布


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/apps/:app_id/upload_and_release_html_code |
| HTTP Method | POST |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app:publish` 发布妙搭应用 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 妙搭应用唯一标识，通过应用创建接口或妙搭管理后台获取<br>**示例值**："app_4k6af8utt2s0n" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file` | `file` | 是 | tar 格式的 HTML 文件<br>**示例值**："./app_html_code.tar" |


### 请求体示例

```json
{
    "file": "./app_html_code.tar"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `url` | `string` | 发布成功后的在线访问地址。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "url": "https://spark.example.com/apps/MDA20240516001"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 输入参数不合法，请检查输入参数 |


