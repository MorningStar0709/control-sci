$$
\left\{ \begin{array}{l} \mathcal {F} _ {0} \cap \mathcal {H} ^ {\perp} = \operatorname{span} \left\{\frac {\partial}{\partial z ^ {2}} \right\}, \\ \mathcal {F} _ {0} = \operatorname{span} \left\{\frac {\partial}{\partial z ^ {2}}, \frac {\partial}{\partial z ^ {1}} \right\}, \\ \mathcal {H} ^ {\perp} = \operatorname{span} \left\{\frac {\partial}{\partial z ^ {2}}, \frac {\partial}{\partial z ^ {4}} \right\}. \end{array} \right. \tag {8.2.18}
$$

定理 8.2.5(Kalman 分解) 对系统 (8.1.1), 设点 $x_0 \in M$ 为 $\mathcal{F}_0, \mathcal{F}_0 \cap \mathcal{H}^\perp, \mathcal{F}_0 \cup \mathcal{H}^\perp$ 的一个正则点, 则可找到 $x_0$ 的一个局部坐标卡 $(V, z)$ 使得系统 (8.1.1) 可局部表示为

$$
\left\{ \begin{array}{l} \dot {z} ^ {1} = f ^ {1} (z ^ {1}, z ^ {3}, u), \\ \dot {z} ^ {2} = f ^ {2} (z, u), \\ \dot {z} ^ {3} = f ^ {3} (z ^ {3}), \\ \dot {z} ^ {4} = f ^ {4} (z ^ {3}, z ^ {4}), \\ y = h (z ^ {1}, z ^ {3}), \end{array} \right. \tag {8.2.19}
$$

这里 $\mathcal{F}_0 = \mathrm{span}\left\{\frac{\partial}{\partial z^2},\frac{\partial}{\partial z^1}\right\} ,\mathcal{H}^\perp = \mathrm{span}\left\{\frac{\partial}{\partial z^2},\frac{\partial}{\partial z^4}\right\} .$

证明 将系统在式 (8.2.18) 规定的局部坐标卡上表示出来，根据引理 8.2.2 及定理 8.2.4, 式 (8.2.19) 是显见的.

将定理8.2.5用于仿射非线性系统，则得：

推论8.2.3(Kalman分解) 对系统(8.1.2)，设 $x_0 \in M$ 为 $\mathcal{F}_0, \mathcal{F}_0 \cap \mathcal{H}^\perp, \mathcal{F}_0 \cup \mathcal{H}^\perp$ 的正则点，于是可得到 $x_0$ 的一个局部坐标卡 $(V, z)$ 使得系统(8.1.2)可局部表示为

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {z} ^ {1} \\ \dot {z} ^ {2} \\ \dot {z} ^ {3} \\ \dot {z} ^ {4} \end{array} \right] = \left[ \begin{array}{c} f ^ {1} (z ^ {1}, z ^ {3}) \\ f ^ {2} (z) \\ f ^ {3} (z ^ {3}) \\ f ^ {4} (z ^ {3}, z ^ {4}) \end{array} \right] + \left[ \begin{array}{c} g ^ {1} (z ^ {1}, z ^ {3}) \\ g ^ {2} (z) \\ 0 \\ 0 \end{array} \right] u,} \\ y = h (z ^ {1}, z ^ {3}), \end{array} \right. \tag {8.2.20}
$$

这里 $\mathcal{F}_0 = \mathrm{span}\left\{\frac{\partial}{\partial z^2},\frac{\partial}{\partial z^1}\right\},\mathcal{H}^\perp = \mathrm{span}\left\{\frac{\partial}{\partial z^2},\frac{\partial}{\partial z^4}\right\}.$
