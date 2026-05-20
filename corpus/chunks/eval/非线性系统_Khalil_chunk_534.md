为了证明对 y 的误差估计, 考虑方程(C.70), 为讨论方便, 将其时间尺度用 $\tau$ 表示, 有

$$\frac {d y}{d \tau} = G (t _ {0} + \varepsilon \tau , x (t _ {0} + \varepsilon \tau , \varepsilon), y, \varepsilon)$$

设 $\hat{y} (\tau)$ 表示边界层模型 $\frac{dy}{d\tau} = G(t_0,\xi_0,y,0), y(0) = \eta_0 - h(t_0,\xi_0)$

的解,并设定 $v(\tau,\varepsilon)=y(\tau,\varepsilon)-\hat{y}(\tau)$

两边对 $\tau$ 求微分,并代入y和 $\hat{y}$ 的导数,得

$$\frac {d v}{d \tau} = G (t _ {0} + \varepsilon \tau , x (t _ {0} + \varepsilon \tau , \varepsilon), y (\tau , \varepsilon), \varepsilon) - G (t _ {0}, \xi_ {0}, \hat {y} (\tau), 0)$$

加减 $G(t_0 + \varepsilon \tau, x(t_0 + \varepsilon \tau, \varepsilon), v, 0)$ ，可得

$$\frac {d v}{d \tau} = G (t, x, v, 0) + \Delta G \tag {C.82}$$

其中 $t = t_0 + \varepsilon \tau, x = x(t_0 + \varepsilon \tau, \varepsilon), \Delta G = \Delta_1 + \Delta_2 + \Delta_3$ ，且

$$\Delta_ {1} = G (t, x, y, 0) - G (t, x, \hat {y}, 0) - G (t, x, v, 0)\Delta_ {2} = G (t, x, y, \varepsilon) - G (t, x, y, 0)\Delta_ {3} = G (t, x, \hat {y}, 0) - G (t _ {0}, \xi_ {0}, \hat {y}, 0)$$

可以验证

$$\left\| \Delta_ {1} \right\| \leqslant k _ {4} \| v \| ^ {2} + k _ {5} \| v \| \| \hat {y} \|, \quad \left\| \Delta_ {2} \right\| \leqslant \varepsilon L _ {3}\left\| \Delta_ {3} \right\| \leqslant L _ {1} \left| t - t _ {0} \right| \| \hat {y} \| + L _ {2} \left\| x - \xi_ {0} \right\| \| \hat {y} \| \leqslant \left(L _ {1} \varepsilon \tau + L _ {2} \varepsilon a + L _ {2} \varepsilon \tau k _ {0}\right) \| \hat {y} \|$$

其中 $k_{4}, k_{5}$ 和 a 是非负常数。重复得出式(C.80)的推导, 可证明

$$\| \hat {y} (\tau) \| \leqslant k _ {1} e ^ {- \alpha \tau}, \forall \tau \geqslant 0 \tag {C.83}$$

因此

$$
\begin{array}{r l} \| \Delta G \| & \leqslant k _ {4} \| v \| ^ {2} + k _ {5} k _ {1} \| v \| e ^ {- \alpha \tau} + \varepsilon L _ {3} + \varepsilon a _ {1} k _ {1} (1 + \tau) e ^ {- \alpha \tau} \\ & \leqslant k _ {6} \| v \| ^ {2} + k _ {7} k _ {1} \| v \| = 0. \end{array} \tag {C.84}
\leqslant k _ {4} \| v \| ^ {2} + k _ {5} k _ {1} \| v \| e ^ {- \alpha \tau} + \varepsilon a _ {2}
$$

其中 $a_1 = \max \{L_2 a, L_1 + L_2 k_0\}, a_2 = L_3 + a_1 k_1 \max \{1, 1 / \alpha\}$ 。我们已用到 $(1 + \tau)e^{-\alpha \tau} \leqslant \max \{1, 1 / \alpha\}$ ，方程(C.82)可看成

$$\frac {d v}{d \tau} = G (t, x, v, 0) \tag {C.85}$$

的扰动,根据引理9.8,上式有李雅普诺夫函数 $V_{1}(t,x,v)$ ,满足式(C.74)至式(C.76)。计算 $V_{1}$ 沿方程(C.82)轨线的导数,并利用估计式(C.84),得
