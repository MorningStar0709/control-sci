其中 $\zeta=\left[e_{0},\cdots,e_{\rho-1}\right]^{T}$ ，A 是赫尔维茨矩阵，利用不等式

$$s \dot {s} \leqslant - a \beta_ {0} (1 - \kappa_ {0}) | s |, \quad | s | \geqslant \varepsilon$$

证明集合 $\{|s|\leqslant c\}$ 是正不变集, $c>\varepsilon$ 。第二步,利用李雅普诺夫函数 $V_{2}(\zeta)=\zeta^{T}P\zeta$ ,以及不等式

$$\dot {V} _ {2} \leqslant - \zeta^ {\mathrm{T}} \zeta + 2 \| \zeta \| \| P B \| | s |$$

证明对于某个 $\rho_{1}>0$ , 集合 $\{|s|\leqslant c\}\cap\{V_{2}\leqslant c_{2}\rho_{1}\}$ 是正不变集, 其中 P 是李雅普诺夫方程 $PA+A^{T}P=-I$ 的解, 且在该集合内, 对于某个 $\rho_{2}>0$ , 有 $\|e\|\leqslant\varphi_{2}$ 。最后利用不等式

$$\dot {V} _ {1} \leqslant - \tilde {\alpha} _ {3} (\| z \|), \quad \forall \| z \| \geqslant \tilde {\gamma} (c \rho_ {2})$$

证明

$$\Omega = \{| s | \leqslant c \} \cap \{V _ {2} \leqslant c ^ {2} \rho_ {1} \} \cap \{V _ {1} \leqslant c _ {0} \}$$

对于任何 $c_{0} \geqslant \tilde{\alpha}_{2} (\tilde{\gamma} (c\rho_{2}))$ 是正不变集。同样可以证明

$$\Omega_ {\varepsilon} = \{| s | \leqslant \varepsilon \} \cap \{V _ {2} \leqslant \varepsilon^ {2} \rho_ {1} \} \cap \{V _ {1} \leqslant \tilde {\alpha} _ {2} (\tilde {\gamma} (\varepsilon \rho_ {2})) \}$$

是正不变集,且始于 $\Omega$ 的每条轨线都能在有限时间内进入 $\Omega_{\varepsilon}$ 。

如果 z=0 是 $\dot{z}=\tilde{f}_{0}(z,e,w,r)$ 的指数稳定平衡点，重复定理 14.2 的证明，可证明 $\Omega_{\varepsilon}$ 内的每条轨线当 t 趋于无穷时都趋近期望的平衡点。特别地，如果由定理 4.14 得到， $V_{3}(z,w,r)$

是对于指数稳定平衡点 $z = 0$ 的逆李雅普诺夫函数， $P$ 是李雅普诺夫方程 $PA + A^{\mathrm{T}}P = -I$ 的解， $(\zeta, \tilde{s})$ 为 $(\zeta, s)$ 与平衡值的偏差，则可以证明，当 $\lambda > 0$ 时，

$$V _ {0} = V _ {3} + \lambda \tilde {\zeta} ^ {\mathrm{T}} P \tilde {\zeta} + \frac {1}{2} \tilde {s} ^ {2}$$

的导数满足不等式①

$$
\dot {V} _ {0} \leqslant - \left[ \begin{array}{c} \| z \| \\ \| \tilde {\zeta} \| _ {2} \\ | \tilde {s} | \end{array} \right] ^ {\mathrm{T}} \left[ \begin{array}{c c c} k _ {1} & - k _ {3} & - k _ {4} \\ - k _ {3} & \lambda & - (\lambda k _ {5} + k _ {6}) \\ - k _ {4} & - (\lambda k _ {5} + k _ {6}) & (k _ {2} / \varepsilon) - k _ {7} \end{array} \right] \left[ \begin{array}{c} \| z \| \\ \| \tilde {\zeta} \| _ {2} \\ | \tilde {s} | \end{array} \right]
$$

其中 $k_{1}$ 和 $k_{2}$ 为正常数, $k_{3}$ 到 $k_{7}$ 为非负常数。选择 $\lambda > k_{3}^{2}/k_{1}$ , 可使导数 $\dot{V}_{0}$ 为负定, 然后选择足够小的 $\varepsilon$ , 使该 $3 \times 3$ 矩阵为正定的。

在 $\beta = k$ (常数) 和 u = v 的特殊情况下, 连续滑模控制器可由下式给出:

$$u = - k \operatorname{sat} \left(\frac {k _ {0} e _ {0} + k _ {1} e _ {1} + \cdots + k _ {\rho - 1} e _ {\rho - 1} + e _ {\rho}}{\varepsilon}\right) \tag {14.29}$$
