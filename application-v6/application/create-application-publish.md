---
title: "提交发布自建应用"
fullPath: "/uAjLw4CM/ukTMukTMukTM/application-v7/application-v7/application-publish/create"
updateTime: "1779344724000"
---

# 提交发布自建应用

自建应用提交应用发布，如果当前自建应用没有待发布的版本，则会自动创建一个版本，如果有待发布的版本，则直接提交该版本。


> **Tip**: - 若用 user_access_token 代表某个终端用户操作API，则需确保该用户为应用的所有者、管理员，否则无法操作成功
> 
> - 若用 tenant_access_token 代表应用操作API，则仅可操作自身


> **Warning**: 仅支持发布[开发者后台](https://open.feishu.cn/app)创建的自建应用，不包含通过机器人助手等其他渠道创建的自建应用


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/application/v7/applications/:app_id/publish |
| HTTP Method | POST |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `application:application:patch` 修改应用信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | 应用的app_id [如何获取应用的 App ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-app-id)<br>**示例值**："cli_a508dbf34038d01c" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `mobile_default_ability` | `string` | 否 | 移动端默认能力<br>**注意**：如果应用开启了小程序、机器人或者网页应用能力，则该参数必填。<br>**示例值**："gadget"<br>**可选值有**：<br>- `gadget`: 小程序 - `web_app`: 网页应用 - `bot`: 机器人 |
| `pc_default_ability` | `string` | 否 | PC端默认能力<br>**注意**：如果应用开启了小程序、机器人或者网页应用能力，则该参数必填。<br>**示例值**："gadget"<br>**可选值有**：<br>- `gadget`: 小程序 - `web_app`: 网页应用 - `bot`: 机器人 |
| `remark` | `string` | 是 | 申请理由（500字符以内）<br>**示例值**："更新了移动端默认应用能力" |
| `changelog` | `string` | 是 | 更新描述（500字符以内）<br>**示例值**："更新了小程序的头像" |
| `version` | `string` | 否 | 应用版本号<br>**示例值**："1.1.1" |


### 请求体示例

```json
{
    "mobile_default_ability": "gadget",
    "pc_default_ability": "gadget",
    "remark": "更新了移动端默认应用能力",
    "changelog": "更新了小程序的头像",
    "version": "1.1.1"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `version_id` | `string` | 应用版本ID |
| &nbsp;&nbsp;└ `version` | `string` | 应用版本号 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "version_id": "oav_d317f090b7258ad0372aa53963cda70d",
        "version": "1.1.1"
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 210001 | As the app was not created in our developer console, it cannot be released using this API. | 仅可以操作开发者后台创建的应用，请使用开发者后台创建的应用调用该API |
| 400 | 210302 | Unable to submit the release request, as the app is currently under review. | 应用正在审核中，不能进行该操作，请等待审核通过后再尝试 |
| 500 | 210003 | Internal server error | 服务内部错误，请稍候重试或联系技术支持(https://applink.feishu.cn/TLJpeNdW) |
| 400 | 210303 | Invalid version number. The number should be in the form X.X.X | 版本号格式不对，且必须递增。请将版本号修改为X.X.X格式（如1.0.0）并确保版本号高于当前版本 |
| 400 | 210304 | Missing required fields | 检查必填字段是否填写 |
| 403 | 210036 | Lack of permission to update other app. | 应用身份调用仅允许更新自身，不允许更新其它应用。请使用应用自身的 app_id 调用该 API，或避免尝试更新其他应用。 |


