$$
\mathbf {z} (t) = \mathbf {P} \overline {{{{\mathbf {z}}}}} (t) = \left[ \begin{array}{l l} 2 & 1 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{l} C _ {1} \mathrm{e} ^ {- t} \\ C _ {2} \mathrm{e} ^ {t} \end{array} \right] = \left[ \begin{array}{l} 2 C _ {1} \mathrm{e} ^ {- t} + C _ {2} \mathrm{e} ^ {t} \\ C _ {1} \mathrm{e} ^ {- t} + C _ {2} \mathrm{e} ^ {t} \end{array} \right] = C _ {1} \mathrm{e} ^ {- t} \left[ \begin{array}{l} 2 \\ 1 \end{array} \right] + C _ {2} \mathrm{e} ^ {t} \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] \tag {3.3.12}
$$

式(3.3.12)说明 $z(t)$ 是 $\overline{z}(t)$ 通过矩阵 $\pmb{P}$ 的线性变换，在通过这个线性变换之后，相轨迹将从 $\overline{z}(t) = \begin{bmatrix} \overline{z}_1(t) \\ \overline{z}_2(t) \end{bmatrix}$ 映射到 $z(t) = \begin{bmatrix} z_1(t) \\ z_2(t) \end{bmatrix}$ 上。如图3.3.8(b)所示，从直观上看，这个线性变换将 $\overline{z}_1(t)$ 和 $\overline{z}_2(t)$ 两个坐标轴沿着图中箭头的方向旋转到 $v_1$ 和 $v_2$ 上，那么相轨迹也会被相应地“拉长”与“压扁”。 $z(t)$ 的相轨迹如图3.3.8(c)所示。更为重要的是，这个线性变化不会改变平衡点的性质，因此平衡点 $z_f$ 的性质与 $\overline{z}_f$ 保持一致，是一个鞍点。这也可以通过式(3.3.12)得到验证：例如在某种初始条件下， $C_2 = 0$ ，可得 $\begin{bmatrix} z_1(t) \\ z_2(t) \end{bmatrix} = C_1 e^{-t} \begin{bmatrix} 2 \\ 1 \end{bmatrix}$ ，说明随着时间的增加， $z_1(t)$ 和 $z_2(t)$ 将沿着 $v_1 = [2,1]^T$ 这条直线向 $[0,0]^T$ 移动（相对应的指数部分为 $\lambda_1 = -1$ ）。同理，当 $C_1 = 0$ 时， $\begin{bmatrix} z_1(t) \\ z_2(t) \end{bmatrix} = \begin{bmatrix} C_2 e^t \\ C_2 e^t \end{bmatrix}$ ，这说明随着时间的增加， $z_1(t)$ 和 $z_2(t)$ 将沿着 $v_2 = [1,1]^T$ 这条直线趋于无穷（对应的指数部分为 $\lambda_2 = 1$ ）。

![](image/2dcb32a6188181b2f53b030d36bc61a817f4baeecd3bf80cd156de45ca04b3f7.jpg)

<details>
<summary>text_image</summary>

(a) z(t)的相轨迹
(b) z(t)通过矩阵P线性变换
(c) z(t)的相轨迹
</details>

图3.3.8 例3.3.2的相轨迹分析

例3.3.3 分析二阶系统 $\frac{\mathrm{dz}(t)}{\mathrm{dt}} = Az(t)$ 的相轨迹，其中 $A = \begin{bmatrix} 3 & -2 \\ 1 & 0 \end{bmatrix}$ 。

解：矩阵 $\mathbf{A}$ 的特征值为 $\left\{ \begin{array}{l} \lambda_{1} = 1 \\ \lambda_{2} = 2 \end{array} \right.$ ，因此平衡点 $z_{\mathrm{f}}$ 是一个不稳定节点。相轨迹的分析方法同例3.3.2，故不再赘述。

例3.3.4 分析二阶系统 $\frac{\mathrm{d}z(t)}{\mathrm{d}t} = Az(t)$ 的相轨迹，其中 $A = \begin{bmatrix} -3 & 2 \\ -1 & 0 \end{bmatrix}$ 。

解：矩阵 $\mathbf{A}$ 的特征值为 $\left\{ \begin{array}{l} \lambda_{1} = -1 \\ \lambda_{2} = -2 \end{array} \right.$ ，因此平衡点 $z_{\mathrm{f}}$ 是一个稳定的节点。相轨迹的分析方

法同例 3.3.2，故不再赘述。

例 3.3.3 和例 3.3.4 的相轨迹如图 3.3.9 所示，请读者自行推导。
