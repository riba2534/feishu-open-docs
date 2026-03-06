---
title: "更新员工信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/directory-v1/employee/patch"
updateTime: "1772099264000"
---

# 更新员工信息

本接口用于更新在职/离职员工的信息、冻结/恢复员工。未传递的参数不会进行更新。
员工指飞书企业内身份为「Employee」的成员，等同于通讯录OpenAPI中的「User」。


> **Tip**: - 员工状态的修改遵循生命周期流转的规则，具体规则详见 [Directory-员工管理-资源介绍](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/directory-v1/employee/resources-introduction) 。
> - 本接口支持tenant_access_token和user_access_token，接口获取方式参考[获取访问凭证](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
> 。
>   - 使用tenant_access_token时，只能在当前应用的通讯录授权范围内更新员工信息。可在开发者后台 > 权限管理 > 通讯录权限 中查看。
>     - 当变更员工的部门信息时，应用需要有变更前后的部门权限，才能变更成功。
>   - 使用user_access_token 时，默认为管理员用户，将校验管理员管理范围。当用户有多个管理员身份均可更新员工信息时，管理员管理范围取最大集。管理员权限可查看帮助中心文档：[管理员创建管理员角色及分配权限](https://www.feishu.cn/hc/zh-CN/articles/360043495213-%E7%AE%A1%E7%90%86%E5%91%98%E5%88%9B%E5%BB%BA%E7%AE%A1%E7%90%86%E5%91%98%E8%A7%92%E8%89%B2%E5%8F%8A%E5%88%86%E9%85%8D%E6%9D%83%E9%99%90#tabs0|lineguid-dU31C)
> - 变更「未加入」、「未激活」状态的员工的联系手机号、工作邮箱，会修改员工的登录凭证，并将员工重置为「未加入」状态，并发送邀请短信/邮件。其他状态的员工修改联系方式不影响登录凭证。
> - 修改员工ID（employee_id）需要悉知以下影响：
>   - 员工ID（employee_id）是员工在企业内的唯一ID，可能会被应用引用来实现各种内部逻辑，唯一ID修改之后可能会导致引用失败，导致所有引用且保存了‘被修改 ID 员工’的业务全部受影响。
> - 更新离职状态的员工信息时，以下字段不可更新：
>   - email、mobile、department_ids、leader_id、is_frozen、work_city_id


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/directory/v1/employees/:employee_id |
| HTTP Method | PATCH |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `directory:employee.update:write` 更新员工 `directory:employee:write` 创建、更新、离职、恢复员工 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `directory:employee.base.external_id:read` 查看员工自定义 ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` 或 `user_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `employee_id` | `string` | 员工ID，与employee_id_type类型保持一致。<br>**示例值**："eehsdna" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employee_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `employee_id`: 企业内在职员工的唯一标识。支持自定义，未自定义时系统自动生成。ID支持修改。 获取employee_id的方式：   - 企业管理员在 管理后台 > 组织架构 > 成员与部门 页面，点击 成员详情，查询员工ID   - 通过 [批量获取员工列表](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/directory-v1/employee/filter) 的接口，通过手机号或邮箱查询员工ID。<br>**默认值**：`open_id`<br>**当值为 `employee_id`，字段权限要求**： `directory:employee.base.external_id:read` 查看员工自定义 ID |
| `department_id_type` | `string` | 否 | 部门ID类型<br>**示例值**：open_department_id<br>**可选值有**：<br>- `department_id`: department_id - `open_department_id`: open_department_id<br>**默认值**：`open_department_id` |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employee` | `update_employee` | 是 | 更新员工对象 |
| &nbsp;&nbsp;└ `name` | `upsert_name` | 否 | 姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `i18n_text` | 是 | 员工的姓名。 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 是 | 默认值<br>长度范围：1- 64 字符<br>**示例值**："工位" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 否 | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值<br>**示例值**：{"zh_cn":"工位1"} |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `another_name` | `string` | 否 | 别名，最多可输入 64 字<br>**示例值**："Jack" |
| &nbsp;&nbsp;└ `mobile` | `string` | 否 | 员工的手机号，最多可输入 255 字。注意： 1. 在企业内的在职员工中不可重复 2. 未认证企业仅支持添加中国大陆手机号，通过飞书认证的企业允许添加海外手机号 3. 国际电话区号前缀中必须包含加号 +<br>**示例值**："13011111111" 或 "+8613011111111" |
| &nbsp;&nbsp;└ `custom_employee_id` | `string` | 否 | 企业内在职员工的唯一标识。支持自定义，未自定义时系统自动生成。ID支持修改。注意： 1. 在职员工的ID不可重复。 2. ID不能包含空格。<br>**示例值**："eesadeq" |
| &nbsp;&nbsp;└ `avatar_key` | `string` | 否 | 员工的头像key。获取图片的key请使用 [上传图片 - 服务端 API - 开发文档 - 飞书开放平台](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/create)，上传时图片类型需要选择 用于设置头像<br>**示例值**："dadwqeqwdsa" |
| &nbsp;&nbsp;└ `email` | `string` | 否 | 员工在工作中的邮箱。注意： 1. 在企业内的在职员工中不可重复。 2. 非中国大陆手机号成员必须同时添加邮箱。<br>**示例值**："zhangsan@163.com" |
| &nbsp;&nbsp;└ `enterprise_email` | `string` | 否 | 员工的企业邮箱。请先确保已在管理后台启用飞书邮箱服务。企业邮箱的域名需要企业在管理后台申请并开启。如果企业没有开启对应域名的企业邮箱，设置用户的企业邮箱会操作失败。<br>**示例值**："zhangsan@163.com" |
| &nbsp;&nbsp;└ `gender` | `int` | 否 | 性别<br>**示例值**：1<br>**可选值有**：<br>- `0`: 未知 - `1`: 男 - `2`: 女 - `3`: 其他 |
| &nbsp;&nbsp;└ `employee_order_in_departments` | `upsert_user_department_sort_info\[\]` | 否 | 员工在所属部门内的排序信息<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 否 | 部门id，与department_id_type类型保持一致。<br>**示例值**："eediasdjw" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `order_weight_in_deparment` | `string` | 否 | 员工在部门内的排序权重<br>**数据校验规则：**<br>**示例值**："100" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `order_weight_among_deparments` | `string` | 否 | 该部门在用户所属的多个部门间的排序权重<br>**示例值**："20" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_main_department` | `boolean` | 否 | 是否为用户的主部门（用户只能有一个主部门，且排序权重应最大，不填则默认使用系统默认排序下的第一个部门作为主部门，系统默认排序与部门数组传入顺序无关）<br>**示例值**：true |
| &nbsp;&nbsp;└ `background_image_key` | `string` | 否 | 背景图的key。获取图片的key请使用 [上传图片 - 服务端 API - 开发文档 - 飞书开放平台](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/create)，上传时图片类型需要选择 用于发送消息<br>**示例值**："qweasdqawqeq" |
| &nbsp;&nbsp;└ `description` | `string` | 否 | 员工的个性签名<br>**示例值**："新员工入职" |
| &nbsp;&nbsp;└ `leader_id` | `string` | 否 | 员工的直属上级ID。注意： 1. 不可成环，即A的上级是B，B的上级是A。 2. 上级需要是一个在职的员工。<br>**示例值**："eeshfosd" |
| &nbsp;&nbsp;└ `dotted_line_leader_ids` | `string\[\]` | 否 | 员工的虚线上级ID，与employee_id_type类型保持一致。注意： 1. 不可成环，即A的上级是B，B的上级是A。 2. 上级需要是一个在职的员工。<br>**示例值**：["eefhdgsd"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `10` |
| &nbsp;&nbsp;└ `work_country_or_region` | `string` | 否 | 工作地国家/地区码。获取国家/地区的编码请使用 [分页批量查询国家/地区](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/mdm-v3/country_region/list)。<br>**示例值**："MDM2312312" |
| &nbsp;&nbsp;└ `work_place_id` | `string` | 否 | 工作地点ID<br>**示例值**："1111sdda" |
| &nbsp;&nbsp;└ `work_station` | `i18n_text` | 否 | 工位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 是 | 默认值<br>**示例值**："工位" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 否 | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值<br>**示例值**：{"zh_cn":"工位"} |
| &nbsp;&nbsp;└ `job_number` | `string` | 否 | 工号。企业内在职员工的工号不可重复。<br>**示例值**："28549233" |
| &nbsp;&nbsp;└ `extension_number` | `string` | 否 | 分机号，最多可输入 99 字。企业内所有员工的分机号不可重复。<br>**示例值**："2854923" |
| &nbsp;&nbsp;└ `join_date` | `string` | 否 | 入职日期<br>固定格式为：'YYYY-MM-DD' , 固定长度为：10<br>**示例值**："2022-10-10" |
| &nbsp;&nbsp;└ `employment_type` | `int` | 否 | 员工类型<br>**示例值**：1<br>**可选值有**：<br>- `0`: 未知 - `1`: 全职 - `2`: 实习 - `3`: 外包 - `4`: 劳务 - `5`: 顾问 |
| &nbsp;&nbsp;└ `job_title_id` | `string` | 否 | 职务ID<br>**示例值**："ewdjdssd" |
| &nbsp;&nbsp;└ `job_level_id` | `string` | 否 | 职级ID<br>**示例值**："asdfghjk" |
| &nbsp;&nbsp;└ `job_family_id` | `string` | 否 | 序列ID<br>**示例值**："qwertyui" |
| &nbsp;&nbsp;└ `resign_date` | `string` | 否 | 离职日期<br>固定格式为：'YYYY-MM-DD' , 固定长度为：10<br>**示例值**："2022-10-10"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `20` 字符 |
| &nbsp;&nbsp;└ `resign_reason` | `string` | 否 | 离职原因<br>**示例值**："1"<br>**可选值有**：<br>- `0`: 置空 - `1`: 薪酬不符合预期 - `2`: 工作时间过长 - `3`: 不满意工作内容 - `4`: 不认可上级或管理层 - `5`: 职业发展机会有限 - `6`: 对公司文化缺乏认同 - `7`: 组织架构调整（主动离职） - `8`: 合同到期 - `9`: 跳槽 - `10`: 转行 - `11`: 家庭原因 - `12`: 健康状况不佳 - `13`: 工作地点原因 - `14`: 其他(主动离职) - `15`: 意外 - `16`: 身故 - `17`: 解雇 - `18`: 试用期不通过 - `19`: 工作表现不佳 - `20`: 工作产出低 - `21`: 组织架构调整（被动离职） - `22`: 违纪 - `23`: 违法 - `24`: 其他（被动离职） - `25`: 其他（其他） |
| &nbsp;&nbsp;└ `resign_remark` | `string` | 否 | 离职备注信息<br>**示例值**："个人原因"<br>**数据校验规则**：<br>- 长度范围：`0` ～ `255` 字符 |
| &nbsp;&nbsp;└ `resign_type` | `string` | 否 | 离职类型<br>**示例值**："1"<br>**可选值有**：<br>- `0`: 置空 - `1`: 主动 - `2`: 被动 - `3`: 其他 |
| &nbsp;&nbsp;└ `is_frozen` | `boolean` | 否 | 是否冻结员工账号。 true为冻结，false为恢复账号。<br>**示例值**：true |
| &nbsp;&nbsp;└ `custom_field_values` | `custom_field_value\[\]` | 否 | 自定义字段<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `field_type` | `string` | 否 | 自定义字段类型<br>**示例值**："1"<br>**可选值有**：<br>- `1`: 多行文本 - `2`: 网页链接 - `3`: 枚举选项 - `4`: 人员 - `9`: 电话 - `10`: 多选枚举类型(目前仅支持文本类型) - `11`: 人员列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text_value` | `i18n_text` | 否 | 文本字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 是 | 默认值<br>**示例值**："姓名字段" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 否 | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值<br>**示例值**：{"zh_cn":"姓名字段"} |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `url_value` | `url_value` | 否 | 网页链接字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `link_text` | `i18n_text` | 是 | 网页标题 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `default_value` | `string` | 是 | 默认值<br>**示例值**："网页标题" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_value` | `map<string, string>` | 否 | 国际化值，key为zh_cn, ja_jp, en_us, value为对应的值<br>**示例值**：{"zh_cn":"网页标题"} |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `url` | `string` | 是 | 移动端网页链接<br>**示例值**："https://m.bytedance.com/afnasjfna" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `pcurl` | `string` | 是 | 桌面端网页链接<br>**示例值**："http://www.fs.cn" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value` | `enum_value` | 否 | 枚举 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_ids` | `string\[\]` | 是 | 选项结果ID<br>**示例值**：["1"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_type` | `string` | 是 | 选项类型<br>**示例值**："1"<br>**可选值有**：<br>- `1`: 文本 - `2`: 图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_values` | `user_value\[\]` | 否 | 人员字段值<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ids` | `string\[\]` | 是 | 人员ID，与employee_id_type类型保持一致。<br>**示例值**：["1"]<br>**数据校验规则**：<br>- 长度范围：`0` ～ `100` |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `phone_value` | `phone_value` | 否 | 电话字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone_number` | `string` | 是 | 电话号<br>**示例值**："18812345678" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `extension_number` | `string` | 否 | 分机号<br>**示例值**："234234234" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `field_key` | `string` | 否 | 自定义字段key<br>**示例值**："C-1000001" |


### 请求体示例

```json
{
    "employee": {
        "name": {
            "name": {
                "default_value": "张三",
                "i18n_value": {
                    "zh_cn": "张三",
                    "ja_jp": "佐藤はるか",
                    "en_us": "Alex Zhang"
                }
            },
            "another_name": "Jack"
        },
        "mobile": "+8613011111111",
        "custom_employee_id": "u273y71",
        "avatar_key": "8abc397a-9950-44ea-9302-e1d8fe00858g",
        "email": "zhangsan@test.com",
        "enterprise_email": "zhangsan@test.com",
        "gender": 1,
        "employee_order_in_departments": [
            {
                "department_id": "0",
                "order_weight_in_deparment": "100",
                "order_weight_among_deparments": "20",
                "is_main_department": false
            }
        ],
        "leader_id": "eeasdqwwe",
        "dotted_line_leader_ids": [
            "hdsuqw"
        ],
        "work_country_or_region": "MDM34234234",
        "work_place_id": "eqwedas",
        "work_station": {
            "default_value": "张三",
            "i18n_value": {
                "zh_cn": "工位",
                "ja_jp": "工位",
                "en_us": "Work Station"
            }
        },
        "job_number": "2845435",
        "extension_number": "2845435",
        "join_date": "2022-10-10",
        "employment_type": "1",
        "staff_status": "",
        "job_title_id": "wqedsaqw",
        "resign_reason": "",
        "resign_type": "",
        "custom_field_values": [
            {
                "field_type": "1",
                "text_value": {
                    "default_value": "姓名字段",
                    "i18n_value": {
                        "zh_cn": "姓名字段",
                        "ja_jp": "姓名字段",
                        "en_us": "Name Filed"
                    }
                },
                "url_value": {
                    "link_text": {
                        "default_value": "网页地址",
                        "i18n_value": {
                            "zh_cn": "网页地址",
                            "ja_jp": "This is a URL",
                            "en_us": "This is a URL"
                        }
                    },
                    "url": "https://www.feishu.cn/",
                    "pcurl": "https://www.feishu.cn/"
                },
                "enum_value": {
                    "enum_ids": [
                        "75ec5g97"
                    ],
                    "enum_type": "1"
                },
                "user_values": [
                    {
                        "ids": [
                            "27al2hef"
                        ]
                ],
                "field_key": "C-1000001"
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
| `data` | `\-` | \- |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {}
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2221164 | User name exceeds limit | 姓名长度超过限制，最多可输入 64 字 |
| 400 | 2221165 | User en_name exceeds limit | 英文名长度超过限制，最多可输入 64 字 |
| 400 | 2221166 | User another_name exceeds limit | 别名长度超过限制，最多可输入 64 字 |
| 400 | 2221103 | Mobile already exists | 手机号已存在，请修改手机号 |
| 400 | 2221106 | Invalid mobile | 无效手机号，请修改手机号 |
| 400 | 2221113 | Mobile or email not set | 手机号或邮箱必填 |
| 400 | 2221114 | User must have a mobile in China | 中国必须有手机号，请添加中国手机号 |
| 400 | 2221156 | Unable to edit verified mobile | 不允许编辑已认证手机号，请不要编辑已认证手机号或通过其他方式修改 |
| 400 | 2221104 | Email already exists | 邮箱已存在，请求修改邮箱 |
| 400 | 2221107 | Invalid email | 无效的邮箱，请求修改企业邮箱 |
| 400 | 2221118 | Enterprise email already exists | 企业邮箱已存在，请求修改企业邮箱 |
| 400 | 2221278 | Invalid enterprise email | 无效的邮箱，请求修改企业邮箱 |
| 400 | 2221126 | Enterprise email domain unavailable | 企业邮箱域名不可用，请求修改企业邮箱 |
| 400 | 2221146 | Enterprise email alias exceeds limit | 企业邮箱别名超过长度限制，最多可输入 255 字 |
| 400 | 2221147 | Enterprise email address in recycle bin | 企业邮箱地址在回收站中，请修改企业邮箱 |
| 400 | 2221176 | Add Feishu allow list tenant. Email must be included with non+86mobile | 飞书租户添加非+86的手机号时必须包含邮件信息，请包含邮件信息 |
| 400 | 2221255 | Main department must be the first | 员工在所属部门内的排序信息中主部门必须在第一个，请修改员工所属部门内的排序信息 |
| 400 | 2221125 | The number of members within the department exceeds the limit. Please contact an administrator for help | 部门内成员人数超过限制，人数不能超过一万，请联系管理员寻求帮助。 |
| 400 | 2221129 | User department is empty | 员工所属部门为空，请修改员工所属部门内的排序信息 |
| 400 | 2221141 | Unable to join multiple departments. Please upgrade relevant 'Organizational Structure Visible'. | 无法加入多个部门，请修改员工所属部门内的排序信息 |
| 400 | 2221181 | Department does not exist | 部门不存在，请修改员工所属部门内的排序信息 |
| 400 | 2221239 | Leader loop error | 直属上级成环，请修改直属上级 |
| 400 | 2221238 | DottedLineLeaderID loop error | 虚线上级成环，请修改虚线上级 |
| 400 | 2221221 | DottedLineLeaderID exceeds length limit | 虚线上级长度超过限制，请修改虚线上级 |
| 400 | 2221222 | Invalid dottedLineLeaderID | 无效的虚线上级ID，请修改虚线上级 |
| 400 | 2221242 | Invalid custom field | 无效的自定义字段，请修改自定义字段 |
| 400 | 2221216 | Invalid work country or region | 无效的工作国家或区域，请修改工作国家或区域 |
| 400 | 2221217 | WorkplaceID not found | 工作城市不存在，请修改工作城市 |
| 400 | 2221240 | JobNumber not unique | 工号已存在，请修改工号 |
| 400 | 2221191 | Invalid extension number | 分机号无效，请修改分机号 |
| 400 | 2221192 | Repeated extension number within the tenant | 分机号已存在，请修改分机号 |
| 400 | 2221193 | Extension number exceeds limit | 分机号长度超过限制，最多可输入 99 字 |
| 400 | 2221210 | Invalid join date | 无效的入职时间，请修改入职时间 |
| 400 | 2221144 | EmployeeType not found | 人员类型不存在，请修改人员类型 |
| 400 | 2221145 | EmployeeType inactive | 人员类型未激活，请修改人员类型 |
| 400 | 2221223 | Invalid job title ID | 职务不存在，请修改职务 |
| 400 | 2221263 | Tenant has not activated multi geo | 租户未开启Multi-Geo，请先开通再试。Multi-Geo指的是多地理位置数据驻留。 |
| 400 | 2221264 | User geo does not exist | 指定的Geo不存在，请检查Geo参数是否正确。可通过**获取地理位置列表**接口查询企业开通的Geo，请注意这里需要传入**小写字母**。 |
| 400 | 2221265 | The application does not have permission to write to the geo | 无权限指定员工Geo，需申请，点击api调试台-权限配置，会显示需要的权限，点击“操作”-“...”-“开通”，即可。 `directory:employee.base.geo:write` 写入员工数据所在地 |
| 400 | 2221266 | The application does not have permission to write to the SubscriptionID | 无权限指定席位，需申请，点击api调试台-权限配置，会显示需要的权限，点击“操作”-“...”-“开通”，即可。        `directory:employee.base.subscription_ids:write` 写入员工席位信息 |
| 400 | 2224001 | No permission to operate | 无操作权限，请检查当前应用的权限或企业版本是否是商业专业版本及以上。 |
| 400 | 2224002 | No permission to operate record | 无操作该记录权限，请检查当前应用的数据管理范围的权限或当前应用所操作的成员是否可更新。 |
| 400 | 2224003 | No permission to operate dependent object | 无操作依赖对象权限，请检查要更新到的部门是否有权限。 |
| 400 | 2221252 | Hybrid license tenant prohibits passing empty licenses to create users | 混合许可证租户禁止传递空许可证来创建用户，请传递有效的许可证 |
| 400 | 2221253 | Designated licenseID is insufficient | 剩余席位不足，请修改席位信息 |
| 400 | 2221254 | Designated licenseID is invalid | 应用没有权限写入员工数据驻留地，需申请写入员工数据驻留地权限(directory:employee.base.geo:write) |
| 400 | 2221111 | Exceeds certified seat limit | 混合许可证租户禁止传递空许可证来创建用户，请传递有效的许可证 |
| 400 | 2221112 | Exceeds billing plan seat limit | 剩余席位不足，请修改席位信息 |
| 400 | 2221115 | ExternalID is not unique | 自定义ID已存在，请修改自定义ID |
| 400 | 2221116 | Invalid ExternalID | 无效的自定义ID，请修改自定义ID |
| 400 | 2221175 | Feishu only supports +86mobile | 飞书租户仅支持+86手机号，请修改手机号 |
| 400 | 2221182 | Unable to freeze tenant founder | 无法冻结企业管理员，请选择非企业管理员用户进行冻结操作 |
| 400 | 2221109 | Name contains sensitive info | 姓名包含敏感信息，请修改姓名 |
| 400 | 2221292 | User department is disabled | 用户部门已停用，请将用户转移至未停用的部门或激活该部门 |
| 400 | 2221213 | Resign date invalid or earlier than join date or empty | 请检查离职日期格式可能非法、离职日期早于加入日期、离职日期为空 |
| 400 | 2221214 | Resign reason invalid or not match resign type | 离职原因非法，或者离职原因和离职类型不匹配，请修改离职原因或离职类型使其匹配 |
| 400 | 2221293 | Only allow update preResigned\resigned employee's resign info field | 只允许更新待离职、离职人员的离职信息字段（离职备注、离职类型、离职原因、离职日期），请更新待离职或离职人员的对应字段 |
| 400 | 2221231 | Resign type invalid or not match resign reason | 离职类型非法，或者离职原因和离职类型不匹配，请修改离职类型或离职原因使其匹配 |


