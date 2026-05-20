# 7.9.2 增益选择

现在，来讨论在选择 $M$ 的三种方法中确定增益 $\overline{N}$ 的选取过程。若使用方法1，控制规律由式(7.188a)给出且有 $\hat{x}_{\mathrm{ss}} = x_{\mathrm{ss}}$ 。因此，可以使用式(7.99)中 $\overline{N} = Nu + KN_x$ 或用 $u = N_u r - K(\hat{x} - N_x r)$ ，这是最常用的选择。若用方法2，则得到的结果无意义；重新考虑对于误差控制， $\overline{N} = 0$ 。若使用方法3，选择 $\overline{N}$ 使得整个闭环直流增益为 $1^{\ominus}$ 。

则整个系统方程为

$$
\left[ \begin{array}{c} \dot {x} \\ \dot {\widetilde {x}} \end{array} \right] = \left[ \begin{array}{c c} A - B K & B K \\ 0 & A - L C \end{array} \right] \left[ \begin{array}{c} x \\ \widetilde {x} \end{array} \right] + \left[ \begin{array}{c} B \\ B - \overline {{M}} \end{array} \right] \overline {{N r}} \tag {7.200a}

y = \left[ \begin{array}{l l} C & 0 \end{array} \right] \left[ \begin{array}{l} x \\ \widetilde {x} \end{array} \right] \tag {7.200b}
$$

其中： $\overline{M}$ 的值是用式(7.191)或式(7.187)选择零点位置得到的。如果有下式成立，则闭环系统具有单位直流增益：

$$
- \left[ \begin{array}{l l} C & 0 \end{array} \right] \left[ \begin{array}{c c} A - B K & B K \\ 0 & A - L C \end{array} \right] ^ {- 1} \left[ \begin{array}{c} B \\ B - \overline {{M}} \end{array} \right] \overline {{N}} = 1 \tag {7.201}
$$

若从式(7.201)求解 $\overline{N}$ ，得到 $^{②}$

$$\overline {{{N}}} = - \frac {1}{C (A - B K) ^ {- 1} B [ 1 - K (A - L C) ^ {- 1} (B - \overline {{{M}}}) ]} \tag {7.202}$$

本节中的方法很容易推广到降阶估计器情况。
