# 4.6 线性时变系统和线性化

对于线性时变系统 $\dot{x}(t)=A(t)x(t)$ (4.29)

作为系统平衡点的原点,其稳定性完全可以由系统的状态转移矩阵描述。由线性系统理论 $^{①}$ 可知,方程(4.29)的解为

$$x (t) = \Phi (t, t _ {0}) x (t _ {0})$$

其中， $\Phi(t,t_{0})$ 是状态转移矩阵。下一个定理将根据 $\Phi(t,t_{0})$ 给出一致渐近稳定性的特征。

定理 4.11 当且仅当对于正常数 k 和 $\lambda$ ，状态转移矩阵满足不等式

$$\| \Phi (t, t _ {0}) \| \leqslant k e ^ {- \lambda (t - t _ {0})}, \forall t \geqslant t _ {0} \geqslant 0 \tag {4.30}$$

时,系统(4.29)的平衡点x=0是(全局)一致渐近稳定的。

证明:由于 $x(t)$ 与 $x(t_{0})$ 线性相关,如果原点是一致渐近稳定的,则也是全局一致渐近稳定的。式(4.30)的充分性是显然的,因为

$$\| x (t) \| \leqslant \| \Phi (t, t _ {0}) \| \| x (t _ {0}) \| \leqslant k \| x (t _ {0}) \| e ^ {- \lambda (t - t _ {0})}$$

为了证明必要性,假设原点是一致渐近稳定的,那么存在一个 $\kappa\mathcal{L}$ 类函数 $\beta$ ,满足

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0}), \forall t \geqslant t _ {0}, \forall x (t _ {0}) \in R ^ {n}$$

由导出阵模的定义(见附录 A), 有

$$\| \Phi (t, t _ {0}) \| = \max _ {\| x \| = 1} \| \Phi (t, t _ {0}) x \| \leqslant \max _ {\| x \| = 1} \beta (\| x \|, t - t _ {0}) = \beta (1, t - t _ {0})$$

由于 $\beta (1,s)\to 0$ ，当 $s\to \infty$

存在 $T > 0$ ，满足 $\beta (1,T)\leqslant 1 / e$ 。对于任何 $t\geqslant t_0$ ，设 $N$ 是满足 $t\leqslant t_0 + NT$ 的最小正整数。将区间 $[t_0,t_0 + (N - 1)T]$ 分为 $N - 1$ 个长度为 $T$ 的子区间，利用 $\Phi (t,t_0)$ 的转移特性，有

$$
\Phi (t, t _ {0}) = \Phi (t, t _ {0} + (N - 1) T) \Phi (t _ {0} + (N - 1) T, t _ {0} + (N - 2) T) \dots \Phi (t _ {0} + T, t _ {0})
\begin{array}{l} \| \Phi (t, t _ {0}) \| \leqslant \| \Phi (t, t _ {0} + (N - 1) T) \| \prod_ {k = 1} ^ {k = N - 1} \| \Phi (t _ {0} + k T, t _ {0} + (k - 1) T) \| \\ \leqslant \beta (1, 0) \prod_ {k = 1} ^ {k = N - 1} \frac {1}{e} = e \beta (1, 0) e ^ {- N} \\ \leqslant e \beta (1, 0) e ^ {- (t - t _ {0}) / T} = k e ^ {- \lambda (t - t _ {0})} \\ \end{array}
$$

因此，

其中 $k = e\beta (1,0),\lambda = 1 / T_{\circ}$

定理4.11说明,在线性系统中,原点的一致渐近稳定与指数稳定是等价的。尽管不等式(4.30)无须找李雅普诺夫函数就给出了原点一致渐近稳定的特征,但更常用的是线性时不变系统中的特征值标准,因为要知道状态转移矩阵 $\Phi(t,t_{0})$ ,需要解状态方程(4.29)。注意,对于线性时变系统,一致渐近稳定性不能由矩阵A的特征值位置描述 $^{①}$ ,如下例所示。

例4.22 考虑矩阵为 $A(t) = \left[ \begin{array}{ll} - 1 + 1.5\cos^2 t & 1 - 1.5\sin t\cos t\\ -1 - 1.5\sin t\cos t & -1 + 1.5\sin^2 t \end{array} \right]$

的二阶线性系统。对于任何 $t, A(t)$ 的特征值均为 $-0.25 \pm 0.25\sqrt{7}j$ 。因此，特征值与 $t$ 无关，且位于左半开平面内。但是，原点是不稳定的，证明如下：

$$
\Phi (t, 0) = \left[ \begin{array}{l l} e ^ {0. 5 t} \cos t & e ^ {- t} \sin t \\ - e ^ {0. 5 t} \sin t & e ^ {- t} \cos t \end{array} \right]
$$

说明存在任意接近原点的初始状态 $x(0)$ ，使解无界且趋于无穷。
