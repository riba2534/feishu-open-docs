---
title: "上传文件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/person/upload"
updateTime: "1720429529000"
---

# 上传文件

上传文件。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/persons/upload |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:file:write` 读写飞书人事的附件信息 `corehr:corehr` 更新核心人事信息 `corehr:person:write` 读写员工的个人信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **示例值**："multipart/form-data; boundary=---7MA4YWxkTrZu0gW" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_content` | `file` | 是 | 文件二进制内容，大小不超过50M<br>**示例值**：file binary |
| `file_name` | `string` | 是 | 文件名称（需带有文件后缀）<br>**示例值**："个人信息.xlsx" |


### 请求体示例

```HTTP
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file_content";
Content-Type: application/octet-stream


---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file_name";

个人信息.xlsx
---7MA4YWxkTrZu0gW
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `id` | `string` | 上传文件ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "id": "100"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1161011 | system exception | 请刷新页面或稍后重试 |


