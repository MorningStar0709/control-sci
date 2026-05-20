(2) 定义映射 $\pi : (G / N) / (M / N) \to G / M$ 为 $gN(M / N) \mapsto gM$ . 我们首先证明 $\pi$ 是定义好的. 设 $g_{1}N(M / N) = g_{2}N(M / N)$ . 那么 $(g_{1}N)^{-1}(g_{2}N) \in M / N$ . 也就是说, $(g_{1}^{-1}g_{2})N \in M / N$ , 这表明 $g_{1}^{-1}g_{2} \in M$ . 等价地, $g_{1}M = g_{2}M$ . 故

$$\pi (g _ {1} N (M / N)) = g _ {1} M = g _ {2} M = \pi (g _ {2} N (M / N)).$$

其次，我们证明 $\pi$ 是一个同态：

$$
\begin{array}{l} \pi ((g _ {1} N) (g _ {2} N) (M / N)) = \pi ((g _ {1} g _ {2} N) (M / N)) = g _ {1} g _ {2} M = (g _ {1} M) (g _ {2} M) \\ = \pi (g _ {1} N (M / N)) \pi (g _ {2} N (M / N)). \\ \end{array}
$$

显见 $\pi$ 是映上，所以只要证明 $\pi$ 是一对一的即可．设

$$\pi (g N (M / N)) = g M = M,$$

则 $g \in M$ , 也就是 $gN \in M / N$ . 这就意味着 $\pi$ 是一对一的.

例3.1.6 (1) 设 $G, Q$ 为给定的两个群。在乘积集合 $G \times Q$ 上定义一个运算 $\otimes$ 为 $(g_1, q_1) \otimes (g_1, q_2) \stackrel{\mathrm{def}}{=} (g_1 g_2, q_1 q_2)$ ，这里 $g_1, g_2 \in G, q_1, q_2 \in Q$ 。那么 $G \times Q$ 成为一个群，它称为 $G$ 和 $Q$ 的乘积群。

如果我们将 $G \times \{e\}$ 等同于 $G$ , 那么容易证明 $G \triangleleft G \times Q$ . 同样, 如果我们将 $Q$ 等同于 $\{e\} \times Q$ , 则 $Q \triangleleft G \times Q$ ;

(2) 一个给定群 $G$ 的中心, $Z(G)$ , 定义为

$$Z (G) = \{x \in G \mid x y = y x, \forall y \in G \}.$$

容易证明 $Z(G) \triangleleft G$ ;

(3) 设 $Q < G$ . 那么, 对任何一个元素 $g \in G$ , 均有 $g^{-1}Qg < G$ . $Q$ 及 $g^{-1}Qg$ 称为两个共轭子群.
