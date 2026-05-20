$$
\begin{array}{l} \hat {x} ^ {o} = \left[ \begin{array}{c} \xi_ {1} ^ {(k _ {1})} \\ \vdots \\ \xi_ {1} ^ {(1)} \\ - - - - \\ \vdots \\ - - - - \\ \xi_ {p} ^ {(k _ {p})} \\ \vdots \\ \xi_ {p} ^ {(1)} \end{array} \right] = \left[ \begin{array}{c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c} 0 & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & \\ 1 & \ddots & \ddots & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & \\ 1 & \ddots & \ddots & \ddots & & & & & & & & & & & & & & & & & & & & & & & & & & & & & \\ 1 & 0 & 0 \\ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 0 \\ \ddots \\ 0 \\ 1 \\ \vdots \\ \xi_ {p} ^ {(k _ {p} ^ {- 1})} \\ 1 \\ \vdots \\ \xi_ {p} \end{array} \right] \left[ \begin{array}{c} \xi_ {1} ^ {(k _ {1} ^ {- 1})} \\ \vdots \\ \xi_ {1} \\ \vdots \\ \xi_ {p} ^ {(k _ {p} ^ {- 1})} \\ \vdots \\ \xi_ {p} \end{array} \right] + \left[ \begin{array}{c c c c c c c c c c c c c c c c c c c c c c c c c c c c} 1 \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right] \\ \times \left[ \begin{array}{c} \xi_ {1} ^ {(k _ {1})} \\ \vdots \\ \vdots \\ \vdots \\ \xi_ {p} ^ {(k _ {p})} \end{array} \right] = A _ {c} ^ {o} x ^ {o} + B _ {c} ^ {o} u _ {o} \tag {9.110} \\ \end{array}
\mathbf {y} _ {o} = C _ {c} ^ {o} \mathbf {x} ^ {o} = \mathbf {x} ^ {o} \tag {9.111}
$$

也就是说，核 MFD $\Psi(s)S^{-1}(s)$ 的核实现 $(A_{c}^{o}, B_{c}^{o}, C_{c}^{o})$ 为：

$$
A _ {c} ^ {o} = \left[ \begin{array}{l l l} 0 & & k _ {1} \\ 1 & & k _ {p} \\ 1 & 0 & \\ \hline & & \ddots \\ & & 0 \\ & & 1 \\ & & 1 & 0 \end{array} \right] \left\{ \begin{array}{l} k _ {1} \\ \vdots \\ B _ {c} ^ {o} = \left[ \begin{array}{c c c} 1 & & \\ 0 & & \\ \vdots & & \\ 0 & & \\ - & \ddots & \\ & 1 & \\ & 0 & \\ & 0 & \end{array} \right] \end{array} \right\} k _ {p}, C _ {c} ^ {o} = I _ {s} (9. 1 1 2)
$$

（5）注意到 $B_{c}^{o}$ 中和 $A_{c}^{o}$ 的各约当块首行相对应的所有行为线性无关，故由约当形能控性判据即知， $\{A_c^o,B_c^o\}$ 为完全能控。

控制器形实现 $(A_{c}, B_{c}, C_{c})$ 的确定 在(9.112)所示的核实现 $(A_{c}^{o}, B_{c}^{o}, C_{c}^{o})$ 的基础上，将可很容易来定出给定 $N(s)D^{-1}(s)$ 的控制器形实现 $(A_{c}, B_{c}, C_{c})$ 。对此，我们有如下的基本结论。

结论 给定 $q \times p$ 的严格真 MFD $N(s)D^{-1}(s)$ ，其中 $D(s)$ 为列既约，则其控制器形实现 $(A_c, B_c, C_c)$ 的各系数矩阵为

$$A _ {c} = A _ {c} ^ {o} - B _ {c} ^ {o} D _ {h c} ^ {- 1} D _ {l e}, \quad B _ {e} = B _ {c} ^ {o} D _ {h c} ^ {- 1}, \quad C _ {e} = N _ {l e} \tag {9.113}$$

其中核实现 $(A_{c}^{o}, B_{c}^{o}, C_{c}^{o})$ 给出于(9.112)中。
