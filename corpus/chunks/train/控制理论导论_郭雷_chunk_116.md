$$
\left[ \begin{array}{c} \dot {\overline {{x}}} (t) \\ \dot {e} (t) \end{array} \right] = \left[ \begin{array}{c c} \overline {{A}} & 0 \\ 0 & \overline {{A}} _ {2 2} - G _ {2} \overline {{A}} _ {1 2} \end{array} \right] \left[ \begin{array}{c} \overline {{x}} (t) \\ e (t) \end{array} \right] + \left[ \begin{array}{c} \overline {{B}} \\ 0 \end{array} \right] u (t).
$$

注意到 $P^{-1} = \left[ \begin{array}{cc}C_1^{-1} & C_1^{-1}C_2\\ 0 & I_{n - m} \end{array} \right]$ 及 $e = [-G_2I_{n - m}]Px - x_c$ ，由式(1.8.21）可得

$$
\begin{array}{l} u (t) = \left[ \begin{array}{l l} \boldsymbol {F} & \boldsymbol {F} _ {c} \end{array} \right] \left[ \begin{array}{l} y (t) \\ x _ {c} (t) \end{array} \right] \\ = K \left[ \begin{array}{c c} C _ {1} ^ {- 1} (I _ {m} - C _ {2} G _ {2}) & - C _ {1} ^ {- 1} C _ {2} \\ G _ {2} & I _ {n - m} \end{array} \right] \left[ \begin{array}{c} y (t) \\ x _ {c} (t) \end{array} \right] \\ = K P ^ {- 1} \left[ \begin{array}{c c} I _ {m} & 0 \\ G _ {2} & I _ {n - m} \end{array} \right] \left[ \begin{array}{l} y (t) \\ x _ {c} (t) \end{array} \right] \\ = K P ^ {- 1} \left[ \begin{array}{c c} I _ {m} & 0 \\ G _ {2} & I _ {n - m} \end{array} \right] \left[ \begin{array}{c c} C _ {1} & C _ {2} \\ - G _ {2} C _ {1} & I _ {n - m} - C _ {2} G _ {2} \end{array} \right] x (t) \\ - K P ^ {- 1} \left[ \begin{array}{c c} I _ {m} & 0 \\ G _ {2} & I _ {n - m} \end{array} \right] \left[ \begin{array}{c} 0 \\ c (t) \end{array} \right] \\ = K P ^ {- 1} \left[ \begin{array}{c c} C _ {1} & C _ {2} \\ 0 & I _ {n - m} \end{array} \right] x (t) - K \left[ \begin{array}{c} - C _ {1} ^ {- 1} C _ {2} \\ I _ {n - m} \end{array} \right] e (t) \\ = K x (t) - F _ {c} e (t) = K P ^ {- 1} \bar {x} (t) - F _ {c} e (t), \\ \end{array}
$$

因此有

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {\overline {{{x}}}} (t) \\ \dot {e} (t) \end{array} \right] = \left[ \begin{array}{c c} \overline {{{A}}} + \overline {{{B K}}} & - \overline {{{B}}} F _ {c} \\ 0 & \overline {{{A}}} _ {2 2} - G _ {2} \overline {{{A}}} _ {1 2} \end{array} \right] \left[ \begin{array}{c} \overline {{{x}}} (t) \\ e (t) \end{array} \right],} \\ y (t) = [ I _ {m} \quad 0 ]   \overline {{{x}}} (t), \end{array} \right. \tag {1.8.28}
$$

其中 $\overline{K} = KP^{-1}$

显然 $\sigma(\overline{A} + \overline{B K}) = \sigma(A + B K) \subset \mathbb{C}^{-}$ ，又由 $\sigma(\overline{A}_{22} - G_2\overline{A}_{12}) \subset \mathbb{C}^{-}$ 知系统 (1.8.28) 是输出调节的。由于这个系统与闭环系统 (1.8.27) 代数等价，因此
