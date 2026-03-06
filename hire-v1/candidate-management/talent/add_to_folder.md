---
title: "将人才加入指定文件夹"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/add_to_folder"
updateTime: "1733294817000"
---

# 将人才加入指定文件夹

根据人才 ID 列表将人才加入指定文件夹。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/talents/add_to_folder |
| HTTP Method | POST |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:talent` 更新人才信息 `hire:talent_folder_association` 操作人才加入/移除文件夹 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `talent_id_list` | `string\[\]` | 是 | 人才 ID 列表，可通过[获取人才列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/list)接口获得<br>**示例值**：["7039620186502138157"]<br>**数据校验规则**：<br>- 长度范围：`1` ～ `200` |
| `folder_id` | `string` | 是 | 文件夹 ID，可通过[获取人才文件夹列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_folder/list)接口获取<br>**示例值**："7039620186502138156" |


### 请求体示例

```json
{
    "talent_id_list": [
        "7039620186502138157"
    ],
    "folder_id": "7039620186502138156"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `talent_id_list` | `string\[\]` | 人才 ID 列表，详情请查看：[获取人才信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/get) |
| &nbsp;&nbsp;└ `folder_id` | `string` | 文件夹 ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "talent_id_list": [
            "7039620186502138157"
        ],
        "folder_id": "7039620186502138156"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |


