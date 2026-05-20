$$\pmb {a} ^ {T} A = \lambda_ {i} \pmb {a} ^ {T}, \pmb {a} ^ {T} B = 0 \tag {3.38}$$

则就有

$$\boldsymbol {a} ^ {T} \boldsymbol {B} = 0, \boldsymbol {a} ^ {T} \boldsymbol {A} \boldsymbol {B} = \lambda_ {i} \boldsymbol {a} ^ {T} \boldsymbol {B} = 0, \dots , \boldsymbol {a} ^ {T} \boldsymbol {A} ^ {n - 1} \boldsymbol {B} = 0 \tag {3.39}$$

从而，可得到

$$\alpha^ {T} [ B \mid A B \mid \dots \mid A ^ {n - 1} B ] = \alpha^ {T} Q _ {i} = 0 \tag {3.40}$$

这意味着 rank $Q_{n} < n$ 即系统为不完全能控。而这和已知条件相矛盾，因而反设不成立，必要性得证。

对充分性的证明可按与上相反的思路来进行,具体推证过程略去。从而,整个证明完成。

应当指出,一般地说,PBH 特征向量判据主要用于理论分析中,特别是线性系统的复频率域分析中。

结论 5 [约当规范形判据] 线性定常系统 (3.7) 为完全能控的充分必要条件是:

(1) 当矩阵 A 的特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 为两两相异时，为由 (3.7) 导出的对角线规范形

$$
\dot {\bar {x}} = \left[ \begin{array}{c c c} \lambda_ {1} & & \\ & \lambda_ {2} & \\ & & \ddots \\ & & \lambda_ {n} \end{array} \right] \bar {x} + \bar {B} u \tag {3.41}
$$

中， $\bar{B}$ 不包含元素全为零的行。

(2) 当矩阵 A 的特征值为 $\lambda_{1}(\sigma_{1}\text{重}), \lambda_{2}(\sigma_{2}\text{重}), \cdots, \lambda_{l}(\sigma_{l}\text{重})$ ，且 $(\sigma_{1} + \sigma_{2} + \cdots + \sigma_{l}) = n$ 时，为对 (3.7) 导出的约当规范形

$$\dot {\hat {x}} = \hat {A} \hat {x} + \hat {B} u \tag {3.42}$$

其中

$$
\hat {A} _ {(n \times n)} = \left[ \begin{array}{c c c} J _ {1} & & \\ & J _ {2} & \\ & & \ddots \\ & & J _ {l} \end{array} \right], \quad \hat {B} _ {(n \times p)} = \left[ \begin{array}{c} \hat {B} _ {1} \\ \hat {B} _ {2} \\ \vdots \\ \hat {B} _ {l} \end{array} \right] \tag {3.43}

J _ {i} \left(e _ {i} \times e _ {i}\right) = \left[ \begin{array}{c c c c} J _ {i 1} & & & \\ & J _ {i 2} & & \\ & & \ddots & \\ & & & J _ {i a _ {j}} \end{array} \right], \quad \hat {B} _ {i} \left(e _ {i} \times p\right) = \left[ \begin{array}{c} \hat {B} _ {i 1} \\ \hat {B} _ {i 2} \\ \vdots \\ \hat {B} _ {i a _ {j}} \end{array} \right] \tag {3.44}

\left. _ {\left(v _ {i k} \times r _ {i k}\right)} ^ {J _ {i k}} - \left[ \begin{array}{c c c c c} \lambda_ {i} & 1 & & & \\ & \lambda_ {i} & 1 & & \\ & & \ddots & \ddots & 1 \\ & & & \ddots & \lambda_ {i} \end{array} \right] \right., \quad \hat {B} _ {(v _ {i k} \times p)} = \left[ \begin{array}{c} \hat {b} _ {1 i k} \\ \hat {b} _ {2 i k} \\ \vdots \\ \hat {b} _ {s i k} \end{array} \right] \tag {3.44a}
$$

而 $(r_{n}+r_{n}+\cdots+r_{i\alpha_{i}})=\sigma_{i}$ ，由 $\hat{B}_{ik}(k=1,2,\cdots,\alpha_{i})$ 的最后一行所组成的矩阵

$$
\left[ \begin{array}{c} \hat {b} _ {r i 1} \\ \hat {b} _ {r i 2} \\ \vdots \\ \hat {b} _ {r i a j} \end{array} \right] \tag {3.45}
$$

对 $i=1,2,\cdots,l$ 均为行线性无关。
