# 3.2.1 矩阵的特征值与特征向量

在线性代数中, 对于一个给定的方阵 A, 它的特征向量 v 经过矩阵 A 线性变换的作用之后, 得到的新的向量仍然与原来的 v 保持在同一条直线上, 但其长度或方向也许会改变。即

$$\boldsymbol {A} \boldsymbol {v} = \lambda \boldsymbol {v} \tag {3.2.2}$$

其中， $\lambda$ 为标量，即特征向量的长度在矩阵 $\mathbf{A}$ 线性变换下缩放的比例，称为矩阵 $\mathbf{A}$ 的特征值。

首先来看线性变换,假设有一个二维矩阵 A 与一个向量 $v_{a}$ , 其中

$$
\boldsymbol {A} = \left[ \begin{array}{c c} 1 & 1 \\ 4 & - 2 \end{array} \right], \quad \boldsymbol {v} _ {\mathrm{a}} = \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] \tag {3.2.3}
$$

用矩阵 A 左乘以 $v_{a}$ ，根据矩阵的乘法法则，可得

$$
\boldsymbol {A} \boldsymbol {v} _ {\mathrm{a}} = \left[ \begin{array}{c c} 1 & 1 \\ 4 & - 2 \end{array} \right] \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] = \left[ \begin{array}{c} 1 \times 1 + 1 \times 2 \\ 4 \times 1 + (- 2) \times 2 \end{array} \right] = \left[ \begin{array}{l} 3 \\ 0 \end{array} \right] \tag {3.2.4}
$$

从 $v_{a}$ 到 $A v_{a}$ 的过程称为线性变换,如图3.2.1(a)所示。向量 $v_{a}$ 经过矩阵A线性变换后,长度发生了改变,而且不再和原向量保持在一条直线上。

![](image/c85a0a93b63a6e0cb003a23e82f5a208f66db5e38adc729220459e285591007a.jpg)

<details>
<summary>line</summary>

| v1 | v2 |
| --- | --- |
| 0 | 0 |
| 1 | 2 |
| 3 | 0 |
</details>

(a) $v_{a}$ 和 $A v_{a}$

![](image/4e917be78247e9e24355df556b6b83bf1b13e72fc534c3eeb0bab118ef2d98ac.jpg)

<details>
<summary>line</summary>

| v1 | v2 |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
</details>

(b) $v_{b}$ 和 $A v_{b}$   
图3.2.1 向量的线性变换

![](image/a29e5e51818b3eed8dd877c450fc6f45f2811a5f178bea833fc8a4fc086d32c4.jpg)

再来考虑另一个向量 $v_{b}=[1,1]^{\mathrm{T}}$ ，对它进行同样的通过矩阵A的线性变换，可得

$$
\boldsymbol {A} \boldsymbol {v} _ {\mathrm{b}} = \left[ \begin{array}{l l} 1 & 1 \\ 4 & - 2 \end{array} \right] \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] = \left[ \begin{array}{l} 2 \\ 2 \end{array} \right] = 2 \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] = \lambda \boldsymbol {v} _ {\mathrm{b}} \tag {3.2.5}
$$

式(3.2.5)说明通过矩阵 A 线性变换后, $A v_{b} = \lambda v_{b} = 2v_{b}$ 。如图 3.2.1(b) 所示, 经过变换后的新向量与原向量在一条直线上, 但是长度发生了改变。根据定义, $v_{b}$ 是矩阵 A 的特征向量, 缩放比例 $\lambda = 2$ 则是矩阵 A 对应于特征向量 $v_{b}$ 的特征值。

现在以矩阵 A 为例,说明如何求解特征值与特征向量。根据式(3.2.2),可得

$$\boldsymbol {A} \boldsymbol {v} - \lambda \boldsymbol {v} = 0\Rightarrow (\boldsymbol {A} - \lambda \boldsymbol {I}) \boldsymbol {v} = 0 \tag {3.2.6}$$

其中，I 为单位矩阵，维度与 A 相同。根据矩阵理论，如果式(3.2.6)有非零解，则矩阵 $(A-\lambda I)$ 的行列式必须为零，即

$$\mid \boldsymbol {A} - \lambda \boldsymbol {I} \mid = 0 \tag {3.2.7}$$
