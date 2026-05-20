因此 $\dim V \leqslant N$ . 如果 $\dim V < N$ , 则 $\operatorname{sp}(A) = \overline{\operatorname{span}}\left\{\psi_n \mid n > N\right\} + V$ 的余维数大于 0, 从而 $\operatorname{sp}(A) \neq H$ , 与 $A$ 的根子空间的完备性结论相矛盾.

因此实际上 $\dim V = N$ ，即 V 恰好由 N 个 A 的广义本征元 $\tilde{\psi}_{1}, \tilde{\psi}_{2}, \cdots, \tilde{\psi}_{N}$ 张成。显然 $\tilde{\psi}_{1}, \tilde{\psi}_{2}, \cdots, \tilde{\psi}_{N}$ 是 V 的 Riesz 基。这样我们证明了 A 的所有广义本征元

$$\{\widetilde {\psi} _ {1}, \widetilde {\psi} _ {2}, \dots , \widetilde {\psi} _ {N} \} \cup \{\psi_ {n} \mid n > N \}$$

构成 $H$ 的Riesz基. 证毕.

定理 10.4.4 的意义在于，一般来说，算子的广义本征值和广义本征元 (特别是低频段) 的解析计算是很难的，有时甚至是不可能的。但通过渐近分析，有可能得到其高频部分的渐近表达式，进而验证式 (10.4.56) 就够了。而 Bari 定理则要求对所有广义本征元验证。下面我们举例说明之。

例 10.4.6 (Euler-Bernoulli 梁的耗散边界反馈镇定) 在例 10.4.4 中，假定了 $\alpha \geqslant 0, \beta > 0$ . 当 $\beta = 0, \alpha > 0$ 时则在时域范畴内难于找到合适的乘子. 现在我们用 Riesz 基方法来研究这一情形. 于是我们考察如下带耗散边界反馈的 Euler-Bernoulli 梁系统:

$$
\left\{ \begin{array}{l l} \ddot {y} (x, t) + a ^ {4} y ^ {\prime \prime \prime \prime} (x, t) = 0, & 0 <   x <   1, t > 0, \\ y (0, t) = 0, \quad y ^ {\prime} (0, t) = 0, & y ^ {\prime \prime \prime} (1, t) = 0, \\ y ^ {\prime \prime} (1, t) = - \alpha \dot {y} ^ {\prime} (1, t), & \alpha > 0. \end{array} \right. \tag {10.4.57}
$$

在状态空间 $\mathcal{H} = V_0^2 (0,1)\times L^2 (0,1)$ 中二阶系统(10.4.57)可以写成 $\mathcal{H}$ 中的一阶发展方程

$$\dot {Y} (t) = \mathcal {A} Y (t).$$

$\mathcal{A}$ 的定义同例10.4.4, $\mathcal{A}$ 生成 $\mathcal{H}$ 中 $C_0$ 压缩半群. 我们要证明 $\mathcal{A}$ 的广义本征元全体构成 $\mathcal{H}$ 的Riesz基. 容易验证 $0 \in \rho(\mathcal{A})$ , 并且 $\mathcal{A}$ 有紧豫解式, 从而 $\sigma(\mathcal{A}) = \sigma_p(\mathcal{A})$ .

(1) $\mathcal{A}$ 的每个本征值 $\lambda$ 都是代数单的，并且若令 $\omega^4 = -\frac{\lambda^2}{a^4}$ ，则 $\omega$ 满足如下特征方程：

$$\mathrm{i} \alpha a ^ {2} \omega (\sinh \omega \cos \omega + \cosh \omega \sin \omega) + (1 + \cosh \omega \cos \omega) = 0. \tag {10.4.58}$$

此外， $A$ 的相应于本征值 $\lambda = \mathrm{i}a^2\omega^2$ 的本征元为 $[f,\lambda f]^{\mathrm{T}}$ ，其中 $f$ 可选为

$$
\begin{array}{l} f (x) = \cosh \omega (1 - x) - \cos \omega (1 - x) + \sinh \omega \sin \omega x \\ + \sin \omega \sinh \omega x - \cosh \omega \cos \omega x + \cos \omega \cosh \omega x. \tag {10.4.59} \\ \end{array}
$$

上述结论都可直接计算得到.

(2) $\mathcal{A}$ 有本征值序列 $\{\lambda_n, \overline{\lambda}_n\}$ , 这里 $n$ 充分大, $\lambda_n = \mathrm{i}\alpha^2\omega_n^2$ , $\omega_n$ 和 $\lambda_n$ 分别有渐近表达式
