---
title: "提取文件中的合同字段"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/ai/document_ai-v1/contract/field_extraction"
updateTime: "1731478121000"
---

# 提取文件中的合同字段

支持从doc、docx和pdf文件类型中提取合同字段。
文件大小需要小于10M。


> **Tip**: 单租户限流：10QPS，同租户下的应用没有限流，共享本租户的 10QPS 限流


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/document_ai/v1/contract/field_extraction |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `document_ai:contract:field_extract` 获取合同字段提取 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **示例值**："multipart/form-data; boundary=---7MA4YWxkTrZu0gW" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file` | `file` | 是 | 合同字段解析的源文件，当前只支持pdf, doc, docx三种类型的文件<br>**示例值**：file binary |
| `pdf_page_limit` | `int` | 是 | pdf页数限制，太长会导致latency增加，最大允许100页<br>**示例值**：15 |
| `ocr_mode` | `string` | 是 | ocr 参数，当前支持force, pdf, unused三种格式<br>**示例值**："auto"<br>**可选值有**：<br>- `force`: pdf类型文件直接走OCR解析 - `auto`: pdf类型文件先走本地解析，无法解析（扫描/图片版）再走OCR - `unused`: 不调用OCR，扫描/图片PDF返回不可解析信息 |


### 请求体示例

```HTTP
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file";
Content-Type: application/octet-stream


---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="pdf_page_limit";

15
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="ocr_mode";

auto
---7MA4YWxkTrZu0gW
```


## 响应


### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `code` | `int` | 错误码，非 0 表示失败 |
| `msg` | `string` | 错误描述 |
| `data` | `\-` | \- |
| &nbsp;&nbsp;└ `file_id` | `string` | 文件的唯一id |
| &nbsp;&nbsp;└ `price` | `extract_price` | 总交易金额 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_price` | `number(float)` | 交易金额 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `contract_price_original` | `string` | 从原文中抽取的交易金额 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 原文中描述交易金额的文字 |
| &nbsp;&nbsp;└ `time` | `extract_time` | 期限相关信息，包括开始日期、结束日期、有效时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `time_start` | `string` | 开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `time_end` | `string` | 结束时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `original_time_start` | `string` | 原文中抽取出的开始时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `original_time_end` | `string` | 原文中抽取出的结束时间 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text_start` | `string` | 原文中关于开始时间的描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text_end` | `string` | 原文中关于结束时间的描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `initial_term` | `extract_term` | 合同持续时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `initial_time` | `string` | 合同持续时长 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `initial_unit` | `string` | 持续时长单位 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text_initial_term` | `string` | 原文中关于持续时间的描述 |
| &nbsp;&nbsp;└ `copy` | `extract_copy` | 盖章份数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `copy_num` | `int` | 盖章份数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `original_copy` | `string` | 从原文中抽取的盖章份数 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `key` | `string` | 盖章文件类型 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `text` | `string` | 原文有关盖章份数的描述 |
| &nbsp;&nbsp;└ `currency` | `extract_currency` | 币种 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `currency_name` | `string` | 币种名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `currency_text` | `string` | 币种符号 |
| &nbsp;&nbsp;└ `header` | `string` | 合同标题 |
| &nbsp;&nbsp;└ `body_info` | `body_info\[\]` | 主体信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `body_type` | `string` | 主体类型<br>**可选值有**：<br>- `buy`: 甲方主体 - `sell`: 乙方主体 - `third`: 第三方、其他方主体 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `body_entity` | 值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `string` | 地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contacts` | `string` | 联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `string` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id_number` | `string` | ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `legal_representative` | `string` | 法人代表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `party` | `string` | 当事人 |
| &nbsp;&nbsp;└ `bank_info` | `bank_info\[\]` | 银行信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bank_type` | `string` | 甲乙方信息类型<br>**可选值有**：<br>- `buy_bank`: 甲方银行 - `sell_bank`: 乙方银行 - `third_bank`: 第三方银行 - `unceratin_bank`: 其他方银行 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `bank_entity` | 值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `account_name` | `string` | 账户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `bank_name` | `string` | 银行名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `account_number` | `string` | 账户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `phone` | `string` | 电话 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `contacts` | `string` | 联系人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `tax_number` | `string` | 传真号码 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `address` | `string` | 联系地址 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id_number` | `string` | id号 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 邮箱 |


### 响应体示例

```json
{"code":0,
"msg":"success",
"data":{"file_id":"121345678",
"price":{"contract_price":200000,
"contract_price_original":""200000"",
"text":"本合同项下总金额共计￥200000（贰拾万元整）"},
"time":{"time_start":"2020-07-01",
"time_end":"2022-06-30",
"original_time_start":"2020年07月1日",
"original_time_end":"2022年6月30日",
"text_start":"本协议自有效期自【2020】年【07】月【1】日至【2022】年【6】月【30】日，有效期2年。",
"text_end":"本协议自有效期自【2020】年【07】月【1】日至【2022】年【6】月【30】日，有效期2年。",
"initial_term":{"initial_time":"2",
"initial_unit":"年"},
"text_initial_term":"2年"},
"copy":{"copy_num":2,
"original_copy":"一式贰份",
"key":"协议",
"text":"此协议一式贰份，双方各执壹份，具有同等法律效力。"},
"currency":{"currency_name":"CNY",
"currency_text":"¥"},
"header":"项目活动框架协议",
"body_info":[{
    "body_type": "buy",
    "value": {
        "address": "北京市A区B园4号楼",
        "contacts": "张三",
        "email": "zhangsan.1111@bytedance.com",
        "phone": "13600000000",
        "id_number": "310XXXXXXXXXXXXXXX",
        "legal_representative": "张三",
        "party": "北京字节跳动网络技术有限公司"
    }
}],
"bank_info":[{
    "bank_type": "buy",
    "value": {
        "account_name": "北京字节跳动网络技术有限公司",
        "bank_name": "中国A银行B支行",
        "account_number": "11230xxxxx004701",
        "phone": "010-8xxxx688",
        "contacts": "张三",
        "tax_number": "911101xxxxx684235",
        "address": "A市B区C园D楼3-8",
        "id_number": "11230xxxxx004701",
        "email": "zhangsan.1111@bytedance.com"
    }
}]}}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2110001 | invalid request | 可能是文件类型或者其他参数配置错误，请检查后重试 |
| 400 | 2110002 | no contract detected | 无字段抽出，请确认合同是否有指定字段 |
| 500 | 2110010 | network anomaly or out of limit, please try it later | 接口调用失败，可能是网络问题或超出限制，请稍后再试 |
| 400 | 2110003 | You have reached the Intelligent document parsing limit. To continue using this function, please contact sales to purchase more. | 智能文档解析次数已达使用上限，如需继续使用，请联系销售购买 |


