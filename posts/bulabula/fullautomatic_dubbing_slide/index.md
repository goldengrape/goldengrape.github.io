<!--
.. title: 全自动录制幻灯片配音
.. slug: fullautomatic_dubbing_slide
.. date: 2019-3-10 00:00 UTC+08:00
.. tags: 
.. category: python
.. link:
.. description:
.. type: text
-->

OK, 完成了自动为PowerPoint幻灯片配音的python3程序. 

提取每一页幻灯片中的备注, 使用语音合成(Text-To-Speech, TTS)产生配音, 并将配音音频插入到幻灯片中. 如果在PowerPoint/ Keyote中导出成视频, 可以产生自动配演讲解的视频.

当前仅仅支持mac OS.

项目页面在[https://github.com/goldengrape/dubbing-pptx](https://github.com/goldengrape/dubbing-pptx)

需要先安装[python-pptx](https://github.com/scanny/python-pptx)

使用方法:
```python dubbing.py inputfile.pptx outputfile.pptx```