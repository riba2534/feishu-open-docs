---
title: "将人才加入人才库"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_pool/move_talent"
updateTime: "1724834871000"
---

# 将人才加入人才库

将人才加入人才库。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/talent_pools/:talent_pool_id/talent_relationship |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:talent_folder` 更新人才库信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `talent_pool_id` | `string` | 人才库 ID，可通过接口 [获取人才库列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_pool/search) 获取<br>**示例值**："6930815272790114325" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `talent_id` | `string` | 是 | 人才 ID，可通过接口 [获取人才列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/list) 获取<br>**示例值**："6930815272790114324" |
| `add_type` | `int` | 是 | 加入类型，加入后是否从其他库移出<br>**示例值**：1<br>**可选值有**：<br>- `1`: 否 - `2`: 是 |


### 请求体示例

```json
{
    "talent_id": "6930815272790114324",
    "add_type": 1
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `talent_pool_id` | `string` | 人才库 ID |
| &nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID，详情请查看接口：[获取人才详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/hire-v2/talent/get) |


### 响应体示例

```json
{
    "code": 0,
    "msg": "SUCCESS",
    "data": {
        "talent_pool_id": "6930815272790114325",
        "talent_id": "6930815272790114324"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 400 | 1002102 | 人才不存在 | 请检查入参 `talent_id` 是否正确 |
| 400 | 1002109 | 人才库不存在 | 请检查入参 `talent_pool_id` 是否正确 |


