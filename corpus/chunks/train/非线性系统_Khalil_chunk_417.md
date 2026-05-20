$$\Omega = \{V (\eta) \leqslant c _ {0} \} \times \{| s _ {i} | \leqslant c, 1 \leqslant i \leqslant p \}, \quad c _ {0} \geqslant \alpha (c) \tag {14.16}$$

也是正不变集, 只要 $c > \varepsilon$ , 且 $\Omega \subset T(D)$ 。适当选择 $\varepsilon, c > \varepsilon$ 和 $c_0 \geqslant \alpha(c)$ 使得 $\Omega \subset T(D)$ , 取紧集 $\Omega$ 作为“吸引区”的估计值, 则初态在 $\Omega$ 中的轨线在 $t \geqslant 0$ 时都是有界的, 在某一有限时间之后, 有 $|s_i(t)| \leqslant \varepsilon$ 。由前面的分析可得, 对于所有 $V(\eta) \geqslant \alpha(\varepsilon)$ , 有 $\dot{V} \leqslant -\alpha_3(\gamma(k_1\varepsilon))$ , 因此轨线在有限时间内到达正不变集

$$\Omega_ {\varepsilon} = \{V (\eta) \leqslant \alpha (\varepsilon) \} \times \{| s _ {i} | \leqslant \varepsilon , 1 \leqslant i \leqslant p \} \tag {14.17}$$

选择足够小的 $\varepsilon$ 可使集合 $\Omega_{\varepsilon}$ 任意小，在极限情况下，即当 $\varepsilon$ 趋于零时， $\Omega_{\varepsilon}$ 收缩到原点，这说明连续滑模控制器补偿了其不连续型的性能缺陷。最后要注意，如果所有假设都全局成立，且 $V(\eta)$ 是径向无界的，那么可以选择任意大的 $\Omega$ ，包含任何初始状态。下面的定理总结了上面的讨论。

![](image/2c58337a00c0dc5a20ea4f43c7e7ef21419ba4e7ad11165707257755f682774e.jpg)  
图 14.12 集合 $\Omega$ 和标量 s 的表示。在 $\alpha(\cdot)$ 曲线的上方 $\dot{V}<0$

定理 14.1 考虑系统(14.4)～(14.5)，假设存在 $\phi(\eta)$ ， $V(\eta)$ ， $\varrho(x)$ 和 $\kappa_{0}$ ，满足式(14.10)，式(14.14)和式(14.15)。设 u 和 v 分别由式(14.8)和式(14.13)给出，并假设选择 $\varepsilon, c > \varepsilon$ 和 $c_{0} \geqslant \alpha(c)$ ，使由式(14.16)定义的集合 $\Omega$ 在 $T(D)$ 内，那么对于所有 $t \geqslant 0$ ，对于所有 $(\eta(0), \xi(0)) \in \Omega$ ，轨线 $(\eta(t), \xi(t))$ 都是有界的，并且在有限时间内都能到达由式(14.17)定义的正不变集 $\Omega_{\varepsilon}$ 。此外，如果假设是全局成立的， $V(\eta)$ 径向无界，则上述结论对于任意初始状态都成立。

该定理说明,滑模控制器是毕竟有界的,其最终边界可通过设计参数 $\varepsilon$ 控制。定理还给出了全局毕竟有界性的条件。由于 $\delta$ 的不确定性,它在 x=0 处可能不为零,所以一般来说,毕竟有界性是我们所期望的最好结果。但是如果 $\delta$ 在原点为零,我们就能证明原点渐近稳定性,正如下面的定理。

定理14.2 假设定理14.1的所有假设在 $\varrho(0) = 0$ 和 $\kappa_0 = 0$ 时都成立，进一步假设 $\dot{\eta} = f_a(\eta, \phi(\eta))$ 的原点是指数稳定的，那么存在 $\varepsilon^* > 0$ ，使得对于所有 $0 < \varepsilon < \varepsilon^*$ ，闭环系统的原点是指数稳定的，并且 $\Omega$ 是吸引区的一个子集。如果假设全局成立，那么原点是全局一致渐近稳定的。

证明:若不等式(14.10)在 $\kappa_{0}=0$ 时成立,则 $\Delta_{i}$ 一定与 v 无关。因此,有 $\Delta_{i}=\Delta_{i}(t,x)$ 。又由定理 14.1 可知所有从 $\Omega$ 内发出的轨线都在有限时间内进入 $\Omega_{\varepsilon}$ 。在 $\Omega_{\varepsilon}$ 内,闭环系统表示为
