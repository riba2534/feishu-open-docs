---
title: "常见问题"
fullPath: "/uAjLw4CM/ukTMukTMukTM/event-subscription-guide/event-card-faq"
updateTime: "1776345901000"
---

# 常见问题
本文档汇集使用**事件与回调**可能出现的常见问题与解决方案

### 如何配置机器人能够接收消息和发送消息

开启机器人对话，需要进行事件配置，同时，需要添加机器人接收消息的事件和配置相应权限，机器人才能接收消息，如果需要机器人拥有发送消息的能力，还需要配置机器人发送消息的 API 能力。以上配置保存并发版后才能开启机器人对话的能力。
1. 进行事件配置：订阅方式，可以选择“使用长连接接收事件”或“将事件发送至开发者服务器”，配置完成后，约1分钟，点击机器人对话页面，可给机器人发送消息
   ![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/af78c2c5fd28baf03728d60e1452b44f_7WdsXuiqwR.png?height=621&lazyload=true&width=1280)
   注：若需要机器人能够接收到消息并处理，还需要添加「接收消息」的事件和配置相关权限

2.  添加「接收消息」的事件
    1. 点击添加事件，添加应用身份订阅下的「接收消息」权限
    
       ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/e5e028570d46dabc81c432dae009661a_oTAxSCOata.png?height=1408&lazyload=true&width=2914)
       ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/aefdcf0d916021b64459e1cc069c8d59_AZakZ6LK4Y.png?height=1414&lazyload=true&width=2910)
    2. 点击权限名称后出现弹窗，在弹窗中可点击开通权限，当列表显示「已开通」，则机器人开通了对应权限
    
        ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/bfda5db437f4520e4a2954c261620bb8_fiGCrUCR3Z.png?height=1398&lazyload=true&width=2904)
        ![](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/864544709141e174486722babd688f3f_dTHXNUTmUU.png?height=1402&lazyload=true&width=2912)
3. 配置机器人发送消息的权限：配置机器人发送消息的 API 权限，机器人才能拥有发送消息的能力，发送消息的API为[发送消息](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create)

### 在使用长连接时，如果部署了多个实例，会如何选择实例呢？

**回答**：

实例采用随机选择策略，长连接无环境、机房归属区分，所有 client 权重相同；例如 A 环境机器人发送的消息，回调节点也可能分配至 B 环境。


### 飞书长连接会出现长时间收不到 pong 回复？cmd 窗口敲回车后才接收到，同时还有报 ERROR。

**回答：**
1. 网络差，检查一下是否有网络出流量限制。
2. 将CMD属性中的“快速编辑模式”关闭。

![jimeng-2026-02-12-9462-去除图片右下角的文字水印，保持其他所有内容不变.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/e8d60a50725bc8b2936b64c4800ef317_a9N4F6hWEI.png?height=2048&lazyload=true&width=2048)

### 使用长连接时，出现 not found handler 错误

**回答：**
1. 检查本地是否实现了对应的Handler
1. 如果有多个Client，检查每个Client是否实现了全部的Handler

  
### 配置了长连接并且开通了对应的事件，但是在后台日志中没有对应的事件。

**回答：**

**按照如下步骤检查**：
1. 切换至长连接模式后，应用是否完成发版；
2. 若涉及回调，检查搭建工具中配置的回调类型是否为对象。
3. 事件开通后需完成应用发版，请先核查应用是否已发版；若已订阅事件但事件日志无任何记录，说明订阅未成功，需联系技术支持排查。
  
### 长连接回调失败，报错“app not online”

**回答：**

若出现短时网络中断，SDK 会自动触发重连，网络恢复后即可正常使用；

  
### 配置了事件订阅，并且应用已经发版，但是在事件触发之后报 500 错误，原因是什么？

**回答**：

该问题通常因**应用存在多个在线长连接实例**所致：其中部分实例未实现对应监听事件的处理器（handler），进而触发 500 错误。

  
### 是否有方式能够查到应用建立了多少个长连接？

**回答：**

当前不支持查看应用已建立多少个长连接
  
### 使用事件订阅长连接方式，点击保存按钮的时候 提示：应用未建立长连接

**回答：**

订阅长连接前，需先确保已通过 SDK 在服务端 / 本地完成长连接的建立。
  
### 监听了指定的事件，但是会出现丢失事件的情况

**回答：**

该问题多因应用部署多个长连接实例，且部分实例未实现对应事件的 handler 所致。
  
### 长连接是否支持配置代理？

**回答：**

不支持。
  
### 卡片回调是否支持设置 LogID？

**回答：**

不支持
  
### 在使用长连接时，出现重复消费

**回答：**

**消息重复消费通常由以下两种原因导致：**

1. 业务 handler 处理逻辑异常并返回错误，触发消息重推机制；
2. 业务 handler 处理耗时超过 3s（事件要求 3s 内完成处理），触发消息重推，可通过异步启线程的方式解决。
  
### 卡片回调经常出现 200671 报错

**回答：** 
该错误属于业务错误，找技术支持排查，不属于 SDK 的问题。

**可能的原因**：
1. 开放平台 SDK 仅支持对象类型的卡片回传参数，不兼容字符串类型，该问题系用户在卡片模板中参数配置类型错误导致。
2. 用户编写的服务端逻辑有问题
  