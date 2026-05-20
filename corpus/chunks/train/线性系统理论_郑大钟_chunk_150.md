显然，上式是一个矛盾的结果，表明反设不成立。由此可见，在区间 $t_0 \leqslant t \leqslant t_2$ 中必存在某个时刻 $t_2$ ，使成立 $\| \phi(t_2; x_0, t_0) \| = \nu(\mu)$ 。

最后，求证对一切 $t \geqslant t_0 + T(\mu, \delta)$ 必成立 $\| \phi(t; x_0, t_0) \| \leqslant \mu_0$ 由于 $\| \phi(t_2; x_0, t_0) \| = \nu(\mu)$ ，因此对一切 $t \geqslant t_2$ 可有

$$\alpha \left(\| \phi (t; x _ {0}, t _ {0}) \|\right) \leqslant V \left(\phi (t; x _ {0}, t _ {0}), t\right) \leqslant V \left(\phi \left(t _ {2}; x _ {0}, t _ {0}\right), t _ {2}\right) \leqslant \beta (\nu) \leqslant \alpha (\mu) \tag {4.39}$$

再注意到 $\alpha (\| x\|)$ 为连续非减函数，所以据此和式(4.39)即可导出，对所有 $t\geqslant t_2$ 成立

$$\left\| \phi (t; x _ {0}, t _ {0}) \right\| \leqslant \mu \tag {4.40}$$

又知 $t_0 + T(\mu, \delta) \geqslant t_2$ ，所以对一切 $t \geqslant t_0 + T(\mu, \delta)$ 显然上式也成立。并且，当 $\mu \to 0$ 时有 $T \to \infty$ 。

如上，我们就证明了，对任意初始时刻 $t_0$ ，由满足 $\| x_0\| \leqslant \delta (s)$ 的任一初态 $x_0$ 出发的受扰运动 $\phi (t;x_0,t_0)$ 当 $t\to \infty$ 时都收敛于原点平衡状态。

③ 证明对状态空间 $X$ 中的任一非零 $\pmb{x}_0$ ，其所确定的受扰运动都为一致有界。为此，注意到 $\| \pmb{x} \| \to \infty$ 时有 $\alpha (\| \pmb{x} \|) \to \infty$ ，所以对任意大的有限实数 $\delta > 0$ ，都必存在有限实数 $\varepsilon (\delta) > 0$ ，使成立 $\beta (\delta) < \alpha (\varepsilon)$ 。于是，对任意非零 $\pmb{x}_0 \in X$ 和一切 $t \geqslant t_0$ ，可有

$$\alpha (\varepsilon) > \beta (\delta) \geqslant V (x _ {0}, t _ {0}) \geqslant V (\phi (t; x _ {0}, t _ {0}), t) \geqslant \alpha (\| \phi (t; x _ {0}, t _ {0}) \|) \tag {4.41}$$

从而，由此并考虑到 $\alpha (\| x\|)$ 为连续非减函数，就可得到

$$\left\| \phi (t; x _ {0}, t _ {0}) \right\| \leqslant \varepsilon (\delta), \quad \forall t \geqslant t _ {0}, \forall x _ {0} \in X \tag {4.42}$$

且 $\varepsilon (\delta)$ 和初始时刻 $t_0$ 无关。这表明，对任意非零 $x_0\in X$ ， $\phi (t;x_0,t_0)$ 为一致有界。

至此，我们就完成了对李亚普诺夫主稳定性定理的证明。

应当强调指出，由结论1所给出的条件，只是保证系统（4.31）为大范围一致渐近稳定的充分条件。充分条件的局限性在于，如果对给定系统找不到一个标量函数 $V(x, t)$ 使满足结论中指出的条件，那么将不能对判断系统的稳定性提供任何信息。而且，在实际问题中，这样的情况是相当常见的。进而，还不难看出，若结论中的条件（iii）不满足，且条件（i）和（ii）仅对原点的一个邻域 $\Omega$ 内满足，则相应地只能导出局部一致渐近稳定的结论，同时进一步的问题是要确定出吸引区 $\Omega$ ，通常这不是一件容易的事。
