# 非齐次发展方程

设 $X$ 是Banach空间， $A$ 是 $X$ 上 $C_0$ 半群 $T(t)$ 的生成算子。现在我们考虑如下初值问题(Cauchy问题)：

$$
\left\{ \begin{array}{l l} \frac {\mathrm{d} x (t)}{\mathrm{d} t} = A x (t) + f (t), & 0 <   t \leqslant t _ {1}, \\ x (0) = x _ {0}, \end{array} \right. \tag {5.3.53}
$$

其中 $x_0 \in \mathcal{D}(A), f: [0, t_1] \to X$ . 我们说 $x(t)$ 是方程 (5.3.53) 的 (强) 解，是指 $x(\cdot) \in C^1([0, t_1]; X), x(t) \in \mathcal{D}(A), \forall t \in [0, t_1]$ ，并且满足方程 (5.3.53).

当 $f = 0$ 时，相应的齐次方程

$$
\left\{ \begin{array}{l l} \frac {\mathrm{d} x (t)}{\mathrm{d} t} = A x (t), & 0 <   t \leqslant t _ {1}, \\ x (0) = x _ {0} \in \mathcal {D} (A) \end{array} \right. \tag {5.3.54}
$$

有唯一解 $x(t) = T(t)x_0$ 。因此，如果方程 (5.3.53) 可解，则其解必是唯一的。

引理 5.3.10 设 A 是 Banach 空间 X 上的闭线性算子， $f \in C([a, b]; X)$ ， $\mathcal{R}(f) \subset \mathcal{D}(A)$ ，其中 $\mathcal{R}(f)$ 表示 f 的值域，并且 $Af \in C([a, b]; X)$ 。那么

$$\int_ {a} ^ {b} f (t) \mathrm{d} t \in \mathcal {D} (A), \quad A \int_ {a} ^ {b} f (t) \mathrm{d} t = \int_ {a} ^ {b} A f (t) \mathrm{d} t.$$

证明 留作练习.

定理5.3.22 设 $A$ 是Banach空间 $X$ 上 $C_0$ 半群的生成算子，并且 $x_0 \in \mathcal{D}(A)$ . 假定 $f: [0, t_1] \to X$ 满足下列两条件之一：

(1) $f \in C([0, t_1]; X), \mathcal{R}(f) \subset \mathcal{D}(A)$ 并且 $Af \in C([0, t_1]; X)$ ;   
(2) $f \in C^{1}([0, t_{1}]; X)$ ,

那么方程 (5.3.53) 有唯一解 $x(t)$ , 表示成

$$x (t) = T (t) x _ {0} + \int_ {0} ^ {t} T (t - s) f (s) \mathrm{d} s, \quad 0 \leqslant t \leqslant t _ {1}. \tag {5.3.55}$$

证明 只需证明存在性．形式上，如果 $x(t)$ 是方程(5.3.53)的解，则

$$\frac {\mathrm{d}}{\mathrm{d} s} [ T (t - s) x (s) ] = T (t - s) f (s).$$

于从 0 到 t 相对于 s 积分便得到式 (5.3.55). 令

$$v (t) = \int_ {0} ^ {t} T (t - s) f (s) \mathrm{d} s,$$

容易看出， $x(t) = T(t)x_0 + v(t)$ 是方程(5.3.53）的解当且仅当

$$\frac {\mathrm{d} v (t)}{\mathrm{d} t} = A v (t) + f (t). \tag {5.3.56}$$

首先设 (1) 成立，那么依据引理 5.3.10, $v(t) \in \mathcal{D}(A)$ 并且

$$A v (t) = \int_ {0} ^ {t} T (t - s) A f (s) \mathrm{d} s.$$

此外， $v\in C^{1}([0,t_{1}];X)$ 并且

$$
\begin{array}{l} \frac {\mathrm{d} v (t)}{\mathrm{d} t} = T (0) f (t) + \int_ {0} ^ {t} \frac {\partial}{\partial t} T (t - s) f (s) \mathrm{d} s \\ = f (t) + \int_ {0} ^ {t} T (t - s) A f (s) d s = f (t) + A v (t), \\ \end{array}
$$

即式 (5.3.56) 成立.

现在设 (2) 成立. 我们知道当 $y \in X$ 时,

$$\int_ {0} ^ {t} T (s) y \mathrm{d} s \in \mathcal {D} (A), \quad A \int_ {0} ^ {t} T (s) y \mathrm{d} s = T (t) y - y. \tag {5.3.57}$$

于是从引理5.3.10得到
