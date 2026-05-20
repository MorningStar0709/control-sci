情况下，乘号 $\otimes$ 可以省略三即 $a \otimes b$ 可写作 $ab$ .

$\text{C} G$ 是 $G$ 的一个子群, 当且仅当, 对 $H$ 中的任意两个元. $I$ -成立:

证明充分性，即 $H$ 满足 $\mathbf{G}1\sim \mathbf{G}3.$

${}^{-1}\bar{h}=e\in H$ . 因此 $e\in H$ , 即 $\mathbf{G2}$ 成立. 对任意 $\bar{h}\in H$ , 是 $\mathbf{G3}$ . 对于 $\mathbf{G1}$ 我们只要证明: 当 $h_1,h_2\in H$ 时, 乘 $\bar{h}_1$ 因为 $h_1\in H\Rightarrow h_2^{\perp}\in K\to(h_1^{\perp})^{n}h_2=h_1h_2\in H$ .

1 11 11111例如，考虑5.5设置
排列从1→2, 2→3, 3→
它实现如下排列：3→4
为1→2→1, 2→3→
得到...

这个群不是Abe.群定义3.1.2：(1)设也是一个群，则称 $H$ 为(2)设 $H < G, g \in$ 同理， $H \otimes g \stackrel{\mathrm{def}}{=} \{h \otimes g\}$ (3) $H < G$ 称为 $C$

正规子群记作 $H \triangleleft G$ 在不会发生混淆的命题3.1.1. $\varnothing \neq H$ 氯 $h_1, h_2 \in H; h_1^{-1} h_2 \in I$ 证明 必要性显见任选 $h \in H$ , 那么 $h$ $h^{-1} = h^{-1} e \in H$ . 这就积 $h_{1} \in H$ , 这是正确

命题3.1.2 左(右)陪集形成一个分割, 即, 如果 $g_{1}H \cap g_{2}H \neq \varnothing (Hg_{1} \cap Hg_{2} \neq \varnothing)$ 则 $g_{1}H = g_{2}H (Hg_{1} = Hg_{2})$ .

证明 设 $g_{1}H \cap g_{2}H \neq \emptyset$ ，可选 $c \in g_{1}H \cap g_{2}H$ 。则存在 $h_{i} \in H, i = 1,2$ 使得 $c = g_{1}h_{1} = g_{2}h_{2}$ 。

设 $g \in g_1H$ ，则存在一个 $h \in H$ 使得 $g = g_1h$ 。于是

$$g = g _ {1} h = g _ {1} h _ {1} h _ {1} ^ {- 1} h = g _ {2} h _ {2} h _ {1} ^ {- 1} h \in g _ {2} H.$$

即 $g_{1}H \subset g_{2}H$ . 同理可证: $g_{2}H \subset g_{1}H$ . 于是 $g_{1}H = g_{2}H$ .

对于任意一个群 $G$ . 它有两个平凡子群: 1. $\{e\}$ , 它只含一个元素, 即单位元; 2. $G$ 自己. 它们都是正规子群. 不等于 $G$ 的子群称为真子群.

对于 Abel 群，任一子群均为正规子群.

设 $G$ 给定， $S \subset G$ 为一子集。包含 $S$ 的最小子群 $H$ ，称为由 $S$ 生成的子群。显然，这样的子群是存在的，它是包含 $S$ 的所有子群的交。

例 3.1.4 给定一个群 G. 形式为 $g = g_{1}^{-1}g_{2}^{-1}g_{1}g_{2}$ 的元素称为 G 的交换子. 由交换子生成的群称为交换子群, 记为 $G'$ . 容易看出 $G'$ 是交换子的有限乘积集合. 即

$$G ^ {\prime} = \left\{\prod_ {i < \infty} a _ {i} ^ {- 1} b _ {i} ^ {- 1} a _ {i} b _ {i} \mid a _ {i}, b _ {i} \in G \right\}. \tag {3.1.5}$$

事实上， $G^{\prime}\triangleleft G$ 要证明这一点，即对任一 $g\in G$ 有

$$g ^ {- 1} \left(\prod_ {i < \infty} a _ {i} ^ {- 1} b _ {i} ^ {- 1} a _ {i} b _ {i}\right) g \in G ^ {\prime}.$$

显然，只要能证明 $g^{-1}a^{-1}b^{-1}abg \in G'$ 就行了。因为

$$g ^ {- 1} (a ^ {- 1} b ^ {- 1} a b) g = (a g) ^ {- 1} b ^ {- 1} (a g) b b ^ {- 1} g ^ {- 1} b g \in G ^ {\prime},$$

获证.

设 $H \triangleleft G$ . 则对任一 $g \in G, gH = Hg$ 均成立. 现在我们在陪集上定义一个运算 $\otimes$ 如下:

$$a H \otimes b H \stackrel {\mathrm{def}} {=} a b H. \tag {3.1.6}$$

由于陪集的代表元不唯一，我们必须证明式 (3.1.6) 是唯一定义好的。即如果 $a_1H = a_2H$ 且 $b_1H = b_2H$ 。则 $a_1b_1H = a_2b_2H$ 。
