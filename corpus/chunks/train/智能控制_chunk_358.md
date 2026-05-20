# 1. 结构为 1-5-1 的 RBF 网络

考虑结构为1-5-1的RBF网络，取网络输入为 $x = x_{1}$ ，令 $\pmb {b} = [b_1\quad b_2\quad b_3\quad b_4\quad b_5]^{\mathrm{T}},\pmb {c} =$ $[c_{11}\quad c_{12}\quad c_{13}\quad c_{14}\quad c_{15}],\pmb {h} = [h_1\quad h_2\quad h_3\quad h_4\quad h_5]^{\mathrm{T}},\pmb {w} = [w_1\quad w_2\quad w_3\quad w_4\quad w_5]^{\mathrm{T}}$ ，则网络输出为 $y_{m}(t) = \pmb{w}^{\mathrm{T}}\pmb {h} = w_{1}h_{1} + w_{2}h_{2} + w_{3}h_{3} + w_{4}h_{4} + w_{5}h_{5}$ 。

取网络的输入为 $\sin t$ 时，网络的输出如图7-14所示，网络隐含层的输出如图7-15所示。仿真程序为 chap7\_3sim.mdl。
