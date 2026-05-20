证明 如果 $\lambda \in \sigma_p(A)$ , 则存在 $x_0 \in \mathcal{D}(A)$ 使得 $x_0 \neq 0$ 和 $Ax_0 = \lambda x_0$ . 从 (5.3.29), 我们得到 $T(t)x_0 = \mathrm{e}^{\lambda t} x_0$ , 因此 $\mathrm{e}^{\lambda t} \in \sigma_p(T(t))$ , 这就证明了第一个论断. 现在假定 $\mathrm{e}^{\lambda t} \in \sigma_p(T(t))$ , 并设 $x_0 \neq 0$ 使得 $T(t)x_0 = \mathrm{e}^{\lambda t} x_0$ . 这意味着 $\mathrm{e}^{-\lambda s} T(s)x_0$ 是 $s$ 的周期为 $t$ 的函数, 并且由于它不恒为零, 其 Fourier 系数中必定有一个非零, 即存在 $k \in \mathbb{N}$ 使得

$$x _ {k} = \frac {1}{t} \int_ {0} ^ {t} \mathrm{e} ^ {- (2 \pi i k / t) s} (\mathrm{e} ^ {- \lambda s} T (s) x _ {0}) \mathrm{d} s \neq 0.$$

现在我们证明 $\lambda_{k} = \lambda + 2\pi k\mathrm{i} / t \in \sigma_{p}(A)$ . 事实上, 对于 $h > 0$ , 我们有

$$
\begin{array}{l} \frac {T (h) - I}{h} x _ {k} = \frac {1}{t h} \int_ {0} ^ {t} \mathrm{e} ^ {- \lambda_ {k} s} T (s + h) x _ {0} \mathrm{d} s - \frac {1}{t h} \int_ {0} ^ {t} \mathrm{e} ^ {- \lambda_ {k} s} T (s) x _ {0} \mathrm{d} s \\ = \frac {1}{t h} \int_ {t} ^ {t + h} \mathrm{e} ^ {- \lambda_ {k} (s - h) t} I (s) x _ {0} \mathrm{d} s - \frac {1}{t h} \int_ {0} ^ {h} \mathrm{e} ^ {- \lambda_ {k} s} T (s) x _ {0} \mathrm{d} s \\ + \frac {\mathrm{e} ^ {\lambda_ {k} h} - 1}{t h} \int_ {h} ^ {t} \mathrm{e} ^ {- \lambda_ {k} s} T (s) x _ {0} \mathrm{d} s. \\ \end{array}
$$

因此

$$\lim _ {h \downarrow 0} \frac {T (h) - I}{h} x _ {k} = \lambda_ {k} x _ {k},$$

这表明 $x_{k}\in \mathcal{D}(A)$ ，并且 $Ax_{k} = \lambda_{k}x_{k}$ ，即 $\lambda_{k}\in \sigma_{p}(A)$ .证毕.

定理5.3.11 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 为其生成算子，那么我们有：

(1) 如果 $\lambda \in \sigma_r(A)$ 和 $\lambda_n = \lambda + 2\pi n\mathrm{i} / t \notin \sigma_p(A), \forall n \in \mathbb{N}$ , 则 $e^{\lambda t} \in \sigma_r(T(t))$ ;  
(2) 如果 $\mathbf{c}^{\lambda t} \in \sigma_r(T(t))$ , 则 $\lambda_n = \lambda + 2\pi n\mathrm{i}/t \notin \sigma_p(A), \forall n \in \mathbb{N}$ , 并且存在 $k \in \mathbb{N}$ 使得 $\lambda_k \in \sigma_r(A)$ .

证明 (1) 设 $\lambda \in \sigma_r(A)$ , 则存在 $x^* \in X^*, x^* \neq 0$ 使得

$$\langle (\lambda I - A) x, x ^ {*} \rangle = 0, \quad \forall x \in \mathcal {D} (A).$$

由此从式 (5.3.28) 得到

$$\langle (\mathrm{e} ^ {\lambda t} I - T (t)) x, x ^ {*} \rangle = 0. \quad \forall x \in X,$$

这意味着 $\mathbf{c}^{\lambda t}I - T(t)$ 的值域在 $X$ 中不稠。如果 $\mathrm{e}^{\lambda t}I - T(t)$ 不是一对一的，则依据定理5.3.10，存在 $k\in \mathbb{N}$ 使得 $\lambda_{k}\in \sigma_{p}(A)$ ，这与(1)的假设矛盾。这样，我们证明了结论 $\mathrm{e}^{\lambda t}\in \sigma_r(T(t))$ ；
