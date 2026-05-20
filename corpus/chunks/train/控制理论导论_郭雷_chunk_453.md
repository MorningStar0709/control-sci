$$
\widehat {U} ^ {\mathbf {T}} (- s) z = \left[ \begin{array}{c} U ^ {\mathbf {T}} (- s) \\ U _ {\perp} ^ {\mathbf {T}} (- s) \end{array} \right] (G _ {c} (s) w + U (s) \nu) = \left[ \begin{array}{c} U ^ {\mathbf {T}} (- s) G _ {c} (s) w + \nu \\ U _ {\perp} ^ {\mathbf {T}} (- s) G _ {c} (s) w \end{array} \right]. \tag {6.5.23}
$$

由于该系统是内部稳定的，所以 $\nu \in H_2$ 。从上式可知使 $\| z \|_2$ 为最小的 $\nu \in H_2$ 为

$$\nu = - P _ {+} U ^ {\mathrm{T}} (- s) G _ {c} (s) w.$$

因此根据假设 (6.5.19), 得

$$
\sup _ {w \in B H _ {2} +} \left\| \left[ \begin{array}{c} P _ {-} U ^ {\mathrm{T}} (- s) G _ {c} (s) w \\ U _ {\perp} ^ {\mathrm{T}} (- s) G _ {c} (s) w \end{array} \right] \right\| _ {2} = \sup _ {w \in B H _ {2} +} \left\| \left[ \begin{array}{c} P _ {-} U ^ {\mathrm{T}} (- s) G _ {c} (s) \\ U _ {\perp} ^ {\mathrm{T}} (- s) G _ {c} (s) \end{array} \right] w \right\| _ {2} <   1. \tag {6.5.24}
$$

定义 Hankel-Toeplitz 混合算子 $\Gamma : \begin{bmatrix} H_2^\perp \\ L_2 \end{bmatrix} \to H_2$ 及其共轭算子 $\Gamma^* : H_2 \to \begin{bmatrix} H_2^\perp \\ L_2 \end{bmatrix}$ 为

$$
\begin{array}{l} \Gamma \left[ \begin{array}{l} q _ {1} \\ q _ {2} \end{array} \right] = P _ {+} \left[ G _ {c} ^ {\mathrm{T}} (- s) U (s) P _ {-} G _ {c} ^ {\mathrm{T}} (- s) U _ {\perp} (s) \right] \left[ \begin{array}{l} q _ {1} \\ q _ {2} \end{array} \right] \\ = P _ {+} \left[ G _ {c} ^ {\mathrm{T}} (- s) U (s) G _ {c} ^ {\mathrm{T}} (- s) U _ {\perp} (s) \right] \left[ \begin{array}{l} q _ {1} \\ q _ {2} \end{array} \right], \tag {6.5.25} \\ \end{array}

\Gamma^ {*} w = \left[ \begin{array}{c} P _ {-} U ^ {\mathrm{T}} (- s) G _ {c} (s) \\ U _ {\perp} ^ {\mathrm{T}} (- s) G _ {c} (s) \end{array} \right] w = \left[ \begin{array}{c} P _ {-} U ^ {\mathrm{T}} (- s) G _ {c} (s) P _ {+} \\ U _ {\perp} ^ {\mathrm{T}} (- s) G _ {c} (s) P _ {+} \end{array} \right] w. \tag {6.5.26}
$$

可以验证 $G_{c}^{\mathrm{T}}(-s)U(s)$ 和 $G_{c}^{\mathrm{T}}(-s)U_{\perp}(s)$ 的状态空间实现分别为

$$G _ {c} ^ {\mathrm{T}} (- s) U (s) = \left\{A _ {F}, B _ {2}, B _ {1} ^ {\mathrm{T}} X _ {0}, 0 \right\},G _ {c} ^ {\mathrm{T}} (- s) U _ {\perp} (s) = \left\{A _ {F}, - X _ {0} ^ {- 1} C _ {1} ^ {\mathrm{T}} D _ {\perp}, B _ {1} ^ {\mathrm{T}} X _ {0}, 0 \right\}.$$

实际上，式(6.5.24)意味着

$$\sup _ {w \in B H _ {2}} | | \Gamma^ {*} w | | _ {2} < 1.$$

于是其共轭算子 $\Gamma$ 也满足

$$\sup _ {\| q \| _ {2} \leqslant 1} | | \Gamma q | | _ {2} < 1.$$

因此根据引理6.5.4可知Riccati方程

$$W A _ {F} + A _ {F} ^ {\mathrm{T}} W + W X _ {0} ^ {- 1} C _ {1} ^ {\mathrm{T}} D _ {\perp} D _ {\perp} ^ {\mathrm{T}} C _ {1} X _ {0} ^ {- 1} W + X _ {0} B _ {1} B _ {1} ^ {\mathrm{T}} X _ {0} = 0 \tag {6.5.27}$$
