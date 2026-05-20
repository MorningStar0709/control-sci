进而，定义输入 $\bar{u} \triangleq (\bar{A}_{21}y + \bar{B}_2u)$ 和输出 $w \triangleq \dot{y} - \bar{A}_{11}y - \bar{B} u$ ，那么还可把(5.329)表示为如下的规范形式：

$$
\begin{array}{l} \dot {\bar {x}} _ {1} = \overline {{A}} _ {2 2} \bar {x} _ {2} + \bar {u} \\ w = \overline {{A}} _ {1 2} \bar {x} _ {2} \end{array} \tag {5.330}
$$

并且， $\{\overline{A}_{11},\overline{A}_{12}\}$ 为能观测的充分必要条件是 $\{A,C\}$ 为能观测。

(4) 对 $(n-q)$ 维子系统 (5.330) 构造全维状态观测器。由 $\{\overline{A}_{22}, \overline{A}_{12}\}$ 为能观测，故知此 $(n-q)$ 维状态观测器必存在，其形式为：

$$\dot {\hat {x}} _ {2} = \left(\bar {A} _ {1 1} - \bar {L} \bar {A} _ {1 2}\right) \hat {x} _ {2} + \bar {L} w + \bar {u} \tag {5.331}$$

并且可通过选取 $\overline{L}$ 而任意配置 $(\overline{A}_{22} - \overline{L}\overline{A}_{12})$ 的全部特征值。再将 $\bar{\pmb{u}}$ 和 $\pmb{w}$ 的定义式代入(5.331)，可得：

$$\hat {\boldsymbol {x}} _ {2} = \left(\bar {A} _ {2 2} - \bar {L} \bar {A} _ {1 2}\right) \hat {\boldsymbol {x}} _ {2} + \bar {L} \left(\dot {\mathbf {y}} - \bar {A} _ {1 1} \mathbf {y} - \bar {B} _ {1} \mathbf {u}\right) + \left(\bar {A} _ {2 1} \mathbf {y} + \bar {B} _ {2} \mathbf {u}\right) \tag {5.332}$$

易见上式中包含输出的导数 $\dot{\pmb{y}}$ ，从抗扰动性的角度而言这是不希望的。为此，通过引入

$$\boldsymbol {z} = \hat {\boldsymbol {x}} _ {2} - \bar {L} \boldsymbol {y} \tag {5.333}$$

而来达到在观测器方程中消去 $\dot{\pmb{y}}$ 的目的。这样，由（5.333）和（5.332）就可导出：

$$
\begin{array}{l} \dot {z} = \dot {\hat {x}} _ {1} - \bar {L} \dot {y} = (\bar {A} _ {2 2} - \bar {L} \bar {A} _ {1 2}) \hat {x} _ {2} + (\bar {A} _ {2 1} - \bar {L} \bar {A} _ {1 1}) y + (\bar {B} _ {2} - \bar {L} \bar {B} _ {1}) u \\ = \left(\bar {A} _ {2 2} - \bar {L} \bar {A} _ {1 2}\right) z + \left[ \left(\bar {A} _ {2 2} - \bar {L} \bar {A} _ {1 2}\right) \bar {L} + \left(\bar {A} _ {2 1} - \bar {L} \bar {A} _ {1 1}\right) \right] y \\ + \left(\bar {B} _ {2} - L \bar {B} _ {1}\right) u \tag {5.334} \\ \end{array}
$$

可以看出，这是一个以 $\pmb{u}$ 和 $\pmb{y}$ 为输入的 $(n - q)$ 维动态系统，且 $(\overline{A}_{22} - \overline{L}\overline{A}_{12})$ 的特征值是可以任意配置的。而且， $\overline{x}_2$ 的重构状态即为：

$$\hat {x} _ {2} = z + \bar {L} y \tag {5.335}$$

(5) 对于变换状态 $\vec{x}$ 的重构状态 $\vec{x}$ , 可容易导出为:

$$
\hat {\bar {x}} = \left[ \begin{array}{l} \hat {\bar {x}} _ {1} \\ \hat {\bar {x}} _ {2} \end{array} \right] = \left[ \begin{array}{c} y \\ z + \bar {L} y \end{array} \right] \tag {5.336}
$$

并且，考虑到 $x = P^{-1}\bar{x} = Q\bar{x}$ ，所以相应地也有 $\hat{x} = Q\hat{x}$ ，于是进而可定出系统状态 $x$ 的重构状态 $\hat{x}$ 为：
