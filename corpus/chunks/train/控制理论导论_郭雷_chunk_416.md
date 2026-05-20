$$\| f \| _ {H ^ {1} (\Omega)} \leqslant C \left(\int_ {\Omega} | \nabla f | ^ {2} \mathrm{d} x\right) ^ {1 / 2}, \quad \forall f \in H _ {0} ^ {1} (\Omega).$$

这就是熟知的 Poincaré 不等式。类似于这样的不等式在求得偏微分方程解的先验估计中是非常有用的。下面的 Deny-Lions 引理是这一类 Poincaré 不等式的基础，见文献 [3].

引理 5.4.1 (Deny-Lions) 设 $P_{k-1}(\Omega)$ 表示 $\Omega$ 上所有阶小于或等于 k-1 的 N 变量多项式空间， $m = \dim(P_{k-1}(\Omega))$ . 假定 $\{\ell_{1}, \ell_{2}, \cdots, \ell_{m}\}$ 是 $H^{k}(\Omega)$ 上 m 个连续线性泛函，使得 $\{\ell_{1}, \ell_{2}, \cdots, \ell_{m}\}$ 在 $P_{k-1}(\Omega)$ 上是线性无关的. 对于 $f \in H^{k}(\Omega)$ ，令

$$\| f \| ^ {\prime} = \left(\sum_ {j = 1} ^ {m} | \ell_ {j} (f) | ^ {2} + | f | _ {k, 2}\right) ^ {1 / 2},$$

那么 $\| \cdot \|'$ 定义 $H^{k}(\Omega)$ 上一等价范数，即存在常数 $C_1, C_2 > 0$ ，使得

$$C _ {1} \| f \| ^ {\prime} \leqslant \| f \| _ {H ^ {k} (\Omega)} \leqslant C _ {1} \| f \| ^ {\prime}, \quad \forall f \in H ^ {k} (\Omega).$$

例5.4.4 设 $\Gamma_0 \subset \partial \Omega$ 使得 $\operatorname{meas}(\Gamma_0) > 0$ , 这里 $\operatorname{meas}(\Gamma_0)$ 为 $\Gamma_0$ 的测度. 定义

$$H _ {\Gamma_ {0}} ^ {1} (\Omega) = \left\{f \in H ^ {1} (\Omega) \mid f | _ {\Gamma_ {0}} = 0 \right\}.$$

注意根据迹定理 5.4.1, 当 $f \in H^{1}(\Omega)$ 时, $f|_{\Gamma_0} \in H^{1/2}(\Gamma_0)$ . 定义线性泛函 $\ell: H^{1}(\Omega) \to \mathbb{R}$ 为

$$\ell (f) = \int_ {\Gamma_ {0}} f (s) \mathrm{d} s.$$

那么根据 Cauchy 不等式、紧嵌入定理 5.4.3 和迹定理 5.4.1, 存在正常数 $C'$ 和 $C$ , 使得

$$
\begin{array}{l} | \ell (f) | \leqslant \operatorname{meas} \left(\Gamma_ {0}\right) ^ {1 / 2} \left(\int_ {\Gamma_ {0}} | f (s) | ^ {2} \mathrm{d} s\right) ^ {1 / 2} \\ \leqslant C ^ {\prime} \| f \| _ {H ^ {1 / 2} (\partial \Omega)} \leqslant C \| f \| _ {H ^ {1} (\Omega)}. \\ \end{array}
$$

从而 $\ell$ 是 $H^{1}(\Omega)$ 上的连续线性泛函。于是从引理5.4.1可知存在正常数 $C_1$ 和 $C_2$ ，使得

$$
\begin{array}{l} C _ {1} \left(\ell (f) ^ {2} + \int_ {\Omega} | \nabla f | ^ {2} \mathrm{d} x\right) \leqslant \int_ {\Omega} \left(| f | ^ {2} + | \nabla f | ^ {2}\right) \mathrm{d} x \\ \leqslant C _ {2} \left(\ell (f) ^ {2} + \int_ {\Omega} | \nabla f | ^ {2} \mathrm{d} x\right), \quad \forall f \in H _ {\Gamma_ {0}} ^ {1} (\Omega). \\ \end{array}
$$

现在对于 $f \in H_{\Gamma_0}^1(\Omega)$ , 有 $\ell(f) = 0$ , 因此我们得到

$$
\begin{array}{l} C _ {1} \int_ {\Omega} | \nabla f | ^ {2} \mathrm{d} x \leqslant \int_ {\Omega} \left(| f | ^ {2} + | \nabla f | ^ {2}\right) \mathrm{d} x \\ \leqslant C _ {2} \int_ {\Omega} | \nabla f | ^ {2} \mathrm{d} x, \quad \forall f \in H _ {\Gamma_ {0}} ^ {1} (\Omega). \\ \end{array}
$$

这表明双线性泛函
