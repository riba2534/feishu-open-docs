---
title: "概述"
fullPath: "/uAjLw4CM/ukTMukTMukTM/spark-v1/overview"
updateTime: "1776914135000"
---

# 功能说明

妙搭 Open API 是飞书妙搭数据平台的一套开放接口，开发者通过此套接口，可通过编程方式，对妙搭应用的数据库进行读写操作，以进行数据导入导出、系统集成等操作。

## 概念说明

| **概念**           | **说明**                                                                 | **示例**                                                                                                                                                                                                                                                                                         |
| ---------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| app_id           | 妙搭应用 id                                                                | 示例值：app_4jsxusxe5zhzz可以从妙搭应用 URL 中获取 https://miaoda.feishu.cn/app/***app_4jsxusxe5zhzz***                                                                                                                                                                                                   |
| table/table_name | 数据表。应用中创建的数据表，用于基于结构化的业务数据。table_name 是数据表的唯一标示，同一应用下，table_name 是唯一的。 | ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/de878ef98b5a3067e192717c76b20a71_7DFfOVeyn1.png?height=927&lazyload=true&width=1920) |
| column/columns   | 数据表中的列                                                                 | ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/388865a2724cdda044d50442758234e9_AbXnMIotJ8.png?height=935&lazyload=true&width=1920) |

## 已开放接口

> 历史版本接口可参考：<https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/apaas-v1/workspace-table/list>
1. [获取数据表列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/get_table_list)
2. [获取数据表详细信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/get_table_detail)
3. [查询数据表数据记录](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/get_table_record_list)
4. [向数据表中添加或更新记录](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/post_table_records)
5. [按条件更新数据表中的记录](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/patch_table_records)
6. [批量更新数据表中的记录](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/batch_update_table_records)
7. [删除数据表中的记录](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-table/delete_table_records)
8. [查询视图数据记录](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-view/get_view_record_list)
9. [获取自定义枚举列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-enum/get_enum_list)
10. [获取自定义枚举详细信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-enum/get_enum_detail)
11. [上传文件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/upload)
12. [下载文件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/download)
13. [分片上传文件 - 创建上传请求](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/upload_initialize)
14. [分片上传文件 - 上传分片](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/upload_part)
15. [分片上传文件 - 完成上传](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app-storage/upload_complete)
16. [执行 SQL](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/spark-v1/app/sql_commands)


# 使用示例

## 1.准备工作

### 1.1 创建飞书开放平台应用，并申请对应的用户身份权限

   ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/3de2bc154b5545eb4d2985ed8f99b89a_RTf47EkcO3.png?height=932&lazyload=true&width=1918)
    
   `offline_access` 权限可根据实际需要选择是否开通，如果是数据集成场景，需要在代码中刷新 user acess token 以处理 token 过期问题，则需要申请权限。详细可参考 [refresh_user_access_token](https://open.larkoffice.com/document/authentication-management/access-token/refresh-user-access-token)。
   
### 1.2  获取用户授权凭证 user_access_token

>    user_access_token(uat) 存在有效期，一般为获取后的 7200s（2h），过期后可以使用获取的 refresh_token 刷新，详情可参考：[refresh_user_access_token](https://open.larkoffice.com/document/authentication-management/access-token/refresh-user-access-token)。
    
####    1.2.1    **方式一**：按照[官方文档](https://open.larkoffice.com/document/authentication-management/access-token/get-user-access-token)说明来获取。

    
####    1.2.2    **方式二**：通过飞书开放平台 API 调试台获取（适合调试接口时使用）

   ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/ea40c8ab1347d3fedd10f7803ddd76f9_kSt1dzJj4k.png?height=934&lazyload=true&width=1920)
   
####    1.2.3    **方式三**：通过妙搭创建的助手应用来获取

>    新版 API：<https://mcnt8r4c3f2k.aiforce.cloud/app/app_4hvvryye0f4j4/spark>
>    
>    历史版本：<https://mcnt8r4c3f2k.aiforce.cloud/app/app_4hvvryye0f4j4>
>  
   ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/fcfa6efe0be27509860837064d76d329_srKgg6oarU.gif?height=1052&lazyload=true&width=1916)
    
####    1.2.4    方式四：也可以使用提供的辅助工具快速获取：<https://get-uat.apaas-apps.com:10444/>

辅助工具源码：<https://cnb.cool/codingtheworld_galaxy/get-feishu-uat>
![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/f82263bf52239665a5f0485bf2aca903_Kjc71QXagL.gif?height=1052&lazyload=true&width=1916)

## 2. 调用接口

> 接口整体语法和 pgREST 一致，具体可参考
> 
> <https://docs.postgrest.org/en/v13/references/api/tables_views.html#read>

以妙搭搭建的应用 https://miaoda.feishu.cn/app/app_4jsxusxe5zhzz 的数据表 `student` 为例：
| **列名**           | **数据类型**                 | **允许空**  | **默认值**           | **注释**      |
| ---------------- | ------------------------ | -------- | ----------------- | ----------- |
| id               | uuid                     | NOT NULL | gen_random_uuid() | 表唯一 ID      |
| record_id        | character varying        | YES      | NULL              | Base 表记录 ID |
| name             | text                     | YES      | NULL              | 姓名          |
| gender           | text                     | YES      | NULL              | 性别          |
| birth_date       | date                     | YES      | NULL              | 出生日期        |
| photo            | text[]                  | YES      | NULL              | 照片          |
| hobby            | text[]                  | YES      | NULL              | 爱好          |
| homeroom_teacher | user_profile             | YES      | NULL              | 班主任         |
| _created_at     | timestamp with time zone | NOT NULL | now()             | 创建时间        |
| _created_by     | user_profile             | YES      | NULL              | 创建人         |
| _updated_at     | timestamp with time zone | NOT NULL | now()             | 更新时间        |
| _updated_by     | user_profile             | YES      | NULL              | 更新人         |
### 2.1  查询 `性别=男` 的学生列表且只返回 `id、name、gender、birth_date` 并按 `birth_date` 降序排序

```
curl --location 'https://open.feishu.cn/open-apis/spark/v1/apps/app_4jsxusxe5zhzz/tables/student/records?filter=gender%3Deq.%E7%94%B7&select=id%2Cname%2Cgender%2Cbirth_date&order=birth_date.desc' \
--header 'Authorization: Bearer xxx......LUY1WMsdk5kZdMk5oXjaGy7Qw00f5t'
```
返回示例
```
{
    "code": 0,
    "data": {
        "has_more": false,
        "items": "[{"birth_date":"2026-06-10","gender":"男","id":"f2424044-9861-470e-9b04-39c820c9fb81","name":"梁一"},{"birth_date":"2026-05-30","gender":"男","id":"1a99e4ba-ea41-4076-81e1-6f087c548e7c","name":"杨九"},{"birth_date":"2026-05-10","gender":"男","id":"169ea02d-054f-47e3-90d3-cdd68a4b2666","name":"郭七"},{"birth_date":"2026-04-20","gender":"男","id":"9bee5b07-eee9-4a0d-a148-9ec15534f9d6","name":"马五"},{"birth_date":"2026-03-30","gender":"男","id":"bae8ae6e-369d-4dd1-b3f7-8fcb3f8789b5","name":"林三"},{"birth_date":"2026-03-10","gender":"男","id":"9005f2ba-b546-4f09-96c6-1b32e0eeba95","name":"刘一"},{"birth_date":"2026-02-28","gender":"男","id":"0e139dad-6c39-4f90-8bd0-67065ccf9db6","name":"吴九"},{"birth_date":"2026-02-10","gender":"男","id":"29334c30-2a13-4686-b7ae-c63f9e0e8ae9","name":"孙七"},{"birth_date":"2026-01-20","gender":"男","id":"8f25b1ca-4175-46de-a159-bbaae5126c3b","name":"王五"},{"birth_date":"2026-01-01","gender":"男","id":"ff5a4db5-b5e8-4267-b79b-6f2185e670a6","name":"张三"}]",
        "page_token": "",
        "total": 10
    },
    "msg": ""
}
```
### 2.2  插入一条记录

> 请求头中增加 `'Prefer: missing=default'`可达到不传的列使用默认值目的。
> 比如 id 是自动生成的 uuid，传入此请求头可在插入数据时让平台自动生成 uuid。
```
curl --location 'https://open.feishu.cn/open-apis/spark/v1/apps/app_4jsxusxe5zhzz/tables/student/records' \
--header 'Prefer: resolution=merge-duplicates' \
--header 'Prefer: missing=default' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer xxx...LUY1WMsdk5kZdMk5oXjaGy7Qw00f5t' \
--data '{
    "records": "[{"name":"王小小","gender":"男", "birth_date": "2026-01-01"}]"
}'
```
```
{
    "code": 0,
    "data": {
        "record_ids": [
            "89b43eec-85d0-49aa-829c-ec6ab703efef"
        ]
    },
    "msg": ""
}
```