# 3.4.3 模糊关系的合成

所谓合成,即由两个或两个以上的关系构成一个新的关系。模糊关系也存在合成运算,是通过模糊矩阵的合成进行的。

R 和 S 分别为 $U \times V$ 和 $V \times W$ 上的模糊关系，而 R 和 S 的合成是 $U \times W$ 上的模糊关系，记为 $R \circ S$ ，其隶属函数为

$$\mu_ {R \cdot S} (u, w) = \bigvee_ {v \in V} \{\mu_ {R} (u, v) \wedge \mu_ {S} (v, w) \}, u \in U, w \in W \tag {3.26}$$

【例3.8】设 $\mathbf{A} = \begin{bmatrix} a_{11} & a_{12}\\ a_{21} & a_{22} \end{bmatrix},\mathbf{B} = \begin{bmatrix} b_{11} & b_{12}\\ b_{21} & b_{22} \end{bmatrix}$ ，则 $C = A\circ B = \begin{bmatrix} c_{11} & c_{12}\\ c_{21} & c_{22} \end{bmatrix}$ ，其中

$$c _ {1 1} = (a _ {1 1} \wedge b _ {1 1}) \vee (a _ {1 2} \wedge b _ {2 1})c _ {1 2} = \left(a _ {1 1} \wedge b _ {1 2}\right) \vee \left(a _ {1 2} \wedge b _ {2 2}\right)c _ {2 1} = \left(a _ {2 1} \wedge b _ {1 1}\right) \vee \left(a _ {2 2} \wedge b _ {2 1}\right)c _ {2 2} = \left(a _ {2 1} \wedge b _ {1 2}\right) \vee \left(a _ {2 2} \wedge b _ {2 2}\right)$$

当 $\mathbf{A} = \begin{bmatrix} 0.8 & 0.7 \\ 0.5 & 0.3 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 0.2 & 0.4 \\ 0.6 & 0.9 \end{bmatrix}$ 时，有

$$
\mathbf {A} \circ \mathbf {B} = \left[ \begin{array}{l l} 0. 6 & 0. 7 \\ 0. 3 & 0. 4 \end{array} \right]

\boldsymbol {B} \circ \boldsymbol {A} = \left[ \begin{array}{l l} 0. 4 & 0. 3 \\ 0. 6 & 0. 6 \end{array} \right]
$$

可见， $A \circ B \neq B \circ A$ 。

采用 Matlab 可实现模糊矩阵的合成,仿真程序见附录程序 chap3\_4.m。

【例 3.9】某家中子女和父母的长相“相似关系”R 为模糊关系, 可表示为

<table><tr><td></td><td>父</td><td>母</td></tr><tr><td>子</td><td>0.2</td><td>0.8</td></tr><tr><td>女</td><td>0.6</td><td>0.1</td></tr></table>

用模糊矩阵 $\pmb{R}$ 表示为

$$
\boldsymbol {R} = \left[ \begin{array}{l l} 0. 2 & 0. 8 \\ 0. 6 & 0. 1 \end{array} \right]
$$

父母与祖父的“相似关系”S也是模糊关系,可表示为

<table><tr><td></td><td>祖父</td><td>祖母</td></tr><tr><td>父</td><td>0.5</td><td>0.7</td></tr><tr><td>母</td><td>0.1</td><td>0</td></tr></table>

用模糊矩阵 S 表示为

$$
\mathbf {S} = \left[ \begin{array}{c c} 0. 5 & 0. 7 \\ 0. 1 & 0 \end{array} \right]
$$

那么在该家中,孙子、孙女与祖父、祖母的相似程度应该如何呢?

模糊关系的合成运算为

$$
\begin{array}{l} \boldsymbol {R} \circ \boldsymbol {S} = \left[ \begin{array}{l l} 0. 2 & 0. 8 \\ 0. 6 & 0. 1 \end{array} \right] \circ \left[ \begin{array}{l l} 0. 5 & 0. 7 \\ 0. 1 & 0 \end{array} \right] \\ = \left[ \begin{array}{l l} (0. 2 \wedge 0. 5) \vee (0. 8 \wedge 0. 1) & (0. 2 \wedge 0. 7) \vee (0. 8 \wedge 0) \\ (0. 6 \wedge 0. 5) \vee (0. 1 \wedge 0. 1) & (0. 6 \wedge 0. 7) \vee (0. 1 \wedge 0) \end{array} \right] \\ = \left[ \begin{array}{l l} 0. 2 & 0. 2 \\ 0. 5 & 0. 6 \end{array} \right] \\ \end{array}
$$

该结果表明,孙子与祖父、祖母的相似程度分别为 0.2 和 0.2,而孙女与祖父、祖母的相似程度分别为 0.5 和 0.6。
