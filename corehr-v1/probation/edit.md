---
title: "编辑试用期"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/probation/edit"
updateTime: "1773228463000"
---

# 编辑试用期

通过本接口可新增、编辑、删除员工试用期信息


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/corehr/v2/probation/edit |
| HTTP Method | POST |
| 接口频率限制 | [100 次/分钟](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `corehr:probation:write` 读写试用期信息 |
| 字段权限要求 | &gt; **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id_type` | `string` | 否 | 用户 ID 类型<br>**示例值**：open_id<br>**可选值有**：<br>- `open_id`: 标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid) - `union_id`: 标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) - `user_id`: 标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id) - `people_corehr_id`: 以飞书人事的 ID 来识别用户<br>**默认值**：`open_id`<br>**当值为 `user_id`，字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `employment_id` | `string` | 是 | 试用期人员的雇佣 ID，类型与查询参数 user_id_type取值一致：<br>1、当user_id_type取值为open_id时，ID获取方式参考[如何获取自己的Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)。<br>2、当user_id_type取值为user_id时，ID获取方式参考[如何获取自己的 User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)。<br>3、当user_id_type取值为union_id时，ID获取方式参考[如何获取自己的 Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)。<br>4、当user_id_type取值为people_corehr_id时，先参考[如何获取自己的 User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)获取User ID。然后通过[ID 转换](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/common_data-id/convert)获取雇佣ID。<br>**示例值**："7140964208476371111" |
| `probation_start_date` | `string` | 否 | 试用期开始日期，格式："YYYY-MM-DD"，填写时满足以下规则 - 权限要求：`corehr:probation.probation_start_date:write` 读写试用期开始日期信息 - 「试用期开始日期」和「试用期预计结束日期」需要一同填写。  - 若该员工存在试用期记录，且同时填写「试用期开始日期」和「试用期预计结束日期」为空串，则删除该试用期记录。  - 若该员工不存在试用期记录，且填写「试用期开始日期」和「试用期预计结束日期」，则新增试用期记录。  - 若该员工不存在试用期记录，且未填写「试用期开始日期」和「试用期预计结束日期」，则试用期记录不会创建，其他写入数据不会生效。  - 入职日期 &lt;= 试用期开始日期 &lt;= 试用期预计结束日期。<br>**示例值**："2024-01-01" |
| `probation_expected_end_date` | `string` | 否 | 试用期预计结束日期，格式："YYYY-MM-DD"，填写时满足以下规则  - 权限要求：`corehr:probation.probation_expected_end_date:write` 读写试用期预计结束日期信息 - 「试用期开始日期」和「试用期预计结束日期」需要一同填写。  - 若该员工存在试用期记录，且同时填写「试用期开始日期」和「试用期预计结束日期」为空串，则删除该试用期记录。  - 若该员工不存在试用期记录，且填写「试用期开始日期」和「试用期预计结束日期」，则新增试用期记录。  - 若该员工不存在试用期记录，且未填写「试用期开始日期」和「试用期预计结束日期」，则试用期记录不会创建，其他写入数据不会生效。  - 试用期开始日期 &lt;= 试用期预计结束日期<br>**示例值**："2025-01-01" |
| `probation_outcome` | `string` | 否 | 试用期结果，填写时满足以下规则  - 权限要求：`corehr:probation.probation_outcome:write` 写试用期结果字段 - 取值区分大小写。 - 填写「通过」时，必填「试用期实际结束日期」。 - 填写「延长」时，「延长后试用期预计结束日期」和「试用期预计延长时长」至少填写一项。 - 填写「未通过」时，需要置空「试用期实际结束日期」。<br>**示例值**："passed"<br>**可选值有**：<br>- `passed`: 通过 - `failed`: 未通过 - `delayed`: 延期 |
| `actual_probation_end_date` | `string` | 否 | 试用期实际结束日期，格式："YYYY-MM-DD"，填写时满足以下规则 - 权限要求：`corehr:probation.actual_probation_end_date:write` 读写试用期实际结束日期信息 - 需同时指定试用期结果为「通过」。 - 试用期开始时间 &lt;= 试用期实际结束日期 &lt;= 试用期预计结束日期。<br>**示例值**："2025-01-01" |
| `probation_extend_expected_end_date` | `string` | 否 | 延长后试用期预计结束日期，格式："YYYY-MM-DD"，填写时满足以下规则 - 权限要求：`corehr:probation.probation_extend_expected_end_date:write` 读写延长后试用期预计结束日期信息 - 需同时指定「试用期结果」为「延期」。 - 若同时填写「试用期预计延长时长」，需保持两者数据一致。 - 延长后试用期预计结束日期 &gt; 试用期预计结束日期。<br>**示例值**："2025-01-01" |
| `extended_probation_period_duration` | `int` | 否 | 试用期预计延长时长，填写时满足以下规则 - 权限要求：`corehr:probation.extended_probation_period_duration:write` 读写试用期预计延长时长信息 - 需同时指定「试用期结果」为「延期」。 - 填写时需要指定「试用期延长时长单位」。 - 若同时填写「延长后试用期预计结束日期」，需保持两者数据一致。 - 试用期预计延长时长 &gt; 0。<br>**示例值**：1<br>**数据校验规则**：<br>- 取值范围：`1` ～ `500` |
| `extended_probation_period_unit` | `string` | 否 | 试用期延长时长单位，填写时满足以下规则 - 权限要求：`corehr:probation.extended_probation_period_duration:write` 读写试用期预计延长时长信息 - 取值区分大小写。 - 需要和「试用期预计延长时长」一同填写。 - 需同时指定「试用期结果」为「延期」。<br>**示例值**："day"<br>**可选值有**：<br>- `day`: 天 - `week`: 周 - `month`: 月 |
| `notes` | `string` | 否 | 备注 - 权限要求：`corehr:probation.notes:write` 读写试用期备注信息<br>**示例值**："试用期表现良好。" |
| `self_review` | `string` | 否 | 员工自评 - 权限要求：`corehr:probation.self_review:write` 读写员工自评信息<br>**示例值**："试用期表现良好。" |
| `custom_fields` | `custom_field_data\[\]` | 否 | 自定义字段（当前不支持附件类型字段写入） - 权限要求：`corehr:probation.custom_field:write` 读写试用期自定义字段信息 - 可填写的字段范围参考[人员档案配置](https://people.feishu.cn/people/hr-settings/profile) &gt; 信息配置 &gt; 试用期 中的自定义字段<br>**数据校验规则**：<br>- 长度范围：`0` ～ `1000` |
| &nbsp;&nbsp;└ `custom_api_name` | `string` | 是 | 自定义字段 apiname，即自定义字段的唯一标识<br>**示例值**："name" |
| &nbsp;&nbsp;└ `name` | `custom_name` | 否 | 自定义字段名称（无需填写） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 否 | 中文<br>**示例值**："自定义姓名" |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 否 | 英文<br>**示例值**："Custom Name" |
| &nbsp;&nbsp;└ `type` | `int` | 否 | 自定义字段类型（无需填写）<br>**示例值**：1 |
| &nbsp;&nbsp;└ `value` | `string` | 是 | 字段值，是 json 转义后的字符串，根据元数据定义不同，字段格式不同，不同类型字段传值格式如下 - 文本，示例："你好" - 超链接，示例："https://www.baidu.com/" - 数字，示例："123" - 布尔，示例："true" - 单选，示例："option1" - 多选，示例："[\"option1\", \"option2\"]" - 人员（单选），示例："7140964208476371111" - 人员（多选），示例："[\"7140964208476371111\", \"7140964208476371112\"]" - 日期，示例："2025-01-01"<br>**示例值**："231" |


### 请求体示例

```json
{
    "employment_id": "7140964208476371111",
    "probation_start_date": "2024-01-01",
    "probation_expected_end_date": "2025-01-01",
    "probation_outcome": "passed",
    "actual_probation_end_date": "2025-01-01",
    "probation_extend_expected_end_date": "2025-01-01",
    "extended_probation_period_duration": 1,
    "extended_probation_period_unit": "day",
    "notes": "试用期表现良好。",
    "self_review": "试用期表现良好。",
    "custom_fields": [
        {
            "custom_api_name": "name",
            "name": {
                "zh_cn": "自定义姓名",
                "en_us": "Custom Name"
            },
            "type": 1,
            "value": "231"
        }
    ]
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
| 400 | 1160403 | You don't have the permission to view this page or perform this operation | 请申请对该员工的数据访问权限 |
| 400 | 1161002 | \"Probation end date\" can't be later than \"Estimated probation end date\" | 「试用期实际结束日期」不能晚于「试用期预计结束日期」 |
| 400 | 1161013 | Please fill in both \"Probation start date\" and \"Estimated probation end date\" | 请同时填写「试用期开始日期」和「试用期预计结束日期」 |
| 400 | 1161015 | \"Probation end date\" can't be earlier than \"Probation start date\" | 「试用期实际结束日期」不能早于「试用期开始日期」 |
| 400 | 1161017 | \"Probation start date\" can't be earlier than \"Onboarding date\" | 「试用期开始日期」不能早于「入职日期」 |
| 400 | 1161018 | \"Estimated probation end date\" can't be earlier than \"Probation start date\" | 「试用期预计结束日期」不能早于「试用期开始日期」 |
| 400 | 1161021 | Probation record pending approval can't be edited | 无法编辑审批中的试用期记录 |
| 400 | 1161034 | \"Probation extension duration\" can't be less than or equal to 0 | 「试用期延长时长」不可小于等于0 |
| 400 | 1161035 | \"Expected end date after probation extension\" can't be earlier than or equal to \"Expected probation end date\" | 「延长后试用期预计结束日期」不能早于等于「试用期预计结束日期」 |
| 400 | 1161037 | \"Probation extension duration\" and \"Extended probation end date\" don't match | 「试用期延长时长」和「延长后试用期预计结束日期」不匹配 |
| 400 | 1161038 | Please fill in both \"Probation extension duration\" and \"Unit of probation extension duration\" | 请同时填写「试用期延长时长」和「试用期延长时长单位」 |
| 400 | 1161039 | If the \"Probation result\" is extend probation, \"Extended probation end date\" or \"Probation extension duration and its unit\" must be filled in | 「试用期结果」为延长试用期，「延长后试用期预计结束日期」或「试用期延长时长及其单位」必填 |
| 400 | 1161041 | If the \"Probation result\" is pass, \"Actual probation end date\" must be filled in | 「试用期结果」为通过，「试用期实际结束日期」必填 |
| 400 | 1161046 | There is an actual probation end date. Please set the probation result to \"Passed\" | 存在试用期实际结束日期，请将试用期结果指定为「通过」 |
| 400 | 1161047 | Probation extension fields are filled. Please set the probation result to \"Extended\" | 已填写试用期延长相关信息，请将试用期结果指定为「延长」 |


