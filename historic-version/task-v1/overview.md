---
title: "任务概述"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/task-v1/overview"
updateTime: "1731048954000"
---

# 任务概述
:::html
<md-alert type="warn">**注意：** 请使用v2的任务接口[任务v2接口功能概述](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/task-v2/overview)，支持任务、清单、自定义分组、评论、自定义字段、附件等功能。本套接口即将废弃。</md-alert>
:::
## 概述
飞书任务是一款轻量级的任务管理工具，拥有强大的协作能力。我们可以轻松地在会话等场景中快捷创建任务，也可以将感兴趣的任务分享给成员，或者关注一些感兴趣的任务。我们还可以围绕任务进行讨论，可以针对任务进行评论等。
## GIF 演示
### 创建任务
![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/ea56c9f12c665555d81334643e75d75f_xUJwjeu5qA.gif?height=474&lazyload=true&width=1110)
### 给任务添加提醒时间、关注人、协作者
![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/a6967a914d4ab84f9ffc632fa21c8458_rJuuOR1SxQ.gif?height=474&lazyload=true&width=1110)

## 如何使用任务 API

### 1、为应用申请调用权限
若应用尚未申请任务 API 权限，需在开发者后台增加权限申请并提交审核。
企业自建应用需要企业管理员在管理后台审核通过；应用商店应用需要经过平台管理员审核、企业管理员在应用市场安装或升级。

权限描述                       | 作用                               
| ---- | ------------------------- | ----------------------------------- |
| 查看飞书任务详情 | 仅获取查询任务详情的权限           
| 查看、创建、编辑和删除飞书任务 | 获取增删改查任务的权限
### 2、API鉴权
当前任务 API 支持 tenant_access_token 和 user_access_token 鉴权方式。
类型                       | tenant_access_token	      |    user_access_token                     
| ---- | ------------------------- | ----------------------------------- |-------- |
| 描述 | 以应用身份调用任务接口，可对应用创建的任务数据进行增删改查，此时任务数据的owner为应用  | 以用户身份调用任务接口，等价于用户直接操作飞书任务中心        
| 使用场景 | 应用需要有属于自己的任务数据时，使用此token <br> 例如：<br>某项目管理应用中，需要为项目成员创建任务，任务owner为应用本身，可通过tenant_access_token调用任务接口数据 | 用户开发第三方任务应用，使用飞书的身份信息和飞书任务的能力，但希望提供与飞书不同的用户界面。
| 获取方式 | 企业安装应用后，应用可获取tenant_access_token <br> [获取应用认证身份访问凭证](/ssl:ttdoc/ukTMukTMukTM/uMTNz4yM1MjLzUzM) | 企业安装应用后，引导用户登录飞书，然后在用户授权下获取user_access_token <br> [获取用户认证身份访问凭证](/ssl:ttdoc/ukTMukTMukTM/uMTNz4yM1MjLzUzM) 
| 是否需要开启机器人能力 | 是 | 否

### 3、创建任务
通过[创建任务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/task/create)接口可以应用的身份创建相应的任务，若想在自己的飞书-任务中看到该任务，需通过[新增执行者](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/task-collaborator/create)或[新增关注人](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/task-follower/create)接口添加自己为执行者或关注人。

## 任务支持AppLink
:::html
<md-alert type="tip">
任务支持 [AppLink](/ssl:ttdoc/uYjL24iN/ucjN1UjL3YTN14yN2UTN)，可通过applink直接打开 Todo 详情页和 Todo Tab。
</md-alert>
:::

:::html
<md-table> 
  <md-thead> 
    <md-tr> 
      <md-th style="width: 10%;">页面/场景</md-th>  
      <md-th style="width: 20%;">path</md-th>  
      <md-th style="width: 40%;">参数</md-th> 
      <md-th>备注</md-th> 
    </md-tr> 
  </md-thead>  
  <md-tbody> 
    <md-tr> 
      <md-td>任务详情</md-td>  
      <md-td>/client/todo/detail</md-td>  
      <md-td>
- `guid: string` **[required]** 
        
- ` authscene?:``1|2`<br>*MESSAGE* = 1;<br>*PANO* = 2;<br>传参使用数字，eg：xxxxx?authscene=2
        
- `authid?: string`
        
- `navigateStyle?: 'push'|'present'`
        
`?` 后缀的参数名，表示可选参数    
      </md-td> 
      <md-td>打开 todo 详情<br>示例：[https://applink.feishu.cn/client/todo/detail?guid=todoGuidStrin](https://applink.feishu.cn/client/todo/detail?guid=todoGuidStrin)<br><br>`navigateStyle` <br>仅移动端使用，用于控制进入详情页时的UI样式，「push」为从右至左，「present」为从下至上</md-td>  
    </md-tr>  
    <md-tr> 
      <md-td>任务中心</md-td>  
      <md-td>/client/todo/open</md-td>  
      <md-td>无</md-td> 
      <md-td>切换至 Todo Tab <br> 示例：[https://applink.feishu.cn/client/todo/open](https://applink.feishu.cn/client/todo/open)</md-td> 
    </md-tr> 
  </md-tbody> 
</md-table>
:::
## 资源 ID 字段说明
:::html
<md-table> 
  <md-thead> 
    <md-tr> 
      <md-th style="width: 10%;">ID 名称</md-th>  
      <md-th style="width: 20%;">简介</md-th>  
      <md-th style="width: 20%;">自定义方式</md-th>  
      <md-th style="width: 40%;">获取方式</md-th> 
    </md-tr> 
  </md-thead>  
  <md-tbody> 
    <md-tr> 
      <md-td>task_id</md-td>  
      <md-td>唯一标识一个任务的 ID</md-td>  
      <md-td>不可自定义，由服务器生成</md-td>  
      <md-td>
        接口获取：[创建任务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/task/create)时返回该字段
      </md-td> 
    </md-tr>  
    <md-tr> 
      <md-td>reminder_id</md-td>  
      <md-td>唯一标识一个任务提醒时间的 ID</md-td>  
      <md-td>不可自定义，由服务器生成</md-td>  
      <md-td>
        接口获取：用 task_id 从[查询提醒时间列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/task-reminder/list)接口获取
      </md-td> 
    </md-tr>
    <md-tr> 
      <md-td>follow_id</md-td>  
      <md-td>唯一标识一个任务关注人的 ID</md-td>  
      <md-td>不可自定义，由服务器生成</md-td>  
      <md-td>
        接口获取：用 task_id 从[获取关注人列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/task-follower/list)接口获取
      </md-td> 
    </md-tr> 
    <md-tr> 
      <md-td>collaborator_id</md-td> 
      <md-td>唯一标识一个任务执行者的 ID</md-td> 
      <md-td>不可自定义，由服务器生成</md-td>  
      <md-td>
        接口获取：用 task_id 从[获取执行者列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/task-collaborator/list)接口获取
      </md-td> 
    </md-tr> 
  </md-tbody> 
</md-table>
:::