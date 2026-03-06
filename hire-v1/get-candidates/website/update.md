---
title: "更新招聘官网推广渠道"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website-channel/update"
updateTime: "1722568751000"
---

# 更新招聘官网推广渠道

根据招聘官网 ID 和推广渠道 ID 更改推广渠道，仅支持修改推广渠道名称。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/websites/:website_id/channels/:channel_id |
| HTTP Method | PUT |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:site` 更新官网信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `website_id` | `string` | 官网 ID，通过[获取招聘官网列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website/list)获取<br>**示例值**："1618209327096" |
| `channel_id` | `string` | 推广渠道 ID，可通过[获取推广渠道列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website-channel/list)获取<br>**示例值**："7085989097067563300" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `channel_name` | `string` | 是 | 推广渠道名称<br>**示例值**："微信推广渠道" |


### 请求体示例

```json
{
    "channel_name": "微信推广渠道"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `website_channel_info` | \- |
| &nbsp;&nbsp;└ `id` | `string` | 推广渠道 ID |
| &nbsp;&nbsp;└ `name` | `string` | 推广渠道名称 |
| &nbsp;&nbsp;└ `link` | `string` | 推广渠道链接 |
| &nbsp;&nbsp;└ `code` | `string` | 推广渠道推广码 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "id": "7085989097067563300",
        "name": "微信推广渠道",
        "link": "http://recrui-demo.jobs.xxx.cn/485083/?spread=A1KM6A5",
        "code": "A1KM6A5"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


