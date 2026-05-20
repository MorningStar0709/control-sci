$$
f (\lambda) = \det [ \lambda I - (A - G C) ] = \det \left[ \begin{array}{c c} \lambda + g _ {1} & - 1 \\ g _ {2} - 1 & \lambda \end{array} \right] = \lambda^ {2} + g _ {1} \lambda + (g _ {2} - 1).
$$

由此可见， $g_{1} = 2\alpha, g_{2} = \alpha^{2} + \beta^{2} + 1.$

于是，在 $G$ 决定之后，由观测器的结构定理可知，所给系统的状态观测器为

$$
\left\{ \begin{array}{l} \dot {x} _ {1 e} (t) = - 2 \alpha x _ {1 e} (t) + x _ {2 e} (t) + u _ {1} (t) + 2 \alpha y (t), \\ \dot {x} _ {2 e} (t) = - (\alpha^ {2} + \beta^ {2}) x _ {1 e} (t) + u _ {2} (t) + (1 + \alpha^ {2} + \beta^ {2}) y (t). \end{array} \right.
$$

例1.7.2 已知定常线性系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = \mu x _ {2} + u _ {1} (t), \\ \dot {x} _ {2} (t) = - \mu x _ {1} (t) + u _ {2} (t), \\ \dot {x} _ {3} (t) = u _ {3} (t), \\ y _ {1} (t) = x _ {1} (t), \\ y _ {2} (t) = x _ {2} (t) - x _ {3} (t), \end{array} \right.
$$

其中 $\mu > 0$ 为常数，试做它的状态观测器.

解 不难验证，这个系统是完全能观测的。令

$$
\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{l l l} 0 & \mu & 0 \\ - \mu & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], \quad \boldsymbol {C} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & - 1 \end{array} \right], \\ \boldsymbol {x} (t) = \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \\ x _ {3} (t) \end{array} \right], \quad u (t) = \left[ \begin{array}{l} u _ {1} (t) \\ u _ {2} (t) \\ u _ {3} (t) \end{array} \right], \quad y (t) = \left[ \begin{array}{l} y _ {1} (t) \\ y _ {2} (t) \end{array} \right], \\ \end{array}
$$

则上述系统可改写成

$$
\left\{ \begin{array}{l} \dot {x} (t) = A x (t) + u (t), \\ y (t) = C x (t). \end{array} \right.
$$

依定理 1.7.1, 观测器结构为

$$\dot {x} _ {e} (t) = (A - G C) x _ {e} (t) + u (t) + G y (t).$$

现在要确定增益矩阵 G，使矩阵 A-GC 是稳定的。假设要求观测器的极点为 $-\alpha$ ， $\alpha \pm \beta j (\alpha, \beta > 0)$ ，则观测器的特征多项式为

$$f (\lambda) = (\lambda + \alpha) (\lambda^ {2} + 2 \alpha \lambda + \alpha^ {2} + \beta^ {2}).$$

另一方面，观测器的特征多项式又为

$$f (\lambda) = \det [ \lambda I _ {3} - (A - G C) ].$$

于是有

$$\det [ \lambda I _ {3} - (A - G C) ] = (\lambda + \alpha) (\lambda^ {2} + 2 \alpha \lambda + \alpha^ {2} + \beta^ {2}).$$

由此可以决定矩阵 $G$ 的诸元。但是，这样做比较复杂，常常需要解关于 $G$ 的元的非线性代数方程，且其解不唯一。当然，这种不唯一性是有利的，它有可能照顾到系统其他性能的要求。对于求 $G$ 问题不再多谈，这实际上是做极点配置的一种方法。当然，还有其他方法可达到同样的目的。

在一些情形下，可以将原系统分为两个子系统，然后对每个子系统单独设计观测器，最后再把两个观测器合起来成为原系统的观测器，而每个子系统的观测器都是比较容易设计的，并且阶数较低。

观察本例所给系统发现，系统状态变量之间存在着解耦关系，即前两个状态变量不受第三个状态变量的影响。根据这个特点，考虑将系统分解为如下两个子系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = \mu x _ {2} + u _ {1} (t), \\ \dot {x} _ {2} (t) = - \mu x _ {1} (t) + u _ {2} (t), \\ y _ {1} (t) = x _ {1} (t), \end{array} \right. \tag {1.7.12}
