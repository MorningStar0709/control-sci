$$
\begin{array}{l} v (t) = \int_ {0} ^ {t} T (t - s) \left[ f (0) + \int_ {0} ^ {s} f ^ {\prime} (\tau) \mathrm{d} \tau \right] \mathrm{d} s \\ = \int_ {0} ^ {t} T (s) f (0) d s + \int_ {0} ^ {t} \int_ {\tau} ^ {t} T (t - s) f ^ {\prime} (\tau) d s d \tau \\ = \int_ {0} ^ {t} T (s) f (0) \mathrm{d} s + \int_ {0} ^ {t} \int_ {0} ^ {t - \tau} T (\tau) f ^ {\prime} (\tau) \mathrm{d} r \mathrm{d} \tau \in \mathcal {D} (A). \tag {5.3.58} \\ \end{array}
$$

此外， $v\in C^{1}([0,t_{1}];X)$ 并且

$$
\begin{array}{l} \frac {\mathrm{d} v (t)}{\mathrm{d} t} = T (t) f (0) + \int_ {0} ^ {t} T (s) f ^ {\prime} (t - s) \mathrm{d} s \\ = T (t) f (0) + \int_ {0} ^ {t} T (t - s) f ^ {\prime} (s) \mathrm{d} s, \tag {5.3.59} \\ \end{array}
$$

而从式 (5.3.57) 和式 (5.3.58) 有

$$A v (t) = T (t) f (0) - f (0) + \int_ {0} ^ {t} [ T (t - s) f ^ {\prime} (s) - f ^ {\prime} (s) ] \mathrm{d} s. \tag {5.3.60}$$

因此从式 (5.3.59) 和式 (5.3.60) 推出式 (5.3.56). 证毕.

在实际应用中，定理5.3.22的条件似乎有些强，因为一般说来，条件 $f \in C^1$ 难于满足。如果我们仅仅要求解在 $(0, t_1)$ 上几乎处处满足方程(5.3.53)，则对 $f$ 的限制可以减弱。然而对于许多应用来说，温和解或弱解的概念将更方便。

定义5.3.7 设 $X$ 是一Banach空间．一向量值函数 $x(\cdot):[0,t_1]\to X$ 称为方程(5.3.53)的弱解，是指 $x(\cdot)\in C([0,t_1];X)$ ，并且对于任意 $x^{*}\in \mathcal{D}(A^{*})$ 和 $t\in [0,t_1]$ 满足

$$\langle x (t), x ^ {*} \rangle = \left\langle x _ {0}, x ^ {*} \right\rangle + \int_ {0} ^ {t} \left\langle x (s), A ^ {*} x ^ {*} \right\rangle \mathrm{d} s + \int_ {0} ^ {t} \left\langle f (s), x ^ {*} \right\rangle \mathrm{d} s. \tag {5.3.61}$$

由

$$x (t) = T ^ {\prime} (t) x _ {0} + \int_ {0} ^ {t} T (t - s) f (s) \mathrm{d} s, \quad 0 \leqslant t \leqslant t _ {1} \tag {5.3.62}$$

给出的函数 $x(t)$ 叫做方程 (5.3.53) 在 $[0, t_1]$ 上积分解或温和解，是指式 (5.3.62) 右端的积分是连续的.

这里我们已经使用了抽象可积函数 Banach 空间 $L^p(0, t_1; X), p \geqslant 1$ . $L^p(0, t_1; X)$ 中赋以范数

$$\| f \| _ {p} = \left(\int_ {0} ^ {t _ {1}} \| f (s) \| ^ {p} \mathrm{d} s\right) ^ {1 / p}, \quad f \in L ^ {p} (0, t _ {1}; X).$$

(关于空间 $L^p (0,t_1;X)$ ，见文献[8],[13].)

引理5.3.11 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群，并设 $f \in L^p(0, t_1; X)$ ， $p \geqslant 1$ 。那么由式(5.3.62)给出的函数 $x(t)$ 在 $[0, t_1]$ 上是连续的。

证明 不失一般性，我们可以取 $x_0 = 0, p = 1$ 。设 $\delta > 0$ ，则

$$
\begin{array}{l} \| x (t + \delta) - x (t) \| \leqslant \int_ {0} ^ {t} \| T (t - s) \| \| T (\delta) f (s) - f (s) \| d s \\ + \int_ {t} ^ {t + \delta} \| T (t + \delta - s) \| \| f (s) \| d s. \\ \end{array}
$$

当 $\delta \to 0$ 时，上式右端第二项积分显然收敛于0，而根据实变函数中的Lebesgue控制收敛定理，第一项积分也收敛于0.类似地，对于 $\delta > 0$ ，我们有
