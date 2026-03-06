---
title: "批量获取员工花名册信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/ehr/ehr-v1/employee/list"
updateTime: "1734660749000"
---

# 批量获取员工花名册信息

根据员工飞书用户 ID / 员工状态 / 雇员类型等搜索条件 ，批量获取员工花名册字段信息。字段包括「系统标准字段 / system_fields」和「自定义字段 / custom_fields」。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/ehr/v1/employees |
| HTTP Method | GET |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `ehr:employee:readonly` 获取飞书人事（标准版）应用中的员工花名册信息 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `view` | `string` | 否 | 返回数据类型，不传值默认为 basic。<br>**示例值**：basic<br>**可选值有**：<br>- `basic`: 概览，只返回 id、name 等基本信息 - `full`: 明细，返回系统标准字段和自定义字段集合 |
| `status` | `int\[\]` | 否 | 员工状态，不传代表查询所有员工状态<br>实际在职 = 2&4<br>可同时查询多个状态的记录，如 status=2&status=4<br>**示例值**：2<br>**可选值有**：<br>- `1`: 待入职 - `2`: 在职 - `3`: 已取消入职 - `4`: 待离职 - `5`: 已离职 |
| `type` | `int\[\]` | 否 | 人员类型，不传代表查询所有人员类型<br>同时可使用自定义员工类型的 int 值进行查询，可通过下方接口获取到该租户的自定义员工类型的名称，参见 [获取人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)<br>**示例值**：1<br>**可选值有**：<br>- `1`: 全职 - `2`: 实习 - `3`: 顾问 - `4`: 外包 - `5`: 劳务 |
| `start_time` | `string` | 否 | 查询开始时间（入职时间 >= 此时间）<br>**示例值**：1608690517811 |
| `end_time` | `string` | 否 | 查询结束时间（入职时间 <= 此时间）<br>**示例值**：1608690517811 |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| `user_ids` | `string\[\]` | 否 | user_id、open_id 或 union_id，默认为 open_id。<br>如果传入的值不是 open_id，需要一并传入 user_id_type 参数。<br>可一次查询多个 id 的用户，例如：user_ids=ou_8ebd4f35d7101ffdeb4771d7c8ec517e&user_ids=ou_7abc4f35d7101ffdeb4771dabcde<br>[用户相关的 ID 概念](https://open.larkoffice.com/document/home/user-identity-introduction/introduction)<br>**示例值**：ou_8ebd4f35d7101ffdeb4771d7c8ec517e<br>**数据校验规则**：<br>- 最大长度：`100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：10 |
| `page_size` | `int` | 否 | 分页大小，取值范围 1~100，默认 10<br>**示例值**：10<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |


请求体示例


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `items` | `employee\[\]` | 员工列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 员工的用户 ID<br>user_id_type 为 user_id 时返回 user_id；<br>user_id_type 为 open_id 时返回 open_id；<br>user_id_type 为 union_id 时返回 union_id；<br>「待入职」和「已取消入职」的员工，此字段值为 null |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `system_fields` | `system_fields` | 系统字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 中文姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department_id` | `string` | 部门的飞书 open_department_id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `manager` | `manager` | 上级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 上级的用户 ID（user_id） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 中文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_name` | `string` | 英文名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `job` | 职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `int` | 职位 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_level` | `job_level` | 职级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `int` | 职级 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 职级名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_location` | `work_location` | 工作地点 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `int` | 工作地点 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 工作地点名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `int` | 性别<br>**可选值有**：<br>- `1`: 男 - `2`: 女 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `birthday` | `string` | 出生日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `native_region` | `native_region` | 籍贯 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `iso_code` | `string` | ISO 编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ethnicity` | `int` | 民族<br>**可选值有**：<br>- `1`: 汉族 - `2`: 蒙古族 - `3`: 回族 - `4`: 藏族 - `5`: 维吾尔族 - `6`: 苗族 - `7`: 彝族 - `8`: 壮族 - `9`: 布依族 - `10`: 朝鲜族 - `11`: 满族 - `12`: 侗族 - `13`: 瑶族 - `14`: 白族 - `15`: 土家族 - `16`: 哈尼族 - `17`: 哈萨克族 - `18`: 傣族 - `19`: 黎族 - `20`: 傈僳族 - `21`: 佤族 - `22`: 畲族 - `23`: 高山族 - `24`: 拉祜族 - `25`: 水族 - `26`: 东乡族 - `27`: 纳西族 - `28`: 景颇族 - `29`: 阿昌族 - `30`: 柯尔克孜族 - `31`: 土族 - `32`: 达斡尔族 - `33`: 仫佬族 - `34`: 羌族 - `35`: 布朗族 - `36`: 撒拉族 - `37`: 毛南族 - `38`: 仡佬族 - `39`: 锡伯族 - `40`: 普米族 - `41`: 塔吉克族 - `42`: 怒族 - `43`: 乌孜别克族 - `44`: 俄罗斯族 - `45`: 鄂温克族 - `46`: 德昂族 - `47`: 保安族 - `48`: 裕固族 - `49`: 京族 - `50`: 塔塔尔族 - `51`: 独龙族 - `52`: 鄂伦春族 - `53`: 赫哲族 - `54`: 门巴族 - `55`: 珞巴族 - `56`: 基诺族 - `57`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `marital_status` | `int` | 婚姻状况<br>**可选值有**：<br>- `1`: 未婚 - `2`: 已婚 - `3`: 离异 - `4`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `political_status` | `int` | 政治面貌<br>**可选值有**：<br>- `1`: 中共党员 - `2`: 中国农工民主党 - `3`: 中国国民党革命委员会 - `4`: 中国民主促进会会员 - `5`: 中国民主同盟成员 - `6`: 中国民主建国会 - `7`: 中国致公党党员 - `8`: 九三学社社员 - `9`: 共青团员 - `10`: 其它党派成员 - `11`: 民主人士 - `12`: 群众 - `13`: 台湾民主自治同盟盟员 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `entered_workforce_date` | `string` | 参加工作日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id_type` | `int` | 证件类型<br>**可选值有**：<br>- `1`: 居民身份证 - `2`: 港澳居民来往内地通行证 - `3`: 台湾居民来往大陆通行证 - `4`: 护照 - `5`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id_number` | `string` | 证件号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_type` | `int` | 户口类型<br>**可选值有**：<br>- `1`: 本市城镇 - `2`: 外埠城镇 - `3`: 本市农村 - `4`: 外埠农村 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hukou_location` | `string` | 户口所在地 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_account_number` | `string` | 银行卡号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_name` | `string` | 开户行 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `social_security_account` | `string` | 社保账号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `provident_fund_account` | `string` | 公积金账号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_no` | `string` | 工号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_type` | `int` | 人员类型<br>同时可读取到自定义员工类型的 int 值，可通过下方接口获取到该租户的自定义员工类型的名称，参见 [获取人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list)<br>**可选值有**：<br>- `1`: 正式 - `2`: 实习 - `3`: 顾问 - `4`: 外包 - `5`: 劳务 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 员工状态<br>**可选值有**：<br>- `1`: 待入职 - `2`: 在职 - `3`: 已取消入职 - `4`: 待离职 - `5`: 已离职 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `hire_date` | `string` | 入职日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `probation_months` | `number(float)` | 试用期（月） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `conversion_date` | `string` | 转正日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `application` | `int` | 转正申请<br>**可选值有**：<br>- `1`: 未申请 - `2`: 审批中 - `3`: 被驳回 - `4`: 已通过 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `application_status` | `int` | 转正状态<br>**可选值有**：<br>- `1`: 无需转正 - `2`: 待转正 - `3`: 已转正 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `last_day` | `string` | 离职日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `departure_type` | `int` | 离职类型<br>**可选值有**：<br>- `1`: 主动 - `2`: 被动 - `3`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `departure_reason` | `int` | 离职原因<br>**可选值有**：<br>- `1`: 身体、家庭原因 - `2`: 职业发展 - `3`: 薪资福利不满意 - `4`: 工作压力大 - `5`: 合同到期不续签 - `6`: 其他 - `7`: 无法胜任工作 - `8`: 组织业务调整和岗位优化 - `9`: 违反公司条例 - `10`: 试用期未通过 - `11`: 其他 - `12`: 不满意工作内容 - `13`: 不认可上级或管理层 - `14`: 对公司文化缺乏认同 - `15`: 组织架构调整（主动离职） - `16`: 跳槽 - `17`: 转行 - `18`: 家庭原因 - `19`: 健康状况不佳 - `20`: 工作地点原因 - `21`: 意外 - `22`: 身故 - `23`: 解雇 - `24`: 工作产出低 - `25`: 违法 - `26`: 其他（其他） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `departure_notes` | `string` | 离职备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_company` | `contract_company` | 合同公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `int` | 公司 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 公司名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_type` | `int` | 合同类型<br>**可选值有**：<br>- `1`: 固定期限劳动合同 - `2`: 无固定期限劳动合同 - `3`: 实习协议 - `4`: 外包协议 - `5`: 劳务派遣合同 - `6`: 返聘协议 - `7`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_start_date` | `string` | 合同开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_expiration_date` | `string` | 合同到期日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contract_sign_times` | `int` | 劳动合同签订次数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `personal_email` | `string` | 个人邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `family_address` | `string` | 家庭地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `primary_emergency_contact` | `emergency_contact` | 主要紧急联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 紧急联系人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `relationship` | `int` | 与紧急联系人的关系<br>**可选值有**：<br>- `1`: 父母 - `2`: 配偶 - `3`: 子女 - `4`: 兄弟姐妹 - `5`: 朋友 - `6`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `emergency_contact` | `emergency_contact\[\]` | 紧急联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 紧急联系人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `relationship` | `int` | 与紧急联系人的关系<br>**可选值有**：<br>- `1`: 父母 - `2`: 配偶 - `3`: 子女 - `4`: 兄弟姐妹 - `5`: 朋友 - `6`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `highest_level_of_edu` | `education` | 最高学历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `int` | 学历<br>**可选值有**：<br>- `1`: 小学 - `2`: 初中 - `3`: 高中 - `4`: 职业高级中学 - `5`: 中等专业学校 - `6`: 大专 - `7`: 本科 - `8`: 硕士 - `9`: 博士 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `string` | 毕业学校 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `major` | `string` | 专业 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `int` | 学位<br>**可选值有**：<br>- `1`: 学士 - `2`: 硕士 - `3`: 博士 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end` | `string` | 结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `education` | `education\[\]` | 教育经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `int` | 学历<br>**可选值有**：<br>- `1`: 小学 - `2`: 初中 - `3`: 高中 - `4`: 职业高级中学 - `5`: 中等专业学校 - `6`: 大专 - `7`: 本科 - `8`: 硕士 - `9`: 博士 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `string` | 毕业学校 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `major` | `string` | 专业 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `int` | 学位<br>**可选值有**：<br>- `1`: 学士 - `2`: 硕士 - `3`: 博士 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end` | `string` | 结束日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `former_work_exp` | `work_experience` | 前工作经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company` | `string` | 公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 部门 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `string` | 职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end` | `string` | 截止日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 工作描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `work_exp` | `work_experience\[\]` | 工作经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company` | `string` | 公司 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 部门 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job` | `string` | 职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start` | `string` | 开始日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end` | `string` | 截止日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 工作描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id_photo_po_side` | `attachment\[\]` | 身份证照片（人像面） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 下载文件所需要的 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 文件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id_photo_em_side` | `attachment\[\]` | 身份证照片（国徽面） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 下载文件所需要的 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 文件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id_photo` | `attachment\[\]` | 证件照 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 下载文件所需要的 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 文件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `diploma_photo` | `attachment\[\]` | 学位证书 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 下载文件所需要的 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 文件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `graduation_cert` | `attachment\[\]` | 毕业证书 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 下载文件所需要的 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 文件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cert_of_merit` | `attachment\[\]` | 奖励证明 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 下载文件所需要的 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 文件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `offboarding_file` | `attachment\[\]` | 离职证明 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 下载文件所需要的 Token |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `mime_type` | `string` | 文件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `size` | `int` | 大小 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cancel_onboarding_reason` | `int` | 取消入职原因<br>**可选值有**：<br>- `1`: 个人原因 - `2`: 原单位留任 - `3`: 接受其他 Offer - `4`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `cancel_onboarding_notes` | `string` | 取消入职备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `employee_form_status` | `int` | 入职登记表状态<br>**可选值有**：<br>- `1`: 未发送 - `2`: 待提交 - `3`: 已提交 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `int` | 创建时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `update_time` | `int` | 更新时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `custom_fields` | `custom_fields\[\]` | 自定义字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 自定义字段key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `label` | `string` | 自定义字段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 自定义字段类型<br>**可选值有**：<br>- `text`: 文本类型 - `date`: 日期类型，如 2020-01-01 - `option`: 枚举类型 - `file`: 附件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 根据 type 不同，结构不同，不同 type 对应的数据结构在 type 的枚举值中有描述 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "user_id": "ou_db362c0e79f5a26db1ca8e94698ee417",
                "system_fields": {
                    "name": "张三",
                    "en_name": "Tony Zhang",
                    "email": "a@b.com",
                    "mobile": "(+86) 13812345678",
                    "department_id": "od-4d551617a5da3cec26666d33175dc8ca",
                    "manager": {
                        "user_id": "ou_db362c0e79f5a26db1ca8e94698ee417",
                        "name": "李四",
                        "en_name": "Tom Li"
                    },
                    "job": {
                        "id": 1695838220091399,
                        "name": "测试工程师"
                    },
                    "job_level": {
                        "id": 1695838220091399,
                        "name": "CEO"
                    },
                    "work_location": {
                        "id": 1695838220091399,
                        "name": "武汉"
                    },
                    "gender": 1,
                    "birthday": "2020-01-01",
                    "native_region": {
                        "iso_code": "CHN-11",
                        "name": "北京"
                    },
                    "ethnicity": 2,
                    "marital_status": 2,
                    "political_status": 2,
                    "entered_workforce_date": "2020-01-01",
                    "id_type": 1,
                    "id_number": "110122XXXXXX",
                    "hukou_type": 1,
                    "hukou_location": "北京市海淀区XXXX",
                    "bank_account_number": "1243253453",
                    "bank_name": "招商银行",
                    "social_security_account": "123124124",
                    "provident_fund_account": "123124235",
                    "employee_no": "TM-00001",
                    "employee_type": 1,
                    "status": 2,
                    "hire_date": "2020-01-01",
                    "probation_months": 2,
                    "conversion_date": "2020-01-01",
                    "application": 1,
                    "application_status": 2,
                    "last_day": "2020-01-01",
                    "departure_type": 1,
                    "departure_reason": 4,
                    "departure_notes": "世界那么大",
                    "contract_company": {
                        "id": 1695838220091399,
                        "name": "油条一号"
                    },
                    "contract_type": 1,
                    "contract_start_date": "2020-01-01",
                    "contract_expiration_date": "2020-01-01",
                    "contract_sign_times": 2,
                    "personal_email": "personal@email.com",
                    "family_address": "北京市海淀区XXXXX",
                    "primary_emergency_contact": {
                        "name": "张三",
                        "relationship": 1,
                        "mobile": "(+86) 13812345678"
                    },
                    "emergency_contact": [
                        {
                            "name": "张三",
                            "relationship": 1,
                            "mobile": "(+86) 13812345678"
                        }
                    ],
                    "highest_level_of_edu": {
                        "level": 8,
                        "school": "XXXX大学",
                        "major": "XXX专业",
                        "degree": 2,
                        "start": "2020-01-01",
                        "end": "2020-01-01"
                    },
                    "education": [
                        {
                            "level": 8,
                            "school": "XXXX大学",
                            "major": "XXX专业",
                            "degree": 2,
                            "start": "2020-01-01",
                            "end": "2020-01-01"
                        }
                    ],
                    "former_work_exp": {
                        "company": "XXXX公司",
                        "department": "部门1",
                        "job": "职位",
                        "start": "2020-01-01",
                        "end": "2020-01-01",
                        "description": "工作描述"
                    },
                    "work_exp": [
                        {
                            "company": "XXXX公司",
                            "department": "部门1",
                            "job": "职位",
                            "start": "2020-01-01",
                            "end": "2020-01-01",
                            "description": "工作描述"
                        }
                    ],
                    "id_photo_po_side": [
                        {
                            "id": "c7273e07ed9e40a394f88c7dccb49212",
                            "mime_type": "png",
                            "name": "Custom Code.png",
                            "size": 57380
                        }
                    ],
                    "id_photo_em_side": [
                        {
                            "id": "c7273e07ed9e40a394f88c7dccb49212",
                            "mime_type": "png",
                            "name": "Custom Code.png",
                            "size": 57380
                        }
                    ],
                    "id_photo": [
                        {
                            "id": "c7273e07ed9e40a394f88c7dccb49212",
                            "mime_type": "png",
                            "name": "Custom Code.png",
                            "size": 57380
                        }
                    ],
                    "diploma_photo": [
                        {
                            "id": "c7273e07ed9e40a394f88c7dccb49212",
                            "mime_type": "png",
                            "name": "Custom Code.png",
                            "size": 57380
                        }
                    ],
                    "graduation_cert": [
                        {
                            "id": "c7273e07ed9e40a394f88c7dccb49212",
                            "mime_type": "png",
                            "name": "Custom Code.png",
                            "size": 57380
                        }
                    ],
                    "cert_of_merit": [
                        {
                            "id": "c7273e07ed9e40a394f88c7dccb49212",
                            "mime_type": "png",
                            "name": "Custom Code.png",
                            "size": 57380
                        }
                    ],
                    "offboarding_file": [
                        {
                            "id": "c7273e07ed9e40a394f88c7dccb49212",
                            "mime_type": "png",
                            "name": "Custom Code.png",
                            "size": 57380
                        }
                    ],
                    "cancel_onboarding_reason": 2,
                    "cancel_onboarding_notes": "个人原因",
                    "employee_form_status": 1,
                    "create_time": 1608690517811,
                    "update_time": 1608690517811
                },
                "custom_fields": [
                    {
                        "key": "field_xxxxxxxx",
                        "label": "自定义字段 1",
                        "type": "date",
                        "value": "2021-01-13"
                    }
                ]
            }
        ],
        "page_token": "10",
        "has_more": true
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1241001 | 服务器内部错误 | 重试或联系飞书人事（标准版）客服 |
| 400 | 1241002 | 请求参数错误 | 检查查询参数 |
| 400 | 1241004 | 你的企业尚未开通飞书人事（标准版）。如需开通，请前往「飞书管理后台」启用飞书人事（标准版） | 前往「飞书管理后台」启用飞书人事（标准版） |


