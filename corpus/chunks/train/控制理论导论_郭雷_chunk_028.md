# Kronecker 积

定义1.1.1 对于任意两个矩阵 $\pmb{A} \in \mathbb{C}^{m \times n}$ 和 $\pmb{B} \in \mathbb{C}^{p \times q}$ , 其Kronecker积(又称张量积)定义为

$$
\boldsymbol {A} \otimes \boldsymbol {B} \stackrel {\text {def}} {=} \left[ \begin{array}{c c c c} a _ {1 1} B & a _ {1 2} B & \dots & a _ {1 n} B \\ a _ {2 1} B & a _ {2 2} B & \dots & a _ {2 n} B \\ \vdots & \vdots & & \vdots \\ a _ {m 1} B & a _ {m 2} B & \dots & a _ {m n} B \end{array} \right] \in \mathbb {R} ^ {m p \times n q}.
$$

对 Kronecker 积，成立下列基本公式：

(a) 数乘 设 $A, B$ 为复数域 $\mathbb{C}$ 上的矩阵， $\alpha \in \mathbb{C}$ ，则

$$\alpha (\boldsymbol {A} \otimes \boldsymbol {B}) = (\alpha \boldsymbol {A}) \otimes \boldsymbol {B} = \boldsymbol {A} \otimes (\alpha \boldsymbol {B}).$$

(b) 分配律 设 $A, B$ 为复数域 $\mathbb{C}$ 上阶数相同的矩阵，则

$$(A + B) \otimes C = (A \otimes C) + (B \otimes C).\boldsymbol {C} \otimes (\boldsymbol {A} + \boldsymbol {B}) = (\boldsymbol {C} \otimes \boldsymbol {A}) + (\boldsymbol {C} \otimes \boldsymbol {B}).$$

(c) 结合律

$$\boldsymbol {A} \otimes (\boldsymbol {B} \otimes \boldsymbol {C}) = (\boldsymbol {A} \otimes \boldsymbol {B}) \otimes \boldsymbol {C}.$$

(d) 转置

$$\left(\boldsymbol {A} \otimes \boldsymbol {B}\right) ^ {\mathrm{T}} = \boldsymbol {A} ^ {\mathrm{T}} \otimes \boldsymbol {B} ^ {\mathrm{T}}.$$

(e) 混合积 设 $A \in \mathbb{C}^{k \times m}, B \in \mathbb{C}^{m \times n}, C \in \mathbb{C}^{p \times q}, D \in \mathbb{C}^{q \times t}$ , 则

$$(A \otimes C) (B \otimes D) = A B \otimes C D.$$

(f) 逆 对于 $A \in \mathbb{C}^{n \times n}, B \in \mathbb{C}^{m \times m}$ , 若 $A^{-1}, B^{-1}$ 存在, 则 $(A \otimes B)^{-1}$ 也存在, 且

$$(A \otimes B) ^ {- 1} = A ^ {- 1} \otimes B ^ {- 1}.$$

(g) 迹 对于 $A \in \mathbb{C}^{n \times n}, B \in \mathbb{C}^{m \times m}$ , 有

$$\operatorname{tr} (\boldsymbol {A} \otimes \boldsymbol {B}) = \operatorname{tr} \boldsymbol {A} \cdot \operatorname{tr} \boldsymbol {B}. \tag {1.1.1}$$

所谓矩阵 $A \in \mathbb{R}^{m \times n}$ 的行展开，是将 $A$ 的各行依次横排后转置得到的 $mn$ 维列向量，列展开是将各列纵排得到的 $mn$ 维列向量，即

行展开

$$V _ {r} (\boldsymbol {A}) \stackrel {\text { def }} {=} [ a _ {1 1}, a _ {1 2}, \dots , a _ {1 n}, a _ {2 1}, a _ {2 2}, \dots , a _ {m n} ] ^ {\mathrm{T}}; \tag {1.1.2}$$

列展开

$$V _ {c} (\boldsymbol {A}) \stackrel {\text { def }} {=} [ a _ {1 1}, a _ {2 1}, \dots , a _ {m 1}, a _ {1 2}, a _ {2 2}, \dots , a _ {m n} ] ^ {\mathrm{T}}. \tag {1.1.3}$$

行展开和列展开有如下性质：

(I) 转置

$$V _ {r} (\boldsymbol {A} ^ {\mathrm{T}}) = V _ {c} (\boldsymbol {A}), \quad V _ {c} (\boldsymbol {A} ^ {\mathrm{T}}) = V _ {r} (\boldsymbol {A}).$$

(II) 积的展开
