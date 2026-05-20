# 例3.19 用Matlab求直流电机的传递函数

在例 2.13 中，假设 $J_{m}=0.01kg\cdot m^{2}$ ， $b=0.001N\cdot m\cdot s$ ， $K_{t}=K_{e}=1$ ， $R_{a}=10\Omega$ 和 $L_{a}=1H$ 。

(1) 求输入 $v_{a}$ 和输出 $\theta_{m}$ 之间的传递函数；

(2) 求输入 $v_{a}$ 与输出 $\omega = \dot{\theta}_{m}$ 之间的传递函数。

解答。

(1) 将上述参数带入到例 2.13，求出系统的传递函数为

$$H (s) = \frac {1 0 0}{s ^ {3} + 1 0 . 1 s ^ {2} + 1 0 1 s} = \frac {1 0 0}{s (s ^ {2} + 1 0 . 1 s + 1 0 1)}$$

在 Matlab 中，我们看到将传递函数的分子多项式系数表示成行矢量 numa 和将分母多项式系数表示成行矢量 denA。所得结果为

$$
\mathrm{numa} = \left[ \begin{array}{l l l l} 0 & 0 & 0 & 1 0 0 \end{array} \right], \quad \mathrm{dena} = \left[ \begin{array}{l l l l} 1 & 1 0. 1 & 1 0 1 & 0 \end{array} \right]
$$

用 Matlab 命令 $[z, p, k] = tf2zp(numa, dena)$ 计算零极点。

结果为

$$
\begin{array}{l} z = [ ], \quad p = [ 0 - 5. 0 5 0 0 + 8. 6 8 8 9 j - 5. 0 5 0 0 - 8. 6 8 8 9 j ] ^ {\mathrm{T}} \\ k = 1 0 0 \\ \end{array}
$$

从而可得传递函数的因式分解形式为

$$H (s) = \frac {1 0 0}{s (s + 5 . 0 5 + \mathrm{j} 8 . 6 8 8 9) (s + 5 . 0 5 - \mathrm{j} 8 . 6 8 8 9)}$$

（2）如果我们认为角速度 $\dot{\theta}_{m}$ 为输出，那么可以求出 $numb=[0\quad0\quad100]$ ， $denb=[1\quad10.1\quad101]$ ，可得传递函数为

$$G (s) = \frac {1 0 0 s}{s ^ {3} + 1 0 . 1 s ^ {2} + 1 0 1 s} = \frac {1 0 0}{s ^ {2} + 1 0 . 1 s + 1 0 1}$$

这是预料之内的，因为 $\dot{\theta}_{m}$ 仅为 $\theta_{m}$ 的导数；所以 $\mathcal{L}(\dot{\theta}_{m}) = s\mathcal{L}\{\theta_{m}\}$ 。对于单位阶跃输入 $v_{a}$ ，用 Matlab 可以计算出阶跃响应（重提例 2.1），其语句如下。

s=tf('s'); % define Laplace variable
sysb=100/(s^3+10.1*s^2+101*s) % form transfer function
t=0:0.01:5; % form time vector
y=step(sysb,t) % compute step response;
plot(t,y) % plot step response

该系统产生一个稳态恒定角速度，如图 3.6 所示，由于系统没有单位交流增益，故曲线存在轻微波动。

当用一个任意阶的微分方程描述动态系统时，用微分方程求多项式形式的传递函数往往比较容易。因此，在这些情况下，最好用传递函数的形式来直接描述系统。
