$$\alpha_ {1} < \alpha_ {2} < \dots < \alpha_ {p}.$$

且设 $\alpha_0 = ((\alpha_1 + \beta_1)W_2 / W_1) / (1 + W_2 / W_1)$ , $\beta_0 = (\alpha_1 + \beta_1) / (1 + W_2 / W_1)$ , $\alpha_{p+1} = \alpha_p + 1$ , $\beta_{p+1} = -\infty$ , 而 $j_0$ 满足

$$\beta_ {j _ {0} + 1} / \alpha_ {j _ {0} + 1} < W _ {1} / W _ {2} \leqslant \beta_ {j _ {0}} / \alpha_ {j _ {0}}. \tag {11.8.13}$$

证明 从几何观点看， $g(M)$ 的分子为 p 条线段形成的折线，斜率 $\alpha_{j}$ 逐段增大；由 $\alpha_{j+1} > \alpha_{j}$ ，及取 $\max_{1 \leqslant j \leqslant p}$ ，易知 $\beta_{j+1} > \beta_{j}, j \leqslant j \leqslant p$ . 于是

$$\beta_ {j + 1} / \alpha_ {j + 1} < \beta_ {j} / \alpha_ {j}. 1 \leqslant j < p.$$

由定理的假设易知

$$\beta_ {0} / \alpha_ {0} = W _ {1} / W _ {2}, \beta_ {p + 1} / \alpha_ {p + 1} = - \infty .$$

于是由上两式总存在 $j_0$ 满足式 (11.8.13). 显然, 式 (11.8.12) 中每条线段与分母形成函数为双曲线形式

$$\frac {(\alpha_ {j} M + \beta_ {j})}{W _ {2} M + W _ {1}} = \frac {\alpha_ {j}}{W _ {2}} \left\{1 + \frac {\frac {\beta_ {j}}{\alpha_ {j}} - \frac {W _ {1}}{W _ {2}}}{M + \frac {W _ {1}}{W _ {2}}} \right\}. \tag {11.8.14}$$

作变量代换 $x = M + W_{1} / W_{2}$ 后，由式(11.8.13)易知双曲线 $(\beta_{j} / \alpha_{j} - W_{1} / W_{2}) / x$ 在 $j \leqslant j_{0}$ 时为单调减函数，在 $j > j_{0}$ 时为单调增函数（注意 $x$ 总大于0，双曲线仅取其中一支），而式(11.8.14)仅把上述曲线加1后乘 $\alpha_{j} / W_{2}$ 而已，不改变其单调增、减性质。因此 $g(M)$ 的最小值在 $j = j_{0}$ 与 $j_{0} + 1$ 这两条双曲线的交点上达到，即 $M$ 为以下方程的解：

$$\alpha_ {j _ {0}} M + \beta_ {j _ {0}} = \alpha_ {j _ {0} + 1} M + \beta_ {j _ {0} + 1}.$$

当解取非整数值时，取最接近它的两个整数，比较相应的 $g(M)$ 的大小，取小的那个对应的 $M$ 作为解，称为这解的整量化.

以上考虑了 $n = 2$ 时的最优调度。对于一般 $n$ ，有以下定理：

定理11.8.9 当 $\sum_{l=1}^{i-1} M_l < j \leqslant \sum_{l=1}^{i} M_l$ 时，各 $P_r(j)$ 相同，记为 $t_r(i)$ ，它表示第 $i$ 种工件在 $m_r$ 上加工所需时间；各 $A(j)$ 也相同，记为

$$
\pmb {A} _ {i} = \left[ \begin{array}{c c c c c} {{t _ {1} (i)}} & {{0}} & {{- \infty}} \\ {{t _ {1 2} (i)}} & {{t _ {2} (i)}} & {{0}} \\ {{\vdots}} & {{\vdots}} & {{\ddots}} & {{\ddots}} \\ {{t _ {1 (m - 1)} (i)}} & {{t _ {2 (m - 1)} (i)}} & {{\dots}} & {{t _ {m - 1} (i)}} & {{0}} \\ {{t _ {1 m} (i)}} & {{t _ {2 m} (i)}} & {{\dots}} & {} & {{t _ {m} (i)}} \end{array} \right], \qquad \text {这里} \quad t _ {r s} (i) = \prod_ {l = r} ^ {s} t _ {l} (i).
$$

类似于定义11.8.2可定义 $A_{i}$ 的对角线元素的一串极大值．于是 $(A_{i}^{M_{i}})^{\mathrm{T}}$ 的元素公式为

$$
a _ {r s} (M _ {i}) = \left\{ \begin{array}{l l} {- \infty , \qquad \text {若} r > s, M _ {i} <   r - s,} \\ { \sum_ {u = 1} ^ {P} t _ {r - j _ {u}. s} (i) \widehat {t _ {u}} (i) ^ {M _ {i} - 1 - j _ {u}} \oplus \sum_ {v = 2} ^ {Q} t _ {r, s + j _ {v} ^ {\prime}} (i) \widetilde {t _ {v}} (i) ^ {M _ {i} - 1 - j _ {v} ^ {\prime}},} \end{array} \right.
$$
