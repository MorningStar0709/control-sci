$$
\begin{array}{l} \frac {| v (t + h) - v (t) |}{h} = \frac {| x (t + h) |}{h} = \frac {1}{h} \left| \int_ {t} ^ {t + h} f (\tau , x (\tau)) d \tau \right| \\ = \left| f (t, 0) + \frac {1}{h} \int_ {t} ^ {t + h} [ f (\tau , x (\tau)) - f (t, x (t)) ] d \tau \right| \\ \leqslant | f (t, 0) | + \frac {1}{h} \int_ {t} ^ {t + h} | f (\tau , x (\tau)) - f (t, x (t)) | d \tau \\ \end{array}
$$

由于 $f(t,x(t))$ 是t的连续函数,因此给定 $\varepsilon>0$ ,存在 $\delta>0$ ,使得对于所有 $|\tau-t|<\delta$ , $|f(\tau,x(\tau))-f(t,x(t))|<\varepsilon$ ,因此,对于所有 $h<\delta$ ,有

$$\frac {1}{h} \int_ {t} ^ {t + h} | f (\tau , x (\tau)) - f (t, x (t)) | d \tau < \varepsilon$$

说明 $\lim_{h\to 0^{+}}\frac{1}{h}\int_{t}^{t + h}|f(\tau ,x(\tau)) - f(t,x(t))|d\tau = 0$

这样，只要 $x(t) = 0$ ，就有 $D^{+}v(t)\leqslant |f(t,0)| = e^{t}$ 。因此，对于所有 $t\in [0,t_1)$ ，有

$$D ^ {+} v (t) \leqslant - v (t) + e ^ {t}, \quad v (0) = | a |$$

设 $u(t)$ 是线性微分方程 $\dot{u} = -u + e^t, u(0) = |a|$

的解,由比较引理可得

$$v (t) \leqslant u (t) = e ^ {- t} | a | + \frac {1}{2} \left[ e ^ {t} - e ^ {- t} \right], \quad \forall t \in [ 0, t _ {1})$$

对于每个有限的 $t_1, v(t)$ 的上界都是有限的，只有当 $t_1$ 趋于无穷时趋于无限。因此，解 $x(t)$ 对于所有 $t \geqslant 0$ 都有定义，且满足

$$| x (t) | \leqslant e ^ {- t} | a | + \frac {1}{2} \left[ e ^ {t} - e ^ {- t} \right], \quad \forall t \geqslant 0$$
