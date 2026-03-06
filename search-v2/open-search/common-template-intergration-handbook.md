---
title: "接入指南"
fullPath: "/uAjLw4CM/ukTMukTMukTM/search-v2/common-template-intergration-handbook"
updateTime: "1753356689000"
---

# 接入指南

## 1.1. 整体介绍

-   **开放搜索简介：** 接入方通过飞书搜索提供的自定义配置能力，实现数据源在飞书内被搜索并展示。
-   **开放搜索价值：** 通过飞书搜索更好地满足用户“办公场景统一入口”的需求，为用户提供更便捷、更直接的使用入口。

## 1.2. 术语说明

-   **数据源**：抽象的数据容器，可联想成关系型数据库的表；
-   **数据项**：搜索结果中的单条记录，是搜索召回的最小数据单元，可联想成数据库表中的一条记录；
-   **Search tab**：Lark 搜索中的“综合”、“消息”、“Meego”等tab。点击“更多”可以看到所有 search tab。理论上一个数据源对应一个 search tab；
-   **ACL**：Access Control Lists，对资源是否能被搜索进行控制；

## 1.3. 说明

-   开放搜索的数据源必须绑定开放平台中的一个应用。应用的可见性（在租户管理后台配置）决定数据源对应的 search tab 对单个用户是否可见。

-   召回策略说明：
    -   中文支持 完整匹配、前缀匹配、分词匹配
    -   英文支持 完整匹配、前缀匹配、分词匹配
-   排序策略说明：默认根据底层 ES 的算分算法和item.id进行排序，也支持根据自定字段来排序
-   应用可见性设置

在 版本管理与发布 - 应用发布时，可以选择应用的“可用性状态”，默认只有应用开发者可见。

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/4cca2aeed43d7ec599f4c73b8592ec6c_35MqI8xfIT.png?height=807&lazyload=true&width=1500)

**租户管理后台**入口（用户必须是租户管理员）：

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/bbb76c5ebd345b1bbd430acf638c4018_n1YEfHUZt9.png?height=2016&lazyload=true&width=2156)

“**应用审核**” 与 “**应用可见性**”配置的入口如下：

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/fcc33486d62946d9a2131432625e9f90_MByXvEtuGA.png?height=1224&lazyload=true&width=3326)

**搜索数据权限** 主要分为两部分，用户**都有**权限才能搜到数据：

-   Search tab 可见性：如果开放平台关联的应用对用户 A 不可见，则该 search tab 对 A 也不可见，即 A 对数据不可搜；在“[飞书管理后台](https://feishu.feishu.cn/admin/appCenter/manage/)”-选择应用-“应用可见性”中编辑可见范围，可从员工或部门的维度进行增删。
-   数据项 ACL 控制：目前支持针对每个数据项来设置权限控制，支持以 人(user)  的粒度来进行设置。如果没有设置，则默认全员不可搜。

# 2. 具体操作

## 2.1. 开放平台

1.  在开放平台（open.feishu.cn）中申请应用；（或者复用已有应用）
	-  如果复用已有应用，需要注意 search tab 的可见性是跟随已有应用的可见性的。例如已有应用（小程序或者 bot）的可见性为全员可见，那么绑定该应用的 search tab 也是全员可见；请注意不要这里做过多测试和长时间停留，可能会对搜索使用者尤其是kp造成困扰
    -  建议新建开放平台应用来单独对 search tab 进行可见性控制；这样可以在测试和导入数据阶段自行控制灰度放量，如果后期想要复用已有应用，目前我们可以支持手动切换
    -  如果不想等待企业管理员审批应用，推荐在测试租户创建应用进行测试，测试完成后线上直接使用上述a)方案，并尽快完成数据导入

2.  在应用的“**权限管理**”中添加“**查询、创建、修改和删除自定义搜索数据源、数据范式或数据项**”和“**查询自定义搜索数据源、数据范式或数据项**”两个权限；

3.  在应用的“**应用发布**”-“**版本管理与发布**”中，创建版本，并申请发布。发布申请会发送给租户管理员，经由租户管理员批准后方可上线；

4.  在应用的“**凭证与基础信息**”中复制 App ID 和 App Secret。后续请求接口时需要使用到；

## 2.2. 开放搜索 OpenAPI

注意：curl 请求中的 `${xxx}` 是需要用户手动替换的。

### 2.2.1. 请求接口获取 tenant access token

推荐使用 SDK ：[服务端 SDK](https://open.larkoffice.com/document/ukTMukTMukTM/uETO1YjLxkTN24SM5UjN)

参考链接：[获取应用身份访问凭证 - 服务端文档 - 开发文档 - 飞书开放平台](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM) 来请求接口

或者用以下的 curl 请求

```bash
curl --location --request POST 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal' \
--header 'Content-Type: application/json' \
--data-raw '{
    "app_id": "${App ID}", 
    "app_secret": "${App Secret}"
}'
```

获取到 tenant_access_token 字段（有效期2小时）


### 2.2.2. 请求创建数据范式
完整能力参考链接：[创建数据范式 - 服务端文档 - 开发文档 - 飞书开放平台](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/search-v2/schema/create)

请求体可以参考以下 curl 请求
```bash
curl --location --request POST 'https://open.feishu.cn/open-apis/search/v2/schemas' \
--header 'Authorization:  Bearer ${Tenant Access Token}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "display": {
        "card_key": "search_common_card",
        "fields_mapping": [
            {
                "data_field": "${expression}",
                "display_field": "${field}"
            },
            {
                "data_field": "${expression}",
                "display_field": "${field}"
            }
        ]
    },
    "properties": [
        {
            "is_returnable": true,
            "is_searchable": true,
            "is_sortable": false,
            "name": "${name}",
            "type": "text",
            "search_options": {
                "enable_semantic_match": true
            }
        },
        {
            "name": "${name}",
            "type": "int",
            "sort_options": {
                "order": "${order}",
                "priority": "${priority}"
            }
        },
        {
            "is_returnable": true,
            "name": "${name}",
            "type": "tag",
            "type_definitions": {
                "tag": [
                    {
                        "color": "${color}",
                        "name": "${name}",
                        "text": "${type}"
                    }
                ]
            }
        }
    ],
    "schema_id": "${schema_id}",
    "validate_only": false
}'
```
说明： 

1.  参数说明请参考接口文档[创建数据范式 - 服务端文档 - 开发文档 - 飞书开放平台](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/search-v2/schema/create)

2.  `card_key` 指定数据范式对应的模版，目前支持``search_common_card``；模版信息如下：
![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/8dd9a52f171a771104311afb11986dc4_M3Z6ypj4UU.png?height=180&lazyload=true&width=1892)
	- 红色框：``icon_url``
    - 黄色框：``title``
	- 绿色框：``summary``
    - 蓝色框：``footer``
    - 黑色框：从左到右依次为``tag1``,``tag2``,``tag3``
    - 灰色框：PC端为``source_url``，移动端为``source_url_mobile``

3.  `fields_mapping` 定义用户字段到模板字段的映射
    - `display_field`字段为模板字段，目前支持的字段有`summary`，`footer`，`icon_url`，`tag1`，`tag2`，`tag3`；
    - `data_field`支持模版语言且支持拼接, 如`这是自定义的字段1: ${field1} 和 字段2: ${field2}`
    
    具体如下：
    
```json 
  "display": {
        "card_key": "search_common_card",
        "fields_mapping": [
         {
                    "data_field": "${priority}",
                    "display_field": "tag1"
                },
                {
                    "data_field": "${status}",
                    "display_field": "tag2"
                },
                {
                    "data_field": "${type}",
                    "display_field": "tag3"
                },
                {
                    "data_field": "this is ${summary} and content is ${content}",
                    "display_field": "summary"
                },
                 {
                    "data_field": "${_create_time}",
                    "display_field": "footer"
                }
        ]
  }
``` 


4.  映射有如下特殊规则：
    - `summary` 和 `footer` 字段的映射支持文本类型和数值类型以及两者的拼接； `tag1`,`tag2`,`tag3`	只支持类型为`tag`的字段映射
    - 对于`footer`字段， 当 `data_field` 为 `${_create_time}` 或 `${_update_time}` 时，展示时会解析为 `创建于 xxx` 和 `更新于 xxx` 且支持i18n，无需另外配置；
5. `properties`为自定义字段处，字段内参数说明可参考上方接口文档
	- 名称为`_create_time`，`_update_time`，`_item_id`，`_title`的字段为特殊字段；除此外，字段命名不能以`_`开头
	- 以上字段对应着数据项的最基本的信息：`_create_time`，`_update_time`，`_title`，`_item_id`分别对应着`metadata`中的`create_time`，`update_time`，`title`以及请求体中的`id`字段；如下为创建item时请求体的`metadata`部分

```json 
{
	    "id":"id_1",
      "metadata": {
        "create_time": 0,
        "source_url": "",
        "source_url_mobile": "",
        "title": "",
        "update_time": 0
    }
``` 


   - 创建schema时如果没有定义上述字段，系统会默认生成相应字段进行存储；如果无特殊需求，不建议手动配置
 
 
6.  字段定义与字段搜索能力需要遵循一定的规范
    - 字段的可搜索属性 `is_searchable` 与可排序属性 `is_sortable` 不能同时为`true`
    - 只有数值类型字段的 `is_sortable` 可以为 `true`；只有文本类型字段的 `is_searchable` 可以为 `true`
    - `tag` 类型的`is_searchable`和的`is_sortable`都不能为`true`


   

### 2.2.3. 请求创建数据源

参考链接：[创建数据源 - 服务端文档 - 开发文档 - 飞书开放平台](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source/create)

或者使用以下 curl 请求

**注**：请求成功会返回相应的 datasource ID

```bash
curl --location --request POST --max-time 10 'https://open.feishu.cn/open-apis/search/v2/data_sources' \
--header 'Authorization: Bearer ${Tenant Access Token}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "${数据源名称}",
    "description": "${数据源描述：可选}",
    "icon_url": "${数据源对应 search tab 的图标}",
    "schema_id": "example_schema",
    "template": "search_common_card",
    "state": 1,
     "i18n_name": {
        "zh_cn": "${中文名}",
        "en_us": "${英文名}",
        "ja_jp": "${日文名}"
    },
    "i18n_description": {
        "zh_cn": "${中文描述}",
        "en_us": "${英文描述}",
        "ja_jp": "${日文描述}"
    }
}'
```

说明：

1.  icon_url 指如下的图标：（支持 png、jpeg 格式图片，>= 200*200 像素）。需要使用**公网可访问**的图片链接。

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/d9cfbc8e595651aa6affe0cdfc353213_OKGy1ZQIye.png?height=296&lazyload=true&width=1690)

2.  `i18n` 目前支持：`i18n_name`、`i18n_description`两个字段，如果没有取到对应的 `i18n` 字段，则会显示默认字段。
3.  由于需要新建集群索引，该请求的耗时较长（大约5s），请耐心等待。如果新建失败了，可以进行重试，重试再失败请提起反馈；
4.  `template`，`schema_id`字段都是指定数据源绑定的模版
    - `template` 目前仅支持 `search_common_card`，`schema_id`是创建好的数据范式对应的ID
    - 如果设置了`schema_id`会优先绑定对应的数据范式，否则会根据`template`对应的模版来创建数据源，建议使用`schema_id`的方式来创建数据源。


### 2.2.4. 请求创建数据项

参考链接：[索引数据项 - 服务端文档 - 开发文档 - 飞书开放平台](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source-item/create)

1.  限频次数：1000次/秒；
2.  可以参考使用以下 curl 请求；
3.  metadata 中的 create_time 和 update_time 可省略。若输入，则输入形式为数字，且为 Unix Timestamp 时间。

```bash
curl --location --request POST 'https://open.feishu.cn/open-apis/search/v2/data_sources/${Datasource ID}/items' \
--header 'Authorization: Bearer ${Tenant Access Token}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": "${Item ID}",
    "acl": [{
        "access": "allow",
        "type": "user",
        "value": "everyone"
    }],
    "metadata": {
        "create_time": ${Unix Timestamp},
        "source_url": "${App Link}",
        "title": "${Title}",
        "update_time": ${Unix Timestamp}
    },
    "structured_data": "{\"summary\":\"${Summary}\",\"icon_url\":\"${IconURL}\"}"
}'
```

说明：


![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/8dd9a52f171a771104311afb11986dc4_M3Z6ypj4UU.png?height=180&lazyload=true&width=1892)
以如下schema为例子
```json
 "display": {
        "card_key": "search_common_card",
        "fields_mapping": [
         {
                    "data_field": "${priority}",
                    "display_field": "tag1"
                },
                {
                    "data_field": "${status}",
                    "display_field": "tag2"
                },
                {
                    "data_field": "${type}",
                    "display_field": "tag3"
                },
                {
                    "data_field": "${content}",
                    "display_field": "summary"
                },
                 {
                    "data_field": "${create_time}",
                    "display_field": "footer"
                }
        ]
    }
```
1.  黄色框：`metadata` 中的 `title` 字段，该字段支持搜索
2.  红色框：数据范式中`field_mapping`定义的映射到`icon_url`字段的信息；支持 png、jpeg 格式图片，>= 200*200 像素；`icon_url`为`structured_data`中字段
```json 
  {				   
    "structured_data":"{\icon_url\":"\www.feishu.com\"}"
   }
```
3.  绿色框：`field_mapping`中定义的映射到`summary`字段的信息，`content`为`structured_data`中字段
	
```json 
  {				   
    "structured_data":"{\content\":"\测试摘要\"}"
   }
``` 


4.  蓝色框：数据范式中`field_mapping`定义的映射到`summary`字段的信息；`create_time`为`metadata`中字段
5. 黑色框： 数据范式中`field_mapping`定义的映射到`tag1``tag2``tag3`字段的信息，为`structured_data`中字段
```json
{				   
    "structured_data":"{\"type\":\"person\",\"status\":\"open\",\"priority\":\"nomal\"}"
   }
```
6.  黑色框：`metadata` 中的 `source_url` 字段中指定的链接,为`metadata`中字段

<br>
特别说明：

1.  目前仅支持根据 `title` 和 `summary` 字段来进行搜索。
2.  请求体中的 `structured_data` 是一个 JSON 字符串。
    -  上图数据完整的请求体为：

```json
{
    "id": "item_1",
    "acl": [{
        "access": "allow",
        "type": "user",
        "value": "everyone"
    }],
    "metadata": {
        "create_time": 1627460490,
        "source_url": "www.baidu.com",
        "title": "title1",
        "update_time": 1627460490
    },
    "structured_data": "{\"content\":\"测试摘要\",\"icon_url\":\"https://sf3-ttcdn-tos.pstatp.com/obj/mosaic-legacy/6eed0002408143b46441\"，\"priority\":\"nomal\"，\"status\":\"open\"，\"type\":\"urgent\"}"
}
```

3.  请求体中的 `id` 字段必须每个数据项唯一，否则会覆盖；
4. icon_url 仅支持 png、jpeg 格式图片。

# 3. 附录

## 3.1. ACL 说明（没有需求可跳过）

ACL 的配置结构如下：

```json
[{
    "access": "allow", // 使用 allow 或者 deny
    "type": "user",   
    "value": "everyone"
},{
    "access": "deny", // 使用 allow 或者 deny
    "type": "user",   
    "value": "${ID}"
},
 // ...
]
```

**规则说明**

1. `acl`参数**必须**填写，如果配置为空数组，则默认不可见；如果配置了 `acl`，则数据项权限默认为全员不可搜，需要在 `acl` 中添加 `access` 为 `allow` 的配置，确保部分人可搜；
    -  如果 `type` 为 `user` ，当 `access` 为 `allow` ，`value` 设置为 `everyone` 则全员可搜；
2.  如果 `type` 为 `user` ，则 `value` 为用户的 employeeID。获取方式为租户的管理员在“飞书管理后台”中查看（可批量导出）。如下图红框中的“6c368g48”；

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/9274ed4558720267df305d12d3b31b5a_tgN6XHUraS.png?height=1678&lazyload=true&width=3770)

3.  在优先级上，deny > allow。即如果 user1 既出现在 allow 列表中，又出现在 deny 列表中。则 user1 不可搜；
4.  `acl` 长度限制：allow和deny分别限制为1000；

<br>
**🙋‍♂️举例说明**

```json
{
    "id": "item_1",
    "acl": [],
    "metadata": {
        "create_time": 1632626242,
        "source_url": "https://www.feishu.cn",
        "title": "item01",
        "update_time": 1632626242
    },
    "structured_data": "{\"summary\":\"由北京发来贺电\",\"icon_url\":\"https://sf3-ttcdn-tos.pstatp.com/obj/mosaic-legacy/6eed0002408143b46441\"}"
}
```

根据规则1，因为没有配置 `acl` 字段，item_1 这个数据项全员不可见；

```json
{
    "id": "item_2",
    "acl": [{
        "access": "allow",
        "type": "user",
        "value": "everyone"
    }],
    "metadata": {
        "create_time": 1632626242,
        "source_url": "https://www.feishu.cn",
        "title": "item02",
        "update_time": 1632626242
    },
    "structured_data": "{\"summary\":\"由北京发来贺电\",\"icon_url\":\"https://sf3-ttcdn-tos.pstatp.com/obj/mosaic-legacy/6eed0002408143b46441\"}"
}
```

根据规则 1 ，item_2 这个数据项全员可搜；

```json
{
    "id": "item_3",
    "acl": [{
        "access": "allow",
        "type": "user",
        "value": "user1_employeeID"
    }, {
        "access": "allow",
        "type": "user",
        "value": "user2_employeeID"
    }],
    "metadata": {
        "create_time": 1632626242,
        "source_url": "https://www.feishu.cn",
        "title": "item03",
        "update_time": 1632626242
    },
    "structured_data": "{\"summary\":\"由北京发来贺电\",\"icon_url\":\"https://sf3-ttcdn-tos.pstatp.com/obj/mosaic-legacy/6eed0002408143b46441\"}"
}
```

因为 item_3 配置了 acl，该数据项仅 user1、user2用户可搜。

```json
{
    "id": item_4",
    "acl": [{
        "access": "allow",
        "type": "user",
        "value": "everyone"
    }, {
        "access": "deny",
        "type": "user",
        "value": "user2"
    }],
    "metadata": {
        "create_time": 1632626242,
        "source_url": "https://www.feishu.cn",
        "title": "item04",
        "update_time": 1632626242
    },
    "structured_data": "{\"summary\":\"由北京发来贺电\",\"icon_url\":\"https://sf3-ttcdn-tos.pstatp.com/obj/mosaic-legacy/6eed0002408143b46441\"}"
}
```

item_4 数据项除user2用户外全员可搜；



