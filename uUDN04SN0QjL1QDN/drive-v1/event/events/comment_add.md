---
title: "添加评论、回复通知事件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/notice/events/comment_add"
updateTime: "1775123703000"
---

# 添加评论、回复通知事件

当用户有新文档评论或回复通知会触发此事件。{使用示例}(url=/api/tools/api_explore/api_explore_config?project=drive&version=v1&resource=notice&event=comment_add)


> **Tip**: 了解事件订阅的使用场景和配置流程，参考[事件订阅概述](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)。


## 说明

用户身份订阅需要先调[订阅用户云文档事件](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/user/subscription)接口。应用身份无需调用。

## 事件

| 项目 | 值 |
| --- | --- |
| 事件类型 | drive.notice.comment_add_v1 |
| 支持的应用类型 | custom,isv |
| 权限要求             订阅该事件所需的权限，开启其中任意一项权限即可订阅 | `docs:document.comment:read` 获取云文档中的评论 |
| 字段权限要求 | > **Tip**: 该接口返回体中存在下列敏感字段，仅当开启对应的权限后才会返回；如果无需获取这些字段，则不建议申请 `contact:user.employee_id:readonly` 获取用户 user ID |
| 推送方式 | `Webhook` |


### 事件体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `schema` | `string` | 事件模式 |
| `header` | `event_header` | 事件头 |
| &nbsp;&nbsp;└ `event_id` | `string` | 事件 ID |
| &nbsp;&nbsp;└ `event_type` | `string` | 事件类型 |
| &nbsp;&nbsp;└ `create_time` | `string` | 事件创建时间戳（单位：毫秒） |
| &nbsp;&nbsp;└ `token` | `string` | 事件 Token |
| &nbsp;&nbsp;└ `app_id` | `string` | 应用 ID |
| &nbsp;&nbsp;└ `tenant_key` | `string` | 租户 Key |
| `event` | `\-` | \- |
| &nbsp;&nbsp;└ `notice_meta` | `notice` | 通知元信息 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `file_type` | `string` | 文档类型<br>**可选值有**：<br>- `doc`: 旧版文档 - `docx`: 新版文档 - `sheet`: 电子表格 - `bitable`: 多维表格 - `slides`: 幻灯片 - `file`: 文件<br>**数据校验规则**：<br>- 长度范围：`1` ～ `50` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `file_token` | `string` | 文档token<br>**数据校验规则**：<br>- 长度范围：`22` ～ `27` 字符 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `from_user_id` | `user_id` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user id<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `to_user_id` | `user_id` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user id<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `notice_type` | `string` | 评论操作类型，枚举值：add_comment、add_reply<br>**可选值有**：<br>- `add_comment`: 添加评论 - `add_reply`: 添加回复<br>**数据校验规则**：<br>- 长度范围：`2` ～ `50` 字符 |
| &nbsp;&nbsp;└ `comment_id` | `string` | 评论ID<br>**数据校验规则**：<br>- 长度范围：`15` ～ `30` 字符 |
| &nbsp;&nbsp;└ `reply_id` | `string` | 回复ID<br>**数据校验规则**：<br>- 长度范围：`15` ～ `30` 字符 |
| &nbsp;&nbsp;└ `is_mentioned` | `boolean` | 接收者是否被mention |


### 事件体示例

```json
{
    "schema": "2.0",
    "header": {
        "event_id": "5e3702a84e847582be8db7fb73283c02",
        "event_type": "drive.notice.comment_add_v1",
        "create_time": "1608725989000",
        "token": "rvaYgkND1GOiu5MM0E1rncYC6PLtF7JV",
        "app_id": "cli_9f5343c580712544",
        "tenant_key": "2ca1d211f64f6438"
    },
    "event": {
        "notice_meta": {
            "file_type": "docx",
            "file_token": "TLLKdcpDro9ijQxA33ycNMabcef",
            "from_user_id": {
                "union_id": "on_8ed6aa67826108097d9ee143816345",
                "user_id": "e33ggbyz",
                "open_id": "ou_84aad35d084aa403a838cf73ee18467"
            },
            "to_user_id": {
                "union_id": "on_8ed6aa67826108097d9ee143816345",
                "user_id": "e33ggbyz",
                "open_id": "ou_84aad35d084aa403a838cf73ee18467"
            },
            "notice_type": "add_comment"
        },
        "comment_id": "7618859513273112345",
        "reply_id": "7618859513273112345",
        "is_mentioned": true
    }
}
```


### 事件订阅示例代码

事件订阅流程可参考：[事件订阅概述](https://open.larkoffice.com/document/ukTMukTMukTM/uUTNz4SN1MjL1UzM)，新手入门可参考：[教程](https://open.larkoffice.com/document/uAjLw4CM/uMzNwEjLzcDMx4yM3ATM/develop-an-echo-bot/introduction)


`订阅方式`


长连接方式（推荐）：无需发布到公网地址，在本地开发环境中即可接收事件回调，且无需处理加解密逻辑。
发送至开发者服务器：需要提供服务器公网地址。


```
package main

import (
	"context"
	"fmt"

	larkcore "github.com/larksuite/oapi-sdk-go/v3/core"
	larkevent "github.com/larksuite/oapi-sdk-go/v3/event"
	"github.com/larksuite/oapi-sdk-go/v3/event/dispatcher"
	"github.com/larksuite/oapi-sdk-go/v3/service/drive/v1"
	larkws "github.com/larksuite/oapi-sdk-go/v3/ws"
)

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/golang-sdk-guide/preparations
func main() {
	// 注册事件 Register event
	eventHandler := dispatcher.NewEventDispatcher("", "").
		OnP2NoticeCommentAddV1(func(ctx context.Context, event *larkdrive.P2NoticeCommentAddV1) error {
			fmt.Printf("[ OnP2NoticeCommentAddV1 access ], data: %s\n", larkcore.Prettify(event))
			return nil
		})

	// 构建 client Build client
	cli := larkws.NewClient("YOUR_APP_ID", "YOUR_APP_SECRET",
		larkws.WithEventHandler(eventHandler),
		larkws.WithLogLevel(larkcore.LogLevelDebug),
	)

	// 建立长连接 Establish persistent connection
	err := cli.Start(context.Background())

	if err != nil {
		panic(err)
	}
}
```


```
# SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/python--sdk/preparations-before-development
import lark_oapi as lark


def do_p2_drive_notice_comment_add_v1(data: lark.drive.v1.P2DriveNoticeCommentAddV1) -> None:
    print(f'[ do_p2_drive_notice_comment_add_v1 access ], data: {lark.JSON.marshal(data, indent=4)}')

# 注册事件 Register event
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_drive_notice_comment_add_v1(do_p2_drive_notice_comment_add_v1) \
    .build()


def main():
    # 构建 client Build client
    cli = lark.ws.Client("APP_ID", "APP_SECRET",
                        event_handler=event_handler, log_level=lark.LogLevel.DEBUG)
    # 建立长连接 Establish persistent connection
    cli.start()

if __name__ == "__main__":
    main()
```


```
package com.example.sample;

import com.lark.oapi.core.utils.Jsons;
import com.lark.oapi.service.drive.DriveService;
import com.lark.oapi.service.drive.v1.model.P2NoticeCommentAddV1;
import com.lark.oapi.event.EventDispatcher;
import com.lark.oapi.ws.Client;

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/java-sdk-guide/preparations
public class Sample {
    // 注册事件 Register event
    private static final EventDispatcher EVENT_HANDLER = EventDispatcher.newBuilder("", "")
            .onP2NoticeCommentAddV1(new DriveService.P2NoticeCommentAddV1Handler() {
                @Override
                public void handle(P2NoticeCommentAddV1 event) throws Exception {
                    System.out.printf("[ onP2NoticeCommentAddV1 access ], data: %s\n", Jsons.DEFAULT.toJson(event.getEvent()));
                }
            })
            .build();

    public static void main(String[] args) {
        // 构建 client Build client
        Client client = new Client.Builder("APP_ID", "APP_SECRET")
                .eventHandler(EVENT_HANDLER)
                .build();
        // 建立长连接 Establish persistent connection
        client.start();
    }
}
```


```
// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/nodejs-sdk/preparation-before-development
import * as Lark from '@larksuiteoapi/node-sdk';
const baseConfig = {
    appId: 'APP_ID',
    appSecret: 'APP_SECRET'
}
// 构建 client Build client
const wsClient = new Lark.WSClient(baseConfig);
// 建立长连接 Establish persistent connection
wsClient.start({
    // 注册事件 Register event
    eventDispatcher: new Lark.EventDispatcher({}).register({
        'drive.notice.comment_add_v1': async (data) => {
            console.log(data);
        }
    })
});
```


```
package main

import (
	"context"
	"fmt"
	"net/http"

	larkcore "github.com/larksuite/oapi-sdk-go/v3/core"
	"github.com/larksuite/oapi-sdk-go/v3/core/httpserverext"
	larkevent "github.com/larksuite/oapi-sdk-go/v3/event"
	"github.com/larksuite/oapi-sdk-go/v3/event/dispatcher"
	"github.com/larksuite/oapi-sdk-go/v3/service/drive/v1"
)

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/golang-sdk-guide/preparations
func main() {
	// 注册事件 Register event
	eventHandler := dispatcher.NewEventDispatcher("", "").
		OnP2NoticeCommentAddV1(func(ctx context.Context, event *larkdrive.P2NoticeCommentAddV1) error {
			fmt.Printf("[ OnP2NoticeCommentAddV1 access ], data: %s\n", larkcore.Prettify(event))
			return nil
		})

	// 创建路由处理器 Create route handler
	http.HandleFunc("/webhook/event", httpserverext.NewEventHandlerFunc(handler, larkevent.WithLogLevel(larkcore.LogLevelDebug)))

	err := http.ListenAndServe(":7777", nil)

	if err != nil {
		panic(err)
	}
}
```


```
# SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/python--sdk/preparations-before-development
from flask import Flask
from lark_oapi.adapter.flask import *
import lark_oapi as lark

app = Flask(__name__)


def do_p2_drive_notice_comment_add_v1(data: lark.drive.v1.P2DriveNoticeCommentAddV1) -> None:
    print(f'[ do_p2_drive_notice_comment_add_v1 access ], data: {lark.JSON.marshal(data, indent=4)}')

# 注册事件 Register event
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_drive_notice_comment_add_v1(do_p2_drive_notice_comment_add_v1) \
    .build()


# 创建路由处理器 Create route handler
@app.route("/webhook/event", methods=["POST"])
def event():
    resp = event_handler.do(parse_req())
    return parse_resp(resp)

if __name__ == "__main__":
    app.run(port=7777)
```


```
package com.lark.oapi.sample.event;

import com.lark.oapi.core.utils.Jsons;
import com.lark.oapi.service.drive.DriveService;
import com.lark.oapi.service.drive.v1.model.P2NoticeCommentAddV1;
import com.lark.oapi.sdk.servlet.ext.ServletAdapter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/java-sdk-guide/preparations
@RestController
public class EventController {

    // 注册事件 Register event
    private static final EventDispatcher EVENT_HANDLER = EventDispatcher.newBuilder("verificationToken", "encryptKey")
            .onP2NoticeCommentAddV1(new DriveService.P2NoticeCommentAddV1Handler() {
                @Override
                public void handle(P2NoticeCommentAddV1 event) throws Exception {
                    System.out.printf("[ onP2NoticeCommentAddV1 access ], data: %s\n", Jsons.DEFAULT.toJson(event.getEvent()));
                }
            })
            .build();

    // 注入 ServletAdapter 实例 Inject ServletAdapter instance
    @Autowired
    private ServletAdapter servletAdapter;

    // 创建路由处理器 Create route handler
    @RequestMapping("/webhook/event")
    public void event(HttpServletRequest request, HttpServletResponse response)
            throws Throwable {
        // 回调扩展包提供的事件回调处理器 Callback handler provided by the extension package
        servletAdapter.handleEvent(request, response, EVENT_DISPATCHER);
    }
}
```


```
// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/nodejs-sdk/preparation-before-development
import http from 'http';
import * as lark from '@larksuiteoapi/node-sdk';

// 注册事件 Register event
const eventDispatcher = new lark.EventDispatcher({
    encryptKey: '',
    verificationToken: '',
}).register({
    'drive.notice.comment_add_v1': async (data) => {
        console.log(data);
        return 'success';
    },
});

const server = http.createServer();
// 创建路由处理器 Create route handler
server.on('request', lark.adaptDefault('/webhook/event', eventDispatcher));
server.listen(3000);
```

