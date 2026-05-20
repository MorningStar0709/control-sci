令 $x = a_{1}b_{1}h \in a_{1}b_{1}H$ . 因为 $a_{1}H = a_{2}H$ , 则存在 $h_{1}, h_{2} \in H$ 使得 $a_{1}h_{1} = a_{2}h_{2}$ . 也就是说, $a_{1} = a_{2}h_{2}h_{1}^{-1} \stackrel{\mathrm{def}}{=} a_{2}h_{3}$ , 这里 $h_{3} \in H$ . 同样有, $b_{1} = b_{2}h_{4}$ , 这里 $h_{4} \in H$ . 于是 $x \in a_{2}h_{3}b_{2}h_{4}H$ . 因为 $H$ 是一个正规子群, 故存在 $h_{5} \in H$ 使得 $h_{3}b_{2} = b_{2}h_{5}$ .

因此 $x \in a_2b_2h_5h_4H = a_2b_2H$ 。即 $a_1b_1H \subset a_2b_2H$ 。由对称性，我们也有 $a_2b_2H \subset a_1b_1H$ 。故 $a_2b_2H = a_1b_1H$ 。

容易检验，陪集加上由式 (3.1.6) 定义的运算形成一个群。因此，我们有

定义3.1.3 设 $H \triangleleft G$ . 则 $H$ 的陪集连同由式(3.1.6)所定义的运算形成一个群，称为 $G$ 对 $H$ 的商群，记作 $G / H$ .

定义3.1.4 (1) 给定两个群 $G$ 和 $Q$ . 一个映射 $F: G \to Q$ 称为一个同态, 如果

$$F (g _ {1} g _ {2}) = F (g _ {1}) F (g _ {2}). \tag {3.1.7}$$

所有从 $G$ 到 $Q$ 的同态集合记为 $\operatorname{Hom}(G, Q)$ . 因此, $F \in \operatorname{Hom}(G, Q)$ ;

(2) 如果一个同态是一对一且映上的，则它称为一个同构。所有从 $G$ 到 $Q$ 的同构集合记着 $\operatorname{Iso}(G, Q)$ ;

(3) 如果 $F \in \operatorname{Hom}(G, G)$ , 即它为 $G$ 到自身的一个同态, 则称为一个自同态. $G$ 上所有的自同态集合记着 $\operatorname{End}(G)$ :

(4) 如果 $F \in \operatorname{Iso}(G, G)$ , 即它为 $G$ 到自身的一个同构, 则称为一个自同构. $G$ 上所有的自同构集合记着 $\operatorname{Aut}(G)$ .

例 3.1.5 (1) 记 $R_{+}$ 为正实数集合. 记普通乘法为 “·”, 那么 $G = (\mathbb{R} \setminus \{0\}, \cdot)$ 和 $Q = (\mathbb{R}_{+}, \cdot)$ 都是群, $Q \triangleleft G$ , 并且 $G/Q = \{[1], [-1]\}$ . 如果我们定义映射 $F: G \to Q$ 为 $x \mapsto |x|$ , 那么 $F \in \operatorname{Hom}(G, Q)$ ;

(2) 设 $W = (\mathbb{R}, +)$ , 即 $W$ 为实数集及普通加法所构成的群, $Q$ 同上. 定义映射 $F: Q \to W$ 为 $F(x) = \ln(x)$ . 则 $F \in \operatorname{Iso}(Q, W)$ ;

(3) 考虑 $F: \mathrm{GL}(n, \mathbb{R}) \to G$ , (GL(n, $\mathbb{R}$ ) 见例 3.1.2), $G$ 同 1, 映射 $F$ 定义为 $F(X) = \det(X)$ . 那么 $F \in \operatorname{Hom}(\mathrm{GL}(n, \mathbb{R}), G)$ ;

(4) 设 $Z \in \mathrm{GL}(n, \mathbb{R})$ . 定义 $F: \mathrm{GL}(n, \mathbb{R}) \to \mathrm{GL}(n, \mathbb{R})$ 为 $F(X) = Z^{-1} X Z$ . 那么 $F \in \operatorname{Aut}(\mathrm{GL}(n, \mathbb{R}))$ .

所有以上的结果都很容易检验，我们将它留给读者.

设 $F \in \operatorname{Hom}(G, Q)$ , $F$ 的象集记为

$$\operatorname{Image} (F) = \{F (g) \mid g \in G \} \subset Q,$$

$F$ 的核记为

$$\ker (F) = \{g \in G \mid F (g) = e \in Q \}.$$

那么，我们有

命题 3.1.3 (1) Image(F) < Q; (2) ker(F) ◁ G;

证明 (1) 令 $x, y \in \operatorname{Image}(F)$ . 则存在 $g, h \in G$ 使得 $F(g) = x$ 及 $F(h) = y$ . 因此

$$x ^ {- 1} y = (F (g)) ^ {- 1} F (h) = F (g ^ {- 1}) F (h) = F (g ^ {- 1} h) \in \operatorname{Image} (F).$$

故 $\operatorname{Image}(F) < Q$ .

(2) 容易验证 $\ker(F) < G$ . 要证明它是正规子群, 设 $g \in G, k \in \ker(F)$ , 我们只要证明 $g^{-1}kg \in \ker(F)$ 即可.
