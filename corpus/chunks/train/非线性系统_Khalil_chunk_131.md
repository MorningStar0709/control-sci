尽管定理4.11并不非常有助于稳定性测试，但随后会看到它保证了线性系统(4.29)存在李雅普诺夫函数。在例4.21中看到，如果能找到一个正定有界矩阵 $P(t)$ ，对于某个正定矩阵 $Q(t)$ ，满足微分方程(4.28)，那么 $V(t,x) = x^{\mathrm{T}}P(t)x$ 就是系统的李雅普诺夫函数。如果矩阵 $Q(t)$ 除正定以外还是有界的，即

$$0 < c _ {3} I \leqslant Q (t) \leqslant c _ {4} I, \forall t \geqslant 0$$

且如果 $A(t)$ 连续有界, 则可以证明: 如果原点是渐近指数稳定的, 则系统(4.28)的解具有期望的特性。

定理4.12 设 $x = 0$ 是系统(4.29)的指数稳定平衡点。假设 $A(t)$ 连续且有界。设 $Q(t)$ 是连续且有界的正定对称矩阵，那么存在一个连续可微的正定对称矩阵 $P(t)$ ，满足方程(4.28)。因此， $V(t,x) = x^{\mathrm{T}}P(t)x$ 是系统的李雅普诺夫函数，满足定理4.10的条件。

证明:设 $P(t)=\int_{t}^{\infty}\Phi^{\mathrm{T}}(\tau,t)Q(\tau)\Phi(\tau,t)d\tau$

$\phi(\tau;t,x)$ 是系统(4.29)始于 $(t,x)$ 的解。由于系统是线性的, $\phi(\tau;t,x)=\Phi(\tau,t)x$ 。按照 $P(t)$ 的定义,有

$$x ^ {\mathrm{T}} P (t) x = \int_ {t} ^ {\infty} \phi^ {\mathrm{T}} (\tau ; t, x) Q (\tau) \phi (\tau ; t, x) d \tau$$

利用式(4.30)可得

$$
\begin{array}{l} x ^ {\mathrm{T}} P (t) x \leqslant \int_ {t} ^ {\infty} c _ {4} \| \Phi (\tau , t) \| _ {2} ^ {2} \| x \| _ {2} ^ {2} d \tau \\ \leqslant \int_ {t} ^ {\infty} k ^ {2} e ^ {- 2 \lambda (\tau - t)} d \tau c _ {4} \| x \| _ {2} ^ {2} = \frac {k ^ {2} c _ {4}}{2 \lambda} \| x \| _ {2} ^ {2} \stackrel {\text { def }} {=} c _ {2} \| x \| _ {2} ^ {2} \\ \end{array}
$$

另一方面,由于 $\|A(t)\|_{2}\leqslant L,\quad\forall t\geqslant0$

解 $\phi(\tau;t,x)$ 是下方有界的(见习题3.17)，

$$\| \phi (\tau ; t, x) \| _ {2} ^ {2} \geqslant \| x \| _ {2} ^ {2} e ^ {- 2 L (\tau - t)}$$

因此 $x^{\mathrm{T}}P(t)x\geqslant \int_{t}^{\infty}c_{3}\| \phi (\tau ;t,x)\|_{2}^{2}d\tau$

$$\geqslant \int_ {t} ^ {\infty} e ^ {- 2 L (\tau - t)} d \tau c _ {3} \| x \| _ {2} ^ {2} = \frac {c _ {3}}{2 L} \| x \| _ {2} ^ {2} \stackrel {{\mathrm{def}}} {{=}} c _ {1} \| x \| _ {2} ^ {2}$$

这样 $c_{1}\| x\|_{2}^{2}\leqslant x^{\mathrm{T}}P(t)x\leqslant c_{2}\| x\|_{2}^{2}$

说明 $P(t)$ 是正定且有界的。 $P(t)$ 的定义说明 $P(t)$ 对称且连续可微。通过对 $P(t)$ 求微分，并利用性质

$$\frac {\partial}{\partial t} \Phi (\tau , t) = - \Phi (\tau , t) A (t)$$

可证明 $P(t)$ 满足方程(4.28)。特别只有

$$
\begin{array}{l} \dot {P} (t) = \int_ {t} ^ {\infty} \Phi^ {\mathrm{T}} (\tau , t) Q (\tau) \frac {\partial}{\partial t} \Phi (\tau , t) d \tau \\ + \int_ {t} ^ {\infty} \left[ \frac {\partial}{\partial t} \Phi^ {T} (\tau , t) \right] Q (\tau) \Phi (\tau , t) d \tau - Q (t) \\ = - \int_ {t} ^ {\infty} \Phi^ {T} (\tau , t) Q (\tau) \Phi (\tau , t) d \tau A (t) \\ - A ^ {\mathrm{T}} (t) \int_ {t} ^ {\infty} \Phi^ {\mathrm{T}} (\tau , t) Q (\tau) \Phi (\tau , t) d \tau - Q (t) \\ = - P (t) A (t) - A ^ {\mathrm{T}} (t) P (t) - Q (t) \\ \end{array}
$$
