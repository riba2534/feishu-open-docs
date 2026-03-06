---
title: "流程概述"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/overview"
updateTime: "1734434138000"
---

# 概述

## 业务介绍

飞书People 流程是飞书 People 系统的流程管理平台，提供业务表单设计、流程搭建、流程管理等能力，帮助企业提升业务运转效率，支持异动、离职、请假、出差等企业内部审批流程

流程的开放接口提供了一系列安全、可靠的 API 接口和事件，来方便企业对流程信息进行查询和操作，通过 API 你可以实现以下功能：
- 流程相关信息查询：包括流程实例信息、审批任务信息、流程中的单据数据等信息查询
- 流程动态监控：可通过事件监听流程实例、流程节点、审批任务等状态变更动态
- 对流程进行操作：包括通过/拒绝审批任务等

### 接入流程
:::html
<md-table>
  <md-thead>
    <md-tr>
      <md-th style="width:20%">编号</md-th>
      <md-th style="width:40%">步骤</md-th>
	  <md-th style="width:40%">介绍</md-th>
	</md-tr>
  </md-thead>
  <md-tbody>
	<md-tr>
		<md-td>1</md-td>
		<md-td>创建一个应用</md-td>
		<md-td>如需创建企业自建应用，可参考[企业自建应用开发流程](/ssl:ttdoc/home/introduction-to-custom-app-development/self-built-application-development-process)，如需创建应用商店应用，可参考 [开发商店应用](/ssl:ttdoc/uMzNwEjLzcDMx4yM3ATM/uYzNwEjL2cDMx4iN3ATM)。</md-td>
	</md-tr>
	<md-tr>
		<md-td>2</md-td>
		<md-td>调用API，对流程进行操作</md-td>
		<md-td>调用API前，你需要先获取访问凭证并开启对应的权限，详情参见 [如何调用服务端API](/ssl:ttdoc/ukTMukTMukTM/uITNz4iM1MjLyUzM)。</md-td>
	</md-tr>
	<md-tr>
		<md-td>3</md-td>
		<md-td>监听事件，获知流程的变化</md-td>
		<md-td>监听事件前，你需要先申请相应的权限，详情参见 [审批事件监听开发指南](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-approver/events/function-introduction)。</md-td>
	</md-tr>
  </md-tbody>
</md-table>
:::

## 资源介绍

资源的定义如下：

:::html
<md-table>
  <md-thead>
	<md-tr>
		<md-th style="width:30%">资源</md-th>
		<md-th style="width:70%">资源定义</md-th>
	</md-tr>
  </md-thead>
  <md-tbody>
	<md-tr>
		<md-td>[流程实例](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/process-instance/resource-introduction)</md-td>
		<md-td>用户在业务功能或者飞书人事的审批中心发起的具体流程，process_id 是其唯一标识。</md-td>
	</md-tr>
  	<md-tr>
		<md-td>[审批任务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/approver-task/resource-introduce)</md-td>
		<md-td>审批任务依赖于流程节点存在，每一个流程节点可能包含一个或多个审批任务，每一个任务表明当前流程节点的审批人是谁</md-td>
	</md-tr>
  </md-tbody>
</md-table>
:::

以下将详细介绍每个资源的字段、方法、事件。

### 资源：流程实例

查看资源 [字段及示例](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/process-instance/resource-introduction)

#### 方法列表

:::html
<md-table>
  <md-thead>
	<md-tr>
 		<md-th style="width:49%">方法 (API)</md-th>
		<md-th style="width:30%">权限要求</md-th>
  		<md-th style="width:21%">访问凭证</md-th>
	</md-tr>
  </md-thead>
  <md-tbody>
    <md-tr>
		<md-td>[撤回流程](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process_withdraw/update)<br>`PUT`/open-apis/corehr/v2/process_withdraw/:process_id</md-td>
		<md-td><md-perm name="corehr:process.instance:write" desc="通过/拒绝审批任务" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
    <md-tr>
		<md-td>[撤销流程](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process_revoke/update)<br>`PUT`/open-apis/corehr/v2/process_revoke/:process_id</md-td>
		<md-td><md-perm name="corehr:process.instance:write" desc="通过/拒绝审批任务" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
	<md-tr>
		<md-td>[查询流程实例列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/list)<br>`GET`/open-apis/corehr/v2/processes</md-td>
		<md-td><md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
	<md-tr>
		<md-td>[获取单个流程详情](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/get)<br>`GET`/open-apis/corehr/v2/processes/:process_id</md-td>
		<md-td>
          <md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv">
          </md-perm>
      </md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
    <md-tr>
		<md-td>[获取流程表单数据](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-form_variable_data/get)<br>`GET`/open-apis/corehr/v2/processes/:process_id/form_variable_data</md-td>
		<md-td>
          <md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv">
          </md-perm>
      </md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
  </md-tbody>
</md-table>
:::                                                 

#### 事件列表

:::html
<md-table>
  <md-thead>
	<md-tr>
 		<md-th style="width:30%">事件（event）</md-th>
		<md-th style="width:30%">权限要求</md-th>
  		<md-th style="width:40%">触发时机</md-th>
	</md-tr>
  </md-thead>
  <md-tbody>
    <md-tr>
		<md-td>[流程实例状态变化](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-status/events/update) </md-td>
		<md-td><md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td>流程实例状态变化时会触发该事件</md-td>
	</md-tr>
	<md-tr>
		<md-td>[流程实例信息变更](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process/events/updated)</md-td>
		<md-td><md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td>流程中有审批人操作、流程数据更新、流程状态变化时会触发该事件</md-td>
	</md-tr>
    <md-tr>
		<md-td>[流程节点状态变更](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-node/events/updated)</md-td>
		<md-td><md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td>流程中节点状态变化时会触发该事件</md-td>
	</md-tr>
  </md-tbody>
</md-table>
:::

### 资源：审批任务

查看资源 [字段及示例](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/approver-task/resource-introduce)

#### 方法列表

:::html
<md-table>
  <md-thead>
	<md-tr>
 		<md-th style="width:49%">方法 (API)</md-th>
		<md-th style="width:30%">权限要求</md-th>
  		<md-th style="width:21%">访问凭证</md-th>
	</md-tr>
  </md-thead>
  <md-tbody>
	<md-tr>
		<md-td>[通过/拒绝审批任务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-approver/update)<br>`PUT`/open-apis/corehr/v2/processes/:process_id/approvers/:approver_id </md-td>
		<md-td><md-perm name="corehr:process.instance:write" desc="通过/拒绝审批任务" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
    <md-tr>
		<md-td>[加签审批任务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-extra/update)<br>`PUT`/open-apis/corehr/v2/processes/:process_id/extra </md-td>
		<md-td><md-perm name="corehr:process.instance:write" desc="通过/拒绝审批任务" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
    <md-tr>
		<md-td>[转交审批任务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-transfer/update)<br>`PUT`/open-apis/corehr/v2/processes/:process_id/transfer </md-td>
		<md-td><md-perm name="corehr:process.instance:write" desc="通过/拒绝审批任务" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
    <md-tr>
		<md-td>[获取指定人员审批任务列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/approver/list)<br>`GET`/open-apis/corehr/v2/approvers </md-td>
		<md-td><md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td><md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag></md-td>
	</md-tr>
  </md-tbody>
</md-table>
:::

#### 事件列表

:::html
<md-table>
  <md-thead>
	<md-tr>
 		<md-th style="width:30%">事件（event）</md-th>
		<md-th style="width:30%">权限要求</md-th>
  		<md-th style="width:40%">触发时机</md-th>
	</md-tr>
  </md-thead>
  <md-tbody>
	<md-tr>
		<md-td>[审批任务状态变更](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-approver/events/updated)</md-td>
		<md-td><md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td>单个审批任务状态变化时会触发该事件</md-td>
	</md-tr>
    <md-tr>
		<md-td>[抄送单据状态变更](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/process-cc/events/updated)</md-td>
		<md-td><md-perm name="corehr:process:read" desc="获取流程数据" support_app_types="custom,isv"></md-perm></md-td>
  		<md-td>生成抄送单据后会触发该事件</md-td>
	</md-tr>
  </md-tbody>
</md-table>
:::

