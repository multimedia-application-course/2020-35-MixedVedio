import os
import sys
from pychorus import find_and_output_chorus


def extract_all_file(files_path):

    """
    批量提取音乐高潮
    Args:
        files_path (str): 文件夹路径
    """
    # 文件夹路径
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    for filepath in os.listdir(files_path):
        # 路径处理
        datapath = os.path.join(modpath, files_path + filepath)
        # output文件夹是否存在
        targets = f"{modpath}\\output\\"
        if not os.path.exists(targets):
            os.makedirs(targets)
        # 提取音乐高潮至当前output文件夹下
        find_and_output_chorus(
            datapath, f"{targets}{filepath.split('.')[0]}_high.wav", 40
        )
