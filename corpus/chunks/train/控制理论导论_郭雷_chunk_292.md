例 4.1.11 $\Omega = [0,1]$ , F 由 $[0,1]$ 上的 Lebesgue 集构成, P 为 $[0,1]$ 的 Lebesgue 测度. 设 $F_{1}$ 由 $\left[0,\frac{1}{3}\right)$ , $\left[\frac{1}{3},1\right]$ 生成. $\xi = \omega$ , 即 $\xi$ 为定义在 $[0,1]$ 上的倾角为 $45^{\circ}$ 的线性函数.

我们来验证

$$E _ {\cdot} ^ {\mathcal {F} _ {1}} \xi = \frac {1}{6} I _ {[ 0, \frac {1}{3})} + \frac {2}{3} I _ {[ \frac {1}{3}, 1 ]}.$$

首先对 $\mathcal{F}_1$ 中的任一集 $A$ , 例如 $A = \left[0, \frac{1}{3}\right)$ ,

$$\int_ {A} \xi \mathrm{d} P = \int_ {0} ^ {\frac {1}{3}} \omega \mathrm{d} \omega = \frac {1}{1 8}, \quad \int_ {A} E ^ {\mathcal {F} _ {1}} \xi \mathrm{d} P = \int_ {0} ^ {\frac {1}{3}} \frac {1}{6} \mathrm{d} \omega = \frac {1}{1 8},$$

两者确实相等，当 $A$ 取 $\mathcal{F}_1$ 中的其他集合时也同样验证。再则， $\frac{1}{6} I_{[0, \frac{1}{3}]} + \frac{2}{3} I_{[\frac{1}{3}, 1)}$ 确实对 $\mathcal{F}_1$ 可测。由唯一性知，它就是 $E^{\mathcal{F}_1}\xi$ 。

同样，

$$P ^ {\mathcal {F} _ {1}} (A) = 3 \int_ {A \cap [ 0, \frac {1}{3} ]} \mathrm{d} \lambda I _ {[ 0, \frac {1}{3} ]} + \frac {3}{2} \int_ {A \cap [ \frac {1}{3}, 1 ]} \mathrm{d} \lambda I _ {[ \frac {1}{3}, 1 ]}.$$

条件期望可由 $\xi$ 对条件概率积分得来

$$\int \xi \mathrm{d} P ^ {\mathcal {F} _ {1}} = 3 \int_ {0} ^ {\frac {1}{3}} \omega \mathrm{d} \omega I _ {[ 0, \frac {1}{3} ]} + \frac {3}{2} \int_ {\frac {1}{3}} ^ {1} \omega \mathrm{d} \omega I _ {[ \frac {1}{3}, 1 ]} = \frac {1}{6} I _ {[ 0, \frac {1}{3} ]} + \frac {2}{3} I _ {[ \frac {1}{3}, 1 ]} = E ^ {\mathcal {F} _ {1}} \xi .$$

例 4.1.12 设 $F_{1} \subset F, F_{1}$ 由 $\{A_{1}, A_{2}, \cdots, \}$ 生成，这里 $A_{i} \cap A_{j} = \phi, \forall i, j, PA_{i} > 0, \forall i,$ 那么，

$$P ^ {\mathcal {F} _ {1}} (B) = \sum_ {i = 1} ^ {\infty} P (B | A _ {i}) I _ {A _ {i}} = \sum_ {i = 1} ^ {\infty} \frac {P (B \cap A _ {i})}{P (A _ {i})} I _ {A _ {i}},E ^ {\mathcal {F} _ {1}} \xi = \sum_ {i = 1} ^ {\infty} \frac {E (\xi I _ {A _ {i}})}{P (A _ {i})} I _ {A _ {i}}.$$

上述两式右端显然对 $\mathcal{F}_1$ 可测，并且很容易验证 (4.1.23). 根据条件期望的唯一性，便知它们正分别是 $P^{\mathcal{F}_1}(B)$ 及 $E^{\mathcal{F}_1}\xi$ .

上面定义了对子 $\sigma$ -代数 $\mathcal{F}_1$ 取条件期望。这个概念可推广到对一个随机变量取条件期望。设 $\eta$ 为随机变量。用 $\mathcal{F}^{\eta}$ 表示包含一切形如 $\{\omega : \eta(\omega) \in B, B$ 为任一Borel集}集合的最小 $\sigma$ -代数。那么 $E(\xi|\mathcal{F}^{\eta})$ 称在 $\eta$ 条件下 $\xi$ 的条件期望，有时也写成 $E^{\eta}\xi$ 。

注4.1.2 $E\xi$ 是一个实数，但条件期望 $E(\xi |\mathcal{F}_1)$ 是一个随机变量.

下面列举条件期望的性质. 设下面涉及的期望都有意义, 即不出现 “ $+\infty - \infty$ ” 的情形.

(1) 设 $\xi$ 和 $\eta$ 为随机变量， $a$ 和 $b$ 为常数，那么

$$E ((a \xi + b \eta) | \mathcal {F} _ {1}) = a E (\xi | \mathcal {F} _ {1}) + b E (\eta | \mathcal {F} _ {1}):$$
