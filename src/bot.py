#Doc: https://github.com/nonebot/adapter-telegram/blob/beta/MANUAL.md
#Ref: https://github.com/nonebot/adapter-telegram/tree/beta/example
#Ref: https://github.com/ColdThunder11/nonebot-adapter-telegram

import nonebot
from nonebot.adapters.telegram.adapter import Adapter

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(Adapter)

nonebot.load_plugin("plugins.echo") # plugins/ 目录下的插件
#nonebot.load_from_toml("pyproject.toml")
#nonebot.load_builtin_plugins("echo")  # 内置插件

if __name__ == "__main__":
    nonebot.run()
