---
title: "恢复入职"
fullPath: "/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/restore_flow_instance"
updateTime: "1734606436000"
---

# 恢复入职

通过本接口对指定已撤销的待入职员工执行恢复入职操作，对应入职管理页面恢复入职按钮{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v2&resource=pre_hire&method=restore_flow_instance)

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
      <md-td>https://open.feishu.cn/open-apis/corehr/v2/pre_hires/restore_flow_instance</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>POST</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[100 次/分钟](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            <md-perm name="corehr:pre_hire:restore_flow_instance" desc="恢复入职" support_app_types="custom,isv" tags="">恢复入职</md-perm>
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
	待入职ID,可从[待入职列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/corehr-v2/pre_hire/search)接口获取

**示例值**："7345005664477775407"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >confirm_workforce</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否强制占编；true为强制占编；false为非强制占编

**示例值**：false
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
    "confirm_workforce": false
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
	是否成功恢复入职
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
  <md-td>1161001</md-td>
  <md-td>param is invalid</md-td>
  <md-td>请填写正确的参数</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1161000</md-td>
  <md-td>Server system error</md-td>
  <md-td>系统出现问题，如需帮助，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。</md-td>
</md-tr>


<md-tr>
  <md-td>503</md-td>
  <md-td>1161204</md-td>
  <md-td>Requset timeout</md-td>
  <md-td>请求超时，请稍后重试</md-td>
</md-tr>


<md-tr>
  <md-td>429</md-td>
  <md-td>1161604</md-td>
  <md-td>QPS over limit</md-td>
  <md-td>接口请求过多，请稍后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161116</md-td>
  <md-td>A conflict occurred as multiple people are operating at the same time. Please refresh the page and try again later.</md-td>
  <md-td>多人同时操作发生冲突，请稍后刷新页面后重试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161097</md-td>
  <md-td>Permission denied, please contact the administrator.</md-td>
  <md-td>无权限操作，请联系管理员</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161105</md-td>
  <md-td>You don't have the permission to view the prehire, or the prehire does not exist</md-td>
  <md-td>无权限查看该待入职人员，或该待入职人员不存在</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161129</md-td>
  <md-td>Unable to submit this task as pre-hire is in the \"{{label}}\" stage.</md-td>
  <md-td>该待入职人员当前状态为「{{label}}」，无法进行此操作</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161063</md-td>
  <md-td>workforce has exceed</md-td>
  <md-td>校验中心，校验 & 预占编失败</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161034</md-td>
  <md-td>Incorrect work email format. Please fill in a valid email address.</md-td>
  <md-td>「工作邮箱」格式不正确，请填写有效邮箱</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161035</md-td>
  <md-td>Incorrect work email domain.</md-td>
  <md-td>「工作邮箱」域名错误</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161036</md-td>
  <md-td>Work email is duplicate with an active individual in the system.</md-td>
  <md-td>「工作邮箱」与系统中的在职人员重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161118</md-td>
  <md-td>Work email is duplicate with the existing mailbox in the Feishu business mailbox.</md-td>
  <md-td>工作邮箱与飞书企业邮箱中已存在的邮箱重复</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161119</md-td>
  <md-td>Work email is duplicate with an offboarded individual in the system, can be viewed in the Feishu Enterprise Mailbox Recycle Bin.</md-td>
  <md-td>工作邮箱与系统中的离职人员重复，可在飞书企业邮箱回收站中查看此邮箱</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161120</md-td>
  <md-td>Currently, there is no permission to edit the work email of the person being operated on. You can modify the address book settings by accessing the application permissions in the 'Feishu HR Application Management' interface within the 'Feishu Management Backend'</md-td>
  <md-td>暂无被操作人工作邮箱编辑权限，可在「飞书管理后台」的飞书人事应用管理界面，找到应用权限以修改通讯录设置</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161121</md-td>
  <md-td>Incorrect email format, work email need to be lowercase</md-td>
  <md-td>「工作邮箱」格式不正确，字母需为小写</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161122</md-td>
  <md-td>Incorrect email format, special character in work email</md-td>
  <md-td>「工作邮箱」格式不正确，存在特殊字符</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161123</md-td>
  <md-td>Incorrect email format</md-td>
  <md-td>「工作邮箱」格式不正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161124</md-td>
  <md-td>Incorrect email format, the total length of the email exceeds 20 characters</md-td>
  <md-td>「工作邮箱」格式不正确，总长度需小于等于 20 位</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161125</md-td>
  <md-td>Work email already exists in the account LDAP</md-td>
  <md-td>「工作邮箱」在账号 LDAP 已存在</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161126</md-td>
  <md-td>There are sensitive words in the email prefix</md-td>
  <md-td>邮箱前缀包含敏感词</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1161127</md-td>
  <md-td>Duplicate with the existing mailbox</md-td>
  <md-td>与系统中已存在的邮箱重复</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




