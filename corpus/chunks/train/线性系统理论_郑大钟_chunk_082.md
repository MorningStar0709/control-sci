$$
\begin{array}{l} \bar {A} (t) = [ P (t) A (t) + \dot {P} (t) ] P ^ {- 1} (t) \\ = \left[ e ^ {2 t} \Psi^ {- 1} (t) A (t) + \bar {A} e ^ {2 t} \Psi^ {- 1} (t) + e ^ {2 t} \Psi^ {- 1} (t) \right] \Psi (t) e ^ {- 2 t} \\ = \bar {A} + \left[ e ^ {2 t} \Psi^ {- 1} (t) A (t) - e ^ {2 t} \Psi^ {- 1} (t) A (t) \right] \Psi (t) e ^ {- 2 t} \\ = \overline {{{A}}} \tag {2.131} \\ \end{array}
$$

就证明了关系式(2.130)。

(5) $A(\cdot)$ 为周期变化的线性时变系统 (2.118) 和变换后的系统 (2.130) 是李亚普诺夫意义下等价的, 也即 (2.118) 为渐近稳定的充分必要条件为 $\overline{A}$ 的特征值均具有负实部。

这个论断可证明如下：由（2.129）定义的变换阵 $P(t)$ 为非奇异，且由（2.129）和(2.121)有

$$
\begin{array}{l} P (t + T) = e ^ {\lambda (t + T)} \Psi^ {- 1} (t + T) = e ^ {\lambda t} e ^ {\lambda T} e ^ {- \lambda T} \Psi^ {- 1} (t) \\ = e ^ {2 t} \Psi^ {- 1} (t) = P (t) \tag {2.132} \\ \end{array}
$$

表明 $P(t)$ 也是周期的，因此为有界。从而 $P(t)$ 为李亚普诺夫变换阵，而 $(\overline{A}, P(t)B(t), C(t)P^{-1}(t), D(t))$ 和 $(A(t), B(t), C(t), D(t))$ 是李亚普诺夫意义下等价的，且两者具有相同的稳定性。
