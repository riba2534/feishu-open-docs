---
title: "删除三方协议"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/tripartite_agreement/delete"
updateTime: "1724834839000"
---

# 删除三方协议

删除投递的三方协议。


## 前提条件
在「飞书招聘」-「设置」-「候选人流程管理」-「三方协议设置」中勾选了「通过 API 维护三方协议」。

## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/tripartite_agreements/:tripartite_agreement_id |
| HTTP Method | DELETE |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:tripartite_agreement` 更新三方协议 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `tripartite_agreement_id` | `string` | 三方协议 ID，由[创建三方协议](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/tripartite_agreement/create)接口返回或通过[获取三方协议](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/tripartite_agreement/list)获取<br>**示例值**："6930815272790114324" |


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
    "msg": "SUCCESS",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 400 | 1002075 | 三方协议不存在 | tripartite_agreement_id 不合法，请检查入参 `tripartite_agreement_id` 是否正确 |
| 400 | 1002076 | 通过 API 维护三方协议开关未开启 | 请联系管理员前往招聘系统后台在「飞书招聘」-「设置」-「候选人流程管理」-「三方协议设置」中勾选「通过 API 维护三方协议」 |


更多错误码信息，参见[通用错误码](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。


