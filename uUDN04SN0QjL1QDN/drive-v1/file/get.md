---
title: "获取文件统计信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file-statistics/get"
updateTime: "1731587188000"
---

# 获取文件统计信息

此接口用于获取各类文件的流量统计信息和互动信息，包括阅读人数、阅读次数和点赞数。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/drive/v1/files/:file_token/statistics |
| HTTP Method | GET |
| 接口频率限制 | [特殊频控](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `drive:drive` 查看、评论、编辑和管理云空间中所有文件 `drive:drive.metadata:readonly` 查看云空间中文件元数据 `drive:drive:readonly` 查看、评论和下载云空间中所有文件 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


::: note
更多云文档接口权限问题，参考[常见问题](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)。
:::

### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `file_token` | `string` | 文件 token。了解如何获取文件 token，参考[文件概述](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/file-overview)。<br>**示例值**："doccnfYZzTlvXqZIGTdAHKabcef" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file_type` | `string` | 是 | 文件类型<br>**示例值**：doc<br>**可选值有**：<br>- `doc`: 旧版文档 - `sheet`: 电子表格 - `mindnote`: 思维笔记 - `bitable`: 多维表格 - `wiki`: 知识库文档 - `file`: 文件 - `docx`: 新版文档 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `file_token` | `string` | 文档 token |
| &nbsp;&nbsp;└ `file_type` | `string` | 文档类型 |
| &nbsp;&nbsp;└ `statistics` | `file_statistics` | 文档统计信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `uv` | `int` | 文档历史访问人数，同一用户（user_id）多次访问按一次计算。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pv` | `int` | 文档历史访问次数，同一用户（user_id）多次访问按多次计算，但同一用户在间隔在半小时内访问两次视为一次访问 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `like_count` | `int` | 文档历史点赞总数。`-1` 表示对应的文档类型不支持点赞 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `timestamp` | `int` | 时间戳（单位：秒） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `uv_today` | `int` | 今日新增文档访问人数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `pv_today` | `int` | 今日新增文档访问次数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `like_count_today` | `int` | 今日新增文档点赞数 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "file_token": "doccnfYZzTlvXqZIGTdAHKabcef",
        "file_type": "doc",
        "statistics": {
            "uv": 10,
            "pv": 15,
            "like_count": 2,
            "timestamp": 1627367349,
            "uv_today": 1,
            "pv_today": 1,
            "like_count_today": 1
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1069601 | fail | 重试，若稳定失败请联系相关业务方 oncall 人员 |
| 400 | 1069602 | param error | 检查参数有效性 |
| 403 | 1069603 | forbidden | 无权限操作，可能是如下原因： * 调用身份无文档管理权限 * 当前租户未开启文档访问记录功能 请参考以下方式为调用身份开通文档管理权限： - 如果你使用的是 `tenant_access_token`，意味着当前应用没有云文档权限。你需通过云文档网页页面右上方 **「...」** -> **「...更多」** ->**「添加文档应用」** 入口为应用添加管理权限。          ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/22c027f63c540592d3ca8f41d48bb107_CSas7OYJBR.png?height=1994&maxWidth=550&width=3278)          **注意**：在 **添加文档应用** 前，你需确保目标应用至少开通了一个云文档或多维表格的 [API 权限](https://open.larkoffice.com/document/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list)。否则你将无法在文档应用窗口搜索到目标应用。     ![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/9f3353931fafeea16a39f0eb887db175_0tjzC9P3zU.png?maxWidth=550) - 如果你使用的是 `user_access_token`，意味着当前用户没有云文档权限。你需通过云文档网页页面右上方 **分享** 入口为当前用户添加管理权限。   ![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/3e052d3bac56f9441296ae22e2969d63_a2DEYrJup8.png?height=278&maxWidth=550&width=1383) 了解具体操作步骤或其它添加权限方式，参考[云文档常见问题 3](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a)。 |
| 400 | 1069604 | document not found | 检查文档是否存在 |


