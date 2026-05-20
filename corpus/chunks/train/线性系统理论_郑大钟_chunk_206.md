$$\boldsymbol {e} _ {i} ^ {T} P (0, 0, t _ {f}) \boldsymbol {e} _ {i} = p _ {i i} (0, 0, t _ {f})\boldsymbol {e} _ {i} ^ {T} P (0, 0, t _ {2}) \boldsymbol {e} _ {i} = p _ {i i} (0, 0, t _ {2})$$

又可导出，当 $t_2 > t_f$ 时，成立

$$p _ {i i} (0, 0, t _ {f}) \leqslant p _ {i i} (0, 0, t _ {2}), \quad i = 1, 2, \dots , n \tag {5.222}$$

这表明， $p_{ii}(0,0,t_f)$ 是关于 $t_f$ 的非降函数；而由前面的结论可知， $p_{ii}(0,0,t_f)$ 对 $t_f$ 有上界。从而就证得， $p_{ii}(0,0,t_f)$ 当 $t_f \to \infty$ 时极限存在。再证明非对角线元 $p_{ij}(0,0,t_f)$ 当 $t_f \to \infty$ 时的存在性。为此，取

$$x _ {0} = e _ {i} + e _ {j}, \quad i \neq j, i, j = 1, 2, \dots , n \tag {5.223}$$

则就有

$$
\begin{array}{l} \left(\boldsymbol {e} _ {i} + \boldsymbol {e} _ {j}\right) ^ {T} P (0, 0, t _ {f}) \left(\boldsymbol {e} _ {i} + \boldsymbol {e} _ {j}\right) = p _ {i i} (0, 0, t _ {f}) \\ + 2 p _ {i j} (0, \mathbf {0}, t _ {f}) + p _ {f i} (0, \mathbf {0}, t _ {f}) \tag {5.224} \\ \end{array}
$$

上式中，等式左端为关于 $t_f$ 的非降函数，同时 $p_{ii}(0, 0, t_f)$ 和 $p_{jj}(0, 0, t_f)$ 也是关于 $t_f$ 的非降函数，所以考虑到问题的一般性 $p_{ij}(0, 0, t_f)$ 也是关于 $t_f$ 的非降函数。但前已证得， $P(0, 0, t_f)$ 也即 $p_{ii}(0, 0, t_f)$ 对 $t_f$ 有界。从而，证明了对一切 $i$ 和 $j p_{ii}(0, 0, t_f)$

当 $t_{f} \to \infty$ 时极限存在。于是， $P(0, 0, \infty)$ 存在。证明完成。

(3) $P(t, 0, \infty)$ 必为不依赖于 $t$ 的常阵，将其记为 $P$ ，也即成立

$$P (t, 0, \infty) = P \tag {5.225}$$

证 考虑到 $P(t,0,\infty) = \lim_{t_f\to \infty}P(t,0,t_f)$ ，而 $P(t,0,t_f)$ 为非时变黎卡提方程(5.212)的解阵。因而，根据非时变性，易知 $P(t,0,t_f)$ 仅与 $(t_f - t)$ 有关而与 $t_f$ 和 $t$ 的具体值无直接的关系，也即成立

$$P (t, 0, t _ {f}) = P (0, 0, t _ {f} - t), \quad t \in [ 0, \infty) \tag {5.226}$$

利用上述关系式,进而可得

$$
\begin{array}{l} P (t, 0, \infty) = \lim _ {t _ {f} \rightarrow \infty} P (t, 0, t _ {f}) = \lim _ {t _ {f} \rightarrow \infty} P (0, 0, t _ {f} - t) \\ = P (0, 0, \infty), \quad t \in [ 0, \infty) \tag {5.227} \\ \end{array}
$$

这表明， $P(t,0,\infty)$ 和 t 无关。由此，若表 $P(0,0,\infty)=P$ 为常阵，就证明了 (5.225)。证明完成。

(4) P 为如下的矩阵黎卡提代数方程的解阵:

$$P A + A ^ {T} P + Q - P B R ^ {- 1} B ^ {T} P = 0 \tag {5.228}$$

证 由于 $P(t,0,\infty)$ 为如下的矩阵黎卡提微分方程

$$
\begin{array}{l} - \dot {P} (t) = P (t) A + A ^ {T} P (t) + Q - P (t) B R ^ {- 1} B ^ {T} P (t) \\ P (\infty) = 0, \quad t \in [ 0, \infty ] \tag {5.229} \\ \end{array}
$$

的解阵，且前已证得 $P(t,0,\infty) = P$ 为常阵，从而将此代入(5.229)即可导出(5.228)。证明完成。

(5) P 为正定对称矩阵。

证 由 $Q$ 和 $R$ 的对称性以及方程 (5.228) 的对称性, 即知 $P$ 为对称矩阵。再可导出:

$$\boldsymbol {x} _ {0} ^ {T} P \boldsymbol {x} _ {0} = \boldsymbol {x} _ {0} ^ {T} P (0, 0, \infty) \boldsymbol {x} _ {0} = \int_ {0} ^ {\infty} \left(\boldsymbol {x} ^ {* T} Q \boldsymbol {x} ^ {*} + \boldsymbol {u} ^ {* T} R \boldsymbol {u} ^ {*}\right) d t \tag {5.230}$$

其中
