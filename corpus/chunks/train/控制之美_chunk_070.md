![](image/b5e0755d97e79c71b36fe7dbf7f8b442fe5329a7e858b58754f4c732b8f610d9.jpg)

<details>
<summary>text_image</summary>

z₂(t)
O
z₁(t)
</details>

(a)例3.3.3的相轨迹

![](image/59e4e315d4a1b3617cc738118602bb15a6b8c5d508f4d34b3dcdde606460e019.jpg)

<details>
<summary>text_image</summary>

z₂(t)
O
z₁(t)
</details>

(b) 例3.3.4的相轨迹  
图3.3.9 例3.3.3与例3.3.4的相轨迹分析

例3.3.5 分析二阶系统 $\frac{\mathrm{d}z(t)}{\mathrm{d}t} = Az(t)$ 的相轨迹，其中 $A = \begin{bmatrix} 0 & 4 \\ -1 & 0 \end{bmatrix}$ 。

解：首先求解矩阵 A 的特征值与特征向量，可得

$$
\left\{ \begin{array}{l} \lambda_ {1} = 2 j \\ \lambda_ {2} = - 2 j \end{array} , \quad \left\{ \begin{array}{l} v _ {1} = \left[ \begin{array}{c} 2 \\ j \end{array} \right] \\ v _ {2} = \left[ \begin{array}{c} 2 \\ - j \end{array} \right] \end{array} \right. \right. \tag {3.3.13}
$$

式(3.3.13)说明矩阵 A 的特征值是一对共轭复数,而且它不存在实数特征向量(特征向量无法在相平面中表达出来)。前面例子的处理方法将无法使用,因此需要从解入手分析。首先令 $z(t)=P\bar{z}(t)$ , 其中 $P=\left[v_{1},v_{2}\right]=\begin{bmatrix}2 & 2 \\ j & -j\end{bmatrix}$ , 可得

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} \overline {{z}} _ {1} (t) \\ \overline {{z}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} 2 \mathrm{j} & 0 \\ 0 & - 2 \mathrm{j} \end{array} \right] \overline {{z}} (t) \tag {3.3.14}
$$

式(3.3.14)的解为

$$
\overline {{{z}}} (t) = \left[ \begin{array}{l} \overline {{{z}}} _ {1} (t) \\ \overline {{{z}}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{l} C _ {1} \mathrm{e} ^ {\mathrm{j} 2 t} \\ C _ {2} \mathrm{e} ^ {- \mathrm{j} 2 t} \end{array} \right] \tag {3.3.15}
$$

根据欧拉公式 $\mathrm{e}^{\mathrm{j}t} = \cos t + \mathrm{j}\sin t$ ，式(3.3.15)可以写成

$$
\overline {{{z}}} (t) = \left[ \begin{array}{l} \overline {{{z}}} _ {1} (t) \\ \overline {{{z}}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{l} C _ {1} \cos 2 t + C _ {1} \mathrm{j} \sin 2 t \\ C _ {2} \cos 2 t - C _ {2} \mathrm{j} \sin 2 t \end{array} \right] \tag {3.3.16}
$$

将式(3.3.16)代入 $z(t)=P\bar{z}(t)$ ，可得
