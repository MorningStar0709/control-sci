$$\deg \det \overline {{D}} (s) < \deg \det D (s) \tag {7.8}$$

证 由(7.7)即可导出

$$
\begin{array}{r l} \bar {N} (s) \bar {D} ^ {- 1} (s) & = N (s) W ^ {- 1} (s) \cdot W (s) D ^ {- 1} (s) \\ & = N (s) D ^ {- 1} (s) = G (s) \end{array} \tag {7.9}
$$

表明 $N(s)D^{-1}(s)$ 为 $G(s)$ 的一个右 $\mathbf{MFD}$ 。再由

$$\bar {D} (s) W (s) = D (s) \tag {7.10}$$

可以得到

$$\deg \det \bar {D} (s) + \deg \det W (s) = \deg \det D (s) \tag {7.11}$$

考虑到 $\deg \det W(s) > 0$ ，从而由此即可导出(7.8)。于是结论得证。

(4) 令 $N(s)D^{-1}(s)$ 为 $G(s)$ 的一个右 MFD，而 $V(s)$ 为任一单模阵，且选取

$$\bar {N} (s) = N (s) V (s), \quad \bar {D} (s) ^ {\varnothing} = D (s) V (s) \tag {7.12}$$

则 $\overline{N}(s)\overline{D}^{-1}(s)$ 也为 $G(s)$ 的一个右MFD，且其阶次和 $N(s)D^{-1}(s)$ 相同，也即有

$$\deg \det \bar {D} (s) = \deg \det D (s) \tag {7.13}$$

(5) 给定传递函数矩阵 $G(s)$ 的所有 MFD 中, 一定存在一个次数为最小的 MFD, 称之为最小阶 MFD。而由性质(4)可知, 最小阶 MFD 也不是唯一的。  
(6) 令 $N(s)D^{-1}(s)$ 为 $G(s)$ 的一个非最小阶 MFD，则通过提出 $N(s)$ 和 $D(s)$ 的一个最大右公因子（gcrd），就可得到 $G(s)$ 的最小阶 MFD。  
(7) 考虑到 $G(s)$ 的右 MFD 和左 MFD 之间存在某种对偶性，因此上面有关右 MFD 所导出的一些属性，对左 MFD 也是对偶地成立的。基于这一原因，在以下各节的讨论中，我们将主要针对右 MFD 来进行。
