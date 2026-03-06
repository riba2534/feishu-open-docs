---
title: "搜索文档"
fullPath: "/uAjLw4CM/ukTMukTMukTM/search-v2/doc_wiki/search"
updateTime: "1769653253000"
---

# 文档搜索

该接口用于根据搜索关键词（query）对当前用户可见的云文档进行搜索{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=search&version=v2&resource=doc_wiki&method=search)

:::html
<md-alert type="tip">

</md-alert>
:::

:::html
<md-alert type="warn">

</md-alert>
:::

:::html
<md-alert type="error">

</md-alert>
:::



## 请求
:::html
<md-table>
  <md-thead>
  <tr>
      <md-th>基本</md-th>
      <md-th></md-th>
  </tr>
  </md-thead>
  <md-tbody>
    <md-tr>
      <md-th>HTTP URL</md-th>
      <md-td>https://open.feishu.cn/open-apis/search/v2/doc_wiki/search</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[100 次/分钟](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
    </md-tr>
    <md-tr>
      <md-th>支持的应用类型</md-th>
      <md-td>
      <md-app-support types="custom,isv"></md-app-support>
      </md-td>
    </md-tr>
    <md-tr>
      <md-th>
            权限要求
            <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
            
      </md-th>
      <md-td>
            <md-perm name="search:docs:read" desc="搜索云文档" support_app_types="custom,isv" tags="">搜索云文档</md-perm>
      </md-td>
    </md-tr>
  </md-tbody>
</md-table>
:::
### 请求头
:::html
<md-table>
  <md-thead>
    <md-tr>
      <md-th style="width: 35%;">名称</md-th>
      <md-th style="width: 13%;">类型</md-th>
       <md-th style="width: 15%;" filters="是,否" >必填</md-th>
      <md-th  style="width: 37%;">描述</md-th>
    </md-tr>
  </md-thead>
  <md-tbody>
    <md-tr>
      <md-td>Authorization</md-td>
      <md-td>string</md-td>
      <md-td>是</md-td>
      	<md-td>
<md-tag mode="inline" type="token-user">user_access_token</md-tag>

**值格式**："Bearer `access_token`"

**示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560"

[了解更多：如何选择与获取 access token](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

</md-td>
</md-tr>
<md-tr>
<md-td>Content-Type</md-td>
<md-td>string</md-td>
<md-td>是</md-td>
<md-td>**固定值**："application/json; charset=utf-8"</md-td>
</md-tr>
</md-tbody>
</md-table>
:::



### 请求体

:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 15%;" filters="是,否" >必填</md-dt-th>
      <md-dt-th style="width: 37%;">描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>

<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >query</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	搜索关键词（query至少搭配一种doc/wiki筛选器）

**示例值**："飞书文档使用指南"

**数据校验规则**：

- 长度范围：`0` ～ `50` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >doc_filter</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >doc_filter</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文档过滤参数

**示例值**：{"folder_tokens": ["fld_123456"]}
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >creator_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文档所有者OpenID

**示例值**：["ou_789012"]

**数据校验规则**：

- 长度范围：`0` ～ `20`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >doc_types</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文档类型

**示例值**：["SHORTCUT"]

**可选值有**：
<md-enum>
<md-enum-item key="DOC" >文档</md-enum-item>
<md-enum-item key="SHEET" >表格</md-enum-item>
<md-enum-item key="BITABLE" >多维表格</md-enum-item>
<md-enum-item key="MINDNOTE" >思维导图</md-enum-item>
<md-enum-item key="FILE" >文件</md-enum-item>
<md-enum-item key="WIKI" >wiki</md-enum-item>
<md-enum-item key="DOCX" >新版文档</md-enum-item>
<md-enum-item key="FOLDER" >space文件夹</md-enum-item>
<md-enum-item key="CATALOG" >wiki2.0文件夹</md-enum-item>
<md-enum-item key="SLIDES" >新版本幻灯片</md-enum-item>
<md-enum-item key="SHORTCUT" >快捷方式</md-enum-item>
</md-enum>

**数据校验规则**：

- 长度范围：`0` ～ `10`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >folder_tokens</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	搜索文件夹内的文档（文件夹token列表）
注：如果存在该字段则wiki筛选器失效

**示例值**：["fld_123456"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >only_title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	仅搜文档标题

**示例值**：false

**默认值**：`false`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >open_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >time_range</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	浏览文档的时间范围（秒级时间戳，包含start和end字段）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	时间范围的起始时间戳

**示例值**：1742348544

**数据校验规则**：

- 取值范围：`0` ～ `9223372036854775807`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	时间范围的截止时间戳

**示例值**：1742348544

**数据校验规则**：

- 取值范围：`0` ～ `9223372036854775807`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >sort_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	排序方式

**示例值**："CREATE_TIME"

**可选值有**：
<md-enum>
<md-enum-item key="DEFAULT_TYPE" >默认排序</md-enum-item>
<md-enum-item key="OPEN_TIME" >User打开时间排序</md-enum-item>
<md-enum-item key="EDIT_TIME" >User编辑时间降序</md-enum-item>
<md-enum-item key="EDIT_TIME_ASC" >User编辑时间升序</md-enum-item>
<md-enum-item key="ENTITY_CREATE_TIME_ASC" >实体创建时间升序</md-enum-item>
<md-enum-item key="ENTITY_CREATE_TIME_DESC" >实体创建时间降序</md-enum-item>
<md-enum-item key="CREATE_TIME" >按文档创建时间排序</md-enum-item>
<md-enum-item key="CREATE_TIME_ASC" >按文档创建时间正序（该排序暂不支持）</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >time_range</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文档创建的时间范围（秒级时间戳，包含start和end字段）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	时间范围的起始时间戳

**示例值**：1742348544

**数据校验规则**：

- 取值范围：`0` ～ `9223372036854775807`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	时间范围的截止时间戳

**示例值**：1742348544

**数据校验规则**：

- 取值范围：`0` ～ `9223372036854775807`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >wiki_filter</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >wiki_filter</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Wiki过滤参数

**示例值**：{"creator_ids": ["ou_789012"], "space_ids": ["space_123456"]}
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >creator_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Wiki所有者OpenID

**示例值**：["ou_7890123456abcdef"]

**数据校验规则**：

- 长度范围：`0` ～ `20`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >doc_types</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Wiki类型

**示例值**：["SHORTCUT"]

**可选值有**：
<md-enum>
<md-enum-item key="DOC" >文档</md-enum-item>
<md-enum-item key="SHEET" >表格</md-enum-item>
<md-enum-item key="BITABLE" >多维表格</md-enum-item>
<md-enum-item key="MINDNOTE" >思维导图</md-enum-item>
<md-enum-item key="FILE" >文件</md-enum-item>
<md-enum-item key="WIKI" >维基</md-enum-item>
<md-enum-item key="DOCX" >新版文档</md-enum-item>
<md-enum-item key="FOLDER" >space文件夹</md-enum-item>
<md-enum-item key="CATALOG" >wiki2.0文件夹</md-enum-item>
<md-enum-item key="SLIDES" >新版本幻灯片</md-enum-item>
<md-enum-item key="SHORTCUT" >快捷方式</md-enum-item>
</md-enum>

**数据校验规则**：

- 长度范围：`0` ～ `10`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >space_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	搜索某个Space下的Wiki（Space ID列表）

**示例值**：["space_1234567890fedcba"]

**数据校验规则**：

- 长度范围：`0` ～ `50`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >only_title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	仅搜Wiki标题

**示例值**：false

**默认值**：`false`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >open_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >time_range</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	浏览文档的时间范围（秒级时间戳，包含start和end字段）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	时间范围的起始时间戳

**示例值**：1742348544

**数据校验规则**：

- 取值范围：`0` ～ `9223372036854775807`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	时间范围的截止时间戳

**示例值**：1742348544

**数据校验规则**：

- 取值范围：`0` ～ `9223372036854775807`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >sort_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	排序方式

**示例值**："CREATE_TIME"

**可选值有**：
<md-enum>
<md-enum-item key="DEFAULT_TYPE" >默认排序</md-enum-item>
<md-enum-item key="OPEN_TIME" >User打开时间排序</md-enum-item>
<md-enum-item key="EDIT_TIME" >User编辑时间降序</md-enum-item>
<md-enum-item key="EDIT_TIME_ASC" >User编辑时间升序</md-enum-item>
<md-enum-item key="ENTITY_CREATE_TIME_ASC" >实体创建时间升序</md-enum-item>
<md-enum-item key="ENTITY_CREATE_TIME_DESC" >实体创建时间降序</md-enum-item>
<md-enum-item key="CREATE_TIME" >按文档创建时间排序</md-enum-item>
<md-enum-item key="CREATE_TIME_ASC" >按文档创建时间正序（该排序暂不支持）</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >time_range</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Wiki创建的时间范围（秒级时间戳，包含start和end字段）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >start</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	时间范围的起始时间戳

**示例值**：1742348544

**数据校验规则**：

- 取值范围：`0` ～ `9223372036854775807`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >end</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	时间范围的截止时间戳

**示例值**：1742348544

**数据校验规则**：

- 取值范围：`0` ～ `9223372036854775807`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >page_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果

**示例值**："token_1234567890fedcba"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >page_size</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	分页大小

**示例值**：15

**默认值**：`0`

**数据校验规则**：

- 取值范围：`0` ～ `20`
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "query": "飞书文档使用指南",
    "doc_filter": {
        "creator_ids": [
            "ou_789012"
        ],
        "doc_types": [
            "SHORTCUT"
        ],
        "folder_tokens": [
            "fld_123456"
        ],
        "only_title": false,
        "open_time": {
            "start": 1742348544,
            "end": 1742348544
        },
        "sort_type": "CREATE_TIME",
        "create_time": {
            "start": 1742348544,
            "end": 1742348544
        }
    },
    "wiki_filter": {
        "creator_ids": [
            "ou_7890123456abcdef"
        ],
        "doc_types": [
            "SHORTCUT"
        ],
        "space_ids": [
            "space_1234567890fedcba"
        ],
        "only_title": false,
        "open_time": {
            "start": 1742348544,
            "end": 1742348544
        },
        "sort_type": "CREATE_TIME",
        "create_time": {
            "start": 1742348544,
            "end": 1742348544
        }
    },
    "page_token": "token_1234567890fedcba",
    "page_size": 15
}
</md-code-json>
:::



## 响应





### 响应体
:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 52%;">描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>

<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	错误码，非 0 表示失败
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >msg</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	错误描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >\-</md-text>
	</md-dt-td>
	<md-dt-td>
	\-
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >total</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	匹配结果总数（辅助分页参考）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >has_more</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否还有更多项
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >res_units</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >doc_res_unit\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	搜索结果列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >title_highlighted</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	标题高亮
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >summary_highlighted</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	摘要高亮
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >entity_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	结果类型

**可选值有**：
<md-enum>
<md-enum-item key="DOC" >doc实体</md-enum-item>
<md-enum-item key="WIKI" >wiki类型</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >result_meta</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >doc_meta</md-text>
	</md-dt-td>
	<md-dt-td>
	文档搜索元信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >doc_types</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文档类型

**可选值有**：
<md-enum>
<md-enum-item key="DOC" >文档</md-enum-item>
<md-enum-item key="SHEET" >表格</md-enum-item>
<md-enum-item key="BITABLE" >多维表格</md-enum-item>
<md-enum-item key="MINDNOTE" >思维导图</md-enum-item>
<md-enum-item key="FILE" >文件</md-enum-item>
<md-enum-item key="WIKI" >维基</md-enum-item>
<md-enum-item key="DOCX" >新版文档</md-enum-item>
<md-enum-item key="FOLDER" >space文件夹</md-enum-item>
<md-enum-item key="CATALOG" >wiki2.0文件夹</md-enum-item>
<md-enum-item key="SLIDES" >新版本幻灯片</md-enum-item>
<md-enum-item key="SHORTCUT" >快捷方式</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >update_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	更新时间戳（秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文档链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >owner_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	所有者名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >owner_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	所有者OpenID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_cross_tenant</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否跨租户
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	文档创建时间戳（秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >last_open_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	上次打开时间戳（秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >edit_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最后一次编辑用户OpenID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >edit_user_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	最后一次编辑用户名称
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文档token
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >page_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
	</md-dt-td>
</md-dt-tr>


  </md-dt-tbody>
</md-dt-table>
:::



### 响应体示例
:::html
<md-code-json>
{
    "code": 0,
    "msg": "success",
    "data": {
        "total": 100,
        "has_more": true,
        "res_units": [
            {
                "title_highlighted": "<h>飞书文档</h>使用指南",
                "summary_highlighted": "本文介绍<h>飞书文档</h>的创建、编辑与分享功能",
                "entity_type": "DOC",
                "result_meta": {
                    "doc_types": "SHORTCUT",
                    "update_time": 1766567446,
                    "url": "https://www.feishu.cn/docs/dox-1234567890abcdef",
                    "owner_name": "张三",
                    "owner_id": "ou-7890123456abcdef",
                    "is_cross_tenant": false,
                    "create_time": 1766567446,
                    "last_open_time": 1766567446,
                    "edit_user_id": "ou-1122334455aabbcc",
                    "edit_user_name": "李四",
                    "token": "dox_9876543210fedcba"
                }
            }
        ],
        "page_token": "token_1234567890fedcba"
    }
}
</md-code-json>
:::



### 错误码
:::html
<md-table>
    <md-thead>
        <md-tr>
            <md-th style="width: 15%;">HTTP状态码</md-th>
            <md-th style="width: 15%;">错误码</md-th>
            <md-th style="width: 30%;">描述</md-th>
            <md-th style="width: 30%;">排查建议</md-th>
        </md-tr>
    </md-thead>
  <md-tbody>

<md-tr>
  <md-td>400</md-td>
  <md-td>1274001</md-td>
  <md-td>invalid param: missing required fields</md-td>
  <md-td>检查请求头和请求体中是否包含必要的认证信息且字段是否完整</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1274002</md-td>
  <md-td>invalid param: illegal enum value</md-td>
  <md-td>验证枚举字段的值是否符合定义的合法枚举范围</md-td>
</md-tr>


<md-tr>
  <md-td>401</md-td>
  <md-td>1274011</md-td>
  <md-td>user_access_token is invalid or expired</md-td>
  <md-td>检查user_access_token是否正确或过期</md-td>
</md-tr>


<md-tr>
  <md-td>429</md-td>
  <md-td>1277001</md-td>
  <md-td>rate limit exceeded</md-td>
  <md-td>检查当前请求频率是否超过接口限制阈值</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




