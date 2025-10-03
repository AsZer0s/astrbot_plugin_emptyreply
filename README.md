# QQEmptyReplyBlocker

一个用于 AstrBot 的 QQ 空回复拦截插件

## 功能描述

本插件专门用于拦截 QQ 平台上仅包含回复引用但没有实际消息内容的消息。当用户发送只包含回复引用而没有任何文字、图片或其他内容的消息时，插件会自动拦截这些消息，防止机器人进行无意义的回复。

## 主要特性

- 🎯 **精准拦截**: 只拦截 QQ 平台上的空回复消息
- 🔍 **智能识别**: 准确识别包含回复引用但无实际内容的消息
- 🛡️ **安全可靠**: 包含完整的错误处理机制，不影响机器人正常功能
- 📝 **详细日志**: 提供详细的调试和运行日志
- ⚡ **高性能**: 轻量级设计，对机器人性能影响极小

## 支持的 QQ 协议端

- aiocqhttp
- lagrange  
- napcat
- 其他兼容 OneBot 协议的 QQ 客户端

## 拦截条件

插件会在以下**所有条件**同时满足时拦截消息：

1. ✅ 消息来源是 QQ 平台
2. ✅ 消息包含回复引用（Reply 组件）
3. ✅ 消息除了回复引用外没有其他内容（无文本、图片、表情等）

## 安装方法

### 方法一：通过 AstrBot 插件市场安装

1. 在 AstrBot WebUI 中进入插件管理页面
2. 搜索 "QQEmptyReplyBlocker" 或 "空回复拦截"
3. 点击安装并启用插件

### 方法二：手动安装

1. 将插件文件下载到 AstrBot 的 `data/plugins/` 目录下
2. 确保目录结构如下：
   ```
   data/plugins/astrbot_plugin_emptyreply/
   ├── main.py
   ├── metadata.yaml
   └── README.md
   ```
3. 在 AstrBot WebUI 中刷新插件列表并启用插件

## 使用方法

插件安装并启用后会自动开始工作，无需额外配置。

### 工作流程

1. 插件监听所有进入 AstrBot 的消息
2. 识别消息来源平台
3. 分析消息内容结构
4. 对符合条件的空回复消息进行拦截
5. 记录拦截日志

### 日志示例

```
[INFO] QQEmptyReplyBlocker 插件已初始化
[INFO] QQEmptyReplyBlocker 插件启动完成
[DEBUG] 收到来自平台 aiocqhttp 的消息
[DEBUG] 检测到回复引用: 1234567890
[INFO] 拦截空回复消息 - 发送者: 用户A, 平台: aiocqhttp
```

## 配置说明

当前版本无需额外配置，插件开箱即用。

## 开发信息

- **插件名称**: QQEmptyReplyBlocker
- **版本**: v1.0.0
- **作者**: AsZer0s
- **许可证**: 请查看 LICENSE 文件

## 技术实现

### 核心组件

- **消息过滤器**: 使用 `@filter.message()` 装饰器监听所有消息
- **平台检测**: 通过 `event.get_platform_name()` 识别消息来源
- **内容分析**: 遍历消息链组件，识别回复引用和实际内容
- **拦截机制**: 返回 `None` 来阻止消息的后续处理

### 消息组件识别

```python
# 回复引用组件
isinstance(component, Comp.Reply)

# 文本内容组件
isinstance(component, Comp.Plain) and component.text.strip()

# 其他内容组件（图片、表情等）
not isinstance(component, Comp.Reply)
```

## 常见问题

### Q: 插件会影响其他平台的消息吗？
A: 不会。插件只处理 QQ 平台的消息，其他平台的消息会正常放行。

### Q: 如何确认插件正在工作？
A: 查看 AstrBot 的日志文件，插件会记录详细的运行信息。

### Q: 可以自定义拦截条件吗？
A: 当前版本不支持自定义配置，但代码结构清晰，可以轻松修改拦截逻辑。

### Q: 插件会影响机器人的性能吗？
A: 不会。插件采用轻量级设计，对性能影响极小。

## 更新日志

### v1.0.0 (2024-01-XX)
- 🎉 首次发布
- ✨ 实现基本的空回复拦截功能
- 📝 添加详细的日志记录
- 🛡️ 完善错误处理机制

## 支持与反馈

如果您在使用过程中遇到问题或有改进建议，请通过以下方式联系：

- **GitHub Issues**: [提交问题](https://github.com/AsZer0s/astrbot_plugin_emptyreply/issues)
- **AstrBot 社区**: [加入讨论](https://astrbot.app)

## 相关链接

- [AstrBot 官方文档](https://docs.astrbot.app)
- [AstrBot 插件开发指南](https://docs.astrbot.app/dev/star/plugin.html)
- [AstrBot 社区](https://astrbot.app)

---

**注意**: 本插件基于 AstrBot 官方 API 开发，请确保您的 AstrBot 版本支持相关功能。
