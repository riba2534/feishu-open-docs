---
title: "妙搭和飞书用户 ID 转换"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/directory-user/id_convert"
updateTime: "1772791400000"
---

# 转换飞书妙搭和飞书开放平台用户 ID

转换飞书妙搭和飞书开放平台之间的用户 ID<br>
#### 使用场景
适用于需要在飞书妙搭和飞书开放平台之间转换用户身份的场景<br>
#### 实现方式
通过指定转换类型（id_convert_type）和待转换的 ID 列表（ids）实现指定 ID 转换


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/spark/v1/directory/user/id_convert |
| HTTP Method | POST |
| 接口频率限制 | [50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `spark:directory.user.id_convert:read` 获取 ID 转换信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `id_convert_type` | `int` | 是 | ID 转换类型，枚举 设置为10、11时，ids需要传入妙搭用户 ID 设置为20时，需要传入飞书开平 OpenID 设置为21时，需要传入飞书开平 UnionID<br>**示例值**：10<br>**可选值有**：<br>- `10`: 妙搭用户 ID 转飞书开放平台 Open ID - `11`: 妙搭用户 ID 转飞书开放平台 Union ID - `20`: 飞书开放平台 Open ID 转妙搭用户 ID - `21`: 飞书开放平台 Union ID 转妙搭用户 ID |
| `ids` | `string\[\]` | 否 | 默认为空，为空时不返回<br>**示例值**：["123456789837364"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |


### 请求体示例

```json
{
    "id_convert_type": 10,
    "ids": [
        "123456789837364"
    ]
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `id_map_item\[\]` | ID 映射，查询不到或者查询出错的不返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `source_id` | `string` | 源 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `target_id` | `string` | 目标 ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "source_id": "123445678933432",
                "target_id": "ou_1234cdjhjfedgfhgdhy3884"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 3340001 | param is invalid | 请检查请求参数的类型、格式或值是否符合接口要求，具体可参考请求参数说明中的数据校验规则。 |


