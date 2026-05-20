这样,不等式 $\sup_{t\geqslant0}\|\dot{u}(t)\|<2c_{1}\alpha_{1}r/c_{4}L$ 成立,又由式(9.47)得

$$
\begin{array}{l} \| z (t) \| \leqslant \sqrt {\frac {c _ {2}}{c _ {1}}} \| z (0) \| e ^ {- \alpha_ {1} t} + \frac {c _ {4} L}{2 c _ {1}} \int_ {0} ^ {t} e ^ {- \alpha_ {1} (t - \tau)} \varepsilon d \tau \\ \leqslant \sqrt {\frac {c _ {2}}{c _ {1}}} \| z (0) \| e ^ {- \alpha_ {1} t} + \frac {c _ {4} L \varepsilon}{2 c _ {1} \alpha_ {1}} = \sqrt {\frac {c _ {2}}{c _ {1}}} \| z (0) \| e ^ {- \alpha_ {1} t} + b \theta \\ \end{array}
$$

在一定时间后,指数衰减项将小于 $(1-\theta)b$ ,这说明 $z(t)$ 是毕竟有界的,由b确定。另外,如果当t趋于无穷时, $\dot{u}(t)$ 趋于零,则由式(9.47)可清楚地得到,当t趋于无穷时, $z(t)$ 趋于零。如果对于所有 $u\in\Gamma,h(u)=0$ ,则可取L=0。因而 $\dot{V}$ 的上界简化为

$$\dot {V} \leqslant - (c _ {3} - c _ {5} \varepsilon) \| z \| ^ {2}$$

这就证明了如果 $\varepsilon < c_{3} / c_{5}$ ，则 $z = 0$ 是指数稳定的。

定理9.3要求冻结系统(9.40)存在一个李雅普诺夫函数 $V(z,\alpha)$ ，满足不等式(9.41)至不等式(9.44)。引理9.8将说明在适度光滑情况下，如果冻结系统的平衡点 $z = 0$ 是关于 $\alpha$ 一致指数稳定的，则这样的李雅普诺夫函数一定存在。如同在4.7节中讨论的逆李雅普诺夫定理，以上结论可以通过推导系统的逆李雅普诺夫函数来获得。

引理9.8 考虑系统(9.40)并假设 $g(z,\alpha)$ 是连续可微的，且雅可比矩阵 $[\partial g / \partial z]$ 和 $[\partial g / \partial \alpha]$ 对于所有 $(z,\alpha)\in D\times \Gamma$ ，满足

$$\left\| \frac {\partial g}{\partial z} (z, \alpha) \right\| \leqslant L _ {1}, \quad \left\| \frac {\partial g}{\partial \alpha} (z, \alpha) \right\| \leqslant L _ {2} \| z \|$$

其中 $D = \{z\in R^n\mid \| z\| < r\}$ 。设 $k,\gamma$ 和 $r_0$ 是正常数且 $r_0 < r / k$ ，定义 $D_{0} = \{z\in R^{n}\mid \| z\| < r_{0}\}$ 。假设系统轨线满足

$$\| z (t) \| \leqslant k \| z (0) \| e ^ {- \gamma t}, \forall z (0) \in D _ {0}, \alpha \in \Gamma , t \geqslant 0$$

则存在函数 $V: D_0 \times \Gamma \to R$ 满足式(9.41)至式(9.44)。此外，如果所有假设（对于 $z$ ）全局成立，则 $V(z, \alpha)$ 在 $R^n \times \Gamma$ 上有定义，且满足式(9.41)至式(9.44)。

证明:由范数的等价性,只对2范数证明该引理即可。设 $\phi(t;z,\alpha)$ 是方程(9.40)始于 $(0,z)$ 的解,即 $\phi(0;z,\alpha)=z$ 。这种表示法强调了解对于参数 $\alpha$ 的依赖性。设

$$V (z, \alpha) = \int_ {0} ^ {T} \phi^ {\mathrm{T}} (t; z, \alpha) \phi (t; z, \alpha) d t$$

其中, $T=\ln(2k^{2})/2\gamma$ 。与定理4.14的证明相似,可以证明当 $c_{1}=[1-\exp(-2L_{1}T)]/2L_{1}$ , $c_{2}=k^{2}[1-\exp(-2\gamma T)]/2\gamma$ , $c_{3}=1/2$ 和 $c_{4}=2k\{1-\exp[-(\gamma-L_{1})T]\}/(\gamma-L_{1})$ 时, $V(z,\alpha)$ 满足式(9.41)至式(9.43)。为了证明 $V(z,\alpha)$ 满足式(9.44),注意灵敏度函数 $\phi_{\alpha}(t;z,\alpha)$ 满足灵敏度方程
