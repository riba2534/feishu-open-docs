---
title: "获取知识空间节点信息"
fullPath: "/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get_node"
updateTime: "1749710137000"
---

# 获取知识空间节点信息

获取知识空间节点信息


> **Tip**: 知识库权限要求，当前使用的 access token 所代表的应用或用户拥有：
> - 节点阅读权限


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/wiki/v2/spaces/get_node |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `wiki:node:read` 查看知识空间节点信息 `wiki:wiki` 查看、编辑和管理知识库 `wiki:wiki:readonly` 查看知识库 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `token` | `string` | 是 | 知识库节点或对应云文档的实际 token。 - 知识库节点 token：如果 URL 链接中 token 前为 wiki，该 token 为知识库的节点 token。 - 云文档实际 token：如果 URL 链接中 token 前为 docx、base、sheets 等非 wiki 类型，则说明该 token 是当前云文档的实际 token。<br>了解更多，请参考[文档常见问题-如何获取云文档资源相关 token（id）](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)。<br>**注意**：<br>使用云文档 token 查询时，需要对 obj_type 参数传入文档对应的类型。<br>**示例值**：wikcnKQ1k3p******8Vabcef<br>**数据校验规则**：<br>- 长度范围：`0` ～ `999` 字符 |
| `obj_type` | `string` | 否 | 文档类型。不传时默认以 wiki 类型查询。<br>**示例值**：docx<br>**可选值有**：<br>- `doc`: 旧版文档 - `docx`: 新版文档 - `sheet`: 表格 - `mindnote`: 思维导图 - `bitable`: 多维表格 - `file`: 文件 - `slides`: 幻灯片 - `wiki`: 知识库节点<br>**默认值**：`wiki` |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `node` | `node` | 节点信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `space_id` | `string` | 知识空间 ID。获取方式参考[知识库概述](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-overview)。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_token` | `string` | 知识库节点 token，如果 URL 链接中 token 前为 wiki，该 token 为知识库的节点 token。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `obj_token` | `string` | 节点的实际云文档的 token，如果 URL 链接中 token 前为 docx、base、sheets 等非 wiki 类型，则说明该 token 是当前云文档的实际 token。如果要获取或编辑节点内容，需要使用此 token 调用对应的接口。可根据 obj_type 判断属于哪种文档类型。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `string` | 文档类型，对于快捷方式，该字段是对应的实体的obj_type。<br>**可选值有**：<br>- `doc`: 旧版文档 - `sheet`: 表格 - `mindnote`: 思维导图 - `bitable`: 多维表格 - `file`: 文件 - `docx`: 新版文档 - `slides`: 幻灯片 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `parent_node_token` | `string` | 父节点 token。若当前节点为一级节点，父节点 token 为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_type` | `string` | 节点类型<br>**可选值有**：<br>- `origin`: 实体 - `shortcut`: 快捷方式 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `origin_node_token` | `string` | 快捷方式对应的实体node_token，当节点为快捷方式时，该值不为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `origin_space_id` | `string` | 快捷方式对应的实体所在的space id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `has_child` | `boolean` | 是否有子节点 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `obj_create_time` | `string` | 文档创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `obj_edit_time` | `string` | 文档最近编辑时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_create_time` | `string` | 节点创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `string` | 文档创建者 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `owner` | `string` | 文档所有者 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `node_creator` | `string` | 节点创建者 |


### 响应体示例

```json
// 使用Wiki Token查询：GET open-apis/wiki/v2/spaces/get_node?token=wikcnKQ1k3p******8Vabcef
// 或使用文档Token查询：GET open-apis/wiki/v2/spaces/get_node?token=doccnzAaOD******Wabcdef&obj_type=doc
{
    "code": 0,
    "msg": "success",
    "data": {
        "node": {
            "space_id": "6946843325487912356",
            "node_token": "wikcnKQ1k3p******8Vabcef",
            "obj_token": "doccnzAaOD******Wabcdef",
            "obj_type": "doc",
            "parent_node_token": "wikcnKQ1k3p******8Vabcef",
            "node_type": "origin",
            "origin_node_token": "wikcnKQ1k3p******8Vabcef",
            "origin_space_id": "6946843325487912356",
            "has_child": false,
            "title": "标题",
            "obj_create_time": "1642402428",
            "obj_edit_time": "1642402428",
            "node_create_time": "1642402428",
            "creator": "ou_xxxxx",
            "owner": "ou_xxxxx",
            "node_creator": "ou_xxxxx",
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 131001 | rpc fail | 服务报错，请稍后重试，或者拿响应体的header头里的x-tt-logid咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)定位。 |
| 400 | 131002 | param err | 通常为传参有误，例如数据类型不匹配。请查看**具体接口报错信息**，报错不明确时请咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)。 |
| 400 | 131004 | invalid user | 非法用户。请咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)。 |
| 400 | 131005 | not found | 未找到相关数据，例如id不存在。相关报错信息参考： - member not found：用户不是知识空间成员（管理员），无法删除。 - identity not found: userid不存在，无法添加/删除成员。 - space not found：知识空间不存在 - node not found：节点不存在 - document not found：文档不存在 - document is not in wiki：文档不在知识库中 报错不明确时请咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)。 |
| 400 | 131006 | permission denied | 权限拒绝，相关报错信息参考： - wiki space permission denied：知识库权限鉴权不通过，需要成为知识空间管理员（成员）。 - node permission denied：文档节点权限鉴权不通过，读操作需要具备节点阅读权限，写操作（创建、移动等）则需要具备节点容器编辑权限。 - no source parent node permission：需要具备原父节点的容器编辑权限。 - no destination parent node permission：需要具备目标父节点的容器编辑权限，若移动到知识空间下，则需要成为知识空间管理员（成员）。 **注意**：应用访问或操作文档时，除了申请 API 权限，还需授权具体文档资源的阅读、编辑或管理权限。 请参考以下步骤操作：  1. **当遇到资源权限不足的情况**：参阅[如何给应用授权访问知识库文档资源](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/wiki-qa#a40ad4ca)。 2. **也可直接将应用添加为知识库管理员（成员）**：参阅[如何将应用添加为知识库管理员（成员）](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/wiki-qa#b5da330b)。 3. **若无法解决或报错信息不明确时**：请咨询[技术支持](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)。 |
| 400 | 131007 | internal err | 服务内部错误，请勿重试，拿返回值的header头里的x-tt-logid咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)定位。 |


