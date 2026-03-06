---
title: "工单消息事件"
fullPath: "/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket_message/events/created"
updateTime: "1673240284000"
---

# 工单消息事件

该消息事件属于工单消息事件。需使用订阅接口订阅：[事件订阅](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/event/subscribe)。{使用示例}(url=/api/tools/api_explore/api_explore_config?project=helpdesk&version=v1&resource=ticket_message&event=created)


## 事件

| 项目 | 值 |
| --- | --- |
| 事件类型 | helpdesk.ticket_message.created_v1 |
| 支持的应用类型 | custom |
| 权限要求             订阅该事件所需的权限，开启其中任意一项权限即可订阅 | `helpdesk:all:readonly` 获取服务台资源详情 |
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
| `event` | `ticket_message_event` | \- |
| &nbsp;&nbsp;└ `ticket_message_id` | `string` | ticket message id |
| &nbsp;&nbsp;└ `message_id` | `string` | open message id |
| &nbsp;&nbsp;└ `msg_type` | `string` | message type, text is the only supported type |
| &nbsp;&nbsp;└ `position` | `string` | position of the message |
| &nbsp;&nbsp;└ `sender_id` | `user_id` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user id<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open id |
| &nbsp;&nbsp;└ `sender_type` | `int` | sender type, 1 for bot, 2 for guest, 3 for agent |
| &nbsp;&nbsp;└ `text` | `string` | message content |
| &nbsp;&nbsp;└ `ticket` | `ticket` | ticket related information |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ticket_id` | `string` | 工单ID<br>[可以从工单列表里面取](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket/list)<br>[也可以订阅工单创建事件获取](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket/events/created) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `comments` | `comments` | 备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 备注 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `created_at` | `int` | 备注时间，单位毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `int` | 备注ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_avatar_url` | `string` | 备注人头像 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_name` | `string` | 备注人姓名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `int` | 备注人ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `ticket_type` | `int` | 工单阶段：1. 机器人 2. 人工 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `status` | `int` | 工单状态，1：已创建 2: 处理中 3: 排队中 4：待定 5：待用户响应 50: 被机器人关闭 51: 被客服关闭 52: 用户自己关闭 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `dissatisfaction_reason` | `i18n` | 不满意原因 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `zh_cn` | `string` | 中文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `en_us` | `string` | 英文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `ja_jp` | `string` | 日文描述 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `customized_fields` | `customized_field_display_item\[\]` | 自定义字段列表，没有值时不设置   下拉菜单的value对应工单字段里面的children.display_name [获取全部工单自定义字段](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/helpdesk-v1/ticket_customized_field/list-ticket-customized-fields) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 自定义字段ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `value` | `string` | 自定义字段值 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `key_name` | `string` | 键名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `display_name` | `string` | 展示名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `position` | `int` | 展示位置 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `required` | `boolean` | 是否必填 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `editable` | `boolean` | 是否可修改 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_service_duration` | `float` | 客服服务时长，客服最后一次回复时间距离客服进入时间间隔，单位分钟 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_first_response_duration` | `int` | 客服首次回复时间距离客服进入时间的间隔(秒) |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `bot_service_duration` | `int` | 机器人服务时间：客服进入时间距离工单创建时间的间隔，单位秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_resolution_time` | `int` | 客服解决时长，关单时间距离客服进入时间的间隔，单位秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `actual_processing_time` | `int` | 工单实际处理时间：从客服进入到关单，单位秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_entry_time` | `int` | 客服进入时间，单位毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_first_response_time` | `int` | 客服首次回复时间，单位毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_last_response_time` | `int` | 客服最后回复时间，单位毫秒 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `agent_owner` | `ticket_user` | 主责客服 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 用户ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `avatar_url` | `string` | 用户头像url |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `name` | `string` | 用户名 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `email` | `string` | 用户邮箱 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `department` | `string` | 所在部门名称 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `city` | `string` | 城市 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `country` | `string` | 国家代号(CountryCode)，参考：http://www.mamicode.com/info-detail-2186501.html |
| &nbsp;&nbsp;└ `event_id` | `string` | event id |
| &nbsp;&nbsp;└ `chat_id` | `string` | chat id |
| &nbsp;&nbsp;└ `content` | `ticket_message_content` | message content |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `content` | `string` | 内容 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `msg_type` | `string` | 消息类型；text：纯文本；post：富文本；image：图片 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `image_keys` | `string\[\]` | 图片ID |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `image_key` | `string` | 图片ID |


### 事件体示例

```json
{
    "schema": "2.0",
    "header": {
        "event_id": "5e3702a84e847582be8db7fb73283c02",
        "event_type": "helpdesk.ticket_message.created_v1",
        "create_time": "1608725989000",
        "token": "rvaYgkND1GOiu5MM0E1rncYC6PLtF7JV",
        "app_id": "cli_9f5343c580712544",
        "tenant_key": "2ca1d211f64f6438"
    },
    "event": {
        "ticket_message_id": "6949088240624222236",
        "message_id": "om_8baa3656c7b41900d29bf9104bf5310b",
        "msg_type": "text",
        "position": "10",
        "sender_id": {
            "union_id": "on_8ed6aa67826108097d9ee143816345",
            "user_id": "e33ggbyz",
            "open_id": "ou_84aad35d084aa403a838cf73ee18467"
        },
        "sender_type": 1,
        "text": "请问vpn怎么下载",
        "ticket": {
            "ticket_id": "6626871355780366331",
            "comments": {
                "content": "备注内容",
                "created_at": 备注时间,
                "id": 备注id,
                "user_avatar_url": "备注人头像",
                "user_name": "备注人姓名",
                "user_id": 备注人id
            },
            "ticket_type": 1,
            "status": 50,
            "dissatisfaction_reason": {
                "zh_cn": "答案看不懂",
                "en_us": "I don't understand",
                "ja_jp": "回答が複雑すぎる"
            },
            "customized_fields": [
                {
                    "id": "123",
                    "value": "value",
                    "key_name": "key",
                    "display_name": "display name",
                    "position": 1,
                    "required": true,
                    "editable": true
                }
            ],
            "agent_service_duration": 42624.95,
            "agent_first_response_duration": 123869,
            "bot_service_duration": 1,
            "agent_resolution_time": 66,
            "actual_processing_time": 68,
            "agent_entry_time": 1636444596000,
            "agent_first_response_time": 1636444696000,
            "agent_last_response_time": 1636444796000,
            "agent_owner": {
                "id": "ou_37019b7c830210acd88fdce886e25c71",
                "avatar_url": "https://xxxx",
                "name": "abc",
                "email": "xxxx@abc.com",
                "department": "用户部门名称(有权限才展示)",
                "city": "城市",
                "country": "国家"
            }
        },
        "event_id": "118a6492-122d-04ad-4370-010a3bb384d3",
        "chat_id": "6949088236610273307",
        "content": {
            "content": "请问vpn怎么下载",
            "msg_type": "text",
            "image_keys": [
                "xxx","yyy"
            ],
            "image_key": "xxx"
        }
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
	"github.com/larksuite/oapi-sdk-go/v3/service/helpdesk/v1"
	larkws "github.com/larksuite/oapi-sdk-go/v3/ws"
)

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/golang-sdk-guide/preparations
func main() {
	// 注册事件 Register event
	eventHandler := dispatcher.NewEventDispatcher("", "").
		OnP2TicketMessageCreatedV1(func(ctx context.Context, event *larkhelpdesk.P2TicketMessageCreatedV1) error {
			fmt.Printf("[ OnP2TicketMessageCreatedV1 access ], data: %s\n", larkcore.Prettify(event))
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


def do_p2_helpdesk_ticket_message_created_v1(data: lark.helpdesk.v1.P2HelpdeskTicketMessageCreatedV1) -> None:
    print(f'[ do_p2_helpdesk_ticket_message_created_v1 access ], data: {lark.JSON.marshal(data, indent=4)}')

# 注册事件 Register event
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_helpdesk_ticket_message_created_v1(do_p2_helpdesk_ticket_message_created_v1) \
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
import com.lark.oapi.service.helpdesk.HelpdeskService;
import com.lark.oapi.service.helpdesk.v1.model.P2TicketMessageCreatedV1;
import com.lark.oapi.event.EventDispatcher;
import com.lark.oapi.ws.Client;

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/java-sdk-guide/preparations
public class Sample {
    // 注册事件 Register event
    private static final EventDispatcher EVENT_HANDLER = EventDispatcher.newBuilder("", "")
            .onP2TicketMessageCreatedV1(new HelpdeskService.P2TicketMessageCreatedV1Handler() {
                @Override
                public void handle(P2TicketMessageCreatedV1 event) throws Exception {
                    System.out.printf("[ onP2TicketMessageCreatedV1 access ], data: %s\n", Jsons.DEFAULT.toJson(event.getEvent()));
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
        'helpdesk.ticket_message.created_v1': async (data) => {
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
	"github.com/larksuite/oapi-sdk-go/v3/service/helpdesk/v1"
)

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/golang-sdk-guide/preparations
func main() {
	// 注册事件 Register event
	eventHandler := dispatcher.NewEventDispatcher("", "").
		OnP2TicketMessageCreatedV1(func(ctx context.Context, event *larkhelpdesk.P2TicketMessageCreatedV1) error {
			fmt.Printf("[ OnP2TicketMessageCreatedV1 access ], data: %s\n", larkcore.Prettify(event))
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


def do_p2_helpdesk_ticket_message_created_v1(data: lark.helpdesk.v1.P2HelpdeskTicketMessageCreatedV1) -> None:
    print(f'[ do_p2_helpdesk_ticket_message_created_v1 access ], data: {lark.JSON.marshal(data, indent=4)}')

# 注册事件 Register event
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_helpdesk_ticket_message_created_v1(do_p2_helpdesk_ticket_message_created_v1) \
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
import com.lark.oapi.service.helpdesk.HelpdeskService;
import com.lark.oapi.service.helpdesk.v1.model.P2TicketMessageCreatedV1;
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
            .onP2TicketMessageCreatedV1(new HelpdeskService.P2TicketMessageCreatedV1Handler() {
                @Override
                public void handle(P2TicketMessageCreatedV1 event) throws Exception {
                    System.out.printf("[ onP2TicketMessageCreatedV1 access ], data: %s\n", Jsons.DEFAULT.toJson(event.getEvent()));
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
    'helpdesk.ticket_message.created_v1': async (data) => {
        console.log(data);
        return 'success';
    },
});

const server = http.createServer();
// 创建路由处理器 Create route handler
server.on('request', lark.adaptDefault('/webhook/event', eventDispatcher));
server.listen(3000);
```

