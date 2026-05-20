$$
\hat {\boldsymbol {A}} ^ {*} = \left[ \begin{array}{c c c} \tilde {\boldsymbol {A}} _ {1 1} & \phi & \phi \\ \tilde {\boldsymbol {A}} _ {2 1} & \tilde {\boldsymbol {A}} _ {2 2} & \tilde {\boldsymbol {A}} _ {2 3} \\ \tilde {\boldsymbol {A}} _ {3 1} & \tilde {\boldsymbol {A}} _ {3 2} & \tilde {\boldsymbol {A}} _ {3 3} \end{array} \right], \tag {11.9.10}
$$

其中 $\hat{A}_{ij}$ 可根据前述求 $A^{*}$ 的图论算法得到。于是式(11.9.9)变为

$$
\left[ \begin{array}{l l l} \tilde {A} _ {1 1} & \phi & \phi \\ \tilde {A} _ {2 1} & \tilde {A} _ {2 2} & \tilde {A} _ {2 3} \\ \tilde {A} _ {3 1} & \tilde {A} _ {3 2} & \tilde {A} _ {3 3} \end{array} \right] \left[ \begin{array}{l} \phi \\ \phi \\ y _ {3} \end{array} \right] \oplus \hat {\boldsymbol {A}} ^ {*} \left[ \begin{array}{l} v _ {1} \\ v _ {2} \\ v _ {3} \end{array} \right] = \left[ \begin{array}{l} y _ {1} \\ y _ {2} \\ y _ {3} \end{array} \right]. \tag {11.9.11}
$$

由上式可知 y 的 3 类分量 $y_{1}, y_{2}, y_{3}$ 可由以下 3 种不同途径求得. 首先求解 $y_{3}$ ，由上式得

$$\tilde {A} _ {3 3} y _ {3} \oplus [ \tilde {A} _ {3 1} \tilde {A} _ {3 2} \tilde {A} _ {3 3} ] \hat {v} = y _ {3}. \tag {11.9.12}$$

所以最小解为

$$\boldsymbol {y} _ {3} = \widetilde {\boldsymbol {A}} _ {3 3} ^ {*} [ \widetilde {\boldsymbol {A}} _ {3 1} \quad \widetilde {\boldsymbol {A}} _ {3 2} \quad \widetilde {\boldsymbol {A}} _ {3 3} ] \widehat {\boldsymbol {v}}. \tag {11.9.13}$$

由于受控变迁的数目 $N$ 一般要比全部变迁的数目 $n$ 小得多，因而求解式 (11.9.13) 要比求解式 (11.9.7) 简单.

求得 $y_{3}$ 后，再应用式 (11.9.11) 可得 $y_{2}$ .

$$\boldsymbol {y} _ {2} = \widetilde {\boldsymbol {A}} _ {2 3} \boldsymbol {y} _ {3} \oplus [ \widetilde {\boldsymbol {A}} _ {2 1} \widetilde {\boldsymbol {A}} _ {2 2} \widetilde {\boldsymbol {A}} _ {2 3} ] \widehat {\boldsymbol {v}}. \tag {11.9.14}$$

至于 $\pmb{y}_1$ ，由式(11.9.11)可知

$$\boldsymbol {y} _ {1} = \widetilde {\boldsymbol {A}} _ {1 1} \boldsymbol {v} _ {1}, \tag {11.9.15}$$

即对应于不能达分量部分的 $y_{1}$ 与 $y_{2}, y_{3}$ 无关. $y_{2}, y_{1}$ 的计算不必解方程，一般比求解式 (11.9.7) 简单.

综上所述，我们证明了以下定理：

定理 11.9.6 $^{[6]}$ 系统 (11.9.5) 的最小能控序列，即方程 (11.9.6) 的最小解 $y = [y_{1}, y_{2}, y_{3}]^{T}$ 的分量有不同的 3 类，仅 $y_{3}$ 需从 N 阶方程 (11.9.12) 解出，其解如式 (11.9.13) 所示； $y_{2}$ 可用式 (11.9.14) 直接由 $y_{3}$ 算出； $y_{1}$ 与 $y_{2}, y_{3}$ 无关，可从式 (11.9.15) 算出。各式中的参数阵由式 (11.9.8)、(11.9.9)、(11.9.10) 定义。

下面简要地介绍一下监控理论中的另一些结果，但略去所有定理的证明.

如11.1节中所述，自动机方法研究了事件串的集合-语言，所谓监控是设法使系统产生的语言在某个目标语言之中，并逼近它．文献[19]研究了ETEG的监控，但代替语言的是时间序列集，因而提出如下概念：

定义11.9.6 考察系统(11.9.5). 易知解为 $x = A^{*}(I_{c}y \oplus v)$ . 若一个序列集 $Y$ 满足
