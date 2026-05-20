推论 14.1 特别适用于当标称闭环系统(14.32)的原点是指数稳定的,扰动 $\delta(t,x,u)$ 对 x 和 u 都是利普希茨的,且在 $(x=0,u=0)$ 处为零时的情况。此时, $\phi(x)$ 正比于 $\|x\|_{2}$ ,且当 $\rho(x)$ 满足式(14.46)时,不确定项满足式(14.35)。通常,条件(14.46)可能比在原点处扰动为零的要求更高,例如,在标量情况下,如果 $\phi(x)=|x|^{3}$ ,则扰动项 x 的边界不可能是 $\rho_{1}\phi(x)$ 。

推论 14.1 的稳定性结果取决于 $\eta$ 的选择是否满足式 (14.45)。可以证明（见习题 14.20），如果 $\eta$ 不满足式 (14.45)，则反馈控制可能不会稳定原点。当 $\eta$ 满足式 (14.45) 时，反馈控制律 (14.41) 在 $\eta \parallel w \parallel_{2} < \varepsilon$ 区域内是高增益反馈控制律 $v = -kw, k \geqslant \eta_{0}^{2}/\varepsilon$ ，当式 (14.44) 到式 (14.46) 成立时，该高增益反馈控制律可稳定原点（见习题 14.24）。

例 14.4 现在继续例 14.3 关于可反馈线性化系统的讨论。假设不等式(14.36)在 $\|\cdot\|_{2}$ 下成立, 进一步假设对于所有 $z \in B_{r} \subset D_{z}$ , 有

$$\left\| \Delta_ {1} (x) + \Delta_ {2} (x) \alpha (x) - \Delta_ {2} (x) \gamma^ {- 1} (x) K z \right\| _ {2} \leqslant \rho_ {1} \| z \| _ {2}$$

则当 $\rho = \rho_{1}\| z\|_{2}$ 时，式(14.37)成立。按照式(14.41)取控制律 $v$ ，其中

$$\eta = 1 + \frac {\rho_ {1} \| z \| _ {2}}{(1 - \kappa_ {0})}, \quad w ^ {\mathrm{T}} = 2 z ^ {\mathrm{T}} P B, \quad \varepsilon < \min \left\{\frac {2 (1 - \kappa_ {0})}{\rho_ {1} ^ {2}}, \frac {2 r ^ {2} \lambda_ {\min} (P)}{(1 - \kappa_ {0}) \lambda_ {\max} (P)} \right\}$$

可以验证当 $\alpha_{1}(r)=\lambda_{\min}(P)r^{2},\alpha_{2}(r)=\lambda_{\max}(P)r^{2},\alpha_{3}(r)=r^{2},\phi(z)=\|z\|_{2}$ 和 a=r 时，定理 14.3 和推论 14.1 的所有假设都成立。这样，在全部反馈控制 $u=\psi(x)+v$ 下，闭环扰动系统的原点是指数稳定的。如果所有假设全局成立，且 $T(x)$ 是全局微分同胚的，则原点 $x = 0$ 就是全局渐近稳定的①。

例14.5 重新考虑例13.18中当 $\delta_{1} = \pi$ 时的单摆方程

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = a \sin x _ {1} - b x _ {2} + c u \\ \end{array}
$$

我们想要在开环平衡点 x=0 处稳定单摆。当 $T(x)=x$ 时，系统是可反馈线性化系统，标称稳定反馈控制可取为

$$\psi (x) = - \left(\frac {\hat {a}}{\hat {c}}\right) \sin x _ {1} - \left(\frac {1}{\hat {c}}\right) (k _ {1} x _ {1} + k _ {2} x _ {2})$$

其中 $\hat{a}$ 和 $\hat{c}$ 分别是 $a$ 和 $c$ 的标称值，且选择 $k_{1}$ 和 $k_{2}$ ，使

$$
A - B K = \left[ \begin{array}{c c} 0 & 1 \\ - k _ {1} & - (k _ {2} + b) \end{array} \right]
$$

为赫尔维茨矩阵。对于 $u = \psi(x) + v$ ，不确定项 $\delta$ 由下式给出：

$$\delta = \frac {1}{\hat {c}} \left[ \left(\frac {a \hat {c} - \hat {a} c}{\hat {c}}\right) \sin x _ {1} - \left(\frac {c - \hat {c}}{\hat {c}}\right) (k _ {1} x _ {1} + k _ {2} x _ {2}) \right] + \left(\frac {c - \hat {c}}{\hat {c}}\right) v$$

因此 $|\delta| \leqslant \rho_1 \| x \|_2 + \kappa_0 |v|$ , $\forall x \in R^2 \forall v \in R$
