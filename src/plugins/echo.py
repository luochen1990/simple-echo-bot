from nonebot.plugin import on_command, on_message
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

#Doc: https://nonebot.dev/docs/advanced/matcher
echo_cmd = on_command("echo",to_me())
echo_msg = on_message(to_me())

@echo_msg.handle()
async def echo_escape(bot: Bot, event: Event):
    await bot.send(event, event.get_message())

#await bot.send(event, "114514") #发送文字
#await bot.send(event, MessageSegment.photo(pic_url)) #发送图片 支持file:///，base64://，bytes，file_id，url(由Telegram服务器下载)
#
