显然，当 $\pmb{u}(t) = \pmb{u}^{*}(t) = -\pmb{R}_{\mathrm{p}}^{-1}(t)\pmb{G}_{\mathrm{p}}^{\mathrm{T}}(t)\pmb{K}(t)\pmb{x}(t)$ 使上式达到极小，故有

$$J \left(\boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}\right) \leqslant J \left(\boldsymbol {u}, \boldsymbol {v} ^ {*}\right)$$

另一方面，当 $\pmb{u}(t) = \pmb{u}^{*}(t) = -\pmb{R}_{\mathrm{p}}^{-1}(t)\pmb{G}_{\mathrm{p}}^{\mathrm{T}}(t)\pmb{K}(t)\pmb{x}(t)$ 时，

$$J \left(\boldsymbol {u} ^ {*}, \boldsymbol {v}\right) = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \left(t _ {0}\right) \boldsymbol {K} \left(t _ {0}\right) \boldsymbol {x} \left(t _ {0}\right) - \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ \boldsymbol {v} (t) +\left. \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} \boldsymbol {K} (t) \boldsymbol {x} (t) \right] ^ {\mathrm{T}} \boldsymbol {R} _ {\mathrm{e}} (t) [ \boldsymbol {v} (t) + \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} \boldsymbol {K} (t) \boldsymbol {x} (t) ] \mathrm{d} t$$

显然，当 $\boldsymbol{v}(t)=\boldsymbol{v}^{*}(t)=-\boldsymbol{R}_{e}^{-1}(t)\boldsymbol{G}_{e}^{\mathrm{T}}(t)\boldsymbol{K}(t)\boldsymbol{x}(t)$ 时，上式达到极大，故有

$$J (\boldsymbol {u} ^ {*}, \boldsymbol {v}) \leqslant J (\boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*})$$

综合上面二种情况, 可知 $(u^{*}, v^{*})$ 满足鞍点条件, 而且最优策略 $(u^{*}, v^{*})$ 对应的性能指标为

$$J ^ {*} = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \left(t _ {0}\right) \boldsymbol {K} \left(t _ {0}\right) \boldsymbol {x} \left(t _ {0}\right) \tag {10-108}$$

例10-5 拦截目标的导引律

用导弹(追逐者)拦截空中目标(逃逸者)时,末制导段常用的经典导引律是比例导引。这里将用微分对策理论来推出比例导引律。

![](image/29943af69a094b5aeab236dd902698e935c2c6187fd7c63d909ce0504615de96.jpg)

<details>
<summary>text_image</summary>

Y
v_p
p
r_p
r_e
O
X
q
e
v_e
</details>

图10-6 拦截问题运动示意图

设导弹(p 方)与目标(e 方)的运动方程分别为

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {r}} _ {\mathrm{p}} = \boldsymbol {v} _ {\mathrm{p}} \\ \dot {\boldsymbol {v}} _ {\mathrm{p}} = \boldsymbol {f} _ {\mathrm{p}} + \boldsymbol {a} _ {\mathrm{p}} \end{array} \right. \tag {10-109}

\left\{ \begin{array}{l} \dot {\boldsymbol {r}} _ {\mathrm{e}} = \boldsymbol {v} _ {\mathrm{e}} \\ \dot {\boldsymbol {v}} _ {\mathrm{e}} = \boldsymbol {f} _ {\mathrm{e}} + \boldsymbol {a} _ {\mathrm{e}} \end{array} \right. \tag {10-110}
$$
