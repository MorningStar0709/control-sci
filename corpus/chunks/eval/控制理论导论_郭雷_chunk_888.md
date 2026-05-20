$$
\begin{array}{l} F _ {1} = \{[ r ] \mid r \in \widetilde {R} \}, \\ F _ {2} = \left\{\left[ z ^ {k} \right] \mid k \in \mathbb {N} \cup \{0 \} \right\}, \\ F _ {3} = \left\{\left[ z ^ {- k} \right] \mid k \in \mathbb {N} \cup \{0 \} \right\}, \\ F _ {4} = \{[ \nabla^ {k} ] \mid k \in \mathbb {N} \}, \\ F _ {5} = \left\{\left[ \Delta^ {k} \right] \mid k \in \mathbb {N} \right\}. \\ \end{array}
$$

记

$$
\begin{array}{l} \overline {{{F}}} = F _ {1} \cup F _ {2} \cup F _ {3} \cup F _ {4} \cup F _ {5}, \\ F = \{\Sigma_ {\oplus} \overline {{f}} _ {i} \mid \overline {{f}} _ {i} = f _ {1} \otimes f _ {2} \otimes \dots \otimes f _ {j}, f _ {i} \in \overline {{F}}, i, j \in \mathbb {N} \}, \\ \end{array}
$$

即 $f_{i}$ 是 $\overline{F}$ 中的一个算子， $\overline{f}_{i}$ 是由 $\overline{F}$ 中的算子通过 “⊗” 运算构成的算子，其中 $\forall\langle s\rangle,\langle t\rangle\in S,\langle s\rangle\oplus\langle t\rangle\stackrel{\operatorname{def}}{=} \langle s_{0}\oplus t_{0},s_{1}\oplus t_{1},\cdots\rangle;\forall f_{1},f_{2}\in F,(f_{1}\otimes f_{2})\langle s\rangle\stackrel{\operatorname{def}}{=}f_{1}(f_{2}\circ\langle s\rangle),(f_{1}\oplus f_{2})\circ\langle s\rangle\stackrel{\operatorname{def}}{=}f_{1}\circ\langle s\rangle\oplus f_{2}\circ\langle s\rangle.$

经过以上对 $\overline{F}$ 的严密定义，可得以下定理.

定理 11.9.1 $(F, \oplus, \otimes)$ (简记为 F) 是一个双子.

只需对11.2节中双子定义的各条要求逐条验证，即可证明以上定理（可参见文献[19],[30]).

设 ETEG 中每个变迁 $t_i$ 前有 $q_i$ 个位置与变迁，记它们为 $p_{ij}, t_{ij}, 1 \leqslant j \leqslant q_i$ . 再记重数 $W(t_{ij}, p_{ij}) = u_{ij}, W(p_{ij}, t_i) = v_{ij}, 1 \leqslant j \leqslant q_i, p_{ij}$ 的初始标识数为 $m_{ij}$ . 由定义 11.9.2 易知

$$[ \nabla^ {u _ {i j}} ] \langle t \rangle_ {i j} = [ z ^ {m _ {i j}} ] \langle p _ {i j} \rangle ,$$

并可断言

$$\sum_ {j = 1} ^ {q _ {i}} \oplus [ \Delta^ {\nu_ {i j}} ] \otimes [ d _ {i j} ] \langle p _ {i j} \rangle = \langle t \rangle_ {i}.$$

由上两式可得

$$\sum_ {j = 1} ^ {q _ {i}} \oplus \left[ \Delta^ {v _ {i j}} \right] \otimes \left[ z ^ {- m _ {i j}} \right] \otimes \left[ \nabla^ {u _ {i j}} \right] \oplus \left[ d _ {i j} \right] \langle t \rangle_ {i j} = \langle t \rangle_ {i}. \tag {11.9.1}$$

记 $\boldsymbol{x} = (\langle t \rangle_{1}, \langle t \rangle_{2}, \cdots, \langle t \rangle_{\bar{n}})^{\mathrm{T}}$ ，这里 $\tilde{n}$ 表示 ETEG 中变迁的总数。设初始时刻为 0，综上所述已证得以下定理：

定理11.9.2 ETEG的双子代数模型为
