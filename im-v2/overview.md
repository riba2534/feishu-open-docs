---
title: "消息流概述"
fullPath: "/uAjLw4CM/ukTMukTMukTM/group/im-v2/overview"
updateTime: "1731048689000"
---

# 消息流概述
## 功能介绍

**「飞书消息流开放」**是指通过调用相关接口，在飞书消息列表中展示形式内容更加丰富的**消息流卡片**，通过自定义消息流卡片的标签、按钮、提示音、临时置顶状态等，让重要信息触达更轻松。

![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/ecb74df5e0624f1c8d4abaf28c5b904c_ixg5CE6DmL.png?height=678&lazyload=true&width=1280)

<br> 
**「飞书消息流开放」优势一览：**


| 接入前 | 接入后 |
| --- | --- |
| -   重要信息难触达，各类消息堆积，信息爆炸 - 新消息不断刷新消息列表，重要信息被淹没 - 信息处理路径长，处理过程操作繁琐，容易遗忘 - 通知提示音无区分，无法感知收到重要信息 ![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/58e64c4370e7d02b1a7a6c4760352f4d_EeVk5CenFE.png?height=1800&lazyload=true&width=4000) | -   消息流卡片醒目的**按钮**、**标签**，重要信息一眼看到 - 重要信息**可持续置顶**展示，防止遗漏 - 关键操作按钮外露，**一键处理**重要事项 - **自定义通知提示音**，第一时间了解重要信息     ![image.png](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/4e4b7421de441c3ea8b66d8c7b1b9021_SesG0VK4Qi.png?height=1800&lazyload=true&width=4000) |
 

<br> 

## 适用场景

**「飞书消息流开放」** 功能应用场景多样，下面列举几个典型的应用场景。


| 使用场景 | 场景描述 | 接入效果 |
| --- | --- | --- |
| **考勤打卡提醒** | 痛点：上下班时间事项繁多，容易忘记打卡，导致缺卡缺勤。          接入后：  - 上下班打卡前十分钟，打卡机器人在消息列表中置顶展示，形成强提醒，避免遗忘； - 配置快捷打卡按钮，可一键打卡，操作简单方便； - 打卡完成后取消置顶，不打扰日常工作。 |  |
 

<br>
## 名词介绍

**「飞书消息流开放」** 中包括如下几种名词介绍：

| 名词 | 标识 | 解释 | 示例图 |
| --- | --- | --- | --- |
| 消息流卡片 | ```app_feed_card``` | -   在消息列表中一种特殊的消息展示类型，使信息更加醒目，更快触达用户。 - 消息流卡片有以下 2 种类型：     - 应用消息流卡片：由应用创建的消息流卡片，可自定义消息流卡片的外观、点击后跳转的链接、消息流长按或右键操作。     - 群聊/机器人消息流卡片：将应用机器人会话、机器人所在群聊直接更新为消息流卡片，仅可自定义卡片按钮、即时提醒状态等。 | 应用消息流卡片           群聊消息流卡片 |
 

<br>
## 接入流程
### 应用消息流卡片：

| 步骤 | 介绍 |
| --- | --- |
| 1. 创建一个应用 | -   如需创建企业自建应用，可参考 [自建应用的开发流程](https://open.larkoffice.com/document/home/introduction-to-custom-app-development/self-built-application-development-process) - 如需创建应用商店应用，可参考 [开发和上架应用商店应用](https://open.larkoffice.com/document/uMzNwEjLzcDMx4yM3ATM/uYzNwEjL2cDMx4iN3ATM) |
 

### 群聊、机器人消息流卡片：

| 步骤 | 介绍 |
| --- | --- |
| 1. 创建一个应用 | -   如需创建企业自建应用，可参考 [自建应用的开发流程](https://open.larkoffice.com/document/home/introduction-to-custom-app-development/self-built-application-development-process) - 如需创建应用商店应用，可参考 [开发和上架应用商店应用](https://open.larkoffice.com/document/uMzNwEjLzcDMx4yM3ATM/uYzNwEjL2cDMx4iN3ATM) |
 


