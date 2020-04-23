<!--
.. title: AI 4 Med 笔记(1.1)胸片诊断
.. slug: AI4med_note_1_1
.. date: 2020-4-23 12:01 UTC+08:00
.. tags: AI4med
.. category: 医学
.. link:
.. description:
.. type: text
-->

第一门课叫AI For Medical Diagnosis, 也就是用于诊断的AI. 有三周的课程

用于诊断一般就是图像识别, 看胸片、眼底照片、CT、核磁. 其中MRI是3D数据, 其他一般是二维. 

诊断问题一般就是二分类, 有病或者没病.  

二分类的loss很简单:

L(X,y)=

* -log(P(Y=1|X)) if y==1
* -log(P(Y=0|X)) if y==0

就是把卷积神经网络CNN最后一步的激活函数设成sigmoid, 得到一个在[0,1]之间的概率, 对这个数字求-log. 

<!-- TEASER_END -->

# 第一周

以胸片为目标来讲解, 用的是[Densenet](https://www.jiqizhixin.com/graph/technologies/d4b7fe6b-e73a-4ad3-af08-1b323f78333b)
![](https://image.jiqizhixin.com/uploads/editor/f5a9d3d0-9656-4367-9bd1-22f466603bfa/1560459229738.png)

和ResNet差不多, 只不过短路的路径可以更多一些, 方便在网络过深时梯度的传递.

讲训练阶段常见的几个问题: 

* imbalance问题: 数据集中病人总是少数
* 多任务问题: 一张片子上, 可能同时有几种病
* 训练集数量少


## imbalance问题

通常来说得病的都是少数, 正常的数据总是更多一些, 那么在训练集中就有阳性与阴性不平衡的问题. 老师讲到应该计算一下总的loss, 看看来自阳性和阴性结果的贡献比例, 应当比较均衡, 这样在训练时去减少loss的时候, 才能够同时优化阳性和阴性的结果. 

所以, 有几种解决方案:

### loss权重方案

我比较喜欢这个方案, 对阳性和阴性的结果添加不同的权重, 使得两部分的贡献更均衡. 如果病人(阳性结果)很少, 那么如果真实值是阳性, 算错了, 就要给更强的惩罚. 

Loss(X,y) =  

* Wp x -log P(Y=1|X), if y=1
* Wn x -log P(Y=0|X), if y=0

其中:
* 阳性权重 Wp=阴性数量/总数
* 阴性权重 Wn=阳性数量/总数

### 重采样方案

如果不改权重, 那么就让训练集中较少的阳性数据被更多次采样. 个人不喜欢, 写代码也麻烦, 可能还容易过拟合.

## 多任务问题

如果是同一张片子上看多个疾病, 就是同时进行多个问题的二分类. (但这样也就切断了疾病之间的联系). 于是把各个疾病的loss加起来就好了.

Loss=L(X, y_疾病0)+L(X, y_疾病1)+L(X, y_疾病2)...

## 训练集数量少

理论上, 而且通常也都是要做数据集的扩充, 把图片移动一下位置、轻微旋转一下之类, 但是注意不要做镜像了, 心脏位置是分左右的. 镜像了诊断可就不一样了. 也就是说, 对图像的扩充修改必须在不影响诊断的基础上进行. 

病例数量这种事, 就是资源的问题吧, 没钱也真是没办法. 

数量少, 就只好使用迁移学习了, 就是把已经训练好的神经网络拿来用, 但是留下最后一层重新训练一下. 

# 训练结果评估

## 分割数据集

数据集要分成train、val、test. 对于医疗数据, 要注意一个病人可能会拍好几张片子, 在分割数据集的时候, 要以病人为单位来分割, 而不能以数据集中的图像来作为单位. 

也就是说一个病人所有的片子, 要么都在训练集里, 要么都在测试集里, 不能同时出现在训练集和测试集里. 否则可能出现数据泄露的问题, 比如患者一直都戴着项链, AI可能识别的是项链, 而不是肺部的纹理. 

## 金标准

要训练机器去学习诊断, 人类给出的诊断要可靠才行, 金标准要么有更进一步的检查, 要么就是委员会投票表决. 

# 代码操作时的问题

这个系列的课程, 课程讲解只占了一部分的知识, 还有很多是在代码里. 

## 探索数据

拿到一个数据集, 先得看看. 检查一下标签数据表的结构, 看看各个字段的数据类型, 检查一下是否有null value, 用```df.info()```可以看个大概. 

要检查一下ID的独立性, 统计一下独立的ID有多少, 是不是少于总数. 

要看看各个标签下阳性的数据量大概是多少. 

打印几张图出来看看. 

## 图像预处理

keras有现成的预处理工具 [ImageDataGenerator](https://keras-cn.readthedocs.io/en/latest/preprocessing/image/)

现把图像按照自身的均值和方差标准化一下, 注意是按照自身的均值和方差, 而不是多个样本的均值和方差. 概念上会不一样. 

```python
from keras.preprocessing.image import ImageDataGenerator
# Normalize images
image_generator = ImageDataGenerator(
    samplewise_center=True, #Set each sample mean to 0.
    samplewise_std_normalization= True # Divide each input by its standard deviation
)
```

然后生成一个generator
```python
# Flow from directory with specified batch size and target image size
generator = image_generator.flow_from_dataframe(
        dataframe=train_df,
        directory="nih/images-small/", # 存放路径
        x_col="Image", # features
        y_col= ['Mass'], # labels
        class_mode="raw", # 'Mass' column should be in train_df
        batch_size= 1, # images per batch
        shuffle=False, # shuffle the rows or not
        target_size=(320,320) # width and height of output image
)
```
可以统一输出大小. 不过吐槽一下, 320x320的图像就能诊断了, 拍那么高清的片子干啥.

## 数数

记得要给每一个标签数出有多少阳性多少阴性, 然后生成loss的权重. 

$$ loss^{(i)} = loss_{阳性}^{(i)} + los_{阴性}^{(i)} $$

$$loss_{阳性}^{(i)} = -1 \times weight_{阳性}^{(i)} \times y^{(i)} \times log(\hat{y}^{(i)} + \epsilon)$$

$$loss_{阴性}^{(i)} = -1 \times weight_{阴性}^{(i)} \times (1- y^{(i)}) \times log(1 - \hat{y}^{(i)} + \epsilon)$$

$$\epsilon = \text{小量}$$

注意计算权重的时候, 是反过来的, 

weight_{阳性}= 阴性数量/总数

才能达到阴阳调和的目的. 

## 病人重叠和数据泄露

训练集的信息不能泄露到了测试集里. 
在医学数据里, 就要检查训练集合和测试集合里是不是有同样的ID, 如果有同一个病人出现在两边, 注意, AI很可能去看他/她的项链或者戒指去了. 

## DensNet121

作业中使用的深度学习网络是[DensNet121](https://www.kaggle.com/pytorch/densenet121)

Keras里有直接写好的, 直接导入就可以了, 我看这前后也通用, 抄下来.

```python
from keras.applications.densenet import DenseNet121
# create the base pre-trained model
# 导入的时候最后一层数据不要
base_model = DenseNet121(weights='./nih/densenet.hdf5', include_top=False) 

x = base_model.output

# add a global spatial average pooling layer
x = GlobalAveragePooling2D()(x)

# and a logistic layer
# 来一层sigmoid, 得到一个[0,1]的预测概率
predictions = Dense(len(labels), activation="sigmoid")(x)

model = Model(inputs=base_model.input, outputs=predictions)

# 用adam训练
model.compile(optimizer='adam', loss=get_weighted_loss(pos_weights, neg_weights))
```

需要训练的话:
```python
history = model.fit_generator(train_generator, 
                              validation_data=valid_generator,
                              steps_per_epoch=100, 
                              validation_steps=25, 
                              epochs = 3)

plt.plot(history.history['loss'])
plt.ylabel("loss")
plt.xlabel("epoch")
plt.title("Training Loss Curve")
plt.show()
```
不过老师在题目里一个劲的劝, 40GB+的数据量, 大家就用我们算好的吧. 

## GradCAM

[GradCAM](https://arxiv.org/abs/1610.02391)太帅了! 可以给出一个热区图, 看哪部分跟诊断关系最密切. 这么有用的工具, 居然就在课程作业里悄悄带过了. 于是我也不知道具体的用法, 但以后自己做东西的话, 一定要用上这个. 

![下载 (1)](https://i.imgur.com/iMYOsTF.png)

关于GradCAM的[参考](https://www.jiqizhixin.com/articles/where-cnn-is-looking-grad-cam)、[Keras实现教程](https://www.pyimagesearch.com/2020/03/09/grad-cam-visualize-class-activation-maps-with-keras-tensorflow-and-deep-learning/)
