---
title: "获取数据知识"
fullPath: "/uAjLw4CM/ukTMukTMukTM/aily-v1/app-data_asset/get"
updateTime: "1752155000000"
---

# 获取数据知识

获取单个数据知识


> **Tip**: - 开发者需要 Aily 平台的应用协作者角色，包括管理员、开发者、运维人员
> - 使用应用身份仅支持[ Aily 平台](https://aily.feishu.cn)渠道的应用身份


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/aily/v1/apps/:app_id/data_assets/:data_asset_id |
| HTTP Method | GET |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `aily:data_asset:read` 获取智能伙伴创建平台数据知识资产 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | Aily 平台的应用的APPID，可以直接从 Aily 应用的URL中获取。获取示例：/ai/{APPID}<br>**示例值**："spring_feafdsaf__c"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `255` 字符 |
| `data_asset_id` | `string` | 数据知识ID，可通过在 Aily 平台查看知识详情页的url中获取，获取示例 https://***/ai/app_namespace/data/data-asset/data_asset_id<br>**示例值**："data_asset_dafefadsaf1"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `255` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `with_data_asset_item` | `boolean` | 否 | 结果是否包含数据与知识项<br>**示例值**：true |
| `with_connect_status` | `boolean` | 否 | 结果是否包含数据知识连接状态<br>**示例值**：true |
| `tenant_type` | `string` | 否 | 应用环境，默认为线上环境，dev代表开发环境<br>**示例值**：dev<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `data_asset` | `data_asset` | 数据知识 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `data_asset_id` | `string` | 数据知识ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `map<string, string>` | 数据知识标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `map<string, string>` | 数据知识描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `data_source_type` | `string` | 数据资源类型<br>**可选值有**：<br>- `excel`: excel - `pdf`: pdf - `pptx`: pptx - `txt`: txt - `docx`: docx - `mysql`: mysql - `postgresql`: postgresql - `larkbase`: 飞书多维表格 - `salesforce`: salesforce - `fenxiangxiaoke`: 分享逍客 - `qianchuan`: 巨量千川 - `clickhouse`: clickhouse - `databricks`: databricks - `servicedesk`: 飞书服务台 - `larkbiz_wiki`: 飞书Wiki - `larkbiz_doc`: 旧版飞书云文档，不支持 - `larkbiz_docs`: 飞书docs - `larkbiz_docx`: 新版飞书云文档，目前线上新创建的云文档均属于此类型 - `larkbiz_pdf`: 云盘/wiki中的pdf - `larkbiz_word`: 云盘/wiki中的.docx（Word文档） - `larkbiz_pptx`: 云盘/wiki中的.pptx（Powerpoint），不包括飞书幻灯片 - `larkbiz_sheets`: 飞书电子表格 - `larkbiz_base`: 飞书多维表格 - `larkbiz_personalfolder`: 飞书个人文件夹 - `larkbiz_sharedfolder`: 飞书共享文件夹 - `object`: 数据表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `connect_status` | `string` | 数据连接状态<br>**可选值有**：<br>- `awaiting`: 等待连接 - `syncing`: 连接中 - `successful`: 连接成功 - `continuously_syncing`: 增量同步中 - `partially_successful`: 部分成功 - `failed`: 连接失败 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `tags` | `data_asset_tag\[\]` | 数据知识分类列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `data_asset_tag_id` | `string` | 数据知识分类名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 数据知识分类ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `items` | `data_asset_item\[\]` | 数据知识项列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `data_asset_item_id` | `string` | 数据知识项ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `api_name` | `string` | 数据知识项标识 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `map<string, string>` | 数据知识项标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `map<string, string>` | 数据知识项描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `resources` | `data_asset_resource\[\]` | 数据知识资源 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `resource_id` | `string` | 数据知识资源ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `resource_type` | `string` | 数据知识资源类型<br>**可选值有**：<br>- `dataset`: 数据视图 - `vector`: 知识视图 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `connect_failed_reason` | `string` | 连接状态失败信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `connect_type` | `string` | 数据连接类型<br>**可选值有**：<br>- `import`: 导入 - `direct`: 直连 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `created_time` | `string` | 创建时间，毫秒时间戳 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `updated_time` | `string` | 更新时间，毫秒时间戳 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "data_asset": {
            "data_asset_id": "asset_aadg3mcgvpybu",
            "label": {
                "zh_ch": "电影评价"
            },
            "description": {
                "zh_ch": "这是一篇关于电影评价的文章"
            },
            "data_source_type": "excel",
            "connect_status": "successful",
            "tags": [
                {
                    "data_asset_tag_id": "spring_5862e4fea8__c__asset_tag_aadg2b5ql4gbs",
                    "name": "电影"
                }
            ],
            "items": [
                {
                    "data_asset_item_id": "asset_item_aadg3mcgvpydu",
                    "api_name": "movie",
                    "label": {
                        "zh_ch": "电影评价"
                    },
                    "description": {
                        "zh_ch": "电影评价信息"
                    },
                    "resources": [
                        {
                            "resource_id": "spring_5862e4fea8__c__dataset_aadg3lxm4j6mg",
                            "resource_type": "dataset"
                        }
                    ]
                }
            ],
            "connect_failed_reason": "连接超时",
            "connect_type": "direct",
            "created_time": "1711975665710",
            "updated_time": "1711975665710"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2700001 | param is invalid | 参数错误，请结合说明文档排查 |
| 404 | 2700404 | not found resource | 数据知识不存在 |
| 403 | 2701004 | permission denied | 无权限，请检查是否有开发者或者运维权限 |


