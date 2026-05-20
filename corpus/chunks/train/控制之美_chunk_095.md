# 5.3 二阶系统的单位阶跃响应

在 5.2 节中, 我们采用相轨迹的方法定性讨论了二阶系统对初始状态的响应。本节将采用传递函数的方法定量分析二阶系统的单位阶跃响应。读者在阅读过程中可以将这两节中所介绍的方法结合起来思考, 例如用传递函数的方法去求解初始状态问题, 或者用相轨迹的方法求解阶跃响应, 相信读者会对这部分内容有更深刻的理解。

当系统的输入为单位阶跃函数时, 输入的拉普拉斯变换为 $U(s)=\frac{1}{s}$ , 将其代入式(5.1.3), 可得

$$X (s) = G (s) U (s) = \frac {\omega_ {\mathrm{n}} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2}} \times \frac {1}{s} \tag {5.3.1}$$

令式(5.3.1)的分母等于0,可以求出三个极点,分别为

$$
\left\{ \begin{array}{l} s _ {\mathrm{p1}} = 0 \\ s _ {\mathrm{p2}} = - \zeta \omega_ {\mathrm{n}} + \omega_ {\mathrm{n}} \sqrt {\zeta^ {2} - 1} \\ s _ {\mathrm{p3}} = - \zeta \omega_ {\mathrm{n}} - \omega_ {\mathrm{n}} \sqrt {\zeta^ {2} - 1} \end{array} \right. \tag {5.3.2}
$$

通过 5.2 节的介绍, 不同的 $\zeta$ 值将对应不同的系统表现, 本节将详细推导其中一个最为复杂

的情况,即欠阻尼系统 $0<\zeta<1$ , 并分析它的系统响应。当 $0<\zeta<1$ 时, 式(5.3.2)变为

$$
\left\{ \begin{array}{l} s _ {\mathrm{p1}} = 0 \\ s _ {\mathrm{p2}} = - \zeta \omega_ {\mathrm{n}} + \omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \mathrm{j} \\ s _ {\mathrm{p3}} = - \zeta \omega_ {\mathrm{n}} - \omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \mathrm{j} \end{array} \right. \tag {5.3.3}
$$

其中， $s_{p1}$ 来自输入， $s_{p2}$ 和 $s_{p3}$ 则是系统传递函数的极点。将式(5.3.3)代入式(5.3.1)，并设三个待定系数分别为A、B和C，可得

$$
\begin{array}{l} X (s) = \frac {\omega_ {n} ^ {2}}{s \left(s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}\right)} = \frac {A}{\left(s - s _ {p 1}\right)} + \frac {B}{\left(s - s _ {p 2}\right)} + \frac {C}{\left(s - s _ {p 3}\right)} \\ = \frac {A (s - s _ {\mathrm{p} 2}) (s - s _ {\mathrm{p} 3}) + B (s - s _ {\mathrm{p} 1}) (s - s _ {\mathrm{p} 3}) + C (s - s _ {\mathrm{p} 1}) (s - s _ {\mathrm{p} 2})}{(s - s _ {\mathrm{p} 1}) (s - s _ {\mathrm{p} 2}) (s - s _ {\mathrm{p} 3})} \tag {5.3.4} \\ \end{array}
$$

比较等式两侧的分子,可得

$$\omega_ {\mathrm{n}} ^ {2} = A \left(s - s _ {\mathrm{p} 2}\right) \left(s - s _ {\mathrm{p} 3}\right) + B \left(s - s _ {\mathrm{p} 1}\right) \left(s - s _ {\mathrm{p} 3}\right) + C \left(s - s _ {\mathrm{p} 1}\right) \left(s - s _ {\mathrm{p} 2}\right) \tag {5.3.5}$$

利用分式分解法求 A、B 和 C：

令 $s=s_{pl}=0$ ，可得
