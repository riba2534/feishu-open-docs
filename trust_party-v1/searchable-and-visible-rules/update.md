---
title: "更新可搜可见规则"
fullPath: "/uAjLw4CM/ukTMukTMukTM/directory-v1/collaboration_rule/update"
updateTime: "1745918555000"
---

# 更新可搜可见规则

管理员视角更新可搜可见规则。用户需具备关联组织管理员权限。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=directory&version=v1&resource=collaboration_rule&method=update)

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
      <md-td>https://open.feishu.cn/open-apis/directory/v1/collaboration_rules/:collaboration_rule_id</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>PUT</md-td>
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
            <md-perm name="trust_party:collaboration_rule:write" desc="变更关联组织协作规则" support_app_types="custom" tags="">变更关联组织协作规则</md-perm>
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
或
<md-tag mode="inline" type="token-user">user_access_token</md-tag>

**值格式**："Bearer `access_token`"

**示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560"

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
	<md-text type="field-name" >collaboration_rule_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	规则ID，可通过[查询可搜可见规则](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/directory-v1/collaboration_rule/list)获得

**示例值**："12121"
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
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
	<md-text type="field-name" >target_tenant_key</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	对方组织的tenant key，可通过[管理员获取所有关联组织列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/directory-v1/collaboration_tenant/list)获取

**示例值**：test_key
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
	<md-text type="field-name" >subjects</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >collaboration_rule_entities</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	实体数量之和需要小于100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >open_user_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户 open id，可以使用通讯录/组织架构接口获取我方ID

**示例值**：["od-112121"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >open_department_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	部门 open id，0代表全部成员。可以使用通讯录/组织架构接口获取我方ID

**示例值**：["od-12121212"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >open_group_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户组 open id，可以使用通讯录/组织架构接口获取我方ID

**示例值**：["od-12121"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >objects</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >collaboration_rule_entities</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	实体数量之和需要小于100
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >open_user_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户 open id，可以使用[获取关联组织双方共享成员范围](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/directory-v1/collboration_share_entity/list)和[获取关联组织的部门和成员信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/collaboration_tenant/visible_organization)来组合获取我方想要设置的关联组织部门/用户组和人员

**示例值**：["od-112121"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >open_department_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	部门 open id，0代表全部成员；可以使用[获取关联组织双方共享成员范围](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/directory-v1/collboration_share_entity/list)和[获取关联组织的部门和成员信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/collaboration_tenant/visible_organization)来组合获取我方想要设置的关联组织部门/用户组和人员

**示例值**：["od-12121212"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >open_group_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用户组 open id，可以使用[获取关联组织双方共享成员范围](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/directory-v1/collboration_share_entity/list)和[获取关联组织的部门和成员信息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/collaboration_tenant/visible_organization)来组合获取我方想要设置的关联组织部门/用户组和人员

**示例值**：["od-12121"]

**数据校验规则**：

- 长度范围：`0` ～ `100`
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "subjects": {
        "open_user_ids": [
            "od-112121"
        ],
        "open_department_ids": [
            "od-12121212"
        ],
        "open_group_ids": [
            "od-12121"
        ]
    },
    "objects": {
        "open_user_ids": [
            "od-112121"
        ],
        "open_department_ids": [
            "od-12121212"
        ],
        "open_group_ids": [
            "od-12121"
        ]
    }
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
  <md-td>400</md-td>
  <md-td>2223101</md-td>
  <md-td>This tenant has no  relationship with the other tenant</md-td>
  <md-td>请选择正确的关联组织</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2223103</md-td>
  <md-td>The rule subject is not within the sharing scope</md-td>
  <md-td>请按照[获取关联组织双方共享成员范围](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/directory-v1/collboration_share_entity/list)设置关联组织规则主体</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2223104</md-td>
  <md-td>The rule object is not within the sharing scope</md-td>
  <md-td>请按照[获取关联组织双方共享成员范围](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/directory-v1/collboration_share_entity/list)设置关联组织规则客体</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2223106</md-td>
  <md-td>can't set empty entity in subject or object</md-td>
  <md-td>请给主客体设置有效的实体</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2223108</md-td>
  <md-td>The update is too frequent. Please try again later</md-td>
  <md-td>操作过于频繁，请稍后再试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2223107</md-td>
  <md-td>The rule id is not exist</md-td>
  <md-td>请选择有效的rule id</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2223110</md-td>
  <md-td>can't set other entity when department is 0</md-td>
  <md-td>在部门设置为0的时候，勿设置其他实体</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>2224001</md-td>
  <md-td>No permission to operate</md-td>
  <md-td>无操作权限，请联系超管配置你为关联组织管理员</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




