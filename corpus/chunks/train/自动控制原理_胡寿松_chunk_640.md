$$\alpha_ {0} ^ {\prime} (t) = 1 - (- 1) ^ {n} \frac {1}{n !} a _ {0} t ^ {n} + (- 1) ^ {n + 1} \frac {1}{(n + 1) !} a _ {n - 1} a _ {0} t ^ {n + 1} + \dots\alpha_ {1} ^ {\prime} (t) = - t - (- 1) ^ {n} \frac {1}{n !} a _ {1} t ^ {n} + (- 1) ^ {n + 1} \frac {1}{(n + 1) !} \left(a _ {n - 1} a _ {1} - a _ {0}\right) t ^ {n + 1} + \dots$$

•
•
•

$$
\begin{array}{l} \alpha_ {n - 1} ^ {\prime} (t) = (- 1) ^ {n - 1} \frac {1}{(n - 1) !} t ^ {n - 1} - (- 1) ^ {n} \frac {1}{n !} a _ {n - 1} t ^ {n} \\ + (- 1) ^ {n + 1} \frac {1}{(n + 1) !} (a _ {n - 1} ^ {2} - a _ {n - 2}) t ^ {n + 1} + \dots \\ \end{array}
$$

秩判据 线性定常连续系统(9-83)完全可控的充分必要条件是

$$
\operatorname{rank} \left[ \begin{array}{l l l l} \boldsymbol {B} & \boldsymbol {A B} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {B} \end{array} \right] = n \tag {9-104}
$$

其中，n 为矩阵 A 的维数； $S = [B \quad AB \quad \cdots \quad A^{n-1}B]$ 称为系统的可控性判别阵。

证明 充分性：已知 $\operatorname{rank} S = n$ ，欲证系统完全可控。

采用反证法。反设系统为不完全可控，则根据格拉姆矩阵判据可知

$$\boldsymbol {W} (0, t _ {1}) = \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} \boldsymbol {B} ^ {T} \mathrm{e} ^ {- \boldsymbol {A} ^ {T} t} \mathrm{d} t, \quad \forall t _ {1} > 0$$

为奇异,这意味着存在某个非零 n 维向量 $\alpha$ 使

$$
\begin{array}{l} \boldsymbol {\alpha} ^ {T} \boldsymbol {W} (0, t _ {1}) \boldsymbol {\alpha} = \int_ {0} ^ {t _ {1}} \boldsymbol {\alpha} ^ {T} e ^ {- A t} \boldsymbol {B B} ^ {T} e ^ {- A ^ {T} t} \boldsymbol {\alpha} d t \\ = \int_ {0} ^ {t _ {1}} [ \boldsymbol {\alpha} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} ] [ \boldsymbol {\alpha} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} ] ^ {\mathrm{T}} \mathrm{d} t = 0 \\ \end{array}
$$

成立。显然，由此可导出

$$\boldsymbol {\alpha} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} = \mathbf {0}, \quad \forall t \in [ 0, t _ {1} ] \tag {9-105}$$

将式(9-105)求导直至 $n - 1$ 次，再在所得结果中令 $t = 0$ ，得到

$$\boldsymbol {\alpha} ^ {T} \boldsymbol {B} = \mathbf {0}, \quad \boldsymbol {\alpha} ^ {T} \boldsymbol {A} \boldsymbol {B} = \mathbf {0}, \quad \boldsymbol {\alpha} ^ {T} \boldsymbol {A} ^ {2} \boldsymbol {B} = \mathbf {0}, \quad \dots , \quad \boldsymbol {\alpha} ^ {T} \boldsymbol {A} ^ {n - 1} \boldsymbol {B} = \mathbf {0} \tag {9-106}$$

式(9-106)又可表示为

$$
\boldsymbol {\alpha} ^ {T} \left[ \begin{array}{l l l l l} \boldsymbol {B} & \boldsymbol {A B} & \boldsymbol {A} ^ {2} \boldsymbol {B} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {B} \end{array} \right] = \boldsymbol {\alpha} ^ {T} \boldsymbol {S} = \boldsymbol {0} \tag {9-107}
$$
