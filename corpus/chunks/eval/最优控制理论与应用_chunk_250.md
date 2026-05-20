# 12.2 用 MATLAB 解线性二次型最优控制问题

一般情况的线性二次问题可表示如下：

设线性时变系统的方程为：

$$
\begin{array}{l} \dot {\boldsymbol {X}} (t) = \boldsymbol {A} (t) \boldsymbol {X} (t) + \boldsymbol {B} (t) \boldsymbol {U} (t) \\ \boldsymbol {Y} (t) = \boldsymbol {C} (t) \boldsymbol {X} (t) \\ \end{array}
$$

其中， $X(t)$ 为 n 维状态向量， $U(t)$ 为 m 维控制向量， $Y(t)$ 为 l 维输出向量。寻找最优控制，使下面的性能指标最小：

$$J (\boldsymbol {u}) = \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P e} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left[ \boldsymbol {e} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {e} (t) + \boldsymbol {U} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {U} (t) \right] \mathrm{d} t$$

其中， $\pmb{P}$ 是 $l \times l$ 对称半正定常数阵， $\pmb{Q}(t)$ 是 $l \times l$ 对称半正定阵， $\pmb{R}(t)$ 是 $m \times m$ 对称正定阵。

用最小值原理求解上述问题,可以把上述问题归结为求解如下黎卡提(Riccati)矩阵微分方程:

$$
\begin{array}{l} \dot {\boldsymbol {K}} (t) = - \boldsymbol {K} (t) \boldsymbol {A} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) + \\ \boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) - \boldsymbol {Q} (t) \\ \end{array}
$$

可以看出,上述的黎卡提矩阵微分方程求解起来非常困难,所以往往求出其稳态解。例如目标函数中指定终止时间可以设置成 $t_{f}\rightarrow\infty$ ,这样可以保证系统状态渐进的趋近于零值,这样可以得出矩阵 $K(t)$ 趋近于常值矩阵,且 $\dot{K}(t)=0$ ,这样上述黎卡提矩阵微分方程可以简化成为

$$- \boldsymbol {K} (t) \boldsymbol {A} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) + \boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) - \boldsymbol {Q} (t) = \boldsymbol {0}$$

这个方程称为代数黎卡提方程。代数黎卡提方程的求解非常简单，并且其求解只涉及到矩阵运算，所以非常适合使用 MATLAB 来求解。

方法一：

求解代数黎卡提方程的算法有很多,下面介绍一种简单的迭代算法来解该方程,令 $\Phi_{0}=0$ , 则可以写出下面的迭代公式
