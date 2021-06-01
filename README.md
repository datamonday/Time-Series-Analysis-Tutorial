# 时间序列分析——分类与预测教程

作者：datamonday

贡献者：datamonday

Github：https://github.com/datamonday/Time-Series-Forecasting-Algorithm

CSDN：[原理+论文+实战：60篇由浅入深的时间序列预测/分类教程汇总](https://blog.csdn.net/weixin_39653948/article/details/105571760?spm=1001.2014.3001.5502)

初次发布：2020-04-17

最后修改：2021-06-01

---

# 更新日志

## 2021-06-01

- 更新Python datetime模块和Pandas 时间序列数据处理的相关知识及代码

---

[toc]

---

# 前言

⏱最一段时间都在学习时间序列预测和时间序列分类相关的知识，一开始感觉无从下手，论文看不懂，代码不会写。经过近三个月的摸索，也算是入门的小白了，这篇博文算是个人经过踩坑，去粗取精之后的经验总结。通过**4篇博客、9篇论文、32篇实战教程**，梳理出了一套系统化的时间序列预测和时间序列分类任务的入门指南。**文中提及的博客论文和教程全部内容字数大约在50万字到100万字之间**。既是对这段时间所学知识的梳理总结，也希望给有需要的同学提供帮助。水平有限，如有问题欢迎指出，谢谢。

---
🎯【**适用人群**】：
- 没有时间序列预测/分类相关的经验的**小白**。

---
⌨【**代码环境**】：
- python 3.7.6
- tensorflow 2.1.0 

---
🔊【**注意事项**】：

- **因为tensorflow 2.0版本开始集成了keras，成为了 `tensorflow.keras` API，因此不用额外安装，并且无需 ~~import keras~~。**

- **本文提及文章的神经网络编写部分使用Keras深度学习框架。**

- **本文提及文章的所有代码均在Jupyter Notebook中编写，并测试通过。**

- **本文提及的所有文章中，参考资料均在每篇文章的文末给出。**

---
📽【**行文顺序**】：
- 原理篇：逻辑顺序
- 论文篇：时间顺序
- 实战篇：逻辑顺序+时间顺序

- 注：本文提及的网络架构、论文、教程都是按照由浅入深介绍的，教程部分（三、实战篇）有些教程是有相互关联的。

---
📖【**主要内容**】：时间序列任务分为**时间序列预测**和**时间序列分类**两种类型，本文主要内容如下：
- **LSTM** 及其不同的网络架构处理时间序列预测/分类任务；
- **CNN** 及其不同的网络架构处理时间序列预测/分类任务；
- **CNN-LSTM** 网络处理时间序列预测/分类任务；
- **ConvLSTM** 网络处理时间序列预测/分类任务；
- **DeepConvLSTM** 网络处理时间序列分类任务；
- **LSTM-FCN** 网络处理时间序列分类任务；
- **Multivariate LSTM-FCNs** 网络处理时间序列分类任务
---
# 一、原理篇
**本部分所有标题都设置了对应文章超链接，直接点击传送。**

**如果对下文提及的原理比较熟悉，可以直接跳过。**

---
## 1.1 CNN 
**1. [零基础入门深度学习(4) - 卷积神经网络](https://www.zybuluo.com/hanbingtao/note/485480)**
- 文章日期：2017/08/28
- 内容梗概：CNN算法原理+数学推导+代码实现

---
## 1.2 RNN
**2. [零基础入门深度学习(5) - 循环神经网络](https://zybuluo.com/hanbingtao/note/541458)**
- 文章日期：2017/08/28
- 内容梗概：RNN算法原理+数学推导+代码实现

---
## 1.3 LSTM

**3. [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)**
- 文章日期：2015/08/27
- 适合人群：了解LSTM的基本原理。

相信大家看过的很多介绍LSTM原理的文章都用到了这篇文章的配图。

---
**4. [零基础入门深度学习(6) - 长短时记忆网络(LSTM)](https://zybuluo.com/hanbingtao/note/581764)**
- 文章日期：2017/08/28
- 内容梗概：LSTM算法原理+数学推导+代码实现

这三篇文章（本篇+之前同系列两篇）应该是我目前遇到的讲解得最详细最全面思路最清晰的文章，由浅入深，原理+推导+代码，墙裂推荐。

---
# 二、论文篇
本部分主要内容：
- 时间序列分类任务数据集构建（人类活动识别）
- CNN-LSTM 网络
- ConvLSTM 网络
- DeepConvLSTM 网络
- LSTM-FCN 网络

本部分可以先跳过，直接看实战篇，如果对其中的网络架构有疑问或者有些内容看不懂，再阅读这些论文也可以。

---
## 2.1 WISDM 实验室论文
**1. [Activity Recognition using Cell Phone Accelerometers](https://blog.csdn.net/weixin_39653948/article/details/104566858)**
- 论文被引：2034
- 论文年份：2010

WISDM实验室应该是最早开始做基于手机传感器的**人类活动识别**的实验室，手机的数据只有**3个特征（3轴传感器数据）**。这篇论文是该实验室的第一篇论文，主要介绍了**关于数据集的构建与处理**。

---
**2. [Cell Phone-Based Biometric Identification](https://blog.csdn.net/weixin_39653948/article/details/104566905)**
- 论文被引：262
- 论文年份：2010

这篇论文是该实验室的第二篇论文，主要介绍了 **数据收集以及将时间序列数据转换为样本的过程**，值得借鉴。

该实验室还有3篇论文，个人感觉参考意义不大，可以先不看。

---
## 2.2 UCI-HAR 数据集论文
**1. [Human Activity Recognition on Smartphones using a Multiclass Hardware-Friendly SVM](https://blog.csdn.net/weixin_39653948/article/details/104563715)**
- 论文被引：619
- 论文年份：2012

这篇论文是创建该数据集的实验室发表的有关人类活动识别的第一篇论文，主要介绍了使用监督机器学习方法通过手机传感器信号来识别人类活动（**6类**，分别是站立，行走，放置，行走，上楼和在下楼）进行分类。使用**9个特征**（6轴传感器+3个分离信号（身体重力加速度））。

---
**2. [A Public Domain Dataset for Human Activity Recognition Using Smartphones](https://blog.csdn.net/weixin_39653948/article/details/104638860)**
- 论文被引：763
- 论文年份：2013

这篇论文介绍了 UCI-HAR Dataset数据集是如何创建的，很有借鉴意义，如果做**时间序列分类**任务的话，是**必读论文**。

---
## 2.3 CNN-LSTM 论文
**1. [Long-term Recurrent Convolutional Networks for Visual Recognition and Description](https://arxiv.org/abs/1411.4389)**
- 论文被引：3634
- 论文年份：2015

该论文提出的网络架构最初被称为长期循环卷积网络（LRCN），现在使用“CNN LSTM”来指代使用CNN作为前端的LSTM。该网络架构最初用于**生成图像的文本描述**的任务。关键是CNN，该CNN在图像分类任务上进行了预训练，使得可以用作字幕生成的特征提取器。

---
**2. [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/abs/1411.4555)**
- 论文被引：3378
- 论文年份：2015

该论文提出的网络架构用于语音识别和自然语言处理问题，其中CNN用作音频和文本输入数据上的特征提取器，之后输入到LSTM进行进一步处理。

这两篇论文是CNN-LSTM网络家族的开篇之作，是必读论文。

---
## 2.4 ConvLSTM 论文
**1. [Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting](https://blog.csdn.net/weixin_39653948/article/details/104575175)**
- 论文被引：1787
- 论文年份：2015

这篇论文是最先提出 ConvLSTM 网络架构的论文，该论文是用于**预测**相对短时间内某个地区未来的**降雨强度**，属于必读论文。

---
## 2.5 DeepConvLSTM 论文
**1. [Deep Convolutional Neural Networks On Multichannel Time Series For Human Activity Recognition](https://blog.csdn.net/weixin_39653948/article/details/104526849)**
- 论文被引：541
- 论文年份：2015

在基准数据集上对所提方法与现有方法的比较进行了广泛的研究。结果表明，该方法是一种很有竞争力的HAR问题求解算法。该论文还研究了CNN的效率，并得出结论：**CNN对于在线人类活动识别是足够快的**。

---
**2. [Deep Convolutional and LSTM RNN for Multimodal Wearable Activity Recognition](https://blog.csdn.net/weixin_39653948/article/details/104536187)**
- 论文被引：836
- 论文年份：2016

该论文提出了**DeepConvLSTM网络架构**：由卷积层和LSTM循环层组成的深度学习框架，它能够自动学习特征表示并对它们的激活之间的时间依赖性进行建模。通过业内的标准的**人类活动识别数据集（OPPORTUNITY和Skoda）**进行实验，证明此框架适**用于可穿戴传感器数据的活动识别**。属于必读论文。

---
## 2.6 LSTM-FCN 论文
**1. [LSTM Fully Convolutional Networks for Time Series Classification](https://arxiv.org/abs/1709.05206)**
- 论文被引：211
- 论文年份：2017

该论文提出的模型**在显著地提高全卷积网络性能的同时保证模型大小只有很少的增加**，并且**几乎不需要对数据集进行预处理**。提出的长短期记忆-全卷积网络 **（LSTM-FCN）** 与其他网络相比，具有最新的性能。利用注意力-长短期记忆-全卷积网络 **（ALSTM-FCN）**，探讨了注意力机制在时间序列分类中的应用。**利用注意力机制可以可视化LSTM细胞的决策过程**。此外，还提出了**微调的方法来提高训练模型的性能**。对模型的性能进行了全面的分析，并与其他技术进行了比较。

---
**2. [Multivariate LSTM-FCNs for Time Series Classification](https://arxiv.org/abs/1801.04503)**
- 论文被引：70
- 论文年份：2018

该论文提出将现有的单变量时间序列分类模型长短期记忆-全卷积网络（LSTM-FCN）和注意力-长短期记忆-全卷积网络（ALSTM-FCN）通过**在全卷积块上增加一个压缩和激励块来进一步提高分类精度**，从而转化为**多变量时间序列分类模型**。提出的模型在少量预处理的情况下优于大多数最新模型。所提出的模型**能有效地处理各种复杂的多元时间序列分类任务，如活动识别或动作识别**。此外，**所提出的模型在满足实时要求（小，快），可以部署在内存受限的系统上。**

---
# 三、实战篇
## 3.1 时间序列任务 入门篇
本部分不涉及具体的数据集，使用构造的数字序列；目的是通过程序了解网络架构和定义方法。

---
- [LSTM 01：理解LSTM网络及训练方法](https://blog.csdn.net/weixin_39653948/article/details/104966046)
- [LSTM 02：如何为LSTMs准备数据](https://blog.csdn.net/weixin_39653948/article/details/104425614) 
- [LSTM 03：如何用Keras编写 LSTMs](https://blog.csdn.net/weixin_39653948/article/details/104433698)
- [LSTM 04：4种序列预测模型及Keras实现](https://blog.csdn.net/weixin_39653948/article/details/104959294)
- [LSTM 05：如何用Keras开发 Vanilla LSTMs 和 Stacked LSTMs](https://blog.csdn.net/weixin_39653948/article/details/104974061)
- [LSTM 06：如何用Keras开发 CNN LSTM](https://blog.csdn.net/weixin_39653948/article/details/104982310)
- [LSTM 07：如何用Keras开发 Encoder-Decoder LSTM](https://blog.csdn.net/weixin_39653948/article/details/104990120)
- [LSTM 08：超详细LSTM调参指南](https://blog.csdn.net/weixin_39653948/article/details/105003294)

---
## 3.2 时间序列预测 基础篇
- [时间序列预测01：如何将时间序列预测转化为监督学习问题](https://blog.csdn.net/weixin_39653948/article/details/105332534)
- [时间序列预测02：经典方法综述 自回归ARIMA/SRIMA 指数平滑法等](https://blog.csdn.net/weixin_39653948/article/details/105333399)
- [时间序列预测03：如何为CNN/LSTM模型构建数据集](https://blog.csdn.net/weixin_39653948/article/details/105332338)
- [时间序列预测04：TF2.1开发多层感知器(MLPs)时间序列预测模型详解](https://blog.csdn.net/weixin_39653948/article/details/105341180)
- [时间序列预测05：CNN时间序列预测模型详解 01 Univariate CNN、Multivariate CNN](https://blog.csdn.net/weixin_39653948/article/details/105352010)
- [时间序列预测06：CNN时间序列预测模型详解 02 Multi-step CNN、Multivariate Multi-step CNN](https://blog.csdn.net/weixin_39653948/article/details/105362939)
- [时间序列预测07：如何开发LSTM实现时间序列预测详解 01 Univariate LSTM](https://blog.csdn.net/weixin_39653948/article/details/105366425)
- [时间序列预测08：如何开发LSTM实现时间序列预测详解 02 Multivariate LSTM](https://blog.csdn.net/weixin_39653948/article/details/105379715)
- [时间序列预测09：如何开发LSTM实现时间序列预测详解 03 Multi-step LSTM](https://blog.csdn.net/weixin_39653948/article/details/105385622)
- [时间序列预测10：如何开发LSTM实现时间序列预测详解 04 Multivariate Multi-step LSTM](https://blog.csdn.net/weixin_39653948/article/details/105391590)

---
## 3.3 时间序列预测 进阶篇
- [时间序列预测11：用电量预测 01 数据分析与建模](https://blog.csdn.net/weixin_39653948/article/details/105397315)
- [时间序列预测12：用电量预测 02 朴素模型多步预测建模](https://blog.csdn.net/weixin_39653948/article/details/105412563)
- [时间序列预测13：用电量预测 03 ARIMA模型多步预测建模](https://blog.csdn.net/weixin_39653948/article/details/105408755)
- [时间序列预测14：CNN 实现用电量/发电量预测](https://blog.csdn.net/weixin_39653948/article/details/105422337)
- **[时间序列预测15：Multi-input / Multi-head CNN 实现用电量/发电量预测](https://blog.csdn.net/weixin_39653948/article/details/105431099)**
- **[时间序列预测16：Encoder-Decoder LSTM 实现用电量/发电量预测](https://blog.csdn.net/weixin_39653948/article/details/105440090)**
- **[时间序列预测17：CNN-LSTM 实现用电量/发电量预测](https://blog.csdn.net/weixin_39653948/article/details/105446709)**
- **[时间序列预测18：ConvLSTM 实现用电量/发电量预测](https://blog.csdn.net/weixin_39653948/article/details/105447616)**

---
- [使用Keras实现预测燃油效率](https://blog.csdn.net/weixin_39653948/article/details/105720276)
- [使用Keras实现LSTM天气预测](https://blog.csdn.net/weixin_39653948/article/details/105927085)

---
## 3.3 时间序列分类 基础篇
- **[时间序列分类01：人类活动识别深度学习模型综述](https://blog.csdn.net/weixin_39653948/article/details/105447899)**
- **[时间序列分类02：数据可视化与问题分析建模流程详解（UCI-HAR）](https://blog.csdn.net/weixin_39653948/article/details/105453824)**
- **[时间序列分类03：如何开发CNNs模型实现人类活动识别（调参）](https://blog.csdn.net/weixin_39653948/article/details/105469455)**
- **[时间序列分类04：如何开发LSTMs模型实现人类活动识别（CNN-LSTM、ConvLSTM）](https://blog.csdn.net/weixin_39653948/article/details/105475898)**

---
## 3.4 时间序列分类 进阶篇 （⏳ 更新中···）
- [TensorFlow实现时间序列滑动窗口](https://blog.csdn.net/weixin_39653948/article/details/105928752)
- [Python yield 实现滑动窗口截取时间序列数据（滑动步长可调）](https://blog.csdn.net/weixin_39653948/article/details/105498685)
- [numpy unique() 方法实现将分类标签转化为数字编码（非one-hot）](https://blog.csdn.net/weixin_39653948/article/details/105516373)

---
# 四. 调参篇
- [深度学习模型24种优化策略详解](https://blog.csdn.net/weixin_39653948/article/details/105962427)

---
# 五. 相关论文（⏳ 更新中···）
1. [Energy consumption prediction using machine learning a review](https://blog.csdn.net/weixin_39653948/article/details/106676919)
2. [Electric Energy Consumption Prediction by Deep Learning with State Explainable Autoencoder](https://blog.csdn.net/weixin_39653948/article/details/106699229)
3. [Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting](https://blog.csdn.net/weixin_39653948/article/details/106751676)
4. [【CMU & AWS 2020】Forecasting Big Time Series: Theory and Practice（Part I）](https://blog.csdn.net/weixin_39653948/article/details/106724670)
5. [【CMU & AWS 2020】Forecasting Big Time Series: Theory and Practice（Part II）](https://blog.csdn.net/weixin_39653948/article/details/106725782)
6. [A review of data-driven building energy consumption prediction studies](https://blog.csdn.net/weixin_39653948/article/details/106774900)
7. [A Comparative Study of Time Series Forecasting Methods for Short T erm Electric Energy Consumption Prediction in Smart Buildings](https://datac.blog.csdn.net/article/details/107849204)

---
# 六. 注意力机制（2020/10/29更新）
1. [Attention Is All You Need（Transformer）](https://blog.csdn.net/weixin_39653948/article/details/107395533)
2. [【Attention】注意力机制简介](https://datac.blog.csdn.net/article/details/108987390)
3. [【Attention】注意力机制的直观理解](https://datac.blog.csdn.net/article/details/108988534)
4. [【Attention】图解 Attention](https://datac.blog.csdn.net/article/details/109322563)
5. [【Attention】注意力机制概述](https://datac.blog.csdn.net/article/details/109295433)
6. [【Transformer】How Transformers Work](https://datac.blog.csdn.net/article/details/109147855)
7. [【Transformer】图解 Transformer](https://datac.blog.csdn.net/article/details/109152169)

---
# 源码获取（2021）
**Github：[https://github.com/datamonday/Time-Series-Forecasting-Algorithm](https://github.com/datamonday/Time-Series-Forecasting-Algorithm)**

**部分源码已经放到Github了，欢迎Star，Fork！**

---
# 公众号
欢迎关注公众号，获取更多干货内容！
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210310095805745.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTY1Mzk0OA==,size_1,color_FFFFFF,t_70#pic_center)


---
以上是三个多月以来对时间序列预测和分类任务的总结，仅供参考。如果给你带来了帮助，请动动手指点个赞；如果对文中内容存疑，欢迎指出交流，谢谢各位人才。

刚开始的时候，无从下手，走了很多弯路。经过这段时间的试错和摸索，算是总结出了一些经验。上文提到的论文，是个人认为帮助比较大的论文，如果在做时间序列预测或分类任务的话最好看一下，理解其中的建模思路和网络架构的优缺点，以便快速上手。

实战篇的代码主要参考澳大利亚博主Jason Brownlee的博客文章，在此表示感谢。博客地址：[传送门](https://machinelearningmastery.com/)。

---