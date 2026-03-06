---
title: "获取任务结果"
fullPath: "/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/task/get"
updateTime: "1749710138000"
---

# 获取任务结果

该方法用于获取wiki异步任务的结果


> **Tip**: 知识库权限要求，当前 access token 所代表的用户或应用（机器人）：
> - 为任务创建者


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/wiki/v2/tasks/:task_id |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `wiki:space:read` 查看知识空间信息 `wiki:wiki` 查看、编辑和管理知识库 `wiki:wiki:readonly` 查看知识库 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `task_id` | `string` | 任务id<br>**示例值**："7037044037068177428-075c9481e6a0007c1df689dfbe5b55a08b6b06f7" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `task_type` | `string` | 是 | 任务类型<br>**示例值**：move<br>**可选值有**：<br>- `move`: [移动云空间文档至知识空间](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space-node/move_docs_to_wiki)任务 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `task` | `task_result` | 任务结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `task_id` | `string` | 任务id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `move_result` | `move_result\[\]` | [移动云空间文档至知识空间](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space-node/move_docs_to_wiki)任务结果 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `node` | `node` | 移动完成的节点信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `space_id` | `string` | 知识空间id [获取方式](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-overview) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `node_token` | `string` | 节点token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_token` | `string` | 对应文档类型的token，可根据 obj_type 判断属于哪种文档类型。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_type` | `string` | 文档类型，对于快捷方式，该字段是对应的实体的obj_type。<br>**可选值有**：<br>- `doc`: 旧版文档 - `sheet`: 表格 - `mindnote`: 思维导图 - `bitable`: 多维表格 - `file`: 文件 - `docx`: 新版文档 - `slides`: 幻灯片 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `parent_node_token` | `string` | 父节点 token。若当前节点为一级节点，父节点 token 为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `node_type` | `string` | 节点类型<br>**可选值有**：<br>- `origin`: 实体 - `shortcut`: 快捷方式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `origin_node_token` | `string` | 快捷方式对应的实体node_token，当节点为快捷方式时，该值不为空。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `origin_space_id` | `string` | 快捷方式对应的实体所在的space id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `has_child` | `boolean` | 是否有子节点 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 文档标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_create_time` | `string` | 文档创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `obj_edit_time` | `string` | 文档最近编辑时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `node_create_time` | `string` | 节点创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `creator` | `string` | 节点创建者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `owner` | `string` | 节点所有者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `node_creator` | `string` | 节点创建者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 节点移动状态码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status_msg` | `string` | 节点移动状态信息 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "task": {
            "task_id": "7037044037068177428-075c9481e6a0007c1df689dfbe5b55a08b6b06f7",
            "move_result": [
                {
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
                        "node_creator": "ou_xxxxx"
                    },
                    "status": 0,
                    "status_msg": "success"
                }
            ]
        }
    }
}
```


### [移动云空间文档至知识空间](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space-node/move_docs_to_wiki)任务 ###

- 结果为什么是数组？

  未来计划支持多个节点批量迁入。因此结果由数组表示，表示批量迁入多个节点的结果。例如，迁入3个节点时，结果返回长度为3的数组，其中可能部分节点迁入成功，部分失败。当前仅支持单个节点迁入，结果返回长度为1。

#### 状态说明 ####


| status取值 | status_msg取值 | 描述 |
| --- | --- | --- |
| 0 | success | 任务成功 |


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 131001 | rpc fail | 服务报错，请稍后重试，或者拿响应体的header头里的x-tt-logid咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)定位。 |
| 400 | 131002 | param err | 通常为传参有误，例如数据类型不匹配。请查看**具体接口报错信息**，报错不明确时请咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)。 |
| 400 | 131004 | invalid user | 非法用户。请咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)。 |
| 400 | 131005 | not found | 未找到相关数据，例如id不存在。相关报错信息参考： - member not found：用户不是知识空间成员（管理员），无法删除。 - identity not found: userid不存在，无法添加/删除成员。 - space not found：知识空间不存在 - node not found：节点不存在 - document not found：文档不存在 报错不明确时请咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)。 |
| 400 | 131006 | permission denied | 权限拒绝，相关报错信息参考： - wiki space permission denied：知识库权限鉴权不通过，需要成为知识空间管理员（成员）。 - node permission denied：文档节点权限鉴权不通过，读操作需要具备节点阅读权限，写操作（创建、移动等）则需要具备节点容器编辑权限。 - no source parent node permission：需要具备原父节点的容器编辑权限。 - no destination parent node permission：需要具备目标父节点的容器编辑权限，若移动到知识空间下，则需要成为知识空间管理员（成员）。 - only task creator can query status：只有任务创建者才能获取任务结果（用户或应用）。 - no move permission for document：缺少移动文档的权限，需要具备文档可管理权限和父文件夹编辑权限。参阅 [如何为应用身份（tenant_access_token）开通个人云空间中文件夹的查看或编辑权限]( https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/faq#b02e5bfb) **注意**：应用访问或操作文档时，除了申请 API 权限，还需授权具体文档资源的阅读、编辑或管理权限。 请参考以下步骤操作：  1. **当遇到资源权限不足的情况**：参阅[如何给应用授权访问知识库文档资源](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/wiki-qa#a40ad4ca)。 2. **也可直接将应用添加为知识库管理员（成员）**：参阅[如何将应用添加为知识库管理员（成员）](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/wiki-qa#b5da330b)。 3. **若无法解决或报错信息不明确时**：请咨询[技术支持](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)。 |
| 400 | 131007 | internal err | 服务内部错误，请勿重试，拿返回值的header头里的x-tt-logid咨询[oncall](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)定位。 |


