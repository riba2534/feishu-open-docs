---
title: "创建 OKR 进展记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/create"
updateTime: "1753428957000"
---

# 创建 OKR 进展记录

创建 OKR 进展记录。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/okr/v1/progress_records |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `okr:okr` 更新 OKR 信息 `okr:okr.progress:writeonly` 更新 OKR 进展 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `source_title` | `string` | 是 | 进展来源<br>**示例值**："周报系统" |
| `source_url` | `string` | 是 | 进展来源链接<br>**示例值**："https://www.zhoubao.com"<br>**数据校验规则**：<br>- 正则校验：`^https?://.*$` |
| `target_id` | `string` | 是 | 目标 id，与 target_type 对应，可通过 OKR 内容相关接口获取<br>**示例值**："7041430377642082323" |
| `target_type` | `int` | 是 | 目标类型<br>**示例值**：2<br>**可选值有**：<br>- `2`: okr的O - `3`: okr的KR |
| `content` | `content_block` | 是 | 进展详情 富文本格式 |
| &nbsp;&nbsp;└ `blocks` | `content_block_element\[\]` | 否 | 文档结构是按行排列的，每行内容是一个 Block |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 否 | 文档元素类型<br>**示例值**："paragraph"<br>**可选值有**：<br>- `paragraph`: 文本段落 - `gallery`: 图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `paragraph` | `content_paragraph` | 否 | 文本段落 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `content_paragraph_style` | 否 | 段落样式 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `list` | `content_list` | 否 | 有序列表/无序列表/任务列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 否 | 列表类型<br>**示例值**："number"<br>**可选值有**：<br>- `number`: 有序列表 - `bullet`: 无序列表 - `checkBox`: 任务列表 - `checkedBox`: 已完成的任务列表 - `indent`: tab缩进 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `indentLevel` | `int` | 否 | 列表的缩进级别，支持指定一行的缩进 除代码块以外的列表都支持设置缩进，支持 1-16 级缩进，取值范围：[1,16]<br>**示例值**：1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number` | `int` | 否 | 用于指定列表的行号，仅对有序列表和代码块生效 如果为有序列表设置了缩进，行号可能会显示为字母或者罗马数字<br>**示例值**：1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `elements` | `content_paragraph_element\[\]` | 否 | 段落元素组成一个段落 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 否 | 元素类型<br>**示例值**："textRun"<br>**可选值有**：<br>- `textRun`: 文本型元素 - `docsLink`: 文档链接型元素 - `person`: 艾特用户型元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `textRun` | `content_text_run` | 否 | 文本 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 否 | 具体的文本内容<br>**示例值**："周报内容" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `style` | `content_text_style` | 否 | 文本内容的样式，支持 BIUS、颜色等 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bold` | `boolean` | 否 | 是否加粗<br>**示例值**：true |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `strikeThrough` | `boolean` | 否 | 是否删除<br>**示例值**：true |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `backColor` | `content_color` | 否 | 背景颜色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `red` | `int` | 否 | 红 取值范围[0,255]<br>**示例值**：216 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `green` | `int` | 否 | 绿 取值范围[0,255]<br>**示例值**：191 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `blue` | `int` | 否 | 蓝 取值范围[0,255]<br>**示例值**：188 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `alpha` | `number(float)` | 否 | 透明度 取值范围[0,1]<br>**示例值**：0.1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `textColor` | `content_color` | 否 | 字体颜色 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `red` | `int` | 否 | 红 取值范围[0,255]<br>**示例值**：216 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `green` | `int` | 否 | 绿 取值范围[0,255]<br>**示例值**：191 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `blue` | `int` | 否 | 蓝 取值范围[0,255]<br>**示例值**：188 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `alpha` | `number(float)` | 否 | 透明度 取值范围[0,1]<br>**示例值**：0.1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link` | `content_link` | 否 | 链接地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 链接地址<br>**示例值**："https://www.xxxxx.com/" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `docsLink` | `content_docs_link` | 否 | 飞书云文档 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 否 | 飞书云文档链接地址<br>**示例值**："https://xxx.feishu.cn/docx/xxxxxxxx" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 否 | 飞书云文档标题<br>**示例值**："项目说明文档" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `person` | `content_person` | 否 | 艾特用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `openId` | `string` | 否 | 员工的OpenID<br>**示例值**："ou_3bbe8a09c20e89cce9bff989ed840674" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `gallery` | `content_gallery` | 否 | 图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `imageList` | `content_image_item\[\]` | 否 | 图片元素 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fileToken` | `string` | 否 | 图片 token，通过上传图片接口获取<br>**示例值**："boxcnOj88GDkmWGm2zsTyCBqoLb" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `src` | `string` | 否 | 图片链接<br>**示例值**："https://example.com/drive/home/" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `width` | `number(float)` | 否 | 图片宽，单位px<br>**示例值**：458 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `height` | `number(float)` | 否 | 图片高，单位px<br>**示例值**：372 |
| `source_url_pc` | `string` | 否 | pc进展来源链接<br>**示例值**："open.feishu.cn"<br>**数据校验规则**：<br>- 正则校验：`^https?://.*$` |
| `source_url_mobile` | `string` | 否 | mobile进展来源链接<br>**示例值**："open.feishu.cn"<br>**数据校验规则**：<br>- 正则校验：`^https?://.*$` |
| `progress_rate` | `progress_rate_new` | 否 | 进展，包括百分比和状态 |
| &nbsp;&nbsp;└ `percent` | `number(float)` | 否 | 进展百分比，保留两位小数<br>**示例值**：50.21<br>**默认值**：`0`<br>**数据校验规则**：<br>- 取值范围：`-99999999999` ～ `99999999999` |
| &nbsp;&nbsp;└ `status` | `int` | 否 | 进展状态<br>**示例值**：0<br>**可选值有**：<br>- `-1`: 暂无 - `0`: 正常 - `1`: 风险 - `2`: 延期 |


### 请求体示例

```json
{
    "source_title":"测试周报系统",
    "source_url":"https://www.baidu.com/",
    "target_id":"7043693679567028244",
    "target_type":2,
    "content":{
        "blocks":[
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"粗体验证",
                                "style":{
                                    "bold":true
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"*",
                                "style":{
                                    "bold":true
                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"删除线验证",
                                "style":{
                                    "strikeThrough":true
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"字体颜色验证",
                                "style":{
                                    "textColor":{
                                        "red":216,
                                        "green":57,
                                        "blue":49,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"背景颜色验证",
                                "style":{
                                    "backColor":{
                                        "red":251,
                                        "green":191,
                                        "blue":188,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"粗体+删除+字体颜色+背景颜色验证",
                                "style":{
                                    "bold":true,
                                    "strikeThrough":true,
                                    "backColor":{
                                        "red":251,
                                        "green":191,
                                        "blue":188,
                                        "alpha":1
                                    },
                                    "textColor":{
                                        "red":216,
                                        "green":57,
                                        "blue":49,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"有序标题1验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"粗体验证",
                                "style":{
                                    "bold":true
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"number",
                            "indentLevel":1,
                            "number":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"有序标题2验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"删除线验证",
                                "style":{
                                    "strikeThrough":true
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"number",
                            "indentLevel":1,
                            "number":2
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"有序标题3验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"字体背景颜色验证",
                                "style":{
                                    "backColor":{
                                        "red":251,
                                        "green":191,
                                        "blue":188,
                                        "alpha":1
                                    },
                                    "textColor":{
                                        "red":216,
                                        "green":57,
                                        "blue":49,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"number",
                            "indentLevel":1,
                            "number":3
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"无序标题1验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"粗体",
                                "style":{
                                    "bold":true
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"bullet",
                            "indentLevel":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"无序标题2验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"删除线",
                                "style":{
                                    "strikeThrough":true
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"bullet",
                            "indentLevel":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"无序标题3验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"字体背景颜色验证",
                                "style":{
                                    "backColor":{
                                        "red":251,
                                        "green":191,
                                        "blue":188,
                                        "alpha":1
                                    },
                                    "textColor":{
                                        "red":216,
                                        "green":57,
                                        "blue":49,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"bullet",
                            "indentLevel":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"https://example.cn/docx/doxcnO2Wkq0YPZQYLuJKyyOvLrh#doxcnSOui82swqk6c0o436Ak3nc",
                                "style":{
                                    "link":{
                                        "url":"https://example.cn/docx/doxcnO2Wkq0YPZQYLuJKyyOvLrh#doxcnSOui82swqk6c0o436Ak3nc"
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"gallery",
                "gallery":{
                    "imageList":[
                        {
                            "src":"https://internal-api-okr.feishu-boe.cn/stream/api/downloadFile/?file_token=boxbcMTBQO9ofLjWkDuPxkxOA2c&ticket=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0YXJnZXRfaWQiOiI3MDQxNDMwMzc3NjQyMDgyMzIzIiwidGFyZ2V0X3R5cGUiOjMsImFjdGlvbiI6MiwiZmlsZV90b2tlbiI6ImJveGJjTVRCUU85b2ZMaldrRHVQeGt4T0EyYyIsInVzZXJfaWQiOiI2OTY5ODU1NTAxNzQ0ODM0MDkyIiwidGVuYW50X2lkIjoiNjg3NzUwMjY4NzYwOTQwNjk5MCIsImV4cCI6MTY0MDE1NTk2M30.yc4qV2pkGUVwSO53-N_XGgeMucjmDn9iso1Ez_8vpghFz8YdeSDf4NHQpxOHYHc8RURvwI0a5UTNKKJ9CWagTQ",
                            "fileToken":"boxbcMTBQO9ofLjWkDuPxkxOA2c",
                            "width":458,
                            "height":372
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"任务列表未勾选验证",
                                "style":{

                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"checkBox",
                            "indentLevel":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"任务列表已勾选验证",
                                "style":{

                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"checkedBox",
                            "indentLevel":1
                        }
                    }
                }
            }
        ]
    }
}
```


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
                                    "style": {
                                        "bold": true
                                    },
                                    "text": "粗体验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "bold": true
                                    },
                                    "text": "*"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "strikeThrough": true
                                    },
                                    "text": "删除线验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "textColor": {
                                            "alpha": 1,
                                            "blue": 49,
                                            "green": 57,
                                            "red": 216
                                        }
                                    },
                                    "text": "字体颜色验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "backColor": {
                                            "alpha": 1,
                                            "blue": 188,
                                            "green": 191,
                                            "red": 251
                                        }
                                    },
                                    "text": "背景颜色验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "backColor": {
                                            "alpha": 1,
                                            "blue": 188,
                                            "green": 191,
                                            "red": 251
                                        },
                                        "bold": true,
                                        "strikeThrough": true,
                                        "textColor": {
                                            "alpha": 1,
                                            "blue": 49,
                                            "green": 57,
                                            "red": 216
                                        }
                                    },
                                    "text": "粗体+删除+字体颜色+背景颜色验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "有序标题1验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "bold": true
                                    },
                                    "text": "粗体验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "number": 1,
                                "type": "number"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "有序标题2验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "strikeThrough": true
                                    },
                                    "text": "删除线验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "number": 2,
                                "type": "number"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "有序标题3验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "backColor": {
                                            "alpha": 1,
                                            "blue": 188,
                                            "green": 191,
                                            "red": 251
                                        },
                                        "textColor": {
                                            "alpha": 1,
                                            "blue": 49,
                                            "green": 57,
                                            "red": 216
                                        }
                                    },
                                    "text": "字体背景颜色验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "number": 3,
                                "type": "number"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "无序标题1验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "bold": true
                                    },
                                    "text": "粗体"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "bullet"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "无序标题2验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "strikeThrough": true
                                    },
                                    "text": "删除线"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "bullet"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "无序标题3验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "backColor": {
                                            "alpha": 1,
                                            "blue": 188,
                                            "green": 191,
                                            "red": 251
                                        },
                                        "textColor": {
                                            "alpha": 1,
                                            "blue": 49,
                                            "green": 57,
                                            "red": 216
                                        }
                                    },
                                    "text": "字体背景颜色验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "bullet"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "link": {
                                            "url": "https://example.cn/docx/doxcnO2Wkq0YPZQYLuJKyyOvLrh#doxcnSOui82swqk6c0o436Ak3nc"
                                        }
                                    },
                                    "text": "https://example.cn/docx/doxcnO2Wkq0YPZQYLuJKyyOvLrh#doxcnSOui82swqk6c0o436Ak3nc"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "gallery": {
                        "imageList": [
                            {
                                "fileToken": "boxbcMTBQO9ofLjWkDuPxkxOA2c",
                                "height": 372,
                                "src": "https://internal-api-okr.feishu-boe.cn/stream/api/downloadFile/?file_token=boxbcMTBQO9ofLjWkDuPxkxOA2c&ticket=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0YXJnZXRfaWQiOiI3MDQxNDMwMzc3NjQyMDgyMzIzIiwidGFyZ2V0X3R5cGUiOjMsImFjdGlvbiI6MiwiZmlsZV90b2tlbiI6ImJveGJjTVRCUU85b2ZMaldrRHVQeGt4T0EyYyIsInVzZXJfaWQiOiI2OTY5ODU1NTAxNzQ0ODM0MDkyIiwidGVuYW50X2lkIjoiNjg3NzUwMjY4NzYwOTQwNjk5MCIsImV4cCI6MTY0MDE1NTk2M30.yc4qV2pkGUVwSO53-N_XGgeMucjmDn9iso1Ez_8vpghFz8YdeSDf4NHQpxOHYHc8RURvwI0a5UTNKKJ9CWagTQ",
                                "width": 458
                            }
                        ]
                    },
                    "type": "gallery"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "任务列表未勾选验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "checkBox"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "任务列表已勾选验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "checkedBox"
                            }
                        }
                    },
                    "type": "paragraph"
                }
            ]
        },
        "modify_time": "1640675837810",
        "progress_id": "7046317985098760212"
    },
    "msg": "success"
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1009999 | internal server error | 内部错误，请联系飞书助手或您的客户成功经理 |
| 500 | 1009998 | system exception | 系统异常，请联系飞书助手或您的客户成功经理 |
| 400 | 1001001 | invalid parameters | 无效的参数，请对照文档检查输入的参数 |
| 400 | 1001002 | no permission | 您无权访问该接口，请确认您的登录凭证 |
| 400 | 1001003 | user not found | 用户不存在 |
| 400 | 1001004 | okr data not found | 对应ID的数据不存在 |


