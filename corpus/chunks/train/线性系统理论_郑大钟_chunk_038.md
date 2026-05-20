$$
\left(\frac {\partial \boldsymbol {f}}{\partial \boldsymbol {x} ^ {T}}\right) _ {0} = \left(\frac {\partial \boldsymbol {f}}{\partial \boldsymbol {x} ^ {T}}\right) _ {x _ {0}, w _ {0}} = \left[ \begin{array}{c c} \frac {\partial f _ {1}}{\partial x _ {1}} & \dots \frac {\partial f _ {1}}{\partial x _ {n}} \\ \vdots & \vdots \\ \frac {\partial f _ {n}}{\partial x _ {1}} & \dots \frac {\partial f _ {n}}{\partial x _ {n}} \end{array} \right] _ {x _ {0}, w _ {0}} = A (t)

\left(\frac {\partial f}{\partial u ^ {r}}\right) _ {0} = \left(\frac {\partial f}{\partial u ^ {r}}\right) _ {x _ {0}, u _ {0}} = \left[ \begin{array}{c c} \frac {\partial f _ {1}}{\partial u _ {1}} & \dots \frac {\partial f _ {1}}{\partial u _ {p}} \\ \vdots & \vdots \\ \frac {\partial f _ {n}}{\partial u _ {1}} & \dots \frac {\partial f _ {n}}{\partial u _ {p}} \end{array} \right] _ {x _ {0}, u _ {0}} = B (t)

\left(\frac {\partial g}{\partial x ^ {T}}\right) _ {0} = \left(\frac {\partial g}{\partial x ^ {T}}\right) _ {x _ {0}, u _ {0}} = \left[ \begin{array}{c c} \frac {\partial g _ {1}}{\partial x _ {1}} & \dots \frac {\partial g _ {1}}{\partial x _ {s}} \\ \vdots & \vdots \\ \frac {\partial g _ {t}}{\partial x _ {1}} & \dots \frac {\partial g _ {t}}{\partial x _ {s}} \end{array} \right] _ {x _ {0}, u _ {0}} = C (t)

\left(\frac {\partial g}{\partial u ^ {T}}\right) _ {t} = \left(\frac {\partial g}{\partial u ^ {T}}\right) _ {x _ {0}, u _ {0}} = \left[ \begin{array}{c c} \frac {\partial g _ {1}}{\partial u _ {1}} & \dots \frac {\partial g _ {1}}{\partial u _ {p}} \\ \vdots & \vdots \\ \frac {\partial g _ {q}}{\partial u _ {1}} & \dots \frac {\partial g _ {q}}{\partial u _ {p}} \end{array} \right] _ {x _ {0}, u _ {0}} = D (t)
$$

则在略去台劳展开中的高次项后，就可导出 $(x_0, u_0)$ 的邻域内非线性系统（1.19）的线性化状态空间描述为

$$
\left\{ \begin{array}{l} \delta \dot {x} = f (x, u, t) - f \left(x _ {0}, u _ {0}, t\right) = A (t) \delta x + B (t) \delta u \\ \delta y = g (x, u, t) - g \left(x _ {0}, u _ {0}, t\right) = C (t) \delta x + D (t) \delta u \end{array} \right. \tag {1.22}
$$

容易看出，(1.22)即为系统的微偏运动的数学描述，当邻域愈小时线性化模型(1.22)能以愈高的精确度代替原非线性系统(1.19)。

比之非线性系统，线性系统无论在分析上或综合上都要简单得多。因此，对于大多数实际系统，通常都通过一定的简化而化为线性系统问题来加以研究。此外，为形象化表示起见，还常将线性系统的状态空间描述（1.20）表示为图1.4所示的方块图。

![](image/369a62c3b4144a81830b3af1dcf9321279bf84a4b8bb31972eeaa38c64a02a08.jpg)

<details>
<summary>flowchart</summary>
