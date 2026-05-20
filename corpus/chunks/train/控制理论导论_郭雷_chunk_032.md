$$\boldsymbol {X} (t; t _ {0}, \boldsymbol {X} _ {0}) = \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} (t - t _ {0})} \boldsymbol {X} _ {0} \mathrm{e} ^ {\boldsymbol {A} (t - t _ {0})} + \int_ {t _ {0}} ^ {t} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} (t - \tau)} \boldsymbol {Q} \mathrm{e} ^ {\boldsymbol {A} (t - \tau)} \mathrm{d} \tau , \tag {1.1.11}$$

且当 $Q = Q^{\mathrm{T}}$ ， $X_0 = X_0^{\mathrm{T}}$ 时，有

$$\boldsymbol {X} (t: t _ {0}, \boldsymbol {X} _ {0}) = [ \boldsymbol {X} (t: t _ {0}, \boldsymbol {X} _ {0}) ] ^ {\mathrm{T}} \in \mathbb {R} ^ {n \times n}. \tag {1.1.12}$$

推论1.1.2 若 $\pmb{A}$ 渐近稳定（即 $\pmb{A}$ 的所有特征值的实部小于零），则对于任意实矩阵 $X_0 \in \mathbb{R}^{n \times n}$ ，方程(1.1.10)的解 $X(t; t_0, X_0)$ 对 $t \geqslant t_0$ 一致有界。

对于给定的矩阵 $D \in \mathbb{R}^{n \times n}$ , $E \in \mathbb{R}^{m \times m}$ , $F \in \mathbb{R}^{m \times n}$ , 考察线性矩阵方程

$$\boldsymbol {X} \boldsymbol {D} + \boldsymbol {E} \boldsymbol {X} = - \boldsymbol {F}. \tag {1.1.13}$$

定理1.1.2 方程(1.1.13)存在唯一解的充分必要条件是， $D$ 及 $\pmb{E}$ 的特征值满足

$$\lambda_ {i} (\boldsymbol {D}) + \lambda_ {j} (\boldsymbol {E}) \neq 0, \quad i = 1, 2, \dots , n; j = 1, 2, \dots , m. \tag {1.1.14}$$

特别地，当 $m = n, D = A, E = A^{\mathrm{T}}, F = Q$ （其中 $Q = Q^{\mathrm{T}}$ ）时，方程 (1.1.13) 成为

$$\boldsymbol {X} \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {X} = - \boldsymbol {Q}. \tag {1.1.15}$$

鉴于线性矩阵方程 (1.1.15) 在稳定性理论等方面的重要性, 下面我们讨论其解的求法及性质.

首先，根据 $Q$ 的对称性容易证明，若方程(1.1.15)的解存在，记为 $\pmb{X}$ ，则 $\pmb{X}^{\mathrm{T}}$ 也是方程(1.1.15)的解。因此，若方程(1.1.15)具有唯一解 $\pmb{X} \in \mathbb{R}^{n \times n}$ ，则必为实对称解。

定理 1.1.3 若 A 渐近稳定，则方程 (1.1.15) 有唯一解 X, X 有下列性质：

(i) $X$ 可表示为

$$\boldsymbol {X} = \int_ {0} ^ {\infty} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {Q} \mathrm{e} ^ {\boldsymbol {A} t} \mathrm{d} t; \tag {1.1.16}$$

(ii) $Q > 0(< 0)\Longrightarrow X > 0(< 0)$ ;

(iii) $Q \geqslant 0 (\leqslant 0) \Longrightarrow X \geqslant 0 (\leqslant 0)$ ;

(iv) 在式 (1.1.13) 中设 $Q = Q_{1}(Q = Q_{2})$ , 令这时的解为 $X_{1}(X_{2})$ , 则

$$Q _ {1} > Q _ {2} \Longrightarrow X _ {1} > X _ {2};(\mathrm{v}) Q _ {1} \geqslant Q _ {2} \Longrightarrow X _ {1} \geqslant X _ {2}.$$
