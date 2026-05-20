# 8.3 类不变定理

在自治系统情况下, LaSalle 不变定理(定理 4.4)说明在 E 中系统轨线趋向最大的不变集, 其中 E 是使得 $\dot{V}(x)=0$ 的集合 $\Omega$ 内所有点的集合。在非自治系统情况下, 由于 $\dot{V}(t,x)$ 是 t 和 x 的函数, 所以很难确定集合 E。如果能证明

$$\dot {V} (t, x) \leqslant - W (x) \leqslant 0$$

问题将得以简化,因为可以把集合 E 定义为所有使 $W(x)=0$ 的点的集合。我们希望当 $t\to\infty$ 时,系统的轨线趋于集合 E,这基本上就是下一个定理。在叙述该定理之前,先介绍一个用于定理证明的引理,称为 Barbalat 引理。

引理8.2 设 $\phi: R \to R$ 是 $[0, \infty)$ 上的一致连续函数。假设 $\lim_{t \to \infty} \int_{0}^{t} \phi(\tau) d\tau$ 存在且有限，则

$$\phi (t) \to 0 \quad {\text {当}} t \to \infty$$

证明:如果上述结论不成立,则存在一个正常数 $k_{1}$ ,使得对于每个 T>0,都可以找到 $T_{1}\geqslant T$ ,满足 $\left|\phi(T_{1})\right| \geqslant k_{1}$ 。因为 $\phi(t)$ 是一致连续的,所以存在正常数 $k_{2}$ ,使得对于所有 $t\geqslant0$ 和 $0\leqslant\tau\leqslant k_{2}$ ,有 $\left|\phi(t+\tau)-\phi(t)\right|<k_{1}/2$ 。从而

$$
\begin{array}{l} \left| \phi (t) \right| = \left| \phi (t) - \phi \left(T _ {1}\right) + \phi \left(T _ {1}\right) \right| \\ \geqslant | \phi (T _ {1}) | - | \phi (t) - \phi (T _ {1}) | \\ > k _ {1} - \frac {1}{2} k _ {1} = \frac {1}{2} k _ {1}, \forall t \in \left[ T _ {1}, T _ {1} + k _ {2} \right] \\ \end{array}
$$

因此

$$\left| \int_ {T _ {1}} ^ {T _ {1} + k _ {2}} \phi (t) d t \right| = \int_ {T _ {1}} ^ {T _ {1} + k _ {2}} | \phi (t) | d t > \frac {1}{2} k _ {1} k _ {2}$$

式中等号成立是因为 $\phi(t)$ 在 $T_{1} \leqslant t \leqslant T_{1} + k_{2}$ 时符号不变。这样当 $t$ 趋于无穷时， $\int_{0}^{t} \phi(\tau) d\tau$ 不能收敛到有限值，与假设矛盾。

定理8.4 设 $D \subset R^n$ 是包含 $x = 0$ 的定义域, 假设函数 $f(t, x)$ 在 $[0, \infty) \times D$ 上对 $t$ 是分段连续的, 对 $x$ 是局部利普希茨的, 对 $t$ 一致。进一步假设对于所有 $t \geqslant 0$ , $f(t, 0)$ 一致有界。设 $V: [0, \infty) \times D \to R$ 是连续可微函数, 使得 $\forall t \geqslant 0, \forall x \in D$ , 满足

$$
\begin{array}{l} W _ {1} (x) \leqslant V (t, x) \leqslant W _ {2} (x) \\ \dot {V} (t, x) = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant - W (x) \\ \end{array}
$$

其中， $W_{1}(x)$ 和 $W_{2}(x)$ 是 $D$ 上的连续正定函数， $W(x)$ 是 $D$ 上的连续半正定函数。选择 $r > 0$ 使 $B_{r}\subset D$ ，并设 $\rho <   \min_{\| x\| = r}W_1(x)$ ，则 $\dot{x} = f(t,x)$ 的所有满足 $x(t_0)\in \{x\in B_r|$ $W_{2}(x)\leqslant \rho \}$ 的解都是有界的，且满足当 $t$ 趋于无穷时

$$W (x (t)) \rightarrow 0$$

此外,如果所有假设全局成立,且 $W_{1}(x)$ 是径向无界的,则上述结论对于所有 $x(t_{0}) \in R^{n}$ 都成立。

证明: 类似定理 4.8 的证明, 可以证明

$$x (t _ {0}) \in \{x \in B _ {r} \mid W _ {2} (x) \leqslant \rho \} \Rightarrow x (t) \in \Omega_ {t, \rho} \subset \{x \in B _ {r} \mid W _ {1} (x) \leqslant \rho \}, \forall t \geqslant t _ {0}$$
