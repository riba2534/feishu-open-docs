---
title: "按 ID 查询考勤组"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/group/get"
updateTime: "1749126320000"
---

# 按 ID 查询考勤组

通过考勤组 ID 获取考勤组详情。包含基本信息、考勤班次、考勤方式、考勤设置信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/attendance/v1/groups/:group_id |
| HTTP Method | GET |
| 接口频率限制 | [50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `attendance:rule` 写入打卡管理规则 `attendance:rule:readonly` 导出打卡管理规则 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `group_id` | `string` | 考勤组 ID，获取方式：1）[创建或修改考勤组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/group/create) 2）[按名称查询考勤组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/group/search) 3）[获取打卡结果](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/user_task/query)<br>**示例值**："6919358128597097404" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employee_type` | `string` | 是 | 请求体和响应体中的 user_id 和 creator_id 的员工id类型。如果没有后台管理权限，可使用[通过手机号或邮箱获取用户 ID](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch_get_id)<br>**示例值**：employee_id<br>**可选值有**：<br>- `employee_id`: 员工 employee ID，即[飞书管理后台](https://example.feishu.cn/admin/contacts/departmentanduser) > 组织架构 > 成员与部门 > 成员详情中的用户 ID - `employee_no`: 员工工号，即[飞书管理后台](https://example.feishu.cn/admin/contacts/departmentanduser) > 组织架构 > 成员与部门 > 成员详情中的工号 |
| `dept_type` | `string` | 是 | 部门 ID 的类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 暂时只支持部门的 openid。具体概念请参考[部门资源介绍](https://open.larkoffice.com/document/server-docs/contact-v3/department/field-overview)中的open_department_id |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `group` | \- |
| &nbsp;&nbsp;└ `group_id` | `string` | 考勤组 ID |
| &nbsp;&nbsp;└ `group_name` | `string` | 考勤组名称 |
| &nbsp;&nbsp;└ `time_zone` | `string` | 时区 |
| &nbsp;&nbsp;└ `bind_dept_ids` | `string\[\]` | 绑定的部门 ID（与「need_punch_members」同时使用时，以当前字段为准）。对应dept_type |
| &nbsp;&nbsp;└ `except_dept_ids` | `string\[\]` | 排除的部门 ID（该字段已下线） |
| &nbsp;&nbsp;└ `bind_user_ids` | `string\[\]` | 绑定的用户 ID（与「need_punch_members」同时使用时，以当前字段为准），对应employee_type |
| &nbsp;&nbsp;└ `except_user_ids` | `string\[\]` | 排除的用户 ID（该字段已下线），对应employee_type |
| &nbsp;&nbsp;└ `group_leader_ids` | `string\[\]` | 考勤主负责人 ID 列表，必选字段（需至少拥有考勤组管理员权限），对应employee_type |
| &nbsp;&nbsp;└ `sub_group_leader_ids` | `string\[\]` | 考勤子负责人 ID 列表，对应employee_type |
| &nbsp;&nbsp;└ `allow_out_punch` | `boolean` | 是否允许外勤打卡 |
| &nbsp;&nbsp;└ `out_punch_need_approval` | `boolean` | 外勤打卡需审批（需要允许外勤打卡才能设置生效） |
| &nbsp;&nbsp;└ `out_punch_need_post_approval` | `boolean` | 外勤打卡需审批，先打卡后审批（需要允许外勤打卡才能设置生效） |
| &nbsp;&nbsp;└ `out_punch_need_remark` | `boolean` | 外勤打卡需填写备注（需要允许外勤打卡才能设置生效） |
| &nbsp;&nbsp;└ `out_punch_need_photo` | `boolean` | 外勤打卡需拍照（需要允许外勤打卡才能设置生效） |
| &nbsp;&nbsp;└ `out_punch_allowed_hide_addr` | `boolean` | 外勤打卡允许员工隐藏详细地址（需要允许外勤打卡才能设置生效） |
| &nbsp;&nbsp;└ `out_punch_allowed_adjust_addr` | `boolean` | 外勤打卡允许微调地址（需要允许外勤打卡才能设置生效） |
| &nbsp;&nbsp;└ `adjust_range` | `int` | 微调范围，默认为 50 米 |
| &nbsp;&nbsp;└ `allow_pc_punch` | `boolean` | 是否允许 PC 端打卡 |
| &nbsp;&nbsp;└ `allow_remedy` | `boolean` | 是否限制补卡 |
| &nbsp;&nbsp;└ `remedy_limit` | `boolean` | 是否限制补卡次数 |
| &nbsp;&nbsp;└ `remedy_limit_count` | `int` | 补卡次数 |
| &nbsp;&nbsp;└ `remedy_date_limit` | `boolean` | 是否限制补卡时间 |
| &nbsp;&nbsp;└ `remedy_date_num` | `int` | 补卡时间，几天内补卡 |
| &nbsp;&nbsp;└ `allow_remedy_type_lack` | `boolean` | 允许缺卡补卡（需要允许补卡才能设置生效） |
| &nbsp;&nbsp;└ `allow_remedy_type_late` | `boolean` | 允许迟到补卡（需要允许补卡才能设置生效） |
| &nbsp;&nbsp;└ `allow_remedy_type_early` | `boolean` | 允许早退补卡（需要允许补卡才能设置生效） |
| &nbsp;&nbsp;└ `allow_remedy_type_normal` | `boolean` | 允许正常补卡（需要允许补卡才能设置生效） |
| &nbsp;&nbsp;└ `show_cumulative_time` | `boolean` | 是否展示累计时长 |
| &nbsp;&nbsp;└ `show_over_time` | `boolean` | 是否展示加班时长 |
| &nbsp;&nbsp;└ `hide_staff_punch_time` | `boolean` | 是否隐藏员工打卡详情 |
| &nbsp;&nbsp;└ `hide_clock_in_rule` | `boolean` | 是否隐藏打卡规则 |
| &nbsp;&nbsp;└ `face_punch` | `boolean` | 是否开启人脸识别打卡 |
| &nbsp;&nbsp;└ `face_punch_cfg` | `int` | 人脸识别打卡规则<br>**可选值有：** * 1：每次打卡均需人脸识别 * 2：疑似作弊打卡时需要人脸识别 |
| &nbsp;&nbsp;└ `face_live_need_action` | `boolean` | 人脸打卡规则。<br>**可选值有：** * false：开启活体验证  * true：动作验证，仅在 face_punch_cfg = 1 时有效 |
| &nbsp;&nbsp;└ `face_downgrade` | `boolean` | 人脸识别失败时是否允许普通拍照打卡 |
| &nbsp;&nbsp;└ `replace_basic_pic` | `boolean` | 人脸识别失败时是否允许替换基准图片 |
| &nbsp;&nbsp;└ `anti_cheat_punch_config` | `anti_cheat_config` | 防作弊打卡配置（仅灰度租户有效） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `intercept_suspected_cheat_punch` | `boolean` | 是否拦截疑似作弊打卡总开关；关闭时，其余防作弊开关都为关闭状态 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `check_cheat_software_punch` | `boolean` | 是否校验疑似作弊软件打卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `check_buddy_punch` | `boolean` | 是否校验疑似他人代打卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `check_simulate_wifi_punch` | `boolean` | 是否校验疑似模拟 WI-FI 打卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `check_change_device_punch` | `boolean` | 是否校验更换设备打卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allow_change_device_num` | `int` | 同一考勤人员最多可绑定打卡设备数量上限 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `suspected_cheat_handle_method` | `int` | 疑似作弊打卡时的处理方式，开启拦截疑似作弊打卡时必填<br>**可选值有**：<br>- `1`: 使用人脸识别打卡 - `2`: 仅记录疑似作弊信息 |
| &nbsp;&nbsp;└ `machines` | `machine\[\]` | 考勤机列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `machine_sn` | `string` | 考勤机序列号 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `machine_name` | `string` | 考勤机名称 |
| &nbsp;&nbsp;└ `gps_range` | `int` | GPS 打卡的有效范围（不建议使用） |
| &nbsp;&nbsp;└ `locations` | `location\[\]` | 地址列表（仅追加，不会覆盖之前的列表） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `location_id` | `string` | 地址 ID，系统ID只透传，暂时无用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `location_name` | `string` | 地址名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `location_type` | `int` | 地址类型<br>**可选值有：** * 1：GPS * 2：Wi-Fi * 8：IP |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `latitude` | `number(float)` | 地址纬度 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `longitude` | `number(float)` | 地址经度 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ssid` | `string` | Wi-Fi 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bssid` | `string` | Wi-Fi 的 MAC 地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `map_type` | `int` | 地图类型，1：高德， 2：谷歌 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `string` | 地址名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ip` | `string` | IP 地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `feature` | `string` | 额外信息，例如：运营商信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `gps_range` | `int` | GPS 打卡的有效范围 |
| &nbsp;&nbsp;└ `group_type` | `int` | 考勤类型，0：固定班制，2：排班制， 3：自由班制 |
| &nbsp;&nbsp;└ `punch_day_shift_ids` | `string\[\]` | 班次 ID 列表。仅当考勤类型为固定班制时，该参数有值。 |
| &nbsp;&nbsp;└ `free_punch_cfg` | `free_punch_cfg` | 配置自由班制 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `free_start_time` | `string` | 自由班制打卡开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `free_end_time` | `string` | 自由班制打卡结束时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `punch_day` | `int` | 打卡的时间，为 7 位数字，每一位依次代表周一到周日，0 为不上班，1 为上班。例如示例值1111100，代表从周一到周五上班，周六周日休息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_day_no_punch_as_lack` | `boolean` | 工作日不打卡是否记为缺卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_hours_demand` | `boolean` | 工作日出勤是否需满足时长要求 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_hours` | `int` | 每日工作时长（分钟),范围[0,1440] |
| &nbsp;&nbsp;└ `calendar_id` | `int` | 国家日历  ID，0：不根据国家日历排休，1：中国大陆，2：美国，3：日本，4：印度，5：新加坡，默认 1 |
| &nbsp;&nbsp;└ `need_punch_special_days` | `punch_special_date_shift\[\]` | 必须打卡的特殊日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `punch_day` | `int` | 打卡日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `shift_id` | `string` | 班次 ID，可使用此id查询[班次详情](https://open.larkoffice.com/document/server-docs/attendance-v1/shift/get) |
| &nbsp;&nbsp;└ `no_need_punch_special_days` | `punch_special_date_shift\[\]` | 无需打卡的特殊日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `punch_day` | `int` | 打卡日期 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `shift_id` | `string` | 班次 ID |
| &nbsp;&nbsp;└ `work_day_no_punch_as_lack` | `boolean` | 自由班制下工作日不打卡是否记为缺卡 |
| &nbsp;&nbsp;└ `remedy_period_type` | `int` | 补卡周期类型。1为按自然月，2为自定义周期 * 1：MONTH * 2：CUSTOM |
| &nbsp;&nbsp;└ `remedy_period_custom_date` | `int` | 补卡自定义周期起始日期 |
| &nbsp;&nbsp;└ `punch_type` | `int` | 打卡类型，位运算。1：GPS 打卡，2：Wi-Fi 打卡，4：考勤机打卡，8：IP 打卡 |
| &nbsp;&nbsp;└ `effect_time` | `string` | 生效时间，精确到秒的时间戳 |
| &nbsp;&nbsp;└ `fixshift_effect_time` | `string` | 固定班次生效时间，精确到秒的时间戳 |
| &nbsp;&nbsp;└ `member_effect_time` | `string` | 参加考勤的人员、部门变动生效时间，精确到秒的时间戳 |
| &nbsp;&nbsp;└ `rest_clockIn_need_approval` | `boolean` | 休息日打卡需审批 |
| &nbsp;&nbsp;└ `clockIn_need_photo` | `boolean` | 每次打卡均需拍照 |
| &nbsp;&nbsp;└ `member_status_change` | `member_status_change` | 人员异动打卡设置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_on_no_need_punch` | `boolean` | 是否入职日上班无需打卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `onboarding_off_no_need_punch` | `boolean` | 是否入职日下班无需打卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `offboarding_on_no_need_punch` | `boolean` | 是否离职日上班无需打卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `offboarding_off_no_need_punch` | `boolean` | 是否离职日下班无需打卡 |
| &nbsp;&nbsp;└ `leave_need_punch` | `boolean` | 请假离岗或返岗是否需打卡 |
| &nbsp;&nbsp;└ `leave_need_punch_cfg` | `leave_need_punch_cfg` | 请假离岗或返岗打卡规则，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_late` | `int` | 晚到超过多久记为迟到，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_lack` | `int` | 晚到超过多久记为缺卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `early_minutes_as_early` | `int` | 早走超过多久记为早退，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `early_minutes_as_lack` | `int` | 早走超过多久记为缺卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `not_during_shift` | `boolean` | 班次中间请假，无需在离岗前或返岗后打卡（仅灰度租户有效，如需使用请联系技术支持） |
| &nbsp;&nbsp;└ `go_out_need_punch` | `int` | 外出期间是否需打卡 |
| &nbsp;&nbsp;└ `go_out_need_punch_cfg` | `leave_need_punch_cfg` | 外出期间打卡规则，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_late` | `int` | 晚到超过多久记为迟到，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_lack` | `int` | 晚到超过多久记为缺卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `early_minutes_as_early` | `int` | 早走超过多久记为早退，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `early_minutes_as_lack` | `int` | 早走超过多久记为缺卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `not_during_shift` | `boolean` | 班次中间外出，无需在离岗前或返岗后打卡（仅灰度租户有效，如需使用请联系技术支持） |
| &nbsp;&nbsp;└ `travel_need_punch` | `int` | 出差期间是否需打卡 |
| &nbsp;&nbsp;└ `travel_need_punch_cfg` | `leave_need_punch_cfg` | 出差期间打卡规则，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_late` | `int` | 晚到超过多久记为迟到，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_lack` | `int` | 晚到超过多久记为缺卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `early_minutes_as_early` | `int` | 早走超过多久记为早退，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `early_minutes_as_lack` | `int` | 早走超过多久记为缺卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `not_during_shift` | `boolean` | 无需在出差离岗前或返岗后打卡（出差不生效） |
| &nbsp;&nbsp;└ `need_punch_members` | `punch_member\[\]` | 需要打卡的人员集合（当「bind_dept_ids」和「bind_user_ids」不为空时，以「bind_dept_ids」和「bind_user_ids」为准） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rule_scope_type` | `int` | 圈人方式<br>**可选值有：** * 0 无  * 1 全部  * 2 自定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scope_group_list` | `scope_group` | 圈人规则列表，返回的规则之间为且关系，或关系的规则暂不支持返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `scope_value_type` | `int` | **类型**： * 1: 部门 * 2:人员 * 3: 国家地区 * 4: 员工类型 * 5: 工作城市 * 6: 职级 * 7: 序列 * 8: 职务（企业版） * 9: 工时制度（企业版） * 100: 自定义字段（企业版） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operation_type` | `int` | 范围类型（是否包含） * 1: 包含 * 2: 不包含 * 3: 相等 * 4: 小于等于 * 5: 大于等于 * 6: 大于 * 7: 小于 * 8: 不相等 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `right` | `scope_value\[\]` | 如果是人员/部门类型 不需要使用该字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 标识Key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `member_ids` | `string\[\]` | 部门/人员id列表（具体类型根据scope_value_type判断） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_field_ID` | `string` | 企业版自定义字段唯一键 ID, 需要从飞书人事获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_field_obj_type` | `string` | 企业版自定义字段对象类型 * "Employment": 主数据对象，员工雇佣信息  * "Person": 主数据对象，个人 |
| &nbsp;&nbsp;└ `no_need_punch_members` | `punch_member\[\]` | 无需打卡的人员集合（当「bind_default_dept_ids」和「bind_default_user_ids」不为空时，以「bind_default_dept_ids」和「bind_default_user_ids」为准） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rule_scope_type` | `int` | 圈人方式<br>**可选值有：** * 0 无  * 1 全部  * 2 自定义 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `scope_group_list` | `scope_group` | 圈人规则列表，返回的规则之间为且关系，或关系的规则暂不支持返回 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `scope_value_type` | `int` | **类型**： * 1: 部门 * 2:人员 * 3: 国家地区 * 4: 员工类型 * 5: 工作城市 * 6: 职级 * 7: 序列 * 8: 职务（企业版） * 9: 工时制度（企业版） * 100: 自定义字段（企业版） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `operation_type` | `int` | 范围类型（是否包含） * 1: 包含 * 2: 不包含 * 3: 相等 * 4: 小于等于 * 5: 大于等于 * 6: 大于 * 7: 小于 * 8: 不相等 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `right` | `scope_value\[\]` | 如果是人员/部门类型 不需要使用该字段 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 标识Key |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `member_ids` | `string\[\]` | 部门/人员id列表（具体类型根据scope_value_type判断） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_field_ID` | `string` | 企业版自定义字段唯一键 ID, 需要从飞书人事获取 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `custom_field_obj_type` | `string` | 企业版自定义字段对象类型 * "Employment": 主数据对象，员工雇佣信息  * "Person": 主数据对象，个人 |
| &nbsp;&nbsp;└ `save_auto_changes` | `boolean` | 是否允许保存有冲突人员的考勤组。如果 true，则冲突人员将被自动拉入到当前设置的考勤组中，并从原考勤组中移除；如果 false，则需手动调整冲突人员 |
| &nbsp;&nbsp;└ `org_change_auto_adjust` | `boolean` | 当有新员工入职或人员异动，符合条件的人员是否自动加入考勤组 |
| &nbsp;&nbsp;└ `bind_default_dept_ids` | `string\[\]` | 参与无需打卡的部门 ID 列表（与「no_need_punch_members」同时使用时，以当前字段为准）。对应dept_type |
| &nbsp;&nbsp;└ `bind_default_user_ids` | `string\[\]` | 参与无需打卡的人员 ID 列表（与「no_need_punch_members」同时使用时，以当前字段为准）。对应employee_type |
| &nbsp;&nbsp;└ `overtime_clock_cfg` | `overtime_clock_cfg` | 加班打卡规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `allow_punch_approval` | `boolean` | 是否允许在非打卡时段申请打卡（仅灰度租户可用） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `need_clock_over_time_start_and_end` | `boolean` | 加班开始和结束需打卡(需灰度) |
| &nbsp;&nbsp;└ `new_calendar_id` | `string` | 节假日id，（如果考勤组使用了自定义节假日，请用此参数传入节假日id） |
| &nbsp;&nbsp;└ `allow_apply_punch` | `boolean` | 定位不准时是否允许申请打卡 |
| &nbsp;&nbsp;└ `clock_in_abnormal_settings` | `ClockInAbnormalSettings` | 异常卡豁免配置 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ignore_until_latest_clockout` | `boolean` | 在最晚下班打卡之前忽略异常卡（仅灰度租户有效） |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "group_id": "6919358128597097404",
        "group_name": "开心考勤",
        "time_zone": "Asia/Shanghai",
        "bind_dept_ids": [
            "od-fcb45c28a45311afd440b7869541fce8"
        ],
        "except_dept_ids": [
            "od-fcb45c28a45311afd440b7869541fce8"
        ],
        "bind_user_ids": [
            "52aa1fa1"
        ],
        "except_user_ids": [
            "4fasdtc2"
        ],
        "group_leader_ids": [
            "52aa1fa1"
        ],
        "sub_group_leader_ids": [
            "4fasdtc2"
        ],
        "allow_out_punch": true,
        "out_punch_need_approval": true,
        "out_punch_need_post_approval": true,
        "out_punch_need_remark": true,
        "out_punch_need_photo": true,
        "out_punch_allowed_hide_addr": true,
        "out_punch_allowed_adjust_addr": true,
        "adjust_range": 50,
        "allow_pc_punch": true,
        "allow_remedy": true,
        "remedy_limit": true,
        "remedy_limit_count": 3,
        "remedy_date_limit": true,
        "remedy_date_num": 3,
        "allow_remedy_type_lack": true,
        "allow_remedy_type_late": true,
        "allow_remedy_type_early": true,
        "allow_remedy_type_normal": true,
        "show_cumulative_time": true,
        "show_over_time": true,
        "hide_staff_punch_time": true,
        "hide_clock_in_rule": false,
        "face_punch": true,
        "face_punch_cfg": 1,
        "face_live_need_action": false,
        "face_downgrade": true,
        "replace_basic_pic": true,
        "anti_cheat_punch_config": {
            "intercept_suspected_cheat_punch": true,
            "check_cheat_software_punch": true,
            "check_buddy_punch": true,
            "check_simulate_wifi_punch": true,
            "check_change_device_punch": true,
            "allow_change_device_num": 1,
            "suspected_cheat_handle_method": 1
        },
        "machines": [
            {
                "machine_sn": "FS0701",
                "machine_name": "创实 9 楼"
            }
        ],
        "gps_range": 300,
        "locations": [
            {
                "location_id": "6921213751454744578",
                "location_name": "浙江省杭州市余杭区五常街道木桥头西溪八方城",
                "location_type": 1,
                "latitude": 30.28994,
                "longitude": 120.04509,
                "ssid": "TP-Link-af12ca",
                "bssid": "08:00:20:0A:8C:6D",
                "map_type": 1,
                "address": "北京市海淀区中航广场",
                "ip": "122.224.123.146",
                "feature": "中国电信",
                "gps_range": 300
            }
        ],
        "group_type": 0,
        "punch_day_shift_ids": [
            "xxx"
        ],
        "free_punch_cfg": {
            "free_start_time": "7:00",
            "free_end_time": "18:00",
            "punch_day": 1111100,
            "work_day_no_punch_as_lack": true,
            "work_hours_demand": false,
            "work_hours": 480
        },
        "calendar_id": 1,
        "need_punch_special_days": [
            {
                "punch_day": 20190101,
                "shift_id": "6919668827865513935"
            }
        ],
        "no_need_punch_special_days": [
            {
                "punch_day": 20190101,
                "shift_id": "6919668827865513935"
            }
        ],
        "work_day_no_punch_as_lack": true,
        "remedy_period_type": 1,
        "remedy_period_custom_date": 1,
        "punch_type": 1,
        "effect_time": "1611476284",
        "fixshift_effect_time": "1611476284",
        "member_effect_time": "1611476284",
        "rest_clockIn_need_approval": true,
        "clockIn_need_photo": true,
        "member_status_change": {
            "onboarding_on_no_need_punch": false,
            "onboarding_off_no_need_punch": false,
            "offboarding_on_no_need_punch": false,
            "offboarding_off_no_need_punch": false
        },
        "leave_need_punch": false,
        "leave_need_punch_cfg": {
            "late_minutes_as_late": 0,
            "late_minutes_as_lack": 0,
            "early_minutes_as_early": 0,
            "early_minutes_as_lack": 0,
            "not_during_shift": false
        },
        "go_out_need_punch": 0,
        "go_out_need_punch_cfg": {
            "late_minutes_as_late": 0,
            "late_minutes_as_lack": 0,
            "early_minutes_as_early": 0,
            "early_minutes_as_lack": 0,
            "not_during_shift": false
        },
        "travel_need_punch": 0,
        "travel_need_punch_cfg": {
            "late_minutes_as_late": 0,
            "late_minutes_as_lack": 0,
            "early_minutes_as_early": 0,
            "early_minutes_as_lack": 0,
            "not_during_shift": false
        },
        "need_punch_members": [
            {
                "rule_scope_type": 0,
                "scope_group_list": {
                    "scope_value_type": 1,
                    "operation_type": 1,
                    "right": [
                        {
                            "key": "CH",
                            "name": "中国大陆"
                        }
                    ],
                    "member_ids": [
                        "ec8ddg56"
                    ],
                    "custom_field_ID": "123213123",
                    "custom_field_obj_type": "employment"
                }
            }
        ],
        "no_need_punch_members": [
            {
                "rule_scope_type": 0,
                "scope_group_list": {
                    "scope_value_type": 1,
                    "operation_type": 1,
                    "right": [
                        {
                            "key": "CH",
                            "name": "中国大陆"
                        }
                    ],
                    "member_ids": [
                        "ec8ddg56"
                    ],
                    "custom_field_ID": "123213123",
                    "custom_field_obj_type": "employment"
                }
            }
        ],
        "save_auto_changes": false,
        "org_change_auto_adjust": false,
        "bind_default_dept_ids": [
            "od-fcb45c28a45311afd440b7869541fce8"
        ],
        "bind_default_user_ids": [
            "dd31248a"
        ],
        "overtime_clock_cfg": {
            "allow_punch_approval": false,
            "need_clock_over_time_start_and_end": false
        },
        "new_calendar_id": "通过查询考勤组接口获取的new_calendar_id，例如7302191700771358252",
        "allow_apply_punch": true,
        "clock_in_abnormal_settings": {
            "ignore_until_latest_clockout": false
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1220001 | param is invalis | 入参校验失败，请根据具体返回的信息检查入参。例如“employee_type invalid”代表人员类型异常。如仍无法解决可联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1220002 | tenant_id is empty | 请检查入参中的 tenant_access_token是否正确 |
| 400 | 1220003 | user_id type is not employee_id or employee_no | employee_type只支持取值为 employee_id或者employee_no |
| 500 | 1225000 | param is invalis | 请参考实际返回的错误信息排查问题。例如“internal server error”代表内部服务异常。如仍无法解决可联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1227000 | 历史错误码，不再使用 | - |
| 400 | 1220600 | 通用错误信息 | 通用错误信息包含多条，详细的错误信息以及处理建议可参见 [错误信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/attendance-development-guidelines) |


