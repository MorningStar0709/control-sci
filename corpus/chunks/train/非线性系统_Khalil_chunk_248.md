$$V (\tau , x (\tau)) \leqslant V (t, x (t)), \forall \tau \in [ t, t + \delta ]$$

对于任意 $t \geqslant t_0$ ，设 $N$ 是满足 $t \leqslant t_0 + N\delta$ 的最小正整数。将区间 $[t_0, t_0 + (N - 1)\delta]$ 等分为 $(N - 1)$ 个长为 $\delta$ 的子区间，则有

$$
\begin{array}{l} V (t, x (t)) \leqslant V \left(t _ {0} + (N - 1) \delta , x \left(t _ {0} + (N - 1) \delta\right)\right) \\ \leqslant (1 - \lambda) V \left(t _ {0} + (N - 2) \delta , x \left(t _ {0} + (N - 2) \delta\right)\right) \\ \begin{array}{c} \bullet \\ \vdots \\ \bullet \end{array} \\ \leqslant (1 - \lambda) ^ {(N - 1)} V \left(t _ {0}, x \left(t _ {0}\right)\right) \\ \leqslant \frac {1}{(1 - \lambda)} (1 - \lambda) ^ {(t - t _ {0}) / \delta} V \left(t _ {0}, x \left(t _ {0}\right)\right) \\ = \frac {1}{(1 - \lambda)} e ^ {- b (t - t _ {0})} V \left(t _ {0}, x \left(t _ {0}\right)\right) \\ \end{array}
$$

其中 $b=\frac{1}{\delta}\ln\frac{1}{(1-\lambda)}$

取 $\sigma(r,s)=\frac{r}{(1-\lambda)}e^{-bs}$

容易看出, $\sigma(r,s)$ 是一个KL类函数,且 $V(t,x(t))$ 满足

$$V (t, x (t)) \leqslant \sigma (V (t _ {0}, x (t _ {0})), t - t _ {0}), \forall V (t _ {0}, x (t _ {0})) \in [ 0, \rho ]$$

此后的证明与定理4.9的证明完全相同,关于所述全局一致渐近稳定性和指数稳定性的证明与定理4.9和定理4.10的证明相同。

例 8.11 考虑线性时变系统

$$\dot {x} = A (t) x$$

其中对于所有 $t \geqslant 0, A(t)$ 是连续的。假设存在一个连续可微的对称矩阵 $P(t)$ ，满足

$$0 < c _ {1} I \leqslant P (t) \leqslant c _ {2} I, \forall t \geqslant 0$$

以及矩阵微分方程 $-\dot{P}(t)=P(t)A(t)+A^{\mathrm{T}}(t)P(t)+C^{\mathrm{T}}(t)C(t)$

其中 $C(t)$ 对 t 是连续的。二次函数

$$V (t, x) = x ^ {\mathrm{T}} P (t) x$$

沿系统轨线的导数为 $\dot{V}(t,x)=-x^{\mathrm{T}}C^{\mathrm{T}}(t)C(t)x\leqslant0$

则线性系统的解可由 $\phi(\tau;t,x)=\Phi(\tau,t)x$ 给出,其中 $\Phi(\tau,t)$ 是状态转移矩阵。因此有

$$
\begin{array}{l} V (t + \delta , \phi (t + \delta ; t, x)) - V (t, x) = \int_ {t} ^ {t + \delta} \dot {V} (\tau , \phi (\tau ; t, x)) d \tau \\ = - x ^ {\mathrm{T}} \int_ {t} ^ {t + \delta} \Phi^ {\mathrm{T}} (\tau , t) C ^ {\mathrm{T}} (\tau) C (\tau) \Phi (\tau , t) d \tau x \\ = - x ^ {T} W (t, t + \delta) x \\ \end{array}
$$

其中 $W(t,t + \delta) = \int_t^{t + \delta}\Phi^{\mathrm{T}}(\tau ,t)C^{\mathrm{T}}(\tau)C(\tau)\Phi (\tau ,t)d\tau$

假设存在一个正常数 $k < c_{2}$ ，使得

$$W (t, t + \delta) \geqslant k I, \forall t \geqslant 0$$

则有 $V(t + \delta, \phi(t + \delta; t, x)) - V(t, x) \leqslant -k \| x\| _2^2 \leqslant -\frac{k}{c_2} V(t, x)$

这样当 $W_{i}(x) = c_{i}\| x\|_{2}^{2}, i = 1,2,\lambda = \frac{k}{c_{2}} < 1$
