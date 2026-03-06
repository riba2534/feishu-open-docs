---
title: "创建人才外部信息"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent-external_info/create"
updateTime: "1725853462000"
---

# 创建人才外部信息

创建外部人才，可将已存在人才标记为外部人才，并写入外部系统创建时间。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/talents/:talent_id/external_info |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:talent` 更新人才信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `talent_id` | `string` | 人才 ID，可通过[获取人才列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/list)获取<br>**示例值**："7043758982146345223" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `external_create_time` | `string` | 是 | 人才在外部系统的创建时间，毫秒时间戳<br>**示例值**："1639992265035" |


### 请求体示例

```json
{
    "external_create_time": "1639992265035"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `external_info` | `talent_external_info` | 人才外部信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID，详情请查看：[获取人才信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `external_create_time` | `string` | 人才在外部系统的创建时间，毫秒时间戳 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "external_info": {
            "talent_id": "7043758982146345222",
            "external_create_time": "1608467675393"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统异常 | 请根据实际报错信息定位问题或联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


