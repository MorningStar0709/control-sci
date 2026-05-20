其中 $g_{*}(\xi) = g_{11}(\xi,0), H(\xi ,y)$ 和 $M(\xi ,y)$ 满足

$$\left\| g _ {1 2} ^ {\mathrm{T}} (\xi , y) y + L _ {g _ {1 1}} ^ {\mathrm{T}} W (\xi) \right\| ^ {2} = \left\| L _ {g _ {*}} ^ {\mathrm{T}} W (\xi) \right\| ^ {2} + M (\xi , y) y,\frac {1}{2} \| h (\xi , y) \| ^ {2} = \frac {1}{2} \| h _ {*} (\xi) \| ^ {2} + H (\xi , y) y.$$

证明 定义正定函数 $V(\xi, y)$ 如式 (6.9.24), 则有

$$
\begin{array}{l} \dot {V} = L _ {f *} W (\xi) + L _ {F} W (\xi) y + \left(I _ {g _ {1 1}} W (\xi) + y ^ {\mathrm{T}} g _ {1 2} (\xi , y)\right) w + y ^ {\mathrm{T}} v, \\ = L _ {f _ {*}} W (\xi) + \frac {1}{2} h ^ {\mathrm{T}} (\xi , y) h (\xi , y) + \frac {1}{2} \left(\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2}\right) - \frac {1}{2} \left\| \frac {1}{\gamma} \left(g _ {1 2} ^ {\mathrm{T}} (\xi , y) y \right. \right. \\ \left. + L _ {g _ {1 1}} ^ {\mathrm{T}} W (\xi)\right) - \gamma w \left\| ^ {2} + \frac {1}{2 \gamma^ {2}} \left\| g _ {1 2} ^ {\mathrm{T}} (\xi , y) y + L _ {g _ {1 1}} ^ {\mathrm{T}} W (\xi) \right\| ^ {2} + y ^ {\mathrm{T}} \left(v + L _ {F} ^ {\mathrm{T}} W (\xi)\right) \right. \\ \leqslant L _ {f _ {*}} W (\xi) + \frac {1}{2 \gamma^ {2}} \left\| L _ {g _ {*}} ^ {\mathrm{T}} W (\xi) \right\| ^ {2} + \frac {1}{2} \left\| h _ {*} (\xi) \right\| ^ {2} + \frac {1}{2} \left(\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2}\right) \\ + y ^ {T} \left(v + L _ {F} ^ {T} W (\xi) + H ^ {T} (\xi , y) + \frac {1}{2 \gamma^ {2}} M ^ {T} (\xi , y)\right). \tag {6.9.34} \\ \end{array}
$$

因此将控制器(6.9.33)和不等式(6.9.32)代入上式, 得耗散不等式(6.9.26). 当 $w = 0$ 时闭环系统的稳定性证明则与定理6.9.2完全类似.

观察定理 6.9.3 的条件可知，Hamilton-Jacobi 偏微分不等式 (6.9.32) 有正定解 $W(\xi)$ 的条件等价于当干扰输入 $w \neq 0$ 时，零输出动态

$$
\left\{ \begin{array}{l} \dot {\xi} = f _ {*} (\xi) + g _ {*} (\xi) w \\ z = h _ {*} (\xi) \end{array} \right. \tag {6.9.35}
$$

是 $\gamma-$ 耗散的。因此定理6.9.3的结果表明，如果系统输出 $y$ 对控制输入 $u$ 的相关阶数为1，且其零输出动态是 $\gamma-$ 耗散的，那么我们可以通过状态反馈实现闭环系统的 $\gamma-$ 耗散性。实际上，与镇定问题的Backstepping设计方法（见文献[11])类似，这个特征表明，使闭环系统满足 $\gamma-$ 耗散性的控制器也可以通过递推构造存储函数的方法来设计。

比如，如果系统(6.9.15)具有相关阶 $r > 1$ ，那么在一定的条件下，该系统反馈等价于系统

$$
\left\{ \begin{array}{c} \dot {\xi} = f _ {0} (\xi , y) + g _ {1 1} (\xi , y _ {1}) w, \\ \dot {y} _ {1} = y _ {2} + g _ {1 2} (\xi , y _ {1}, y _ {2}) w, \\ \vdots \\ \dot {y} _ {r} = v + g _ {1 r + 1} (\xi , y _ {1}, \dots , y _ {r}) w, \\ z = h (\xi , y _ {1}, y _ {2}, \dots , y _ {r}). \end{array} \right. \tag {6.9.36}
$$

因此，如果 $\xi-$ 子系统具有 $\gamma$ 耗散性，那么首先可以把 $y_{2}$ 作为假想输入，将定理6.9.3应用于 $(\xi, y_{1})$ 子系统得到满足 $\gamma-$ 耗散性和稳定性的控制输入 $y_{2} = \alpha(\xi, y_{1})$ 。然后，利用得到的控制输入函数 $\alpha$ 进行坐标变换，在新的坐标下，再将 $y_{3}$ 看做是假想的控制输入。依次类推，反复应用定理6.9.3，就可以得到全系统的 $H_{\infty}$ 控制器。而且，若 $g_{11}(\xi) = 0$ ，那么在上述递推设计的第一步可以不要求 $W$ 满足Hamilton-Jacobi不等式，即只要 $\xi-$ 子系统是渐近稳定或指数稳定即可。关于这种递推设计方法，感兴趣的读者可参阅文献[13]、[14]。
