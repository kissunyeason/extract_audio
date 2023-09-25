音频提取工具
这个项目是一个简单的音频提取工具，它可以从视频文件中提取音频，并将其保存为独立的音频文件。无论您是想提取电影中的配乐，还是从录制的视频中获取音频片段，这个工具都能够满足您的需求。

主要特点
简单易用：提供了一个直观的用户界面，只需提供视频文件路径和输出音频文件路径，即可快速提取音频。
多种格式支持：支持保存音频为常见的格式，如MP3、WAV、OGG等。
自定义编解码器：支持自定义编解码器参数，以便根据需要选择合适的音频编码格式。
基于pydub库：使用了功能强大且易于使用的pydub库来处理音频，确保提取过程高效且稳定。
安装和使用
安装依赖：确保您的环境中已经安装了pydub库和FFmpeg工具。
克隆项目：使用以下命令克隆项目到本地：
git clone https://github.com/your-username/audio-extraction-tool.git
运行工具：在命令行中进入项目目录，并运行提取音频的脚本。按照提示输入视频文件路径和输出音频文件路径。
示例代码：

from pydub import AudioSegment

def extract_audio():
    input_path = input("请输入视频文件路径：")
    output_path = input("请输入输出音频文件路径：")

    video = AudioSegment.from_file(input_path)
    audio = video.export(output_path, format='mp3')

    print("音频提取完成！")

extract_audio()
贡献
如果您对这个项目感兴趣并希望做出贡献，欢迎提交问题和拉取请求。在提交拉取请求之前，请确保您的代码经过了适当的测试，并遵循项目的代码风格和指南。

许可证
这个项目采用了 MIT许可证，请查阅许可证文件了解更多详情。