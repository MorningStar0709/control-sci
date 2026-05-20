$$F (g ^ {- 1} k g) = F (g ^ {- 1}) F (k) F (g) = F (g ^ {- 1}) F (g) = F (e) = e,$$

它表明 $g^{-1}kg\in \ker (F)$ .因此 $\ker (F)\triangleleft G$

定理 3.1.1(第一同态定理)

(1) 设 $F \in \operatorname{Hom}(G, Q)$ . $K = \ker(F)$ . 定义映射 $\theta: G / K \to \operatorname{Image}(F)$ 为 $gK \mapsto F(g)$ , 那么, $\theta: G / K \to \operatorname{Image}(F)$ 是一个同构, 即

$$G / \ker (F) \cong \operatorname{Image} (F); \tag {3.1.8}$$

(2) If $H \triangleleft G$ , 定义映射 $\pi: G \to G / H$ 为 $g \mapsto gH$ . 那么 $\pi: G \to G / H$ 是一个映上的同态. 并且, $\ker(\pi) = H$ .

证明 (1) 首先证明 $\theta$ 是定义好的：设 $gK = hK$ 则 $g^{-1}h \in K$ . 因此

$$\theta (h K) = \theta (g g ^ {- 1} h K) = F (g g ^ {- 1} h) = F (g) F (g ^ {- 1} h) = F (g) = \theta (g K).$$

同时，我们还有

$$\theta (g h K) = F (g h) = F (g) F (h) = \theta (g K) \theta (h K).$$

因此， $\theta$ 是一个同态。 $\theta$ 显然是映上的。这样，要证明 $\theta$ 是同构，只要证明 $\theta$ 是一对一的即可。

设 $\theta(gK) = F(g) = e$ . 那么 $g \in K$ , 因此 $gK = K$ , 这就说明 $\theta$ 是一对一的.

(2) 利用与 1 的证明类似的方法可知， $\pi$ 是一个映上的同态。如果 $g \in H$ 则 $\pi(g) = gH = H$ ，如果 $g \notin H$ 则 $\pi(g) = gH \neq H$ 。因此 $\ker(\pi) = H$ 。

定理 3.1.2(第二同态定理)

(1) 设 $H < G$ , 且 $N \triangleleft G$ . 则 $N \cap H \triangleleft H$ ;

(2) 设

$$N H = \{n h \mid n \in N, h \in H \},$$

则 $NH < G$ ;

(3) 对任一 $h \in H$ 定义 $\pi: H / (N \cap H) \to NH / N$ 为 $h(N \cap H) \mapsto hN$ , 那么 $\pi$ 是一个同构. 即

$$H / (H \cap N) \cong N H / N. \tag {3.1.9}$$

证明 (1) 令 $h \in H$ 及 $n \in N \cap H$ . 我们只要证明 $h^{-1}nh \in N \cap H$ 即可. 显然 $h^{-1}nh \in H$ . 因为 $n \in N$ 而且 $N$ 是正规的, 故有某个 $n' \in N$ 使得 $hn = n'h$ . 因此 $h^{-1}nh = n' \in N$ .

(2) 令 $n_1, n_2 \in N$ 及 $h_1, h_2 \in H$ , 我们只要证明 $(n_1 h_1)^{-1} n_2 h_2 \in NH$ 即可. 因为

$$(n _ {1} h _ {1}) ^ {- 1} n _ {2} h _ {2} = h _ {1} ^ {- 1} n _ {1} ^ {- 1} n _ {2} h _ {2} = h _ {1} ^ {- 1} n _ {3} h _ {2} = n _ {4} h _ {1} ^ {- 1} h _ {2} \in N H,$$

这里 $n_3, n_4 \in N, n_3 = n_1^{-1}n_2$ 以及 $h_1^{-1}n_3 = n_4h_1^{-1}$ . (因为 $N$ 是正规子群，这样的 $n_4$ 存在.)

(3) 首先证明 $\pi$ 是一个同态

$$
\begin{array}{l} \pi (x (N \cap H) y (N \cap H)) = \pi (x y (N \cap H)) = x y N = (x N) (y N) \\ = \pi (x (N \cap H)) \pi (y (N \cap H)), \quad x, y \in H. \\ \end{array}
$$

其次证明 $\pi$ 是映上的．对每一个 $x = nh\in NH$ ，存在某个 $n^{\prime}\in H$ 使得

$$x N = n h N = h n ^ {\prime} N = h N,$$

因此

$$\pi (h (N \cap H)) = h N = x N.$$

最后证明 $\pi$ 是一对一的：设 $x \in H$ 并且

$$\pi (x (N \cap H)) = x N = N.$$

那么 $x \in N$ . 即 $x \in N \cap H$ .

定理 3.1.3(第三同态定理) 设 $M \triangleleft G, N \triangleleft G$ 并且 N < M. 那么

(1)

$$M / N \triangleleft G / N; \tag {3.1.10}$$

(2)

$$(G / N) / (M / N) \cong G / M. \tag {3.1.11}$$

证明 (1) $M / N < G / N$ 是显然的. 我们证明它是正规的: 令 $g \in G$ 且 $m \in M$ . 那么

$$(g N) ^ {- 1} (m N) (g N) = (g ^ {- 1} m g) N = m ^ {\prime} N \in M / N$$

这里 $m' \in M$ . 因此 $M / N \triangleleft G / N$ .
