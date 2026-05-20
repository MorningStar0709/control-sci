# 例 7.5 建立状态变量形式的直流电动机模型

试求如图 2.33a 所示的直流电动机等价电路的状态空间方程。

解答。回顾第2章中运动方程[式(2.62)和式(2.63)]，即

$$J _ {\mathrm{m}} \ddot {\theta} _ {\mathrm{m}} + b \dot {\theta} _ {\mathrm{m}} = K _ {\mathrm{t}} i _ {\mathrm{a}}L _ {\mathrm{a}} \frac {\mathrm{d} i _ {\mathrm{a}}}{\mathrm{d} t} + R _ {\mathrm{a}} i _ {\mathrm{a}} = v _ {\mathrm{a}} - K _ {\mathrm{e}} \dot {\theta} _ {\mathrm{m}}$$

该三阶系统的状态矢量是 $X \stackrel{\text{def}}{=} \left[\theta_{\mathrm{m}} \quad \dot{\theta}_{\mathrm{m}} \quad i_{\mathrm{a}}\right]^{\mathrm{T}}$ ，由此推出标准矩阵分别为

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & - \frac {b}{J _ {\mathrm{m}}} & \frac {K _ {1}}{J _ {\mathrm{m}}} \\ 0 & - \frac {K _ {\mathrm{e}}}{L _ {\mathrm{a}}} & - \frac {R _ {\mathrm{a}}}{L _ {\mathrm{a}}} \end{array} \right]

\boldsymbol {B} = \left[ \begin{array}{l} 0 \\ 0 \\ \frac {1}{L _ {\mathrm{a}}} \end{array} \right]

\mathbf {C} = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right]
D = 0
$$

其中：输入 $u \stackrel{\operatorname{def}}{=} v_{a}$ 。

状态变量形式可以应用到任意阶的系统中。例 7.6 通过一个四阶系统阐明了这一点。
