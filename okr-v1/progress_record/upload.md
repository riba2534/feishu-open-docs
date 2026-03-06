---
title: "上传进展记录图片"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/image/upload"
updateTime: "1753428958000"
---

# 上传进展记录图片

上传图片，以获取在进展记录富文本中使用的 token。成功调用该接口后，你可继续调用[创建 OKR 进展记录](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/create)或[更新 OKR 进展记录](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/update)，将返回的 `url`参数和`file_token` 参数传入 `imageList` 参数中。{尝试一下}(url=/api/tools/api_explore/api_explore_config?project=okr&version=v1&resource=image&method=upload)

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
      <md-td>https://open.feishu.cn/open-apis/okr/v1/images/upload</md-td>
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
            <md-perm name="okr:okr.progress.file:upload" desc="上传 OKR 进展图片附件" support_app_types="custom" tags="">上传 OKR 进展图片附件</md-perm>
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
<md-td>

**示例值**："multipart/form-data; boundary=---7MA4YWxkTrZu0gW"</md-td>
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
	<md-text type="field-name" >data</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >file</md-text>
	</md-dt-td>
	<md-dt-td>
	是
	</md-dt-td>
	<md-dt-td>
	图片二进制文件。目前仅支持上传 JPG、JPEG、PNG、WEBP、GIF、BMP、ICO、TIFF、HEIC 格式的图片。

**示例值**：file binary
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
	插入图片所在的待创建/修改的进展记录对应的目标 ID，可以通过调用“批量获取 OKR”或“获取用户的 OKR 列表”接口获取对应的 Objective 或 KR 的 ID。

**示例值**："6974586812998174252"
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
	插入图片所在的待创建/修改的进展记录对应的目标类型

**示例值**：2

**可选值有**：
<md-enum>
<md-enum-item key="2" >okr的O</md-enum-item>
<md-enum-item key="3" >okr的KR</md-enum-item>
</md-enum>
	</md-dt-td>
</md-dt-tr>

  </md-dt-tbody>
</md-dt-table>
:::





### 请求体示例

```HTTP
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="data";
Content-Type: application/octet-stream


---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="target_id";

6974586812998174252
---7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="target_type";

2
---7MA4YWxkTrZu0gW
```



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
	<md-text type="field-type" >image_info</md-text>
	</md-dt-td>
	<md-dt-td>
	\-
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >file_token</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	图片token
	</md-dt-td>
</md-dt-tr>


<md-dt-tr level="1">
	<md-dt-td>
	<md-text type="field-name" >url</md-text>
	</md-dt-td>
	<md-dt-td>
	<md-text type="field-type" >string</md-text>
	</md-dt-td>
	<md-dt-td>
	图片下载链接
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
        "file_token": "boxbcc6DmPfgi4rNXIaGfptc9HX",
        "url": "https://internal-****.cn/stream/api/downloadFile/?file_token=boxbcc6DmPfgi4rNXIaGfptc9HX&ticket=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0YXJnZXRfaWQiOiI3MDQxNTA5NTg4MzkwMzQ2NzcyIiwidGFyZ2V0X3R5cGUiOjEsImFjdGlvbiI6MiwiZmlsZV90b2tlbiI6ImJveGJjYzZEbVBmZ2k0ck5YSWFHZnB0YzlIWCIsInVzZXJfaWQiOiI2OTY5ODU1NTAxNzQ0ODM0MDkyIiwidGVuYW50X2lkIjoiNjg3NzUwMjY4NzYwOTQwNjk5MCIsImV4cCI6MTY0MDY4MzI4OX0.VqOLS7kDtCuhyU_WuWeXvxg1XIyJxskBfNGFQP8uGkCBhYh9scwcbWQJ4xubAZs3cmsrPMVm-aho3tz5d7NT5Q"
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




