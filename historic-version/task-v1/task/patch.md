---
title: "更新任务"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/task-v1/task/patch"
updateTime: "1713178780000"
---

# 更新任务

该接口用于修改任务的标题、描述、时间、来源等相关信息。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=task&version=v1&resource=task&method=patch)

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
      <md-td>https://open.feishu.cn/open-apis/task/v1/tasks/:task_id</md-td>
    </md-tr>
    <md-tr>
      <md-th>HTTP Method</md-th>
      <md-td>PATCH</md-td>
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
            
      </md-th>
      <md-td>
            <md-perm name="task:task" desc="查看、创建、编辑和删除任务（旧版）" support_app_types="custom,isv" tags="">查看、创建、编辑和删除任务（旧版）</md-perm>
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
	<md-text type="field-name" >task_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务 ID

**示例值**："83912691-2e43-47fc-94a4-d512e03984fa"
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
	<md-text type="field-name" >task</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >task</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	被更新的任务实体基础信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >summary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务的标题，类型为文本字符串。
如果要在任务标题中插入 URL 或者 @某个用户，请使用rich_summary字段。
创建任务时，任务标题(summary字段)和任务富文本标题(rich_summary字段)不能同时为空，需要至少填充其中一个字段。
<md-alert>
任务标题和任务富文本标题同时存在时只使用富文本标题。
</md-alert>

**示例值**："完成本季度OKR编写"

**数据校验规则**：

- 长度范围：`0` ～ `1000` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务的描述，类型为文本字符串。
如果要在任务描述中插入 URL 或者 @某个用户，请使用rich_description字段。
<md-alert>
任务备注和任务富文本备注同时存在时只使用富文本备注。
</md-alert>

**示例值**："对本次会议内容复盘总结，编写更新本季度OKR"

**数据校验规则**：

- 长度范围：`0` ～ `65536` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >extra</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	附属信息。
接入方可以传入base64 编码后的自定义的数据。用户如果需要对当前任务备注信息，但对外不显示，可使用该字段进行存储。
该数据会在获取任务详情时，原样返回给用户。

**示例值**："dGVzdA=="

**数据校验规则**：

- 长度范围：`0` ～ `65536` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >due</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >due</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务的截止时间设置
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	表示截止时间的Unix时间戳（单位为秒）。

**示例值**："1623124318"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >timezone</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	截止时间对应的时区。
传入值需要符合IANA Time Zone Database标准，规范见[Time Zone Database](https://www.iana.org/time-zones)。

**示例值**："Asia/Shanghai"

**默认值**：`Asia/Shanghai`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >is_all_day</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	标记任务是否为全天任务。
包括如下取值：
- true：表示是全天任务，全天任务的截止时间为当天 UTC 时间的 0 点。
- false：表示不是全天任务。

**示例值**：false

**默认值**：`false`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >origin</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >origin</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务关联的第三方平台来源信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >platform_i18n_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	任务来源的名称。
用于在任务中心详情页展示。需要提供一个字典，支持多种语言名称映射。应用在使用不同语言时，导入来源也将展示对应的内容。详细参见：[任务字段补充说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/Supplementary-directions-of-task-fields)

**示例值**："{\"zh_cn\": \"IT 工作台\", \"en_us\": \"IT Workspace\"}"

**数据校验规则**：

- 长度范围：`0` ～ `1024` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >href</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >href</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务关联的来源平台详情页链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	具体链接地址。
URL仅支持解析http、https。详细参见：[任务字段补充说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/Supplementary-directions-of-task-fields)

**示例值**："https://support.feishu.com/internal/foo-bar"

**数据校验规则**：

- 长度范围：`0` ～ `1024` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	链接对应的标题

**示例值**："反馈一个问题，需要协助排查"

**数据校验规则**：

- 长度范围：`0` ～ `512` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >can_edit</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	此字段用于控制该任务在飞书任务中心是否可编辑，默认为false
<md-alert>
已经废弃，向前兼容故仍然保留，但不推荐使用
</md-alert>

**示例值**：true

**默认值**：`false`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >custom</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	自定义完成配置。
此字段用于设置完成任务时的页面跳转，或展示提示语。详细参见：[任务字段补充说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/Supplementary-directions-of-task-fields)

**示例值**："{\"custom_complete\":{\"android\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}},\"ios\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}},\"pc\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}}}}"

**数据校验规则**：

- 长度范围：`0` ～ `65536` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >followers</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >follower\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务的关注者

**示例值**：ou_03c21c80caea2c816665f8056dc59027
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务关注人 ID

**示例值**："ou_99e1a581b36ecc4862cbfbce473f3123"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	要删除的关注人ID列表

**示例值**：["ou_99e1a581b36ecc4862cbfbce473f3123"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >collaborators</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >collaborator\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务的执行者

**示例值**：ou_558d4999baae26e32aa2fd9bb228660b
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	任务执行者的 ID。
传入的值为 user_id 或 open_id，由user_id_type 决定。user_id和open_id的获取可见文档[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)。
<md-alert>
已经废弃，为了向前兼容早期只支持单次添加一个人的情况而保留，但不再推荐使用，建议使用id_list字段
</md-alert>

**示例值**："ou_99e1a581b36ecc4862cbfbce473f1234"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	执行者的用户ID列表。
传入的值为 user_id 或 open_id，由user_id_type 决定。user_id和open_id的获取可见文档[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)。

**示例值**：["ou_99e1a581b36ecc4862cbfbce473f3123"]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >collaborator_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	创建任务时添加的执行者用户id列表。
传入的值为 user_id 或 open_id ，由user_id_type 决定。user_id和open_id的获取可见文档：[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)。

**示例值**：["ou_49dadcd6fd55da971d887087c4f3a37a"]

**数据校验规则**：

- 最大长度：`100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >follower_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	创建任务时添加的关注者用户id列表。
传入的值为 user_id 或 open_id ，由user_id_type 决定。user_id和open_id的获取可见文档：[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)。

**示例值**：["ou_49dadcd6fd55da971d887087c4f3a37a"]

**数据校验规则**：

- 最大长度：`100`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >repeat_rule</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	重复任务的规则表达式。
语法格式参见[RRule语法规范](https://www.ietf.org/rfc/rfc2445.txt) 4.3.10小节

**示例值**："FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >rich_summary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	富文本任务标题。语法格式参见[Markdown模块](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/markdown-module)
。创建任务时，任务标题(summary字段)和任务富文本标题(rich_summary字段)不能同时为空，需要至少填充其中一个字段。

**示例值**："完成本季度OKR编写\[飞书开放平台](https://open.feishu.cn/)"

**数据校验规则**：

- 长度范围：`0` ～ `1000` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >rich_description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	富文本任务备注。语法格式参见[Markdown模块](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/markdown-module)

**示例值**："对本次会议内容复盘总结，编写更新本季度OKR\[飞书开放平台](https://open.feishu.cn/)"

**数据校验规则**：

- 长度范围：`0` ～ `65536` 字符
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >update_fields</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	指定需要更新的任务字段。可以更新的字段包括：
<md-enum>
<md-enum-item key="summary" >任务标题（普通文本）</md-enum-item>
<md-enum-item key="rich_summary" >任务标题（富文本）</md-enum-item>
<md-enum-item key="description" >任务描述（普通文本）</md-enum-item>
<md-enum-item key="rich_description" >任务描述（富文本）</md-enum-item>
<md-enum-item key="due" >任务截止时间</md-enum-item>
<md-enum-item key="extra" >任务附属信息</md-enum-item>
<md-enum-item key="custom" >任务自定义完成规则</md-enum-item>
<md-enum-item key="follower_ids" >任务关注人ID列表</md-enum-item>
<md-enum-item key="collaborator_ids" >任务执行者ID列表</md-enum-item>
<md-enum-item key="repeat_rule" >任务重复规则</md-enum-item>
</md-enum>

**示例值**：["summary"]
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
	"task": {
		"summary": "每天喝八杯水，保持身心愉悦",
		"description": "多吃水果，多运动，健康生活，快乐工作。",
		"extra": "dGVzdA==",
		"due": {
			"time": "1623124318",
			"timezone": "Asia/Shanghai",
			"is_all_day": false
		},
		"origin": {
			"platform_i18n_name": "{\"zh_cn\": \"IT 工作台\", \"en_us\": \"IT Workspace\"}",
			"href": {
				"url": "https://support.feishu.com/internal/foo-bar",
				"title": "反馈一个问题，需要协助排查"
			}
		},
		"can_edit": true,
		"custom": "{\"custom_complete\":{\"android\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}},\"ios\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}},\"pc\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}}}}",
		"repeat_rule": "FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR"
	},
	"update_fields": ["summary"]
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
	<md-text type="field-name" >task</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >task</md-text>
	</md-dt-td>
	<md-dt-td>
	返回修改后的任务详情
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的唯一ID，例如"83912691-2e43-47fc-94a4-d512e03984fa"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >summary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的标题，类型为文本字符串。
如果要在任务标题中插入 URL 或者 @某个用户，请使用rich_summary字段。
创建任务时，任务标题(summary字段)和任务富文本标题(rich_summary字段)不能同时为空，需要至少填充其中一个字段。
<md-alert>
任务标题和任务富文本标题同时存在时只使用富文本标题。
</md-alert>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的描述，类型为文本字符串。
如果要在任务描述中插入 URL 或者 @某个用户，请使用rich_description字段。
<md-alert>
任务备注和任务富文本备注同时存在时只使用富文本备注。
</md-alert>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >complete_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的完成时间戳（单位为秒），完成时间为0则表示任务尚未完成。
不支持部分完成，只有整个任务完成，该字段才会有非0值。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >creator_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的创建者 ID。
其中查询字段 user_id_type 是用于控制返回体中 creator_id 的类型，不传时默认返回 open_id。
特别的，使用tenant_access_token 调用接口时，如果是user_id_type是openid，则返回代表该应用身份的openid；当user_id_type为user_id时，不返回creator_id。原因是user_id代表一个真实飞书用户的id，应用身份没有user_id。使用user_access_token调用接口正常返回创建者。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >extra</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	附属信息。
接入方可以传入base64 编码后的自定义的数据。用户如果需要对当前任务备注信息，但对外不显示，可使用该字段进行存储。
该数据会在获取任务详情时，原样返回给用户。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >create_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的创建时间的Unix时间戳（单位为秒）
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >update_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的更新时间的Unix时间戳（单位为秒）
创建任务时update_time与create_time相同
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >due</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >due</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的截止时间设置
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	表示截止时间的Unix时间戳（单位为秒）。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >timezone</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	截止时间对应的时区。
传入值需要符合IANA Time Zone Database标准，规范见[Time Zone Database](https://www.iana.org/time-zones)。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >is_all_day</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	标记任务是否为全天任务。
包括如下取值：
- true：表示是全天任务，全天任务的截止时间为当天 UTC 时间的 0 点。
- false：表示不是全天任务。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >origin</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >origin</md-text>
	</md-dt-td>
	<md-dt-td>
	任务关联的第三方平台来源信息
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >platform_i18n_name</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务来源的名称。
用于在任务中心详情页展示。需要提供一个字典，支持多种语言名称映射。应用在使用不同语言时，导入来源也将展示对应的内容。详细参见：[任务字段补充说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/Supplementary-directions-of-task-fields)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >href</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >href</md-text>
	</md-dt-td>
	<md-dt-td>
	任务关联的来源平台详情页链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	具体链接地址。
URL仅支持解析http、https。详细参见：[任务字段补充说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/Supplementary-directions-of-task-fields)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	链接对应的标题
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >custom</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	自定义完成配置。
此字段用于设置完成任务时的页面跳转，或展示提示语。详细参见：[任务字段补充说明](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/Supplementary-directions-of-task-fields)
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >source</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	任务创建的来源

**可选值有**：
<md-enum>
<md-enum-item key="0" >未知类型</md-enum-item>
<md-enum-item key="1" >来源任务中心创建</md-enum-item>
<md-enum-item key="2" >来源消息转任务</md-enum-item>
<md-enum-item key="3" >来源云文档</md-enum-item>
<md-enum-item key="4" >来源文档单品</md-enum-item>
<md-enum-item key="5" >来源PANO</md-enum-item>
<md-enum-item key="6" >来源tenant_access_token创建的任务</md-enum-item>
<md-enum-item key="7" >来源user_access_token创建的任务</md-enum-item>
<md-enum-item key="8" >来源新版云文档</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >followers</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >follower\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的关注者
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务关注人 ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	要删除的关注人ID列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >collaborators</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >collaborator\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	任务的执行者
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	任务执行者的 ID。
传入的值为 user_id 或 open_id，由user_id_type 决定。user_id和open_id的获取可见文档[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)。
<md-alert>
已经废弃，为了向前兼容早期只支持单次添加一个人的情况而保留，但不再推荐使用，建议使用id_list字段
</md-alert>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >id_list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	执行者的用户ID列表。
传入的值为 user_id 或 open_id，由user_id_type 决定。user_id和open_id的获取可见文档[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >collaborator_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	创建任务时添加的执行者用户id列表。
传入的值为 user_id 或 open_id ，由user_id_type 决定。user_id和open_id的获取可见文档：[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >follower_ids</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	创建任务时添加的关注者用户id列表。
传入的值为 user_id 或 open_id ，由user_id_type 决定。user_id和open_id的获取可见文档：[如何获取不同的用户 ID](/ssl:ttdoc/home/user-identity-introduction/open-id)。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >repeat_rule</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	重复任务的规则表达式。
语法格式参见[RRule语法规范](https://www.ietf.org/rfc/rfc2445.txt) 4.3.10小节
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >rich_summary</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	富文本任务标题。语法格式参见[Markdown模块](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/markdown-module)
。创建任务时，任务标题(summary字段)和任务富文本标题(rich_summary字段)不能同时为空，需要至少填充其中一个字段。
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >rich_description</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	富文本任务备注。语法格式参见[Markdown模块](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/markdown-module)
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
    "data": {
        "task": {
            "can_edit": true,
            "complete_time": "0",
            "create_time": "1630304148",
            "creator_id": "ou_05b67908bc5d12a086e909a076f7f1b6",
            "description": "多吃水果，多运动，健康生活，快乐工作。",
            "due": {
                "time": "1623124318",
                "timezone": "Asia/Shanghai"
            },
            "extra": "dGVzdA==",
            "id": "68c9b9ff-d5b5-41bf-b407-6d956f23143f",
            "origin": {
                "href": {
                    "title": "反馈一个问题，需要协助排查",
                    "url": "https://support.feishu.com/internal/foo-bar"
                },
                "platform_i18n_name": "{\"en_us\":\"IT Workspace\",\"zh_cn\":\"IT 工作台\"}"
            },
            "summary": "每天喝八杯水，保持身心愉悦",
            "custom": "{\"custom_complete\":{\"android\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}},\"ios\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}},\"pc\":{\"href\":\"https://www.feishu.cn/\",\"tip\":{\"zh_cn\":\"你好\",\"en_us\":\"hello\"}}}}",
            "update_time": "1630304149",
            "source": 6,
            "repeat_rule": "FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR"
        }
    },
    "msg": "success"
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
  <md-td>1470400</md-td>
  <md-td>The request failed due to incorrect request parameters.</md-td>
  <md-td>一般可能是请求参数存在问题，导致请求失败，建议根据返回的具体错误进行排查</md-td>
</md-tr>


<md-tr>
  <md-td>403</md-td>
  <md-td>1470403</md-td>
  <md-td>The identity token is incorrect. It should be either user_access_token or tenant_access_token.</md-td>
  <md-td>发起请求方的身份token不正确，需要为UserAccessToken或TenantAccessToken其中一种</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470410</md-td>
  <md-td>failed to parse rich_summary</md-td>
  <md-td>富文本标题解析错误，建议检查一下rich_summary是否存在格式错误，语法格式参见[Markdown模块](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/markdown-module)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470411</md-td>
  <md-td>failed to parse rich_description</md-td>
  <md-td>富文本描述解析错误，建议检查一下rich_description是否存在格式错误，语法格式参见[Markdown模块](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/task-v1/markdown-module)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470412</md-td>
  <md-td>invalid follower id</md-td>
  <md-td>关注者id无效，建议确认一下是否向follower_ids字段传入了非法的关注者id，如空值“”</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470413</md-td>
  <md-td>invalid collaborator id</md-td>
  <md-td>协作者id无效，建议确认一下是否向collaborator_ids字段传入了非法的协作者id，如空值“”</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470414</md-td>
  <md-td>invalid time zone</md-td>
  <md-td>填入的时区信息不合规，建议检查timezone字段是否格式正确，传入值需要符合IANA Time Zone Database标准，规范见[Time Zone Database](https://www.iana.org/time-zones)</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470415</md-td>
  <md-td>invalid platform_i18n_name</md-td>
  <md-td>任务导入来源的名称不合规，建议检查platform_i18n_name字段是否格式正确，可能传入了不支持的地区名</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470423</md-td>
  <md-td>task id is missing</md-td>
  <md-td>传入的任务id丢失</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470424</md-td>
  <md-td>update_fields include unknown field</md-td>
  <md-td>update_field中包含了未知的字段</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470425</md-td>
  <md-td>update_fields include forbidden field</md-td>
  <md-td>update_field中包含了禁止更新的字段</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470426</md-td>
  <md-td>expected one or more update field</md-td>
  <md-td>update_field为空，应该填充需要更新的字段</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470450</md-td>
  <md-td>request too fast</md-td>
  <md-td>当前同时发起的请求过多，峰值较高导致了限流，请稍后重新尝试</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470602</md-td>
  <md-td>Invalid task id.</md-td>
  <md-td>请检查任务的 id 是否合法</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1470603</md-td>
  <md-td>update task failed</md-td>
  <md-td>一般是业务逻辑校验未通过</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470740</md-td>
  <md-td>Text content fails to pass the audit.</md-td>
  <md-td>一般是任务的标题或描述或富文本内容存在非法内容，没有通过安全内容检查</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1470741</md-td>
  <md-td>failed to audit task</md-td>
  <md-td>任务内容审核失败，建议结合失败原因排查。如果无法解决，请提供 request id 并联系飞书技术人员协助排查</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470404</md-td>
  <md-td>be refused to create or update task, perhaps you have no permission</md-td>
  <md-td>一般是因为操作者没有操作权限，导致更新任务或其他更新任务的操作失败。如，任务的关注者没有权限修改任务。</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470434</md-td>
  <md-td>invalid repeat rule, please check the format</md-td>
  <md-td>重复规则无法解析，可能是传入了不正确的格式，请检查是否符合语法规范</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470435</md-td>
  <md-td>decode extra by base64 failed</md-td>
  <md-td>extra字段无法按base64格式解析，请检查传入的内容是否由base64编码后传入</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470436</md-td>
  <md-td>failed to parse url of origin, should start with http, https or applink</md-td>
  <md-td>解析Origin中的URL失败，请检查是否以http、https或applink开头</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470437</md-td>
  <md-td>summary or description length exceed limit, the maximum length of summary is 256, the maximum length of description is 65536</md-td>
  <md-td>任务标题或者描述的文本长度超出限制，标题文本最大长度为256个字符，描述文本最大长度是65536个字符</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470438</md-td>
  <md-td>invalid custom, please check the format</md-td>
  <md-td>Custom字段格式错误，请根据字段说明检查</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1470439</md-td>
  <md-td>failed to get time by timestamp</md-td>
  <md-td>无法解析时间戳，请根据字段说明检查时间戳是否符合规范</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




