---
title: "识别文件中的食品生产许可证"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/ai/document_ai-v1/food_produce_license/recognize"
updateTime: "1731478056000"
---

# 识别文件中的食品生产许可证

食品生产许可证识别接口，支持JPG/JPEG/PNG/BMP/PDF五种文件类型的一次性的识别。
文件大小需要小于10M。


> **Tip**: 单租户限流：10QPS，同租户下的应用没有限流，共享本租户的 10QPS 限流


## 请求

| 项目 | 值 |
| --- | --- |
| HTTP URL | https://open.feishu.cn/open-apis/document_ai/v1/food_produce_license/recognize |
| HTTP Method | POST |
| 接口频率限制 | [10 次/秒](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN) |
| 支持的应用类型 | custom,isv |
| 权限要求             调用该 API 所需的权限。开启其中任意一项权限即可调用 | `document_ai:food_produce_license:recoginze` 食品生产许可证识别 |

### 请求头

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| Authorization | string | 是 | `tenant_access_token` **值格式**："Bearer `access_token`" **示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560" [了解更多：如何选择与获取 access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use) |
| Content-Type | string | 是 | **示例值**："multipart/form-data; boundary=---7MA4YWxkTrZu0gW" |


### 请求体


| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `file` | `file` | 是 | 识别的食品生产许可证源文件<br>**示例值**：file binary |


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
| &nbsp;&nbsp;└ `food_produce_license` | `food_produce_license` | 食品生产许可证信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `entities` | `food_produce_entity\[\]` | 识别出的实体列表 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `type` | `string` | 识别的字段种类<br>**可选值有**：<br>- `validity_period`: 有效期 - `issuer`: 签发人 - `issuing_authority`: 发证机关 - `complaints_hotline`: 投诉举报电话 - `food_category`: 食品类别 - `production_address`: 生产地址 - `license_number`: 许可证编号 - `domicile`: 住所 - `legal_representative`: 法定代表人(负责人) - `credit_code`: 社会信用代码(身份证号) - `producer`: 生产者名称 - `daily_supervisory_authorities`: 日常监督管理机构 - `daily_supervisor`: 日常监督管理人员 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 识别出字段的文本信息 |


### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "food_produce_license": {
            "entities": [
                {
                    "type": "issuer",
                    "value": "张三"
                }
            ]
        }
    }
}
```


### 错误码

| HTTP状态码 | 错误码 | 描述 | 排查建议 |
| --- | --- | --- | --- |
| 400 | 2110001 | Param is invalid. | 输入文件错误，参考文档检查输入参数 |
| 400 | 2110002 | No valid entity. | 未检测出食品生产许可证信息，参考文档检查输入文件是否有效 |
| 500 | 2110010 | Internal error, please try later. | 后端服务异常或网络异常，可重新请求 |
| 400 | 2110003 | You have reached the Intelligent document parsing limit. To continue using this function, please contact sales to purchase more. | 智能文档解析次数已达使用上限，如需继续使用，请联系销售购买 |


