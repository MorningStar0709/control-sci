N _ {l e} = \left[ \begin{array}{c c c c c} 1 & 0 & 0 & 0 & 0 \\ - 1 & 0 & 1 & 0 & 0 \end{array} \right]
$$

进一步，又可算出

$$
D _ {h c} ^ {- 1} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right], \quad D _ {h c} ^ {- 1} D _ {l e} = \left[ \begin{array}{c c c c c} 4 & 4 & 0 & 1 & 2 \\ 0 & 0 & 4 & 5 & 2 \end{array} \right]
$$

于是，根据推论1和2，就即可定出给定 $N(s)D^{-1}(s)$ 的控制器形实现 $(A_{\bullet}, B_{\bullet}, C_{\bullet})$ 为：

$$
A _ {e} = \left[ \begin{array}{c c c c c c} - 4 & - 4 & 0 & - 1 & - 2 \\ 1 & 0 & 0 & 0 & 0 \\ \hline 0 & 0 & - 4 & - 5 & - 2 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \end{array} \right], \quad B _ {e} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \\ \hline - 1 & 0 \\ 0 & 0 \\ 0 & 0 \end{array} \right]

C _ {e} = \left[ \begin{array}{c c c c c} 1 & 0 & 0 & 0 & 0 \\ - 1 & 0 & 1 & 0 & 0 \end{array} \right]
$$

控制器形实现的性质 下面,我们进一步来指出并论证控制器形实现 $(A_{c}, B_{c}, C_{c})$ 的一些性质。

性质1 对于一般的右 MFD $N(s)D^{-1}(s)$ ，其控制器形实现 $(A_{e}, B_{e}, C_{e})$ 中， $(A_{e}, B_{e})$ 必是完全能控的，但 $(A_{e}, C_{e})$ 不能保证必是完全能观测的。

性质2 右 MFD $N(s) D^{-1}(s)(D(s)$ 为列既约）和其控制器形实现 $(A_{c}, B_{c}, C_{c})$ 之间存在如下的关系式：

$$
\left[ \begin{array}{c c} s I - A _ {c} & B _ {c} \\ - C _ {c} & 0 \end{array} \right] \left[ \begin{array}{l l} \Psi (s) & 0 \\ 0 & I \end{array} \right] = \left[ \begin{array}{l l} B _ {c} & 0 \\ 0 & I \end{array} \right] \left[ \begin{array}{l l} D (s) & I \\ - N (s) & 0 \end{array} \right] \tag {9.115}
$$

其中

$$\{\Psi (s), D (s) \} \text {为右互质} \tag {9.116}\{s I - A _ {c}, B _ {e} \} \text {为左互质} \tag {9.117}$$

证（1）先证明(9.115)。为此，利用等式

$$N _ {l c} (s I - A _ {c}) ^ {- 1} B _ {e} = C _ {c} (s I - A _ {c}) ^ {- 1} B _ {e} = N (s) D ^ {- 1} (s) = N _ {l c} \Psi (s) D ^ {- 1} (s)$$

并考虑到 $N_{lc}$ 的任意性，故可导出

$$(s I - A _ {c}) ^ {- 1} B _ {e} = \Psi (s) D ^ {- 1} (s) \tag {9.118}$$

从而，必可建立如下的一组等式：

$$
\left\{ \begin{array}{c} (s I - A _ {c}) \Psi (s) = B _ {c} D (s) \\ B _ {c} = B _ {c} \\ - C _ {c} \Psi (s) = - N (s) \\ 0 = 0 \end{array} \right. \tag {9.119}
$$

于是,将其表为分块矩阵形式,就即得(9.115)。

(2) 再来证明(9.116)。从 $\Psi(s)$ 的表达式

$$
\Psi (s) = \left[ \begin{array}{c c c} \left[ \begin{array}{c c c} s ^ {k _ {1} - 1} & & \\ \vdots & & \\ 1 & & \\ \hdashline \ddots & & \\ & \ddots & \\ & & \left| \begin{array}{c c c} s ^ {k _ {p} - 1} & & \\ & \vdots & \\ & 1 & \end{array} \right. \end{array} \right] \Bigg \} k _ {1} \\ \underbrace {\left[ \begin{array}{c c c} & & \\ & \ddots & \\ & & \end{array} \right]} _ {p} \end{array} \right\}. \tag {9.120}
$$

不难看出， $\Psi(s)$ 中包含一个 $I_{p0}$ 这表明，必有

$$
\operatorname{rank} \left[ \begin{array}{l} D (s) \\ \Psi (s) \end{array} \right] = p, \forall s \in \mathcal {C} \tag {9.121}
$$
