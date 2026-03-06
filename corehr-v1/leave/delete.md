---
title: "删除假期发放记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave_granting_record/delete"
updateTime: "1722912175000"
---

# 删除假期发放记录

删除飞书人事休假系统中的发放记录，假勤管理-休假管理-[发放记录](https://example.feishu.cn/people/workforce-management/manage/leave/leave_admin/granting_record)（仅支持删除发放来源是「手动发放」或「外部系统发放」的记录）。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=corehr&version=v1&resource=leave_granting_record&method=delete)

:::html
<md-alert type="error">

</md-alert>
:::

:::html
<md-alert type="warn">

</md-alert>
:::

:::html
<md-alert type="tip">
仅飞书人事企业版可用
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
      <md-td>https://open.feishu.cn/open-apis/corehr/v1/leave_granting_records/:leave_granting_record_id</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>DELETE</md-td>
    </md-tr>
    <md-tr>
      <md-th>接口频率限制</md-th>
      <md-td>[1000 次/分钟、50 次/秒](/ssl:ttdoc/ukTMukTMukTM/uUzN04SN3QjL1cDN)</md-td>
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
            
            <div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
            
      </md-th>
      <md-td>
            <md-perm name="corehr:leave_granting_record:write" desc="更新假期授予记录" support_app_types="custom,isv" tags="">更新假期授予记录</md-perm>
            <md-perm name="corehr:corehr" desc="更新核心人事信息" support_app_types="custom" tags="">更新核心人事信息</md-perm>
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
	<md-text type="field-name" >leave_granting_record_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	假期发放记录 ID，从[创建假期发放记录](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/corehr-v1/leave_granting_record/create)中可以获得

**示例值**："6893014062142064135"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
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
  <md-td>400</md-td>
  <md-td>1160001</md-td>
  <md-td>No tenant ID</md-td>
  <md-td>租户ID为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160002</md-td>
  <md-td>Invalid granting unit</md-td>
  <md-td>授予单位出错</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160003</md-td>
  <md-td>Invalid effective date</md-td>
  <md-td>日期格式必须是类似“2020-01-01”</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160004</md-td>
  <md-td>Invalid granting quantity</md-td>
  <md-td>必须是能解析成数字的字符串，例如“2.5”</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160005</md-td>
  <md-td>Accessed data object not found</md-td>
  <md-td>检查leaveTypeID是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160006</md-td>
  <md-td>Employment not found</md-td>
  <md-td>检查employmentID是否正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160007</md-td>
  <md-td>Leave plan version not found</md-td>
  <md-td>假期计划版本数据不存在，请检查该类型的假期对应的计划配置是否创建</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160008</md-td>
  <md-td>Error occurred while checking if the employee is eligible for the vacation plan</md-td>
  <md-td>员工不适用于假期计划版本，请检查该假期计划适用人员范围是否和员工信息匹配</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160009</md-td>
  <md-td>Accrual rule not found</md-td>
  <md-td>检查该假期计划版本是否正确创建，是否存在有效的发放规则</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160010</md-td>
  <md-td>Granting record already exists</md-td>
  <md-td>response里会带上已存在的发放记录的信息，用户可以将其取出，不需要再重试请求</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160011</md-td>
  <md-td>Error occurred when getting employment information</md-td>
  <md-td>获取员工信息失败</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160012</md-td>
  <md-td>An exception occurs in the database</md-td>
  <md-td>数据库异常，请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160013</md-td>
  <md-td>Error occurred while checking if the employee is eligible for the vacation plan.</md-td>
  <md-td>检查员工是否符合假期计划适用范围时发生错误</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160014</md-td>
  <md-td>Error occurred when calculate accrual record</md-td>
  <md-td>计算授予计划错误</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160024</md-td>
  <md-td>There is a subclass for the leave type, but the subclass ID has not been passed</md-td>
  <md-td>如果假期类型存在子类，那么leaveTypeID必须传子类ID</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160025</md-td>
  <md-td>The granting quantity range is from -9999 to 9999</md-td>
  <md-td>额度范围为-9999～9999</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160026</md-td>
  <md-td>The number of decimal places of the granted quantity cannot exceed 6</md-td>
  <md-td>发放数量最多6位小数</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160027</md-td>
  <md-td>The length of the granting reason cannot exceed 3000</md-td>
  <md-td>发放原因长度最多3000</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160028</md-td>
  <md-td>There is an error in the unit conversion configuration in the granting rule</md-td>
  <md-td>检查假期计划版本的单位转换规则是否配置正确</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160029</md-td>
  <md-td>The leave type has been deactivated</md-td>
  <md-td>不能往已停用的假期类型写发放记录</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1169999</md-td>
  <md-td>Unknown error</md-td>
  <md-td>未知错误，请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160015</md-td>
  <md-td>Internal error</md-td>
  <md-td>内部错误，请联系 [技术支持](https://applink.feishu.cn/TLJpeNdW)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160016</md-td>
  <md-td>Invalid param</md-td>
  <md-td>对照接口文档的入参排查，是否漏填参数、格式错误等（例如数值参数传了字母、日期格式错误等）</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160017</md-td>
  <md-td>User not found</md-td>
  <md-td>未找到用户信息</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160018</md-td>
  <md-td>Invalid leave balance calculate Conf</md-td>
  <md-td>无效的假期余额计算配置</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160019</md-td>
  <md-td>The calculation result of leave balance is empty</md-td>
  <md-td>假期余额计算为空</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160020</md-td>
  <md-td>When calculating the leave balance, there is no leave plan version that matches the employee</md-td>
  <md-td>没有与员工匹配的假期计划版本</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160021</md-td>
  <md-td>For the leave type that is not granted according to the cycle, balance calculation is not supported</md-td>
  <md-td>不按周期授予的假期类型，不支持余额计算</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160022</md-td>
  <md-td>The data of the leave plan version is invalid</md-td>
  <md-td>假期计划版本数据不合法</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1160023</md-td>
  <md-td>Error occurred when calculating the leave balance</md-td>
  <md-td>假期余额计算出错</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160030</md-td>
  <md-td>The length of the granted unique ID cannot exceed 64</md-td>
  <md-td>授予唯一ID长度不能超过64</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160031</md-td>
  <md-td>This granting record cannot be edited or deleted</md-td>
  <md-td>该授予记录不可编辑或删除</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160032</md-td>
  <md-td>The expiration time of this granting record is invalid</md-td>
  <md-td>该授予记录过期时间不合法</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160033</md-td>
  <md-td>The effective date is after the granting date</md-td>
  <md-td>生效日期在发放日期之后</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160034</md-td>
  <md-td>The expiration date format is incorrect</md-td>
  <md-td>失效日期格式错误</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1160035</md-td>
  <md-td>No permission to access the employee data</md-td>
  <md-td>无权访问该员工数据</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




