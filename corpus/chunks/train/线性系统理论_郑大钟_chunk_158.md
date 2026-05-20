现选取一个 $x_0$ ，使成立 $\| x_0 \| = \delta$ 和 $\| \Phi(t_0 + T, t_0) x_0 \| = \| \Phi(t_0 + T, t_0) \| \| x_0 \|$ ，同时取 $\mu = \delta / 2$ ，则由（4.69）可进而导出：

$$\left\| \Phi \left(t _ {0} + T, t _ {0}\right) \right\| \leqslant \frac {1}{2}, \quad \forall t _ {0} > 0 \tag {4.70}$$

于是，利用（4.68）和（4.70），得到

$$\| \Phi (t, t _ {0}) \| \leqslant k _ {3}, \quad \forall t \in [ t _ {0}, t _ {0} + T) \tag {4.71}\left\| \Phi (t, t _ {0}) \right\| = \left\| \Phi (t, t _ {0} + T) \Phi (t _ {0} + T, t _ {0}) \right\|\leqslant \| \Phi (t, t _ {0} + T) \| \| \Phi (t _ {0} + T, t _ {0}) \| \leqslant \frac {k _ {3}}{2}\forall t \in [ t _ {0} + T, t _ {0} + 2 T) \tag {4.72}\left\| \Phi (t, t _ {0}) \right\| \leqslant \left\| \Phi (t, t _ {0} + 2 T) \right\| \left\| \Phi (t _ {0} + 2 T, t _ {0} + T) \right\|\cdot \| \Phi (t _ {0} + T, t _ {0}) \| \leqslant \frac {k _ {3}}{2 ^ {2}}, \quad \forall t \in [ t _ {0} + 2 T, t _ {0} + 3 T) \tag {4.73}\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet\left\| \Phi (t, t _ {0}) \right\| \leqslant \frac {k _ {3}}{2 ^ {m}}, \quad \forall t \in [ t _ {0} + m T, t _ {0} + (m + 1) T) \tag {4.74}$$

现在，构造一个指数函数 $k_{1}e^{-k_{2}(t - t_{0})}$ ，使得成立

$$\left[ k _ {1} e ^ {- k _ {2} (t - t _ {0})} \right] _ {s = s _ {0} + m T} = \frac {k _ {3}}{2 ^ {m - 1}}, \quad m = 1, 2, \dots \tag {4.75}$$

则由此可进而得到

$$k _ {1} \left(e ^ {- k _ {2} T}\right) ^ {m} = 2 k _ {3} \left(\frac {1}{2}\right) ^ {m} \tag {4.76}$$

于是，可取 $k_{1} = 2k_{3}$ 和取 $k_{2}$ 使 $e^{-k_{2}T} = 1 / 2$ 。这表明，存在正实数 $k_{1}$ 和 $k_{2}$ ，使(4.66)成立，必要性得证。至此，证明完成。

结论2[李亚普诺夫判据] 考虑线性时变系统(4.63)， $x_{e}=0$ 为其唯一的平衡状态， $A(t)$ 的元均为分段连续的一致有界的实函数。则原点平衡状态为一致渐近稳定的充分必要条件，是对任意给定的一个实对称、一致有界和一致正定的时变矩阵 $Q(t)$ ，即存在正实数 $\beta_{2}>\beta_{1}>0$ 使成立

$$0 < \beta_ {1} I \leqslant Q (t) \leqslant \beta_ {2} I, \quad \forall t \geqslant t _ {0} \tag {4.77}$$

如下形式的李亚普诺夫方程

$$- \dot {P} (t) = P (t) A (t) + A ^ {T} (t) P (t) + Q (t), \quad \forall t \geqslant t _ {0} \tag {4.78}$$

有唯一的实对称、一致有界和一致正定的矩阵解 $P(t)$ ，即存在正实数 $\alpha_{2} > \alpha_{1} > 0$ 使成立

$$0 < \alpha_ {1} I \leqslant P (t) \leqslant \alpha_ {2} I, \quad \forall t \geqslant t _ {0} \tag {4.79}$$

证 利用李亚普诺夫第二方法的主稳定性定理，即可直接导出此结论。推证过程略去。
