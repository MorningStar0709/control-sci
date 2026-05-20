实际上，奈奎斯特图中通常的“-1”点都被临界圆所替代。这一结果称为圆判据或圆定理，且这一结果来自桑德伯格(Sandberg)(1964)和赞默斯(Zames)(1966)。注意，这些条件都是充分而非必要的，因为传递函数的图像与临界圆相交并不能证明不稳定。临界圆的圆心位于

$$c = \frac {1}{2} \left[ - \frac {1}{k _ {1}} - \frac {1}{k _ {2}} \right] = - \frac {k _ {1} + k _ {2}}{2 k _ {1} k _ {2}}$$

半径为

$$\frac {k _ {1} - k _ {2}}{2 k _ {1} k _ {2}}$$

如果 $k_{1}=0$ ，那么临界圆将退化为由 $\mathrm{Re}\{G\}\geqslant-1/k_{2}$ 定义的半平面。

圆判据与描述函数是相关的。实际上，对于一个位于扇形区且其描述函数是实函数的时不变奇非线性项的情况，描述函数满足

$$k _ {1} \leqslant K _ {\mathrm{eq}} (a) \leqslant k _ {2}, \text {对所有的} a \tag {9.110}$$

从而，

$$- \frac {1}{k _ {1}} \leqslant - \frac {1}{K _ {\mathrm{eq}} (a)} \leqslant - \frac {1}{k _ {2}} \tag {9.111}$$

且描述函数的负倒数的图像将位于临界圆内。这可以由如下的上界和下界看出。

$$
\begin{array}{l} K _ {\mathrm{eq}} (\bar {a}) = \frac {2}{\pi a} \int_ {0} ^ {\pi} f (a \sin (\omega t)) \sin (\omega t) \mathrm{d} (\omega t) \\ \geqslant \frac {2 k _ {1}}{\pi} \int_ {0} ^ {\pi} \sin^ {2} (\omega t) \mathrm{d} (\omega t) = k _ {1} (9.112) \\ K _ {\mathrm{eq}} (a) = \frac {2}{\pi a} \int_ {0} ^ {\pi} f (a \sin \omega t) \sin (\omega t) \mathrm{d} (\omega t) \\ \leqslant \frac {2 k _ {2}}{\pi} \int_ {0} ^ {\pi} \sin^ {2} (\omega t) \mathrm{d} (\omega t) = k _ {2} (9.113) \\ \end{array}
$$

等效增益分析法和描述函数法产生同样的结果。如果我们采取描述函数的增益分析法，则可以预测极限环的幅值。这两种等效的增益分析法均可以用于判定稳定性，但正如我们所看到的，圆判据可用于时变非线性系统。
