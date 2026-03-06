---
title: "删除待入职（不推荐）"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/pre_hire/delete"
updateTime: "1720766086000"
---

# 删除待入职人员（不推荐）

删除待入职人员接口，本接口直接删除待入职数据，不会判断入职流程，推荐使用新接口进行删除[【删除待入职】](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/delete)。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v1/pre_hires/:pre_hire_id |
| HTTP Method | DELETE |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `corehr:corehr` 更新核心人事信息 `corehr:pre_hire:write` 读写待入职人员信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `pre_hire_id` | `string` | 需要删除的待入职人员信息ID<br>**示例值**："76534545454" |


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


