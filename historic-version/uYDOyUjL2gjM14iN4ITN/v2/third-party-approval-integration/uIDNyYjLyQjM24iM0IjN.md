---
title: "三方审批定义创建"
fullPath: "/ukTMukTMukTM/uIDNyYjLyQjM24iM0IjN"
updateTime: "1705571166000"
---

# 三方审批定义创建
:::html
<md-alert type="error">
为了更好地提升接口文档的的易理解性，我们对文档进行了升级，请尽快迁移至[新版本>>](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/approval-v4/external_approval/create)
</md-alert>
:::
审批定义是审批的描述，包括审批名称、图标、描述等基础信息。创建好审批定义，用户就可以在审批应用的发起页中看到审批，如果用户点击发起，则会跳转到配置的发起三方系统地址去发起审批。
<br>
另外，审批定义还配置了审批操作时的回调地址：审批人在待审批列表中进行【同意】【拒绝】操作时，审批中心会调用回调地址通知三方系统。


:::html
<md-alert type="tip">
注意，审批中心不负责审批流程的流转，只负责展示、操作、消息通知。因此审批定义创建时没有审批流程的信息。
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
      <md-td>https://www.feishu.cn/approval/openapi/v3/external/approval/create</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>

   <md-tr>
     <md-th>支持的应用类型</md-th>
      <md-td>
	  <md-app-support types="custom,isv"></md-app-support>
      </md-td>
   </md-tr>


    
    
    <md-tr>
      <md-th>
 权限要求
 <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
</md-th>
      <md-td>
<md-perm name="approval:approval:readonly" desc="访问审批应用" support_app_types="custom,isv" tags="">访问审批应用</md-perm>
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
:::html
<md-table>
  <md-thead>
      <tr>
      <md-th style="width: 21%;">名称</md-th>
      <md-th style="width: 15%;">类型</md-th>
      <md-th>说明</md-th>
      <md-th style="width: 15%;">示例</md-th>
      </tr>
  </md-thead>
  <md-tbody>





<md-tr>
	<md-td>
	<md-text type="field-name" >approval_name</md-text>
<md-tag mode="block" type="field-required" >必选</md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
  
	<md-td>
	
审批定义名称， 创建审批定义返回的值，表示该实例属于哪个流程；该字段会影响到列表中该实例的标题，标题取自对应定义的 name 字段。
     

</md-td>
  
  <md-td>
	@i18n@1
	</md-td>
</md-tr>


<md-tr>
	<md-td>
	<md-text type="field-name" >approval_code</md-text>
<md-tag mode="block" type="field-required" >必选</md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	审批定义 code，用户自定义，定义的唯一标识，如果不存在该 code，则创建，否则更新
	</md-td>
  <md-td>
	permission_test
	</md-td>
</md-tr>

    
<md-tr>
	<md-td>
	<md-text type="field-name" >group_code</md-text>
<md-tag mode="block" type="field-required" >必选</md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	审批定义所属审批分组，用户自定义；
      <br>
如果group_code当前不存在，则会新建审批分组；
      <br>
      如果group_code已经存在，则会使用group_name更新审批分组名称
	</md-td>
  <md-td>
	work_group
	</md-td>
</md-tr>


<md-tr>
	<md-td>
	<md-text type="field-name" >group_name</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
      
分组名称，值的格式是 i18n key，文案放在 i18n_resource；<br>
如果是 group_code 当前不存在，则该 group_name 必填，否则，如果填写了则会更新分组名称，不填则不更新分组名称；<br>
审批发起页 审批定义的分组名称来自该字段

	</md-td>
  <md-td>
	@i18n@2
	</md-td>
</md-tr>
    

<md-tr>
	<md-td>
	<md-text type="field-name" >description</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
      
审批定义的说明，值的格式是 i18n key，文案放在 i18n_resource；<br>
审批发起页 审批定义的说明内容来自该字段

	</md-td>
  <md-td>
	@i18n@2
	</md-td>
</md-tr>
    
    
<md-tr>
	<md-td>
	<md-text type="field-name" >external
  <md-tag mode="block" type="field-required" >必选</md-tag>
      </md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >map</md-text>
	</md-td>
	<md-td>
	三方审批相关
	</md-td>
</md-tr>
    
    
<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >biz_name</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>列表中用于提示审批来自哪里，i18n key， 注意不需要“来自”前缀，审批中心会拼上前缀
	</md-td>
  <md-td>
	@i18n@3
	</md-td>
</md-tr>
    
<md-tr>
	<md-td>
&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" > biz_type</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	审批定义业务类别
	</md-td>
  <md-td>
	permission
	</md-td>
</md-tr>
<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟ </span>&nbsp;<md-text type="field-name" >create_link_mobile
  <md-tag mode="block" type="field-required" >必选</md-tag> 
  </md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>移动端发起链接，如果设置了该链接，则会在移动端审批发起页展示该审批，用户点击后会跳转到该链接进行发起；
      <br>
如果不填，则在mobile端不显示该审批
	</md-td>
  <md-td>
	 https://applink.feishu.cn/client/mini_program/open?appId=cli_9c90fc38e07a9101&path=pages/approval-form/index?id=9999
	</md-td>
</md-tr>
<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >     create_link_pc </md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>PC端发起链接，如果设置了该链接，则会在PC端审批发起页展示该审批，用户点击后会跳转到该链接进行发起；<br>
如果不填，则在PC端不显示该审批；
      
	</md-td>
  <md-td>
	 https://applink.feishu.cn/client/mini_program/open?mode=appCenter&appId=cli_9c90fc38e07a9101&path=pc/pages/create-form/index?id=9999
	</md-td>
</md-tr>
<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >support_pc</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >bool</md-text>
	</md-td>
	<md-td>
审批实例、审批任务、审批抄送是否要在PC端展示，如果为 true，则PC端列表会展示该定义下的实例信息，否则，不展示<br>
      
  
	</md-td>
  <md-td>
	true
	</md-td>
</md-tr>
<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >
      support_mobile</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >bool</md-text>
	</md-td>
	<md-td>
审批实例、审批任务、审批抄送是否要在移动端展示，如果为 true，则移动端列表会展示该定义下的实例信息，否则，不展示；<br>
support_pc和support_mobile不可都为false，否则不展示<br>
      

	</md-td>
  <md-td>
	true
	</md-td>
</md-tr>
<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >
      support_batch_read</md-text>
	</md-td>
	<md-text type="field-type" >bool</md-text>
	<md-td>
	是否支持批量已读
	</md-td>
  <md-td>
	true
	</md-td>
</md-tr>
   <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >
      enable_mark_readed</md-text>
	</md-td>
	<md-text type="field-type" >bool</md-text>
	<md-td>
	是否支持标注可读
	</md-td>
     <md-td>
	true
	</md-td>
</md-tr>
    <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >
      enable_quick_operate</md-text>
	</md-td>
	<md-text type="field-type" >bool</md-text>
	<md-td>
	是否支持快速操作
	</md-td>
      <md-td>
	true
	</md-td>
</md-tr>
 
<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >
      allow_batch_operate</md-text>
	</md-td>
	<md-text type="field-type" >bool</md-text>
	<md-td>
	是否支持批量审批
	</md-td>
      <md-td>
	true
	</md-td>
</md-tr>
 
  <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >
      action_callback_url</md-text>
	</md-td>
	<md-text type="field-type" >string</md-text>
	<md-td>
	三方系统的操作回调 url，【待审批】列表的任务审批人点同意或拒绝操作后，审批中心调用该地址通知三方系统，回调地址相关信息可参见：https://open.feishu.cn/document/ukTMukTMukTM/ukjNyYjL5YjM24SO2IjN/quick-approval-callback

	</md-td>
    <md-td>
	  http://www.feishu.cn/approval/openapi/instanceOperate

	</md-td>
</md-tr>   
  <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >
      action_callback_token</md-text>
	</md-td>
	<md-text type="field-type" >string</md-text>
	<md-td>
	回调时带的 token， 用于业务系统验证请求来自审批,具体参考 [开放平台文档](/ssl:ttdoc/ukTMukTMukTM/uUTNz4SN1MjL1UzM)
	</md-td>
    <md-td>
	sdjkljkx9lsadf110
	</md-td>
</md-tr>  
      <md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >
      action_callback_key</md-text>
	</md-td>
	<md-text type="field-type" >string</md-text>
	<md-td>
	请求参数加密密钥，如果配置了该参数，则会对请求参数进行加密，业务需要对请求进行解密，加解密算法参考[关联外部选项说明](/ssl:ttdoc/ukTMukTMukTM/uADM4QjLwADO04CMwgDN) 
	</md-td>
        <md-td>
	gfdqedvsadfgfsd
	</md-td>
</md-tr>  


<md-tr>
	<md-td>
	<md-text type="field-name" >viewers</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >list</md-text>
	</md-td>
	<md-td>
	可见人列表，可通知配置多个可见人(**最大支持长度200**)，只有在配置的范围内用户可以在审批发起也看到该审批，默认不传，则是任何人不可见
	</md-td>
</md-tr>
    

<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >viewer_type</md-text>
<md-tag mode="block" type="field-required" ></md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	可见人类型  
**可选值有：**
- `TENANT`：租户内可见
- `DEPARTMENT`：指定部门
- `USER`：指定用户
- `NONE`：任何人都不可见
	</md-td>
  <md-td>
	USER
	</md-td>
</md-tr>

    
<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >viewer_id</md-text>
      <md-tag mode="block" type="field-required" ></md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	可见人 ID，如果 view_type 是 TENANT 和 NONE, viewer_id 可为空;<br> 如果 view_type 为DEPARTMENT，viewer_id 是 open_department_id;<br>如果 view_type 是 USER，viewer_id 为 user_id

	</md-td>
  <md-td>
	19a294c2

	</md-td>
</md-tr>
    

<md-tr>
	<md-td>
	<md-text type="field-name" >i18n_resources</md-text>
      <md-tag mode="block" type="field-required" >必选</md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >list</md-text>
	</md-td>
	<md-td>
	国际化文案
	</md-td>
</md-tr>
    

<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >locale</md-text>
<md-tag mode="block" type="field-required" >必选</md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	语言
**可选值有：**
- `zh-CN`：中文
- `en-US`：英文
- `ja-JP`：日文
	</md-td>
  <md-td>
	zh-CN

	</md-td>
</md-tr>
   

<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >is_default</md-text>
<md-tag mode="block" type="field-required" >必选</md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >bool</md-text>
	</md-td>
	<md-td>
	是否默认语言，默认语言需要包含所有key，非默认语言如果key不存在会使用默认语言代替

	</md-td>
  <md-td>
	true

	</md-td>
</md-tr>
    

<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >texts</md-text>
<md-tag mode="block" type="field-required" >必选</md-tag>
	</md-td>
	<md-td>
	<md-text type="field-type" >map</md-text>
	</md-td>
	<md-td>
	文案 key, value,  i18n key 以  **@i18n@** 开头；<br>
该字段主要用于做国际化，允许用户同时传多个语言的文案，审批中心会根据用户当前的语音环境使用对应的文案，如果没有传用户当前的语音环境文案，则会使用默认的语言文案。
	</md-td>
  <md-td>
	
{<br>
   "@i18n@1": "权限申请",  <br>    "@i18n@2": "OA审批",<br>
   "@i18n@3": "Permission"<br>
}
	</md-td>
</md-tr>

  </md-tbody>
</md-table>
:::

### 请求体示例

```json
{
    "approval_name": "@i18n@1",
    "approval_code": "permission_test",
    "group_code": "work_group",
    "group_name": "@i18n@2",
    "external": {
        "create_link_pc": "https://applink.feishu.cn/client/mini_program/open?mode=appCenter&appId=cli_9c90fc38e07a9101&path=pc%2Fpages%2Fcreate-form%2Findex%3Fid%3D9999",
        "create_link_mobile": "https://applink.feishu.cn/client/mini_program/open?appId=cli_9c90fc38e07a9101&path=pages%2Fapproval-form%2Findex%3Fid%3D9999",
        "support_pc": true,
        "support_mobile": true,
        "support_batch_read": false,
        "action_callback_url":"http://feishu.cn/approval/openapi/operate",
        "action_callback_token":"sdjkljkx9lsadf110",
        "action_callback_key":"gfdqedvsadfgfsd",
        "enable_mark_readed": false,
        "enable_quick_operate": false,
        "allow_batch_operate": false,
        "key": "",
        "token":""
    },
    "i18n_resources":[
     {
        "locale":"zh-CN",
        "is_default":true,
         "texts":{
            "@i18n@1":"people",
             "@i18n@2":"hr",
             "@i18n@3":"HR"
         }
      }
    ],
    "viewers": [
        {
            "viewer_type": "TENANT"
        }
    ]
}
```

## 响应

### 响应体
:::html
<md-table>
  <md-thead>
      <tr>
      <md-th>名称</md-th>
      <md-th>类型</md-th>
      <md-th>描述</md-th>
      </tr>
  </md-thead>
  <md-tbody>

<md-tr>
	<md-td>
	<md-text type="field-name" >code</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >int</md-text>
	</md-td>
	<md-td>
	错误码，非0表示失败
	</md-td>
</md-tr>
    
    
<md-tr>
	<md-td>
	<md-text type="field-name" >msg</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	返回码的描述
	</md-td>
</md-tr>
    

<md-tr>
	<md-td>
	<md-text type="field-name" >data</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >map</md-text>
	</md-td>
	<md-td>
	返回业务信息
	</md-td>
</md-tr>
    

<md-tr>
	<md-td>
	&emsp;<span style="color: #8F959E">∟</span>&nbsp;<md-text type="field-name" >approval_code</md-text>
	</md-td>
	<md-td>
	<md-text type="field-type" >string</md-text>
	</md-td>
	<md-td>
	审批定义 Code，用于发起实例
	</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::
### 响应体示例

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "approval_code": "C30381C8-7A5F-4717-A9CF-C233BF0202D4"
    }
}
```
