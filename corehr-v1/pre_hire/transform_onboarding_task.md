---
title: "流转入职任务"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/transform_onboarding_task"
updateTime: "1758722082000"
---

# 流转入职任务

处于进行中的入职流程，可通过本接口实现手动开启、提交或审批入职任务

- 当任务处于「手动开启」时，可通过本接口手动开启任务，将任务状态流转到「进行中」
- 当任务处于「进行中」时，可通过本接口提交任务，将任务流转到「审批中」或「已完成」
- 当任务处于「审批中」时，可通过本接口审批任务，将任务流转到「已完成」或「已拒绝」
- 当任务处于「已拒绝」时，可通过本接口提交任务，将任务流转到「审批中」{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=pre_hire&method=transform_onboarding_task)

:::html
<md-alert type="tip">
该接口会按照应用拥有的「待入职人员」的权限范围返回数据，请提前在「开发者后台 - 权限管理 - 数据权限-飞书人事(企业版)数据权限范围」中申请「待入职人员」权限范围
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/pre_hires/transform_onboarding_task</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[1000 次/分钟、50 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="corehr:pre_hire:transform_onboarding_task" desc="入职常规任务的通用流转" support_app_types="custom" tags="">入职常规任务的通用流转</md-perm>
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
	<md-text type="field-name" >pre_hire_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	待入职ID，可以通过[搜索待入职人员信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/search)接口获得

**示例值**："7345005664477775407"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >task_code</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	任务标识码。

- 对于系统内置的任务，标识码与任务名称的对应关系如下所示：

   > 其中 **创建账户SSO** 为隐藏的任务节点，在 **个人信息** 前自动执行。

    - 1：职位信息
    - 2：个人信息
    - 3：创建账户SSO
    - 4：签到
    - 9：签署入职文件


- 对于自定义的任务节点（如：3095697a-065f-4627-a47c-46fe958a6754），名称的获取方式如下所示：
    1.  通过 `pre_hire_id` 调用[搜索待入职人员信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/search)接口或[查询待入职](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/query)
   2.  查询字段 `fields` 中添加 `onboarding_info.onboarding_task_list`
       
       查询后返回的 onboarding_task_list 结构体中包含标识码和任务名字的对应关系，示例如下所示：
```json
{
    "onboarding_task_list": [
        {
            "task_code": "3095697a-065f-4627-a47c-46fe958a6754",
            "task_name": "修改入职日期",
            "task_status": "uninitialized"
        },
        {
            "task_code": "d37b9d7c-232d-4a55-98fa-541318234ede",
            "task_name": "工签补充任务",
            "task_status": "uninitialized"
        }
    ]
}
```


**示例值**："27691344-699b-47fb-a352-7b41e992a536"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >transform_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	流转类型，当任务处于不同的状态时，通过该字段指定任务做何种类型的流转。

入职任务状态：
- uninitialized：任务未初始化
- not_started：任务未开始
- in_progress：任务进行中
- in_review：任务审批中
- rejected：任务已拒绝
- failed：任务失败
- skipped：任务自动跳过
- completed：任务完成
- exception：任务异常
- terminated：任务终止
- initiating：任务发起中
- manual_skipped：任务手动跳过

任务流转类型：
- manual_start_task：手动开启任务
> 当任务处于未开始状态时，可通过指定该类型手动开启任务
- submit_task：提交任务
> 当任务处于进行中和已拒绝时，可以通过指定该类型提交任务。创建账户(`task_code：3`)、签到（`task_code：4`）和电子签（`task_code：9`）任务不支持提交
- review_task：审批任务
> 当任务处于审批中时，可以通过指定该类型审批任务。通过本接口审批任务时，会忽略多个审批人审批的场景。

**示例值**："review_task"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >review_decision</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	审批结果，当`transform_type`为`review_task`时，该字段需要传值，否则报错。

审批结果：
- approve：通过
- reject：拒绝，

**示例值**："approve"
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
	审批原因，审批任务时，如果`review_decision`传参为`approve`时，审批原因可以不填；如果`review_decision`传参为`reject`时，审批原因必填。
> 审批原因长度需小于3000字节

**示例值**："信息填写完整，允许通过"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "pre_hire_id": "7345005664477775407",
    "task_code": "27691344-699b-47fb-a352-7b41e992a536",
    "transform_type": "review_task",
    "review_decision": "approve",
    "reason": "信息填写完整，允许通过"
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
	<md-text type="field-name" >success</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否成功流转任务，流转成功时返回true，流转失败时返回false
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
        "success": true
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
  <md-td>400</md-td>
  <md-td>1161093</md-td>
  <md-td>Transit task failed.</md-td>
  <md-td>流转任务时系统报错，请联系管理员</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161095</md-td>
  <md-td>The task was not found, unable to operate.</md-td>
  <md-td>没有找到需要流转的任务，请检查pre_hire_id和task_code传参是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161096</md-td>
  <md-td>Task status error, unable to operate.</md-td>
  <md-td>任务状态不满足当前流转类型，不允许流转</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161097</md-td>
  <md-td>Permission denied, please contact the administrator.</md-td>
  <md-td>无权限，请先确认是否已申请`入职常规任务的通用流转`的应用权限</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161098</md-td>
  <md-td>The values of the required fields in the form are missing, and the task can not be submitted.</md-td>
  <md-td>任务表单配置的必填字段没有填写，需要填写之后再流转</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161116</md-td>
  <md-td>A conflict occurred as multiple people are operating at the same time. Please refresh the page and try again later.</md-td>
  <md-td>多人同时操作发生冲突，请稍后刷新页面后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161129</md-td>
  <md-td>Unable to perform this action as this pre-hire isn't in the "To be onboarded" stage.</md-td>
  <md-td>该待入职人员流程不处于进行中，无法进行此操作，请检查待入职人员的入职状态是否处于进行中</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161142</md-td>
  <md-td>Current task not support to submit.</md-td>
  <md-td>当前任务不支持提交，请检查task_code传参，参数不支持传3（创建SSO任务），4（签到任务），9（电子签任务）</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




