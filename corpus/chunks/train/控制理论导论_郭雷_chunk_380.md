$$A = \frac {1}{4} \frac {\mathrm{d} ^ {2}}{\mathrm{d} x ^ {2}}, \quad \mathcal {D} (A) = \left\{f \in L ^ {1} (- \infty , \infty) \mid f ^ {\prime}, f ^ {\prime \prime} \in L ^ {1} (- \infty , \infty) \right\}.$$

例5.3.9 例5.3.5中 $C_0$ 半群的生成算子是

$$A x = \sum_ {k = 1} ^ {\infty} \lambda_ {k} (x, e _ {k}) e _ {k},\mathcal {D} (A) = \left\{x \in H \left| \sum_ {k = 1} ^ {\infty} | \lambda_ {k} (x, e _ {k}) | ^ {2} < \infty \right. \right\}.$$

例5.3.10 考虑人口演化过程。一种描述人口演化过程的连续模型是

$$
\left\{ \begin{array}{l} \frac {\partial p (r , t)}{\partial t} + \frac {\partial p (r , t)}{\partial r} + \mu (r) p (r, t) = 0, \\ p (0, t) = \int_ {0} ^ {m} b (r) p (r, t) \mathrm{d} r, \quad t > 0, \\ p (r, 0) = p _ {0} (r), \quad 0 \leqslant r \leqslant m, \end{array} \right. \tag {5.3.21}
$$

这里 $p(r, t)$ 表示一个封闭人口在年龄 $r$ 和时间 $t$ 时的年龄 - 密度分布， $\mu(r), b(r)$ 是相应的死亡率和生育模式， $p_0(r)$ 是初始密度分布，而 $m$ 是人口个体的最大存活年龄（见文献 [12]). 我们假定

(1) $\mu(r) \geqslant 0, \forall r \in [0, m]$ ; $\int_{0}^{r} \mu(s) \mathrm{d}s < \infty$ , $\forall r \in [0, m)$ , $\int_{0}^{m} \mu(s) \mathrm{d}s = \infty$ ;

(2) $b(r) \geqslant 0, \forall r \in [0, m], b(\cdot) \in C[0, m], \operatorname{supp} b = [r_1, r_2] \subset (0, m).$ （这里 $[r_1, r_2]$ 通常称为妇女的生育周期）.

我们在Banach空间 $L^1 (0,m)$ 中定义线性算子 $\pmb{A}$

$$A \varphi = - \varphi^ {\prime} (r) - \mu (r) \varphi (r),\mathcal {D} (A) = \left\{\varphi \in L ^ {1} (0, m) \mid \varphi^ {\prime} + \mu \varphi \in L ^ {1} (0, m), \varphi (0) = \int_ {0} ^ {m} b (s) \varphi (s) d s \right\}.$$

那么式 (5.3.21) 可以改写成 $L^1(0, m)$ 中的发展方程形式

$$\frac {\mathrm{d} p}{\mathrm{d} t} = A p, \quad p (0) = p _ {0}. \tag {5.3.22}$$

可以证明 $A$ 生成 $L^1 (0,m)$ 上一 $C_0$ 半群.

例 5.3.11 设 A 是 Hilbert 空间 H 中正定自伴算子. 我们考虑 H 中如下二阶发展方程:

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} ^ {2} y}{\mathrm{d} t ^ {2}} + \alpha \frac {\mathrm{d} y}{\mathrm{d} t} + A y (t) = 0, \\ y (0) = y _ {0}, \dot {y} (0) = y _ {1}, \end{array} \right. \tag {5.3.23}
$$

其中 $\alpha$ 为一非负常数. 令 $\frac{\mathrm{dy}}{\mathrm{dt}} = z$ , 则

$$\frac {\mathrm{d} z}{\mathrm{d} t} = - \alpha z - A y,$$

从而式 (5.3.23) 可以写成一阶发展方程形式

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} w}{\mathrm{d} t} = \mathcal {A} w, \\ w (0) = w _ {0} = [ y _ {0}, y _ {1} ] ^ {\mathbf {T}}, \end{array} \right. \tag {5.3.24}
$$

其中 $w = [y,z]^{\mathrm{T}}$ ，而

$$
\mathcal {A} \left[ \begin{array}{c} y \\ z \end{array} \right] = \left[ \begin{array}{c c} 0 & I \\ - A & - \alpha \end{array} \right] \left[ \begin{array}{c} y \\ z \end{array} \right].
$$
