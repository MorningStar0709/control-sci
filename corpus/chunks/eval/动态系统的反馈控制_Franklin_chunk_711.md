# 9. 巴塞伐尔定理

巴塞伐尔的著名定理，用来计算一个信号的能量或两个信号之间的能量的关系。它告诉我们在时域或频域中都可以计算能量的大小。如果

$$\int_ {0} ^ {+ \infty} | y (t) | ^ {2} \mathrm{d} t < 1 \quad \text { and } \quad \int_ {0} ^ {+ \infty} | u (t) | ^ {2} \mathrm{d} t < 1 \tag {A.17}$$

(即 $y(t)$ 和 $u(t)$ 是平方可积的)，那么

$$\int_ {0} ^ {+ \infty} y (t) u (t) \mathrm{d} t = \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} Y (- \mathrm{j} \omega) U (\mathrm{j} \omega) \mathrm{d} \omega \tag {A.18}$$

巴塞伐尔定理的结果仅仅包含时间函数和一个积分改变量的变换：

$$
\begin{array}{l} \int_ {0} ^ {+ \infty} y (t) u (t) \mathrm{d} t = \int_ {0} ^ {+ \infty} y (t) \left[ \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} U (\mathrm{j} \omega) \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} \omega \right] \mathrm{d} t (A.19) \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} U (\mathrm{j} \omega) \left[ \int_ {0} ^ {+ \infty} y (t) \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} t \right] \mathrm{d} \omega (A.20) \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} U (\mathrm{j} \omega) Y (- \mathrm{j} \omega) \mathrm{d} \omega (A.21) \\ \end{array}
$$
