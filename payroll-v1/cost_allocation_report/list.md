---
title: "查询成本分摊报表汇总数据"
fullPath: "/uAjLw4CM/ukTMukTMukTM/payroll-v1/cost_allocation_report/list"
updateTime: "1765505834000"
---

# 查询成本分摊报表汇总数据

根据算薪期间和成本分摊方案id获取成本分摊汇总数据。调用接口前，需在payroll 系统中打开「财务过账」开关，并且完成发布成本分摊报表。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/payroll/v1/cost_allocation_reports |
| HTTP Method | GET |
| 接口频率限制 | [5 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `payroll:cost_allocation_report:read` 获取成本分摊报表汇总数据 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 查询参数

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_size` | `int` | 是 | 分页大小<br>**示例值**：50<br>**数据校验规则**：<br>- 取值范围：`1` ～ `100` |
| `page_token` | `string` | 否 | 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果<br>**示例值**：6823630319749592415 |
| `cost_allocation_plan_id` | `string` | 是 | 成本分摊方案ID，通过[批量查询成本分摊方案](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/payroll-v1/cost_allocation_plan/list)获取<br>**示例值**：6823630319749580304 |
| `pay_period` | `string` | 是 | 期间，成本分摊数据对应的年月，格式 为yyyy-MM<br>**示例值**：2023-11 |
| `report_type` | `int` | 是 | 报表类型<br>**示例值**：1<br>**可选值有**：<br>- `0`: 默认，表示没有开通计提和实发功能时的报表类型，开通计提和实发之后，该类型报表将无法发布。 - `1`: 计提 - `2`: 实发 |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `pay_period` | `string` | 期间，成本分摊报表对应的年月 |
| &nbsp;&nbsp;└ `page_token` | `string` | 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token |
| &nbsp;&nbsp;└ `has_more` | `boolean` | 是否还有更多项 |
| &nbsp;&nbsp;└ `cost_allocation_report_names` | `i18n_content\[\]` | 报表名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;└ `cost_allocation_report_datas` | `cost_allocation_report_data\[\]` | 汇总数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `data_summary_dimensions` | `data_summary_dimension\[\]` | 数据维度汇总 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_level` | `int` | 层级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_type` | `int` | 类型：<br>公司主体 - 1<br>成本中心 - 2<br>部门 - 3<br>薪资组 - 4<br>人员类型 - 5<br>雇佣状态 - 6<br>转正状态 - 7<br>职务 - 8<br>序列 - 9<br>职级 - 10<br>工时制度 - 11<br>合同类型 - 12<br>算薪项 - 13<br>自定义维度 - 100 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_value_id` | `string` | 维度ID，需要根据dimension_type再次转换，如：当dimension_type为1时，该值表示公司主体的ID。<br>对应的接口映射如下：<br>dimension_type = 1 [公司主体](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)<br>dimension_type = 2 [成本中心](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)<br>dimension_type = 3 [部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)<br>dimension_type = 4 [薪资组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/payroll-v1/paygroup/list)<br>dimension_type = 5 [人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)<br>dimension_type = 8 [职务](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)<br>dimension_type = 9 [序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)<br>dimension_type = 10 [职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)<br>dimension_type = 11 [工时制度](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_dimension` | `enum_object` | 算薪项汇总维度时，当算薪项是特定枚举值，会使用该字段返回枚举值ID以及枚举值Key，业务需要获取枚举对象的详情信息，可根据ID去对应的对象中查找，其中枚举对象的映射如下：<br> workCalendar [工作日历](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave/work_calendar)<br> location [地点](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/location/batch_get)<br>company [公司主体](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)<br>costCenter  [成本中心](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)<br>department [部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)<br>employeeType [人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)<br>job [职务](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)<br>jobFamily [序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)<br>jobLevel [职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)<br>workingHoursType [工时制度](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_value_id` | `string` | 枚举对象ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `enum_key` | `string` | 枚举对象 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_value_lookup_info` | `dimension_value_lookup_info` | 维度引用对象的基础信息，当维度为引用类型字段才会有值，目前支持的引用对象类型见type |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 引用对象类型，类型对应的对象映射包括不仅限：<br>type = company [公司主体](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)<br>type = cost_center [成本中心](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)<br>type = department [部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)<br>type = pay_group [薪资组](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/payroll-v1/paygroup/list)<br>type = employee_type [人员类型](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/employee_type/get)<br>type = job [职务](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)<br>type = job_family [序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)<br>type = job_level [职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)<br>type = working_hours_type [工时制度](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/working_hours_type/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 引用对象的id，可根据相关API查询到对象的完整信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `code` | `string` | 引用对象的code，目前下面的对象会有code：<br>type = company [公司主体](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/company/batch_get)<br>type = cost_center [成本中心](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/cost_center/search)<br>type = department [部门](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/department/get)<br>type = job [职务](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job/get)<br>type = job_family [序列](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_family/batch_get)<br>type = job_level [职级](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/job_level/batch_get)<br>type = location [地点](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/corehr-v2/location/batch_get) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_names` | `i18n_content\[\]` | 维度名称，算薪项、自定义维度使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `dimension_titles` | `i18n_content\[\]` | 数据维度表头，算薪项、自定义维度使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 名称对应的实体id<br>需要根据dimension_type再次转换，如：当dimension_type为13时，该值表示算薪项的ID。<br>对应的接口映射如下：<br>dimension_type = 13 [算薪项](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/payroll-v1/acct_item/list) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_cost_item` | `compensation_cost_item` | 成本项数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `number_of_individuals_for_payment` | `int` | 发薪人数 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_costs` | `compensation_cost\[\]` | 成本项数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `compensation_cost_value` | `string` | 成本项值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `i18n_names` | `i18n_content\[\]` | 成本项名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `locale` | `string` | 语种 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 语种对应的值 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "pay_period": "2023-11",
        "page_token": "6823630319749580302",
        "has_more": true,
        "cost_allocation_report_names": [
            {
                "locale": "zh_cn",
                "value": "名称"
            }
        ],
        "cost_allocation_report_datas": [
            {
                "data_summary_dimensions": [
                    {
                        "dimension_level": 1,
                        "dimension_type": 1,
                        "dimension_value_id": "6823630319749580306",
                        "enum_dimension": {
                            "enum_value_id": "7188920315914207276",
                            "enum_key": "company"
                        },
                        "dimension_value_lookup_info": {
                            "type": "work_calendar",
                            "id": "6961286846093788621",
                            "code": "D1230011115"
                        },
                        "dimension_names": [
                            {
                                "locale": "zh_cn",
                                "value": "名称"
                            }
                        ],
                        "dimension_titles": [
                            {
                                "locale": "zh_cn",
                                "value": "名称",
                                "id": "723123123123123213"
                            }
                        ]
                    }
                ],
                "compensation_cost_item": {
                    "number_of_individuals_for_payment": 100,
                    "compensation_costs": [
                        {
                            "compensation_cost_value": "123456.78",
                            "i18n_names": [
                                {
                                    "locale": "zh_cn",
                                    "value": "名称"
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 2500001 | unknown error | 未知错误，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 400 | 2500002 | param is invalid | 参数错误，请检查参数 |
| 500 | 2500003 | rpc fail | 请求调用出错，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 500 | 2500004 | get plan version fail | 获取成本分摊方案版本出错，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 200 | 2500005 | report has changed, please fetch again | 报表已变更，请重新获取。一般为报表拉取过程中新发布了报表。需要不传page_token参数，重新从头拉取 |
| 200 | 2500006 | report not found or unpublished | 报表不存在或者未发布，请检查参数并且联系报表管理员确认发布报表后再尝试 |
| 500 | 2500007 | report fetch fail | 获取报表数据失败，请联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |


