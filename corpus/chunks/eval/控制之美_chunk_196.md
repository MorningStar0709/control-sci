$$
\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] \boldsymbol {z} (t) + \boldsymbol {B} (- k \boldsymbol {y} (t)) = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] \boldsymbol {z} (t) + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] (- k) [ 1, 0 ] \boldsymbol {z} (t)
$$

![](image/36e6f0731ff108002b8c5d9f6b9614d398813f885f1363fe0cad403d46ab9381.jpg)

<details>
<summary>text_image</summary>

z₂(t)
Oₜ
z₁(t)
</details>

图10.3.1 无输入系统 $u(t) = 0$ 的相轨迹

$$
= \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] z (t) + \left[ \begin{array}{l l} 0 & 0 \\ - k & 0 \end{array} \right] z (t) = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} - k & 0 \end{array} \right] z (t) \tag {10.3.6}
$$

其中, 矩阵 $\left[ \begin{array}{ll} 0 & 1 \\ \frac{g}{d} - k & 0 \end{array} \right]$ 的两个特征值分别为 $\pm \sqrt{\frac{g}{d} - k}$ 。当 $\frac{g}{d} > k$ 时, 特征值依然是一正一负; 而当 $\frac{g}{d} < k$ 时, 特征值为两个共轭纯虚数。这说明仅仅通过输出 $y(t)$ 的比例反馈是无法使系统稳定的。

此结论与图 10.1.2(a)、(b) 通过根轨迹的方法得出的结论一致, 即随着 $k$ 的增加, 闭环传递函数的极点从一正一负移动到虚轴上两个共轭的位置。请读者体会这两种方法的相似之处。

上述分析说明只依靠输出的比例反馈控制不能满足设计要求,所以需要考虑设计全状态反馈控制器,可以令

$$
\pmb {u} (t) = - \pmb {K z} (t), \quad \text {其中}, \pmb {K} = \left[ \begin{array}{c c} k _ {1} & k _ {2} \end{array} \right] \tag {10.3.7}
$$

此时的输入 $u(t)$ 与所有状态变量 $\pmb{z}(t)$ 有关。将式(10.3.7)代入式(10.3.1a)，可得

$$
\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) - \boldsymbol {B} \boldsymbol {K} \boldsymbol {z} (t) = (\boldsymbol {A} - \boldsymbol {B} \boldsymbol {K}) \boldsymbol {z} (t) = \boldsymbol {A} _ {\mathrm{cl}} \boldsymbol {z} (t) \tag {10.3.8a}
$$

其中, $A_{cl}=A-BK$ ,代表闭环控制系统的状态矩阵。称其为闭环控制系统是因为它将状态反馈集成到系统之中。在本例中

$$
\mathbf {A} _ {\mathrm{cl}} = \mathbf {A} - \mathbf {B K} = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] - \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \left[ \begin{array}{l l} k _ {1} & k _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ \frac {g}{d} - k _ {1} & - k _ {2} \end{array} \right] \tag {10.3.8b}
$$

令 $\left|A_{cl}-\lambda I\right|=0$ ，可以求其特征值，得到

$$
\left| \begin{array}{c c} - \lambda & 1 \\ \frac {g}{d} - k _ {1} & - k _ {2} - \lambda \end{array} \right| = 0 \tag {10.3.9a}
$$

即

$$
(- \lambda) \left(- k _ {2} - \lambda\right) - \left(\frac {g}{d} - k _ {1}\right) \times (1) = 0
$$
