---
title: "获取地理位置列表"
fullPath: "/uAjLw4CM/ukTMukTMukTM/security_and_compliance-v1/multi_geo_entity-tenant/get"
updateTime: "1773718666000"
---

# 获取数据驻留地理位置列表

获取租户可用的数据驻留地理位置列表


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/security_and_compliance/v1/multi_geo_entity/tenant |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `security_and_compliance:multi_geo_entity.tenant:readonly` 查看数据驻留租户信息 `security_and_compliance:user_migration:multi-geo` 查询、更新员工的数据驻留地 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `tenant` | `tenant` | 数据驻留租户信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `available_geo_locations` | `string\[\]` | 可选地理位置列表 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "tenant": {
            "available_geo_locations": [
                "sg"
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1781001 | Your request contains an invalid request parameter. | 请求参数无效，请修正请求参数 |
| 403 | 1781002 | Lack of necessary permissions. | 缺少必要的权限。请在管理员后台为操作人开通数据驻留服务操作权限，参考[管理员创建管理员角色及分配权限](https://www.feishu.cn/hc/zh-CN/articles/360043495213) |
| 400 | 1781003 | Data Residency service is not enabled for this tenant. | 租户未开通「数据驻留服务」。请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)开通「数据驻留服务」 |
| 500 | 1782001 | Internal service error. | 服务出现内部错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


