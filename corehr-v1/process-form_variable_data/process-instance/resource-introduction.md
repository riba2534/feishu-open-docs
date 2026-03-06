---
title: "流程实例资源介绍"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/process-form_variable_data/process-instance/resource-introduction"
updateTime: "1734434181000"
---

# 资源介绍

## 资源定义

流程实例：是指用户在业务功能或者飞书人事的审批中心发起的具体流程，process_id 是其唯一标识。

流程定义：是指管理员在设置侧配置的流程，类似流程模板，flow_definition_id 是其唯一标识。用户发起的流程是按照对应的流程定义的配置生成。

## 字段说明

:::html
<md-dt-table>
  <md-dt-thead>
      <md-dt-tr>
      <md-dt-th style="width: 30%;">名称</md-dt-th>
      <md-dt-th style="width: 30%;">类型</md-dt-th>
      <md-dt-th style="width: 40%;">描述</md-dt-th>
      </md-dt-tr>
  </md-dt-thead>
  
  <md-dt-tbody>
    
	<md-dt-tr>
        <md-dt-td>process_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>流程实例ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr>
        <md-dt-td>status</md-dt-td>
        <md-dt-td>int</md-dt-td>
        <md-dt-td>
流程状态
          
**可选值有：**
          
- `1`：进行中
- `2`：拒绝
- `4`：撤回
- `8`：撤销
- `9`：已完成
      </md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr>
        <md-dt-td>flow_template_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>业务类型ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="0">
        <md-dt-td>flow_template_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>业务类型名称</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr>
        <md-dt-td>flow_definition_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>流程定义ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="0">
        <md-dt-td>flow_definition_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>流程定义名称</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr>
        <md-dt-td>initiator_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>流程发起人ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="0">
        <md-dt-td>initiator_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>流程发起人姓名</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr>
        <md-dt-td>create_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>流程发起时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    <md-dt-tr>
        <md-dt-td>complete_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>流程结束时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr level="0">
        <md-dt-td>start_links</md-dt-td>
        <md-dt-td>process_link</md-dt-td>
        <md-dt-td>发起单据地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>web_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>web端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>pc_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书pc端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>mobile_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书移动端单据详情页地址</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr level="0">
        <md-dt-td>abstracts</md-dt-td>
        <md-dt-td>process_abstract_item[]</md-dt-td>
        <md-dt-td>流程摘要，会随着流程流转发生变化</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>摘要标题</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>value</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>摘要值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr level="0">
        <md-dt-td>todos</md-dt-td>
        <md-dt-td>process_todo_item[]</md-dt-td>
        <md-dt-td>待办列表</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>approver_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>单据ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>type</md-dt-td>
        <md-dt-td>int</md-dt-td>
        <md-dt-td>
单据类型
          
**可选值有：**
          
- `1`：审批单
- `5`：表单
      </md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>links</md-dt-td>
        <md-dt-td>process_link</md-dt-td>
        <md-dt-td>发起单据地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>web_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>web端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>pc_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书pc端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>mobile_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书移动端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>operator_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>操作人ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>operator_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>操作人姓名</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>节点名称</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>create_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>创建时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_definition_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>节点定义ID（注：在回退场景，同一个节点会对应多个节点实例）</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr level="0">
        <md-dt-td>cc_list</md-dt-td>
        <md-dt-td>process_cc_item[]</md-dt-td>
        <md-dt-td>抄送列表</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>approver_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>单据ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>links</md-dt-td>
        <md-dt-td>process_link</md-dt-td>
        <md-dt-td>发起单据地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>web_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>web端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>pc_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书pc端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>mobile_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书移动端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>operator_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>操作人ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>operator_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>操作人姓名</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>节点名称</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>create_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>创建时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_definition_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>节点定义ID（注：在回退场景，同一个节点会对应多个节点实例）</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr level="0">
        <md-dt-td>done_list</md-dt-td>
        <md-dt-td>process_done_item[]</md-dt-td>
        <md-dt-td>已办列表</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>approver_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>单据ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>type</md-dt-td>
        <md-dt-td>int</md-dt-td>
        <md-dt-td>
单据类型
          
**可选值有：**
          
- `1`：审批单
- `5`：表单
      </md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>status</md-dt-td>
        <md-dt-td>int</md-dt-td>
        <md-dt-td>
单据状态
          
**可选值有：**
          
- `3`：已完成
- `2`：拒绝
- `4`：取消
      </md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>links</md-dt-td>
        <md-dt-td>process_link</md-dt-td>
        <md-dt-td>发起单据地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>web_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>web端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>pc_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书pc端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>mobile_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书移动端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>operator_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>操作人ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>operator_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>操作人姓名</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>节点名称</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>create_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>创建时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>complete_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>完成时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_definition_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>节点定义ID（注：在回退场景，同一个节点会对应多个节点实例）</md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr>
        <md-dt-td>properties</md-dt-td>
        <md-dt-td>int</md-dt-td>
        <md-dt-td>
普通流程或撤销流程等
          
**可选值有：**
          
- `1`：普通流程
- `2`：撤销流程
      </md-dt-td>
	</md-dt-tr>
    
    <md-dt-tr level="0">
        <md-dt-td>system_todos</md-dt-td>
        <md-dt-td>process_system_todo_item[]</md-dt-td>
        <md-dt-td>系统待办列表</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>approver_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>单据ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>type</md-dt-td>
        <md-dt-td>int</md-dt-td>
        <md-dt-td>
单据类型
          
**可选值有：**
          
- `1`：审批单
- `5`：表单
      </md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>links</md-dt-td>
        <md-dt-td>process_link</md-dt-td>
        <md-dt-td>发起单据地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>web_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>web端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>pc_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书pc端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>mobile_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书移动端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>operator_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>操作人姓名</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>节点名称</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>create_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>创建时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_definition_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>节点定义ID（注：在回退场景，同一个节点会对应多个节点实例）</md-dt-td>
	</md-dt-tr>

        <md-dt-tr level="0">
        <md-dt-td>system_done_list</md-dt-td>
        <md-dt-td>process_system_done_item[]</md-dt-td>
        <md-dt-td>系统已办列表</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>approver_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>单据ID</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>type</md-dt-td>
        <md-dt-td>int</md-dt-td>
        <md-dt-td>
单据类型
          
**可选值有：**
          
- `1`：审批单
- `5`：表单
      </md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>status</md-dt-td>
        <md-dt-td>int</md-dt-td>
        <md-dt-td>
单据状态
          
**可选值有：**
          
- `3`：已完成
- `2`：拒绝
- `4`：取消
      </md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>links</md-dt-td>
        <md-dt-td>process_link</md-dt-td>
        <md-dt-td>发起单据地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>web_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>web端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>pc_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书pc端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>mobile_link</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>飞书移动端单据详情页地址</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>operator_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>操作人姓名</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_name</md-dt-td>
        <md-dt-td>dataengine_i18n</md-dt-td>
        <md-dt-td>节点名称</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>zh_cn</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>中文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="2">
        <md-dt-td>en_us</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>英文值</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>create_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>创建时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>complete_time</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>完成时间，Unix毫秒时间戳</md-dt-td>
	</md-dt-tr>
    <md-dt-tr level="1">
        <md-dt-td>node_definition_id</md-dt-td>
        <md-dt-td>string</md-dt-td>
        <md-dt-td>节点定义ID（注：在回退场景，同一个节点会对应多个节点实例）</md-dt-td>
	</md-dt-tr>
    
</md-dt-tbody>
</md-dt-table>
:::

## 数据示例


```json 
{
    "process_id": "7278949005675988535",
    "status": 1,
    "flow_template_id": "leave",
    "flow_template_name": {
        "zh_cn": "中文",
        "en_us": "English"
    },
    "flow_definition_id": "people_6961286846093788680_7081951411982077732",
    "flow_definition_name": {
        "zh_cn": "中文",
        "en_us": "English"
    },
    "initiator_id": "7124991993901827628",
    "initiator_name": {
        "zh_cn": "中文",
        "en_us": "English"
    },
    "create_time": "1694769814036",
    "complete_time": "1694769814036",
    "start_links": {
        "web_link": "http://xxxx.com/xxx/xxx?a=b",
        "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
        "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
    },
    "abstracts": [
        {
            "name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "value": {
                "zh_cn": "中文",
                "en_us": "English"
            }
        }
    ],
    "todos": [
        {
            "approver_id": "7278949005675988535",
            "type": 1,
            "links": {
                "web_link": "http://xxxx.com/xxx/xxx?a=b",
                "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
            },
            "operator_id": "7124991993901827628",
            "operator_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "node_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "create_time": "1694769814036",
            "node_definition_id": "approval_d25b5eddfef"
        }
    ],
    "cc_list": [
        {
            "approver_id": "7278949005675988535",
            "links": {
                "web_link": "http://xxxx.com/xxx/xxx?a=b",
                "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
            },
            "operator_id": "7124991993901827628",
            "operator_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "node_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "create_time": "1694769814036",
            "node_definition_id": "approval_d25b5eddfef"
        }
    ],
    "done_list": [
        {
            "approver_id": "7278949005675988535",
            "type": 1,
            "status": 3,
            "links": {
                "web_link": "http://xxxx.com/xxx/xxx?a=b",
                "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
            },
            "operator_id": "7124991993901827628",
            "operator_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "node_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "create_time": "1694769814036",
            "complete_time": "1694769814036",
            "node_definition_id": "approval_d25b5eddfef"
        }
    ],
    "properties": 1,
    "system_todos": [
        {
            "approver_id": "7278949005675988535",
            "type": 1,
            "links": {
                "web_link": "http://xxxx.com/xxx/xxx?a=b",
                "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
            },
            "operator_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "node_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "create_time": "1694769814036",
            "node_definition_id": "approval_d25b5eddfef"
        }
    ],
    "system_done_list": [
        {
            "approver_id": "7278949005675988535",
            "type": 1,
            "status": 3,
            "links": {
                "web_link": "http://xxxx.com/xxx/xxx?a=b",
                "pc_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx",
                "mobile_link": "https://applink.feishu.cn/client/mini_program/open?appId=xxx"
            },
            "operator_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "node_name": {
                "zh_cn": "中文",
                "en_us": "English"
            },
            "create_time": "1694769814036",
            "complete_time": "1694769814036",
            "node_definition_id": "approval_d25b5eddfef"
        }
    ]
}
``` 


