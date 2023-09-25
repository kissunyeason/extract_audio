from pydub import AudioSegment

def extract_audio():
    input_path = input("请输入视频文件路径：")
    output_path = input("请输入输出音频文件路径：")

    video = AudioSegment.from_file(input_path)
    audio = video.export(output_path, format='mp3')

    print("音频提取完成！")

extract_audio()
