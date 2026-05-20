$$\mathcal {X} _ {1 2} \stackrel {\text { def }} {=} \mathcal {X} _ {1} \cap \mathcal {X} _ {2}, \quad \mathcal {X} _ {1 1} \oplus \mathcal {X} _ {1 2} \stackrel {\text { def }} {=} \mathcal {X} _ {1}, \quad \mathcal {X} _ {2 2} \oplus \mathcal {X} _ {1 2} \stackrel {\text { def }} {=} \mathcal {X} _ {2}, \quad \mathcal {X} _ {2 1} \oplus (\mathcal {X} _ {1} \cup \mathcal {X} _ {2}) \stackrel {\text { def }} {=} \mathbb {R} ^ {n}.$$

显然，对系统 $(A, B, C)$ ， $\chi_{12}$ 是它的能控不能观测的子空间， $\chi_{11}$ 是它的既能控又能观测的子空间， $\chi_{21}$ 是它的不能控但能观测的子空间， $\chi_{22}$ 是它的既不能控又不能观测的子空间。不难看出

$$\mathbb {R} ^ {n} = \chi_ {1 1} \oplus \chi_ {1 2} \oplus \chi_ {2 1} \oplus \chi_ {2 2}.$$

由于 $\mathcal{X}_1$ 和 $\mathcal{X}_2$ 都是 $A$ 的不变子空间，因此 $\mathcal{X}_{12}$ 也是 $A$ 的不变子空间.

在子空间 $\chi_{11}, \chi_{12}, \chi_{21}, \chi_{22}$ 中分别取一组基，使之构成状态空间 $R^{n}$ 中的一组基，令 $\chi_{11}, \chi_{12}, \chi_{21}, \chi_{22}$ 的维数分别为 $n_{1}, n_{2}, n_{3}, n_{4}$ ，则 $n_{1} + n_{2} + n_{3} + n_{4} = n$ 。于是这组基可记为 $e_{1}, e_{2}, \cdots, e_{n}$ ，其中前 $n_{1}$ 个为 $\chi_{11}$ 的基，从第 $n_{1} + 1$ 到第 $n_{1} + n_{2}$ 个为 $\chi_{12}$ 的基，从第 $n_{1} + n_{2} + 1$ 到第 $n_{1} + n_{2} + n_{3}$ 个为 $\chi_{21}$ 的基，最后 $n_{4}$ 个为 $\chi_{22}$ 的基。把 A 作用在每个变量 $e_{i}$ 上有

$$
\left\{ \begin{array}{l} A e _ {1} = \overline {{a}} _ {1 1} e _ {1} + \overline {{a}} _ {2 1} e _ {2} + \dots + \overline {{a}} _ {n 1} e _ {n}, \\ A e _ {2} = \overline {{a}} _ {1 2} e _ {1} + \overline {{a}} _ {2 2} e _ {2} + \dots + \overline {{a}} _ {n 2} e _ {n}, \\ \vdots \\ A e _ {n} = \overline {{a}} _ {1 n} e _ {1} + \overline {{a}} _ {2 n} e _ {2} + \dots + \overline {{a}} _ {n n} e _ {n}, \end{array} \right. \tag {1.3.19}
$$

由于 $\chi_{1}$ 是 A 的不变子空间，因此，当 $i=1,2,\cdots,\mu,j=\mu+1,\mu+2,\cdots,n$ 时有 $\overline{a}_{ij}=0$ 。又因为 $\chi_{2}$ 是 A 的不变子空间，因此，当 $i=1,2,\cdots,n_{1},j=n_{1}+n_{2}+n_{3}+1,\cdots,n,i=\mu+1,\mu+2,\cdots,\mu+n_{3},j=n_{1}+n_{2}+n_{3}+1,\cdots,n$ 时有 $\overline{a}_{ij}=0$ 。同理，由于 $\chi_{12}$ 是 A 的不变子空间，因此，当 $i=1,2,\cdots,n_{1},j=n_{1}+1,n_{1}+2,\cdots,n$ 时有 $\overline{a}_{ij}=0$ 。于是，可以把式 (1.3.19) 右边的系数排成一个具有如下形式的矩阵：

$$
\overline {{{A}}} = \left[ \begin{array}{c c c c} \overline {{{A}}} _ {1 1} & 0 & \overline {{{A}}} _ {1 3} & 0 \\ \overline {{{A}}} _ {2 1} & \overline {{{A}}} _ {2 2} & \overline {{{A}}} _ {2 3} & \overline {{{A}}} _ {2 4} \\ 0 & 0 & \overline {{{A}}} _ {3 3} & 0 \\ 0 & 0 & \overline {{{A}}} _ {4 3} & \overline {{{A}}} _ {4 4} \end{array} \right],
$$
