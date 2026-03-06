---
title: "创建字段编组"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field_group/create"
updateTime: "1772538329000"
---

# 创建字段编组

该接口用于为多维表格数据表的字段创建编组。创建字段编组后，字段将被组织到该编组中，便于多维表格的数据管理
#### 业务使用场景
适用于多维表格字段较多，需要分类管理字段的场景


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/:table_id/field_groups |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `base:field_group:create` 创建字段编组 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_token` | `string` | 多维表格 App 的唯一标识。不同形态的多维表格，其 app_token 的获取方式不同： - 如果多维表格的 URL 以 ==**feishu.cn/base**== 开头，该多维表格的 app_token 是下图高亮部分：     ![app_token.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/6916f8cfac4045ba6585b90e3afdfb0a_GxbfkJHZBa.png?height=766&lazyload=true&width=3004)<br>- 如果多维表格的 URL 以 ==**feishu.cn/wiki**== 开头，你需调用知识库相关[获取知识空间节点信息](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get_node)接口获取多维表格的 app_token。当 obj_type 的值为 bitable 时，obj_token 字段的值才是多维表格的 app_token。<br>了解更多，参考[多维表格 app_token 获取方式](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/bitable-overview#-752212c)。<br>**示例值**："bascnv1jIEppJdTCn3jOosaxxxxx" |
| `table_id` | `string` | 多维表格数据表的唯一标识。获取方式： - 你可通过多维表格 URL 获取 `table_id`，下图高亮部分即为当前数据表的 `table_id` - 也可通过[列出数据表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/list)接口获取 `table_id`<br>  ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/18741fe2a0d3cafafaf9949b263bb57d_yD1wkOrSju.png?height=746&lazyload=true&maxWidth=700&width=2976)<br>**数据校验规则**：<br>- 长度范围：`0` ～ `50` 字符<br>**示例值**："tblz8nadEUdxNMt5" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `field_groups` | `field_group\[\]` | 是 | 要新增字段编组列表<br>**数据校验规则**：<br>- 长度范围：`1` ～ `300` |
| &nbsp;&nbsp;└ `id` | `string` | 否 | 字段编组的ID，默认由系统生成新的字段编组ID<br>**示例值**："fldPTb0U2y" |
| &nbsp;&nbsp;└ `name` | `string` | 是 | 字段编组的名称<br>**示例值**："用户信息组"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `100` 字符 - 正则校验：`^[^[\]]+$` |
| &nbsp;&nbsp;└ `children` | `field_group_child\[\]` | 是 | 字段编组的成员<br>**数据校验规则**：<br>- 长度范围：`1` ～ `300` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 是 | 编组成员类型<br>**示例值**："field"<br>**可选值有**：<br>- `field`: 字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 是 | 编组成员ID，必须与type的取值一致（如type为field时，id为字段的ID）；字段ID可以通过调用[获取字段列表]接口获取<br>**示例值**："fldPTb0U2y" |
| &nbsp;&nbsp;└ `description` | `string` | 否 | 字段编组的描述<br>**示例值**："用于组织用户信息相关的字段"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `2000` 字符 |


### 请求体示例

```json
{
    "field_groups": [
        {
            "id": "fldPTb0U2y",
            "name": "用户信息组",
            "children": [
                {
                    "type": "field",
                    "id": "fldPTb0U2y"
                }
            ],
            "description": "用于组织用户信息相关的字段"
        }
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
| &nbsp;&nbsp;└ `field_groups` | `string` | 字段编组的内容 |


### 响应体示例

```json
{"code":0,
"msg":"success",
"data":{"field_groups":"[   {     "id": "fldjX7dUj5",     "name": "编组1"   },   {     "id": "fldjX7dUj6",     "name": "编组2"   } ]"}}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1254000 | WrongRequestJson | 请求体错误，请检查请求体的格式是否符合接口要求（如JSON格式是否正确），或是否包含必填参数（如field_groups）。 |
| 400 | 1254001 | WrongRequestBody | 请求体错误，请检查请求体的格式是否符合接口要求（如JSON格式是否正确），或是否包含必填参数（如field_groups）。 |
| 500 | 1254002 | Fail | 内部错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1254003 | WrongBaseToken | 请检查app_token是否正确，获取方式参考[多维表格 app_token 获取方式](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/bitable-overview#-752212c) |
| 400 | 1254004 | WrongTableId | 请检查table_id是否正确，获取方式参考[列出数据表](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/list)接口或多维表格URL |
| 400 | 1254009 | WrongFieldId | 检查field_id是否正确，获取方式参考[获取字段列表](https://open.larkoffice.com/document/server-docs/docs/bitable-v1/app-table-field/list)接口 |
| 400 | 1254036 | Bitable is copying, please try again later. | 复制多维表格为异步操作，该错误码表示当前多维表格仍在复制中，在复制期间无法操作当前多维表格。需要等待复制完成后再操作 |
| 404 | 1254040 | BaseTokenNotFound | 请检查app_token是否存在，获取方式参考[多维表格 app_token 获取方式](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/bitable-overview#-752212c) |
| 404 | 1254041 | TableIdNotFound | 请检查table_id是否存在，获取方式参考[列出数据表](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/list)接口或多维表格URL |
| 404 | 1254044 | FieldIdNotFound | 请检查field_id是否存在，获取方式参考[获取字段列表](https://open.larkoffice.com/document/server-docs/docs/bitable-v1/app-table-field/list)接口 |
| 400 | 1254114 | The name of field group is empty | 字段编组的名称不可以为空 |
| 400 | 1254115 | The name of field group is invalid | 字段编组的名称无效，请检查字段编组的名称是否符合要求（如长度范围1~100字符，正则校验^[^[\]]+$） |
| 400 | 1254116 | The description of field group is too long | 字段编组的描述过长，请将描述缩短至2000字符以内（参考请求体参数中description字段的长度限制） |
| 400 | 1254117 | The name of field group is duplicated | 字段编组的名称重复 |
| 400 | 1254118 | The children of field group is empty | 字段编组内未包含子成员 |
| 400 | 1254119 | The children of field group is too large | 一个字段编组内最多包含300个子元素 |
| 400 | 1254120 | The field groups to be created is empty | 待创建的字段编组数量为空 |
| 400 | 1254121 | The field groups to be created is too large | 单次最多支持创建300个字段编组 |
| 400 | 1254122 | Child belongs to multiple field groups | 子元素不允许被多个字段编组引用 |
| 400 | 1254123 | The child type of field group is invalid | 字段编组的子元素类型无效，请检查字段编组的子元素类型是否为允许的值（如type为field时，id为字段的ID， 字段ID可通过[获取字段列表](https://open.larkoffice.com/document/server-docs/docs/bitable-v1/app-table-field/list)接口获取) |
| 400 | 1254290 | TooManyRequest | 请求过快，稍后重试 |
| 400 | 1254291 | Write conflict | 同一个数据表(table) 不支持并发调用写接口，请检查是否存在并发调用写接口。写接口包括：新增、修改、删除记录；新增、修改、删除字段；修改表单；修改视图；升级表单等。 |
| 403 | 1254302 | Permission denied. | 调用身份缺少多维表格的高级权限。你需要为调用身份授予高级权限： - 对用户授予高级权限，你需要在多维表格页面右上方 **分享** 入口为当前用户添加可管理权限。![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/df3911b4f747d75914f35a46962d667d_dAsfLjv3QC.png?height=546&lazyload=true&maxWidth=550) - 对应用授予高级权限，你需通过多维表格页面右上方 **「...」** -> **「...更多」** ->**「添加文档应用」** 入口为应用添加可管理权限。          ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/22c027f63c540592d3ca8f41d48bb107_CSas7OYJBR.png?height=1994&maxWidth=550&width=3278)          ![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/9f3353931fafeea16a39f0eb887db175_0tjzC9P3zU.png?maxWidth=550)     **注意**：     在 **添加文档应用** 前，你需确保目标应用至少开通了一个多维表格的 [API 权限](https://open.larkoffice.com/document/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list)。否则你将无法在文档应用窗口搜索到目标应用。     - 你也可以在 **多维表格高级权限设置** 中添加用户或一个包含应用的群组, 给予这个群自定义的读写等权限。 |
| 403 | 1254304 | You are not authorized to perform this operation. | 仅企业版和旗舰版飞书支持行列权限 |
| 500 | 1254607 | Data not ready, please try again later | 该报错一般是由于前置操作未执行完成，或本次操作数据太大，服务器计算超时导致。遇到该错误码时，建议等待一段时间后重试。通常有以下几种原因： - **编辑操作频繁**：开发者对多维表格的编辑操作非常频繁。可能会导致由于等待前置操作处理完成耗时过长而超时的情况。多维表格底层对数据表的处理基于版本维度的串行方式，不支持并发。因此，并发请求时容易出现此类错误，不建议开发者对单个数据表进行并发请求。 - **批量操作负载重**：开发者在多维表格中进行批量新增、删除等操作时，如果数据表的数据量非常大，可能会导致单次请求耗时过长，最终导致请求超时。建议开发者适当降低批量请求的 page_size 以减少请求耗时。 - **资源分配与计算开销**：资源分配是基于单文档维度的，如果读接口涉及公式计算、排序等计算逻辑，会占用较多资源。例如，并发读取一个文档下的多个数据表也可能导致该文档阻塞。 |
| 500 | 1255001 | internal error | 内部错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1254200 | Something went wrong | 内部错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1255003 | MarshalError | 序列化错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1255004 | UmMarshalError | 反序列化错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 504 | 1255040 | Request timed out, please try again later | 进行重试 |


