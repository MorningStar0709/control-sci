设 $P$ 是定义在 $\mathcal{F}$ 上的集合函数，它有以下性质：

(1) $P$ 为非负函数， $P(A) \geqslant 0, \forall A \in \mathcal{F}$ ;  
(2) $P(\Omega) = 1$ ，即当集合为全空间时， $P$ 的取值为1；

(3) $P$ 为可列可加：对互不相交的集合序列 $\{A_i\}$ , $A_i \cap A_j = \emptyset$ , $\forall i \neq j$ , $A_i \in \mathcal{F}$ , $\forall i$ , $P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$ .

满足上述条件的集合函数 $P$ 叫定义在 $\mathcal{F}$ 上的概率测度，或简称概率，而 $(\Omega, \mathcal{F}, P)$ 叫概率空间，也叫概率三要素。 $\Omega$ 中的点 $\omega$ 也叫基本事件，也叫样本点，或样本。 $\mathcal{F}$ 中的集合叫可测集，也叫事件。

例4.1.1 取 $\Omega = [0,1]$ , $\mathcal{F}$ 为包含在 $[0,1]$ 中的Lebesgue可测集，即 $\mathcal{L} \cap [0,1]$ ，而 $P$ 为 $[0,1]$ 上的Lebesgue测度 $\lambda$ ，那么 $([0,1],\mathcal{L} \cap [0,1],\lambda)$ 就是一个概率空间.

例4.1.2 仍取 $\Omega = [0,1]$ , 但取 $\mathcal{F}$ 只有 4 个元, $\mathcal{F} = \left\{\varnothing, \Omega, \left(0, \frac{1}{3}\right), \left[\frac{1}{3}, 1\right]\right\}$ , 并取 $P\left(\left[0, \frac{1}{3}\right]\right) = p$ , $P\left(\left[\frac{1}{3}, 1\right]\right) = 1 - p$ , $p \geqslant 0$ , 那么 $(\Omega, \mathcal{F}, P)$ 也构成一个概率空间.

例 4.1.3 设一个盒子里装有 10 个球，分别标号 0,1,…,9. 那么可取 $\Omega$ 为这

10个球， $\mathcal{F}$ 中的集合为这10个球及空集的任意组合。并赋予每个球的概率为 $\frac{1}{10}$ ，那么这就组成一个概率空间。

对任一 $A \in \mathcal{F}$ , 若 $PA = 0$ , 但 $A$ 的子集不一定属 $\mathcal{F}$ . 此时, 直线上的 Borel 可测集完备成 Lebesgue 可测集一样, 需要把 $\mathcal{F}$ 完备化. 把概率空间 $(\Omega, \mathcal{F}, A)$ 中任一零概率集 $A(PA = 0)$ 的任一子集都算作 $\mathcal{F}$ 中的集合, 并定义其概率为 0. 这样的概率空间叫完备概率空间. 今后我们所提到的概率空间一律认为是已完备化了的.

设 $A \in \mathcal{F}, A' \in \mathcal{F}, P(A \neq A') = 0$ , 则称 $A$ 和 $A'$ 属等价类, 记为 $A = A'$ a.s., 或以概率 1, $A = A'$ .
