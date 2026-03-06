---
title: "批量新增用户"
fullPath: "/ukTMukTMukTM/uIDOwUjLygDM14iM4ATN"
updateTime: "1626181326000"
---

# 批量新增用户

该接口用于向通讯录中批量新增多个用户。<br>


:::html
<md-alert type="warn">
调用该接口需要具有待添加用户所在部门的通讯录授权范围。<br>
应用商店应用无权限调用此接口。<br>
调用该接口需要申请 `更新通讯录` 以及 `以应用身份访问通讯录` 权限。
</md-alert>
:::


## 请求
:::html
<md-table>
  <md-thead>
  <tr>
      <md-th>基本</md-th>
      <md-th></md-th>
  </tr>
  </md-thead>
  <md-tbody>
    <md-tr>
      <md-th>HTTP URL</md-th>
      <md-td>https://open.feishu.cn/open-apis/contact/v2/user/batch_add</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    
    
    <md-tr>
      <md-th>
权限要求
 <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
<div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
</md-th>
      <md-td>
        <md-perm href="/ssl:ttdoc/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN"> 更新通讯录 </md-perm>
         <md-perm href="/ssl:ttdoc/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN">以应用身份访问通讯录（历史版本）</md-perm>
      </md-td>
    </md-tr>
  </md-tbody>
</md-table>
:::
### 请求头
:::html
<md-table> 
  <md-thead> 
    <md-tr> 
      <md-th style="width: 18%;">名称</md-th>  
      <md-th style="width: 15%;">类型</md-th>  
       <md-th style="width: 15%;">必填</md-th>  
      <md-th>描述</md-th> 
    </md-tr> 
  </md-thead>  
  <md-tbody> 
    <md-tr> 
      <md-td>Authorization</md-td>  
      <md-td>string</md-td>  
      <md-td> 是 </md-td> 
      	<md-td>
<md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag>
 
**值格式**："Bearer `access_token`"

**示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560"
          
 [了解更多：如何选择与获取 access token](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
	</md-td>
</md-tr>
     <md-tr> 
      <md-td>Content-Type</md-td>  
      <md-td>string</md-td>  
      <md-td> 是 </md-td> 
     <md-td>**固定值**："application/json; charset=utf-8"</md-td>
</md-tr>
   
  </md-tbody> 
</md-table>
:::
### 请求体
参数 | 类型 | 必填 / 选填 | 说明
-- | -- | -- | --
users | array | 必填 | 所有待新增用户的集合。
&emsp;∟name | string | 必填 | 用户名。
&emsp;∟departments | array | 必填 | 待新增用户所属部门，目前仅支持单个用户所属单个部门。<br>需要应用的通讯录权限范围包含该部门。
&emsp;∟user_id | string | 选填 | 用户企业内唯一标识。只能在创建用户时指定，不支持更新。<br>不指定时由平台自动生成。<br>自定义唯一标识不区分大小写，长度为 1 ~ 64 个字符。只能由数字、字母和“_”、“-”、“@”、“.”四种特殊字符组成，且第一个字符必须是数字或字母。
&emsp;∟email | string | 选填 | 用户邮箱。
&emsp;∟mobile | string | 必填 | 用户手机号。
&emsp;∟mobile_visible | bool | 选填 | 手机号码可见性，true 为可见，false 为不可见，目前默认为 true。<br>不可见时，企业内其他员工将无法在客户端内查看该员工的手机号码。
&emsp;∟city | string | 选填 | 用户所在城市。
&emsp;∟country | string | 选填 | 用户所在国家。<br>字段值请参考国际标准化组织 [ISO 3166-1 标准](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) 中的二位代码。
&emsp;∟gender | int | 选填 | 性别，1：男，2：女。
&emsp;∟employee_type | int | 选填 | 员工类型，1：正式员工，2：实习生，3：外包，4：劳务，5：顾问。
&emsp;∟join_time | int | 选填 | 入职时间，以秒为单位的 Unix 时间戳。
&emsp;∟leader_user_id<br>&emsp;∟leader_open_id | string | 选填 | 直属上级用户 ID，支持通过 user_id 或 open_id 进行设置。<br>请求同时传递两个字段时只使用 leader_user_id，忽略 leader_open_id。
&emsp;∟employee_no | string | 选填 | 员工工号。
&emsp;∟custom_attrs | array | 选填 | 自定义用户属性。<br>该字段仅当企业管理员在企业管理后台开启了“允许开放平台 API 调用”时有效。 <br>传入的每个自定义用户属性需要包含平台生成的属性 ID 和要设置的属性对应类型的值。<br>当企业管理后台未开启“允许开放平台 API 调用”时，或者传入的属性 ID 不存在 / 非法时，会忽略该条属性的设置信息。
&emsp;&emsp;∟id | string | 必填 | 自定义属性 ID。
&emsp;&emsp;∟value | object | 必填 | 自定义属性值。
&emsp;&emsp;&emsp;∟text | string | 选填 | 当自定义属性类型为 text 时，传入此字段，表示属性的文字值。
&emsp;&emsp;&emsp;∟url | string | 选填 | 当自定义属性类型为 href 时，传入此字段，表示属性的 URL 值。
&emsp;&emsp;&emsp;∟pc_url | string | 选填 | 当自定义属性类型为 href 时，传入此字段，表示属性的 PC 端 URL 值。
&emsp;∟work_station | string | 选填 | 员工工位。
need_send_notification | bool | 选填 | 是否对本次新增的所有用户发送邀请通知，默认为 false，不发送通知。<br>该字段为 true 时， 用户添加成功后会向对应的邮箱或手机发送邀请通知。

### 请求体示例
```json
{
    "users": [
        {
            "name": "张三",
            "departments": [
                "od-234355343342acdbef33"
            ],
            "user_id": "id_zhangsan",
            "email": "zhangsan@gmail.com",
            "mobile": "+8613822235671",
            "mobile_visible": false,
            "city": "北京",
            "country": "CN",
            "gender": 1,
            "employee_type": 1,
            "join_time": 1534222800,
            "leader_open_id": "ou_3454556545acdb12324",
            "leader_user_id": "2ab56f23",
            "employee_no": "323463",
            "custom_attrs": [
                {
                    "id": "C-6702376000044400907",
                    "value": {
                        "url": "http://www.feishu.cn/",
                        "pc_url": "http://www.feishu.cn/pc"
                    }
                }
            ],
            "work_station": "Poly, F6-123"
        },
        {
            "name": "李四",
            "departments": [
                "od-234355343342acdbef33"
            ],
            "user_id": "id_lisi",
            "mobile": "+8613822235672",
            "leader_user_id": "id_zhangsan"
        }
    ],
    "need_send_notification": false
}
```
## 响应
### 响应体
参数 | 说明
-- | --
code | 返回码，非 0 表示失败。
msg | 对返回码的文本描述。
data | -
&emsp;∟task_id | 生成的异步任务 ID，参见 [查询批量任务执行状态](/ssl:ttdoc/ukTMukTMukTM/uUDOwUjL1gDM14SN4ATN) 接口。
### 响应体示例
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "task_id": "123456784b68a7c89abcdef092dc09ea"
    }
}
```
### 错误码

具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)
