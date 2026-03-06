---
title: "创建班次"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/shift/create"
updateTime: "1740742982000"
---

# 创建班次

班次是描述一次考勤任务时间规则的统称，比如一天打多少次卡，每次卡的上下班时间，晚到多长时间算迟到，晚到多长时间算缺卡等。在假勤设置-[班次设置](https://example.feishu.cn/people/workforce-management/setting/group/shifts)中点击班次名称可以进行班次详情查看。如果入参中传入了班次id，那么支持编辑班次的能力


> **Tip**: - 创建一个考勤组前，必须先创建一个或者多个班次。
> - 一个公司内的班次是共享的，你可以直接引用他人创建的班次，但是需要注意的是，若他人修改了班次，会影响到你的考勤组及其考勤结果。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/attendance/v1/shifts |
| HTTP Method | POST |
| 接口频率限制 | [50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `attendance:rule` 写入打卡管理规则 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employee_type` | `string` | 否 | 请求体中的 user_ids 和响应体中的 user_id 的员工ID类型。如果没有后台管理权限，可使用[通过手机号或邮箱获取用户 ID](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch_get_id)<br>**示例值**：employee_id<br>**可选值有**：<br>- `employee_id`: 员工 employee ID，即[飞书管理后台](https://example.feishu.cn/admin/contacts/departmentanduser) > 组织架构 > 成员与部门 > 成员详情中的用户 ID，或者[通过手机号或邮箱获取用户 ID](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch_get_id)获取的userid。 - `employee_no`: 员工工号，即[飞书管理后台](https://example.feishu.cn/admin/contacts/departmentanduser) > 组织架构 > 成员与部门 > 成员详情中的工号 |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `shift_name` | `string` | 是 | 班次名称，不可重复<br>**示例值**："早班" |
| `punch_times` | `int` | 是 | 打卡次数（历史字段，已无用，以punch_time_rule为准）<br>**示例值**：1 |
| `sub_shift_leader_ids` | `string\[\]` | 否 | 班次负责人，与employee_type类型对应<br>**示例值**：["456123"] |
| `is_flexible` | `boolean` | 否 | 是否弹性打卡，默认为false，不开启<br>**示例值**：false |
| `flexible_minutes` | `int` | 否 | 弹性打卡时间，单位：分钟，设置【上班最多可晚到】与【下班最多可早走】时间。仅当未设置 flexible_rule 参数时，该参数生效。如果设置了 flexible_rule 参数，则该参数不生效<br>**示例值**：60 |
| `flexible_rule` | `flexible_rule\[\]` | 否 | 弹性打卡时间设置 |
| &nbsp;&nbsp;└ `flexible_early_minutes` | `int` | 是 | 下班最多可早走，单位：分钟（上班早到几分钟，下班可早走几分钟）<br>**示例值**：60 |
| &nbsp;&nbsp;└ `flexible_late_minutes` | `int` | 是 | 上班最多可晚到，单位：分钟（上班晚到几分钟，下班须晚走几分钟）<br>**示例值**：60 |
| `no_need_off` | `boolean` | 否 | true为不需要打下班卡。默认为false，需要下班打卡<br>**示例值**：true |
| `punch_time_rule` | `punch_time_rule\[\]` | 是 | 打卡规则 |
| &nbsp;&nbsp;└ `on_time` | `string` | 是 | 上班时间<br>**示例值**："9:00" |
| &nbsp;&nbsp;└ `off_time` | `string` | 是 | 下班时间。如果下班时间跨天，则需要在 24 小时的基础上累加时间。例如，第二天凌晨 2 点取值为 26:00<br>**示例值**："18:00" |
| &nbsp;&nbsp;└ `late_minutes_as_late` | `int` | 是 | 晚到多久记为迟到。单位：分钟<br>**示例值**：30 |
| &nbsp;&nbsp;└ `late_minutes_as_lack` | `int` | 是 | 晚到多久记为缺卡。单位：分钟<br>**示例值**：60 |
| &nbsp;&nbsp;└ `on_advance_minutes` | `int` | 是 | 最早多久可打上班卡。最大值为 720。单位：分钟<br>**示例值**：60 |
| &nbsp;&nbsp;└ `early_minutes_as_early` | `int` | 是 | 早退多久记为早退。单位：分钟<br>**示例值**：30 |
| &nbsp;&nbsp;└ `early_minutes_as_lack` | `int` | 是 | 早退多久记为缺卡。单位：分钟<br>**示例值**：60 |
| &nbsp;&nbsp;└ `off_delay_minutes` | `int` | 是 | 最晚多久可打下班卡。最大值为 960。单位：分钟<br>**示例值**：60 |
| &nbsp;&nbsp;└ `late_minutes_as_serious_late` | `int` | 否 | 晚到多久记为严重迟到。单位：分钟<br>**示例值**：40 |
| &nbsp;&nbsp;└ `no_need_on` | `boolean` | 否 | true为不需要打上班卡，这里需要特别注意，第一段打卡规则须为false。后续可按需配置<br>**示例值**：true |
| &nbsp;&nbsp;└ `no_need_off` | `boolean` | 否 | true为不需要打下班卡。默认为false，需要下班打卡（优先级高于data.shift.no_need_off）<br>**示例值**：true |
| `late_off_late_on_rule` | `late_off_late_on_rule\[\]` | 否 | 晚走晚到规则（仅飞书人事企业版可用） |
| &nbsp;&nbsp;└ `late_off_minutes` | `int` | 是 | 晚走多久。单位：分钟<br>**示例值**：60 |
| &nbsp;&nbsp;└ `late_on_minutes` | `int` | 是 | 晚到多久。单位：分钟<br>**示例值**：30 |
| `rest_time_rule` | `rest_rule\[\]` | 否 | 休息规则 |
| &nbsp;&nbsp;└ `rest_begin_time` | `string` | 是 | 休息开始<br>**示例值**："13:00" |
| &nbsp;&nbsp;└ `rest_end_time` | `string` | 是 | 休息结束<br>**示例值**："14:00" |
| `overtime_rule` | `overtime_rule\[\]` | 否 | 加班时段（仅飞书人事企业版可用） |
| &nbsp;&nbsp;└ `on_overtime` | `string` | 是 | 开始时间<br>**示例值**："9:00" |
| &nbsp;&nbsp;└ `off_overtime` | `string` | 是 | 结束时间<br>**示例值**："18:00" |
| `day_type` | `int` | 否 | 日期类型，【是否弹性打卡 = ture】时，不可设置为“休息日”  可选值：1：工作日 2：休息日。默认值：1<br>**示例值**：1 |
| `overtime_rest_time_rule` | `rest_rule\[\]` | 否 | 班外休息规则 |
| &nbsp;&nbsp;└ `rest_begin_time` | `string` | 是 | 休息开始<br>**示例值**："13:00" |
| &nbsp;&nbsp;└ `rest_end_time` | `string` | 是 | 休息结束<br>**示例值**："14:00" |
| `late_minutes_as_serious_late` | `int` | 否 | 晚到多久记为严重迟到。单位：分钟（优先级高于data.shift.punch_time_rule.late_minutes_as_serious_late）<br>**示例值**：40 |
| `shift_middle_time_rule` | `shift_middle_time_rule` | 否 | 半天分割规则（仅飞书人事企业版可用） |
| &nbsp;&nbsp;└ `middle_time_type` | `int` | 否 | 半天分割类型<br>**示例值**：0<br>**可选值有**：<br>- `0`: 按全天班次时长（含休息）的中点分割 - `1`: 按全天班次时长（不含休息）的中点分割 - `2`: 按休息时间分割 - `3`: 按固定时间点分割<br>**默认值**：`0` |
| &nbsp;&nbsp;└ `fixed_middle_time` | `string` | 否 | 固定分割时间点（middle_time_type 为 3 时有效）<br>**示例值**："12:00" |
| `shift_attendance_time_config` | `shift_attendance_time_config` | 否 | 应出勤配置（灰度中，暂未开放） |
| &nbsp;&nbsp;└ `attendance_time` | `number(float)` | 否 | 应出勤时长<br>**示例值**：1<br>**默认值**：`1`<br>**数据校验规则**：<br>- 取值范围：`0` ～ `3` |
| &nbsp;&nbsp;└ `on_attendance_time` | `number(float)` | 否 | 上半天应出勤时长<br>**示例值**：1<br>**默认值**：`1`<br>**数据校验规则**：<br>- 取值范围：`0` ～ `3` |
| &nbsp;&nbsp;└ `off_attendance_time` | `number(float)` | 否 | 下半天应出勤时长<br>**示例值**：1<br>**默认值**：`1`<br>**数据校验规则**：<br>- 取值范围：`0` ～ `3` |
| `late_off_late_on_setting` | `late_off_late_on_setting` | 否 | 晚走次日晚到配置规则 |
| &nbsp;&nbsp;└ `late_off_base_on_time_type` | `int` | 否 | 当日晚走时间计算规则<br>**示例值**：0<br>**可选值有**：<br>- `0`: 弹性规则 - `1`: 固定规则<br>**默认值**：`0` |
| &nbsp;&nbsp;└ `late_on_base_on_time_type` | `int` | 否 | 次日晚到时间计算规则<br>**示例值**：0<br>**可选值有**：<br>- `0`: 固定规则 - `1`: 弹性规则<br>**默认值**：`0` |
| `id` | `string` | 否 | 班次id(更新班次时需要传递)，获取方式：1）[按名称查询班次](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/shift/query) 2）[创建班次](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/shift/create)<br>**示例值**："6919358778597097404" |


### 请求体示例

```json
{
    "shift_name": "早班",
    "punch_times": 1,
    "sub_shift_leader_ids": [
        "456123"
    ],
    "is_flexible": false,
    "flexible_minutes": 60,
    "flexible_rule": [
        {
            "flexible_early_minutes": 60,
            "flexible_late_minutes": 60
        }
    ],
    "no_need_off": true,
    "punch_time_rule": [
        {
            "on_time": "9:00",
            "off_time": "18:00",
            "late_minutes_as_late": 30,
            "late_minutes_as_lack": 60,
            "on_advance_minutes": 60,
            "early_minutes_as_early": 30,
            "early_minutes_as_lack": 60,
            "off_delay_minutes": 60,
            "late_minutes_as_serious_late": 40,
            "no_need_on": true,
            "no_need_off": true
        }
    ],
    "late_off_late_on_rule": [
        {
            "late_off_minutes": 60,
            "late_on_minutes": 30
        }
    ],
    "rest_time_rule": [
        {
            "rest_begin_time": "13:00",
            "rest_end_time": "14:00"
        }
    ],
    "overtime_rule": [
        {
            "on_overtime": "9:00",
            "off_overtime": "18:00"
        }
    ],
    "day_type": 1,
    "overtime_rest_time_rule": [
        {
            "rest_begin_time": "13:00",
            "rest_end_time": "14:00"
        }
    ],
    "late_minutes_as_serious_late": 40,
    "shift_middle_time_rule": {
        "middle_time_type": 0,
        "fixed_middle_time": "12:00"
    },
    "shift_attendance_time_config": {
        "attendance_time": 1,
        "on_attendance_time": 1,
        "off_attendance_time": 1
    },
    "late_off_late_on_setting": {
        "late_off_base_on_time_type": 0,
        "late_on_base_on_time_type": 0
    },
    "id": "6919358778597097404"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `shift` | `shift` | 班次 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `shift_id` | `string` | 班次 ID，调用本接口系统自动生成 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `shift_name` | `string` | 班次名称，对应入参的班次名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `punch_times` | `int` | 打卡次数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `sub_shift_leader_ids` | `string\[\]` | 班次负责人，与employee_type类型对应 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `is_flexible` | `boolean` | 是否弹性打卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `flexible_minutes` | `int` | 弹性打卡时间，单位：分钟，设置【上班最多可晚到】与【下班最多可早走】时间，如果不设置flexible_rule则生效 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `flexible_rule` | `flexible_rule\[\]` | 弹性打卡时间设置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `flexible_early_minutes` | `int` | 下班最多可早走，单位：分钟（上班早到几分钟，下班可早走几分钟） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `flexible_late_minutes` | `int` | 上班最多可晚到，单位：分钟（上班晚到几分钟，下班须晚走几分钟） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `no_need_off` | `boolean` | 不需要打下班卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `punch_time_rule` | `punch_time_rule\[\]` | 打卡规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `on_time` | `string` | 上班时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `off_time` | `string` | 下班时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_late` | `int` | 晚到多久记为迟到，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_lack` | `int` | 晚到多久记为缺卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `on_advance_minutes` | `int` | 最早多久可打上班卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `early_minutes_as_early` | `int` | 早退多久记为早退，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `early_minutes_as_lack` | `int` | 早退多久记为缺卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `off_delay_minutes` | `int` | 最晚多久可打下班卡，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_serious_late` | `int` | 晚到多久记为严重迟到。单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `no_need_on` | `boolean` | 是否不需要打上班卡 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `no_need_off` | `boolean` | 是否不需要打下班卡（优先级高于data.shift.no_need_off） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_off_late_on_rule` | `late_off_late_on_rule\[\]` | 晚走晚到规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `late_off_minutes` | `int` | 晚走多久，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `late_on_minutes` | `int` | 晚到多久，单位：分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `rest_time_rule` | `rest_rule\[\]` | 休息规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rest_begin_time` | `string` | 休息开始 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rest_end_time` | `string` | 休息结束 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `overtime_rule` | `overtime_rule\[\]` | 打卡规则（暂不支持） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `on_overtime` | `string` | 上班时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `off_overtime` | `string` | 下班时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `day_type` | `int` | 日期类型，【是否弹性打卡 = ture】时，不可设置为“休息日”  可选值：1：工作日 2：休息日。默认值：1 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `overtime_rest_time_rule` | `rest_rule\[\]` | 班外休息规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rest_begin_time` | `string` | 休息开始 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `rest_end_time` | `string` | 休息结束 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_minutes_as_serious_late` | `int` | 晚到多久记为严重迟到。单位：分钟（优先级高于data.shift.punch_time_rule.late_minutes_as_serious_late） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `shift_middle_time_rule` | `shift_middle_time_rule` | 半天分割规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `middle_time_type` | `int` | 半天分割类型<br>**可选值有**：<br>- `0`: 按全天班次时长（含休息）的中点分割 - `1`: 按全天班次时长（不含休息）的中点分割 - `2`: 按休息时间分割 - `3`: 按固定时间点分割 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `fixed_middle_time` | `string` | 固定分割时间点（middle_time_type 为 3 时有效） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `shift_attendance_time_config` | `shift_attendance_time_config` | 应出勤配置（灰度中，暂未开放） |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `attendance_time` | `number(float)` | 应出勤时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `on_attendance_time` | `number(float)` | 上半天应出勤时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `off_attendance_time` | `number(float)` | 下半天应出勤时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `late_off_late_on_setting` | `late_off_late_on_setting` | 晚走次日晚到配置规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `late_off_base_on_time_type` | `int` | 当日晚走时间计算规则<br>**可选值有**：<br>- `0`: 弹性规则 - `1`: 固定规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `late_on_base_on_time_type` | `int` | 次日晚到时间计算规则<br>**可选值有**：<br>- `0`: 固定规则 - `1`: 弹性规则 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 班次id(更新班次时需要传递) |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "shift": {
            "shift_id": "6919358778597097404",
            "shift_name": "早班",
            "punch_times": 1,
            "sub_shift_leader_ids": [
                "456123"
            ],
            "is_flexible": false,
            "flexible_minutes": 60,
            "flexible_rule": [
                {
                    "flexible_early_minutes": 60,
                    "flexible_late_minutes": 60
                }
            ],
            "no_need_off": true,
            "punch_time_rule": [
                {
                    "on_time": "9:00",
                    "off_time": "18:00， 第二天凌晨2点， 26:00",
                    "late_minutes_as_late": 30,
                    "late_minutes_as_lack": 60,
                    "on_advance_minutes": 60,
                    "early_minutes_as_early": 30,
                    "early_minutes_as_lack": 60,
                    "off_delay_minutes": 60,
                    "late_minutes_as_serious_late": 40,
                    "no_need_on": true,
                    "no_need_off": true
                }
            ],
            "late_off_late_on_rule": [
                {
                    "late_off_minutes": 60,
                    "late_on_minutes": 30
                }
            ],
            "rest_time_rule": [
                {
                    "rest_begin_time": "13:00",
                    "rest_end_time": "14:00"
                }
            ],
            "overtime_rule": [
                {
                    "on_overtime": "9:00",
                    "off_overtime": "18:00"
                }
            ],
            "day_type": 1,
            "overtime_rest_time_rule": [
                {
                    "rest_begin_time": "13:00",
                    "rest_end_time": "14:00"
                }
            ],
            "late_minutes_as_serious_late": 40,
            "shift_middle_time_rule": {
                "middle_time_type": 0,
                "fixed_middle_time": "12:00"
            },
            "shift_attendance_time_config": {
                "attendance_time": 1,
                "on_attendance_time": 1,
                "off_attendance_time": 1
            },
            "late_off_late_on_setting": {
                "late_off_base_on_time_type": 0,
                "late_on_base_on_time_type": 0
            },
            "id": "6919358778597097404"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 1220001 | param is invalis | 入参校验失败，请根据具体返回的信息检查入参。例如“employee_type invalid”代表人员类型异常。如仍无法解决可联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1220002 | tenant_id is empty | 请检查入参中的 tenant_access_token是否正确 |
| 400 | 1220005 | 没有权限 | 请前往[考勤管理后台](https://oa.feishu.cn/attendance/manage/member/list)检查数据权限范围 |
| 500 | 1225000 | param is invalis | 请参考实际返回的错误信息排查问题。例如“internal server error”代表内部服务异常。如仍无法解决可联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 1226000 | param is invalis | 班次服务异常错误码，请参考实际返回的错误信息排查问题。例如“internal server error”代表内部服务异常。如仍无法解决可联系 [技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1226001 | 历史错误码，不再使用 | - |
| 400 | 1226002 | 历史错误码，不再使用 | - |
| 400 | 1220600 | 通用错误信息 | 通用错误信息包含多条，详细的错误信息以及处理建议可参见[错误信息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/attendance-development-guidelines)。 |


