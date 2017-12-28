<!--
.. title: 序列一致性检验工具
.. slug: compare-seq
.. date: 2017-12-28 15:00:07 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

本程序用于检查专利文件中的蛋白质序列是否一致. 在专利撰写时, 发明人往往在技术交底书中使用Word文件来提交蛋白质序列. 而在USPTO的要求中, 需要使用PatentIn软件来生成标准的序列提交文件.

<!-- TEASER_END -->

专利代理人在撰写专利说明书时可能通过ctrl+C/ ctrl+V 等操作将技术交底书中的序列复制粘贴到PatentIn软件中, 在这一动作中有可能引起增加或减少字母, 造成说明书中的序列与发明人所期望的序列不一致.

# 适用文件形式

适用文件的样例在demo文件夹中. 其中:

* 技术交底书样例, AAA.docx,序列以word表格的形式出现
* PantentIn生成文件样例, BBB.txt

# 安装

推荐使用Microsoft Azure Notebooks在云端运行.

## Azure Notebooks安装

* 打开https://notebooks.azure.com 以注册或以MS账户登录.
* 新建Lib: +New Library
* 从Github中导入:
    *  在GitHub repository中填入: https://github.com/goldengrape/check_patentIn_sequence
    * 自行设定好Library Name和Library ID
    * Import
* 设置:
    * 选择刚刚建立的Library, 点击Setting
    * Infomation:  如果不想泄露数据, 请确认 Public library **不**被选上
    * Environment:  Shell scirpt->script.txt

## 在本地电脑安装

### 依赖包
* python 3.5
* biopython
* python-docx
* numpy
* pandas

太麻烦了, 你不会真的打算本地运行吧. 实在要装的话推荐使用anaconda进行安装, 但anaconda装python-docx有坑, 最好调用anaconda下的pip进行安装python-docx.

### 安装
从github clone.

# 使用
* 上传或copy需要检查校对的文件到指定的目录.
* 打开compare_seq.ipynb
* 设定文件名:
    ```
    input_path='demo'
    output_path='demo'
    docx_name='AAA.docx'
    txt_name='BBB.txt'
    ```
* 指定word文件中表格的属性
    ```
    table_catalog_dict={
        0: {"head": 1, "seqtype":'chain', "chaintype":'HeavyChain'},
        1: {"head": 1, "seqtype":'chain', "chaintype":'LightChain'},
        2: {"head": 2, "seqtype":'CDR', "chaintype":'HC'},
        3: {"head": 2, "seqtype":'CDR', "chaintype":'LC'},
        4: {"head": 1, "seqtype":'chain', "chaintype":'HeavyChain'},
        5: {"head": 1, "seqtype":'chain', "chaintype":'LightChain'},
    ```
    其中:
    * head: 表格中标题行的行数
    * seqtype: 表格所描述的序列是长链chain或是CDR
    * chaintype: 序列的类型, 是
        * HeavyChain: 重链
        * LightChain: 轻链
        * HC: 重链CDR
        * LC: 轻链CDR
* 完成设定后, 在菜单中选择Kernel->restart&run all
* 结果:
    * 结果首先会显示在程序页面中
    * 结果以report.txt文件存储在output_path所指定的路径中
    * 为方便进一步处理,
        * PatnetIn生成的txt文件, 会被转换成同名的json文件和csv文件.
        * word文件, 会被转换成同名的csv文件.

# 更新

本程序还将不断更新.
## 在Azure Notebooks中更新
* 点击Terminal
* 输入```cd Library```
* 输入```git checkout . ``` 注意末尾有个点
* 输入```git pull```
