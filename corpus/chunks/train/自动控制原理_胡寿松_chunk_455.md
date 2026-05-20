$$
\begin{array}{l} b _ {k} = \left| \begin{array}{c c} a _ {0} & a _ {n - k} \\ a _ {n} & a _ {k} \end{array} \right|; \qquad k = 0, 1, \dots , n - 1 \\ c _ {k} = \left| \begin{array}{c c} b _ {0} & b _ {n - k - 1} \\ b _ {n - 1} & b _ {k} \end{array} \right|; \qquad k = 0, 1, \dots , n - 2 \\ d _ {k} = \left| \begin{array}{c c} c _ {0} & c _ {n - k - 2} \\ c _ {n - 2} & c _ {k} \end{array} \right|; \qquad k = 0, 1, \dots , n - 3 \\ q _ {0} = \left| \begin{array}{l l} p _ {0} & p _ {3} \\ p _ {3} & p _ {0} \end{array} \right|, \quad q _ {1} = \left| \begin{array}{l l} p _ {0} & p _ {2} \\ p _ {3} & p _ {1} \end{array} \right|, \quad q _ {2} = \left| \begin{array}{l l} p _ {0} & p _ {1} \\ p _ {3} & p _ {2} \end{array} \right| \\ \end{array}
$$

• • • • • •

朱利稳定判据 特征方程 $D(z) = 0$ 的根，全部位于 $z$ 平面上单位圆内的充分必要条件是

$$
D (1) > 0, \quad D (- 1) \left\{ \begin{array}{l l} {> 0,} & {\text {当} n \text {为偶数时}} \\ {<   0,} & {\text {当} n \text {为奇数时}} \end{array} \right.
$$

以及下列 $n - 1$ 个约束条件成立

$$\left| a _ {0} \right| < a _ {n}, \quad \left| b _ {0} \right| > \left| b _ {n - 1} \right|, \quad \left| c _ {0} \right| > \left| c _ {n - 2} \right|\left| d _ {0} \right| > \left| d _ {n - 3} \right|, \quad \dots , \quad \left| q _ {0} \right| > \left| q _ {2} \right|$$

只有当上述诸条件均满足时，离散系统才是稳定的，否则系统不稳定。

例 7-25 已知离散系统闭环特征方程为

$$D (z) = z ^ {4} - 1. 3 6 8 z ^ {3} + 0. 4 z ^ {2} + 0. 0 8 z + 0. 0 0 2 = 0$$

试用朱利判据判断系统的稳定性。

解 由于 $n = 4, 2n - 3 = 5$ ，故朱利阵列有5行5列。根据给定的 $D(z)$ 知： $a_0 = 0.002, a_1 = 0.08, a_2 = 0.4, a_3 = -1.368, a_4 = 1$ 。

计算朱利阵列中的元素 $b_{k}$ 和 $c_{k}$ :

$$
\begin{array}{l} b _ {0} = \left| \begin{array}{l l} a _ {0} & a _ {4} \\ a _ {4} & a _ {0} \end{array} \right| = - 1, \quad b _ {1} = \left| \begin{array}{l l} a _ {0} & a _ {3} \\ a _ {4} & a _ {1} \end{array} \right| = 1. 3 6 8 \\ b _ {2} = \left| \begin{array}{l l} a _ {0} & a _ {2} \\ a _ {4} & a _ {2} \end{array} \right| = - 0. 3 9 9, \quad b _ {3} = \left| \begin{array}{l l} a _ {0} & a _ {1} \\ a _ {4} & a _ {3} \end{array} \right| = - 0. 0 8 2 \\ c _ {0} = \left| \begin{array}{l l} b _ {0} & b _ {3} \\ b _ {3} & b _ {0} \end{array} \right| = 0. 9 9 3, \quad c _ {1} = \left| \begin{array}{l l} b _ {0} & b _ {2} \\ b _ {3} & b _ {1} \end{array} \right| = - 1. 4 0 1 \\ c _ {2} = \left| \begin{array}{l l} b _ {0} & b _ {1} \\ b _ {3} & b _ {2} \end{array} \right| = 0. 5 1 1 \\ \end{array}
$$

作出如下朱利阵列：
