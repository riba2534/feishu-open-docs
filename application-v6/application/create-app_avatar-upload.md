---
title: "上传应用图标"
fullPath: "/uAjLw4CM/ukTMukTMukTM/application-v7/application-v7/app_avatar-upload/create"
updateTime: "1779344647000"
---

# 上传应用图标

上传应用图标


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/application/v7/app_avatar/upload |
| HTTP Method | POST |
| 接口频率限制 | [10 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `application:application:patch` 修改应用信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **示例值**："multipart/form-data; boundary=---7MA4YWxkTrZu0gW" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `avatar` | `file` | 是 | 图片，JPEG/PNG/SVG/BMP 格式，2 MB 以内，大于 240*240 px，无圆角<br>**示例值**：file binary |


### 请求体示例

```HTTP
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="avatar";
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
| &nbsp;&nbsp;└ `url` | `string` | 图片 URL，给创建/更新应用使用 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "url": "https://s3-imfile.feishucdn.com/static-resource/v1/v3_006n_24c0a858-0b0d-490b-a8d4-b1e2ef421c8g"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 210001 | param is invalid | 请检查请求参数的类型、格式或值是否与接口要求一致（如avatar参数需为file类型的二进制数据） |


