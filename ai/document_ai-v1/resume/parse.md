---
title: "识别文件中的简历信息"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/ai/document_ai-v1/resume/parse"
updateTime: "1731477912000"
---

# 识别文件中的简历信息

简历信息解析接口，支持PDF/DOCX/PNG/JPG四种文件类型的一次性的识别。文件大小需要小于30M。


> **Tip**: 单租户限流：10QPS，同租户下的应用没有限流，共享本租户的 10QPS 限流


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/document_ai/v1/resume/parse |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `document_ai:resume:recognize` 识别简历 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **示例值**："multipart/form-data; boundary=---7MA4YWxkTrZu0gW" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file` | `file` | 是 | 简历文件，支持 PDF / DOCX / PNG / JPG<br>**示例值**：file binary |


### 请求体示例

```HTTP
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file";
Content-Type: application/octet-stream


---7MA4YWxkTrZu0gW
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `resumes` | `resume\[\]` | 简历信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `file_md5` | `string` | 文件标识ID，依据文件内容自动生成 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 文本内容，当接口返回成功时，该字段才存在 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `new_content` | `string` | 经过排序后的文本内容，当接口返回成功时，该字段才存在 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mobile` | `string` | 手机号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `mobile_is_virtual` | `boolean` | 手机号码是否虚拟号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `country_code` | `string` | 手机号码国家编码 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `educations` | `resume_education\[\]` | 教育经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `school` | `string` | 学校名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始时间,格式：YYYY-MM-DD |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间,格式：YYYY-MM-DD,跟start_date值一样 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束时间,格式：YYYY-MM-DD |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间,格式：YYYY-MM-DD 或 “至今”，当值为“至今”时，end_date=="",值为其他时，end_date==end_time |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `major` | `string` | 专业 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `degree` | `string` | 学历——小学、初中、中职、高中、专科、本科、硕士、博士、其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `qualification` | `int` | 学历对应ID<br>**可选值有**：<br>- `1`: 小学 - `2`: 初中 - `3`: 中职 - `4`: 高中 - `5`: 专科 - `6`: 本科 - `7`: 硕士 - `8`: 博士 - `9`: 其他 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `careers` | `resume_career\[\]` | 职业经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `company` | `string` | 公司名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始时间,格式：YYYY-MM-DD |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 始时间,格式：YYYY-MM-DD,跟start_date值一样 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束时间,格式：YYYY-MM-DD |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间,格式：YYYY-MM-DD 或 “至今”，当值为“至今”时，end_date=="",值为其他时，end_date==end_time |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 职位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `int` | 工作类型<br>**可选值有**：<br>- `1`: 实习 - `2`: 全职 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type_str` | `string` | 工作类型——'实习'、'全职' |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `job_description` | `string` | 工作描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `projects` | `resume_project\[\]` | 项目经历 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 项目名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `title` | `string` | 项目岗位 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_date` | `string` | 开始时间,格式：YYYY-MM-DD |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 开始时间,格式：YYYY-MM-DD,跟start_date值一样 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_date` | `string` | 结束时间,格式：YYYY-MM-DD |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 结束时间,格式：YYYY-MM-DD 或 “至今”，当值为“至今”时，end_date=="",值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 项目描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `work_year` | `int` | 工作年限，为空表示工作年限未知，数字单位为年，整数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `date_of_birth` | `string` | 生日，格式YYYY-MM-DD |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `gender` | `int` | 性别<br>**可选值有**：<br>- `0`: 未知 - `1`: 男性 - `2`: 女性 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `willing_positions` | `string\[\]` | 希望获得的职位列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `current_location` | `string` | 当前工作地点(城市) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `willing_locations` | `string\[\]` | 希望工作地点列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `home_location` | `string` | 家乡(城市) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `languages` | `resume_language\[\]` | 语言 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `level` | `int` | 语言等级 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 语言描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `awards` | `resume_award\[\]` | 获奖 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `award` | `string` | 奖项 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `date` | `string` | 获奖时间，格式：YYYY |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `description` | `string` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `certificates` | `resume_certificate\[\]` | 证书 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 证书名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `desc` | `string` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `competitions` | `resume_competition\[\]` | 竞赛 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 竞赛名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `desc` | `string` | 描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `self_evaluation` | `string` | 自我评价 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `urls` | `string\[\]` | 链接列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `social_links` | `string\[\]` | 社交链接 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "resumes": [
            {
                "file_md5": "825c59042dxxxxx3ff90b45xxxxx88",
                "content": "XX负责行政人事管理和日常事务...",
                "new_content": "XX负责行政人事管理和日常事务...",
                "name": "张三",
                "email": "zhangsan.1111@company.com",
                "mobile": "13600000000",
                "mobile_is_virtual": false,
                "country_code": "86",
                "educations": [
                    {
                        "school": "A大学",
                        "start_date": "2020-01-03",
                        "start_time": "2020-01-03",
                        "end_date": "2021-01-03",
                        "end_time": "至今",
                        "major": "XX工程",
                        "degree": "本科",
                        "qualification": 6
                    }
                ],
                "careers": [
                    {
                        "company": "XX公司",
                        "start_date": "2022-01-03",
                        "start_time": "2022-01-03",
                        "end_date": "2023-01-03",
                        "end_time": "2023-01-03",
                        "title": "XXX工程师",
                        "type": 2,
                        "type_str": "全职",
                        "job_description": "负责XXX开发..."
                    }
                ],
                "projects": [
                    {
                        "name": "XX项目",
                        "title": "客户端研发",
                        "start_date": "2023-01-03",
                        "start_time": "2023-01-03",
                        "end_date": "2023-01-04",
                        "end_time": "2023-01-04",
                        "description": "XXX项目是一个..."
                    }
                ],
                "work_year": 5,
                "date_of_birth": "1995-01-01",
                "gender": 1,
                "willing_positions": [
                    "XX岗位"
                ],
                "current_location": "上海",
                "willing_locations": [
                    "上海"
                ],
                "home_location": "上海",
                "languages": [
                    {
                        "level": 2,
                        "description": "英语四级:600"
                    }
                ],
                "awards": [
                    {
                        "award": "XXX大赛奖项",
                        "date": "2015",
                        "description": "曾获XXX大赛奖项..."
                    }
                ],
                "certificates": [
                    {
                        "name": "XXX证书",
                        "desc": "曾获得XXX证书..."
                    }
                ],
                "competitions": [
                    {
                        "name": "XXX竞赛",
                        "desc": "曾参加XXX竞赛..."
                    }
                ],
                "self_evaluation": "我是一个...",
                "urls": [
                    "https://github.com/"
                ],
                "social_links": [
                    "https://github.com/"
                ]
            }
        ]
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2110001 | param is invalid | 输入文件错误，参考文档检查输入参数 |
| 400 | 2110002 | No resume detected | 未检测出简历文件，参考文档检查输入文件是否有效 |
| 500 | 2110010 | Internal error, please try later. | 后端服务异常或网络异常，可重新请求 |
| 400 | 2110003 | You have reached the Intelligent document parsing limit. To continue using this function, please contact sales to purchase more. | 智能文档解析次数已达使用上限，如需继续使用，请联系销售购买 |


