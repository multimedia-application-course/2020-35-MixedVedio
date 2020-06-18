# 2020-35-MixedVedio
项目介绍
=======
  本队伍此次大作业做的是一个混剪视频，题材是 中国唱诗班 中的一节。  
  具体视频请移步： https://www.bilibili.com/video/BV1C54y1B7jy 观看  
  在制作混剪视频当中，发现两个较为繁琐的工作：音频格式的转换和BGM的选择。  
  其中音频格式的问题还比较好解决，但是BGM的选择就比较难，因为需要提取音乐的高潮部分。  
  为了解决以上两个问题，写了两份python代码，共享到此。  
    
  音频格式转换
  ===
  本功能使用Pydub模块实现。  
  Pydub是一个基于ffmpeg的Python音频处理模块，封装了许多ffmpeg底层接口，因此用它来做音乐歌曲文件格式转换会非常方便。  
  1.  安装  
    1.1 进入 http://ffmpeg.org/download.html#build-windows  ，点击windows对应的图标，进入下载界面点击 download 下载按钮。    
    1.2 解压好下载的ZIP文件到指定目录（任意你喜欢的目录下）  
    1.3 将解压后的文件目录中bin目录（包含ffmpeg.exe）添加进path环境变量中  
    1.4 打开命令提示符（cmd），安装pydub：  
   ` pip install pydub `  
  2. 使用Trans2Vedio.py 代码  
  3. ffpeg支持多种音频格式，具体请参考http://ffmpeg.org/ffplay.html
     
  音乐高潮部分提取
  ===
 1. 原理介绍  
 对音乐片段与片段之间的相似度进行计算，使用相似函数  
![相似函数]https://github.com/multimedia-application-course/2020-35-MixedVedio/Similar.png
