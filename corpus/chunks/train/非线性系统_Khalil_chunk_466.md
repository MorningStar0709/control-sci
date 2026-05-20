$$| \gamma (x) [ \hat {\alpha} (x) - \alpha (x) ] | \leqslant \rho_ {0} (x), \quad \left| \frac {\gamma (x) - \hat {\gamma} (x)}{\hat {\gamma} (x)} \right| \leqslant k < 1$$

其中函数 $\rho_0(x)$ 和常数 $k$ 已知。设 $r(t)$ 是参考信号并假设 $r$ 及其到 $r^{(\rho)}$ 导数都是连续且有界的。应用李雅普诺夫再设计,设计一个连续状态反馈控制器,使输出 y 渐近跟踪 r,预先给定容差为 $\mu$ ,即对于某个有限时间 T,对于所有 $t \geqslant T$ ,有 $|y(t) - r(t)| \leqslant \mu$ 。

14.19 在参考信号为常数时,利用积分控制重新设计上一题,并验证调节误差收敛到零。

14.20 考虑系统 $\dot{x}_1 = x_2, \quad \dot{x}_2 = u + \delta(x)$

其中 $\delta$ 未知，但已知估计值 $\rho_{1}$ 满足 $|\delta (x)|\leqslant \rho_1\| x\| _2$ ，设 $u = \psi (x) = -x_{1} - x_{2}$ 为标称稳定控制，且

$$
v = \left\{ \begin{array}{l l} - \rho_ {1} \| x \| _ {2} (w / \| w \| _ {2}), & \rho_ {1} \| x \| _ {2} \| w \| _ {2} \geqslant \varepsilon \\ - \rho_ {1} ^ {2} \| x \| _ {2} ^ {2} (w / \varepsilon), & \rho_ {1} \| x \| _ {2} \| w \| _ {2} <   \varepsilon \end{array} \right.
$$

其中 $w^{T}=2x^{T}PB$ ，且 $V(x)=x^{T}Px$ 是标称闭环系统的李雅普诺夫函数。采用控制律 $u=-x_{1}-x_{2}+v$ 。

(a) 验证在推论 14.1 的所有假设中, 除式(14.45) 在 $\eta_{0}=0$ 时成立外, 其余假设都成立。

(b) 证明当 $\delta(x)=2(x_{1}+x_{2}),\rho_{1}=2\sqrt{2}$ 时，原点是不稳定的。

14.21 假设式(14.33)至式(14.35)在 $\| \cdot \|_{\infty}$ 下成立,考察对不连续控制(14.40)的连续逼近

$$
v _ {i} = \left\{ \begin{array}{l l} - \eta (t, x) \operatorname{sgn} (w _ {i}), & \eta (t, x) | w _ {i} | \geqslant \varepsilon \\ - \eta^ {2} (t, x) (w _ {i} / \varepsilon), & \eta (t, x) | w _ {i} | <   \varepsilon \end{array} \right.
$$

$i=1,2,\cdots,p$ ,并且 $w^{T}=\left[\partial V/\partial x\right]G(t,x)$ 。

(a) 证明如果 $\eta(t, x) |w_i| < \varepsilon$ ，则

$$\dot {V} \leqslant - \alpha_ {3} (\| x \| _ {\infty}) + \sum_ {i \in I} \left[ \eta (t, x) | w _ {i} | - \frac {\eta^ {2} (t , x) | w _ {i} | ^ {2}}{\varepsilon} \right]$$

其中 $i \in I$ 。

(b) 对当前控制器, 叙述并证明一个类似于定理 14.3 的定理。

14.22 考察习题 14.21 的控制器, 希望证明类似于推论 14.1 的结论。假设 $\alpha_{3}(\|x\|_{\infty}) \geqslant \phi^{2}(x), \eta(t,x) \geqslant \eta_{0} > 0$ , 且

$$| \delta_ {i} | \leqslant \rho_ {1} \phi (x) + \kappa_ {0} | v _ {i} |, 0 \leqslant \kappa_ {0} < 1$$

$i=1,2,\cdots,p$ 。这些不等式说明式(14.35)在 $\|\cdot\|_{\infty}$ 下成立，但条件更为严格，因为 $|\delta_{i}|$ 的上界取决于 $|v_{i}|$ 。

(a) 证明 $\dot{V} \leqslant -\phi^2(x) + \sum_{i \in I} \left\{-(1 - \kappa_0)\eta_0^2\frac{|w_i|^2}{\varepsilon} + \rho_1\phi(x)|w_i|\right\}$

(b) 叙述并证明类似于推论 14.1 的结论。

14.23 假设不等式(14.35)取为

$$\| \delta (t, x, \psi (t, x) + v) \| _ {2} \leqslant \rho_ {0} + \rho_ {1} \phi (x) + \kappa_ {0} \| v \| _ {2}, \quad 0 \leqslant \kappa_ {0} < 1$$
