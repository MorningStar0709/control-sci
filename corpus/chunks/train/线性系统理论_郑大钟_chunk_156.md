$$X (\infty) - X (0) = A ^ {T} \left(\int_ {0} ^ {\infty} X (t) d t\right) + \left(\int_ {0} ^ {\infty} X (t) d t\right) A \tag {4.54}$$

考虑到系统为渐近稳定，故知当 $t \to \infty$ 时有 $e^{At} \to 0$ ，从而可导出 $X(\infty) = 0$ 。由此，且注意到 $X(0) = Q$ ，并表 $P = \int_{0}^{\infty} X(t) dt$ ，那么 (4.54) 可进而表为：

$$A ^ {T} P + P A = - Q \tag {4.55}$$

这表明 $P = \int_0^\infty X(t)dt$ 即为李亚普诺夫方程的解矩阵。进一步，由 $X(t)$ 存在且唯一和 $X(\infty) = 0$ ，可知 $P = \int_0^\infty X(t)dt$ 存在且唯一。而由

$$P ^ {T} = \int_ {0} ^ {\infty} \left[ e ^ {A T _ {t}} Q e ^ {A t} \right] ^ {T} d t = \int_ {0} ^ {\infty} e ^ {A T _ {t}} Q e ^ {A t} d t = P$$

可知， $P = \int_0^\infty X(t)dt$ 为对称。再对任意的 $\pmb {x}_0\neq \pmb {0}$ ，可有

$$\boldsymbol {x} _ {0} ^ {T} P \boldsymbol {x} _ {0} = \int_ {0} ^ {\infty} \left(e ^ {A t} \boldsymbol {x} _ {0}\right) ^ {T} Q \left(e ^ {A t} \boldsymbol {x} _ {0}\right) d t \tag {4.56}$$

由于 $Q$ 为正定故可将其表为 $Q = N^{T}N$ ，其中 $N$ 为非奇异，于是（4.56）可进而表为

$$
\begin{array}{l} \boldsymbol {x} _ {0} ^ {T} P \boldsymbol {x} _ {0} = \int_ {0} ^ {\infty} \left(e ^ {A t} \boldsymbol {x} _ {0}\right) ^ {T} N ^ {T} N \left(e ^ {A t} \boldsymbol {x} _ {0}\right) d t \\ = \int_ {0} ^ {\infty} \| N e ^ {A t} x _ {0} \| ^ {2} d t > 0 \tag {4.57} \\ \end{array}
$$

也即 $P$ 为唯一且正定。至此，就完成了证明。

对结论2所给出的李亚普诺夫判据需要作如下四点说明。第一，在利用李亚普诺夫判据时，对 $Q$ 的唯一限制是其应为对称正定。显然，满足这种限制的 $Q$ 可有无穷多个；但是可以断言的是，判断的结果即系统是否为渐近稳定，和对 $Q$ 阵的不同选择无关。第二，这个结论实质上给出了矩阵 $A$ 的所有特征值均具有负实部的充分必要条件。第三，考虑到一般地说求解李亚普诺夫方程（4.50）并非是一件容易的事，所以李亚普诺夫判据的意义主要在于理论研究上的用途。第四，在结论2中，如果取 $Q$ 为正半定，且 $(A, Q^{1/2})$ 为能观测，则结论仍成立。

进而，表 $\lambda_{i}(A)$ 为矩阵 A 的特征值， $i=1,2,\cdots,n$ 。那么，我们可通过推广结论 2，而导出判断 A 的所有特征值的实部均小于某个负实值的李亚普诺夫判据。

结论3[李亚普诺夫判据的推广形式] 矩阵 $A$ 的所有特征值均小于负实值 $-\sigma_{2}$ 即

$$\operatorname{Re} \lambda_ {i} (A) < - \sigma , \quad \sigma \geqslant 0, i = 1, 2, \dots , n \tag {4.58}$$

的充分必要条件是对任意给定的一个正定对称矩阵 $Q$ ，如下的推广形式的李亚普诺夫方程

$$2 \sigma P + A ^ {T} P + P A = - Q \tag {4.59}$$

有唯一正定对称矩阵解 $P$ 。

证 表 $\tilde{A} = A + \sigma I$ ，则由

$$
\begin{array}{l} \det (\tilde {s} I - \tilde {A}) = \det (\tilde {s} I - A - \sigma I) = \det [ (\tilde {s} - \sigma) I - A ] \\ = \det (s I - A), \quad \tilde {s} = s + \sigma \tag {4.60} \\ \end{array}
$$

可知

$$\lambda_ {i} (\widetilde {A}) = \lambda_ {i} (A) + \sigma , \quad i = 1, 2, \dots , n \tag {4.61}$$

再利用结论2知， $\tilde{A}$ 的所有特征值均具有负实部的充分必要条件为对任一正定对称阵 $Q$

$$\widetilde {A} ^ {T} P + P \widetilde {A} = - Q \tag {4.62}$$
