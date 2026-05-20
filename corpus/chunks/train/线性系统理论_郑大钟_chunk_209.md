$$0 \equiv \boldsymbol {x} ^ {T} (t) H ^ {T} H \boldsymbol {x} (t) = [ H \boldsymbol {x} (t) ] ^ {T} [ H \boldsymbol {x} (t) ] \tag {5.251}$$

从而可导出 $H\pmb{x}(t) \equiv \mathbf{0}$ 。显然，这是和已知 $\{A, H\}$ 为能观测相矛盾的。所以，反设不成立，也即有 $\dot{V}(\pmb{x}(t)) \neq 0$ 。此外易知，当 $\| \pmb{x} \| \to \infty$ 时有 $V(\pmb{x}) \to \infty$ 。从而，根据李亚普诺夫主稳定性定理知，闭环系统（5.246）为大范围渐近稳定。证明完成。

但是，应当指出，当 $Q \geqslant 0$ 时，矩阵分解式 $Q = H^{T}H$ 将不是唯一的。然而，尽管如此，却可断言：对任意分解式 $Q = H_{1}^{T}H_{1}$ 和 $Q = H_{2}^{T}H_{2}$ ，只要 $\{A, H_{1}\}$ 为能观测，则 $\{A, H_{2}\}$ 也必定是能观测的。对此，可采用反证法证明这个论断。反设当 $\{A, H_{1}\}$ 为能观测而 $\{A, H_{2}\}$ 为不完全能观测，那么意味着存在某个非零初态 $\pmb{x}_{0}$ 使成立

$$H _ {2} e ^ {A t} x _ {0} \equiv 0, \quad \forall t \geqslant 0 \tag {5.252}$$

利用这一事实，并注意到 $H_{1}^{T}H_{1} = H_{2}^{T}H_{2}$ ，则就可导出对此 $\pmb{x_0}$ 成立

$$
\begin{array}{l} \left(H _ {1} e ^ {A t} \boldsymbol {x} _ {0}\right) ^ {T} \left(H _ {1} e ^ {A t} \boldsymbol {x} _ {0}\right) = \left(e ^ {A t} \boldsymbol {x} _ {0}\right) ^ {T} H _ {1} ^ {T} H _ {1} \left(e ^ {A t} \boldsymbol {x} _ {0}\right) \\ = \left(e ^ {A t} x _ {0}\right) ^ {T} H _ {2} ^ {T} H _ {2} \left(e ^ {A t} x _ {0}\right) = \left(H _ {2} e ^ {A t} x _ {0}\right) ^ {T} \left(H _ {2} e ^ {A t} x _ {0}\right) \\ \equiv 0, \quad \forall t \geqslant 0 \tag {5.253} \\ \end{array}
$$

这表明,对此 $x_{0}\neq0$ 也有

$$H _ {1} e ^ {A t} x _ {0} \equiv 0, \quad \forall t \geqslant 0 \tag {5.254}$$

而这显然是和已知 $\{A, H_1\}$ 为能观测相矛盾的。所以，反设不成立，即 $\{A, H_2\}$ 也为能观测。于是，这一论断得到证明。

进一步,如果在定常的 LQ 调节问题中同时引入指定衰减度的要求,则问题的提法就

变成为:

$$\dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u}, \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0}, t \geqslant 0J (\boldsymbol {u} (\cdot)) = \int_ {0} ^ {\infty} e ^ {2 \alpha t} \left(\boldsymbol {x} ^ {T} Q \boldsymbol {x} + \boldsymbol {u} ^ {T} R \boldsymbol {u}\right) d t \tag {5.255}\lim _ {t \rightarrow \infty} x (t) e ^ {\alpha t} = 0, \quad \alpha \geqslant 0$$

其中， $\alpha$ 为指定的衰减上限，它表示在综合得到的最优调节系统中，状态 $x(t)$ 的每一个分量的衰减速度将限制为快于 $\beta_{i}e^{-\alpha t}$ ( $\beta_{i}$ 为常数)，或者等价地说闭环系统矩阵的所有特征值的实部均小于 $-\alpha$ 。现引入变量代换

$$\bar {x} = x e ^ {\alpha t}, \quad \bar {u} = u e ^ {\alpha t} \tag {5.256}$$

则通过简单的推导，就可将（5.255）所给出的问题等价地化成为一般形式的无限时间定常LQ调节问题

$$\dot {\bar {x}} = (A + \alpha I) \bar {x} + B \bar {u}, \quad \bar {x} (0) = x _ {0}J (\bar {\boldsymbol {u}} (\cdot)) = \int_ {0} ^ {\infty} \left(\bar {\boldsymbol {x}} ^ {T} Q \bar {\boldsymbol {x}} + \bar {\boldsymbol {u}} ^ {T} R \bar {\boldsymbol {u}}\right) d t \tag {5.257}$$
