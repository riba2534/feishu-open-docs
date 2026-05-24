---
title: "更新应用基础信息配置"
fullPath: "/uAjLw4CM/ukTMukTMukTM/application-v7/application-v7/application-base/patch"
updateTime: "1779344666000"
---

# 更新应用基础信息配置

通过该接口可更新自建应用的基础信息（名称、头像等），不传入的参数则保持不变，仅针对传入的参数则进行更新。如果应用正在审核中，则无法更新配置


> **Tip**: - 若用 user_access_token 代表某个终端用户操作API，则需确保该用户为应用的所有者、管理员、开发者，否则无法操作成功
> 
> - 若用 tenant_access_token 代表应用操作API，则仅可以操作应用自身


> **Warning**: - 仅支持更新[开发者后台](https://open.feishu.cn/app)创建的自建应用，不包含通过机器人助手等其他渠道创建的自建应用
> - 应用配置修改后需要[提交发布](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/application-v7/application-v7/application-publish/create)，并审核通过后才会在线上生效


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/application/v7/applications/:app_id/base |
| HTTP Method | PATCH |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
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
| `app_id` | `string` | 应用的app_id [如何获取应用的 App ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-app-id)<br>**示例值**："cli_a306c5476fb8d00c" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `i18ns` | `app_i18n_info\[\]` | 否 | 应用名称描述多语种<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` |
| &nbsp;&nbsp;└ `i18n_key` | `string` | 是 | 必填，国际化语言的 key<br>**示例值**："zh_cn"<br>**可选值有**：<br>- `zh_cn`: 中文 - `en_us`: 英文 - `ja_jp`: 日文 - `zh_hk`: 繁体中文(中国香港) - `zh_tw`: 繁体中文(中国台湾) - `id_id`: 印度尼西亚语 - `ms_my`: 马来语 - `de_de`: 德语 - `es_es`: 西班牙语 - `fr_fr`: 法语 - `it_it`: 意大利语 - `pt_br`: 葡萄牙语(巴西) - `vi_vn`: 越南语 - `ru_ru`: 俄语 - `th_th`: 泰语 - `ko_kr`: 韩语 |
| &nbsp;&nbsp;└ `name` | `string` | 否 | i18n_key对应的应用国际化名称<br>**示例值**："应用名称"<br>**数据校验规则**：<br>- 最小长度：`1` 字符 |
| &nbsp;&nbsp;└ `description` | `string` | 否 | 应用国际化描述（副标题）<br>**示例值**："应用描述"<br>**数据校验规则**：<br>- 最小长度：`1` 字符 |
| &nbsp;&nbsp;└ `help_use` | `string` | 否 | 帮助国际化文档链接<br>**示例值**："https://www.example.com" |
| `avatar_url` | `string` | 否 | 应用icon图片链接<br>**示例值**："https://s3-imfile.feishucdn.com/static-resource/v1/v2_953a8fc1-50bd-4b2e-87e2-b09e47dba23g"<br>**数据校验规则**：<br>- 最大长度：`512` 字符 |
| `homepage_url` | `string` | 否 | 应用管理后台url链接<br>**示例值**："https://open.feishu.cn/"<br>**数据校验规则**：<br>- 最大长度：`512` 字符 |


### 请求体示例

```json
{
    "i18ns": [
        {
            "i18n_key": "zh_cn",
            "name": "应用名称",
            "description": "应用描述",
            "help_use": "https://www.example.com"
        }
    ],
    "avatar_url": "https://s3-imfile.feishucdn.com/static-resource/v1/v2_953a8fc1-50bd-4b2e-87e2-b09e47dba23g",
    "homepage_url": "https://open.feishu.cn/"
}
```


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


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 404 | 210002 | The specified application does not exist | 指定的应用不存在，请检查传入的app_id参数是否正确 |
| 500 | 210003 | Internal server error | 服务内部错误，请稍候重试或联系技术支持(https://applink.feishu.cn/TLJpeNdW) |
| 400 | 210004 | This API only does not support to update ISV App, only support to update Self-Built App | 仅自建应用可以使用该API，请使用自建应用调用 |
| 403 | 210005 | As the App was created via Base, it cannot be updated using this API. | 仅可以操作开发者后台创建的应用，请使用开发者后台创建的应用调用该API |
| 403 | 210006 | Lack of permission to update other app. | 应用身份调用仅允许更新自身，请使用应用自身的身份调用该API |
| 403 | 210007 | The current user has no permission to modify the app configurations | 用户没有应用管理权限，请申请相关权限后再调用；或检查是否使用了正确的应用身份更新应用 |
| 400 | 210010 | Unable to update configurations, as the app is currently under review. | 应用正在审核中，不能进行该操作，请等待审核通过后再尝试 |
| 400 | 210011 | Param is invalid | 根据错误提示信息，检查参数是否符合要求 |
| 403 | 210021 | The specified application is not created via developer platform, can not modify by this API | 仅可以操作开发者后台创建的应用，请使用开发者后台创建的应用调用该API |


