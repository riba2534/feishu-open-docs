---
title: "创建外部投递"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/external_application/create"
updateTime: "1725853508000"
---

# 创建外部投递

创建外部投递，可用于导入来自其他系统的投递信息。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/external_applications |
| HTTP Method | POST |
| 接口频率限制 | [20 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `hire:external_application` 更新外部投递 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **固定值**："application/json; charset=utf-8" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `external_id` | `string` | 否 | 外部系统投递主键 （仅用于幂等） - 若不传此值，则不进行幂等校验 - 若传此值，则用于幂等校验，同一 `external_id` 24小时内仅可创建一次<br>**示例值**："729557715718" |
| `job_recruitment_type` | `int` | 否 | 职位招聘类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: 社招 - `2`: 校招 |
| `job_title` | `string` | 否 | 职位名称<br>**示例值**："高级 Java" |
| `resume_source` | `string` | 否 | 简历来源<br>**示例值**："内推" |
| `stage` | `string` | 否 | 阶段名称<br>**示例值**："简历初筛" |
| `talent_id` | `string` | 是 | 人才 ID，可通过[获取人才列表](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/list)接口获取<br>**示例值**："6960663240925956459" |
| `termination_reason` | `string` | 否 | 终止原因<br>**示例值**："不合适" |
| `delivery_type` | `int` | 否 | 投递类型<br>**示例值**：1<br>**可选值有**：<br>- `1`: HR 寻访 - `2`: 候选人主动投递 - `3`: 人才推荐 - `4`: 其他 |
| `modify_time` | `int` | 否 | 投递在外部系统终止时间，毫秒时间戳（字段类型为：int64）<br>**示例值**：1618500278645 |
| `create_time` | `int` | 否 | 投递在外部系统创建时间，毫秒时间戳（字段类型为：int64）<br>**示例值**：1618500278644 |
| `termination_type` | `string` | 否 | 终止类型<br>**示例值**："HR 主动终止" |


### 请求体示例

```json
{
    "external_id": "729557715718",
    "job_recruitment_type": 1,
    "job_title": "高级 Java",
    "resume_source": "内推",
    "stage": "简历初筛",
    "talent_id": "6960663240925956459",
    "termination_reason": "不合适",
    "delivery_type": 1,
    "modify_time": 1618500278645,
    "create_time": 1618500278644,
    "termination_type": "HR 主动终止"
}
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `external_application` | `external_application` | 外部投递信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 外部投递 ID（由飞书招聘系统生成） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_recruitment_type` | `int` | 职位招聘类型<br>**可选值有**：<br>- `1`: 社招 - `2`: 校招 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_title` | `string` | 职位名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `resume_source` | `string` | 简历来源 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `stage` | `string` | 阶段名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID，详情请查看：[获取人才信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/get) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `termination_reason` | `string` | 终止原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `delivery_type` | `int` | 投递类型<br>**可选值有**：<br>- `1`: HR 寻访 - `2`: 候选人主动投递 - `3`: 人才推荐 - `4`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `modify_time` | `int` | 投递在外部系统终止时间，毫秒时间戳（字段类型为：int64） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `create_time` | `int` | 投递在外部系统创建时间，毫秒时间戳（字段类型为：int64） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `termination_type` | `string` | 终止类型 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "ok",
    "data": {
        "external_application": {
            "id": "6989202908470446380",
            "job_recruitment_type": 1,
            "job_title": "高级Java",
            "resume_source": "内推",
            "stage": "简历初筛阶段",
            "talent_id": "6960663240925956459",
            "termination_reason": "不合适",
            "delivery_type": 1,
            "modify_time": 1618500278645,
            "create_time": 1618500278644,
            "termination_type": "HR 主动终止"
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统异常 | 请根据实际报错信息定位问题或联系[技术支持](https://applink.feishu.cn/TLJpeNdW) |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 400 | 1002102 | 人才不存在 | 人才不存在，请检查`talent_id`参数的正确性 |


