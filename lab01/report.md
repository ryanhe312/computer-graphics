<h3 align="center">编程实现音乐节奏或旋律的可视化</h3>
<p align="center">16307110216 何瑞安</p>

#### 一、程序说明

##### 1. 功能说明

我们实现了根据音乐的音高、时值和音量的旋律可视化，我们使用短时傅里叶变换，得到每一小段的音高音量的分布，然后绘图进行可视化。

##### 2. 运行说明

本项目代码包含一个`main.py`文件、一个文档`report.pdf`和一个演示视频`demo.mp4`。其中`main.py`是Python源代码，可以直接在Python环境中执行。

Python环境运行中请提前用`pip`安装`librosa`，`numpy`和`matplotlib`的包，然后运行`main.py`程序。演示视频的录制环境是 MacOS Catalina 10.15.7 (19H15)，Python 3.8.5。

```bash
pip install librosa numpy matplotlib
python main.py
```

##### 3.实现说明

我们使用的`librosa`库是一个非常强大的Python语音信号处理的第三方库，里面有很多实现好的信号处理函数和模块，我们使用它的读取波形函数（load）和短时傅里叶变化函数（stft）以及振幅分贝转换函数（amplitude_to_db）进行处理。它也有一些内置的音乐样例，比如我们这里使用的匈牙利舞曲（Brahms - Hungarian Dance #5）。

我们使用的`numpy`库是用Python进行科学计算的基础软件包，能够很方便的对向量、矩阵进行操作，我们这里用`numpy`对生成的特征向量以及绘制的图形进行处理。

我们使用的`matplotlib`库是Matplotlib是一个用于在Python中创建静态，动画和交互式可视化的综合库，我们利用`matplotlib`的动画功能，绘制根据音乐音高不断变化的直方图。

#### 二、算法原理

1. 波形图与频谱

波形图是音频的振幅（或能量）的图形表达，波形图的横坐标一般为时间，纵轴为振幅。我们通过WAV音频文件提取出来的就是各个时值的振幅，这样的图形我们无法得到频率的信息，所以我们还需要进行一定的处理。

我们可以通过短时距傅立叶变换得到每一个时刻的频谱，频谱是一个以幅度及相位为纵轴，频率为横轴的图像。我们通过观察频谱就可以得到音乐旋律的信息。我们将频谱绘制成直方图形式，当某个频率的幅度大时相应的直方图的组高度会越高。

2. 短时傅里叶变换

短时距傅立叶变换（STFT）通过在短重叠窗口上计算离散傅里叶变换（DFT）来表示时频域中的信号。实际上，计算短时距傅立叶变换(STFT)的过程是将长时间信号分成数个较短的等长信号，然后再分别计算每个较短段的傅立叶转换。通过短时傅里叶变换我们就可以获得这一小段时间内的频率与振幅的关系。

$$
X(t,f)=\int _{-\infty }^{\infty }w(t-\tau )x(\tau )e^{-j2\pi f\tau }\,d\tau
$$


#### 三、参考文献

[1] McFee, Brian, Colin Raffel, Dawen Liang, Daniel PW Ellis, Matt McVicar,  Eric Battenberg, and Oriol Nieto. "librosa: Audio and music signal  analysis in python." In Proceedings of the 14th python in science  conference, pp. 18-25. 2015.

[2] Oliphant, Travis E. *A guide to NumPy*. Vol. 1. USA: Trelgol Publishing, 2006.

[3] Hunter, John D. "Matplotlib: A 2D graphics environment." *Computing in science & engineering* 9.3 (2007): 90-95.