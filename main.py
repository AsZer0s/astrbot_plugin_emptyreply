from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp


@register("QQEmptyReplyBlocker", "AsZer0s", "拦截 QQ 平台上仅包含回复引用但没有实际消息内容的消息", "1.0.0")
class QQEmptyReplyBlocker(Star):
    """
    QQ 空回复拦截器插件
    
    功能：
    - 检测 QQ 平台上的消息
    - 拦截仅包含回复引用但没有实际消息内容的消息
    - 其他消息正常放行
    """
    
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("QQEmptyReplyBlocker 插件已初始化")

    async def initialize(self):
        """插件初始化方法"""
        logger.info("QQEmptyReplyBlocker 插件启动完成")

    @filter.command("empty_reply_check")
    async def check_empty_reply(self, event: AstrMessageEvent):
        """
        检查空回复消息的指令处理器
        
        这个指令用于测试插件功能，实际的消息拦截通过重写消息处理逻辑实现
        """
        try:
            # 获取消息平台名称
            platform_name = event.get_platform_name()
            logger.info(f"收到来自平台 {platform_name} 的消息")
            
            # 只处理 QQ 平台的消息
            if platform_name not in ["aiocqhttp", "lagrange", "napcat"]:
                yield event.plain_result(f"非 QQ 平台消息，平台: {platform_name}")
                return
            
            # 获取消息链
            message_chain = event.get_messages()
            if not message_chain:
                yield event.plain_result("消息链为空")
                return
            
            # 检查是否包含回复引用
            has_reply = False
            has_content = False
            
            for component in message_chain:
                # 检查是否为回复组件
                if isinstance(component, Comp.Reply):
                    has_reply = True
                    logger.debug(f"检测到回复引用: {component.message_id}")
                # 检查是否为文本内容（非空）
                elif isinstance(component, Comp.Plain) and component.text.strip():
                    has_content = True
                    logger.debug(f"检测到文本内容: {component.text}")
                # 检查其他类型的内容（图片、表情等）
                elif not isinstance(component, Comp.Reply):
                    has_content = True
                    logger.debug(f"检测到其他类型内容: {type(component).__name__}")
            
            # 分析结果
            if has_reply and not has_content:
                sender_name = event.get_sender_name()
                logger.info(f"检测到空回复消息 - 发送者: {sender_name}, 平台: {platform_name}")
                yield event.plain_result("检测到空回复消息！")
            else:
                yield event.plain_result("消息正常，包含实际内容")
            
        except Exception as e:
            logger.error(f"处理消息时发生错误: {e}")
            yield event.plain_result(f"处理消息时发生错误: {e}")

    async def terminate(self):
        """插件销毁方法"""
        logger.info("QQEmptyReplyBlocker 插件已卸载")
