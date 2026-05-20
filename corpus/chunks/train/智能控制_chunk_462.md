$$
\Delta V (k) = \left\{ \begin{array}{l l} - V _ {1} - \frac {2 \beta}{c _ {1} ^ {2}} \left(\Delta_ {f} (\boldsymbol {x} (k - 1)) + v (k)\right) e _ {1} (k) + & \\ \left(\frac {\beta}{\sqrt {\gamma} c _ {1} ^ {2}}\right) ^ {2} \boldsymbol {h} ^ {\mathrm{T}} (\boldsymbol {x} (k - 1)) \boldsymbol {h} (\boldsymbol {x} (k - 1)) e _ {1} ^ {2} (k) & | e _ {1} (k) | > \varepsilon_ {f} / G \\ - V _ {1} - \frac {2 \beta}{c _ {1} ^ {2}} \left[ \left((\widetilde {\boldsymbol {w}} ^ {\mathrm{T}} (k - 1) \boldsymbol {h} (\boldsymbol {x} (k - 1))) + \right. \right. & \\ v (k) + \Delta_ {f} (\boldsymbol {x} (k - 1)) e _ {1} (k) ] & | e _ {1} (k) | \leqslant \varepsilon_ {f} / G \end{array} \right. \tag {9.90}
$$

辅助控制信号 $v(k)$ 的设计应保证 $e_{1}(k) \rightarrow 0$ ，从而 $e(k) \rightarrow 0$ 。设计辅助控制信号为 $^{[38]}$

$$v (k) = v _ {1} (k) + v _ {2} (k) \tag {9.91}$$

式中， $v_{1}(k)=\frac{\beta}{2\gamma c_{1}^{2}}\boldsymbol{h}^{\mathrm{T}}(\boldsymbol{x}(k-1))\boldsymbol{h}(\boldsymbol{x}(k-1))e_{1}(k)$ 和 $v_{2}(k)=Ge_{1}(k)$ 。

如果 $\left|e_{1}(k)\right|>\varepsilon_{f}/G$ ，将式(9.91)代入式(9.90)，整理可得

$$\Delta V (k) = - V _ {1} - \frac {2 \beta}{c _ {1} ^ {2}} \left(\Delta_ {f} (\boldsymbol {x} (k - 1)) + G e _ {1} (k)\right) e _ {1} (k)\leqslant - \frac {2 \beta}{c _ {1} ^ {2}} \left(\Delta_ {f} (\boldsymbol {x} (k - 1)) + G e _ {1} (k)\right) e _ {1} (k)$$

由 $|\Delta_f(x)| < \varepsilon_f, |e_1(k)| > \varepsilon_f / G$ ，则 $|e_1(k)| > \frac{|\Delta_f(x(k-1))|}{G}, e_1^2(k) > -\frac{\Delta_f(x(k-1))e_1(k)}{G}$ ，因

此 $(\Delta_f(x(k - 1)) + Ge_1(k))e_1(k) > 0$ ，从而可得 $\Delta V(k) < 0$ 。

如果 $\left|e_{1}(k)\right|\leqslant\varepsilon_{f}/G$ ，则可保证跟踪性能，且 $\Delta V(k)$ 可以任意小。

仿真说明如下：

(1) 由式(9.86) 可得 $e_1(k) = \beta \left(e(k) - \frac{1}{1 + c_1 z^{-1}} v(k)\right)$ , 则 $e_1(k)(1 + c_1 z^{-1}) = \beta (e(k)(1 + c_1 z^{-1}) - v(k))$ , 因此

$$e _ {1} (k) = - c _ {1} e _ {1} (k - 1) + \beta (e (k) + c _ {1} e (k - 1) - v (k)) \tag {9.92}$$

(2) 通过 Lyapunov 稳定性分析, 如果 $k \to \infty$ , $e_1(k) \to 0$ , 由式 (9.91) 可得 $v(k) \to 0$ , 再由式 (9.92), 很显然 $e(k) + c_1 e(k-1) \to 0$ , 考虑到 $|c_1| < 1$ , 可得 $e(k) \to 0$ 。

(3) $v(k)$ 是一个虚拟变量，由式(9.91)，令 $v_1'(k) = \frac{\beta}{2\gamma c_1^2}\pmb{h}^{\mathrm{T}}(\pmb{x}(k - 1))\pmb{h}(\pmb{x}(k - 1))$ ，可得 $v(k) = (v_1'(k) + G)e_1(k)$ ，将 $v(k)$ 代入式(9.92）中，可得 $e_1(k) = -c_1e_1(k - 1) + \beta (e(k) + c_1e(k - 1) - (v_1'(k) + G)e_1(k))$ ，进一步整理得

$$e _ {1} (k) = \frac {- c _ {1} e _ {1} (k - 1) + \beta (e (k) + c _ {1} e (k - 1))}{1 + \beta \left(v _ {1} ^ {\prime} (k) + G\right)} \tag {9.93}$$
