是满秩矩阵。分布 $\Delta = \mathrm{span}(g, ad_f g, ad_f^2 g)$ 是对合的，因为 $g, ad_f g$ 和 $ad_f^2 g$ 都是常数向量场，这样定理13.2的条件对于所有 $x \in R^4$ 都成立。为了找到变量代换将状态方程转换为式(13.6)的形式，需要找到 $h(x)$ ，使之满足

$$\frac {\partial (L _ {f} ^ {i - 1} h)}{\partial x} g = 0, i = 1, 2, 3, \frac {\partial (L _ {f} ^ {3} h)}{\partial x} g \neq 0, h (0) = 0$$

根据条件 $[\partial h / \partial x]g = 0$ ，有 $(\partial h / \partial x_4) = 0$ ，所以必须选择 $h$ 与 $x_{4}$ 无关，因此

$$L _ {f} h (x) = \frac {\partial h}{\partial x _ {1}} x _ {2} + \frac {\partial h}{\partial x _ {2}} [ - a \sin x _ {1} - b (x _ {1} - x _ {3}) ] + \frac {\partial h}{\partial x _ {3}} x _ {4}$$

又根据条件 $[\partial (L_f h) / \partial x]g = 0$ ，有

$$\frac {\partial (L _ {f} h)}{\partial x _ {4}} = 0 \Rightarrow \frac {\partial h}{\partial x _ {3}} = 0$$

所以必须选择 $h$ 与 $x_{3}$ 无关。因此， $L_{f}h$ 简化成

$$L _ {f} h (x) = \frac {\partial h}{\partial x _ {1}} x _ {2} + \frac {\partial h}{\partial x _ {2}} [ - a \sin x _ {1} - b (x _ {1} - x _ {3}) ]$$

和

$$L _ {f} ^ {2} h (x) = \frac {\partial (L _ {f} h)}{\partial x _ {1}} x _ {2} + \frac {\partial (L _ {f} h)}{\partial x _ {2}} [ - a \sin x _ {1} - b (x _ {1} - x _ {3}) ] + \frac {\partial (L _ {f} h)}{\partial x _ {3}} x _ {4}$$

最后，有

$$\frac {\partial (L _ {f} ^ {2} h)}{\partial x _ {4}} = 0 \Rightarrow \frac {\partial (L _ {f} h)}{\partial x _ {3}} = 0 \Rightarrow \frac {\partial h}{\partial x _ {2}} = 0$$

由上式可知 $h$ 还应与 $x_{2}$ 无关，因此

$$L _ {f} ^ {3} h (x) = \frac {\partial (L _ {f} ^ {2} h)}{\partial x _ {1}} x _ {2} + \frac {\partial (L _ {f} ^ {2} h)}{\partial x _ {2}} [ - a \sin x _ {1} - b (x _ {1} - x _ {3}) ] + \frac {\partial (L _ {f} ^ {2} h)}{\partial x _ {3}} x _ {4}$$

并且只要 $(\partial h / \partial x_{1})\neq 0$ ，条件 $[\partial (L_f^3 h) / \partial x]g\neq 0$ 即成立。因而取 $h(x) = x_{1}$ ，进行变量代换

$$
\begin{array}{l} z _ {1} = h (x) = x _ {1} \\ z _ {2} = L _ {f} h (x) = x _ {2} \\ z _ {3} = L _ {f} ^ {2} h (x) = - a \sin x _ {1} - b \left(x _ {1} - x _ {3}\right) \\ z _ {4} = L _ {f} ^ {3} h (x) = - a x _ {2} \cos x _ {1} - b \left(x _ {2} - x _ {4}\right) \\ \end{array}
$$

将状态方程转换为

$$
\begin{array}{l} \dot {z} _ {1} = z _ {2} \\ \dot {z} _ {2} = z _ {3} \\ \dot {z} _ {3} = z _ {4} \\ \dot {z} _ {4} = - (a \cos z _ {1} + b + c) z _ {3} + a \left(z _ {2} ^ {2} - c\right) \sin z _ {1} + b d u \\ \end{array}
$$

上式即具有方程(13.6)的形式。与例13.13不同的是，本例在z坐标系下的状态方程全局有效，因为 $z=T(x)$ 是全局微分同胚映射。

例 13.15 在例 13.3 和例 13.7 中, 讨论了一个由三阶模型

$$\dot {x} = f (x) + g u$$

表示的场控直流电机,式中

$$
f (x) = \left[ \begin{array}{c} {- a x _ {1}} \\ {- b x _ {2} + k - c x _ {1} x _ {3}} \\ {\theta x _ {1} x _ {2}} \end{array} \right], g = \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right]
$$
