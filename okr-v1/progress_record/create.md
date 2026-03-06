---
title: "创建 OKR 进展记录"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/create"
updateTime: "1753428957000"
---

# 创建 OKR 进展记录

创建 OKR 进展记录。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=okr&version=v1&resource=progress_record&method=create)

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
      <md-td>https://open.feishu.cn/open-apis/okr/v1/progress_records</md-td>
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
      <md-app-support types="custom"></md-app-support>
      </md-td>
    </md-tr>
    <md-tr>
      <md-th>
            权限要求
            <md-tooltip type="info">调用该 API 所需的权限。开启其中任意一项权限即可调用</md-tooltip>
            
            <div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
            
      </md-th>
      <md-td>
            <md-perm name="okr:okr" desc="更新 OKR 信息" support_app_types="custom" tags="">更新 OKR 信息</md-perm>
            <md-perm name="okr:okr.progress:writeonly" desc="更新 OKR 进展" support_app_types="custom" tags="">更新 OKR 进展</md-perm>
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
	<md-text type="field-name" >source_title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	进展来源

**示例值**："周报系统"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >source_url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	进展来源链接

**示例值**："https://www.zhoubao.com"

**数据校验规则**：

- 正则校验：`^https?://.*$`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >target_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	目标 id，与 target_type 对应，可通过 OKR 内容相关接口获取

**示例值**："7041430377642082323"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >target_type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	目标类型

**示例值**：2

**可选值有**：
<md-enum>
<md-enum-item key="2" >okr的O</md-enum-item>
<md-enum-item key="3" >okr的KR</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >content</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_block</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	进展详情 富文本格式
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >blocks</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_block_element\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文档结构是按行排列的，每行内容是一个 Block
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文档元素类型

**示例值**："paragraph"

**可选值有**：
<md-enum>
<md-enum-item key="paragraph" >文本段落</md-enum-item>
<md-enum-item key="gallery" >图片</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >paragraph</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_paragraph</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文本段落
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >style</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_paragraph_style</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	段落样式
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_list</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	有序列表/无序列表/任务列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	列表类型

**示例值**："number"

**可选值有**：
<md-enum>
<md-enum-item key="number" >有序列表</md-enum-item>
<md-enum-item key="bullet" >无序列表</md-enum-item>
<md-enum-item key="checkBox" >任务列表</md-enum-item>
<md-enum-item key="checkedBox" >已完成的任务列表</md-enum-item>
<md-enum-item key="indent" >tab缩进</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >indentLevel</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	列表的缩进级别，支持指定一行的缩进 除代码块以外的列表都支持设置缩进，支持 1-16 级缩进，取值范围：[1,16]

**示例值**：1
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	用于指定列表的行号，仅对有序列表和代码块生效 如果为有序列表设置了缩进，行号可能会显示为字母或者罗马数字

**示例值**：1
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >elements</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_paragraph_element\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	段落元素组成一个段落
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	元素类型

**示例值**："textRun"

**可选值有**：
<md-enum>
<md-enum-item key="textRun" >文本型元素</md-enum-item>
<md-enum-item key="docsLink" >文档链接型元素</md-enum-item>
<md-enum-item key="person" >艾特用户型元素</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >textRun</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_text_run</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文本
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	具体的文本内容

**示例值**："周报内容"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >style</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_text_style</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	文本内容的样式，支持 BIUS、颜色等
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >bold</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否加粗

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >strikeThrough</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	是否删除

**示例值**：true
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >backColor</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_color</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	背景颜色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >red</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	红 取值范围[0,255]

**示例值**：216
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >green</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	绿 取值范围[0,255]

**示例值**：191
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >blue</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	蓝 取值范围[0,255]

**示例值**：188
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >alpha</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	透明度 取值范围[0,1]

**示例值**：0.1
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >textColor</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_color</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	字体颜色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >red</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	红 取值范围[0,255]

**示例值**：216
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >green</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	绿 取值范围[0,255]

**示例值**：191
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >blue</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	蓝 取值范围[0,255]

**示例值**：188
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >alpha</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	透明度 取值范围[0,1]

**示例值**：0.1
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >link</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_link</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	链接地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
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
	链接地址

**示例值**："https://www.xxxxx.com/"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >docsLink</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_docs_link</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	飞书云文档
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
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
	飞书云文档链接地址

**示例值**："https://xxx.feishu.cn/docx/xxxxxxxx"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
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
	飞书云文档标题

**示例值**："项目说明文档"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >person</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_person</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	艾特用户
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >openId</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	员工的OpenID

**示例值**："ou_3bbe8a09c20e89cce9bff989ed840674"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >gallery</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_gallery</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	图片
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >imageList</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_image_item\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	图片元素
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >fileToken</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	图片 token，通过上传图片接口获取

**示例值**："boxcnOj88GDkmWGm2zsTyCBqoLb"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >src</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	图片链接

**示例值**："https://example.com/drive/home/"
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >width</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	图片宽，单位px

**示例值**：458
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >height</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	图片高，单位px

**示例值**：372
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >source_url_pc</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	pc进展来源链接

**示例值**："open.feishu.cn"

**数据校验规则**：

- 正则校验：`^https?://.*$`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >source_url_mobile</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	mobile进展来源链接

**示例值**："open.feishu.cn"

**数据校验规则**：

- 正则校验：`^https?://.*$`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="0">
	<md-dt-td>
	<md-text type="field-name" >progress_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >progress_rate_new</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	进展，包括百分比和状态
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >percent</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	进展百分比，保留两位小数

**示例值**：50.21

**默认值**：`0`

**数据校验规则**：

- 取值范围：`-99999999999` ～ `99999999999`
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	否
	</md-dt-td>
	<md-dt-td>
	进展状态

**示例值**：0

**可选值有**：
<md-enum>
<md-enum-item key="-1" >暂无</md-enum-item>
<md-enum-item key="0" >正常</md-enum-item>
<md-enum-item key="1" >风险</md-enum-item>
<md-enum-item key="2" >延期</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例
:::html
<md-code-json>
{
    "source_title":"测试周报系统",
    "source_url":"https://www.baidu.com/",
    "target_id":"7043693679567028244",
    "target_type":2,
    "content":{
        "blocks":[
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"粗体验证",
                                "style":{
                                    "bold":true
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"*",
                                "style":{
                                    "bold":true
                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"删除线验证",
                                "style":{
                                    "strikeThrough":true
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"字体颜色验证",
                                "style":{
                                    "textColor":{
                                        "red":216,
                                        "green":57,
                                        "blue":49,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"背景颜色验证",
                                "style":{
                                    "backColor":{
                                        "red":251,
                                        "green":191,
                                        "blue":188,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"粗体+删除+字体颜色+背景颜色验证",
                                "style":{
                                    "bold":true,
                                    "strikeThrough":true,
                                    "backColor":{
                                        "red":251,
                                        "green":191,
                                        "blue":188,
                                        "alpha":1
                                    },
                                    "textColor":{
                                        "red":216,
                                        "green":57,
                                        "blue":49,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"有序标题1验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"粗体验证",
                                "style":{
                                    "bold":true
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"number",
                            "indentLevel":1,
                            "number":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"有序标题2验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"删除线验证",
                                "style":{
                                    "strikeThrough":true
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"number",
                            "indentLevel":1,
                            "number":2
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"有序标题3验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"字体背景颜色验证",
                                "style":{
                                    "backColor":{
                                        "red":251,
                                        "green":191,
                                        "blue":188,
                                        "alpha":1
                                    },
                                    "textColor":{
                                        "red":216,
                                        "green":57,
                                        "blue":49,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"number",
                            "indentLevel":1,
                            "number":3
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"无序标题1验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"粗体",
                                "style":{
                                    "bold":true
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"bullet",
                            "indentLevel":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"无序标题2验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"删除线",
                                "style":{
                                    "strikeThrough":true
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"bullet",
                            "indentLevel":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"无序标题3验证，",
                                "style":{

                                }
                            }
                        },
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"字体背景颜色验证",
                                "style":{
                                    "backColor":{
                                        "red":251,
                                        "green":191,
                                        "blue":188,
                                        "alpha":1
                                    },
                                    "textColor":{
                                        "red":216,
                                        "green":57,
                                        "blue":49,
                                        "alpha":1
                                    }
                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"bullet",
                            "indentLevel":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"https://example.cn/docx/doxcnO2Wkq0YPZQYLuJKyyOvLrh#doxcnSOui82swqk6c0o436Ak3nc",
                                "style":{
                                    "link":{
                                        "url":"https://example.cn/docx/doxcnO2Wkq0YPZQYLuJKyyOvLrh#doxcnSOui82swqk6c0o436Ak3nc"
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "type":"gallery",
                "gallery":{
                    "imageList":[
                        {
                            "src":"https://internal-api-okr.feishu-boe.cn/stream/api/downloadFile/?file_token=boxbcMTBQO9ofLjWkDuPxkxOA2c&ticket=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0YXJnZXRfaWQiOiI3MDQxNDMwMzc3NjQyMDgyMzIzIiwidGFyZ2V0X3R5cGUiOjMsImFjdGlvbiI6MiwiZmlsZV90b2tlbiI6ImJveGJjTVRCUU85b2ZMaldrRHVQeGt4T0EyYyIsInVzZXJfaWQiOiI2OTY5ODU1NTAxNzQ0ODM0MDkyIiwidGVuYW50X2lkIjoiNjg3NzUwMjY4NzYwOTQwNjk5MCIsImV4cCI6MTY0MDE1NTk2M30.yc4qV2pkGUVwSO53-N_XGgeMucjmDn9iso1Ez_8vpghFz8YdeSDf4NHQpxOHYHc8RURvwI0a5UTNKKJ9CWagTQ",
                            "fileToken":"boxbcMTBQO9ofLjWkDuPxkxOA2c",
                            "width":458,
                            "height":372
                        }
                    ]
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"任务列表未勾选验证",
                                "style":{

                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"checkBox",
                            "indentLevel":1
                        }
                    }
                }
            },
            {
                "type":"paragraph",
                "paragraph":{
                    "elements":[
                        {
                            "type":"textRun",
                            "textRun":{
                                "text":"任务列表已勾选验证",
                                "style":{

                                }
                            }
                        }
                    ],
                    "style":{
                        "list":{
                            "type":"checkedBox",
                            "indentLevel":1
                        }
                    }
                }
            }
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
	<md-text type="field-type" >progress_record</md-text>
	</md-dt-td>
	<md-dt-td>
	\-
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >progress_id</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	OKR 进展ID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >modify_time</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	进展更新时间 毫秒
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >content</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_block</md-text>
	</md-dt-td>
	<md-dt-td>
	进展 对应的 Content 详细内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >blocks</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_block_element\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	文档结构是按行排列的，每行内容是一个 Block
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	文档元素类型

**可选值有**：
<md-enum>
<md-enum-item key="paragraph" >文本段落</md-enum-item>
<md-enum-item key="gallery" >图片</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >paragraph</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_paragraph</md-text>
	</md-dt-td>
	<md-dt-td>
	文本段落
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >style</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_paragraph_style</md-text>
	</md-dt-td>
	<md-dt-td>
	段落样式
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >list</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_list</md-text>
	</md-dt-td>
	<md-dt-td>
	有序列表/无序列表/任务列表
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	列表类型

**可选值有**：
<md-enum>
<md-enum-item key="number" >有序列表</md-enum-item>
<md-enum-item key="bullet" >无序列表</md-enum-item>
<md-enum-item key="checkBox" >任务列表</md-enum-item>
<md-enum-item key="checkedBox" >已完成的任务列表</md-enum-item>
<md-enum-item key="indent" >tab缩进</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >indentLevel</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	列表的缩进级别，支持指定一行的缩进 除代码块以外的列表都支持设置缩进，支持 1-16 级缩进，取值范围：[1,16]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >number</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	用于指定列表的行号，仅对有序列表和代码块生效 如果为有序列表设置了缩进，行号可能会显示为字母或者罗马数字
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >elements</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_paragraph_element\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	段落元素组成一个段落
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >type</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	元素类型

**可选值有**：
<md-enum>
<md-enum-item key="textRun" >文本型元素</md-enum-item>
<md-enum-item key="docsLink" >文档链接型元素</md-enum-item>
<md-enum-item key="person" >艾特用户型元素</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >textRun</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_text_run</md-text>
	</md-dt-td>
	<md-dt-td>
	文本
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >text</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	具体的文本内容
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >style</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_text_style</md-text>
	</md-dt-td>
	<md-dt-td>
	文本内容的样式，支持 BIUS、颜色等
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >bold</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否加粗
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >strikeThrough</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >boolean</md-text>
	</md-dt-td>
	<md-dt-td>
	是否删除
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >backColor</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_color</md-text>
	</md-dt-td>
	<md-dt-td>
	背景颜色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >red</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	红 取值范围[0,255]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >green</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	绿 取值范围[0,255]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >blue</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	蓝 取值范围[0,255]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >alpha</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	透明度 取值范围[0,1]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >textColor</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_color</md-text>
	</md-dt-td>
	<md-dt-td>
	字体颜色
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >red</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	红 取值范围[0,255]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >green</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	绿 取值范围[0,255]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >blue</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	蓝 取值范围[0,255]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >alpha</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	透明度 取值范围[0,1]
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="7">
	<md-dt-td>
	<md-text type="field-name" >link</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_link</md-text>
	</md-dt-td>
	<md-dt-td>
	链接地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="8">
	<md-dt-td>
	<md-text type="field-name" >url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	链接地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >docsLink</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_docs_link</md-text>
	</md-dt-td>
	<md-dt-td>
	飞书云文档
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	飞书云文档链接地址
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >title</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	飞书云文档标题
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >person</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_person</md-text>
	</md-dt-td>
	<md-dt-td>
	艾特用户
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="6">
	<md-dt-td>
	<md-text type="field-name" >openId</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	员工的OpenID
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="3">
	<md-dt-td>
	<md-text type="field-name" >gallery</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_gallery</md-text>
	</md-dt-td>
	<md-dt-td>
	图片
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="4">
	<md-dt-td>
	<md-text type="field-name" >imageList</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >content_image_item\[\]</md-text>
	</md-dt-td>
	<md-dt-td>
	图片元素
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >fileToken</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	图片 token，通过上传图片接口获取
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >src</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	图片链接
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >width</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	图片宽，单位px
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="5">
	<md-dt-td>
	<md-text type="field-name" >height</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	图片高，单位px
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >progress_rate</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >progress_rate_new</md-text>
	</md-dt-td>
	<md-dt-td>
	进展，包括百分比和状态
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >percent</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >number(float)</md-text>
	</md-dt-td>
	<md-dt-td>
	进展百分比，保留两位小数
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="2">
	<md-dt-td>
	<md-text type="field-name" >status</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >int</md-text>
	</md-dt-td>
	<md-dt-td>
	进展状态

**可选值有**：
<md-enum>
<md-enum-item key="-1" >暂无</md-enum-item>
<md-enum-item key="0" >正常</md-enum-item>
<md-enum-item key="1" >风险</md-enum-item>
<md-enum-item key="2" >延期</md-enum-item>
</md-enum>
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
        "content": {
            "blocks": [
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "bold": true
                                    },
                                    "text": "粗体验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "bold": true
                                    },
                                    "text": "*"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "strikeThrough": true
                                    },
                                    "text": "删除线验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "textColor": {
                                            "alpha": 1,
                                            "blue": 49,
                                            "green": 57,
                                            "red": 216
                                        }
                                    },
                                    "text": "字体颜色验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "backColor": {
                                            "alpha": 1,
                                            "blue": 188,
                                            "green": 191,
                                            "red": 251
                                        }
                                    },
                                    "text": "背景颜色验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "backColor": {
                                            "alpha": 1,
                                            "blue": 188,
                                            "green": 191,
                                            "red": 251
                                        },
                                        "bold": true,
                                        "strikeThrough": true,
                                        "textColor": {
                                            "alpha": 1,
                                            "blue": 49,
                                            "green": 57,
                                            "red": 216
                                        }
                                    },
                                    "text": "粗体+删除+字体颜色+背景颜色验证"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "有序标题1验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "bold": true
                                    },
                                    "text": "粗体验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "number": 1,
                                "type": "number"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "有序标题2验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "strikeThrough": true
                                    },
                                    "text": "删除线验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "number": 2,
                                "type": "number"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "有序标题3验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "backColor": {
                                            "alpha": 1,
                                            "blue": 188,
                                            "green": 191,
                                            "red": 251
                                        },
                                        "textColor": {
                                            "alpha": 1,
                                            "blue": 49,
                                            "green": 57,
                                            "red": 216
                                        }
                                    },
                                    "text": "字体背景颜色验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "number": 3,
                                "type": "number"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "无序标题1验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "bold": true
                                    },
                                    "text": "粗体"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "bullet"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "无序标题2验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "strikeThrough": true
                                    },
                                    "text": "删除线"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "bullet"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "无序标题3验证，"
                                },
                                "type": "textRun"
                            },
                            {
                                "textRun": {
                                    "style": {
                                        "backColor": {
                                            "alpha": 1,
                                            "blue": 188,
                                            "green": 191,
                                            "red": 251
                                        },
                                        "textColor": {
                                            "alpha": 1,
                                            "blue": 49,
                                            "green": 57,
                                            "red": 216
                                        }
                                    },
                                    "text": "字体背景颜色验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "bullet"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {
                                        "link": {
                                            "url": "https://example.cn/docx/doxcnO2Wkq0YPZQYLuJKyyOvLrh#doxcnSOui82swqk6c0o436Ak3nc"
                                        }
                                    },
                                    "text": "https://example.cn/docx/doxcnO2Wkq0YPZQYLuJKyyOvLrh#doxcnSOui82swqk6c0o436Ak3nc"
                                },
                                "type": "textRun"
                            }
                        ]
                    },
                    "type": "paragraph"
                },
                {
                    "gallery": {
                        "imageList": [
                            {
                                "fileToken": "boxbcMTBQO9ofLjWkDuPxkxOA2c",
                                "height": 372,
                                "src": "https://internal-api-okr.feishu-boe.cn/stream/api/downloadFile/?file_token=boxbcMTBQO9ofLjWkDuPxkxOA2c&ticket=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0YXJnZXRfaWQiOiI3MDQxNDMwMzc3NjQyMDgyMzIzIiwidGFyZ2V0X3R5cGUiOjMsImFjdGlvbiI6MiwiZmlsZV90b2tlbiI6ImJveGJjTVRCUU85b2ZMaldrRHVQeGt4T0EyYyIsInVzZXJfaWQiOiI2OTY5ODU1NTAxNzQ0ODM0MDkyIiwidGVuYW50X2lkIjoiNjg3NzUwMjY4NzYwOTQwNjk5MCIsImV4cCI6MTY0MDE1NTk2M30.yc4qV2pkGUVwSO53-N_XGgeMucjmDn9iso1Ez_8vpghFz8YdeSDf4NHQpxOHYHc8RURvwI0a5UTNKKJ9CWagTQ",
                                "width": 458
                            }
                        ]
                    },
                    "type": "gallery"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "任务列表未勾选验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "checkBox"
                            }
                        }
                    },
                    "type": "paragraph"
                },
                {
                    "paragraph": {
                        "elements": [
                            {
                                "textRun": {
                                    "style": {},
                                    "text": "任务列表已勾选验证"
                                },
                                "type": "textRun"
                            }
                        ],
                        "style": {
                            "list": {
                                "indentLevel": 1,
                                "type": "checkedBox"
                            }
                        }
                    },
                    "type": "paragraph"
                }
            ]
        },
        "modify_time": "1640675837810",
        "progress_id": "7046317985098760212"
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
  <md-td>500</md-td>
  <md-td>1009999</md-td>
  <md-td>internal server error</md-td>
  <md-td>内部错误，请联系飞书助手或您的客户成功经理</md-td>
</md-tr>


<md-tr>
  <md-td>500</md-td>
  <md-td>1009998</md-td>
  <md-td>system exception</md-td>
  <md-td>系统异常，请联系飞书助手或您的客户成功经理</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1001001</md-td>
  <md-td>invalid parameters</md-td>
  <md-td>无效的参数，请对照文档检查输入的参数</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1001002</md-td>
  <md-td>no permission</md-td>
  <md-td>您无权访问该接口，请确认您的登录凭证</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1001003</md-td>
  <md-td>user not found</md-td>
  <md-td>用户不存在</md-td>
</md-tr>


<md-tr>
  <md-td>400</md-td>
  <md-td>1001004</md-td>
  <md-td>okr data not found</md-td>
  <md-td>对应ID的数据不存在</md-td>
</md-tr>


  </md-tbody>
</md-table>
:::




