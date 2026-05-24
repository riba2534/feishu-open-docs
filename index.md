---
layout: home

hero:
  name: 飞书开放平台
  text: Server API 中文文档镜像
  tagline: 2,173 篇文档 · 48 个分类 · 自动同步官方
  actions:
    - theme: brand
      text: API 列表
      link: /api-call-guide/server-api-list
    - theme: alt
      text: GitHub 源码
      link: https://github.com/riba2534/feishu-open-docs

features:
  - title: 通讯录
    details: 用户、部门、用户组、自定义字段、工作城市
    link: /contact-v3/custom_attr/events/updated
  - title: 即时消息 v1
    details: 消息发送、消息卡片、表情回复、Pin、群聊
    link: /im-v1/batch_message/delete
  - title: 即时消息 v2
    details: 消息能力增强版，话题、Feed 流
    link: /im-v2/app_feed_card/create
  - title: 群组
    details: 群信息、成员、群公告（块结构）
    link: /group/chat-announcement/get
  - title: 卡片组件
    details: Interactive 卡片（v2.0）的服务端 API
    link: /cardkit-v1/card-callback-communication
  - title: 机器人
    details: 自定义机器人信息查询与配置
    link: /bot-v3/events/menu
  - title: 应用信息
    details: 应用版本、能力、可见性、使用反馈
    link: /application-v6/app_badge/set
  - title: 身份验证管理
    details: tenant_access_token / app_access_token / user_access_token
    link: /authentication-management/access-token/app_access_token_internal
  - title: 实名认证
    details: 人脸识别、身份证认证
    link: /human_authentication-v1/create
  - title: 认证服务
    details: 登录态校验
    link: /verification-v1/get

  - title: 日历
    details: 日历、日程、Exchange 绑定、会议室
    link: /calendar-v4/calendar-acl/create
  - title: 视频会议
    details: 会议、预约、参会人员、录制、纪要
    link: /vc-v1/alert/list
  - title: 妙记
    details: 录音/视频转写产物
    link: /minutes-v1/minute-media/get
  - title: 邮箱
    details: 邮箱、邮件草稿、文件夹、规则、用户邮箱
    link: /mail-v1/mail-group/mailgroup-alias/create
  - title: 公司圈
    details: 帖子、评论、表情互动
    link: /moments-v1/comment/events/created

  - title: 飞书人事
    details: 员工、组织架构、合同、签证、薪酬、审批
    link: /corehr-v1/about-timeline-version
  - title: 智能 HR
    details: 人员档案、附件
    link: /ehr-v1/get
  - title: 招聘
    details: 候选人、职位、面试、Offer、内推
    link: /hire-v1/attachment/create_attachment
  - title: 考勤打卡
    details: 打卡记录、班次、考勤组、假勤
    link: /attendance-v1/archive_rule/del_report
  - title: 飞书薪酬
    details: 算薪明细、人员
    link: /payroll-v1/acct_item/list
  - title: 飞书绩效
    details: 周期、人员、评估、校准
    link: /performance-v1/metric_detail/import
  - title: OKR
    details: 周期、O / KR、进展
    link: /okr-v1/okr-guide
  - title: 汇报
    details: 规则、任务
    link: /report-v1/rule-view/remove
  - title: 在线学习
    details: 课程、报名、学习记录
    link: /elearning-v2/course_registration/events/created
  - title: 智能门禁
    details: 门禁权限、打卡记录
    link: /acs-v1/access_record/events/created

  - title: 审批
    details: 实例、任务、抄送、外部、自定义事件
    link: /approval-v4/approval-overview
  - title: 任务
    details: 任务、清单、子任务、提醒
    link: /task-v2/attachment/attachment-feature-overview
  - title: 服务台
    details: 工单、客服、知识库
    link: /helpdesk-v1/agent-function/agent_skill_rule/list
  - title: 词典
    details: 词条、分类、草稿
    link: /lingo-v1/classification/list
  - title: 搜索
    details: 应用搜索、消息搜索、自定义数据源
    link: /search-v2/doc_wiki/search

  - title: 云文档
    details: 文档（docx / docs）、表格 sheets、知识库 wiki、评论
    link: /uUDN04SN0QjL1QDN/bitable-v1/advanced-permission/advanced-permission-guide
  - title: 多维表格
    details: Base / 多维表格的应用、表、视图、记录
    link: /spark-v1/app-enum/get_enum_detail
  - title: AI 能力
    details: OCR、文本识别等 AI 接口
    link: /ai/document_ai-v1/bank_card/recognize
  - title: 智能伙伴 Aily
    details: AI 助手会话、消息
    link: /aily-v1/aily_session-aily_message/create
  - title: 主数据
    details: 国家/地区、用户数据维度
    link: /mdm-v1/mdm-v3/country_region/get

  - title: 工作台
    details: 工作台首页、自定义工作台
    link: /workplace-v1/app_recommend_rule/favourite
  - title: 个人设置
    details: 用户的个人偏好
    link: /personal_settings-v1/system_status/batch_close
  - title: 管理后台
    details: 部门数据维度、用户徽章、系统徽章
    link: /admin-v1/badge/badge-grant/create
  - title: 企业信息
    details: 租户信息、产品分配
    link: /tenant-v2/query
  - title: 租户标签
    details: 标签、标签值
    link: /tenant-tag/create-biz_entity_tag_relation
  - title: 组织架构
    details: 部门、员工的最新接口
    link: /directory-v1/department/create
  - title: 互通群
    details: 关联租户的可见用户/部门
    link: /trust_party-v1/-collaboraiton-organization/get-collaboration_tenant-collaboration_department
  - title: 安全合规
    details: 行为审计、客户端安全、用户迁移
    link: /security_and_compliance-v1/audit_log/appendix
  - title: 低代码 aPaaS
    details: aPaaS 应用、对象、流程
    link: /apaas-v1/app/list

  - title: API 调用指南
    details: 鉴权、流控、API 列表、权限列表
    link: /api-call-guide/scope-list
  - title: 事件订阅指南
    details: 事件列表、订阅方式、回调验签
    link: /event-subscription-guide/callback-subscription/add-callback
  - title: 服务端 SDK
    details: Java / Python / Go / Node.js / PHP / .NET
    link: /server-side-sdk/faq
  - title: 历史版本
    details: 旧版本接口（已废弃，仅供查阅）
    link: /historic-version/apaas-v3/workspace/events/record_change
---
