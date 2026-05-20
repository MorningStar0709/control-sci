# 3.2 线性连续时间系统的能控性判据

本节讨论连续时间的线性系统的能控性判别问题，给出可直接利用系统的系数矩阵判定其能控性的一些准则。为了使讨论易于理解，我们首先研究线性定常系统的能控性判据，随后再推广导出线性时变系统的能控性判据。

线性定常系统的能控性判据 考虑线性定常系统的状态方程

$$\dot {x} = A x + B u, x (0) = x _ {0}, t \geqslant 0 \tag {3.7}$$

其中，x 为 n 维状态向量，u 为 p 维输入向量，A 和 B 分别为 $n \times n$ 和 $n \times p$ 常阵。下面，我们来给出直接根据 A 和 B 以判别系统的能控性的一些常用判据。

结论1[格拉姆矩阵判据] 线性定常系统（3.7）为完全能控的充分必要条件是，存在时刻 $t_1 > 0$ ，使如下定义的格拉姆（Gram）矩阵

$$W _ {c} [ 0, t _ {1} ] \triangleq \int_ {0} ^ {t _ {1}} e ^ {- A t} B B ^ {T} e ^ {- A ^ {T} t} d t. \tag {3.8}$$

为非奇异。

证 充分性：已知 $W_{c}[0, t_{1}]$ 非奇异，欲证系统为完全能控。

采用构造性方法来证明。已知 $W_{c}$ 非奇异，故 $W_{c}^{-1}$ 存在，由此对任一非零初始状态 $\pmb{x_0}$ 可构造控制 $\pmb{u}(t)$ 为：

$$\boldsymbol {u} (t) = - B ^ {T} e ^ {- A ^ {T} t} W _ {c} ^ {- 1} \left[ 0, t _ {1} \right] \boldsymbol {x} _ {0}, t \in [ 0, t _ {1} ] \tag {3.9}$$

而 $\boldsymbol{u}(t)$ 作用下系统状态 $\boldsymbol{x}(t)$ 在 $t_{1}$ 时刻的结果为：

$$
\begin{array}{l} \boldsymbol {x} \left(t _ {1}\right) = e ^ {A t _ {1}} \boldsymbol {x} _ {0} + \int_ {0} ^ {t _ {1}} e ^ {A \left(t _ {1} - t\right)} B \boldsymbol {u} (t) d t \\ = e ^ {A t _ {1}} x _ {0} - e ^ {A t _ {1}} \int_ {0} ^ {t _ {1}} e ^ {- A t} B B ^ {T} e ^ {- A ^ {T} t} d t W _ {e} ^ {- 1} [ 0, t _ {1} ] x _ {0} \\ = e ^ {A t _ {1}} x _ {0} - e ^ {A t _ {1}} W _ {c} [ 0, t _ {1} ] W _ {c} ^ {- 1} [ 0, t _ {1} ] x _ {0} \\ = e ^ {A t _ {1}} x _ {0} - e ^ {A t _ {1}} x _ {0} = 0, \quad \forall x _ {0} \in \mathcal {R} ^ {n} \tag {3.10} \\ \end{array}
$$

这表明，对任一 $x_0 \neq 0$ ，存在有限时刻 $t_1 > 0$ 和控制 $\pmb{u}(t)$ ，使状态由 $x_0$ 转移到 $t_1$ 时刻 $\pmb{x}(t_1) = 0$ 。于是，按定义可知系统为完全能控。充分性得证。

必要性：已知系统为完全能控，欲证 $W_{c}[0,t_{1}]$ 非奇异。

采用反证法。反设 $W_{e}$ 为奇异，也即反设存在某个非零 $\overline{x}_0\in \mathcal{R}^n$ ，使成立

$$\bar {x} _ {0} ^ {T} W _ {c} [ 0, t _ {1} ] \bar {x} _ {0} = 0 \tag {3.11}$$

由此，进而有

$$
\begin{array}{l} 0 = \bar {x} _ {0} ^ {T} W _ {c} [ 0, t _ {1} ] \bar {x} _ {0} = \int_ {0} ^ {t _ {1}} \bar {x} _ {0} ^ {T} e ^ {- A t} B B ^ {T} e ^ {- A ^ {T} t} \bar {x} _ {0} d t \\ = \int_ {0} ^ {t _ {1}} \left[ B ^ {T} e ^ {- A ^ {T} t} \bar {\mathbf {x}} _ {0} \right] ^ {T} \left[ B ^ {T} e ^ {- A ^ {T} t} \bar {\mathbf {x}} _ {0} \right] d t \\ = \int_ {0} ^ {t _ {1}} \| B ^ {T} e ^ {- A ^ {T} t} \bar {x} _ {0} \| ^ {2} d t \tag {3.12} \\ \end{array}
$$

其中 $\| \cdot \|$ 为范数，故其必为正值。这样，欲上式成立，应当有

$$B ^ {T} c ^ {- A ^ {T} t} \vec {x} _ {0} = 0, \quad \forall t \in [ 0, t _ {1} ] \tag {3.13}$$

另一方面，因系统为完全能控，所以对此非零 $\tilde{\pmb{x}}_0$ 又应成立

$$0 = x \left(t _ {1}\right) = e ^ {A t _ {1}} \bar {x} _ {0} + \int_ {0} ^ {t _ {1}} e ^ {A t _ {1}} e ^ {- A t} B u (t) d t \tag {3.14}$$

从而，由此又可导出
