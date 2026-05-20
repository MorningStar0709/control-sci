$$u _ {k} ^ {0} = - L _ {k} x _ {k} + (I - M _ {k} ^ {+} M _ {k}) u _ {k}, \tag {4.4.51}$$

$u_{k}$ 为任一 $r$ 维确定性向量.

推论4.4.2 当 $Q_{2}(k) > 0$ 时， $M_{k} > 0$ ，则式(4.4.47)和式(4.4.51)分别成为

$$u _ {k} ^ {0} = - L _ {k} \hat {x} _ {k} \quad \text {及} \quad u _ {k} ^ {0} = - L _ {k} x _ {k}.$$

注4.4.2 从定理4.4.1看出，滤波精度 $P_{k}$ 不受控制影响，滤波公式可独立于控制进行，而带噪声时的最优控制可直接得自确定性系统的最优控制，为此只要把确定性系统的状态换成它的滤波值。这时我们称成立分离原理。

上面我们限定了控制 $u_{k}$ 只能线性地依赖 $y_{0}, \cdots, y_{k}$ ，现在考察一般的依赖关系， $u_{k}$ 可以是 $y_{0}, \cdots, y_{k}$ 的任意 Borel 可测函数，也就是说， $u_{k}$ 是一般的反馈控制。但对系统 (4.4.40)，(4.4.41) 作如下要求：

C1) $\Phi_{k + 1,k}, D_{k + 1}, B_{k + 1}, C_k, F_k$ 是确定性阵；  
C2) 在 $y_0$ 条件下， $x_0$ 是期望为 $E(x_0|y_0)$ ，协方差阵为 $R_{x_0}^{y_0}$ 的条件正态向量；  
C3) $\{w_k\}$ 相互独立，相同分布，并且和 $\left[ \begin{array}{c}x_0\\ y_0 \end{array} \right]$ 独立， $w_{k}\in \mathcal{N}(0,I)$ 记 $\mathcal{U}\stackrel {\mathrm{def}}{=}$ $\{u_k:$ 对 $y^{k}$ 可测，且 $E\| u_k\|^2 < \infty \}$ . $\mathcal{U}$ 称为容许控制集．在 $\mathcal{U}$ 中要找 $u^0$ ，使 $EJ(u)$ 达极小，其中

$$J (u) = x _ {N} ^ {\mathrm{T}} Q _ {0} x _ {N} + \sum_ {k = 0} ^ {N - 1} (x _ {k} ^ {\mathrm{T}} Q _ {1} (k) x _ {k} + u _ {k} ^ {\mathrm{T}} Q _ {2} (k) u _ {k}), \tag {4.4.52}$$

$Q_{0}(k), Q_{1}(k), Q_{2}(k)$ 均为对称非负定确定性阵.

定理 4.4.4 在条件 C1)\~C3) 下，使性能指标 (4.4.52) 达最小的最优随机控制为 $u_{k}^{0}$ ， $u_{k}^{0}$ 形式上仍由式 (4.4.47) 给出，只是其中 $u_{k}$ 可为任一 U 中的容许控制， $\hat{x}_{k}=E(x_{k}|y^{k})$ .

证明 首先注意到 C1)\~C3) 保证了 A1)\~A4) 成立，所以定理 4.4.2 的结论成立.

对式 (4.4.50) 式两边取期望，并注意到对任意随机向量 $\chi, E(\cdot) = E(E(\cdot|\chi))$ ，便知

$$
\begin{array}{l} E J (u) = E x _ {0} ^ {\mathrm{T}} S _ {0} x _ {0} + E \sum_ {k = 0} ^ {N - 1} E \left\{\left[ w _ {k + 1} ^ {\mathrm{T}} D _ {k + 1} ^ {\mathrm{T}} S _ {k + 1} \left(\Phi_ {k + 1, k} x _ {k} + B _ {k} u _ {k}\right) \right. \right. \\ \left. + \left(\Phi_ {k + 1, k} x _ {k} + B _ {k} u _ {k}\right) ^ {\mathrm{T}} S _ {k + 1} D _ {k + 1} w _ {k + 1} ] | y ^ {k}, x _ {k} \right\} \\ + E \sum_ {k = 0} ^ {N - 1} w _ {k + 1} ^ {\mathrm{T}} D _ {k + 1} ^ {\mathrm{T}} S _ {k + 1} D _ {k + 1} w _ {k + 1} \\ + E \sum_ {k = 0} ^ {N - 1} E \left[ \left(u _ {k} + L _ {k} x _ {k}\right) ^ {\mathrm{T}} M _ {k} \left(u _ {k} + L _ {k} x _ {k}\right) \mid y ^ {k} \right]. \\ \end{array}
$$

由于 $u_{k},\hat{x}_{k}$ 对 $y^{k}$ 可测，所以
