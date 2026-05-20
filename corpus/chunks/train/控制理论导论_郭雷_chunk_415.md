# Sobolev 嵌人定理

对于非负整数 $m$ 和 $\varepsilon, 0 \leqslant \varepsilon < 1$ , $C^{m,\varepsilon}(\Omega)$ 表示 $\Omega$ 上直到 $m$ 次连续可微，并且 $m$ 次导数为 $\varepsilon$ -Hölder 连续的函数空间: $f \in C^{m,\varepsilon}(\Omega)$ ,

$$\| f \| _ {C ^ {m, \epsilon}} = \sum_ {| \alpha | \leqslant m} \sup _ {x \in \Omega} | D ^ {\alpha} f (x) | + \sum_ {| \alpha | = m} \sup _ {x \neq y} \left\{\frac {| D ^ {\alpha} f (x) - D ^ {\alpha} f (y) |}{| x - y | ^ {\epsilon}} \right\} < \infty .$$

定理5.4.2 (Sobolev 嵌入定理) 设 $\Omega \subset \mathbb{R}^N$ 为有界开区域，边界 $\partial \Omega$ 充分光滑，设 $s = m + N / 2 + \varepsilon, 0 < \varepsilon < 1, m$ 为非负整数，则嵌入

$$H ^ {s} (\Omega) \hookrightarrow C ^ {m, \varepsilon} (\Omega)$$

是连续的.

根据定理 5.4.2, 若空间维数 $N = 1$ , $\Omega = (a, b)$ , 则 $H^{1}(a, b) \hookrightarrow C^{0,1/2}(a, b)$ , 故 $f \in H^{1}(a, b)$ 至少在 $(a, b)$ 上是连续的. 但当 $N = 2$ 时, $H^{1}(\Omega)$ 中的元未必是连续的. 例如, 取 $\Omega$ 为 $\mathbb{R}^2$ 中半径为 $1/2$ 中心在原点的开圆盘, $y(x) = \ln \ln(|x|^{-1})$ , 则 $y \in H^{1}(\Omega)$ , 但 $y$ 显然在 $x = 0$ 处是不连续的.

定理 5.4.3 (Sobolev 紧嵌入定理) 设 $\Omega \subset \mathbb{R}^N$ 为有界开区域，边界 $\partial \Omega$ 充分光滑，设 $s_1, s_2 \in \mathbb{R}, s_2 > s_1$ ，则嵌入 $H^{s_2}(\Omega) \hookrightarrow H^{s_1}(\Omega)$ 是紧的，即对于 $H^{s_2}(\Omega)$ 中的有界序列 $\{y_k\}$ ，必有 $\{y_k\}$ 的子序列 $\{y_{k_i}\}$ 使得 $\| y_{k_i} - y \|_{H^{s_1}(\Omega)} \to 0 (i \to \infty)$ ，其中 $y \in H^{s_1}(\Omega)$ .

定理5.4.4 设 $\Omega \subset \mathbb{R}^N$ 为开集，则嵌入

$$H ^ {s} (\varOmega) \hookrightarrow L ^ {p} (\varOmega), \qquad \text {当} \frac {1}{p} = \frac {1}{2} - \frac {s}{N} > 0,$$

和

$$H ^ {s} (\varOmega) \hookrightarrow L ^ {p} (\varOmega), \qquad \forall p \in [ 1, \infty), \quad \text {当} \frac {1}{2} - \frac {s}{N} = 0,$$

是连续的；进而当 $\Omega$ 还是有界时，上述嵌入还是紧的.

定理5.4.5（插值不等式）设 $\Omega \subset \mathbb{R}^N$ 为有界开区域，具有充分光滑边界， $m$ 为自然数。那么对于任意 $\varepsilon > 0$ ，存在常数 $C(\varepsilon) > 0$ ，使得

$$\| f \| _ {H ^ {m} (\Omega)} \leqslant \varepsilon \sum_ {| \alpha | = m} \| D ^ {\alpha} f \| _ {L ^ {2} (\Omega)} ^ {2} + C (\varepsilon) \| f \| _ {L ^ {2} (\Omega)}, \quad \forall f \in H ^ {m} (\Omega).$$

设 $\Omega$ 是 $\mathbb{R}^N$ 中的单连通有界开区域，具有充分光滑边界。一般说来，对于 $f \in H^{m}(\Omega)$ ，若令

$$| f | _ {m, 2} = \sum_ {| \alpha | = m} \| D ^ {\alpha} f \| _ {L ^ {2} (\Omega)},$$

则 $|\cdot|_{m,2}$ 仅仅是 $H_m(\Omega)$ 中一个拟范数，就是说，范数中条件 $|f|_{m,2} = 0 \Longrightarrow f = 0$ 不满足．下面要说明，如果对 $f$ 加上适当的边条件，则使用 $f$ 的最高阶导数就可以定义出 $H^m(\Omega)$ 的一较小闭子空间中的范数.

在 $H_0^1 (\Omega)$ 中，我们有
