---
title: "停止录制"
fullPath: "/uAjLw4CM/ukTMukTMukTM/reference/vc-v1/meeting/events/recording_ended"
updateTime: "1679916446000"
---

# 停止录制

发生在录制结束时【仅通过Open API预约的会议会产生此类事件】{使用示例}(url=/api/tools/api_explore/api_explore_config?project=vc&version=v1&resource=meeting&event=recording_ended)


## 事件

| 项目 | 值 |
| --- | --- |
| 事件类型 | vc.meeting.recording_ended_v1 |
| 支持的应用类型 | custom,isv |
| 权限要求             订阅该事件所需的权限，开启其中任意一项权限即可订阅 | `vc:meeting:readonly` 获取会议信息 |
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
| &nbsp;&nbsp;└ `meeting` | `meeting_event_meeting` | 会议数据 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `string` | 会议ID（视频会议的唯一标识，视频会议开始后才会产生） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `topic` | `string` | 会议主题 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `meeting_no` | `string` | 9位会议号（飞书用户可通过输入9位会议号快捷入会） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `start_time` | `string` | 会议结束时间（unix时间，单位：秒） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `end_time` | `string` | 会议结束时间（unix时间，单位：秒） |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `host_user` | `meeting_event_user` | 会议主持人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `user_id` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user id<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_role` | `int` | 用户会中角色<br>**可选值有**：<br>- `1`: 普通参会人 - `2`: 主持人 - `3`: 联席主持人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_type` | `int` | 用户类型<br>**可选值有**：<br>- `1`: 飞书用户 - `2`: rooms用户 - `3`: 文档用户 - `4`: neo单品用户 - `5`: neo单品游客用户 - `6`: pstn用户 - `7`: sip用户 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `owner` | `meeting_event_user` | 会议拥有者 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `user_id` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user id<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_role` | `int` | 用户会中角色<br>**可选值有**：<br>- `1`: 普通参会人 - `2`: 主持人 - `3`: 联席主持人 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_type` | `int` | 用户类型<br>**可选值有**：<br>- `1`: 飞书用户 - `2`: rooms用户 - `3`: 文档用户 - `4`: neo单品用户 - `5`: neo单品游客用户 - `6`: pstn用户 - `7`: sip用户 |
| &nbsp;&nbsp;└ `operator` | `meeting_event_user` | 事件操作人 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `id` | `user_id` | 用户 ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `union_id` | `string` | 用户的 union id |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `user_id` | `string` | 用户的 user id<br>**字段权限要求**： `contact:user.employee_id:readonly` 获取用户 user ID |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ `open_id` | `string` | 用户的 open id |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_role` | `int` | 用户会中角色<br>**可选值有**：<br>- `1`: 普通参会人 - `2`: 主持人 - `3`: 联席主持人 |
| &nbsp;&nbsp;&nbsp;&nbsp;└ `user_type` | `int` | 用户类型<br>**可选值有**：<br>- `1`: 飞书用户 - `2`: rooms用户 - `3`: 文档用户 - `4`: neo单品用户 - `5`: neo单品游客用户 - `6`: pstn用户 - `7`: sip用户 |


### 事件体示例

```json
{
    "schema": "2.0",
    "header": {
        "event_id": "5e3702a84e847582be8db7fb73283c02",
        "event_type": "vc.meeting.recording_ended_v1",
        "create_time": "1608725989000",
        "token": "rvaYgkND1GOiu5MM0E1rncYC6PLtF7JV",
        "app_id": "cli_9f5343c580712544",
        "tenant_key": "2ca1d211f64f6438"
    },
    "event": {
        "meeting": {
            "id": "6911188411934433028",
            "topic": "my meeting",
            "meeting_no": "235812466",
            "start_time": "1608883322",
            "end_time": "1608883899",
            "host_user": {
                "id": {
                    "union_id": "on_8ed6aa67826108097d9ee143816345",
                    "user_id": "e33ggbyz",
                    "open_id": "ou_84aad35d084aa403a838cf73ee18467"
                },
                "user_role": 1,
                "user_type": 1
            },
            "owner": {
                "id": {
                    "union_id": "on_8ed6aa67826108097d9ee143816345",
                    "user_id": "e33ggbyz",
                    "open_id": "ou_84aad35d084aa403a838cf73ee18467"
                },
                "user_role": 1,
                "user_type": 1
            }
        },
        "operator": {
            "id": {
                "union_id": "on_8ed6aa67826108097d9ee143816345",
                "user_id": "e33ggbyz",
                "open_id": "ou_84aad35d084aa403a838cf73ee18467"
            },
            "user_role": 1,
            "user_type": 1
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
	"github.com/larksuite/oapi-sdk-go/v3/service/vc/v1"
	larkws "github.com/larksuite/oapi-sdk-go/v3/ws"
)

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/golang-sdk-guide/preparations
func main() {
	// 注册事件 Register event
	eventHandler := dispatcher.NewEventDispatcher("", "").
		OnP2MeetingRecordingEndedV1(func(ctx context.Context, event *larkvc.P2MeetingRecordingEndedV1) error {
			fmt.Printf("[ OnP2MeetingRecordingEndedV1 access ], data: %s\n", larkcore.Prettify(event))
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


def do_p2_vc_meeting_recording_ended_v1(data: lark.vc.v1.P2VcMeetingRecordingEndedV1) -> None:
    print(f'[ do_p2_vc_meeting_recording_ended_v1 access ], data: {lark.JSON.marshal(data, indent=4)}')

# 注册事件 Register event
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_vc_meeting_recording_ended_v1(do_p2_vc_meeting_recording_ended_v1) \
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
import com.lark.oapi.service.vc.VcService;
import com.lark.oapi.service.vc.v1.model.P2MeetingRecordingEndedV1;
import com.lark.oapi.event.EventDispatcher;
import com.lark.oapi.ws.Client;

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/java-sdk-guide/preparations
public class Sample {
    // 注册事件 Register event
    private static final EventDispatcher EVENT_HANDLER = EventDispatcher.newBuilder("", "")
            .onP2MeetingRecordingEndedV1(new VcService.P2MeetingRecordingEndedV1Handler() {
                @Override
                public void handle(P2MeetingRecordingEndedV1 event) throws Exception {
                    System.out.printf("[ onP2MeetingRecordingEndedV1 access ], data: %s\n", Jsons.DEFAULT.toJson(event.getEvent()));
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
        'vc.meeting.recording_ended_v1': async (data) => {
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
	"github.com/larksuite/oapi-sdk-go/v3/service/vc/v1"
)

// SDK 使用说明 SDK user guide：https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/server-side-sdk/golang-sdk-guide/preparations
func main() {
	// 注册事件 Register event
	eventHandler := dispatcher.NewEventDispatcher("", "").
		OnP2MeetingRecordingEndedV1(func(ctx context.Context, event *larkvc.P2MeetingRecordingEndedV1) error {
			fmt.Printf("[ OnP2MeetingRecordingEndedV1 access ], data: %s\n", larkcore.Prettify(event))
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


def do_p2_vc_meeting_recording_ended_v1(data: lark.vc.v1.P2VcMeetingRecordingEndedV1) -> None:
    print(f'[ do_p2_vc_meeting_recording_ended_v1 access ], data: {lark.JSON.marshal(data, indent=4)}')

# 注册事件 Register event
event_handler = lark.EventDispatcherHandler.builder("", "") \
    .register_p2_vc_meeting_recording_ended_v1(do_p2_vc_meeting_recording_ended_v1) \
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
import com.lark.oapi.service.vc.VcService;
import com.lark.oapi.service.vc.v1.model.P2MeetingRecordingEndedV1;
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
            .onP2MeetingRecordingEndedV1(new VcService.P2MeetingRecordingEndedV1Handler() {
                @Override
                public void handle(P2MeetingRecordingEndedV1 event) throws Exception {
                    System.out.printf("[ onP2MeetingRecordingEndedV1 access ], data: %s\n", Jsons.DEFAULT.toJson(event.getEvent()));
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
    'vc.meeting.recording_ended_v1': async (data) => {
        console.log(data);
        return 'success';
    },
});

const server = http.createServer();
// 创建路由处理器 Create route handler
server.on('request', lark.adaptDefault('/webhook/event', eventDispatcher));
server.listen(3000);
```

