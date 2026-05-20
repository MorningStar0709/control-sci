# 迹定理

定理5.4.1(迹定理) 对于任意 $f \in H^{m}(\Omega)$ , 我们可以定义 $f$ 在边界 $\Gamma = \partial \Omega$ 上的迹为

$$\gamma (f) = \left[ f \big | _ {\Gamma}, \frac {\partial f}{\partial \nu} \big | _ {\Gamma}, \dots , \frac {\partial^ {m - 1} f}{\partial \nu^ {m - 1}} \big | _ {\Gamma} \right].$$

我们有

$$\frac {\partial^ {k} f}{\partial \nu^ {k}} \in H ^ {m - k - 1 / 2} (\Gamma), \quad 0 \leqslant k \leqslant m - 1,$$

并且

(1) 迹映射 $\gamma: H^{m}(\Omega) \to \prod_{k=0}^{m-1} H^{m-k-1/2}(\Gamma)$ 是线性连续满射；

(2) $\gamma$ 的零空间

$$\mathcal {N} (\gamma) = \left\{f \in H ^ {m} (\Omega) \mid \frac {\partial^ {k} f}{\partial \nu^ {k}} = 0, 0 \leqslant k \leqslant m - 1 \right\}$$

恰好是 $\mathcal{D}(\Omega)$ 在 $H^{m}(\Omega)$ 中的闭包 $H_0^m (\Omega)$ , 从而

$$H _ {0} ^ {m} (\Omega) = \left\{f \in H ^ {m} (\Omega) \mid \frac {\partial^ {k} f}{\partial \nu^ {k}} = 0, 0 \leqslant k \leqslant m - 1 \right\}.$$

由于 $\mathcal{D}(\Omega)$ 在 $H_0^m (\Omega)$ 中稠，从而可以把 $H_0^m (\Omega)$ 的对偶等同于 $\mathcal{D}'(\Omega)$ 的一个子空间

$$H ^ {- m} (\Omega) = \left(H _ {0} ^ {m} (\Omega)\right) ^ {\prime}.$$

显然我们有

$$H _ {0} ^ {m} (\Omega) \subset L ^ {2} (\Omega) \subset H ^ {- m} (\Omega).$$

对于 $f \in H^{-m}(\Omega)$ , 必定存在 $f_{\alpha} \in L^{2}(\Omega), 0 \leqslant |\alpha| \leqslant m$ , 使得

$$f = \sum_ {| \alpha | \leqslant m} D ^ {\alpha} f _ {\alpha}.$$

上述迹定理对于非整数 $s > 0$ 也成立：这时对于 $f \in H^{s}(\Omega)$ ，我们有

$$\gamma (f) \in \prod_ {k = 0} ^ {m - 1} H ^ {s - k - 1 / 2} (\Gamma),$$

其中

$$\gamma (f) = \left[ f \Big | _ {\Gamma}, \frac {\partial f}{\partial \nu} \Big | _ {\Gamma}, \dots , \frac {\partial^ {m - 1} f}{\partial \nu^ {m - 1}} \Big | _ {\Gamma} \right], \quad s - m + 1 / 2 > 0.$$
