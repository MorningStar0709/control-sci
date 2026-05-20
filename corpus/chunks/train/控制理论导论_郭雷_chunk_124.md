$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {x} _ {1} (t) \\ \dot {z} _ {c _ {1}} (t) \\ \dot {z} _ {c _ {2}} (t) \end{array} \right] = \left[ \begin{array}{c c c} A _ {1} + B _ {1} F C _ {1} & B _ {1} F _ {c _ {1}} & B _ {1} F _ {c _ {2}} \\ B _ {c _ {1}} C _ {1} & A _ {c _ {1}} & 0 \\ B _ {c _ {2}} C _ {1} & A _ {c _ {2}} & A _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ z _ {c _ {1}} (t) \\ z _ {c _ {2}} (t) \end{array} \right] + \left[ \begin{array}{c} A _ {3} \\ 0 \\ 0 \end{array} \right] x _ {2} (t),} \\ \dot {x} _ {2} (t) = A _ {2} x _ {2}, \\ z (t) = x _ {1} (t). \end{array} \right.
$$

考虑到闭环系统的稳定性，因此对任意 $\lambda \in \mathbb{C}^{+}$ 必有

$$
\operatorname{rank} \left[ \begin{array}{c c c} A _ {1} + B _ {1} F C _ {1} - \lambda I _ {n _ {1}} & B _ {1} F _ {c _ {1}} & B _ {1} F _ {c _ {2}} \\ B _ {c _ {1}} C _ {1} & A _ {c _ {1}} - \lambda I _ {l _ {1}} & 0 \\ B _ {c _ {2}} C _ {1} & A _ {c _ {2}} & A _ {2} - \lambda I _ {n _ {2}} \end{array} \right] = n _ {1} + l _ {1} + n _ {2}.
$$

由此得出，对 $\lambda \in \sigma(A_2)$ 有

$$
\operatorname{rank} \left[ \begin{array}{c c} A _ {1} + B _ {1} F C _ {1} - \lambda I _ {n _ {1}} & A _ {3} \\ B _ {c _ {1}} C _ {1} & 0 \\ B _ {c _ {2}} C _ {1} & A _ {2} - \lambda I _ {n _ {2}} \end{array} \right] = n _ {1} + n _ {2}.
$$

又因为

$$
\begin{array}{l} \left[ \begin{array}{c c} A _ {1} + B _ {1} F C _ {1} - \lambda I _ {n _ {1}} & A _ {3} \\ B _ {c _ {2}} C _ {1} & A _ {2} - \lambda I _ {n _ {2}} \\ B _ {c _ {1}} C _ {1} & 0 \end{array} \right] \\ = \left[ \begin{array}{c c c} I _ {n _ {1}} & 0 & B _ {1} F \\ 0 & I _ {n _ {2}} & B _ {c _ {2}} \\ 0 & 0 & B _ {c _ {1}} \end{array} \right] \left[ \begin{array}{c c} A - \lambda I _ {n _ {1}} & A _ {3} \\ 0 & A _ {2} - \lambda I _ {n _ {2}} \\ C _ {1} & 0 \end{array} \right], \\ \end{array}
$$

所以必有

$$
\operatorname{rank} \left[ \begin{array}{c c} A - \lambda I _ {n _ {1}} & A _ {3} \\ 0 & A _ {2} - \lambda I _ {n _ {2}} \\ C _ {1} & 0 \end{array} \right] = n _ {1} + n _ {2}.
$$

这就是前面所说的干扰能估计的条件 B). 可见定理 1.8.1 的条件 (1.8.31) 和条件 B) 也是必要的. 归纳起来我们得到如下定理:

定理1.8.3 已知定常线性系统(1.8.39). 它存在全状态输出调节器的充分必要条件是

(1) $(A_{1}, B_{1})$ 能稳， $(A_{1}, C_{1})$ 能检测；  
(2) $\operatorname{rank} B_1 = \operatorname{rank}[B_1, A_3]$ ;   
(3) 对任意 $\lambda \in \sigma(A_2)$ 都有

$$
\operatorname{rank} \left[ \begin{array}{c c} A - \lambda I _ {n _ {1}} & A _ {3} \\ 0 & A _ {2} - \lambda I _ {n _ {2}} \\ C _ {1} & 0 \end{array} \right] = n _ {1} + n _ {2}.
$$
