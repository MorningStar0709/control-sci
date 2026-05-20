(3) 定义 $M / \sim$ 上的一个子集族如下，它称为商拓扑，

$$\mathcal {T} _ {\sim} = \{U \in M / \sim | \pi^ {- 1} (U) \text {为} M \text {中的开集} \}.$$

命题3.3.5 设 $M / \sim$ 及 $\mathcal{T}_{\sim}$ 定义如上．那么 $(M / \sim, \mathcal{T}_{\sim})$ 是一个拓扑空间，称为 $M$ 对 $\sim$ 的商空间.

证明 我们只要证明 $T_{\sim}$ 是一个拓扑就够了。显见， $M / \sim, \varnothing \in T_{\sim}$ 。

设 $\pi^{-1}(U_{\lambda}) \in T_{\sim}, \lambda \in \Lambda$ . 那么因为 $\bigcup_{\lambda \in \Lambda} U_{\lambda}$ 在 $M$ 中开，则

$$\bigcup_ {\lambda \in \Lambda} \pi^ {- 1} (U _ {\lambda}) = \pi^ {- 1} \left(\bigcup_ {\lambda \in \Lambda} U _ {\lambda}\right) \in \mathcal {T} _ {\sim}.$$

设 $\pi^{-1}(U_{i})\in T_{\sim}, i=1,\cdots,k.$ 那么因为 $\bigcap_{i=1}^{k}U_{i}$ 在 M 中开，则

$$\bigcap_ {i = 1} ^ {k} \pi^ {- 1} (U _ {i}) = \pi^ {- 1} \left(\bigcap_ {i = 1} ^ {k} U _ {i}\right) \in \mathcal {T} _ {\sim}.$$

因此， $T_{\sim}$ 是一个拓扑.

如果在一个拓扑空间 $M$ 中，有等价关系 $\sim$ 使得 $x \sim y$ ，则称这两点被粘接到一起。各种拓扑空间可由一个空间通过粘接某些点而得到。

例3.3.19 令 $S$ 为 $\mathbb{R}^2$ 中的一个矩形

$$S = [ 0, 1 ] \times [ 0, 1 ] \in \mathbb {R} ^ {2}.$$

设 $\mathbb{R}^2$ 具有普通拓扑且 $S\subset \mathbb{R}^2$ 为其拓扑子空间.

(1) 如果我们将 $S$ 的左边与右边粘接，即

$$(0, y) \sim (1, y), \quad 0 \leqslant y \leqslant 1,$$

那么商空间 $S / \sim$ 就是一个圆柱面（图3.3.5(a));

(2) 如果我们将 $S$ 的左边与右边反向粘接，即

$$(0, y) \sim (1, 1 - y), \quad 0 \leqslant y \leqslant 1,$$

那么商空间 $S / \sim$ 就是一个带，它没有“里面”和“外面”之分。直观地说，一只蚂蚁可以从带的一个面爬到另一个面而无须穿过带的边缘。这样的面称为不可定向面。上面这个面称为Mobius带(图3.3.5(b));

(3) 如果我们将 $S$ 的右边与上边粘接，即

$$(1, z) \sim (z, 1), \quad 0 \leqslant z \leqslant 1,$$

并将 $S$ 的左边与下边粘接，即

$$(0, z) \sim (z, 0), \qquad 0 \leqslant z \leqslant 1,$$

那么商空间 $S / \sim$ 是一个球面（图3.3.5(c));

(4) 如果我们将 $S$ 的右边与左边粘接，即

$$(0, y) \sim (1, y), \quad 0 \leqslant y \leqslant 1,$$

![](image/5b531cfb0a42a1780174b6064f9dcf2f37e0a4c2551864fbf23c3de48c91f17c.jpg)  
图3.3.5 矩形的粘接空间

并将 $S$ 上边与下边粘接，即

$$(x, 0) \sim (x, 1), \qquad 0 \leqslant x \leqslant 1,$$

那么商空间 $S/\sim$ 是一个轮胎面 (图 3.3.5(d));

(5) 如果我们将 $S$ 的右边与左边粘接，即

$$(0, y) \sim (1, y), \quad 0 \leqslant y \leqslant 1,$$

并将 $S$ 的上边与下边反向粘接，即

$$(x, 0) \sim (1 - x, 1), \quad 0 \leqslant x \leqslant 1,$$

那么商空间 $S / \sim$ 是这样一个密封的瓶子，蚂蚁可以由瓶子里面爬到外面。它称为Klein瓶(图3.3.5(e))。实际上这样的瓶子不能在三维空间 $\mathbb{R}^3$ 实现。
