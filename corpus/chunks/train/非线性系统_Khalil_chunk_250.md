如果能证明 $\dot{x} = A(t)x$ 的原点是一致渐近稳定的，就可以应用性质 $\lim_{t\to \infty}B(t) = 0$ 证明 $\dot{x} = [A(t) + B(t)]x$ 的原点是一致渐近稳定的①，这样就把问题集中到系统 $\dot{x} = A(t)x$ 上来。再次以 $V$ 作为备选李雅普诺夫函数，得

$$
\dot {V} = \frac {a _ {m}}{k _ {p}} e _ {o} ^ {2} = - x ^ {\mathrm{T}} C ^ {\mathrm{T}} C x, \quad \text {其中} \quad C = \sqrt {\frac {- a _ {m}}{k _ {p}}} \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right]
$$

从例 8.12 可知, 若矩阵对于 $(A(t), C)$ 是一致可观测的, 则原点是一致渐近稳定的。由于对任意分段连续有界矩阵 $K(t), (A(t), C)$ 的一致可观测性等价于 $(A(t) - K(t)C, C)$ 的一致可观测性 $^{②}$ , 故取

$$
K (t) = \sqrt {\frac {k _ {p}}{- a _ {m}}} \left[ \begin{array}{l l l} a _ {m} & - \gamma r _ {\mathrm{ss}} (t) & - \gamma y _ {\mathrm{ss}} (t) \end{array} \right] ^ {\mathrm{T}}
$$

矩阵对简化为

$$
A (t) - K (t) C = \left[ \begin{array}{c c c} 0 & k _ {p} r _ {\mathrm{ss}} (t) & k _ {p} y _ {\mathrm{ss}} (t) \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], \quad C = \sqrt {\frac {- a _ {m}}{k _ {p}}} \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right]
$$

通过研究该矩阵对于给定参考信号的可观测性,可确定是否满足定理8.5的条件。例如,如果r是非零恒定信号,容易看出该矩阵对不是可观测的。这并不奇怪,因为我们已经知道在这种情况下原点不是一致渐近稳定的。另一方面,如果 $r(t)=a\sin\omega t$ ,其中a和 $\omega$ 均为正,则有 $r_{ss}(t)=r(t)$ , $y_{ss}(t)=aM\sin(\omega t+\delta)$ ,其中M和 $\delta$ 由参考模型的传递函数确定。可以验证该矩阵对是一致可观测的,因此原点 $(e_{o}=0,\phi_{1}=0,\phi_{2}=0)$ 是一致渐近稳定的,且当t趋于无穷时,参数误差 $\phi_{1}(t)$ 和 $\phi_{2}(t)$ 都收敛于零 $^{①}$ 。
