是指数稳定的，因此根据引理10.3.2， $(A,B)$ 在某个 $[0,t_f]$ 上是精确能控的。此外从引理10.3.2的证明可知，所述的控制律 $u(t)$ 正好把 $x_0$ 引导到零。证毕。

定理10.3.8 设 $A$ 是Hilbert空间 $H$ 中斜自伴算子，即 $A^{*} = -A$ ，而 $B \in \mathcal{L}(U, H)$ .那么下列命题是等价的：

(1) $(A, B)$ 按任意衰减指数是指数能稳的；  
(2) $(A, B)$ 是指数能稳的；  
(3) 对于任意正定对称算子 $K \in \mathcal{L}(U)$ , $T^{A-BKB^*}(t)$ 是指数稳定的;  
(4) 存在一对称算子 $K \in \mathcal{L}(U)$ 使得 $T^{A - BKB^*}(t)$ 是指数稳定的；  
(5) 存在 $t_f > 0$ 使得 $(A, B)$ 在某个区间 $[0, t_f]$ 上是精确能控的；  
(6) 存在常数 $t_f > 0$ 和 $\delta > 0$ 使得

$$\int_ {0} ^ {t _ {f}} \| B ^ {*} T ^ {A ^ {*}} (- t) x \| _ {U} ^ {2} \mathrm{d} t \geqslant \delta \| x \| ^ {2}, \quad \forall x \in H;$$

(7) $\mathbf{i}\mathbb{R} \subset \rho(A - BB^{*})$ , 并且

$$M \stackrel {\text { def }} {=} \sup _ {\omega \in \mathbb {R}} \| R (\mathrm{i} \omega ; A - B B ^ {*}) \| < \infty .$$

证明 (1) $\Longrightarrow$ (2) 是显然的.

(2) $\Longrightarrow (3)$ . 由于 $(A, B)$ 指数能稳，并且 $A^{*} = -A$ ，故 $(B^{*}, -A)$ 是指数能检测的。因此对于任意正定算子 $K \in \mathcal{L}(U)$ ， $(K^{\frac{1}{2}}B^{*}, -A)$ 也是指数能检测的。在引理

10.3.1 中，用 $K^{\frac{1}{2}}B^{*}, K^{-1}, -KB^{*}, I$ 分别代替 $C, R, K, P,$ 并考虑到 $\operatorname{Re}(Ax, x) = 0,$ 我们有

$$2 \operatorname{Re} (x, (A - B K B ^ {*}) x) + (B K B ^ {*} x, x) + (B K B ^ {*} x, x) \leqslant 0, \quad \forall x \in \mathcal {D} (A),$$

根据引理 10.3.1, 这蕴含 $T^{A-BKB^{*}}(t)$ 是指数稳定的.

(3) $\Longrightarrow$ (4) 是显然的.

(4) $\rightarrow$ (5) 从推论 10.3.3 推出.

(5) $\Rightarrow$ (6) 从定理10.2.1推出.

(6) $\Longrightarrow$ (1) 直接从定理 10.3.1 推出，因为这里 $A$ 生成一 $C_0$ 群.

(3) $\Longrightarrow (7)$ . 由于 $T^{A - BB^*}(t)$ 是指数稳定的, 故 $s(A - BB^*) < 0$ . 因此 $\mathrm{i}\omega \in \rho (A - BB^*)$ , $\forall \omega \in \mathbb{R}$ . 此外, 根据 Hille-Yosida 定理, 存在常数 $\mu < 0$ 和 $M > 0$ 使得

$$\| R (\mathrm{i} \omega ; A - B B ^ {*}) \| \leqslant M / | \mu |, \quad \forall \omega \in \mathbb {R}.$$

(7) $\Longrightarrow$ (4) 从定理10.1.6推出. 证毕.

现在我们讨论保守系统的近似能控性和强能稳性之间的关系.

定理10.3.9 设 $A$ 是 $H$ 中具有紧豫解式的闭稠定线性算子， $B \in \mathcal{L}(U, H)$ . 假定 $A^{*} = -A$ . 那么如下命题是等价的：

(1) $(A, B)$ 是完全近似能控的；  
(2) $(A, B)$ 是强能稳的；  
(3) 对于任意正定对称算子 $K \in \mathcal{L}(U)$ , $T^{A-BKB^*}(t)$ 是强稳定的;  
(4) $T^{A - BB^*}(t)$ 是强稳定的；  
(5) $\sigma(A - BB^{*}) \cap \mathrm{i}\mathbb{R} = \varnothing$ (闭环频域条件);   
(6) $\mathcal{N}(B^{*}) \cap \mathcal{N}(\mathrm{i}\omega I - A) = \{0\}, \forall \omega \in \mathbb{R}$ . (唯一性条件).

证明 我们按 $(1) \Longrightarrow (6), (5) \Longrightarrow (4), (2) \Longrightarrow (6) \Longrightarrow (5), (6) \Longrightarrow (1), (4) \Longrightarrow (3) \Longrightarrow (2)$ 的顺序证明.
