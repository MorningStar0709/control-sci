设 $\{x_{n}\} \subset X_{0}$ 使得 $\lim_{n\to \infty}x_n = x_0$ 。为简单起见，令 $r_n(\lambda) = (\lambda I - T)^{-1}x_n$ 。根据假设， $r_n(\lambda)$ 在 $J_0^c$ 中是解析的，并且对于 $\lambda \in \rho(T)$ ，有 $\lim_{n\to \infty}r_n(\lambda) = (\lambda I - T)^{-1}x_0$ 。为证 $x_0 \in X_0$ ，我们只需证明 $r_n(\lambda)$ 在 $G_{1}$ 中一致收敛于某个解析函数。为此，令于是 $f$ 是整个平面 $\mathbb{C}$ 上的整函数，并且 $f(\lambda)r_n(\lambda)$ 在 $\overline{G_1} \setminus \{z_1, z_2\}$ 上是解析的。注意当 $\lambda \in \Gamma_1$ 时， $\lambda - z_1 = (|\lambda| - 1)z_1$ 。于是当 $\lambda \in \Gamma_1 \setminus \{z_1\}$ 时

![](image/e61cb157539c641eb419ad6b1e14f13b268caddc4b308080b9209051c11421f2.jpg)

<details>
<summary>text_image</summary>

f(\lambda) = (\lambda - z_1)^2 (\lambda - z_2)^2.
\Gamma_3
\Gamma_4
z_1
G_1
0
\Gamma_1
G_2
\Gamma_2
z_2
</details>

图5.3.2

$$\| f (\lambda) r _ {n} (\lambda) \| = | f (\lambda) | \| (\lambda I - T) ^ {- 1} x _ {n} \| \leqslant | | \lambda | - 1 | (| \lambda | + 1) ^ {2} \| x _ {n} \| \leqslant 9 \| x _ {n} \|.$$

同样地，当 $\lambda \in \Gamma_2\backslash \{z_2\}$ 时

$$\| f (\lambda) r _ {n} (\lambda) \| \leqslant 9 \| x _ {n} \|,$$

而当 $\lambda \in \Gamma_3$ 时，我们有

$$\| f (\lambda) r _ {n} (\lambda) \| \leqslant (| \lambda | + 1) ^ {4} \| x _ {n} \| \leqslant 8 1 \| x _ {n} \|.$$

因此 $f(\lambda)r_n(\lambda)$ 在 $\partial G_{1}$ 上是连续的，并且根据Cauchy积分公式

$$f (\lambda) r _ {n} (\lambda) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {1} \cup \Gamma_ {2} \cup \Gamma_ {3}} \frac {f (\mu) r _ {n} (\mu)}{\mu - \lambda} \mathrm{d} \mu , \quad \forall \lambda \in G _ {1}.$$

于是

$$\| f (\lambda) r _ {n} (\lambda) - f (\lambda) r _ {m} (\lambda) \| \leqslant \frac {8 1 \| x _ {n} - x _ {m} \|}{2 \pi} \int_ {\Gamma_ {1} \cup \Gamma_ {2} \cup \Gamma_ {3}} \frac {1}{| \mu - \lambda |} d \mu , \quad \forall \lambda \in G _ {1},$$

这意味着 $f(\lambda)r_n(\lambda)$ , 从而 $r_n(\lambda)$ 在 $G_1$ 的任意闭子集中一致收敛于某个解析函数. 因此我们得出结论: $x_0 \in X_0$ .

最后我们证明 $X_0 \neq \{0\}$ . 对任意 $x \in X$ , 令

$$y (x) = \int_ {\partial G _ {2}} f (\lambda) (\lambda I - T) ^ {- 1} x \mathrm{d} \lambda .$$

今证 $y(x) \in X_0$ . 事实上，利用豫解恒等式 (5.2.1) 得到
