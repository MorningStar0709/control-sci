$$I _ {3} = \operatorname{span} \left\{\left[ 0, 0, 1, 0 \right] ^ {\mathrm{T}}, \left[ 0, 1, 0, - 1 \right] ^ {\mathrm{T}} \right\}.$$

容易证明 $I_{1}$ 与 $I_{3}$ 线性无关. 选择

$$X _ {1} = [ 1, 0, \mathrm{e} ^ {z _ {1}}, 0 ] ^ {\mathrm{T}}, X _ {2} = [ 0, 1, 0, 1 ] ^ {\mathrm{T}},X _ {2} = [ 0, 1, 0, - 1 ] ^ {\mathrm{T}}, X _ {4} = [ 0, 0, 1, 0 ] ^ {\mathrm{T}},$$

则下述微分同胚给出平整坐标

$$F (x _ {1}, x _ {2}, x _ {3}, x _ {4}) = \phi_ {x _ {1}} ^ {X _ {1}} \phi_ {x _ {2}} ^ {X _ {2}} \phi_ {x _ {3}} ^ {X _ {3}} \phi_ {x _ {4}} ^ {X _ {4}} (0).$$

于是 $F(x)$ 可表示为

$$
\left\{ \begin{array}{l} z _ {1} = x _ {1}, \\ z _ {2} = x _ {2} + x _ {3}, \\ z _ {3} = e ^ {x _ {1}} - 1 + x _ {4}, \\ z _ {4} = x _ {2} - x _ {3}. \end{array} \right.
$$

利用新的坐标卡 $x$ ，系统成为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = \sin (2 x _ {2} + u _ {2}), \\ \dot {x} _ {2} = \frac {1}{2} u _ {1} u _ {2} \mathrm{e} ^ {x _ {1}}, \\ \dot {x} _ {3} = \frac {1}{2} x _ {4}, \\ \dot {x} _ {4} = u _ {3} (2 x _ {3} + 1). \end{array} \right.
$$

显然系统解耦为两个子系统，第一个子系统由 $x_{1}$ 和 $x_{2}$ 组成，第二个子系统由 $x_{3}$ 和 $x_{4}$ 组成.

由于系统在原点满足强能控条件，这里没有作为 $x^0$ 的分量.

现在考虑仿射非线性系统

$$\dot {x} = f (x) + \sum_ {i = 1} ^ {m} g _ {i} (x) u _ {i}, \quad x \in M \tag {8.4.55}$$

我们有

$$\mathcal {F} = \{f, g _ {1}, \dots , g _ {m} \} _ {L A},\mathcal {F} _ {0} = \left\{\mathrm{ad} _ {f} ^ {i} g _ {j} \mid j = 1, \dots , m, i \geqslant 0 \right\} _ {L A},F _ {i} = \left\{g _ {j} ^ {i} \mid j = 1, \dots , m _ {i} \right\}, \quad i = 1, \dots , k.$$

于是

$$I _ {i} = \left\{\mathrm{ad} _ {f} ^ {s} g _ {j} ^ {i} \mid g _ {j} ^ {i} \in F _ {i}, s \geqslant 0 \right\} _ {L A}, \quad i = 1, \dots , k.$$

以上对一般非线性系统 (8.4.42) 的解耦结论当然对仿射非线性系统也适用.

最后，我们讨论仿射非线性系统(8.4.55)的反馈块解耦问题。为此我们需要讨论对若干分布均合适的反馈。

定义 8.4.8 设 $\Delta_{1},\cdots,\Delta_{k}$ 为一组分布. $\Delta_{i}, i=1,\cdots,k,$ 称为局部同时 $(f,g)$ 不变的，如果存在一个局部正则反馈控制 $(\alpha(x),\beta(x))$ ，使得

$$
\left\{ \begin{array}{l} {[ f (x) + g (x) \alpha (x), \Delta_ {i} (x) ] \subset \Delta_ {i} (x),} \\ {[ g (x) \beta (x), \Delta_ {i} (x) ] \subset \Delta_ {i} (x), \quad i = 1, \dots , k.} \end{array} \right. \tag {8.4.56}
$$

为方便，在本节余下部分我们假设系统(8.4.55)满足强能控秩条件，即

$$\operatorname{rank} \left(\mathcal {F} _ {0}\right) = \operatorname{rank} \left(\left\{\mathrm{ad} _ {f} ^ {\bullet} g \mid s \geqslant 0 \right\} _ {L A}\right) = n. \tag {8.4.57}$$

如果式 (8.4.57) 满足，由于 $\operatorname{rank}(\mathcal{F}_0) = \operatorname{const}$ ，则可用标准分解将系统 (8.4.55) 变为

$$
\left\{ \begin{array}{l} \dot {x} ^ {1} = f ^ {1} (x ^ {1}), \\ \dot {x} ^ {2} = f ^ {2} (x) + \sum_ {i = 1} ^ {m} g _ {i} u _ {i}. \end{array} \right.
$$
