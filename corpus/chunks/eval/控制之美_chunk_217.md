$$\frac {1}{x (t)} = \frac {1}{x _ {\mathrm{f}}} + \frac {\mathrm{d} f (x (t))}{\mathrm{d} x (t)} \Bigg | _ {x = x _ {\mathrm{f}}} (x (t) - x _ {\mathrm{f}}) = \frac {1}{x _ {\mathrm{f}}} - \frac {1}{x _ {\mathrm{f}} ^ {2}} x _ {\delta} (t) \tag {A.5}$$

代入 $x_{\mathrm{f}} = 1$ ，得到

$$\frac {1}{x (t)} = 1 - x _ {\delta} (t) \tag {A.6}$$

将 $x(t) - x_{\mathrm{f}} = x_{\delta}(t)$ 与式(A.6)代入式(A.4)，得到

$$
\begin{array}{l} \frac {\mathrm{d} ^ {2} \left(x _ {\mathrm{f}} + x _ {\delta} (t)\right)}{\mathrm{d} t ^ {2}} + \frac {\mathrm{d} \left(x _ {\mathrm{f}} + x _ {\delta} (t)\right)}{\mathrm{d} t} + 1 - x _ {\delta} (t) = 1 \\ \Rightarrow \frac {\mathrm{d} ^ {2} x _ {\delta} (t)}{\mathrm{d} t ^ {2}} + \frac {\mathrm{d} x _ {\delta} (t)}{\mathrm{d} t} - x _ {\delta} (t) = 0 \tag {A.7} \\ \end{array}
$$

式(A.7)即为非线性系统在平衡点 $x_{f}=1$ 附近的线性化方程。

考虑使用状态空间方程表达的非线性动态系统,定义为

$$\frac {\mathrm{d} z (t)}{\mathrm{d} t} = f (z (t)) \tag {A.8}$$

其中， $f()$ 是非线性运算， $z(t)=\left[z_{1}(t),z_{2}(t),\cdots,z_{n}(t)\right]^{T}$ 是状态变量。其平衡点为 $z_{f}$ ，在平衡点附近的线性化为

$$
\frac {\mathrm{d} \mathbf {z} _ {\delta} (t)}{\mathrm{d} t} = \left[ \begin{array}{c c c} \frac {\partial f _ {1}}{\partial z _ {1} (t)} & \dots & \frac {\partial f _ {1}}{\partial z _ {n} (t)} \\ \vdots & \ddots & \vdots \\ \frac {\partial f _ {n}}{\partial z _ {1} (t)} & \dots & \frac {\partial f _ {n}}{\partial z _ {n} (t)} \end{array} \right] \Bigg | _ {z = z _ {\mathrm{f}}} \mathbf {z} _ {\delta} (t) \tag {A.9}
$$

其中， $\begin{bmatrix}\frac{\partial f_{1}}{\partial z_{1}(t)}&\cdots&\frac{\partial f_{1}}{\partial z_{n}(t)}\\\vdots&\ddots&\vdots\\\frac{\partial f_{n}}{\partial z_{1}(t)}&\cdots&\frac{\partial f_{n}}{\partial z_{n}(t)}\end{bmatrix}$ 为 $n\times n$ 矩阵，称为雅可比矩阵(Jacobi Matrix)。

以式(A.4)为例,将它写成状态空间方程,令 $z_{1}(t)=x(t)$ , $z_{2}(t)=\frac{\mathrm{d}x(t)}{\mathrm{d}t}$ , 得到

$$\frac {\mathrm{d} z _ {1} (t)}{\mathrm{d} t} = z _ {2} (t) = f _ {1} (z (t)) \tag {A.10a}\frac {\mathrm{d} z _ {2} (t)}{\mathrm{d} t} = 1 - \frac {1}{z _ {1} (t)} - z _ {2} (t) = f _ {2} (z (t)) \tag {A.10b}$$

求它的平衡点，令 $\frac{\mathrm{d}z_1(t)}{\mathrm{d}t} = \frac{\mathrm{d}z_2(t)}{\mathrm{d}t} = 0$ ，得到

$$
\left\{ \begin{array}{l} 0 = z _ {2} (t) \\ 0 = 1 - \frac {1}{z _ {1} (t)} - z _ {2} (t) \end{array} \right.

\Rightarrow \left\{ \begin{array}{l} z _ {1 \mathrm{f}} = 1 \\ z _ {2 \mathrm{f}} = 0 \end{array} \right. \tag {A.11}
$$

使用式(A.9)，其雅可比矩阵为
