from pydub import AudioSegment
import os
import sys


def trans_any_audio_types(filepath, input_audio_type, output_audio_type):
    """"
    任意音频文件格式转化为任意音频文件格式
    filepath(str): 文件路径
    input_audio_type（str): 输入音频文件格式
    output_audio_type(str): 输出音频文件格式
    """

    song = AudioSegment.from_file(filepath, input_audio_type)
    filename = filepath.split('.')[0]
    song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")


def trans_all_file(files_path, target="mp3"):
    """
    批量转化音频音乐格式
    Args:
        files_path (str): 文件夹路径
        target (str, optional): 目标音乐格式. Defaults to "mp3".
    """
    for filepath in os.listdir(files_path):
        # 路径处理
        modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        datapath = os.path.join(modpath, files_path + filepath)
        # 分割为文件名字和后缀并载入文件
        input_audio = os.path.splitext(datapath)
        song = AudioSegment.from_file(datapath, input_audio[-1].split(".")[-1])
        # 导出
        song.export(f"{input_audio[0]}.{target}", format=target)


