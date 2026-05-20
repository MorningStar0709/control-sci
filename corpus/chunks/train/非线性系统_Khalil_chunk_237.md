$$
\begin{array}{l} \dot {\nu} (y, w) = \frac {\partial V}{\partial y} [ A _ {1} y + g _ {1} (y, h (y)) + N _ {1} (y, w) ] \\ + \frac {1}{2 \sqrt {w ^ {\mathrm{T}} P w}} \left[ w ^ {\mathrm{T}} \left(P A _ {2} + A _ {2} ^ {\mathrm{T}} P\right) w + 2 w ^ {\mathrm{T}} P N _ {2} (y, w) \right] \\ \leqslant - \alpha_ {3} (\| y \| _ {2}) + k k _ {1} \| w \| _ {2} - \frac {\| w \| _ {2}}{2 \sqrt {\lambda_ {\max} (P)}} + \frac {k _ {2} \lambda_ {\max} (P)}{\sqrt {\lambda_ {\min} (P)}} \| w \| _ {2} \\ = - \alpha_ {3} (\| y \| _ {2}) - \frac {1}{4 \sqrt {\lambda_ {\max} (P)}} \| w \| _ {2} \\ - \left[ \frac {1}{4 \sqrt {\lambda_ {\max} (P)}} - k k _ {1} - k _ {2} \frac {\lambda_ {\max} (P)}{\sqrt {\lambda_ {\min} (P)}} \right] \| w \| _ {2} \\ \end{array}
$$

因为通过缩小原点的邻域可以使 $k_{1}$ 和 $k_{2}$ 取任意小, 所以可选择其足够小, 保证

$$\frac {1}{4 \sqrt {\lambda_ {\max} (P)}} - k k _ {1} - k _ {2} \frac {\lambda_ {\max} (P)}{\sqrt {\lambda_ {\min} (P)}} > 0$$

因此 $\dot{\nu} (y,w)\leqslant -\alpha_{3}(\| y\|_{2}) - \frac{1}{4\sqrt{\lambda_{\max}(P)}}\| w\|_{2}$

说明 $\dot{\nu}(y,w)$ 是负定的, 因而整个系统(8.9)\~(8.10)的原点是渐近稳定的。

扩展定理 8.2 的证明,以证明下面两个推论,这项工作作为习题留给读者(见习题 8.1 和习题 8.2)。

推论8.1 在定理8.1的假设条件下,如果降阶系统(8.5)的原点 $y = 0$ 是稳定的,且存在一个连续可微的李雅普诺夫函数 $V(y)$ ,在 $y = 0$ 的某个邻域内满足②

$$\frac {\partial V}{\partial y} [ A _ {1} y + g _ {1} (y, h (y)) ] \leqslant 0$$

则整个系统(8.2)\~(8.3)的原点是稳定的。

推论8.2 在定理8.1的假设条件下,当且仅当整个系统(8.2)\~(8.3)的原点渐近稳定时,降阶系统(8.5)的原点是渐近稳定的。

在应用定理8.2时，需要求出中心流形 $z = h(y)$ 。函数 $h$ 为偏微分方程

$$\mathcal {N} (h (y)) \stackrel {\text { def }} {=} \frac {\partial h}{\partial y} (y) [ A _ {1} y + g _ {1} (y, h (y)) ] - A _ {2} h (y) - g _ {2} (y, h (y)) = 0 \tag {8.11}$$

的一个解,其边界条件为 $h(0)=0;\quad\frac{\partial h}{\partial y}(0)=0$ (8.12)

但是,在大多数情况下,该方程对 h 不能准确求解(如果能获得准确的解,则表明已求出整个系统(8.2)\~(8.3)的解),但该解能够以 y 的泰勒级数任意逼近。

定理8.3 如果可以找到一个连续可微的函数 $\phi(y)$ , 且 $\phi(0) = 0$ , $[\partial \phi / \partial y](0) = 0$ , 使得对于 $p > 1$ , 有 $\mathcal{N}(\phi(y)) = O(\|y\|^p)$ , 则对于足够小的 $\|y\|$ , 有

$$h (y) - \phi (y) = O (\| y \| ^ {p})$$

且降阶系统可表示为 $\dot{y}=A_{1}y+g_{1}(y,\phi(y))+O(\|y\|^{p+1})$

证明: 见附录 C.15。

量值记号(magnitude notation) $O(\cdot)$ 的阶数将在第10章正式引入(见定义10.1)。这里只需了解，对于足够小的 $\| y\|$ ，可以把 $\| f(y)\| \leqslant k\| y\|^p$ 简记为 $f(y) = O(\| y\|^p)$ 。下面将通过几个例题介绍中心流形定理的应用。在前两个例子中，将研究标量状态方程

$$\dot {y} = a y ^ {p} + O \left(| y | ^ {p + 1}\right)$$

其中 $p$ 为正整数。如果 $p$ 是奇数且 $a < 0$ ，则原点是渐近稳定的；如果 $p$ 是奇数且 $a > 0$ ，或者 $p$ 是偶数且 $a \neq 0$ ，则原点是不稳定的（见习题4.2）。

例8.1 考虑系统 $\dot{x}_1 = x_2$
