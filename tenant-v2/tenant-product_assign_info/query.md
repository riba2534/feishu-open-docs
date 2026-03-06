---
title: "获取企业席位信息接口"
fullPath: "/uAjLw4CM/ukTMukTMukTM/tenant-v2/tenant-product_assign_info/query"
updateTime: "1755680235000"
---

# 获取企业席位信息

获取租户下待分配的席位列表（仅返回未满的席位），包含席位名称、席位ID、数量及对应有效期。
返回的待分配席位范围为：​
1. 客户当前已订阅且处于生效状态的席位（注：不包含增购的、尚未生效的未来席位）；​
2. 客户已订阅且未来生效的全新订阅席位。​

即增购的未来席位不在本接口返回的待分配席位列表范围内。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/tenant/v2/tenant/assign_info_list/query |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `tenant:tenant.product_assign_info:read` 查询租户下的席位信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `assign_info_list` | `tenant_assign_info\[\]` | 租户待分配席位列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `subscription_id` | `string` | 席位id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `license_plan_key` | `string` | license_plan_key |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `product_name` | `string` | 商业化产品名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_name` | `product_i18n_name` | 国际化名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 商业化产品的中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 商业化产品的日文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 商业化产品的英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `total_seats` | `string` | 席位总数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `assigned_seats` | `string` | 已分配席位数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 席位起始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 席位结束时间 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "assign_info_list": [
            {
                "subscription_id": "7079609167680782300",
                "license_plan_key": "suite_enterprise_e5",
                "product_name": "旗舰版 E5",
                "i18n_name": {
                    "zh_cn": "zh_cn_name",
                    "ja_jp": "ja_jp_name",
                    "en_us": "en_name"
                },
                "total_seats": "500",
                "assigned_seats": "20",
                "start_time": "1674981000",
                "end_time": "1674991000"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1180001 | param is invalid | 请检查请求参数 |


