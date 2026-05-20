# 7.2 描述函数法

考虑一个由图7.1所示的反馈连接表示的单输入-单输出非线性系统，其中 $G(s)$ 是严格正则的有理传递函数， $\psi$ 是时不变、无记忆的非线性特性。假设外部输入 $r = 0$ ，研究周期解的存在性。周期解对于所有 $t$ 满足 $y(t + 2\pi /\omega) = y(t)$ ，其中 $\omega$ 是振荡频率。我们用一般方法来求周期解，即调和平衡法。该方法的思想是用傅里叶级数表示周期解，并找到一个频点 $\omega$ 及满足系统方程的傅里叶系数的集合。假设 $y(t)$ 是周期函数并设

$$y (t) = \sum_ {k = - \infty} ^ {\infty} a _ {k} \exp (j k \omega t)$$

是其傅里叶级数,其中 $a_{k}$ 是复系数 $^{①}$ 。 $a_{k}=\bar{a}_{-k},j=\sqrt{-1}$ 。由于 $\psi(\cdot)$ 是时不变非线性的， $\psi(y(t))$ 也是频率为 $\omega$ 的周期函数,且可表示为

$$\psi (y (t)) = \sum_ {k = - \infty} ^ {\infty} c _ {k} \exp (j k \omega t)$$

其中每个复系数 $c_{k}$ 是所有 $a_{i}$ 的函数。若 $y(t)$ 为反馈系统的一个解，则必须满足微分方程

$$d (p) y (t) + n (p) \psi (y (t)) = 0$$

其中， $p$ 是微分算子 $p(\cdot) = d(\cdot) / dt, n(s)$ 和 $d(s)$ 分别是 $G(s)$ 的分子多项式和分母多项式。因为

$$p \exp (j k \omega t) = \frac {d}{d t} \exp (j k \omega t) = j k \omega \exp (j k \omega t)$$

有 $d(p)\sum_{k = -\infty}^{\infty}a_k\exp (jk\omega t) = \sum_{k = -\infty}^{\infty}d(jk\omega)a_k\exp (jk\omega t)$

和 $n(p)\sum_{k = -\infty}^{\infty}c_k\exp (jk\omega t) = \sum_{k = -\infty}^{\infty}n(jk\omega)c_k\exp (jk\omega t)$

将这些表达式回代到微分方程,得到

$$\sum_ {k = - \infty} ^ {\infty} [ d (j k \omega) a _ {k} + n (j k \omega) c _ {k} ] \exp (j k \omega t) = 0$$

当所有整数 k 取不同值时, 利用函数 $\exp(jk\omega t)$ 的正交性, 求出傅里叶系数必须满足

$$G (j k \omega) c _ {k} + a _ {k} = 0 \tag {7.20}$$

因为 $G(jk\omega) = \bar{G}(-jk\omega), a_k = \bar{a}_{-k}$ 且 $c_k = \bar{c}_{-k}$ ，所以只需要考虑方程(7.20)在 $k \geqslant 0$ 时的情况。方程(7.20)是一个无限维方程，难以求解，因而需要找一个有限维的方程逼近方程(7.20)。注意，传递函数 $G(s)$ 是严格正则的，即当 $\omega$ 趋于无穷时 $G(j\omega)$ 趋于零。因此可以假设存在一个整数 $q > 0$ ，使得对于所有 $k > q, |G(jk\omega)|$ 足够小，可以用 0 代替 $G(jk\omega)$ 。该近似将方程(7.20)简化为一个有限维问题

$$G (j k \omega) \hat {c} _ {k} + \hat {a} _ {k} = 0, k = 0, 1, 2, \dots , q \tag {7.21}$$

其中傅里叶系数上方的符号强调方程(7.21)的解仅是方程(7.20)的近似解。实际上可以继续解方程(7.21)，但随着 $q$ 的增加，问题会变得越来越复杂，而且当 $q$ 较大时，方程(7.21)可能仍然难以求解。如果可以取 $q = 1$ ，则是最简单的情况。当然这要求传递函数 $G(s)$ 具有锐截止的“低通滤波”特性，这样才允许当 $k > 0$ 时将 $G(jk\omega)$ 近似为零。即使知道了 $G(s)$ ，但由于振荡频率 $\omega$ 未知，仍不能判断出近似程度。然而，经典的描述函数法应用了该近似，并当 $k > 1$ 时设定 $\hat{a}_k = 0$ ，使问题简化为求解如下两个方程：

$$G (0) \hat {c} _ {0} (\hat {a} _ {0}, \hat {a} _ {1}) + \hat {a} _ {0} = 0 \tag {7.22}G (j \omega) \hat {c} _ {1} (\hat {a} _ {0}, \hat {a} _ {1}) + \hat {a} _ {1} = 0 \tag {7.23}$$
