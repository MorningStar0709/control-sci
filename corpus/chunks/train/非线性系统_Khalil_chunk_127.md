根据引理4.3,存在定义在 $[0,r]$ 上的 $\kappa$ 类函数 $\alpha_{1}$ 和 $\alpha_{2}$ , 满足

$$\alpha_ {1} (\| x \|) \leqslant W _ {1} (x) \leqslant V (t, x) \leqslant W _ {2} (x) \leqslant \alpha_ {2} (\| x \|)$$

将上述两个不等式结合,有

$$\| x (t) \| \leqslant \alpha_ {1} ^ {- 1} (V (t, x (t))) \leqslant \alpha_ {1} ^ {- 1} (V (t _ {0}, x (t _ {0}))) \leqslant \alpha_ {1} ^ {- 1} (\alpha_ {2} (\| x (t _ {0}) \|))$$

根据定理4.2可知 $\alpha_{1}^{-1}\circ \alpha_{2}$ 是 $\mathcal{K}$ 类函数（根据引理4.2），则不等式 $\| x(t)\| \leqslant \alpha_1^{-1}(\alpha_2(\| x(t_0)\|))$ 表明原点是一致稳定的。

定理4.9 假设定理4.8中的假定条件都满足不等式(4.23)的加强形式

$$\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant - W _ {3} (x) \tag {4.24}$$

$\forall t \geqslant 0, \forall x \in D$ ，其中 $W_{3}(x)$ 是 $D$ 上的连续正定函数。那么， $x = 0$ 是一致渐近稳定的。如果选择 $r$ 和 $c$ 满足 $B_{r} = \{\| x \| \leqslant r\} \subset D$ 和 $c < \min_{\| x \| = r} W_{1}(x)$ ，则始于 $\{x \in B_{r} \mid W_{2}(x) \leqslant c\}$ 的每条轨线对于某个 $\mathcal{KL}$ 类函数 $\beta$ 都满足

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0}), \forall t \geqslant t _ {0} \geqslant 0$$

如果 $D = R^n$ 和 $W_{1}(x)$ 径向无界，则 $x = 0$ 是全局一致渐近稳定的。

证明:由定理4.8的证明可知,对于所有 $t\geqslant t_{0}$ ,始于 $\{x\in B_{r}|W_{2}(x)\leqslant c\}$ 的轨线都保持在 $\{x\in B_{r}|W_{1}(x)\leqslant c\}$ 内。由引理4.3可知,存在定义在 $[0,r]$ 上的K类函数 $\alpha_{3}$ ,满足

$$\dot {V} (t, x) = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant - W _ {3} (x) \leqslant - \alpha_ {3} (\| x \|)$$

利用不等式 $V \leqslant \alpha_{2}(\| x\|) \Leftrightarrow \alpha_{2}^{-1}(V) \leqslant \| x\| \Leftrightarrow \alpha_{3}(\alpha_{2}^{-1}(V)) \leqslant \alpha_{3}(\| x\|)$

可见, V 满足微分不等式 $\dot{V} \leqslant -\alpha_{3}(\alpha_{2}^{-1}(V)) \stackrel{\mathrm{def}}{=} -\alpha(V)$

其中 $\alpha = \alpha_{3} \circ \alpha_{2}^{-1}$ 是定义在 $[0, r]$ 上的 $K$ 类函数（见引理4.2）。为了不失一般性①，假设 $\alpha$ 是局部利普希茨函数，并设 $y(t)$ 满足一阶自治微分方程

$$\dot {y} = - \alpha (y), y (t _ {0}) = V (t _ {0}, x (t _ {0})) \geqslant 0$$

根据引理 3.4(比较引理),有

$$V (t, x (t)) \leqslant y (t), \forall t \geqslant t _ {0}$$

根据引理4.4,存在一个定义在 $[0,r]\times [0,\infty)$ 上的 $\mathcal{KL}$ 类函数 $\sigma (r,s)$ ，满足：

$$V (t, x (t)) \leqslant \sigma (V (t _ {0}, x (t _ {0})), t - t _ {0}), \forall V (t _ {0}, x (t _ {0})) \in [ 0, c ]$$

因此，任何始于 $\{x\in B_r|W_2(x)\leqslant c\}$ 的解都满足不等式
