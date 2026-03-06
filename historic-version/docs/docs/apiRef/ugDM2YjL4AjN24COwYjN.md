---
title: "创建旧版文档"
fullPath: "/ukTMukTMukTM/ugDM2YjL4AjN24COwYjN"
updateTime: "1735541937000"
---

# 创建旧版文档


:::html
<md-alert type="error">
此接口已废弃，不允许应用再调用该接口，若继续调用将返回 95054 的错误码。

要创建文档，请使用[创建文档](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document/create)接口。
</md-alert>
:::
该接口用于创建并初始化文档。

## 前提条件
在使用此接口前，请仔细阅读[文档概述](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/docs-doc-overview)和[准备接入文档 API](/ssl:ttdoc/ukTMukTMukTM/ugzNzUjL4czM14CO3MTN/guide/getting-start)了解文档调用的规则和约束，确保你的文档数据不会丢失或出错。 
文档数据结构定义可参考：[文档数据结构概述](/ssl:ttdoc/ukTMukTMukTM/uAzM5YjLwMTO24CMzkjN)。
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
      <md-td>https://open.feishu.cn/open-apis/doc/v2/create</md-td>
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
<div style="color: rgb(100, 106, 115);font-size: 12px;line-height: 20px;white-space: pre-line;font-weight: 500;padding-top: 4px;">开启任一权限即可</div>
</md-th>
   <md-td>
<md-perm name="drive:drive" desc="查看、评论、编辑和管理云空间中所有文件" support_app_types="custom,isv" tags="">查看、评论、编辑和管理云空间中所有文件</md-perm>
<md-perm name="docs:doc" desc="查看、评论、编辑和管理文档" support_app_types="custom,isv" tags="">查看、评论、编辑和管理文档</md-perm>
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
<md-tag mode="inline" type="token-user">user_access_token</md-tag> 或 <md-tag mode="inline" type="token-tenant">tenant_access_token</md-tag>
 
**值格式**："Bearer `access_token`"

**示例值**："Bearer u-7f1bcd13fc57d46bac21793a18e560"
          
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


::: note
关于云文档接口的 AccessToken 调用说明详见 [云文档接口快速入门](/ssl:ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)
:::
<br>
### 请求体
|参数|类型|必须|说明|来源|
|--|-----|--|----|----|
|FolderToken|string|否|文件夹 token，获取方式见[如何获取云文档资源相关 token](/ssl:ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df6)；空表示根目录，tenant_access_token应用权限仅允许操作应用创建的目录|post body json 字段 | 
|Content|string|否|传入符合[文档数据结构](/ssl:ttdoc/ukTMukTMukTM/uAzM5YjLwMTO24CMzkjN)的字符串，若为空表示创建空文档|post body json 字段|

### Curl 请求 Demo
```
curl -X POST 'https://open.feishu.cn/open-apis/doc/v2/create' \
	-H 'Authorization: Bearer u-s12okJw4R1VCZLWhk9Zyzg' \
	-H 'Content-Type: application/json; charset=utf-8' \
	-d '{"FolderToken":"","Content":"{\"title\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"Hello Docs\",\"style\":{}}}]},\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"恭喜你成功通过 Open API 创建了一篇在线文档。这篇文档中，描述了大部分 Open API 已经支持的文档内容，你可以对照示例代码，了解 Docs Open API 的使用方法。\",\"style\":{}}}]}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[],\"style\":{}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"你可以通过文档的 URL，截取获得文档的 token，文档所有的 API 操作，都需要提供 token，例如：\",\"style\":{}}}]}},{\"type\":\"code\",\"code\":{\"language\":\"Plain Text\",\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"https://xxx.feishu.cn/docs/\",\"style\":{}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"doccnmPiiJWfj1uk8bV7N5SzXaa\",\"style\":{\"backColor\":{\"red\":255,\"green\":246,\"blue\":122,\"alpha\":0.8}}}}],\"style\":{}}}]}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[],\"style\":{}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"从上面的例子中，可以看出：文档中的每一行都是一个 Block\",\"style\":{}}}],\"style\":{\"headingLevel\":1}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"文档中有多种 Block 类型，在插入内容时，你需要指定当前行是什么类型的 Block，文本类型的 Block 叫做 Paragraph。\",\"style\":{}}}],\"style\":{}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"一行文本可能由多个元素组成，例如这一行，就由公式 \",\"style\":{}}},{\"type\":\"equation\",\"equation\":{\"equation\":\"E=mc^2\"}},{\"type\":\"textRun\",\"textRun\":{\"text\":\" 和 \",\"style\":{}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"行内代码块\",\"style\":{\"codeInline\":true}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\" 组成。如果一些文本包含\",\"style\":{}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"独立的样式\",\"style\":{\"backColor\":{\"red\":255,\"green\":246,\"blue\":122,\"alpha\":0.8}}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"，也会被视为一个独立的 element。\",\"style\":{}}}],\"style\":{}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[],\"style\":{}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"你可以通过 API 插入各种样式的内容\",\"style\":{}}}],\"style\":{\"headingLevel\":1}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"支持插入有序列表\",\"style\":{}}}],\"style\":{\"list\":{\"type\":\"number\",\"indentLevel\":1,\"number\":1}}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"你可以自己指定有序列表的编号\",\"style\":{}}}],\"style\":{\"list\":{\"type\":\"number\",\"indentLevel\":1,\"number\":2}}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"也可以插入无序列表\",\"style\":{}}}],\"style\":{\"list\":{\"type\":\"bullet\",\"indentLevel\":1}}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"插入更多无序列表\",\"style\":{}}}],\"style\":{\"list\":{\"type\":\"bullet\",\"indentLevel\":1}}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"支持插入任务列表和日期提醒 \",\"style\":{}}},{\"type\":\"reminder\",\"reminder\":{\"isWholeDay\":false,\"timestamp\":1609497000,\"shouldNotify\":true}}],\"style\":{\"list\":{\"type\":\"checkBox\",\"indentLevel\":1},\"todoUUID\":\"126f1471-f013-4ed1-9820-60f24da80677\"}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"或者插入引用的内容\",\"style\":{}}}],\"style\":{\"quote\":true}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"改变文档的对齐方式，例如\",\"style\":{}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"右对齐\",\"style\":{}}}],\"style\":{\"align\":\"right\"}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"此外，还能灵活应用各种文字样式，增强文档的表达能力，例如：\",\"style\":{}}}],\"style\":{\"align\":\"left\"}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"加粗 \",\"style\":{\"bold\":true}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"斜体 \",\"style\":{\"italic\":true}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"下划线 \",\"style\":{\"underLine\":true}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"删除线\",\"style\":{\"strikeThrough\":true}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\" \",\"style\":{}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"inline code\",\"style\":{\"codeInline\":true}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\" \",\"style\":{}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"高亮\",\"style\":{\"backColor\":{\"red\":255,\"green\":246,\"blue\":122,\"alpha\":0.8}}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"色\",\"style\":{\"backColor\":{\"red\":255,\"green\":246,\"blue\":122,\"alpha\":0.8}}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\" \",\"style\":{}}},{\"type\":\"textRun\",\"textRun\":{\"text\":\"超链接\",\"style\":{\"link\":{\"url\":\"https%3A%2F%2Fopen.feishu.cn%2Fdocument%2FukTMukTMukTM%2FuUDN04SN0QjL1QDN%2Fdocs-doc-overview\"}}}}]}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"或者一条删除线\",\"style\":{}}}],\"style\":{\"align\":\"center\"}}},{\"type\":\"horizontalLine\",\"horizontalLine\":{}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[],\"style\":{}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"各种表格也支持通过 API 插入，例如\",\"style\":{}}}],\"style\":{\"headingLevel\":1}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"普通表格\",\"style\":{}}}],\"style\":{\"headingLevel\":2}}},{\"type\":\"table\",\"table\":{\"rowSize\":3,\"columnSize\":3,\"tableRows\":[{\"rowIndex\":0,\"tableCells\":[{\"columnIndex\":0,\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"你可以通过表格进行排版\",\"style\":{}}}],\"style\":{\"align\":\"center\"}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"表格中的每一行也是一个 Block\",\"style\":{}}}],\"style\":{\"align\":\"center\"}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"此外，每个单元格都通过唯一的 zoneId 进行标记\",\"style\":{}}}],\"style\":{\"align\":\"center\"}}}]}},{\"columnIndex\":1,\"body\":{\"blocks\":null}},{\"columnIndex\":2,\"body\":{\"blocks\":null}}]},{\"rowIndex\":1,\"tableCells\":[{\"columnIndex\":0,\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"在\",\"style\":{\"codeInline\":true}}}],\"style\":{\"align\":\"center\"}}}]}},{\"columnIndex\":1,\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"飞\",\"style\":{\"codeInline\":true}}}],\"style\":{\"align\":\"center\"}}}]}},{\"columnIndex\":2,\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"书\",\"style\":{\"codeInline\":true}}}],\"style\":{\"align\":\"center\"}}}]}}]},{\"rowIndex\":2,\"tableCells\":[{\"columnIndex\":0,\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"享\",\"style\":{\"codeInline\":true}}}],\"style\":{\"align\":\"center\"}}}]}},{\"columnIndex\":1,\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"高\",\"style\":{\"codeInline\":true}}}],\"style\":{\"align\":\"center\"}}}]}},{\"columnIndex\":2,\"body\":{\"blocks\":[{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"效\",\"style\":{\"codeInline\":true}}}],\"style\":{\"align\":\"center\"}}}]}}]}],\"tableStyle\":{\"tableColumnProperties\":[{\"width\":100},{\"width\":100},{\"width\":100}]},\"mergedCells\":[{\"mergedCellId\":\"p47dtbcp\",\"rowStartIndex\":0,\"columnStartIndex\":0,\"rowEndIndex\":1,\"columnEndIndex\":3}]}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"数据表\",\"style\":{}}}],\"style\":{\"headingLevel\":2}}},{\"type\":\"bitable\",\"bitable\":{\"viewType\":\"grid\"}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"看板\",\"style\":{}}}],\"style\":{\"headingLevel\":2}}},{\"type\":\"bitable\",\"bitable\":{\"viewType\":\"kanban\"}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[]}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"电子表格\",\"style\":{}}}],\"style\":{\"headingLevel\":2}}},{\"type\":\"sheet\",\"sheet\":{\"rowSize\":3,\"columnSize\":4}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[],\"style\":{}}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[{\"type\":\"textRun\",\"textRun\":{\"text\":\"我是网页\",\"style\":{}}}],\"style\":{\"headingLevel\":2}}},{\"type\":\"embeddedPage\",\"embeddedPage\":{\"type\":\"xigua\",\"url\":\"https%3A%2F%2Fwww.ixigua.com%2Fiframe%2F6763174234282787341%3Fautoplay%3D0\",\"width\":637,\"height\":358}},{\"type\":\"paragraph\",\"paragraph\":{\"elements\":[]}}]}}"}'
```

## 响应

### 响应体  
|参数|说明|
|--|--|
|objToken|新建文档的token|
|url|新建文档的访问链接|

### 响应体示例   
```json
{
	"code": 0,
	"data": {
		"objToken": "doccn2EwbGEdcmryBvKzk0loaCd",
		"url": "https://xxx.feishu.cn/docs/doccn2EwbGEdcmryBvKzk0loaCd"
	},
	"msg": "Success"
}
```

### 错误码

:::html
<md-table> 
  <md-thead> 
    <md-tr> 
      <md-th style="width: 15%;">错误码</md-th>  
      <md-th style="width: 25%;">说明</md-th>  
      <md-th style="width: 60%;">排查建议</md-th>  
    </md-tr> 
  </md-thead>  
  <md-tbody> 
    <md-tr>
        <md-td>91401</md-td>
        <md-td>PARAMERR</md-td>
        <md-td>参数出现错误，检查参数有效性</md-td>
    </md-tr>
    <md-tr>
        <md-td>91402</md-td>
        <md-td>NOTEXIST</md-td>
        <md-td>未找到，检查token是否有效</md-td>
    </md-tr>
    <md-tr>
        <md-td>91403</md-td>
        <md-td>FORBIDDEN</md-td>
        <md-td>没有权限，检查是否有文档读权限</md-td>
    </md-tr>
    <md-tr>
        <md-td>91404</md-td>
        <md-td>LOGIN_REQUIRED</md-td>
        <md-td>需要登录</md-td>
    </md-tr>
    <md-tr>
        <md-td>95001</md-td>
        <md-td>internal error</md-td>
        <md-td>内部错误，请稍后重试</md-td>
    </md-tr>
    <md-tr>
        <md-td>95003</md-td>
        <md-td>internal error</md-td>
        <md-td>内部错误，请稍后重试</md-td>
    </md-tr>
    <md-tr>
        <md-td>95005</md-td>
        <md-td>internal error</md-td>
        <md-td>内部错误，请稍后重试</md-td>
    </md-tr>
    <md-tr>
        <md-td>95006</md-td>
        <md-td>Failed</md-td>
        <md-td>文档未找到，检查token是否有效</md-td>
    </md-tr>
    <md-tr>
        <md-td>95007</md-td>
        <md-td>Failed</md-td>
        <md-td>文档已删除，已删除文件无法获取文档meta信息</md-td>
    </md-tr>
    <md-tr>
        <md-td>95008</md-td>
        <md-td>FORBIDDEN</md-td>
        <md-td>检查用户对文档、文件夹的权限</md-td>
    </md-tr>
    <md-tr>
        <md-td>95009</md-td>
        <md-td>Failed</md-td>
        <md-td>没有权限，检查是否有文档读权限。[添加文档权限](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/permission-member/create)</md-td>
    </md-tr>
    <md-tr>
        <md-td>95010</md-td>
        <md-td>internal error</md-td>
        <md-td>内部错误，请稍后重试</md-td>
    </md-tr>
    <md-tr>
        <md-td>95011</md-td>
        <md-td>internal error</md-td>
        <md-td>内部错误，请稍后重试</md-td>
    </md-tr>
    <md-tr>
        <md-td>95013</md-td>
        <md-td>Failed</md-td>
        <md-td>挂载文档失败：无效的folderToken、同一目录不能并发创建、目录无权限或超过目录文件数1500上限</md-td>
    </md-tr>
    <md-tr>
        <md-td>95017</md-td>
        <md-td>具体错误信息</md-td>
        <md-td>读取文档内容失败，检查revison是否正确</md-td>
    </md-tr>
    <md-tr>
        <md-td>95018</md-td>
        <md-td>具体错误信息</md-td>
        <md-td>解析文档内容失败，详见具体错误信息</md-td>
    </md-tr>
    <md-tr>
        <md-td>95020</md-td>
        <md-td>具体错误信息</md-td>
        <md-td>批量更新文档操作失败，详见具体错误信息</md-td>
    </md-tr>
    <md-tr>
        <md-td>95023</md-td>
        <md-td>revision too old</md-td>
        <md-td>版本号太老，请使用最新版本号</md-td>
    </md-tr>
    <md-tr>
        <md-td>95024</md-td>
        <md-td>Failed</md-td>
        <md-td>参数无效，检查参数有效性</md-td>
    </md-tr>
    <md-tr>
        <md-td>95025</md-td>
        <md-td>Failed</md-td>
        <md-td>解析请求失败，检查请求是否合法json</md-td>
    </md-tr>
    <md-tr>
        <md-td>95029</md-td>
        <md-td>folder locked</md-td>
        <md-td>不支持在同一文件夹下并发创建文档，同一文件夹下请串行调用该接口</md-td>
    </md-tr>
        <md-tr>
        <md-td>95030</md-td>
        <md-td>folder size exceeded limit</md-td>
        <md-td>云空间目录下挂载数量超过限制</md-td>
    </md-tr>
    <md-tr>
        <md-td>95050</md-td>
        <md-td>具体错误信息</md-td>
        <md-td>保存文档内容失败，详见具体错误信息</md-td>
    </md-tr>
    <md-tr>
        <md-td>95051</md-td>
        <md-td>具体错误信息</md-td>
        <md-td>创建文档失败，详见具体错误信息</md-td>
    </md-tr>
        <md-tr>
        <md-td>95054</md-td>
        <md-td>this api is deprecated</md-td>
        <md-td>此接口已废弃。请使用[创建文档](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document/create)接口创建新版文档。</md-td>
    </md-tr>
  </md-tbody> 
</md-table>
:::
具体可参考：[服务端错误码说明](/ssl:ttdoc/ukTMukTMukTM/ugjM14COyUjL4ITN)