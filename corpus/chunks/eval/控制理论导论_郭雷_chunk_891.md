$$\left| t _ {q} - d \log_ {p} q \right| < b.$$

这里 $b$ 为与 $q$ 无关的常数， $d = \sum_{i=1}^{L} d_i, \sum$ 为普通加法运算；

(3) $P < 1$ 时， $\langle t \rangle_{i}$ 为有限序列 $\langle t_0, t_1, \dots, t_q \rangle$ .

证明略去。以上定理说明， $P$ 这个参数非常重要。 $P < 1, P = 1, P > 1$ 对应了三种序列：有限序列，准周期序列，近似对数序列。从特征值观点看， $P < 1, P = 1, P > 1$ 基本上对应于 $A$ 的相应特征值为 $+\infty$ ，周期 $\lambda_1 1 / +\infty$ 。进一步，当 $v$ 的分量不设为常数序列，而是有界序列，或 $v$ 的第 $i$ 个分量 $\langle v \rangle_i$ 的第 $q$ 个元 $w_q = o(\log_p q)$ ，或当 $\langle t \rangle_i$ 为准周期序列时， $w_q = o(q)$ ，则上述主要结论仍成立，这是因为 $q$ 充分大后 $t_q$ 增长快， $w_q$ 不再起作用。以上结果还可推广到 $G(A)$ 含多个回路的情况，但要求 $G(A)$ 中任两条回路间没有路及公共点。

以上仅是建立分析理论的开始，我们相信：使用与发展上述方法后，可以先把上述结果推广到由多条相交回路、每条回路的 $P = 1$ 组成的 $G(A)$ 中去，再推广到一般的 $G(A)$ 上，从而完成分析理论。这需要做进一步的研究工作。

现在来分析例11.9.1. 由图11.9.3这正是所有回路 $P = 1$ 的情况。不妨设 $\tilde{t}_1 \geqslant \tilde{t}_2$ 。对这具体例子，文献[30]用双子代数与Petri网运行原理相结合的方法，证明了 $\langle t \rangle_i$ 是准周期序列，并进一步分析回路 $L_2$ 中，位置 $p_{n+m+5}$ 里标识的变化规律，指出第一个标识到达需时 $\tilde{t}_1 + \tilde{t}_2 + \tilde{t}_r$ ；因设 $\tilde{t}_1 \geqslant \tilde{t}_2$ 。后 $N$ 个标识，在前一个标识离开 $p_{n+m+4}$ 时，已在这位置中等待(冷却)了 $\tilde{t}_r - \tilde{t}_1$ 时间，所以仅需时 $N\tilde{t}_1$ 。于是仅看回路 $L_2$ 时 $\langle t \rangle_{n+m+5}$ 的周期为

$$\lambda = (2 N + 1) \widetilde {t} _ {1} + \widetilde {t} _ {2}. \tag {11.9.3}$$

类似可证 $L_{1}$ 中 $\langle t\rangle_{n + m + 6}$ 的周期为

$$\widetilde {\lambda} = \max \{\widetilde {t _ {0}}, k \lambda \}. \tag {11.9.4}$$

把上述建模与分析的方法与结果应用到某个板材公司的热轧线上, 例 11.9.1 就具体化为下例.

例 11.9.2 已知加热炉的加工时间为 45, 一批加热 18 个工件, 轧机前后存储器个数分别为 4,3, 且它的第一、二两次加工时间分别为 2、1.5, 两次加工间的轧件冷却时间为 4, 上面时间均以分钟为单位.

由例11.9.1的 $\langle t\rangle_{i}$ 间关系式可得

$$\langle t \rangle_ {1} = [ z ^ {- 1} ] [ 4 5 ] \langle t \rangle_ {1} \oplus [ z ^ {- 2} ] \langle t \rangle_ {1 3} \oplus \overline {{{u}}},\langle t \rangle_ {2} = [ 4 5 ] \langle t \rangle_ {1} \oplus [ z ^ {- 1} ] \langle t \rangle_ {1 3} \oplus \overline {{{0}}},\langle t \rangle_ {3} = [ \Delta^ {3} ] [ \nabla^ {1 8} ] \langle t \rangle_ {2} \oplus [ \Delta^ {3} ] [ z ^ {- 3} ] [ 1. 5 ] \langle t \rangle_ {1 2} \oplus \overline {{{0}}},$$

• • •

$$\langle t \rangle_ {1 1} = \langle t \rangle_ {1 0} \oplus [ z ^ {- 1} ] \langle t \rangle_ {1 1} \oplus \overline {{0}},\langle t \rangle_ {1 2} = [ 4 ] \langle t \rangle_ {1 1} ⓛ [ z ^ {- 1} ] [ 1. 5 ] \langle t \rangle_ {1 2} ⓛ \overline {{0}},\langle t \rangle_ {1 3} = [ \Delta^ {6} ] \langle t \rangle_ {3} \oplus \overline {{{0}}}.$$
