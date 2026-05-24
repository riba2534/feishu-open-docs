---
title: "上传妙搭应用图标"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/app/icon"
updateTime: "1779366605000"
---

# 上传妙搭应用图标

上传妙搭应用图标


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/icon |
| HTTP Method | POST |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:app:write` 创建与更新妙搭应用 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file` | `file` | 是 | File 待上传的图标文件，multipart/form-data 的 file 部分<br>**示例值**："./image.png" |


### 请求体示例

```json
{
    "file": "./image.png"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `icon_url` | `string` | IconURL 上传成功后的图标访问 URL。 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "icon_url": "https://spark-cdn.example.com/tenant/10001/app-icons/20240520/abcdef123456.png"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 输入参数不合法，请检查输入参数 |


