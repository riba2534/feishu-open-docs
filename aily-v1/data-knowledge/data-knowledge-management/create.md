---
title: "创建数据知识"
fullPath: "/uAjLw4CM/ukTMukTMukTM/aily-v1/app-data_asset/create"
updateTime: "1752154988000"
---

# 创建数据知识

在 Aily 中添加单个数据知识


> **Tip**: - 仅支持开发环境
> - 开发者需要 Aily 平台的应用协作者角色，包括管理员、开发者、运维人员
> - 使用应用身份仅支持[ Aily 平台](https://aily.feishu.cn)渠道的应用身份


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/aily/v1/apps/:app_id/data_assets |
| HTTP Method | POST |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `aily:data_asset:write` 创建、更新、删除智能伙伴创建平台数据知识资产 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_id` | `string` | Aily 平台的应用的APPID，可以直接从 Aily 应用的URL中获取。获取示例：/ai/{APPID}<br>**示例值**："spring_dfasdf__c"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `tenant_type` | `string` | 否 | 应用环境，枚举值： - `online`：线上环境（默认值） - `dev`：开发环境；目前只支持 `dev`<br>**示例值**：dev<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `connect_type` | `string` | 是 | 连接类型<br>**示例值**："direct"<br>**可选值有**：<br>- `import`: 导入模式 - `direct`: 直连模式<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| `source_type` | `string` | 是 | 数据源类型<br>**示例值**："file"<br>**可选值有**：<br>- `file`: 文件，只支持导入模式 - `lark_wiki_space`: 飞书知识空间，只支持直连模式 - `lark_doc`: 飞书云文档，导入模式只支持docx - `lark_helpdesk`: 飞书服务台，只支持直连模式<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| `import_knowledge_setting` | `data_asset_import_knowledge_setting` | 否 | 知识导入配置 |
| &nbsp;&nbsp;└ `chunk_setting` | `data_asset_knowledge_chunk_setting` | 否 | 知识切片配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rule_type` | `string` | 是 | 切片规则<br>**示例值**："intelligent"<br>**可选值有**：<br>- `separator`: 按标识符 - `intelligent`: 智能切片<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `separate_type` | `string` | 否 | 切片分割符类型<br>**示例值**："paragraph"<br>**可选值有**：<br>- `paragraph`: 段落分隔符："\n\n"、"\n"、空格 - `title`: 标题分割符：######<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 否 | 分段最大长度（字符），按标识符切片时必须填写<br>**示例值**：600<br>**数据校验规则**：<br>- 取值范围：`200` ～ `1000` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `overlap` | `int` | 否 | 分段重叠字符数，按标识符切片时必须填写，不能超过size的数值<br>**示例值**：10<br>**数据校验规则**：<br>- 取值范围：`0` ～ `200` |
| &nbsp;&nbsp;└ `file` | `data_asset_import_knowledge_file` | 否 | 知识导入-文件 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 文件标题<br>**示例值**："文件标题"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 否 | 上传文件获取到的token。和content二选一，优先使用token。<br>**示例值**："bb690637b49440b08f39459a2fdcd2ca"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 否 | 文件内容。和token二选一，优先使用token。有长度限制，大文件优先使用token方式。<br>**示例值**："这是文件内容"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `65536` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 否 | 文件内容对应的 MIME 类型，必须填写 可选值： - text/plain (.txt) - application/pdf (.pdf) - application/vnd.openxmlformats-officedocument.presentationml.presentation (.pptx) - application/vnd.openxmlformats-officedocument.wordprocessingml.document (.docx)<br>**示例值**："application/pdf"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 文件源的URL<br>**示例值**："https://document.com/1"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `65535` 字符 |
| &nbsp;&nbsp;└ `lark_doc` | `data_asset_import_knowledge_lark_doc` | 否 | 知识导入-飞书云文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 是 | 云文档类型<br>**示例值**："docx"<br>**可选值有**：<br>- `doc`: 飞书文档 - `file`: 飞书文件 - `wiki`: 飞书知识库 - `docx`: 飞书新版文档 - `folder`: 飞书文件夹<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 是 | 云文档token，可以通过[搜索云文档](https://open.larkoffice.com/document/server-docs/docs/drive-v1/search/document-search)API获取<br>**示例值**："T8FAcuilgC1fdaxkt58vcp91xngh"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `with_sub_docs` | `boolean` | 否 | 是否包含子文档，只有wiki类型的云文档支持<br>**示例值**：false |
| &nbsp;&nbsp;└ `lark_wiki_space` | `data_asset_import_knowledge_wiki` | 否 | 知识导入-飞书知识空间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `space_id` | `string` | 是 | 飞书知识空间ID，可以通过[搜索 Wiki](https://open.larkoffice.com/document/server-docs/docs/wiki-v2/search_wiki)API获取<br>**示例值**："798546548961351"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_docs` | `data_asset_import_knowledge_wiki_sub_doc\[\]` | 否 | 指定知识空间子节点时使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 是 | 云文档类型，只支持wiki中的云文档<br>**示例值**："wiki"<br>**可选值有**：<br>- `wiki`: 飞书知识库<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `token` | `string` | 是 | 云文档token，可以通过[搜索云文档](https://open.larkoffice.com/document/server-docs/docs/drive-v1/search/document-search)API获取<br>**示例值**："T8FAcuilgC1fdaxkt58vcp91xngh"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 云文档链接<br>**示例值**："https://cdas.feishu.cn/wiki/fdisu1"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `65535` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 知识空间URL<br>**示例值**："https://ai-tenant.feishu-boe.cn/wiki/space/7283525110814736404"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `65535` 字符 |
| &nbsp;&nbsp;└ `lark_helpdesk` | `data_asset_import_knowledge_helpdesk` | 否 | 知识导入-飞书服务台 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `helpdesk_id` | `string` | 是 | 飞书服务台ID，可以通过[服务台-接入指南](https://open.larkoffice.com/document/server-docs/helpdesk-v1/access-guide) 获取<br>**示例值**："123"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| `description` | `map<string, string>` | 否 | 数据知识描述信息<br>**示例值**：{"zh_cn":"描述"} |


### 请求体示例

```json
{
    "connect_type": "direct",
    "source_type": "file",
    "import_knowledge_setting": {
        "chunk_setting": {
            "rule_type": "intelligent",
            "separate_type": "paragraph",
            "size": 600,
            "overlap": 10
        },
        "file": {
            "title": "文件标题",
            "token": "bb690637b49440b08f39459a2fdcd2ca",
            "content": "这是文件内容",
            "mime_type": "application/pdf",
            "url": "https://document.com/1"
        },
        "lark_doc": {
            "type": "docx",
            "token": "T8FAcuilgC1fdaxkt58vcp91xngh",
            "with_sub_docs": false
        },
        "lark_wiki_space": {
            "space_id": "798546548961351",
            "sub_docs": [
                {
                    "type": "wiki",
                    "token": "T8FAcuilgC1fdaxkt58vcp91xngh",
                    "url": "https://cdas.feishu.cn/wiki/fdisu1"
                }
            ],
            "url": "https://ai-tenant.feishu-boe.cn/wiki/space/7283525110814736404"
        },
        "lark_helpdesk": {
            "helpdesk_id": "123"
        }
    },
    "description": {
        "zh_cn": "描述"
    }
}
```


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
| &nbsp;&nbsp;&nbsp;&nbsp;└ `data_source_type` | `string` | 数据资源类型<br>**可选值有**：<br>- `excel`: excel - `pdf`: pdf - `pptx`: pptx - `txt`: txt - `docx`: docx - `mysql`: mysql - `postgresql`: postgresql - `larkbase`: 飞书多维表格 - `salesforce`: salesforce - `fenxiangxiaoke`: 分享逍客 - `qianchuan`: 巨量千川 - `clickhouse`: clickhouse - `databricks`: databricks - `servicedesk`: 飞书服务台 - `larkbiz_wiki`: 飞书Wiki - `larkbiz_doc`: 旧版飞书云文档，目前已不支持 - `larkbiz_docs`: 飞书docs - `larkbiz_docx`: 新版飞书云文档，当前创建的飞书云文档均为此类型 - `larkbiz_pdf`: 云盘/wiki中的pdf文件pdf文件 - `larkbiz_word`: 云盘/wiki中的.docx（Word） - `larkbiz_pptx`: 云盘/wiki中的.pptx（Powerpoint） - `larkbiz_sheets`: 飞书电子表格 - `larkbiz_base`: 飞书多维表格 - `larkbiz_personalfolder`: 飞书个人文件夹 - `larkbiz_sharedfolder`: 飞书共享文件夹 - `object`: 数据表 |
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
                "zh_cn": "标题"
            },
            "description": {
                "zh_cn": "描述"
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
                        "zh_cn": "标题"
                    },
                    "description": {
                        "zh_cn": "描述"
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
| 403 | 2701004 | permission denied | 无权限，请检查是否有开发者或者运维权限 |
| 400 | 2700026 | only support development environment | 仅支持开发环境操作 |
| 400 | 2700027 | only supports uploading a single file | 仅支持上传单个文件 |
| 400 | 2700028 | invalid chunk setting parameter | 无效的切片参数 |
| 400 | 2700029 | the data source information is invalid | 数据源信息无效 |
| 400 | 2700030 | data source not found | 未找到数据源 |
| 403 | 2700031 | import cloud document permission check failed | 导入云文档权限检查失败，操作者需要有云文档的下载权限 |
| 400 | 2700032 | unsupported data connection type | 不支持的数据连接类型，请结合文档排查 |
| 400 | 2700033 | unsupported data source type | 不支持的数据源类型，请结合文档排查 |
| 400 | 2700034 | unsupported file types | 不支持的文件类型 |
| 400 | 2700460 | failed to get doc meta | 获取云文档元信息失败，请检查云文档参数是否正确以及操作者是否拥有相关文档的权限 |
| 400 | 2700036 | cloud document-related resources only support user identity calls | 云文档相关资源仅支持用户身份调用 |
| 400 | 2700472 | some param miss or invalid | 请求参数缺失或者不合法 |


