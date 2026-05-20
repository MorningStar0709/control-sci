# 习题 8.4

8.4.1 考虑线性系统

$$
\left\{ \begin{array}{l l} \dot {x} = A x + B u, & x \in \mathbb {R} ^ {n}, u \in \mathbb {R} ^ {m} \\ y = C x, & y \in \mathbb {R} ^ {p}. \end{array} \right.
$$

则 $(f,g)$ 不变分布变为 $(A,B)$ 能控不变子空间；

(i) 给出子空间 $V \subset \mathbb{R}^n$ 为能控不变子空间的条件；  
(ii) 推出在 $\ker(C)$ 中最大能控不变子空间的算法.

8.4.2 解下列系统的反馈块解耦问题：

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c} \sin (x _ {2} - x _ {1}) + 2 x _ {3} (x _ {2} - x _ {3} ^ {2}) \\ \cos (x _ {1} - x _ {2}) + 2 x _ {3} (\mathrm{e} ^ {x _ {2} - x _ {1}} - 1) \mathrm{e} ^ {x _ {3} ^ {2}} + 2 x _ {2} (x _ {2} - x _ {3} ^ {2}) \\ - \mathrm{e} ^ {x _ {3} ^ {2}} + x _ {2} - x _ {3} ^ {2} \end{array} \right] \\ + \left[ \begin{array}{c} \mathrm{e} ^ {x _ {1}} + 2 x _ {3} (x _ {2} - x _ {3} ^ {2}) \\ \mathrm{e} ^ {x _ {2}} + 2 x _ {3} (x _ {2} - x _ {3} ^ {2}) \\ (x _ {2} - x _ {3} ^ {2}) \end{array} \right] u _ {1} + \left[ \begin{array}{c} 2 x _ {3} \mathrm{e} ^ {x _ {1} - x _ {2}} \\ 2 x _ {3} \mathrm{e} ^ {x _ {1} - x _ {2}} \\ \mathrm{e} ^ {x _ {1} - x _ {2}} \end{array} \right] u _ {2}. \\ \end{array}
$$

提示：利用以下分布，

$$\Delta_ {1} = \operatorname{span} \left\{\left[ 2 x _ {3}, 2 x _ {3}, 1 \right] ^ {\mathrm{T}} \right\}, \quad \Delta_ {2} = \operatorname{span} \left\{\left[ 1, 0, 0 \right] ^ {\mathrm{T}}, [ 0, 1, 0 ] ^ {\mathrm{T}} \right\}.$$
