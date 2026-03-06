---
title: "调用服务端 API"
fullPath: "/uAjLw4CM/ukTMukTMukTM/server-side-sdk/nodejs-sdk/invoke-server-api"
updateTime: "1769589215000"
---

# 调用服务端 API

本文档介绍通过 NodeJS SDK 构造 API 请求、调用开放平台服务端 API 的详细步骤。

## 步骤一：创建并配置 API Client

调用 API 之前，需要先创建一个 API Client，用于指定应用信息、日志级别、超时时间等基本信息。

1. 创建 API Client。
    
    企业自建应用与商店应用的创建方式有所不同，具体说明如下：
    
    - 企业自建应用，使用以下代码创建 API Client。

      ```javascript
      import * as lark from '@larksuiteoapi/node-sdk';

      const client = new lark.Client({
          appId: 'app id',
          appSecret: 'app secret'
      });
      ```

    - 商店应用，使用以下代码创建 API Client，其中需要通过 `appType: lark.AppType.ISV` 标识当前的应用为商店应用。

      ```javascript
      import * as lark from '@larksuiteoapi/node-sdk';

      const client = new lark.Client({
          appId: 'app id',
          appSecret: 'app secret',
          appType: lark.AppType.ISV,
      });
      ```

      :::note  
      **说明**：使用商店应用发起 API 调用时，必须传入租户 Key（tenant_key）以及 app_ticket（用于获取商店应用的 app_access_token）。详细说明参见下文 **商店应用调用 API 的必要操作** 章节。
      :::

2. （可选）自定义 API Client 配置
    
    在创建 API Client 时，支持自定义 API Client 的配置。例如，设置日志级别、缓存器等。Client 构造参数说明如下表所示。
    
    :::html
    <md-table>
    <md-thead>
    <md-tr>
    <md-th style="width:20%">参数</md-th>
    <md-th style="width:15%">类型</md-th>
    <md-th style="width:15%">是否必填</md-th>
    <md-th style="width:50%">描述</md-th>
    </md-tr>
    </md-thead>
    <md-tbody>

    <md-tr>
    <md-td>appId</md-td>
    <md-td>string</md-td>
    <md-td>是</md-td>
    <md-td>应用的 App ID。获取方式：登录[开发者后台](https://open.feishu.cn/app)，在应用详情页的 **凭证与基础信息** 页面内，获取应用凭证（包括 App ID 和 App Secret）。</md-td>
    </md-tr>

    <md-tr>
    <md-td>appSecret</md-td>
    <md-td>string</md-td>
    <md-td>是</md-td>
    <md-td>应用的 App Secret。</md-td>
    </md-tr>

    <md-tr>
    <md-td>domain</md-td>
    <md-td>Domain | string</md-td>
    <md-td>否</md-td>
    <md-td>
	应用域名。一般用于指定飞书域名：
      
   - 飞书：https://open.feishu.cn
   - Lark：https://open.larksuite.com
      
   如需配置其它域名，则需确保传递完整的域名。
      
   **默认值**：Domain.Feishu，该默认值表示使用飞书域名，如果是 Lark 需要设置为 Domain.Lark。  
    </md-td>
    </md-tr>

    <md-tr>
    <md-td>httpInstance</md-td>
    <md-td>HttpInstance</md-td>
    <md-td>否</md-td>
    <md-td>SDK 发送请求的 HTTP 实例。SDK 内部默认使用 `axios.create()` 构造出一个 defaultHttpInstance 进行 HTTP 调用。

   可以从 SDK 中 `import defaultHttpInstance`，在其中添加 interceptors 完成业务需求。例如，SDK 默认过滤了响应结果中的 data，如需获取 logid 等数据，可以重置 interceptors。示例代码如下：
   
   ```javascript 
   import { defaultHttpInstance } from '@larksuiteoapi/node-sdk';

   defaultHttpInstance.interceptors.response.use((resp) => {
      // 这里可以做一些业务逻辑处理

      // 记得返回resp.data 
     return resp.data;
   })
   ```
      
   **默认值**：defaultHttpInstance
    </md-td>
    </md-tr>

    <md-tr>
    <md-td>loggerLevel</md-td>
    <md-td>LoggerLevel</md-td>
    <md-td>否</md-td>
    <md-td>日志级别。枚举值：

   - error：记录错误事件，这些事件阻止了部分程序的执行。
   - warn：记录一些异常问题，但这些异常可能不影响程序继续运行。
   - info：记录运行过程中关键的、需要被监控的信息。
   - debug：记录调试信息，用于在调试时诊断问题。
   - trace：记录详细信息，可用于开发或调试时跟踪程序运行过程。
   
   **默认值**：info</md-td>
    </md-tr>

    <md-tr>
    <md-td>logger</md-td>
    <md-td>Logger</md-td>
    <md-td>否</md-td>
    <md-td>日志器，可根据需要自定义配置。</md-td>
    </md-tr>

    <md-tr>
    <md-td>cache</md-td>
    <md-td>Cache</md-td>
    <md-td>否</md-td>
    <md-td>缓存器，用于缓存数据的存储与获取，如 token。如果你没有指定缓存器，SDK 会初始化一个缓存器。如果需要和现有系统共享数据，可以自定义缓存器，实现 Cache 的接口即可。默认缓存器的实现：[default-cache.ts](https://github.com/larksuite/node-sdk/blob/main/utils/default-cache.ts)
    
   ```javascript
   import get from 'lodash.get';
   import { Cache } from '@node-sdk/typings';

   export class DefaultCache implements Cache {
       values: Map<
           string | Symbol,
           {
               value: any;
               expiredTime?: number;
           } 
       >;

       constructor() {
           this.values = new Map();
       }

       // When there is a namespace, splice the namespace and key to form a new key
       private getCacheKey(key: string | Symbol, namespace?: string) {
           if (namespace) {
               return `${namespace}/${key.toString()}`;
           }
           return key;
       }

       async get(key: string | Symbol, options?: {
           namespace?: string
       }) {
           const cacheKey = this.getCacheKey(key, get(options, 'namespace'));
           const data = this.values.get(cacheKey);

           if (data) {
               const { value, expiredTime } = data;
               if (!expiredTime || expiredTime - new Date().getTime() > 0) {
                   return value;
               }
           }

           return undefined;
       }

       async set(key: string | Symbol, value: string, expiredTime?: number, options?: {
           namespace?: string
       }) {
           const cacheKey = this.getCacheKey(key, get(options, 'namespace'));
           this.values.set(cacheKey, {
               value,
               expiredTime,
           });
           return true;
       }
   }

   export const internalCache = new DefaultCache();
   ```
    </md-td>
    </md-tr>

    <md-tr>
    <md-td>disableTokenCache</md-td>
    <md-td>boolean</md-td>
    <md-td>否</md-td>
    <md-td>是否禁用用于保存 token 的缓存。如果禁用（取值 true），则不会缓存 token，系统会在每次需要使用 token 时自动重新拉取。

   **默认值**：false，表示不禁用</md-td>
    </md-tr>

    <md-tr>
    <md-td>appType</md-td>
    <md-td>AppType</md-td>
    <md-td>否</md-td>
    <md-td>应用类型。默认不传值表示企业自建应用，如果是商店应用则必须传入 AppType.ISV。

   - AppType.ISV：商店应用
   - AppType.SelfBuild：自建应用
   
   **默认值**：AppType.SelfBuild</md-td>
    </md-tr>

    <md-tr>
    <md-td>helpDeskId</md-td>
    <md-td>string</md-td>
    <md-td>否</md-td>
    <md-td>服务台的 ID。仅在调用服务台业务的 API 时需要配置。可在[服务台管理后台](https://feishu.cn/helpdesk/admin) **设置中心** > **API 凭证** 处获取，详情参见[服务台接入指南](/ssl:ttdoc/ukTMukTMukTM/ugDOyYjL4gjM24CO4IjN)。

   **注意**：服务台的 ID、Token 只有服务台创建者可以查看到。
     
   ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/dcc3b0ac14729354c2bc4b44af26c4f9_kscamGsRfP.png?height=693&lazyload=true&width=1916)
    </md-td>
    </md-tr>
      
    <md-tr>
    <md-td>helpDeskToken</md-td>
    <md-td>string</md-td>
    <md-td>否</md-td>
    <md-td>服务台的 token。仅在调用服务台业务的 API 时需要配置。可在[服务台管理后台](https://feishu.cn/helpdesk/admin) **设置中心** > **API 凭证** 处获取，详情参见[服务台接入指南](/ssl:ttdoc/ukTMukTMukTM/ugDOyYjL4gjM24CO4IjN)。

   **注意**：服务台的 ID、Token 只有服务台创建者可以查看到。
   
   ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/dcc3b0ac14729354c2bc4b44af26c4f9_MRSix1MTBO.png?height=693&lazyload=true&width=1916)
    </md-td>
    </md-tr>

    </md-tbody>
    </md-table>
    :::
  
## 步骤二：构造 API 请求

在项目内创建 API Client 后，即可开始调用飞书开放接口。你可以使用 **client.业务域.资源.方法名称** 来定位具体的 API 方法，然后对具体 API 发起调用。建议通过 [API 调试台](https://open.feishu.cn/api-explorer)快速定位 API 方法，以[发送消息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create)接口为例，可以通过地址栏参数拼接 API 方法，也可以查看接口示例代码定位 API 方法，如下图所示。
  
- 方式一：查阅指定 API 的示例代码，从代码中直接获取用于构造 API 请求的方法。
- 方式二：通过指定 API 的浏览器地址栏获取相关参数，以 **client.业务域.资源.方法名称** 格式拼接 API 方法。
  
  - 下图中 ① project 代表 **业务域**
  - 下图中 ② resource 代表 **资源**
  - 下图中 ③ apiName 代表 **方法名称**
  
![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/e4a1d9a22691614ca4fef355a4a365cb_qNqo4NHMwn.png?height=1694&lazyload=true&maxWidth=600&width=2882)
  
在 NodeJS SDK 1.22 版本开始支持多版本的调用，如果遇到某个业务域（project）下的 API 在 SDK 中搜索不到，可通过 project.version 来获取，例如下图，任务（task）下包含 v1、v2 两个版本（version）。
  
![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/71e4da95e5023fe51acb57f27d376865_9rk45yH2y4.png?height=410&lazyload=true&maxWidth=500&width=860)

选择 v2 后，会多出一些方法。

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/7fc8aaab7e6c55e6e5b4258a67acafc0_8JQL1ucgKm.png?height=576&lazyload=true&maxWidth=500&width=1608)

调用的示例代码如下，代码内通过 client 调用发送消息接口。

```javascript
import * as lark from '@larksuiteoapi/node-sdk';

// 构建 API Client
const client = new lark.Client({
    appId: 'app id',
    appSecret: 'app secret'
});

// 通过 Client 调用「发送消息」接口
const res = await client.im.message.create({
    params: {
        receive_id_type: 'chat_id',
    },
    data: {
        receive_id: 'receive_id',
        content: JSON.stringify({text: 'hello world'}),
        msg_type: 'text',
  },
});
```
  
在 SDK 中包含了 API 对应的飞书开放平台 [API 调试台](https://open.feishu.cn/api-explorer)链接，在开发工具内，你可在具体 API 的方法注释中点击 **click to debug** 跳转 API 调试台进行调试。

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/3860ebdf6797d3e75b161bf1409281cd_ent8KutOhk.png?height=234&lazyload=true&maxWidth=500&width=1082)

### 商店应用调用 API 的必要操作

如果使用商店应用调用 API，在 client 中必须声明 `appType: lark.AppType.ISV`，SDK 会根据该声明执行不同的逻辑分支。商店应用的逻辑分支不同于企业自建应用，商店应用必须在代码内传入租户 Key（tenant_key）以及 app_ticket。

:::note  
商店应用调用 API 为什么需要租户 Key（tenant_key）以及 app_ticket：

- [tenant_key](/ssl:ttdoc/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/terminology#495685b5)：一个商店应用会被安装到多个租户中，tenant_key 是租户的唯一标识，用来区分不同的租户。

- [app_ticket](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/application-v6/event/app_ticket-events)：为了提高数据访问的安全性，飞书对商店应用应用增加了`app_ticket`作为安全凭证，用于获取商店应用的 app_access_token。每隔 1 小时向商店应用配置的事件订阅请求地址自动推送一次 `app_ticket`。
:::
  
获取企业的授权访问凭证 `tenant_access_token` 时，需要用到这两个值，但这两个值通过 SDK 无法主动获取到，必须由外部传递进来。因此对于商店应用，SDK 提供了一种方式来传递这两个值。

1. 在应用内订阅 app_ticket 事件。
    
    如何订阅事件参考，具体说明参考 [app_ticket 事件](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/application-v6/event/app_ticket-events)。

2. 在项目中构造好商店应用的 API Client 后，需要使用 `EventDispatcher` 接收并处理 app_ticket 事件。
    
    以 node 的默认 HTTP 服务为例，示例代码如下：
    
    ```javascript
    import * as http from "http";

    const ISVEventDispatcher = new lark.EventDispatcher();

    const server = http.createServer();
    // /webhook/event 为在开放平台配置的事件接收地址的 Path
    server.on('request', lark.adaptDefault('/webhook/event', ISVEventDispatcher));
    server.listen(3000);
    ```
  
    `EventDispatcher` 内部会默认接收 `app_ticket` 事件，将获得的 `app_ticket` 写到缓存（Cache）中。
  
3. 使用 client 调用接口，使用 `withTenantKey` 方法显示传递 `tenant_key` 值。
    
  	client 会结合上一步写入缓存中的 `app_ticket`，完成 `tenant_access_token` 的获取（并缓存），最后发起接口调用请求。

    ```javascript
    import * as fs from "fs";

    const res = await SDKClient.im.file.create({
        data: {
            file_type: "mp4",
            file_name: "测试.mp4",
            file: fs.readFileSync("文件路径"),
        }
     }, lark.withTenantKey('tenant key'));

    console.log(res);
    ```

## 步骤三（可选）：设置请求选项
  
在每次发起 API 调用时，你可以设置请求级别的相关参数，例如传递 userAccessToken（用户访问凭证）、自定义 headers 等。

- 自定义 headers 示例代码如下所示。
  
```javascript
await client.im.message.create({
    params: {
        receive_id_type: 'chat_id',
    },
    data: {
        receive_id: 'receive_id',
        content: JSON.stringify({text: 'hello world'}),
        msg_type: 'text',
    },
}, {
    headers: {
        customizedHeaderKey: 'customizedHeaderValue'
    }
});
```
  
- SDK 内将常用的修改操作封装成了方法，可以使用的方法如下所示。
  
:::html
<md-table>
<md-thead>
<md-tr>
<md-th style="width:30%">方法</md-th>
<md-th style="width:70%">描述</md-th>
</md-tr>
</md-thead>
<md-tbody>

<md-tr>
<md-td>withTenantKey</md-td>
<md-td>设置租户 Key（tenant_key），使用商店应用调用 API 时，必须传入该值。如何获取参见 [tenant_key](/ssl:ttdoc/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/terminology#495685b5)。</md-td>
</md-tr>

<md-tr>
<md-td>withTenantToken</md-td>
<md-td>设置应用身份 Token（tenant_access_token）。获取方式：

- [商店应用获取 tenant_access_token](/ssl:ttdoc/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token)
- [自建应用获取 tenant_access_token](/ssl:ttdoc/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal)</md-td>
</md-tr>

<md-tr>
<md-td>withUserAccessToken</md-td>
<md-td>设置用户身份 Token（user_access_token）。获取方式：[获取 user_access_token](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token)</md-td>
</md-tr>

<md-tr>
<md-td>withHelpDeskCredential</md-td>
<md-td>是否在请求中带入服务台 Token。仅在调用服务台业务的 API 时需要配置，Token 可在[服务台管理后台](https://feishu.cn/helpdesk/admin) **设置中心** > **API 凭证** 处获取，详情参见[服务台接入指南](/ssl:ttdoc/ukTMukTMukTM/ugDOyYjL4gjM24CO4IjN)。

**注意**：服务台的 Token 只有服务台创建者可以查看到。

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/dcc3b0ac14729354c2bc4b44af26c4f9_MRSix1MTBO.png?height=693&lazyload=true&maxWidth=400&width=1916)</md-td>
</md-tr>

<md-tr>
<md-td>withAll</md-td>
<md-td>用于合并上述方法的结果。</md-td>
</md-tr>

</md-tbody>
</md-table>
:::
  
以上方法在代码中的配置示例如下，更多代码示例参考 [request-with.ts](https://github.com/larksuite/node-sdk/blob/main/client/request-with.ts)。
  
```javascript
// 单个方法的使用示例
await client.im.message.create({
    params: {
        receive_id_type: 'chat_id',
    },
    data: {
        receive_id: 'receive_id',
        content: JSON.stringify({text: 'hello world'}),
        msg_type: 'text',
    },
}, lark.withTenantToken('tenant token'));

// 多个方法的使用示例，需要使用 withAll 合并方法
await client.im.message.create({
    params: {
        receive_id_type: 'chat_id',
    },
    data: {
        receive_id: 'receive_id',
        content: JSON.stringify({text: 'hello world'}),
        msg_type: 'text',
    },
}, lark.withAll([
  lark.withTenantToken('tenant token'),
  lark.withTenantKey('tenant key')
]));
```
  
## 步骤四：运行项目

完成以上步骤后，即可运行项目调用 API。你可以通过开发工具运行项目，也可以根据项目部署情况在命令行内通过 `node {.js 项目文件}` 命令运行，如下图所示。

- 运行成功将返回接口响应参数
  
  ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/98e93241e89f978971e5be1168bb6a9c_CfRluI0hXM.png?height=880&lazyload=true&maxWidth=500&width=1080)
  
- 运行失败则会返回对应的错误码与错误信息
  
  ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/de226cbbcb3e54ff8e9d0c26645421ce_8uIIDtP7qL.png?height=840&lazyload=true&maxWidth=500&width=2220)
  
## API 调用方式介绍

NodeJS SDK 为了提高 API 调用效率，封装了部分 API 的调用方法，包括分页查询、上传文件、下载文件等。

### 分页查询

针对返回值以分页形式呈现的接口，SDK 提供了迭代器方式的封装（方法名后缀为 WithIterator），消除了根据 page_token 反复获取数据的操作，提升易用性。例如，以[获取部门直属用户列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/find_by_department)接口为例，分页查询方式如下所示。

```javascript
// 每次处理20条数据
for await (const items of await client.contact.user.findByDepartment({
    params: {
        department_id: '0',
        page_size: 20,
    },
})) {
    console.log(items);
}

// 也可用next来手动控制迭代，每次取20条数据
const listIterator = await SDKClient.contact.user.findByDepartment({
    params: {
        department_id: '0',
        page_size: 20,
    },
});
const { value } = await listIterator[Symbol.asyncIterator]().next();
console.log(value);
```

你也可以使用无迭代器封装的版本，需要自己每次根据返回的 page_token 来手动进行分页调用。

### 上传文件

SDK 内封装了对文件上传的处理逻辑，和普通的 API 调用方式一样，以[上传文件](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/file/create)接口为例，传递参数即可调用。

```javascript
const res = await client.im.file.create({
    data: {
        file_type: 'mp4',
        file_name: 'test.mp4',
        file: fs.readFileSync('file path'),
    },
});
```

如果以上方式实际应用时报错 1061002，可以尝试将 file 类型变为 stream。示例代码如下：

```javascript
let Duplex = require('stream').Duplex;
 
function bufferToStream(buffer) {  
  let stream = new Duplex();
  stream.push(buffer);
  stream.push(null);
  return stream;
}
```

### 下载文件

SDK 对返回的二进制流进行了封装，消除了对流本身的处理，调用[下载文件](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/file/get)接口时，只需要调用 writeFile 方法即可将数据写入文件。

```javascript
const resp = await client.im.file.get({
    path: {
        file_key: 'file key',
    },
});
await resp.writeFile(`filepath.suffix`);
```

如果想要自定义对流的处理，可以调用 getReadableStream 方法获取到流，如下示例将流写入文件。

```javascript
import * as fs from 'fs';

const resp = await client.im.file.get({
    path: {
        file_key: 'file key',
    },
});
const readableStream = resp.getReadableStream();
const writableStream = fs.createWriteStream('file url');
readableStream.pipe(writableStream);
```

:::note
**注意**：流只能被消费一次，即如果使用了 writeFile 消费了流，则 getReadableStream 获取流会报错或者获取到的流为空。如需消费多次流，可以使用 getReadableStream 获取流，然后读取流中的数据做缓存，将缓存的数据给消费方使用。
:::

### 飞书卡片

开放平台提供了[卡片模板](/ssl:ttdoc/uAjLw4CM/ukzMukzMukzM/feishu-cards/send-feishu-card#718fe26b)能力，在[发送卡片消息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create)时只需要提供模板 ID 和内容即可。SDK 对卡片模板进行了调用上的封装，在支持消息卡片的接口中增加了 ByCard 的调用方式，你只需要传递 `template_id` 和 `template_variable` 即可。

```javascript
client.im.message.createByCard({
  params: {
    receive_id_type: 'chat_id',
  },
  data: {
    receive_id: 'your receive_id',
    template_id: 'your template_id',
    template_variable: {
      content: "Card Content",
      title: "Card Title"
    }
  }
});
```

如果你需要基于卡片的 JSON 数据发送消息，以调用[发送消息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create)接口发送一个简单的具备 `title` 和 `content` 的卡片为例，示例代码如下。

```javascript
client.im.message.create({
  params: {
    receive_id_type: 'chat_id',
  },
  data: {
    receive_id: 'your receive_id',
    content: JSON.stringify({
        "config": {
          "wide_screen_mode": true
        },
        "elements": [
          {
            "tag": "markdown",
            "content": "Card Content"
          }
        ],
        "header": {
          "template": "blue",
          "title": {
            "content": "Card Title",
            "tag": "plain_text"
          }
        }
      }
    ),
    msg_type: 'interactive'
  }
})
```

示例效果如下：

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/9d27fcddc76396b4ab5b20b43f97c8d8_lOuLAagpBA.png?height=210&lazyload=true&maxWidth=500&width=1224)

SDK 内置了一个基础消息卡片供你体验。

```javascript
import * as lark from '@larksuiteoapi/node-sdk';
client.im.message.create({
  params: {
    receive_id_type: 'chat_id',
  },
  data: {
    receive_id: 'your receive_id',
    content: lark.messageCard.defaultCard({
      title: 'Card Title',
      content: 'Card Content'
    }),
    msg_type: 'interactive'
  }
})
```

示例效果如下：

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/9d27fcddc76396b4ab5b20b43f97c8d8_seTUt6LN9m.png?height=210&lazyload=true&maxWidth=500&width=1224)
  
## 常见问题

### 如何快速获取接口对应的示例代码？

飞书开放平台提供了 [API 调试台](https://open.feishu.cn/api-explorer)，通过该平台可以快速调试服务端 API，快速获取资源 ID 及生成多语言示例代码的能力，为您节省开发成本。例如，通过 API 调试台调用[发送消息](https://open.feishu.cn/api-explorer/cli_a61e4f821889d00c?apiName=create&from=op_doc_tab&project=im&resource=message&version=v1)接口，在调试台成功完成测试后，可通过 **示例代码** 页面查阅 Node SDK 对应的接口调用代码。

![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/58e96229a8333d013f3c54eac9d4ce8d_it8ldccDWh.png?height=1324&lazyload=true&maxWidth=600&width=2878)

### 如何调用历史版本 API、API 调试台搜索不到的 API、SDK 内找不到方法的 API ？

可以使用 SDK 提供的原生模式调用 API（需要使用 Client 上的 request 方法）。

```js
import * as lark from '@larksuiteoapi/node-sdk';

const client = new lark.Client({
    appId: 'app id',
    appSecret: 'app secret'
});

const res = await client.request({
    method: 'POST',
    url: 'xxx',
    data: {},
    params: {},
});
```
参数说明如下，你可以通过具体的 API 文档获取以下接口信息。例如：[发送消息](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create)

- method：指定 API 所需的 HTTP Method。
- url：指定 API 的 HTTP URL，如果接口有路径参数也需要拼接在 url 内。
- data：接口的请求体。
- params：接口的查询参数。

### 在 Client 中自定义 domain 时 URL 后是否需要 ‘/’ ？

不需要。例如：`domain: https://www.example.com` 后面不需要加 `/`。

### 调用 API 时 Query 参数为列表如何传值？

- 方式一：将 NodeJS SDK 升级到 1.37.2 版本解决。
- 方式二：使用 paramsSerializer 并通过 [https://www.npmjs.com/package/qs](https://www.npmjs.com/package/qs) 序列化参数。

	```js
    axios.get('/myController/myAction', {
      params: {
        storeIds: [1,2,3]
      },
      paramsSerializer: params => {
        return qs.stringify(params)
      }
    })
	```
### Token 的自动获取、缓存与刷新

SDK 默认会自动管理 `tenant_access_token` 的获取、缓存和刷新。您在初始化 `Client` 时只需提供 `appId` 和 `appSecret`，SDK 会在首次调用 API 前自动请求 Token，并将其缓存在Cache。
为防止因网络延迟等因素导致 Token 在传输过程中恰好过期，SDK 会在其 `expire` 时间的基础上**提前 3 分钟**将其置为失效，并在下次请求时重新获取，从而有效避免临界点过期的风险。
```javascript
import { Client } from '@larksuiteoapi/node-sdk';
// 只需要提供 App ID 和 App Secret
const client = new Client({
    appId: 'YOUR_APP_ID',
    appSecret: 'YOUR_APP_SECRET',
});
// 直接调用 API，SDK 会自动处理 Token
async function main() {
    const response = await client.im.message.create({
        /* ...params */
    });
    console.log(response);
}
```
**实践建议**：
- 除非有特殊需求（如自行实现中心化的 Token 管理服务），否则**建议**保持默认行为，这是最高效、最简单的使用方式。
- 飞书开放平台 API Explorer 中的示例代码为了方便调试，可能会展示 `lark.withTenantToken("token")` 的用法。这种方式适用于临时测试，但在生产环境中**不推荐**，因为 Token 会过期，硬编码或手动传递会导致服务中断。

### 禁用缓存与手动传递 Token

在某些场景下（例如，在 Serverless 等无状态环境中使用外部缓存），您可以禁用 SDK 的内置缓存。将 `disableTokenCache` 设置为 `true` 后，每次 API 请求都**必须**通过 `lark.withTenantToken()` 或 `lark.withUserAccessToken()` 手动传递有效 Token。
```javascript
import { Client, withTenantToken } from '@larksuiteoapi/node-sdk';
const client = new Client({
    appId: 'YOUR_APP_ID',
    appSecret: 'YOUR_APP_SECRET',
    disableTokenCache: true, // 禁用内置 Token 缓存
});
async function sendMessageWithManualToken(token: string) {
    const res = await client.im.chat.list(
        {},
        withTenantToken(token) // 每次调用都必须手动传递 Token
    );
    console.log(res);
}
```
**注意**：如果禁用了缓存却未手动传递 Token，将会收到 `Missing access token for authorization` 的错误（错误码 `99991661`）。

### 使用 `withUserAccessToken` 代表用户调用

当需要代表某个用户执行操作时（例如，操作该用户的云空间文件），应使用 `withUserAccessToken` 来传递该用户的 `user_access_token`。
```javascript
import { Client, withUserAccessToken } from '@larksuiteoapi/node-sdk';
const client = new Client({
    appId: 'YOUR_APP_ID',
    appSecret: 'YOUR_APP_SECRET',
});
// 使用 User Access Token 访问用户云空间
async function listUserDriveFiles(userToken: string) {
    const res = await client.drive.file.list(
        {}, 
        withUserAccessToken(userToken) // 传入用户的 Access Token
    );
    console.log(res.data.files);
}
```

### 自定义缓存实现

如果您希望将 Token 存储在 Redis 或其他外部存储中，可以自定义缓存实现。只需创建一个符合 `ICache` 接口（`get`, `set`, `has` 方法）的对象，并在初始化客户端时传入即可。
```javascript
import { Client, ICache } from '@larksuiteoapi/node-sdk';
// 示例：使用 Map 实现的简单缓存，实际场景可替换为 Redis
class RedisCache implements ICache {
    // private redisClient; // 假设这是您的 Redis 客户端实例
    async set(key: string, value: any, expired?: number): Promise<void> {
        // 在实际场景中，您可以将 expired 参数用于 Redis 的 TTL
        // await this.redisClient.set(key, JSON.stringify(value), { EX: expired });
        console.log(`Setting cache for key: ${key}`);
    }
    async get(key: string): Promise<any> {
        // const value = await this.redisClient.get(key);
        // return value ? JSON.parse(value) : null;
        console.log(`Getting cache for key: ${key}`);
        return null;
    }
    async has(key: string): Promise<boolean> {
        // const exists = await this.redisClient.exists(key);
        // return exists === 1;
        console.log(`Checking cache for key: ${key}`);
        return false;
    }
}
const client = new Client({
    appId: 'YOUR_APP_ID',
    appSecret: 'YOUR_APP_SECRET',
    cache: new RedisCache(),
});
```
**多实例Client的缓存隔离**
从 SDK `v1.10.0` 版本开始，默认的内存缓存已支持**基于 App ID 的** **命名空间** **隔离**。这意味着每个 `Client` 实例会自动拥有独立的缓存空间，您无需额外配置即可安全地在同一进程中使用多个 `Client` 实例。
如果您使用自定义缓存（如上例），请确保您的缓存 `key` 设计中也包含了 `appId` 作为隔离维度，以防止不同应用的 Token 发生混淆。SDK 传递给 `cache.set` 的 `key` 默认已包含 `appId`，您直接使用即可。

### 获取完整的响应信息（如 Log ID）

默认情况下，SDK 的 API 调用仅返回响应体中的 `data` 部分。如果您需要获取完整的响应信息，例如 `headers`（其中包含 `X-Tt-Logid` 用于问题排查），可以通过修改 `axios` 拦截器来实现。
**差异说明：自定义拦截器与响应结构风险**
SDK 允许通过修改 `defaultHttpInstance` 或传入自定义 `httpInstance` 来添加拦截器，但这两种方式在修改响应结构时存在不同级别的风险。
- **方式一（低风险）：修改默认** **实例** **以获取额外信息** 如果您只是想获取 `logid` 等额外信息，然后继续返回 `resp.data`，可以直接修改 `defaultHttpInstance`。这种方式风险较低，因为 SDK 的 Token 管理逻辑最终仍然能拿到期望的 `data` 结构。
- **方式二（高风险）：传入自定义** **实例** **并改变响应结构** 如果您在初始化 `Client` 时传入一个全新的 `httpInstance`，并在其响应拦截器中彻底改变了返回结构（例如，返回 `resp` 而不是 `resp.data`），这会**破坏** **SDK** **内置的 Token 管理机制**，导致 Token 获取和刷新失败。
**结论**：除非您完全理解 SDK 内部机制并打算自行管理 Token，否则**不要**在自定义 `httpInstance` 的响应拦截器中改变最终返回给 SDK 的数据结构。
**示例：仅获取** **Log ID** **，不破坏原有流程**
```javascript
import { defaultHttpInstance } from '@larksuiteoapi/node-sdk';
// 清空默认的响应拦截器
defaultHttpInstance.interceptors.response.handlers = [];
// 添加一个新的拦截器，返回完整的响应对象
defaultHttpInstance.interceptors.response.use((resp) => {
    // resp 对象包含 headers, status, data 等完整信息
    console.log('Log ID:', resp.headers['x-tt-logid']);
  
    // 您可以在这里进行自定义处理，但最后必须返回 data 以确保 SDK 正常工作
    return resp.data;
});
// 在此之后的所有 API 请求都将经过新的拦截器
```

### 批量添加自定义请求头

如果您需要为所有发出的 API 请求统一添加自定义 Header（例如，用于网关验证、链路追踪），可以利用 `request` 拦截器实现。
```javascript
import { defaultHttpInstance } from '@larksuiteoapi/node-sdk';
defaultHttpInstance.interceptors.request.use(
  (req) => {
    if (req.headers) {
      req.headers['X-Custom-Header'] = 'Your-Value';
    }
    return req;
  }
);
```
### 如何定位语义化方法？

SDK 的核心优势之一是提供了与飞书开放平台 [API Explorer](https://open.feishu.cn/api-explorer) 一致的语义化调用方法。您可以根据 API 文档或调试台的 URL 路径来拼接对应的方法名，其结构遵循 `client.{project}.{resource}.{method}`。
**示例**：获取用户信息的 API `https://open.feishu.cn/open-apis/contact/v3/users/:user_id`：
- `project`: `contact`
- `version`: `v3`
- `resource`: `user`
- `method`: `get` (HTTP 方法)
对应的 SDK 调用为 `client.contact.v3.user.get()`。
**实践建议**：
- **最快方式**：在 API Explorer 页面的代码示例中，可以直接找到对应的 Node.js SDK 用法。
- **版本注意**：如果某个 API 在 `client.{project}` 下找不到，请尝试加上版本号，如 `client.{project}.{version}`。

### API 多版本支持

从 `v1.22.0` 版本开始，SDK 支持了 API 的多版本调用。当一个 API 有多个版本时（例如 `v1`, `v2`），建议**显式指定版本号**进行调用，以使用最新的功能和定义。
```javascript
// 调用 v1 版本的创建任务接口
await client.task.v1.task.create({ /* ... */ });
// 调用 v2 版本的创建任务接口
await client.task.v2.task.create({ /* ... */ });
```
**说明**：为了保持向后兼容，不带版本号的调用方式（如 `client.task.comment.create`）将继续指向 `v1.22.0` 版本发布时所固化的历史版本。

### 如何处理数组形式的 Query 参数？

对于某些 GET 请求，其查询参数（Query Parameter）可能是一个数组，例如批量获取用户信息时传递多个 `user_id`。
**解决方案**：
- **方案一（推荐）** ：**升级** **SDK** **到** **`1.37.2`** **或更高版本**。从该版本开始，SDK 内部已自动处理数组参数的序列化，您可以直接在 `params` 中传递数组。
- **方案二（旧版** **SDK** **）** ：如果暂时无法升级，可以手动调用 `client.request` 方法，并提供自定义的 `paramsSerializer` 函数，将数组参数“拍平”。
```javascript
import qs from 'qs';
// 仅适用于无法升级 SDK 的旧版处理方式
await client.request({
  url: '/open-apis/contact/v3/users/batch',
  method: 'GET',
  params: {
    user_ids: ['ou_xxx', 'ou_yyy'], // 直接传递数组
  },
  // 使用 qs 库来序列化参数
  paramsSerializer: params => {
    return qs.stringify(params, { arrayFormat: 'repeat' });
  },
});
```

### SDK未覆盖的 API 如何调用？
尽管 SDK 的目标是覆盖所有飞书开放平台 API，但由于文档结构、发布周期或灰度测试等原因，仍有少量 API 未被包含。
对于这种情况，您可以使用通用的 `client.request` 方法来发起调用，它提供了与 `axios` 类似的配置项。
```javascript
const response = await client.request({
  method: 'POST',
  url: '/open-apis/some/unsupported/api/v1',
  data: {
    // request body
  },
  params: {
    // query params
  }
});
```

### 在 Cloudflare Workers 等非 Node.js 环境中使用

Cloudflare Workers、Deno 等现代 Serverless 环境基于 Fetch API，与标准的 Node.js 环境不同。`axios`（SDK 的底层依赖）的默认 `adapter` 在这些环境下无法工作，会导致 `adapter is not a function` 的错误。
**解决方案**：您需要手动为 `axios` 实例更换一个兼容 Fetch API 的适配器，例如 `@haverstack/axios-fetch-adapter`。
**差异说明：两种适配方式**
有两种方式可以实现对 Cloudflare Workers 的适配，它们效果相同，您可以根据自己的代码风格和是否需要更多自定义 `axios` 功能来选择。
- **方式一（推荐）：传入自定义** **`httpInstance`** 这种方式更灵活，允许您在创建 `axios` 实例时进行更多配置（如设置超时、添加拦截器等）。
- **方式二：直接修改默认** **实例** **的** **`adapter`** 这种方式更直接，如果您只需要更换 `adapter` 而不做其他改动，代码会更简洁。
**方式一：传入自定义** **`httpInstance`** **（推荐）**
```javascript
import { Client } from '@larksuiteoapi/node-sdk';
import axios from 'axios';
import fetchAdapter from '@haverstack/axios-fetch-adapter';
// 1. 创建一个配置了 fetch adapter 的 axios 实例
const customHttpInstance = axios.create({
    adapter: fetchAdapter,
    // 您还可以在此添加其他 axios 配置
});
// 2. 初始化 Client 时传入该实例
const client = new Client({
    appId: 'YOUR_APP_ID',
    appSecret: 'YOUR_APP_SECRET',
    httpInstance: customHttpInstance,
});
// 现在 client 可以在 Cloudflare Workers 环境中正常发起请求
```
**方式二：直接修改默认** **实例** **的** **`adapter`**
```javascript
import { Client } from '@larksuiteoapi/node-sdk';
import fetchAdapter from '@haverstack/axios-fetch-adapter';
const client = new Client({
  appId: 'YOUR_APP_ID',
  appSecret: 'YOUR_APP_SECRET',
});
// 直接更换默认 HTTP 实例的适配器
client.httpInstance.defaults.adapter = fetchAdapter;
// 现在 client 同样可以正常发起请求
```

### Deno 支持现状

当前 SDK 主要为 Node.js 环境设计，并未正式支持 Deno。主要障碍是底层依赖（如 `axios`）的打包和环境兼容性问题。社区有通过 `import_map` 强制指定 `axios` 兼容版本的临时方案，但这并非官方支持，且可能随依赖更新而失效。
如果您需要在 Deno 环境中调用飞书 API，现阶段更稳妥的选择是直接使用 Deno 内置的 `fetch` API 进行调用。

### 分页与迭代器
SDK 为许多支持分页的 `list` 接口提供了便捷的迭代器封装（如 `client.im.chat.listWithIterator()`），可以自动处理分页逻辑。
但是，并非所有分页接口都支持此特性。如果某个 `list` 接口没有提供对应的 `...WithIterator` 方法，这通常是因为其 API 定义不符合自动生成迭代器的规范。在这种情况下，您需要手动进行分页轮询：
```javascript
async function listAllItemsManually(client) {
  let allItems = [];
  let pageToken: string | undefined = undefined;
  let hasMore = true;
  while (hasMore) {
    const res = await client.im.chat.list({ // 假设此接口无迭代器
      params: {
        page_size: 100,
        page_token: pageToken,
      },
    });
    if (res.data.items) {
      allItems = allItems.concat(res.data.items);
    }
    
    hasMore = res.data.has_more;
    pageToken = res.data.page_token;
  }
  return allItems;
}
```
**何时使用手动分页 vs. 语义化方法？**
- **优先使用迭代器**：如果 `client.{...}.listWithIterator` 方法存在，请始终优先使用它，代码更简洁且不易出错。
- **备选手动** **轮询**：仅在迭代器方法缺失时，采用上述手动分页轮询的模式。

### 注册与处理事件
`EventDispatcher` 是处理所有事件订阅的核心。您可以通过 `register` 方法为不同类型的事件注册异步处理函数，并在您的 Web 框架中调用 `invoke` 方法进行分发。
```javascript
import { Client, EventDispatcher } from '@larksuiteoapi/node-sdk';
import express from 'express';
// 1. 初始化 Client 和 EventDispatcher
const client = new Client({ /* ... */ });
const eventDispatcher = new EventDispatcher({
    verificationToken: 'YOUR_VERIFICATION_TOKEN',
    encryptKey: 'YOUR_ENCRYPT_KEY', // 如果开启了加密
}).register({
    // 2. 注册消息接收事件处理器
    'im.message.receive_v1': async (event) => {
        console.log('Received message event:', event);
        const { message } = event;
        // 在此处理您的业务逻辑，例如回复消息
        if (message.message_type === 'text') {
            await client.im.message.reply({
                path: { message_id: message.message_id },
                data: {
                    content: JSON.stringify({ text: '消息已收到！' }),
                    msg_type: 'text',
                },
            });
        }
        return { success: true };
    },
    'contact.user.created_v3': async (data) => {
        console.log('New user created:', data);
    }
});
// 3. 在您的 Web 框架中调用
const app = express();
app.use(express.json());
app.post('/webhook/event', (req, res) => {
    const data = { headers: req.headers, body: req.body };
    
    // 建议：先响应 200，再异步处理，避免超时重试
    res.status(200).send('OK');
    eventDispatcher.invoke(data).catch(err => {
        console.error('Event processing error:', err);
    });
});
app.listen(3000, () => console.log('Server is running on port 3000'));
```

### URL 验证挑战（Challenge）

当您在开放平台配置事件订阅的 Request URL 时，飞书会向该 URL 发送一个 `url_verification` 类型的 `challenge` 请求。SDK 内置的 `EventDispatcher` 或框架适配器（如 Express, Koa）会**自动处理此过程**，您无需编写任何特殊代码。只要您的服务能正确接收请求并将其传递给 SDK，验证就会自动通过。

### 避免事件重复推送与事件去重

飞书的事件推送机制要求您的服务在收到事件后的 **3 秒内** 返回 HTTP 200 状态码。如果超时未收到响应，飞书会认为推送失败并进行重试，这会导致您的业务逻辑被重复执行。
**综合解决方案**：
1. **快速响应，** **异步** **处理**：在您的 HTTP 路由处理函数中，**立即响应 200 OK**，然后将事件数据传递给后台进行异步处理。这可以从根本上避免因处理耗时过长导致的超时重试。
1. **业务侧** **幂等** **设计**：即使快速响应，网络抖动等原因仍可能导致事件重复。因此，业务侧进行幂等性设计至关重要。飞书的每个事件都包含一个唯一标识符，可用于去重：
    1. **V2.0 协议事件**：`header.event_id`
    1. **V1.0 协议事件**：`uuid`
**示例：结合快速响应和内存去重（生产环境建议使用** **Redis** **）**
```javascript
const processedEventIds = new Set<string>();
// 在事件处理器中增加去重逻辑
eventDispatcher.register({
    'im.message.receive_v1': async (event) => {
        const eventId = event.header.event_id;
        
        if (processedEventIds.has(eventId)) {
            console.log(`Event ${eventId} already processed, skipping.`);
            return;
        }
        // ... 执行您的业务逻辑 ...
        processedEventIds.add(eventId);
        
        // 设置一个定时器来清理旧的 ID，防止内存无限增长
        setTimeout(() => processedEventIds.delete(eventId), 5 * 60 * 1000); // 5 分钟后清理
    },
});
```

### 处理未在 SDK 中定义的事件

由于文档同步延迟或版本较老，某些事件类型可能未在 SDK 的 TypeScript 定义中提供。此时，您可以直接将事件的字符串名称作为 `key` 进行注册。这在运行时是有效的，只是在编译时会有类型检查错误。
**差异说明：处理未知事件的两种方式**
- **方式一（简单直接）：使用** **`@ts-ignore`** 这是最快捷的方式，只需在注册的代码行上方添加 `// @ts-ignore` 即可忽略 TypeScript 的类型检查错误。
- **方式二（类型安全）：使用泛型** 如果您希望在处理未知事件时也能获得一定的类型提示，可以在 `.register()` 方法上使用泛型，手动定义事件体的接口。
**方式一：使用**`@ts-ignore`
```javascript
eventDispatcher.register({
    // @ts-ignore
    'approval.instance.status_changed_v4': async (data: any) => {
        console.log('Handling custom event:', data);
    }
});
```
**方式二：使用泛型**
```javascript
interface MyCustomEventData {
    // 根据实际事件体定义接口
    approval_code: string;
    status: string;
}
eventDispatcher.register<{ 'approval.instance.create_v4'?: MyCustomEventData }>({
    'approval.instance.create_v4': async (data) => {
        // 此时 `data` 会被推断为 MyCustomEventData 类型
        console.log(data.approval_code);
    }
});
```

### 发送与更新消息卡片

- **发送卡片**：调用 `client.im.message.create`，将 `msg_type` 设置为 `interactive`，并将卡片 JSON 结构字符串化后作为 `content` 发送。
- **更新卡片**：对于已发送的交互式卡片，可以使用 `client.im.message.patch` 方法通过 `message_id` 对其进行更新。这对于实现延迟响应或多步交互非常有用。
```javascript
// 示例：发送并随后更新一张卡片
async function sendAndUpdateCard(chatId: string) {
    // 1. 发送初始卡片
    const initialCard = { /* ... 卡片 JSON ... */ };
    const createRes = await client.im.message.create({
        params: { receive_id_type: 'chat_id' },
        data: {
            receive_id: chatId,
            msg_type: 'interactive',
            content: JSON.stringify(initialCard),
        },
    });
    const messageId = createRes.data?.message_id;
    if (!messageId) return;
    // 2. 延迟 5 秒后，使用 patch 方法更新卡片
    setTimeout(async () => {
        const updatedCard = { /* ... 新的卡片 JSON ... */ };
        await client.im.message.patch({
            path: { message_id: messageId },
            data: { content: JSON.stringify(updatedCard) },
        });
        console.log('Card updated successfully.');
    }, 5000);
}
```

### 卡片交互回调验签失败

如果您使用了新版消息卡片（Interactive Message Card 2.0），并遇到了交互回调的验签失败问题，这通常是因为 SDK 版本过低。
**解决方案**：请将 `@larksuiteoapi/node-sdk` 升级到 **`1.27.0`** **或更高版本**。该版本已兼容新版卡片的验签逻辑。
```javascript
// 检查当前版本
npm list @larksuiteoapi/node-sdk
// 升级到最新版本
npm install @larksuiteoapi/node-sdk@latest
```

### `fields` 字段的格式：使用对象而非 Map

在创建（`create`）或更新（`update`/`batchUpdate`）多维表格记录时，`fields` 字段应为一个 **JavaScript 普通对象 (Object)** ，其 `key` 为字段名，`value` 为对应的值。
```javascript
await client.bitable.appTableRecord.create({
  path: {
    app_token: 'YOUR_APP_TOKEN',
    table_id: 'YOUR_TABLE_ID',
  },
  data: {
    fields: {
      "文本字段": "这是一个字符串",
      "数字字段": 123,
      "单选字段": "选项A",
    },
  },
});
```
**注意**：API Explorer 或旧文档中可能存在使用 `Map` 对象的错误示例，这是不正确的。请始终使用普通对象。

### 清空单元格：使用 `null`

要清空一个或多个单元格的内容，可以在更新记录时将对应字段的值设置为 `null`。
**注意**：将字段值设置为 `undefined` 是**无效**的。该字段在请求中会被忽略，无法达到清空单元格的效果。
```javascript
await client.bitable.appTableRecord.update({
  path: {
    app_token: 'YOUR_APP_TOKEN',
    table_id: 'YOUR_TABLE_ID',
    record_id: 'recXXXXX',
  },
  data: {
    fields: {
      "需要清空的字段": null,
      "另一个需要清空的字段": null,
    },
  },
});
```

### 处理多维表格相关事件

多维表格的事件（如记录变更 `drive.file.bitable_record_changed_v1`）同样通过 `EventDispatcher` 订阅和处理。如果某些事件在 SDK 的类型定义中缺失，您可以参考上文“处理未在 SDK 中定义的事件”一节进行手动注册。
要了解 `field_value` 中各种字段类型对应的 JSON 结构，请参考开放平台的官方文档：[数据结构概述](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/bitable/development-guide/bitable-structure)。

### 文件上传：优先使用 Stream

无论是上传到云空间（`drive.file.uploadAll`）还是作为消息附件发送图片（`im.image.create`），都**建议优先使用文件流 (Stream)** 而非 Buffer。Stream 的内存效率更高，尤其适合大文件，可以有效避免内存溢出。
```javascript
import * as fs from 'fs';
const filePath = '/path/to/your/file.png';
const fileStream = fs.createReadStream(filePath);
const fileSize = fs.statSync(filePath).size;
await client.drive.file.uploadAll({
  data: {
    file_name: 'my-image.png',
    parent_type: 'explorer',
    parent_node: 'YOUR_FOLDER_TOKEN',
    size: fileSize,
    file: fileStream,
  },
});
```

### 文件下载/导出：处理返回的流

对于文件下载（`drive.file.download`）或表格导出等操作，从 SDK `v1.37.0` 版本开始，已支持直接获取文件流 (`ReadableStream`)。您可以直接将其 `pipe` 到一个文件写入流中，从而高效处理大文件。
```javascript
import * as fs from 'fs';
const resp = await client.im.file.get({
    path: {
        file_key: 'file key',
    },
});
const readableStream = resp.getReadableStream();
const writableStream = fs.createWriteStream('file url');
readableStream.pipe(writableStream);
```

### Node.js v18+ 文件上传兼容性策略

在 `node-sdk` 的 `v1.17.1` 之前的版本中，使用 Node.js v18+ 并通过 `Buffer` 上传文件时，可能会遇到 `source.on is not a function` 的错误。这是因为 Node.js v18 引入了原生的 `Blob` 类型，导致 `axios` 的依赖库 `form-data` 内部逻辑出现兼容性问题。
**最佳实践与解决方案**
1. **升级 SDK (推荐)** ：将 `@larksuiteoapi/node-sdk` 升级到 **`1.17.1`** **或更高版本**，该版本已从内部解决此兼容性问题。
1. **使用 Stream (推荐)** ：如上所述，始终优先使用 `fs.createReadStream` 进行文件上传。这不仅是最佳实践，也能从根本上规避不同 Node.js 版本间的底层差异。
1. **缓解措施 (如无法升级)** ：如果暂时无法升级 SDK，可以将 `Buffer` 手动转换为 `Stream` 作为临时解决方案。
**缓解措施示例：Buffer 转 Stream**
```javascript
import { Duplex } from 'stream';
function bufferToStream(buffer: Buffer): Duplex {
  const stream = new Duplex();
  stream.push(buffer);
  stream.push(null);
  return stream;
}
// 在上传时使用
// const fileBuffer = fs.readFileSync(filePath);
// const fileStream = bufferToStream(fileBuffer);
// ... 然后在 API 调用中传递 fileStream
```

### 如何实现自定义日志记录？

您可以通过为 `Client` 提供自定义的 `logger` 来接管 SDK 的日志输出。`logger` 需要实现 `debug`, `info`, `warn`, `error` 四个方法。
```javascript
import { Client, ILogger, LogLevel } from '@larksuiteoapi/node-sdk';
class MyCustomLogger implements ILogger {
    debug(message: any, ...args: any[]) { console.debug(`[SDK-DEBUG]`, message, ...args); }
    info(message: any, ...args: any[]) { console.info(`[SDK-INFO]`, message, ...args); }
    warn(message: any, ...args: any[]) { console.warn(`[SDK-WARN]`, message, ...args); }
    error(message: any, ...args: any[]) { console.error(`[SDK-ERROR]`, message, ...args); }
}
const client = new Client({
    appId: 'YOUR_APP_ID',
    appSecret: 'YOUR_APP_SECRET',
    logger: new MyCustomLogger(),
    logLevel: LogLevel.DEBUG, // 设置日志级别，如 'debug'
});
```
此外，结合自定义 `axios` 实例的拦截器，您可以实现更详细的 HTTP 请求级别日志。