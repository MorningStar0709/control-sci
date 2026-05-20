$$V (\phi (\tau , x)) - V (x) \leqslant - \int_ {0} ^ {\tau} \psi (\phi (t; x)) d t, \forall \tau \in [ 0, \delta ]$$

利用 $V(\phi (\tau ,x))\geqslant 0$ ，得 $V(x)\geqslant \int_0^\tau \psi (\phi (t;x))dt$

现在假设存在 $\bar{x} \neq 0$ ，使 $V(\bar{x}) = 0$ ，前面的不等式表示

$$\int_ {0} ^ {\tau} \psi (\phi (t; \bar {x})) d t = 0, \forall \tau \in [ 0, \delta ] \Rightarrow \psi (\phi (t; \bar {x})) \equiv 0 \Rightarrow \phi (t; \bar {x}) \equiv 0 \Rightarrow \bar {x} = 0$$

这与 $\bar{x} \neq 0$ 的假设矛盾。因此对于所有 $x \neq 0$ ，有 $V(x) > 0$ ，该 $V(x)$ 满足作为备选李雅普诺夫函数的要求，又因为 $\dot{V}(x) \leqslant -\psi(x)$ ，可知原点是渐近稳定的。

现假设系统是严格输出无源的,并设 $V(x)$ 为其存储函数,则当 u=0 时, $\dot{V}$ 满足不等式 $\dot{V}\leqslant-y^{\mathrm{T}}\rho(y)$ ,其中对于所有 $y\neq0$ ,有 $y^{\mathrm{T}}\rho(y)>0$ 。重复先前的论证,可利用不等式证明 $V(x)$ 是正定的。特别地,对于任意 $x\in R^{n}$ ,有

$$V (x) \geqslant \int_ {0} ^ {\tau} h ^ {\mathrm{T}} (\phi (t; x), 0) \rho (h (\phi (t; x), 0)) d t$$

现假设存在 $\bar{x} \neq 0$ ，使 $V(\bar{x}) = 0$ 。前面的不等式表示

$$\int_ {0} ^ {\tau} h ^ {\mathrm{T}} (\phi (t; \bar {x}), 0) \rho (h (\phi (t; \bar {x}), 0)) d t = 0, \forall \tau \in [ 0, \delta ] \Rightarrow h (\phi (t; \bar {x}), 0) \equiv 0$$

由零状态可观测性,有

$$\phi (t; \bar {x}) \equiv 0 \Rightarrow \bar {x} = 0$$

因此对于所有 $x \neq 0$ ，有 $V(x) > 0$ 。该 $V(x)$ 可作为备选李雅普诺夫函数，且因为 $\dot{V}(x) \leqslant -y^{\mathrm{T}}\rho(y)$ 和 $y(t) \equiv 0 \Rightarrow x(t) \equiv 0$ ，由不变原理推出原点是渐近稳定的。最后，如果 $V(x)$ 是径向无界的，可分别由定理4.2和推论4.2推断出全局渐近稳定性。

例6.5 考虑一个 $p$ 输入 $-p$ 输出系统①

$$
\begin{array}{l} \dot {x} = f (x) + G (x) u \\ y = h (x) \\ \end{array}
$$

其中 $f$ 和 $G$ 是局部利普希茨的， $h$ 是连续的，且 $f(0) = 0, h(0) = 0$ 。假设存在连续可微的半正定函数 $V(x)$ ，满足

$$\frac {\partial V}{\partial x} f (x) \leqslant 0, \quad \frac {\partial V}{\partial x} G (x) = h ^ {\mathrm{T}} (x)$$

则 $u^{\mathrm{T}}y - \frac{\partial V}{\partial x} [f(x) + G(x)u] = u^{\mathrm{T}}h(x) - \frac{\partial V}{\partial x} f(x) - h^{\mathrm{T}}(x)u = -\frac{\partial V}{\partial x} f(x)\geqslant 0$

这表明系统是无源的。如果 $V(x)$ 是正定的，则可得 $\dot{x}=f(x)$ 的原点是稳定的。如果有更严格的条件

$$\frac {\partial V}{\partial x} f (x) \leqslant - k h ^ {\mathrm{T}} (x) h (x), \quad \frac {\partial V}{\partial x} G (x) = h ^ {\mathrm{T}} (x)$$

$k > 0$ ，则 $u^{\mathrm{T}}y - \frac{\partial V}{\partial x}[f(x) + G(x)u]\geqslant ky^{\mathrm{T}}y$

且系统是严格输出无源的, $\rho(y)=ky$ 。由引理6.5可知,系统是有限增益 $L_{2}$ 稳定的,且其 $L_{2}$ 增益小于或等于1/k。另外,如果系统是零状态可观测的,则 $\dot{x}=f(x)$ 的原点是渐近稳定的。进一步,如果 $V(x)$ 是径向无界的,则原点将是全局渐近稳定的。

例 6.6 考虑一个单输入-单输出系统 $^{②}$

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - a x _ {1} ^ {3} - k x _ {2} + u \\ y = x _ {2} \\ \end{array}
$$

其中 a 和 k 是正常数。仍以正定的径向无界函数 $V(x)=(1/4)ax_{1}^{4}+(1/2)x_{2}^{2}$ 作为备选存储函数。其导数 $\dot{V}$ 由下式给出：

$$\dot {V} = a x _ {1} ^ {3} x _ {2} + x _ {2} \left(- a x _ {1} ^ {3} - k x _ {2} + u\right) = - k y ^ {2} + y u$$

因此系统是严格输出无源的, $\rho(y)=ky$ 。由引理6.5可得系统是有限增益 $L_{2}$ 稳定的,其 $L_{2}$ 增益小于或等于1/k。此外当u=0时,

$$y (t) \equiv 0 \Rightarrow x _ {2} (t) \equiv 0 \Rightarrow a x _ {1} ^ {3} (t) \equiv 0 \Rightarrow x _ {1} (t) \equiv 0$$

因此系统是零状态可观测的。由引理6.7可知无激励系统在原点是全局稳定的。
