---
title: "列出工作流"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-block_workflow/list"
updateTime: "1770823266000"
---

# 列出工作流

此接口用于返回多维表格中所有工作流，多维表格管理员可通过此接口来管理表中的工作流


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/block_workflows |
| HTTP Method | GET |
| 接口频率限制 | [20 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `base:workflow:read` 查看自动化流程/工作流 `bitable:app` 查看、评论、编辑和管理多维表格 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `app_token` | `string` | 多维表格 App 的唯一标识。不同形态的多维表格，其 app_token 的获取方式不同： - 如果多维表格的 URL 以 ==**feishu.cn/base**== 开头，该多维表格的 app_token 是下图高亮部分：     ![app_token.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/6916f8cfac4045ba6585b90e3afdfb0a_GxbfkJHZBa.png?height=766&lazyload=true&width=3004)<br>- 如果多维表格的 URL 以 ==**feishu.cn/wiki**== 开头，你需调用知识库相关[获取知识空间节点信息](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get_node)接口获取多维表格的 app_token。当 obj_type 的值为 bitable 时，obj_token 字段的值才是多维表格的 app_token。<br>了解更多，参考[多维表格 app_token 获取方式](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/bitable-overview#-752212c)。<br>**示例值**："U9sGw5wyoiOIqdk1C4mcbYmMnbt"<br>**数据校验规则**：<br>- 长度范围：`1` ～ `200` 字符 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `workflows` | `block_workflow\[\]` | 工作流列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `workflow_id` | `string` | 工作流唯一键 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 工作流标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `string` | 工作流状态<br>**可选值有**：<br>- `Enable`: 启用 - `Disable`: 禁用 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "workflows": [
            {
                "workflow_id": "12412312421312",
                "title": "工作流",
                "status": "Enable"
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1254000 | WrongRequestJson | 请求体格式错误。请检查请求体格式是否符合 JSON 规范 |
| 400 | 1254001 | WrongRequestBody | 请求体参数有误。请检查请求体中是否已传入所有必填参数 |
| 400 | 1254002 | Fail | 内部错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1254003 | WrongBaseToken | app_token 错误，请检查是否从链接中截取了正确的 token 值 |
| 400 | 1254004 | WrongTableId | table_id 错误，请检查是否从链接中截取了正确的 table id 值 |
| 400 | 1254005 | WrongViewId | view id 错误，请检查是否从链接中截取了正确的 view id 值 |
| 400 | 1254006 | WrongRecordId | record id 错误，请检查是否从页面上获取正确的 record id |
| 400 | 1254007 | EmptyValue | 空值，请检查输入参数值 |
| 400 | 1254008 | EmptyView | 空视图，请检查查询的视图是否合法 |
| 400 | 1254009 | WrongFieldId | field id 错误，请检查 field id 是否合法 |
| 400 | 1254010 | ReqConvError | 请检查请求参数的类型或格式是否与接口要求一致，请检查请求参数是否有误 |
| 400 | 1254015 | Field types do not match. | 字段类型不匹配，请检查字段类型是否与多维表格中的字段类型一致 |
| 403 | 1254027 | UploadAttachNotAllowed | 附件未挂载, 禁止写入，请先上传并挂载附件 |
| 400 | 1254030 | InvalidPageToken | page token 错误，请从返回体中取出合法的 next page token 来作为请求的 page token |
| 400 | 1254036 | Bitable is copying, please try again later. | 操作的多维表格是一个副本，正在复制中，请稍后重试 |
| 400 | 1254037 | Invalid client token, make sure that it complies with the specification. | 幂等键为空，请检查幂等键是否为空 |
| 400 | 1254040 | BaseTokenNotFound | 多维表格 Token 不存在，请检查传入的 app token 是否合法 |
| 400 | 1254041 | TableIdNotFound | table_id 不存在，请检查传入的 table id 是否合法 |
| 400 | 1254042 | ViewIdNotFound | view id 不存在，请检查传入的 view id 是否合法 |
| 400 | 1254043 | RecordIdNotFound | record id 不存在，请检查传入的 record id 是否合法 |
| 400 | 1254044 | FieldIdNotFound | field id 不存在，请检查传入的 field id 是否存在 |
| 400 | 1254045 | FieldNameNotFound | 字段名称不存在，请检查传入的字段名称是否合法 |
| 400 | 1254060 | TextFieldConvFail | 多行文本单元格格式错误，请检查多行文本字段的格式或值是否符合要求 |


