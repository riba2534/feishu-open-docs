---
title: "纪要概述"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/note/notes_overview"
updateTime: "1774580773000"
---

#  资源介绍
##  资源定义
通过纪要资源，用户可以查看会议生成的纪要文档、逐字稿等产物，并获取相关上下文（例如会中共享文档等），可以用于复盘、检索增强、对齐校验与可追溯引用。目前支持的方法有：[获取纪要详情](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/note/get)。

##  字段说明

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `data` | `-` | `-` |
| ∟ `note` | `note` | 纪要实体 |
| ∟ `creator_id` | `string` | 纪要创建者 User ID |
| ∟ `create_time` | `string` | 纪要创建时间（unix时间，单位sec） |
| ∟ `artifacts` | `note_artifact[]` | 纪要产物 |
| ∟ `artifact_type` | `int` | 产物类型            **可选值有**： - `1`：纪要文档 - `2`：逐字稿文档 |
| ∟ `create_time` | `string` | 产物创建时间（unix时间，单位sec） |
| ∟ `doc_token` | `string` | 产物的doc token |
| ∟ `references` | `note_reference[]` | 关联引用 |
| ∟ `reference_type` | `int` | 关联引用类型            **可选值有**： - `1`：会中共享文档 |
| ∟ `doc_token` | `string` | 关联引用的doc token |


###  数据示例
```json
{
    "data": {
        "note": {
            "creator_id": "ou_3ec3f6a28a0d08c45d895276e8e5e19b",
            "create_time": "1608885566",
            "artifacts": [
                {
                    "artifact_type": 1,
                    "create_time": "1608885566",
                    "doc_token": "UxBjd9Txxxxxxxxxxxxx"
                },
                {
                    "artifact_type": 2,
                    "create_time": "1608885566",
                    "doc_token": "RcaPd46xxxxxxxxxxxxx"
                }
            ],
            "references": [
                {
                    "reference_type": 1,
                    "doc_token": "TQqvwbpPLxxxxxxxxxxx"
                }
            ]
        }
    }
}
```