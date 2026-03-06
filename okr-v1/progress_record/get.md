---
title: "获取 OKR 进展记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/get"
updateTime: "1753428958000"
---

# 获取 OKR 进展记录

根据 ID 获取 OKR 进展记录详情，接口返回进展记录的内容、更新时间以及进展百分比和状态。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/okr/v1/progress_records/:progress_id |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `okr:okr:readonly` 获取 OKR 信息 `okr:okr.progress:readonly` 获取 OKR 进展 `okr:okr` 更新 OKR 信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `progress_id` | `string` | 待查询的 OKR进展记录 ，可以通过调用“批量获取 OKR”或“获取用户的 OKR 列表”接口获取 <br>**示例值**："7041857032248410131" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `progress_record` | \- |
| &nbsp;&nbsp;└ `progress_id` | `string` | OKR 进展ID |
| &nbsp;&nbsp;└ `modify_time` | `string` | 进展更新时间 毫秒 |
| &nbsp;&nbsp;└ `content` | `content_block` | 进展 对应的 Content 详细内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `blocks` | `content_block_element\[\]` | 文档结构是按行排列的，每行内容是一个 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 文档元素类型<br>**可选值有**：<br>- `paragraph`: 文本段落 - `gallery`: 图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `paragraph` | `content_paragraph` | 文本段落 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `content_paragraph_style` | 段落样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `list` | `content_list` | 有序列表/无序列表/任务列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 列表类型<br>**可选值有**：<br>- `number`: 有序列表 - `bullet`: 无序列表 - `checkBox`: 任务列表 - `checkedBox`: 已完成的任务列表 - `indent`: tab缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentLevel` | `int` | 列表的缩进级别，支持指定一行的缩进 除代码块以外的列表都支持设置缩进，支持 1-16 级缩进，取值范围：[1,16] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `int` | 用于指定列表的行号，仅对有序列表和代码块生效 如果为有序列表设置了缩进，行号可能会显示为字母或者罗马数字 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `content_paragraph_element\[\]` | 段落元素组成一个段落 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 元素类型<br>**可选值有**：<br>- `textRun`: 文本型元素 - `docsLink`: 文档链接型元素 - `person`: 艾特用户型元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `textRun` | `content_text_run` | 文本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 具体的文本内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `content_text_style` | 文本内容的样式，支持 BIUS、颜色等 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 是否加粗 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikeThrough` | `boolean` | 是否删除 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `backColor` | `content_color` | 背景颜色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `red` | `int` | 红 取值范围[0,255] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `green` | `int` | 绿 取值范围[0,255] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `blue` | `int` | 蓝 取值范围[0,255] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `alpha` | `number(float)` | 透明度 取值范围[0,1] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `textColor` | `content_color` | 字体颜色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `red` | `int` | 红 取值范围[0,255] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `green` | `int` | 绿 取值范围[0,255] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `blue` | `int` | 蓝 取值范围[0,255] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `alpha` | `number(float)` | 透明度 取值范围[0,1] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `content_link` | 链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `docsLink` | `content_docs_link` | 飞书云文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 飞书云文档链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 飞书云文档标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person` | `content_person` | 艾特用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `openId` | `string` | 员工的OpenID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gallery` | `content_gallery` | 图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `imageList` | `content_image_item\[\]` | 图片元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fileToken` | `string` | 图片 token，通过上传图片接口获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `src` | `string` | 图片链接 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `width` | `number(float)` | 图片宽，单位px |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `height` | `number(float)` | 图片高，单位px |
| &nbsp;&nbsp;└ `progress_rate` | `progress_rate_new` | 进展，包括百分比和状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `percent` | `number(float)` | 进展百分比，保留两位小数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 进展状态<br>**可选值有**：<br>- `-1`: 暂无 - `0`: 正常 - `1`: 风险 - `2`: 延期 |


### 响应体示例

```json
{
    "code": 0,
    "data": {
        "content": {
            "blocks": [
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": " "
                                },
                                "type": "textRun"
                            },
                            {
                                "person": {
                                    "openId": "ou_b1ba99a5340289d7af30839fd95ce1ee",
                                    "userId": "7012194140645721644"
                                },
                                "type": "person"
                            }
                        ]
                    },
                    "type": "paragraph"
                }
            ]
        },
        "modify_time": "1640677213095",
        "progress_id": "7046518160811425812"
    },
    "msg": "success"
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1009999 | internal server error | 内部错误，请联系飞书助手或您的客户成功经理 |
| 500 | 1009998 | system exception | 系统异常，稍后重试。 |
| 400 | 1001001 | invalid parameters | 无效的参数，请对照文档检查输入的参数(如参数类型不匹配、参数值超出限制) |
| 400 | 1001002 | no permission | 您无权访问该数据，请确认当前用户身份是否有对应数据权限。 |
| 400 | 1001003 | user not found | 用户不存在，请检查传入的用户 ID 是否正确 |
| 400 | 1001004 | okr data not found | 对应ID的数据不存在，请检查传入的 OKR 进展记录 ID（progress_id）是否正确 |


