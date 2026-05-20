$$J = \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {C X} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left(\boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {X} + \boldsymbol {u} ^ {\mathrm{T}} \boldsymbol {R} \boldsymbol {u}\right) \mathrm{d} t \tag {12-18}$$

式中

$$
\boldsymbol {C} = \left[ \begin{array}{l l} c _ {1} & 0 \\ 0 & c _ {2} \end{array} \right], \boldsymbol {Q} = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] \tag {12-19}
$$

即

$$J = \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {C X} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {0} ^ {t _ {\mathrm{f}}} \boldsymbol {R u} ^ {2} \mathrm{d} t \tag {12-20}$$

给定初始条件 $X(t_{0})$ ，应用最优控制理论，可以求出使 J 为最小的 u。

由于系统是线性的,指标函数是二次型的,因此,求最优控制规律就可以认为是一个求解线性二次型的过程。

对于线性二次型问题,可采用变分法、极小值原理、动态规划或其他方法求得最优控制

$$\boldsymbol {u} ^ {*} (t) = - \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K X} \tag {12-21}$$

式中，K 满足下列黎卡提矩阵微分方程

$$\dot {\boldsymbol {K}} = - \boldsymbol {K} \boldsymbol {A} - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {K} + \boldsymbol {K B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} - \boldsymbol {Q} \tag {12-22}$$

$\pmb{K}$ 的终端条件为

$$\boldsymbol {K} \left(t _ {\mathrm{f}}\right) = \boldsymbol {C} \tag {12-23}$$

因此求解线性二次型问题的关键是求解黎卡提矩阵微分方程。
