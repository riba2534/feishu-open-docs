---
title: "导入外部内推奖励"
fullPath: "/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/external_referral_reward/create"
updateTime: "1731926631000"
---

# 导入外部内推奖励

支持将外部的内推奖励（积分/现金）导入到招聘的「内推账号」中{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=hire&version=v1&resource=external_referral_reward&method=create)

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
      <md-td>https://open.feishu.cn/open-apis/hire/v1/external_referral_rewards</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[10 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="hire:external_referral_reward" desc="导入内推奖励" support_app_types="custom" tags="">导入内推奖励</md-perm>
      </md-td>
    </md-tr>
    <md-tr>
      <md-th>
            字段权限要求
      </md-th>
      <md-td>
        <md-alert type="tip" icon="none">
        该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请
        </md-alert>
        <md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
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



### 查询参数
:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 35%;">名称</md-dt-th>
      <md-dt-th style="width: 13%;">类型</md-dt-th>
      <md-dt-th style="width: 15%;" filters="是,否" >必填</md-dt-th>
      <md-dt-th style="width: 37%;" >描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  <md-dt-tbody>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >user_id_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户 ID 类型

**示例值**：open_id

**可选值有**：
<md-enum>
<md-enum-item key="open_id" >标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。[了解更多：如何获取 Open ID](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)</md-enum-item>
<md-enum-item key="union_id" >标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。[了解更多：如何获取 Union ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)</md-enum-item>
<md-enum-item key="user_id" >标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。[了解更多：如何获取 User ID？](/ssl:ttdoc/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)</md-enum-item>
</md-enum>

**默认值**：`open_id`

**当值为 `user_id`，字段权限要求**：
<md-perm name="contact:user.employee_id:readonly" desc="获取用户 user ID" support_app_types="custom" tags="">获取用户 user ID</md-perm>
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
	<md-text type="field-name" >referral_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	内推人 ID

内推人的唯一标识，在[获取用户信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/get)中获取

**示例值**："on_94a1ee5551019f18cd73d9f111898cf2"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >create_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	奖励创建人，管理员与内推人可见，若不传，则默认为「外部系统」

**示例值**："on_94a1ee5551019f18cd73d9f111898cf2"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >confirm_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	确认人，若导入的「内推奖励状态」为「已确认」可传入，若不传，则默认为「外部系统」

**示例值**："on_94a1ee5551019f18cd73d9f111898cf2"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >pay_user_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	发放人，导入的「内推奖励状态」为「已发放」的奖励传入，若不传，则默认为「外部系统」

**示例值**："on_94a1ee5551019f18cd73d9f111898cf2"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >external_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	外部系统奖励唯一id（仅用于幂等）

**示例值**："6930815272790114324"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >application_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	内推的候选人投递 ID，可通过[获取投递列表](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/list)获取
若未传入`talent_id`，该参数必填
若传入了`talent_id`，该参数选填
若同时传入了`application_id`和`talent_id`，以`application_id`为准


<md-alert type="warn">
若不传入投递 ID（`application_id`），当前内推奖励将无法关联到投递，
系统内无法展示该内推对应的「职位」、「职位负责人」、「offer负责人」，对应字段将展示为「--」。
</md-alert>

**示例值**："6930815272790114325"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >talent_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	内推的候选人人才 ID

若未传入`application_id`，该参数必填

若传入了`application_id`，该参数可不填，将以「内推的候选人投递 ID」为准

**示例值**："6930815272790114326"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >job_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	内推职位 ID

招聘系统内的职位 ID。若不传入，对管理员与内推人将展示为--

若传入了「内推的候选人投递 ID」，该参数可不填，职位ID将自动以「投递ID」关联的「职位ID」为准

<md-alert type="warn">
若不传入「内推职位 ID」，且未传入「内推的投递 ID」，当前内推奖励将无法关联到职位，
「职位的相关权限人」（如社/校招管理员、职位负责人、协助人、用人经理等）无法看到该条内推记录
</md-alert>

**示例值**："6930815272790114327"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >reason</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	奖励原因，若不传则为 「--」

将展示在内推奖励明细中，管理员与内推人可见。
如需与飞书招聘判定的内推奖励原因保持一致，方便统计，可参考下方说明传入
- 若「奖励规则类型」为「过程奖励」，建议传入如下原因：
   - 推荐奖励
   - 进入{阶段名称}阶段
   - 候选人到面奖励 
- 若「奖励规则类型」为「入职奖励」，建议传入如下原因: 
   - 入职 
   - 转正 
- 若「奖励规则类型」为「活动奖励」，建议传入如下原因：
   - 累计推荐 n 个候选人{过程奖励或入职奖励原因}
   - 推荐满 n 个候选人
- 若「奖励规则类型」为「开源奖励」，建议传入如下原因：
   - 入职｜开源 
   - 转正｜开源

**示例值**："入职｜开源"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >rule_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	导入的奖励规则类型，将展示在内推奖励明细中，管理员与内推人可见

如需与飞书招聘内的奖励原因保持一致，方便统一统计，可参考下方说明传入

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="1" >入职奖励，候选人入职或转正后产生的奖励</md-enum-item>
<md-enum-item key="2" >过程奖励，入职奖励外，若候选人有阶段性进展，则给予内推人对应的奖励</md-enum-item>
<md-enum-item key="3" >活动奖励，额外奖励，用于支持内推周期性活动</md-enum-item>
<md-enum-item key="4" >开源奖励，若内推候选人首次进入人才库，且在被推荐后一段时间内，入职了规则内的任意职位的奖励</md-enum-item>
<md-enum-item key="5" >其他奖励，以上奖励无法覆盖的奖励</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >bonus</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >bonus_amount</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	奖励额度
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >bonus_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	奖励发放形式

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="1" >积分</md-enum-item>
<md-enum-item key="2" >现金</md-enum-item>
</md-enum>

**默认值**：`1`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >point_bonus</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	导入积分数量，若奖励发放形式为现金为必填

**示例值**：100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >cash</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >cash</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	现金奖励
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >currency_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	导入现金币种，若奖励发放形式为现金为必填，币种参数可在[「枚举常量介绍中查询」](https://open.feishu.cn/document/server-docs/hire-v1/enum)

**示例值**："CNY"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >amount</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	导入现金数量，若奖励发放形式为现金为必填，需传入非负数

**示例值**：100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >stage</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	导入的内推奖励状态

**示例值**：1

**可选值有**：
<md-enum>
<md-enum-item key="1" >待确认，建议导入需人工审核的奖励明细，导入后，需管理员在「内推奖励管理」-「待确认」中，手动审核确认才会展示给内推人</md-enum-item>
<md-enum-item key="2" >已确认，建议导入已通过人工审核但仍未发放的奖励明细
导入后，将展示给管理员和内推人，奖励状态展示为「已确认」（未发放）</md-enum-item>
<md-enum-item key="3" >已发放，建议导入已发放完成的奖励明细，导入后，将展示给管理员和内推人，奖励状态展示为「已发放」</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	奖励产生时间

时间戳，内推奖励触发时间，若未传入，取接口调用时间

**示例值**："1704720275000"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >confirm_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	确认时间

时间戳，若导入的「内推奖励状态」为「已确认」可传入，若未传入，取接口传入时间

**示例值**："1704720275000"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >pay_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	发放时间

时间戳，若导入的「内推奖励状态」为「已确认」可传入，若未传入，取接口传入时间

**示例值**："1704720275001"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >onboard_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	入职时间

时间戳，管理员与内推人可见，当「奖励规则类型」为「入职奖励」时，建议传入该参数

**示例值**："1704720275002"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >conversion_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	转正时间

时间戳，管理员与内推人可见，当「奖励规则类型」为「入职奖励」时，建议传入该参数

**示例值**："1704720275003"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >comment</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	操作备注

管理员与内推人可见，若为空，将展示为奖励原因

**示例值**："已发放"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "referral_user_id": "on_94a1ee5551019f18cd73d9f111898cf2",
    "create_user_id": "on_94a1ee5551019f18cd73d9f111898cf2",
    "confirm_user_id": "on_94a1ee5551019f18cd73d9f111898cf2",
    "pay_user_id": "on_94a1ee5551019f18cd73d9f111898cf2",
    "external_id": "6930815272790114324",
    "application_id": "6930815272790114325",
    "talent_id": "6930815272790114326",
    "job_id": "6930815272790114327",
    "reason": "入职｜开源",
    "rule_type": 1,
    "bonus": {
        "bonus_type": 1,
        "point_bonus": 100,
        "cash": {
            "currency_type": "CNY",
            "amount": 100
        }
    },
    "stage": 1,
    "create_time": "1704720275000",
    "confirm_time": "1704720275000",
    "pay_time": "1704720275001",
    "onboard_time": "1704720275002",
    "conversion_time": "1704720275003",
    "comment": "已发放"
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


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	创建的内推奖励的id
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
    "data": {
        "id": "6930815272790114324"
    }
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
  <md-td>请根据实际报错信息定位</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1002002</md-td>
  <md-td>参数错误</md-td>
  <md-td>请根据实际报错信息定位</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




