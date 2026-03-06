---
title: "获取招聘官网投递任务结果"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website-delivery_task/get"
updateTime: "1722568752000"
---

# 获取招聘官网投递任务结果

通过[根据简历附件创建招聘官网投递](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website-delivery/create_by_attachment)接口创建的投递任务，可通过本接口获取投递任务结果。如果获取到的数据 data 为空，可继续轮询（正常情况下不会超过1分钟）直到获取到的 data 不为空。


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/hire/v1/websites/:website_id/delivery_tasks/:delivery_task_id |
| HTTP Method | GET |
| 接口频率限制 | [1000 次/分钟、50 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 开启任一权限即可 | `hire:site_application:readonly` 获取官网投递信息 `hire:site_application` 更新官网投递信息 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |


### 路径参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `website_id` | `string` | 官网 ID，可通过[获取招聘官网列表](https://open.larkoffice.com/document/server-docs/hire-v1/get-candidates/website/list)获取<br>**示例值**："7047318856652261676" |
| `delivery_task_id` | `string` | 投递任务 ID，可通过[根据简历附件创建招聘官网投递](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website-delivery/create_by_attachment)获取<br>**示例值**："f1c2a0f138ec492d99d7ab73594158ad" |


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `status` | `int` | 任务状态<br>**可选值有**：<br>- `0`: 新建 - `1`: 处理中 - `2`: 成功 - `3`: 失败 |
| &nbsp;&nbsp;└ `delivery` | `website_delivery_dto` | 官网投递信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `application_id` | `string` | 投递 ID，可通过[获取投递信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | ID，废弃字段，请勿使用 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_id` | `string` | 职位 ID，可通过[获取职位信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `job_post_id` | `string` | 职位广告 ID，可通过[获取招聘官网下职位广告详情](https://open.larkoffice.com/document/server-docs/hire-v1/get-candidates/website/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `portal_resume_id` | `string` | 官网简历 ID，可通过[获取附件信息](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get)获取详细信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 官网用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `talent_id` | `string` | 人才 ID，可通过[获取人才信息](https://open.larkoffice.com/document/server-docs/hire-v1/candidate-management/talent/get-2)获取详细信息 |
| &nbsp;&nbsp;└ `status_msg` | `string` | 状态信息，仅在任务状态（status）为失败（3）时返回 |
| &nbsp;&nbsp;└ `extra_info` | `string` | 附加信息，在任务状态（status）为失败（3）时、且状态信息（status_msg）标识为重复投递时，返回重复投递的 ID |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "status": 1,
        "delivery": {
            "application_id": "6960663240925956657",
            "id": "6960663240925956655",
            "job_id": "6960663240925956659",
            "job_post_id": "6960663240925956658",
            "portal_resume_id": "6960663240925956660",
            "user_id": "6960663240925956656",
            "talent_id": "7095600054216542508"
        },
        "status_msg": " ",
        "extra_info": "  "
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 500 | 1002001 | 系统错误 | 请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。 |
| 400 | 1002002 | 参数错误 | 检查参数是否正确，例如类型，大小 |
| 400 | 1002008 | Task not found or task error | 任务不存在，请检查任务ID是否正确；如果正确，可能是任务已经超时被删除了；如果没创建成功，可重新调用[根据简历附件创建招聘官网投递](https://open.larkoffice.com/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/website-delivery/create_by_attachment)创建投递任务 |


