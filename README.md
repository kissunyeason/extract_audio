```
# 音频提取工具

这个项目是一个简单的音频提取工具，它可以从视频文件中提取音频，并将其保存为独立的音频文件。无论您是想提取电影中的配乐，还是从录制的视频中获取音频片段，这个工具都能够满足您的需求。

## 主要特点

- **简单易用**：提供了一个直观的用户界面，只需提供视频文件路径和输出音频文件路径，即可快速提取音频。
- **多种格式支持**：支持保存音频为常见的格式，如MP3、WAV、OGG等。
- **自定义编解码器**：支持自定义编解码器参数，以便根据需要选择合适的音频编码格式。
- **基于pydub库**：使用了功能强大且易于使用的pydub库来处理音频，确保提取过程高效且稳定。

## 安装

使用以下命令安装所需的依赖库：

```
pip install pydub
```

确保您的环境中已经安装了FFmpeg工具。如果尚未安装，请根据您的操作系统进行安装。

- **Windows**: 可以从 [FFmpeg官方网站](https://ffmpeg.org/download.html#build-windows) 下载预编译的静态版本，并将其添加到系统路径中。
- **macOS**: 使用Homebrew进行安装，运行以下命令：

```
brew install ffmpeg
```

- **Linux**: 使用适合您的包管理器进行安装，例如：

```
apt-get install ffmpeg
```

## 使用

1. 克隆项目到本地：

```
git clone https://github.com/your-username/audio-extraction-tool.git
```

2. 进入项目目录：

```
cd audio-extraction-tool
```

3. 创建一个Python虚拟环境（可选）：

```
python -m venv venv
```

4. 激活虚拟环境：

- **Windows**:

```
venv\Scripts\activate
```

- **macOS/Linux**:

```
source venv/bin/activate
```

5. 安装依赖库：

```
pip install -r requirements.txt
```

6. 运行音频提取工具：

```
python audio_extraction.py
```

7. 按照提示输入视频文件路径和输出音频文件路径，然后按回车键开始音频提取。

## 贡献

如果您对这个项目感兴趣并希望做出贡献，欢迎提交问题和拉取请求。在提交拉取请求之前，请确保您的代码经过了适当的测试，并遵循项目的代码风格和指南。

## 许可证

这个项目采用了 [MIT许可证](LICENSE)，请查阅许可证文件了解更多详情。
```
