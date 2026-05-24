---
title: "搜索地理库信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/approval-v4/district/search"
updateTime: "1773383141000"
---

# 搜索地理库信息

搜索审批的地理库数据，可用于在发起审批时填写地址控件的区域信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/approval/v4/districts/search |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `approval:approval` 查看、创建、更新、删除审批应用相关信息 `approval:approval:readonly` 访问审批应用 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `locale` | `string` | 否 | 返回值的语言，目前仅部分数据支持中文，不支持中文的数据默认返回英文<br>**示例值**：zh-CN<br>**可选值有**：<br>- `zh-CN`: 中文 - `en-us`: 英文 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `district_ids` | `string\[\]` | 否 | 根据ID查询指定区域的信息，ID即地理库数据的ID，如果传了该参数，则以该参数作为唯一筛选项<br>**示例值**：["1816670"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `30` |
| `keyword` | `string` | 否 | 关键字，用于模糊查询符合条件的地址信息<br>**示例值**："北京" |


### 请求体示例

```json
{
    "district_ids": [
        "1816670"
    ],
    "keyword": "北京"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `district\[\]` | 区域列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 区域的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `string` | 层级 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `has_sub_district` | `boolean` | 是否有子区域 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_districts` | `district_base_info\[\]` | 父区域列表，顺序由叶子节点到根节点，不包含叶子节点本身，仅遍历方式为leaf_level时返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 区域的唯一标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `string` | 层级 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": "2038349",
                "name": "Beijing",
                "level": "Province",
                "has_sub_district": false,
                "parent_districts": [
                    {
                        "id": "1814991",
                        "name": "China",
                        "level": "Country"
                    }
                ]
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1395001 | system error | 请根据实际报错信息定位或[咨询客服](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952&extra=%7B%22channel%22:14,%22created_at%22:1614493146,%22scenario_id%22:6885151765134622721,%22signature%22:%22ca94c408b966dc1de2083e5bbcd418294c146e98%22%7D) |
| 400 | 1390001 | invalid parameter | 检查参数是否正确，例如类型，大小 |


