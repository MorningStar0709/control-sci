# 随机变量、分布函数

设 $(\Omega, \mathcal{F}, P)$ 为概率空间， $\xi(\omega)$ 为定义在 $\Omega$ 上的实值函数.

如果对任一 Borel 集 $B, \{\omega : \xi(\omega) \in B\} \in \mathcal{F}$ , 那么称 $\xi$ (为了简化符号, 有时不写 $(\omega)$ ) 为对 $\mathcal{F}$ 可测, 或简称为可测, 记为 $\xi \in \mathcal{F}$ . 其实, $\xi \in \mathcal{F}$ 等价于对任一实数 $a, \{\omega : \xi(\omega) \leqslant a\} \in \mathcal{F}$ .

设 $\xi$ 为定义在 $\Omega$ 上的可测函数，并且 $P(|\xi| < \infty) = 1$ ，那么 $\xi$ 称为随机变量.

以后如不作特别说明，总认为 $(\Omega, \mathcal{F}, P)$ 为概率空间，单独用到 $\Omega, \mathcal{F}$ 或 $P$ 时，不再阐明它们的含义.

例4.1.4 设 $A \in \mathcal{F}$ , 定义

$$
I _ {A} = \left\{ \begin{array}{l l} 1, & \omega \in A, \\ 0, & \omega \notin A. \end{array} \right.
$$

$I_{A}$ 叫 $A$ 的示性函数．显然，示性函数为随机变量.

例4.1.5 设概率空间由例4.1.1定义，那么定义在[0,1]上任一a.e.有穷的Lebesgue可测函数都是随机变量.

例4.1.6 设概率空间由例4.1.2定义，定义

$$
\xi (\omega) = \left\{ \begin{array}{l l} a, & \quad \omega \in \left[ 0, \frac {1}{3}\right), \\ b, & \quad \omega \in \left[ \frac {1}{3}, 1 \right], \end{array} \right.
$$

a 和 b 为常数。那么 $\xi$ 为随机变量。但除此外，定义在 [0,1] 上的任何函数都不是随机变量。例如简单的线性函数 $\xi(\omega)=\omega,\omega\in[0,1]$ ，注意到当 0<x<1 时， $\{\omega:\xi(\omega)<x\}=[0,x)$ ，只要 $x\neq\frac{1}{3}$ 。它就不是可测集，所以在此概率空间中线性函数不是随机变量。

当 $\xi$ 是多维时， $\xi = [\xi^{1}, \cdots, \xi^{l}]^{T}$ ，如果每个分量 $\xi^{i}, i = 1, \cdots, l$ 都是随机变量，那么 $\xi$ 称为 l 维随机向量.

对随机变量 $\xi$ 可定义分布函数

$$F _ {\xi} (x) \stackrel {{\mathrm{def}}} {{=}} P (\omega : \xi (\omega) < x),$$

相应地对随机向量可定义多维的分布函数

$$F _ {\xi} (x ^ {1}, \dots , x ^ {l}) \stackrel {{\text { def }}} {{=}} P (\omega : \xi^ {1} (\omega) < x ^ {1}, \dots , \xi^ {l} (\omega) < x ^ {l}).$$

如果 $F_{\xi}(x)$ 可微分，那么它的导数 $f_{\xi}(x) = \frac{\mathrm{d}F_{\xi}(x)}{\mathrm{d}x}$ 叫 $\xi$ 的密度，

$$F _ {\xi} (x) = \int_ {- \infty} ^ {x} f _ {\xi} (t) \mathrm{d} t.F _ {\xi} (x ^ {1}, \dots , x ^ {l}) = \int_ {- \infty} ^ {x ^ {1}} \dots \int_ {- \infty} ^ {x ^ {l}} f _ {\xi} (t ^ {1}, \dots , t ^ {l}) \mathrm{d} t ^ {1} \dots \mathrm{d} t ^ {l}. \tag {4.1.5}$$

分布函数有下列简单性质：

(1) 左连续 $\lim_{\epsilon \to +0} F_{\xi}(x - \epsilon) = F_{\xi}(x)$ ;   
(2) $F(-\infty)=0, F(+\infty)=1;$   
(3) 单调非降;  
(4) $F(\cdot)$ 的不连续点最多可列个.

例4.1.7 在例4.1.4中给出的随机变量的分布函数为

$$
F (x) = \left\{ \begin{array}{l l} 1, & \quad 1 <   x <   \infty , \\ P (A ^ {c}), & \quad 0 <   x \leqslant 1, \\ 0, & \quad - \infty <   x \leqslant 0. \end{array} \right.
$$

例4.1.8 在例4.1.6中的随机变量的分布函数为（设 $a < b$ ）

$$
F (x) = \left\{ \begin{array}{l l} 1, & b <   x <   \infty , \\ p, & a <   x \leqslant b, \\ 0, & - \infty <   x \leqslant a. \end{array} \right.
$$

分布函数中最重要者是正态分布，也叫 Gauss 分布，它有密度

$$f (x) = \frac {1}{\sqrt {2 \pi} \sigma} \exp \left\{- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}} \right\}, \quad x \in \mathbb {R} ^ {1}, \sigma > 0.$$

它的多维形式为

$$\frac {1}{(2 \pi) ^ {\frac {1}{2}} (\det R) ^ {\frac {1}{2}}} \exp \left\{- \frac {1}{2} (x - \mu) ^ {\mathrm{T}} R ^ {- 1} (x - \mu) \right\}, \quad R > 0, x, \mu \in \mathbb {R} ^ {l}. \tag {4.1.6}$$
