因为 Lie 代数是一个特殊的代数，则 Lie 子代数，理想都是定义好的子代数。由于 Lie 括号有反对称性， $I \subset V$ 是 Lie 代数 $V$ 的一个理想，当且仅当

$$[ X, Y ] \in I, \quad \forall X \in I, Y \in V.$$

对于一个 Lic 代数 $\mathcal{G}$ , 显然 $\mathcal{G}$ 自己和 $\{0\}$ 均为其理想. 这两个理想都为平凡理想.

Lie 代数之间作为代数的同态和同构，分别称为 Lie 代数同态和 Lie 代数同构.

例3.2.6 设 $V$ 为一 $n$ 维向量空间， $V$ 到自身的一个线性映射 $L: V \to V$ 称为一个自同态。自同态集合记为 $\operatorname{End}(V)$ 。给定两个自同态 $\phi, \psi \in \operatorname{End}(V)$ 。我们定义Lie括号

$$[ \phi , \psi ] X = \phi \psi (X) - \psi \phi (X), \quad \forall X \in V.$$

End(V) 带上这个 Lie 括号是一个 Lie 代数，将它记为 gl(V). 实际上，如果我们固定 V 的一组基，那么每一个 $\psi \in \text{End}(V)$ 都有一个矩阵表示。将它记作 $M_{\psi}$ 。那么由 $\psi \mapsto M_{\psi}$ 所定义的一个映射 $\Psi: \text{gl}(V) \to \text{gl}(n, \mathbb{R})$ 是一个 Lie 代数同构。

对 Lie 代数 $\mathcal{G}$ , 可定义两个导出列如下:

$$
\begin{array}{l} \mathcal {G} ^ {1} = \mathcal {G}, \\ \mathcal {G} ^ {k + 1} = [ \mathcal {G}, \mathcal {G} ^ {k} ], \quad k \geqslant 1; \\ \mathcal {G} ^ {(1)} = \mathcal {G}, \\ \mathcal {G} ^ {(k + 1)} = [ \mathcal {G} ^ {(k)}, \mathcal {G} ^ {(k)} ], \quad k \geqslant 1. \\ \end{array}
$$

定义 3.2.9 (1) 如果存在 $k^{*}$ 使 $G^{k^{*}} = \{0\}$ ，则称 Lie 代数 G 为幂零的；

(2) 如果存在 $k^{*}$ 使 $\mathcal{G}^{(k^{*})} = \{0\}$ , 则称 Lie 代数是可解的;  
(3) Lie 代数 $\mathcal{G}$ 称为单代数，如果它没有非平凡理想；  
(4) Lie 代数 G 称为半单的，如果它没有非零可解理想；  
(5) Lie 代数的最大可解理想称为根基 (radical), 记作 $r$ .

定理 3.2.1 $^{[16]}$ 任一 Lie 代数 G 可分解为

$$\mathcal {G} = s \oplus r, \tag {3.2.12}$$

这里 s 是半单 Lie 子代数，r 是根基.

式 (3.2.12) 称为 Levi 分解.

设 $\mathcal{G}$ 为一Lie代数， $V$ 为一 $n$ 维向量空间， $\operatorname {gl}(V)$ 为 $V$ 上所有线性变换构成的Lie代数(固定基 $\operatorname {gl}(V)$ 即为 $\operatorname {gl}(n,\mathbb{R})$

定义 3.2.10 一个 Lie 代数同态 $\phi: \mathcal{G} \to \operatorname{gl}(V)$ 称为 $\mathcal{G}$ 在 $V$ 上的一个表现. $\mathcal{G}$ 在自身的表现称为伴随表现 (adjoint representation), 记作 $\operatorname{ad}_{\mathcal{G}}$ .

例3.2.7 $\operatorname{sl}(2, \mathbb{R})$ 是迹为0的 $2 \times 2$ 实矩阵集。它是 $\operatorname{gl}(2, \mathbb{R})$ 的Lie子代数。它的一个基为

$$
\boldsymbol {e} _ {1} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right], \quad \boldsymbol {e} _ {2} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right], \quad \boldsymbol {e} _ {3} = \left[ \begin{array}{c c} 0 & 0 \\ 1 & 0 \end{array} \right].
$$

现在计算 $\mathrm{ad}_{\mathcal{G}}$ .因

$$[ e _ {1}, e _ {2} ] = e _ {1} e _ {2} - e _ {2} e _ {1} = 2 e _ {2},\left[ e _ {1}, e _ {3} \right] = e _ {1} e _ {3} - e _ {3} e _ {1} = - 2 e _ {3},\left[ e _ {2}, e _ {3} \right] = e _ {2} e _ {3} - e _ {3} e _ {2} = e _ {1},$$

以及
