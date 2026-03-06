---
title: "更新 Offer 状态"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/offer_status"
updateTime: "1725526529000"
---

# 更新 Offer 状态

通过 Offer ID 更新候选人 Offer 的「Offer 审批状态」或 「Offer 发送和接受状态」。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=hire&version=v1&resource=offer&method=offer_status)

:::html
<md-alert type="tip">

</md-alert>
:::

:::html
<md-alert type="warn">

</md-alert>
:::

:::html
<md-alert type="error">

</md-alert>
:::

## 注意事项

- 若当前 Offer 是通过飞书招聘发起的审批，则不可通过此接口更新「Offer 审批状态」。
- 若当前 Offer 通过飞书招聘发送过候选人，则不可通过此接口更新「Offer 发送和接受状态」。
- 若当前 Offer 所属投递阶段已进入「待入职」阶段，则不可通过此接口更新「Offer 审批状态」和「Offer 发送和接受状态」。

## 前提条件
- 更新 Offer 审批状态前，请前往「飞书招聘」-「设置」-「Offer 设置」-「Offer 规则设置」开启「通过 OA 系统创建和审批 Offer」。
- 更新 Offer 发送和接受状态前，请前往「飞书招聘」-「设置」-「Offer 设置」-「Offer 规则设置」开启「通过 OA 系统发送 Offer」。

## Offer 状态说明

### Offer 状态分类
- Offer 被创建后，状态为`「Offer 已创建」`
- Offer 审批状态：`「Offer 审批中」`、`「Offer 审批通过」`、`「Offer 审批不通过」`、`「Offer 审批已撤回」`
- Offer 发送和接受状态：`「Offer 已发送」`、`「Offer 已失效」`、`「Offer 被候选人接受」`、`「Offer 被候选人拒绝」`

### Offer 状态流转图
![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/6faaeda86bbe8f1b9f2c7ef91062edd2_xU7rL7qrof.png)


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
      <md-td>https://open.feishu.cn/open-apis/hire/v1/offers/:offer_id/offer_status</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>PATCH</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[100 次/分钟](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
    </md-tr>
    <md-tr>
      <md-th>支持的应用类型</md-th>
      <md-td>
      <md-app-support types="custom"></md-app-support>
      </md-td>
    </md-tr>
    <md-tr>
      <md-th>
            权限要求
            <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
            
      </md-th>
      <md-td>
            <md-perm name="hire:offer" desc="更新 offer 信息" support_app_types="custom" tags="">更新 offer 信息</md-perm>
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
      <md-th style="width: 35%;">名称</md-th>
      <md-th style="width: 13%;">类型</md-th>
       <md-th style="width: 15%;" filters="是,否" >必填</md-th>
      <md-th  style="width: 37%;">描述</md-th>
    </md-tr>
  </md-thead>
  <md-tbody>
    <md-tr>
      <md-td>Authorization</md-td>
      <md-td>string</md-td>
      <md-td>是</md-td>
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
<md-td>是</md-td>
<md-td>**固定值**："application/json; charset=utf-8"</md-td>
</md-tr>
</md-tbody>
</md-table>
:::



### 路径参数
:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 52%;">描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>

<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offer_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	Offer ID，如何获取请参考[获取 Offer 列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer/list)

**示例值**："6930815272790114324"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::



### 请求体

:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 15%;" filters="是,否" >必填</md-dt-th>
      <md-dt-th style="width: 37%;">描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>

<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >offer_status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	Offer 状态

**示例值**：6

**可选值有**：
<md-enum>
<md-enum-item key="2" >Offer 审批中</md-enum-item>
<md-enum-item key="3" >Offer 审批已撤回</md-enum-item>
<md-enum-item key="4" >Offer 审批通过</md-enum-item>
<md-enum-item key="5" >Offer 审批不通过</md-enum-item>
<md-enum-item key="6" >Offer 已发送</md-enum-item>
<md-enum-item key="7" >Offer 被候选人接受</md-enum-item>
<md-enum-item key="8" >Offer 被候选人拒绝</md-enum-item>
<md-enum-item key="9" >Offer 已失效</md-enum-item>
<md-enum-item key="10" >Offer 已创建</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >expiration_date</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Offer 失效时间
<br>

**注意**：当请求参数 offer_status 为「Offer 已发送」时必填
<br>

**值格式**："YYYY-MM-DD"

**示例值**："2023-01-01"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >termination_reason_id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	终止原因 ID 列表，可通过[获取终止投递原因](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/termination_reason/list)接口获取
<br>

**最大长度**：
50
<br>

**注意**：当请求参数 offer_status 为「Offer 被候选人拒绝」时必填

**示例值**：["6891560630172518670"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >termination_reason_note</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	Offer 终止备注信息

**示例值**："不符合期望"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "offer_status": 6,
    "expiration_date": "2023-01-01",
    "termination_reason_id_list": [
        "6891560630172518670"
    ],
    "termination_reason_note": "不符合期望"
}
</md-code-json>
:::



## 响应





### 响应体
:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 52%;">描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>

<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	错误码，非 0 表示失败
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >msg</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	错误描述
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >\-</md-text>
	</md-dt-td>
	<md-dt-td>
	\-
	</md-dt-td>
</md-dt-tr>


  </md-dt-tbody>
</md-dt-table>
:::



### 响应体示例
:::html
<md-code-json>
{
    "code": 0,
    "msg": "success",
    "data": {}
}
</md-code-json>
:::



### 错误码
:::html
<md-table>
    <md-thead>
        <md-tr>
            <md-th style="width: 15%;">HTTP状态码</md-th>
            <md-th style="width: 15%;">错误码</md-th>
            <md-th style="width: 30%;">描述</md-th>
            <md-th style="width: 30%;">排查建议</md-th>
        </md-tr>
    </md-thead>
  <md-tbody>

<md-tr>
  <md-td>500</md-td>
  <md-td>1002001</md-td>
  <md-td>系统错误</md-td>
  <md-td>请根据实际报错信息定位或咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002002</md-td>
  <md-td>参数错误</md-td>
  <md-td>检查参数是否正确，例如类型，大小</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002064</md-td>
  <md-td>Offer 不存在</md-td>
  <md-td>Offer ID 非法，请检查入参 `offer_id` 是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1002069</md-td>
  <md-td>Offer 审批状态更新失败</md-td>
  <md-td>确认 Offer 当前状态，更新 Offer 审批状态需遵循状态流转规则</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002070</md-td>
  <md-td>当前 Offer 已通过飞书招聘发起过审批，不可再通过此接口更新 Offer 状态</md-td>
  <md-td>确认 Offer 是否已由飞书招聘系统发起审批</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002071</md-td>
  <md-td>当前投递阶段不可更新Offer 接受状态</md-td>
  <md-td>确认当前投递阶段是否在「待入职」之前</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002072</md-td>
  <md-td>不可将 Offer 置为已失效</md-td>
  <md-td>确认当前 Offer 的状态为「已发出」或「候选人已接受」</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1002073</md-td>
  <md-td>当前 Offer 已通过飞书招聘发送给候选人，不可通过该接口更新 Offer 发送和接受状态</md-td>
  <md-td>确实当前 Offer 是否已经在飞书招聘系统发送给候选人</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1002074</md-td>
  <md-td>同步开关尚未打开，仅支持在招聘系统中创建 
 Offer、修改 Offer 状态和发送 Offer</md-td>
  <md-td>请前往「飞书招聘」-「设置」-「Offer 设置」-「Offer 规则设置」开启对应开关</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




