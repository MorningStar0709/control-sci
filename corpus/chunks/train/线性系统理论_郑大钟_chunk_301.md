$$\hat {\mathbf {y}} (s) = G (s) \hat {\mathbf {u}} (s) = G (s) \mathbf {u} _ {0} / s - z _ {0} \tag {8.27}$$

其中，已利用了(8.25)所示输入向量 $u(t)$ 的拉普拉斯变换式 $\hat{u}(s) = u_0 / s - z_{00}$ 相应地，

由 $u(t)$ 引起的输出响应则为

$$
\begin{array}{l} \mathbf {y} (t) = \left[ \lim _ {s \rightarrow x _ {0}} G (s) u _ {0} \frac {1}{s - z _ {0}} \cdot (s - z _ {0}) \right] e ^ {x _ {0} t} \\ = G \left(z _ {0}\right) u _ {0} a ^ {s _ {0} t} \tag {8.28} \\ \end{array}
$$

考虑到 $G(z_0) = C(x_0I - A)^{-1}B$ ，并利用式(8.24)的条件，于是进一步可得到

$$
\begin{array}{l} y (t) = C \left(z _ {0} I - A\right) ^ {- 1} B u _ {0} e ^ {x _ {0} t} = - C \left(z _ {0} I - A\right) ^ {- 1} \left(z _ {0} I - A\right) x _ {0} e ^ {x _ {0} t} \\ = - C x _ {0} e ^ {x _ {0} t} = 0, \forall t \geqslant 0 \tag {8.29} \\ \end{array}
$$

从而，结论得证。
