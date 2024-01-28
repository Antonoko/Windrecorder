![Windrecorder](https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/product-header-cn.jpg)
<h1 align="center"> 🦝 Windrecorder | 捕风记录仪</h1>
<p align="center"> An Open Source <a href="https://www.rewind.ai/">Rewind</a>’s alternative tool on Windows to help you retrieve memory cues.</p>
<p align="center">一款运行在 Windows 平台上的 <a href="https://www.rewind.ai/">Rewind</a> 替代工具，帮助你找回记忆线索</p>

<p align="center"> <a href="https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/README-en.md">English</a>  | <a href="https://github.com/yuka-friends/Windrecorder/blob/main/README.md">简体中文</a> | <a href="https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/README-ja.md">日本語</a> </p>

---

这是一款可以持续记录屏幕画面、通过关键词搜索等方式随时回溯过去与记忆的工具。

**它的所有能力（录制、识别处理、存储回溯等）完全运行在本地，无需联网，不上传任何数据，只做应该做的事。**

![Windrecorder](https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/product-preview-cn.jpg)

**Windrecorder 目前可以做到：**
- 以较小的文件体积稳定持续地录制屏幕，只索引有变化的画面，将画面与 OCR 内容更新到数据库；在闲时自动维护、清理与压缩视频文件；
- 具有完善的 webui 界面，可以对画面回溯、OCR 文本查询；提供词云、时间轴、光箱、散点图的数据摘要；支持多语言；
- 正在施工特性：简化安装过程、多屏幕支持、画面语义搜索、数据库加密、词嵌入索引与 LLM 查询、更完善的查询体验界面……

---

> [!WARNING]
> 该项目仍在较早期开发阶段，体验与使用上可能会遇上些小问题。如果遇到，欢迎提出 issue 反馈、关注更新，也欢迎在 [Discussions 讨论区](https://github.com/yuka-friends/Windrecorder/discussions)发起讨论。
> 
>  🤯 **如果你擅长 Python / 客户端前端方向、且对项目感兴趣，欢迎通过提出 issue / PR / PR review 参与到构建中，在 [Dissuasions](https://github.com/yuka-friends/Windrecorder/discussions) 查看 Roadmap 与讨论！**

> [!IMPORTANT]  
> 由于代码编写小失误，`0.0.5` 以前版本可能无法正常检测更新、或通过 install_update.bat 进行升级。如是，请在 `Windrecorder` 根目录的路径框输入`cmd`打开命令行，输入`git pull`进行更新。🙇‍♀️
>
> 别担心！带上属于你的 `videos`、 `db`、 `config\config_user.json` 等目录与文件，随时可以迁移到最新的版本上。

## 🦝🎉 0.1.0 上新预告（即将发布）

![Windrecorder](https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/product-update-0.1.0.jpg)

- 现在，我们将工具集成到系统托盘中了，并将发布可直接运行的整合包，捕风记录仪将前所未有地更加直观易用。和繁杂的手动安装、`start_record.bat` & `start_webui.bat` 说拜拜！👋
- 添加了时间标记功能：当想为正在经历的重要会议、突发情况、某场直播、游戏与观影高光时刻……等添加标记、以方便未来回顾时，可以通过托盘标记当下，也可以在回顾时为重要事件添加记录；
- 为压缩视频添加了更多的格式与参数支持；
- 重构大量代码结构，修复部分 bug 与提升了性能。更多的升级与改动，敬请查阅[更新日志](https://github.com/yuka-friends/Windrecorder/blob/main/CHANGELOG.md)


如果你之前已经在使用捕风记录仪了，谢谢你！可以通过如下方法更新到最新版本：

- 方法 A：从 [Releases](https://github.com/yuka-friends/Windrecorder/releases) 下载整合包并解压，接着：
    - 在工具目录下新建 `userdata` 文件夹，将原先的 `videos`、`db`、`result_lightbox`、`result_timeline`、`result_wordcloud` 文件夹移动到 `userdata` 中；
    - 将原先的 `config\config_user.json` 文件移动到 `userdata` 文件夹中；
    - 打开 `windrecorder.exe` 即可使用 🎉
- 方法 B：在目录下执行 `git pull`，然后打开 `install_update.bat` 进行升级；


# 🦝 首次使用安装

## 自动安装（即将就绪）

从 [Releases](https://github.com/yuka-friends/Windrecorder/releases) 下载整合包，将其解压到希望存储数据的目录下，打开 `windrecorder.exe` 即可开始使用。


## 手动安装

- 下载 [ffmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip) ，将其中 bin 目录下的ffmpeg.exe、ffprobe.exe 解压至 `C:\Windows\System32` 下（或其他位于 PATH 的目录下）

- 安装 [Git](https://git-scm.com/downloads)、[Python](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe)（安装时勾选 Add python.exe to PATH）、[Pip](https://pip.pypa.io/en/stable/installation/)；
    - **注意！目前暂未支持 python 3.12**，推荐使用 python 3.11，即上面链接指向的版本

- 导航到想要安装此工具的目录下（推荐放在空间富足的分区中），通过终端命令 `git clone https://github.com/yuka-friends/Windrecorder` 下载该工具；

    - 可以打开想要安装的文件夹，在路径栏输入`cmd` 并回车，进入当前目录终端，将以上命令贴入、回车执行；

- 打开目录下的 `install_update.bat` 进行工具安装与配置，顺利的话就可以开始使用了！


# 🦝 如何使用

目前暂时需要通过打开目录下的批处理脚本来使用工具：

- 通过打开目录下的`start_app.bat`开始记录屏幕；

> 注意：目前需要一直将终端窗口最小化放在后台运行来记录。

> [!TIP]
> 最佳实践：在 webui 中设置开机自启动，即可无感记录下一切。
> 
> **当画面没有变化、或屏幕睡眠时将自动暂停记录。当电脑空闲无人使用时，工具会自动维护数据库、压缩、清理过期视频**
> 
> _Just set it and forget it！_


# 🦝 如何运作
![Windrecorder](https://github.com/yuka-friends/Windrecorder/blob/main/__assets__/how-it-work-sc.jpg)

当启动记录后，捕风记录仪将逐段录制 15 分钟的视频，在录制完毕后对视频片段进行 OCR 索引（因此，数据的查询可能会有 15 分钟的延迟时间）。当屏幕没有变化、或电脑进入锁屏时，将会自动暂停录制，并进行闲时维护，进行包括压缩与清理视频、进行图像嵌入识别等工作，直到用户回来继续操作电脑。

> 未来可能会改进录制方法，降低 ffmpeg 占用、让回溯不必等待。


# 🦝 Q&A | 常见问题

Q: 打开 webui 时没有近期一段时间的数据。

- A: 当工具正在索引数据时，webui 将不会创建最新的临时数据库文件。
解决方法：尝试稍等一段时间，等待工具索引完毕后，刷新 webui 界面，或删除 db 目录下后缀为 _TEMP_READ.db 的数据库文件后刷新即可（若出现数据库文件损坏提示，不必担心，可能是工具仍然在索引中，请尝试过段时间刷新/删除）。此项策略未来将会修复重构。 [#26](https://github.com/yuka-friends/Windrecorder/issues/26)

Q: 在打开webui时提示：`FileNotFoundError: [WinError 2] The system cannot find the file specified: './db\\user_2023-10_wind.db-journal'`

- A: 通常在初次访问 webui 时、工具仍正在索引数据时出现。
解决方法：在工具后台索引完毕后，删除 db 文件夹下对应后缀为 _TEMP_READ.db 的数据库文件后刷新即可。

Q: 录制过程中鼠标闪烁

- A：Windows历史遗留问题，可尝试[该帖](https://stackoverflow.com/questions/34023630/how-to-avoid-mouse-pointer-flicker-when-capture-a-window-by-ffmpeg)方法解决🤔。（其实习惯了不去在意也还好（逃

Q: Windows.Media.Ocr.Cli OCR 不可用/识别率过低

- A1: 检查系统中是否添加了目标语言的语言包/输入法：https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr

- A2: 早期版本的默认策略会将高度大于 1500 的屏幕分辨率视为「高 DPI /高分辨率屏幕」，其录制视频分辨率将缩小至原来的四分之一。比如在 3840x2160 的 4k 显示器上，录制视频的分辨率将为 1920x1080，而这可能导致 OCR 识别准确率的下降。如果你在高分辨率屏幕上使用较小的字体或缩放，可以前往`录制与视频存储`中关闭此选项，且可以将`原视频保留几天后进行压缩`的天数设定为较小的值，从而在视频 OCR 索引后一段时间压缩视频体积。

- A3: Windows.Media.Ocr.Cli 对较小的文本识别率可能不良，通过在设置中打开「相近字形搜索」选项可以提高搜索时的召回命中率。

# 🧡
引入了这些项目的帮助：

- https://github.com/DayBreak-u/chineseocr_lite

- https://github.com/zh-h/Windows.Media.Ocr.Cli


---

🧡 喜欢这个工具？欢迎到 Youtube 与流媒体音乐平台上听听 [長瀬有花 / YUKA NAGASE](https://www.youtube.com/channel/UCf-PcSHzYAtfcoiBr5C9DZA) 温柔的音乐，谢谢！

> "Your tools suck, check out my girl Yuka Nagase, she's amazing, I code 10 times faster when listening to her." -- @jpswing
