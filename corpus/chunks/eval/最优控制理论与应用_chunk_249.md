# 6. 系统的复域与频域分析

对于根轨迹的绘制,控制系统工具箱中给出了一个函数 rlocus() 函数来绘制系统的根轨迹,该函数可以由如下格式来调用:

$$\mathrm{R} = \mathrm{rlocus} (\mathrm{G}, \mathrm{k})$$

对于 Nyquist 曲线的绘制, 控制系统工具箱中给出了一个函数 nyquist ( ) 函数, 该环数可以用来直接求解 Nyquist 阵列, 绘制出 Nyquist 曲线, 该函数可以由如下格式来调用:

$$[ \mathrm{rx}, \mathrm{ry} ] = \text { nyquist } (\mathrm{G}, \mathrm{w})$$

对于 Bode 图, MATLAB 控制工具箱中提供了 bode() 函数来求取、绘制系统的 Bode 图, 该函数可以由下面的格式来调用:

$$[ \mathrm{mag}, \mathrm{pha} ] = \mathrm{bode} (\mathrm{G}, \mathrm{w})$$
