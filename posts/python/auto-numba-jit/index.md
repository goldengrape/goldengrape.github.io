<!--
.. title: 自动添加Numba-jit修饰
.. slug: auto-numba-jit
.. date: 2017-12-28 15:00:20 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

今天拖延症犯了. 我的拖延症表现是狂做另一件以后可能用到, 但现在无关紧要的事情. 比如加速python的运行速度.

# Numba
[Numba](https://numba.pydata.org/)是个很神奇的东西, 加上以后可以提高python的运行速度.
<!-- TEASER_END -->

这里有一篇报道翻译, [使用NumPy、Numba和Python异步编程的高性能大数据分析与对比](http://www.infoq.com/cn/news/2017/08/NumPy0-Numba-Python)

直接看我在自己电脑上测试的结果:

| 行数     | numpy   | numpy+numba   |
| :------------- | :------------- |------------- |
| 10^7    | 9.1       |1.2秒       |
| 10^8    | 99.7       |4.9秒       |

报道里还有22. 6分钟对40.2秒的成绩, 我可不会去测试的.


Numba在使用时几乎不用修改代码, 最简单的用法就是在每个函数之前加入@jit的修饰, 这篇报道里就是这么做的. 感觉是免费升级了电脑.

# 自动给每个函数加@jit

但我连给函数加@jit都懒得做, 既然是好像加错了也没有太多的坏处, 那干脆统一给所有的函数都加上这个修饰好了.

所以, 就干脆写了一段代码, 把py文件/ipynb文件当作文本处理, 用正则表达式搜索出所有的函数定义, 在前面加一句@jit好了.

复习了一下正则表达式. 之前写[<序列一致性检验工具>]()的时候, 主要练习的是正则表达式中的查找, 这一次练习的是替换.

此处请参考[Python3 cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p05_search_and_replace_text.html), 需要小心的一个问题是, 如果用非转译的"\n"来替换字符串的时候, re.sub好像容易把\n给翻译了, 用\\n也没有办法. 但用.replace还是可以的. 在处理ipynb文件的时候费了很大周折.

代码在[这里](https://github.com/goldengrape/decorate_with_numba_jit)

# 使用说明
* 对本路径下所有的py文件添加@jit修饰, 并存入outputpath中
```python
python3 decorate_with_jit.py --a allpy outputpath
```
* 对本路径下所有的ipynb文件添加@jit修饰, 并存入outputpath中
```python
python3 decorate_with_jit.py --a allipynb outputpath
```
* 对本路径下所有的py文件去除@jit修饰, 并存入outputpath中
```python
python3 decorate_with_jit.py --r allpy outputpath
```
* 对本路径下所有的ipynb文件去除@jit修饰, 并存入outputpath中
```python
python3 decorate_with_jit.py --r allipynb outputpath
```

* 对文件A.py添加@jit修饰, 并保存为文件B.py
```python
python3 decorate_with_jit.py --a A.py B.py
```
* 对文件A.py去除@jit修饰, 并保存为文件B.py
```python
python3 decorate_with_jit.py --r A.py B.py
```






EOF.
