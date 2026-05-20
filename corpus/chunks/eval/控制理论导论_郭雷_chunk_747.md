$$G (t _ {f}) u = \int_ {0} ^ {t _ {f}} T (t _ {f} - s) B u (s) \mathrm{d} s, \qquad u \in L ^ {p} (0, t _ {f}; U), \tag {10.2.3}$$

则显然 $G(t_{f})$ 的值域 $\mathcal{R}(G(t_f))$ 在研究各种能控性概念时起着十分重要的作用.

定理10.2.1 设 $X$ 和 $U$ 是两个自反Banach空间，并设 $p > 1$ 满足 $\frac{1}{p} + \frac{1}{q} = 1$ . 那么下列三个命题是等价的，

(1) $(A, B)$ 在 $[0, t_f]$ 上精确能控；

(2) $\forall x \in X$ , 存在 $u \in L^{p}(0, t_{f}; U)$ 使得 $x = G(t_{f})u$ , 换句话说, $\mathcal{R}(G(t_{f})) = X$ ;

(3) 存在一常数 $\gamma > 0$ 使得

$$\left(\int_ {0} ^ {t _ {f}} \| B ^ {*} T ^ {*} (s) x ^ {*} \| ^ {q} \mathrm{d} s\right) ^ {\frac {1}{q}} \geqslant \gamma \| x ^ {*} \|, \quad \forall x ^ {*} \in X ^ {*}. \tag {10.2.4}$$

证明 (1) $\Longleftrightarrow$ (2) 是显然的. 为证 (2) $\Longleftrightarrow$ (3), 我们应用定理 5.1.9 于 $G = G(t_f)$ , $F = I, Y = X, Z = L^p(0, t_f; U)$ , 可知 $G(t_f) = X$ 等价于存在一常数 $\gamma > 0$ 使得

$$\| G (t _ {f}) ^ {*} x ^ {*} \| _ {L ^ {q} (0, t _ {f}; U ^ {*})} \geqslant \gamma \| x ^ {*} \|, \quad \forall x ^ {*} \in X ^ {*}, \tag {10.2.5}$$

这里我们已经使用了事实： $L^p (0,t_f;U)^* = L^q (0,t_f;U^*)$ .但简单的计算表明伴随算子 $G(t_{f})^{*}:X^{*}\to L^{q}(0,t_{f};U^{*})$ 由下式定义：

$$(G (t _ {f}) ^ {*} x ^ {*}) (t) = B ^ {*} T ^ {*} (t _ {f} - s) x ^ {*}, \qquad 0 \leqslant s \leqslant t _ {f}, \tag {10.2.6}$$

由此易见式 (10.2.5) 正好是式 (10.2.4). 证毕.

注意 $(A, B)$ 精确零能控等价于

$$\mathcal {R} (G (t _ {f})) \supset \mathcal {R} (T (t _ {f})),$$

由此从定理5.1.9, 我们直接得到

定理10.2.2 $(A,B)$ 在 $[0,t_f]$ 上精确零能控，当且仅当存在一常数 $\gamma >0$ 使得

$$\left\| T ^ {*} \left(t _ {f}\right) x ^ {*} \right\| \leqslant \gamma \| B ^ {*} T ^ {*} (\cdot) x ^ {*} \| _ {L ^ {q} \left(0, t _ {f}; U ^ {*}\right)}, \quad \forall x ^ {*} \in X ^ {*}.$$

定理10.2.3 设 $X$ 和 $U$ 是两个自反Banach空间．那么：

(1) $(A, B)$ 在 $[0, t_f]$ 上近似能控当且仅当

$$x ^ {*} \in X ^ {*}, B ^ {*} T ^ {*} (t) x ^ {*} = 0, \forall t \in [ 0, t _ {f} ] \Longrightarrow x ^ {*} = 0; \tag {10.2.7}$$

(2) $(A, B)$ 在 $[0, t_f]$ 上近似零能控当且仅当

$$x ^ {*} \in X ^ {*}, B ^ {*} T ^ {*} (t) x ^ {*} = 0, \forall t \in [ 0, t _ {f} ] \Longrightarrow T ^ {*} (t _ {f}) x ^ {*} = 0. \tag {10.2.8}$$

证明 应用定理 5.1.10 于 $G = G(t_f), F = I, Y = X, Z = L^p(0, t_f; U)$ 和 $p > 1$ ，立即得到所要的结论。

现在我们来讨论控制系统的另一个重要概念——能观测性，这是能控性的对偶概念。我们考虑如下线性系统：

$$
\left\{ \begin{array}{l l} \frac {\mathrm{d} z}{\mathrm{d} t} = F z (t), & z (0) = z _ {0}, \\ y (t) = C z (t), \end{array} \right. \tag {10.2.9}
$$

其中 $F$ 是自反Banach空间 $Z$ 中 $C_0$ 半群 $S(t)$ 的生成算子， $C \in \mathcal{L}(Z, Y)$ ， $Y$ 是另一个自反Banach空间，叫做观测空间。量测 $y(t)$ 可以通过方程(10.2.9)的温和解表示成

$$y (t) = C S (t) z _ {0}.$$

设 $q > 1$ 并定义线性算子 $P(t_{f}):Z\to L^{q}(0,t_{f};Y),$
