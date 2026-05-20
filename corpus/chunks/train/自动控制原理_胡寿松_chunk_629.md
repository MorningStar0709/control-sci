y (k) = \left[ \begin{array}{l l l l} \beta_ {0} & \beta_ {1} & \dots & \beta_ {n - 1} \end{array} \right] x (k) + b _ {n} u (k) \tag {9-66b}
$$

简记为

$$\boldsymbol {x} (k + 1) = \boldsymbol {G x} (k) + \boldsymbol {h u} (k) \tag {9-67a}y (k) = c x (k) + d u (k) \tag {9-67b}$$

式中，G 为友矩阵；G,h 为可控标准型。可以看出，离散系统状态方程描述了 $(k+1)T$ 时刻的状态与kT时刻的状态及输入量之间的关系，其输出方程描述了kT时刻的输出量与kT时刻的状态及输入量之间的关系。

线性定常多输入-多输出离散系统的动态方程为

$$\boldsymbol {x} (k + 1) = \boldsymbol {G x} (k) + \boldsymbol {H u} (k) \tag {9-68a}\mathbf {y} (k) = \mathbf {C x} (k) + \mathbf {D u} (k) \tag {9-68b}$$

系统结构图如图9-3所示，图中 $z^{-1}$ 为单位延迟器，其输入为 $(k + 1)T$ 时刻的状态，输出为延迟一个采样周期的 $kT$ 时刻的状态。
