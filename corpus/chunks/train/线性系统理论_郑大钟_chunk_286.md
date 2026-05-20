$$\bar {N} (s) = N (s) T (s), \quad \bar {D} (s) = D (s) T (s) \tag {7.77}$$

其中 $T(s)$ 为非奇异多项式矩阵。而由(7.77)，可进一步导出

$$\deg \det \bar {D} (s) = \deg \det D (s) + \deg \det T (s) \tag {7.78}$$

考虑到 $\deg \det T(s) > 0$ ，所以即有

$$\deg \det \overline {{D}} (s) > \deg \det D (s) \tag {7.79}$$

表明，当 $N(s)D^{-1}(s)$ 为不可简约时，其阶数为最小。必要性得证。

（2）充分性：已知 $N(s)D^{-1}(s)$ 的阶次为最小，但反设 $N(s)D^{-1}(s)$ 是可简约的。则据性质3的证明过程可知，通过定出 $N(s)$ 和 $D(s)$ 的一个最大右公因子 $R(s)$ ，那么由

$$\widetilde {N} (s) = N (s) R ^ {- 1} (s), \quad \widetilde {D} (s) = D (s) R ^ {- 1} (s) \tag {7.80}$$

构成的 MFD $\widetilde{N}(s)\widetilde{D}^{-1}(s)$ 必为不可简约的。进而，由(7.80)又可导出 $\widetilde{D}(s)R(s) = D(s)$ ，并相应地有

$$\deg \det \widetilde {D} (s) + \deg \det R (s) = \deg \det D (s) \tag {7.81}$$

但已知 $R(s)$ 为非奇异而不是单模阵，所以可知 $\deg \det R(s) > 0$ ，从而还可导出

$$\deg \det \widetilde {D} (s) < \deg \det D (s) \tag {7.82}$$

而这是和 $N(s)D^{-1}(s)$ 已知为最小阶的事实相矛盾的。因而，反设不成立，即 $N(s)D^{-1}(s)$ 为不可简约MFD。充分性得证。

(3) 当 $N(s)D^{-1}(s)$ 和 $A^{-1}(s)B(s)$ 均为 $G(s)$ 的不可简约 MFD 时，则由性质6的关系式(7.75)即可导出结论 $n_r = n_l$ 。于是就完成了证明。
