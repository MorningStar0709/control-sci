# 习题 6.4

6.4.1 令 $n \times m$ 传递函数阵 $G_{1}(s)$ 和 $m \times p$ 传递函数阵 $G_{2}(s)$ 的状态空间实现分别为

$$G _ {1} (s) = \left\{A _ {1}, B _ {1}, C _ {1}, D _ {1} \right\}, \quad G _ {2} (s) = \left\{A _ {2}, B _ {2}, C _ {2}, D _ {2} \right\}.$$

试验证由两个子系统并联构成的系统 $G_{1}(1) + G_{2}(s)$ 和串联构成的系统 $G_{1}(s)G_{2}(s)$ 的状态空间实现分别为

$$
G _ {1} (s) + G _ {2} (s) = \left\{\left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right], \left[ \begin{array}{c} B _ {1} \\ B _ {2} \end{array} \right], [ C _ {1}, C _ {2} ], D _ {1} + D _ {2} \right\},

G _ {1} (s) G _ {2} (s) = \left\{\left[ \begin{array}{c c} A _ {1} & B _ {1} C _ {2} \\ 0 & A _ {2} \end{array} \right], \left[ \begin{array}{c} B _ {1} D _ {2} \\ B _ {2} \end{array} \right], [ C _ {1}, D _ {1} C _ {2} ], D _ {1} D _ {2} \right\}.
$$

6.4.2 令

$$P (s) = \frac {1}{s - 1}.$$

试利用定理 6.4.2 求使得闭环系统稳定的所有反馈控制器.
