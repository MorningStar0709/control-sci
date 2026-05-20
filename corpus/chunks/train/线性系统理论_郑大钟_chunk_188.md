其中， $\dim(\boldsymbol{u})=\dim(\boldsymbol{y})=p,\{A,B\}$ 为能控。再规定以实现解耦为主要综合目标，同时对解耦后的每一个单输入-单输出控制系统要实现期望的极点配置。

第1步：计算 $\{d_{i}, i=1,2,\cdots,p\}$ 和 $\{E_{i}=c_{i}A^{d_{i}}B, i=1,2,\cdots,p\}$ 。判断 $E^{T}=[E_{1}^{T},\cdots,E_{p}^{T}]$ 是否为非奇异。若是，可解耦，进入下一步。若否，不能解耦，退出计算。

第2步：计算 $E^{-1}$ 和

$$
F \triangleq \left[ \begin{array}{c} \mathbf {c} _ {1} A ^ {d _ {1} + 1} \\ \vdots \\ \mathbf {c} _ {p} A ^ {d _ {p} + 1} \end{array} \right]
$$

第3步：取 $\{\overline{L},\overline{K}\}$ 为

导出积分型解耦系统：

$$\bar {L} = E ^ {- 1}, \quad \bar {K} = E ^ {- 1} F\dot {\boldsymbol {x}} = \bar {A} \boldsymbol {x} + \bar {B} \boldsymbol {v}y = C x$$

其中， $\overline{A}=A-BE^{-1}F,\quad\overline{B}=BE^{-1}$ ，且由 $\{A,B\}$ 能控知 $\{\overline{A},\overline{B}\}$ 为能控。

第4步：引入线性非奇异变换 $\pmb{x} = Q\pmb{x}$ ，把 $\{\overline{A},\overline{B},C\}$ 变换为如下的解耦规范形：

$$
\widetilde {A} = \left[ \begin{array}{c c c c} \widetilde {A} _ {1} & & & 0 \\ & \ddots & & \vdots \\ & & \widetilde {A} _ {p} & 0 \\ \hline \widetilde {A} _ {c 1} & \dots & \widetilde {A} _ {c p} & \widetilde {A} _ {p + 1} \end{array} \right]

\tilde {B} = \left[ \begin{array}{c c c} \tilde {b} _ {1} & & \\ & \ddots & \\ & & \tilde {b} _ {p} \\ \hline \tilde {b} _ {c 1} & \dots & \tilde {b} _ {c p} \end{array} \right]

\widetilde {C} = \left[ \begin{array}{c c c c} \tilde {\mathbf {c}} _ {1} & & & 0 \\ & \ddots & & \vdots \\ & & \ddots & \\ & & \tilde {\mathbf {c}} _ {p} & 0 \end{array} \right]
$$

其中，虚线分块化表示按能观测性的结构分解形式 $^{①}$ ，当 $\{\bar{A}, C\}$ 为能观测时则 $\{\tilde{A}, \tilde{B}, \tilde{C}\}$ 中不出现不能观测部分。此外，进而有：

$$
\widetilde {A} _ {i} = \underbrace {\left[ \begin{array}{c c c c} 0 & & & \\ \vdots & I _ {d _ {i}} & & \\ 0 & & & \\ - & & & \\ 0 & 0 \cdots 0 & & \\ - & * & & \\ \hline (d _ {i} + 1) & & m _ {i} - (d _ {i} + 1) \end{array} \right]} _ {(d _ {i} + 1)} \left. \begin{array}{l} 0 \\ * \\ * \end{array} \right\} m _ {i} - (d _ {i} + 1)

\begin{array}{l} \tilde {b} _ {i} = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \\ 0 \\ \vdots \\ 0 \end{array} \right] \leftarrow (d _ {i} + 1) \\ \tilde {c} _ {i} = [ 1 \quad 0 \dots 0 ] \end{array}
$$

其中， $m_{i} \geqslant d_{i} + 1$ ， $m_{1} + m_{2} + \cdots + m_{p+1} = n_{0}$

第5步：对解耦规范形 $\{\tilde{A},\tilde{B},\tilde{C}\}$ ，引入状态反馈，来实现解耦控制和解耦后的单输入-单输出控制系统的极点配置。状态反馈增益矩阵取为如下形式的 $p\times n$ 常阵：

$$
\widetilde {K} = \left[ \begin{array}{c c c} \tilde {\boldsymbol {k}} _ {1} & & 0 \\ & \ddots & \vdots \\ & \tilde {\boldsymbol {k}} _ {p} & 0 \end{array} \right]
$$

其中
