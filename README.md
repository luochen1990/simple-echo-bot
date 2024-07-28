Simple Echo Bot
===============

这是一个简单的聊天机器人, 它只干一件事: 把用户对它说的话重复一遍。

你很可能会问, 为什么要搞这么个 bot, 它有什么用?

那实际上, 在代码的世界里, 任何什么都不干的东西都很无用, 但却很有意义. 就像 Unit Type 之于 type system, free monad 之于 monad, etc.

用人话说, 这个机器人的目的就只是作为演示学习, 你可以 fork 它然后开发你自己的机器人并实现更复杂的功能。

技术栈
-----

- 聊天机器人框架: nonebot2
- 编程语言: python3.10+
- 包管理: poetry
- 可重现打包发布: nix flake

用法
----

方式1, 不想 git clone 代码, 也不想准备专门的 python 环境, 可以直接以 nix flake 运行 (已经安装 nix 的情况下可用)

```bash
nix run github:luochen1990/simple-echo-bot
```

方式2, 不想装 nix, 但有现成的满足条件的 python 环境, 可以 git clone 后在项目目录下运行

```bash
poetry shell
python src/bot.py
```

当然，直接跑一下你会发现它不会工作，毕竟你没有配置任何 bot 所以它当然不会工作，配置的方式也有两种

配置方式1, 环境变量 (你如果用 direnv 的话可以把它放到 .envrc 文件里)

```
export TELEGRAM_BOTS='[{"token": "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHI"}]'
```

配置方式2, 修改 .env.prod 文件 (当然这个方式就只有在你 git clone 代码之后才能用了)

注意以上是以 telegram 为例子, 如果是其他 IM, 则需要去 [nonebot的适配器商店](https://nonebot.dev/store/adapters) 里找到对应的适配器, 用 `poetry add` 安装, 并从它的 github README 文档里查看如何配置
