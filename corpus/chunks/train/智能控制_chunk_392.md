Hopfield 网络的动态特性要在状态空间中考虑, 分别令 $u = [u_{1}, u_{2}, \cdots, u_{n}]^{T}$ 为具有 n 个神经元的 Hopfield 神经网络的状态向量, $V = [v_{1}, v_{2}, \cdots, v_{n}]^{T}$ 为输出向量, $I = [I_{1}, I_{2}, \cdots, I_{n}]^{T}$ 为网络的外加输入。

为了描述 Hopfield 网络的动态稳定性, 定义标准能量函数为

$$E _ {N} = - \frac {1}{2} \sum_ {i} \sum_ {j} w _ {i j} v _ {i} v _ {j} + \sum_ {i} \frac {1}{R _ {i}} \int_ {0} ^ {v _ {i}} g _ {i} ^ {- 1} (v) d v - \sum_ {i} I _ {i} v _ {i} \tag {8.18}$$

若权值矩阵 W 是对称的 $(w_{ij} = w_{ji})$ ，则 $^{[16]}$

$$\frac {\mathrm{d} E _ {N}}{\mathrm{d} t} = \sum_ {i = 1} ^ {n} \frac {\partial E _ {N}}{\partial v _ {i}} \cdot \frac {\mathrm{d} v _ {i}}{\mathrm{d} t} + \sum_ {i = 1} ^ {n} \frac {\partial E _ {N}}{\partial w _ {i j}} \cdot \frac {\mathrm{d} w _ {i j}}{\mathrm{d} t} + \sum_ {i = 1} ^ {n} \frac {\partial E _ {N}}{\partial I _ {i}} \cdot \frac {\mathrm{d} I _ {i}}{\mathrm{d} t}$$

上式中右式的后两项可以很小, 原因如下: 首先, 由于 $\frac{\partial E_N}{\partial \omega_{ij}} = -\sum_i \sum_j v_i v_j, \frac{\partial E_N}{\partial I_i} = -\sum_i v_i$ , 故 $\frac{\partial E_N}{\partial \omega_{ij}}$ 和 $\frac{\partial E_N}{\partial I_i}$ 与 $v_i, v_j$ 有关, 而 $v_i, v_j$ 为双曲函数 $g(\cdot)$ 的有界输出; 其次, $W$ 和 $I$ 的表达式与系统状态有关, 如取 $u$ 为低速激活信号, 则系统状态值很小, 从而 $\frac{\mathrm{d}\omega_{ij}}{\mathrm{d}t}$ 和 $\frac{\mathrm{d}I_i}{\mathrm{d}t}$ 很小。令 $\sum_{i=1}^{n} \frac{\partial E_N}{\partial \omega_{ij}} \frac{\mathrm{d}\omega_{ij}}{\mathrm{d}t} + \sum_{i=1}^{n} \frac{\partial E_N}{\partial I_i} \frac{\mathrm{d}I_i}{\mathrm{d}t} = \Delta$ , 则上式可写为

$$\frac {\mathrm{d} E _ {N}}{\mathrm{d} t} = \sum_ {i = 1} ^ {n} \frac {\partial E _ {N}}{\partial v _ {i}} \cdot \frac {\mathrm{d} v _ {i}}{\mathrm{d} t} + \Delta = - \sum_ {i} \frac {\mathrm{d} v _ {i}}{\mathrm{d} t} \left(\sum_ {j} w _ {i j} v _ {j} - \frac {u _ {i}}{R _ {i}} + I _ {i}\right) + \Delta = - \sum_ {i} \frac {\mathrm{d} v _ {i}}{\mathrm{d} t} \left(C _ {i} \frac {\mathrm{d} u _ {i}}{\mathrm{d} t}\right) + \Delta \tag {8.19}$$

由于 $v_{i} = g(u_{i})$ ，则

$$\frac {\mathrm{d} E _ {N}}{\mathrm{d} t} = - \sum_ {i} C _ {i} \frac {\mathrm{d} g ^ {- 1} (v _ {i})}{\mathrm{d} v _ {i}} \left(\frac {\mathrm{d} v _ {i}}{\mathrm{d} t}\right) ^ {2} + \Delta \tag {8.20}$$

由于 $C_{i}>0$ ，双曲函数是单调上升函数，显然它的反函数 $g^{-1}(v_{i})$ 也为单调上升函数，即有 $\frac{\mathrm{d}g^{-1}(v_{i})}{\mathrm{d}v_{i}}>0$ ，取 $C_{i}$ 足够大，若能保证 $\Delta$ 足够小，则可得到 $\frac{\mathrm{d}E_{N}}{\mathrm{d}t}\leqslant0$ ，即能量函数 $E_{N}$ 具有负的梯度，当且仅当 $\frac{\mathrm{d}v_{i}}{\mathrm{d}t}=0$ 时 $\frac{\mathrm{d}E_{N}}{\mathrm{d}t}=0(i=1,2,\cdots,n)$ 。由此可见，随着时间的演化，网络的解在状态空间中总是朝着能量 $E_{N}$ 减少的方向运动。网络最终输出向量 V 为网络的稳定平衡点，即 $E_{N}$ 的极小点。

Hopfield 网络在优化计算中得到了成功应用,有效地解决了著名的旅行推销员问题(TSP 问题)。另外,Hopfield 网络在智能控制和系统辨识中也有广泛的应用。
