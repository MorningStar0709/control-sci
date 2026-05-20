$y(t)$ 是系统输出, 是一个 m 维向量, $y(t)=\left[y_{1}(t),y_{2}(t),\cdots,y_{m}(t)\right]^{\mathrm{T}}$ ;

$u(t)$ 是系统输入, 是一个 p 维向量, $u(t)=\left[u_{1}(t),u_{2}(t),\cdots,u_{p}(t)\right]^{\mathrm{T}}$ 。

这说明, 当使用状态空间方程来描述系统时, 有 $n$ 个状态变量、 $m$ 个输出和 $p$ 个输入。它可以表达多状态、多输出、多输入的系统。其中, 矩阵 $\mathbf{A}$ 是 $n \times n$ 矩阵, 表示系统状态变量之间的关系, 称为状态矩阵或者系统矩阵。矩阵 $\mathbf{B}$ 是 $n \times p$ 矩阵, 表示输入对状态变量的影响, 称为输入矩阵或者控制矩阵。矩阵 $\mathbf{C}$ 是 $m \times n$ 矩阵, 表示系统的输出与系统状态变量之间的关系,称为输出矩阵。矩阵 D 是 $m \times p$ 矩阵,表示系统的输入直接作用在系统输出的部分,称为直接传递矩阵。状态空间方程符号说明见表 3.1.1。

表 3.1.1 状态空间方程符号说明

<table><tr><td>符号</td><td>名称</td><td>维度</td></tr><tr><td>z(t)</td><td>状态变量</td><td>n×1</td></tr><tr><td>y(t)</td><td>系统输出</td><td>m×1</td></tr><tr><td>u(t)</td><td>系统输入</td><td>p×1</td></tr><tr><td>A</td><td>状态矩阵</td><td>n×n</td></tr><tr><td>B</td><td>输入矩阵</td><td>n×p</td></tr><tr><td>C</td><td>输出矩阵</td><td>m×n</td></tr><tr><td>D</td><td>直接传递矩阵</td><td>m×p</td></tr></table>

以上述弹簧质量阻尼系统为例,参考式(3.1.6)和式(3.1.7),其状态变量 $z(t)=\begin{bmatrix}z_{1}(t)\\z_{2}(t)\end{bmatrix}$ ,是n=2维向量。输出 $y(t)=x(t)$ ,是m=1维向量。输入 $u(t)=f(t)$ ,是p=1
维向量。因此,对应的状态矩阵 $A=\begin{bmatrix}0&1\\-\frac{k}{m}&-\frac{B}{m}\end{bmatrix}$ ，是一个 $n\times n=2\times2$ 的矩阵。输入矩阵 $B=\begin{bmatrix}0\\ \frac{1}{m}\end{bmatrix}$ ，是一个 $n\times p=2\times1$ 的矩阵。输出矩阵 $C=[1\quad0]$ ，是一个 $m\times n=1\times2$ 的矩阵。直接传递矩阵D=[0]，是一个 $m\times p=1\times1$ 的矩阵。因为它只有一个输入和一个输出，所以本系统属于单输入单输出(Single Input Single Output,SISO)系统。

下面请看一个多输入多输出(Multiple Inputs Multiple Outputs, MIMO)系统的例子。

根据图3.1.2所示的电路网络，列出其状态空间方程表达式。其中，系统有两个输入 $\pmb {u}(t) = [e_1(t),e_2(t)]^{\mathrm{T}}$ 和两个输出 $\mathbf{y}(t) = [i_1(t),e_{R_3}(t)]^{\mathrm{T}}$ 。

![](image/de44a803f890fa07a19cb7278986fd2ad4599e298ffbbb39137bf885a2b9a836.jpg)

<details>
<summary>text_image</summary>

L₁
i₁(t)
R₃
eᵣ₃(t)
L₂
i₂(t)
R₁
R₂
e₁(t)
+
-
闭合回路1
闭合回路2
-
</details>

图 3.1.2 多输入多输出电路系统

若要建立上述系统的状态空间方程,首先要掌握它的动态微分方程。这个系统可以考虑成两个闭合回路,在每一个闭合回路里面使用基尔霍夫电压定律。可以得到

闭合回路1

$$L _ {1} \frac {\mathrm{d} i _ {1} (t)}{\mathrm{d} t} + i _ {1} (t) R _ {1} + e _ {R _ {3}} (t) = e _ {1} (t) \tag {3.1.9a}$$

闭合回路2

$$L _ {2} \frac {\mathrm{d} i _ {2} (t)}{\mathrm{d} t} + i _ {2} (t) R _ {2} - e _ {R _ {3}} (t) = e _ {2} (t) \tag {3.1.9b}$$

其中

$$e _ {R _ {3}} (t) = \left(i _ {1} (t) - i _ {2} (t)\right) R _ {3} \tag {3.1.9c}$$
