正如图 10.31 所示。根据这些条件，求得平衡(见第 9 章)方程为

$$0 = X _ {0} - m g _ {0} \sin \theta_ {0} + \kappa T \cos \theta_ {0}0 = Y _ {0}0 = Z _ {0} + m g _ {0} \cos \theta_ {0} - \kappa T \sin \theta_ {0}0 = L _ {0}0 = M _ {0}0 = N _ {0} \tag {10.20}$$

根据假设(布顿森，1994年)

$$\left(v ^ {2}, w ^ {2}\right) \ll u ^ {2}\left(\varphi^ {2}, \theta^ {2}\right) < < 1\left(p ^ {2}, q ^ {2}, r ^ {2}\right) \ll \frac {u ^ {2}}{b ^ {2}} \tag {10.21}$$

![](image/7bdfb70047acc323c5b4a3398ebe454c13d6107cdea8e60b46d65ab7a793caff.jpg)  
图 10.31 稳态飞行条件

其中：b 代表翼展。方程组式(10.16)和式(10.17)中许多非线性项都可以被忽略。将式(10.20)代入非线性运动方程中，能够得到一组在定速、垂直、水平飞行状态下描述微小偏差的线性扰动方程。那么，运动方程就可以分成互不相关的两部分：纵向运动方程和横向运动方程。

对于线性化的纵向运动，其结果为

$$
\left[ \begin{array}{l} \dot {u} \\ \dot {w} \\ \dot {q} \\ \dot {\theta} \end{array} \right] = \left[ \begin{array}{c c c c} X _ {u} & X _ {w} & - W _ {0} & - g _ {0} \cos \theta_ {0} \\ Z _ {u} & Z _ {w} & U _ {0} & - g _ {0} \sin \theta_ {0} \\ M _ {u} & M _ {w} & M _ {q} & 0 \\ 0 & 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} u \\ w \\ q \\ \theta \end{array} \right] + \left[ \begin{array}{l} X _ {\delta_ {e}} \\ Z _ {\delta_ {e}} \\ M _ {\delta_ {e}} \\ 0 \end{array} \right] \delta_ {e} \tag {10.22}
$$

其中：u 为飞行器 x 轴方向的前向速度摄动（见图 10.30）；w 为在 z 轴方向上的速度扰动（也与攻角方向的扰动成正比，即 $\alpha=\frac{w}{U_{0}}$ ）；q 为 y 轴正向的角速度或俯仰速度； $\theta$ 为来自参考值 $\theta_{0}$ 的俯仰角扰动； $X_{u,w,\delta_{e}}$ 为 x 轴方向上的空气动力对摄动量 u、w 和 $\delta_{e}$ 的偏微分 $^{\ominus}$ ； $Z_{u,w,\delta_{e}}$ 为 z 轴方向上的空气动力对摄动量 u、w 和 $\delta_{e}$ 的偏微分； $M_{u,w,q,\delta_{e}}$ 为空气动力（俯仰）力矩对摄动量 u、w、q 和 $\delta_{e}$ 的偏微分； $\delta_{e}$ 为俯仰控制可移动尾部或“升降舵”的角。

方程中的 $W_{0q}$ ， $U_{0q}$ 项是由机体固定（旋转）参考机架的角速度产生的，并且可直接从式（10.16）左侧获得。

为了确定高度的变化，我们需要在纵向运动方程中增加如下等式：

$$\dot {h} = V _ {\mathrm{ref}} \sin \theta - w \cos \theta \tag {10.23}$$

该等式将会衍生出一个线性化的高度方程：

$$\dot {h} = V _ {\mathrm{ref}} \theta - w \tag {10.24}$$

将其增加到等式(10.22)中，可以得到一个增广的运动方程。

对于线性化的横向运动，结果如下：
