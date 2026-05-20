的一个单模矩阵， $R(s)$ 为 $\overline{D}(s)$ 和 $\overline{N}(s)$ 的一个最大右公因子。再表

$$
U ^ {- 1} (s) = V (s) = \left[ \begin{array}{l l} V _ {1 1} (s) & V _ {1 2} (s) \\ V _ {2 1} (s) & V _ {2 2} (s) \end{array} \right] \tag {7.84}
$$

其中， $\dim V_{u}(s)=\dim\overline{D}(s)$ 。则 $V_{u}(s)V_{u}^{-1}(s)$ 是给定 $\bar{N}(s)\overline{D}^{-1}(s)$ 的一个不可简约 MFD。

证 由(7.83)即可导出

$$
\begin{array}{l} \left[ \begin{array}{l} \bar {D} (s) \\ \bar {N} (s) \end{array} \right] = V (s) \left[ \begin{array}{c} R (s) \\ \mathbf {0} \end{array} \right] = \left[ \begin{array}{l l} V _ {1 1} (s) & V _ {1 2} (s) \\ V _ {2 1} (s) & V _ {2 2} (s) \end{array} \right] \left[ \begin{array}{c} R (s) \\ \mathbf {0} \end{array} \right] \\ = \left[ \begin{array}{l} V _ {1 1} (s) R (s) \\ V _ {2 1} (s) R (s) \end{array} \right] \tag {7.85} \\ \end{array}
$$

进而,考虑到 $R(s)$ 为非奇异的同时,又可得到

$$V _ {2 1} (s) = \bar {N} (s) R ^ {- 1} (s), \quad V _ {1 1} (s) = \bar {D} (s) R ^ {- 1} (s) \tag {7.86}$$

再根据算法1中的结论，即知 $V_{\mathbf{u}}(s)V_{\mathbf{u}}^{-1}(s)$ 为给定 $\bar{N} (s)\overline{D}^{-1}(s)$ 的一个不可简约MFD。证明完成。

从上述结论出发,可给出此算法的计算步骤如下:

① 求出使式(7.83)成立的单模矩阵 $U(s)$ ，这个步骤通常可采用行初等变换来完成。

② 计算 $U(s)$ 的逆矩阵 $U^{-1}(s)=V(s)$ 。

③ 将 $V(s)$ 进行分块化。令 $\overline{N}(s)$ 和 $\overline{D}(s)$ 分别为 $q \times p$ 和 $p \times p$ 矩阵，则在(7.84)中 $V_{11}(s)$ 和 $V_{21}(s)$ 相应地为 $p \times p$ 和 $q \times p$ 矩阵。而 $V_{21}(s)V_{11}^{-1}(s)$ 即为所要求取的不可简约 MFD。

算法3 和上述算法不同，此算法提供了由可简约 MFD $\vec{N}(s)\vec{D}^{-1}(s)$ 求出其左不可简约 MFD $A^{-1}(s)B(s)$ 的计算方法。这个算法的计算步骤为：

① 求解多项式矩阵方程

$$
[ - \bar {B} (s) \quad \bar {A} (s) ] \left[ \begin{array}{l} \bar {D} (s) \\ \bar {N} (s) \end{array} \right] = 0 \tag {7.87}
$$

找出它的一个多项式矩阵解 $\{\overline{A}(s),\overline{B}(s)\}$ ，且必成立 $\overline{A}^{-1}(s)\overline{B}(s) = \overline{N}(s)\overline{D}^{-1}(s)$ 。

② 判断 $\{\overline{A}(s), \overline{B}(s)\}$ 的左互质性。如果 $\overline{A}(s)$ 和 $\overline{B}(s)$ 为左互质，则 $\overline{A}^{-1}(s)\overline{B}(s)$ 即为所求的不可简约左 MFD。如果 $\overline{A}(s)$ 和 $\overline{B}(s)$ 不是左互质，则转入下一步。

③ 利用列初等运算, 求出 $\overline{A}(s)$ 和 $\overline{B}(s)$ 的一个最大左公因子 $\overline{R}(s)$ 。

④ 计算 $\bar{R}(s)$ 的逆矩阵 $\bar{R}^{-1}(s)$ 。

⑤ 计算 $\overline{R}^{-1}(s)\overline{A}(s)$ 和 $\overline{R}^{-1}(s)\overline{B}(s)$ ，取 $A(s) = \overline{R}^{-1}(s)\overline{A}(s)$ 和 $B(s) = \overline{R}^{-1}(s) \times \overline{B}(s)$ ，则 $A^{-1}(s)B(s)$ 即为不可简约的 MFD。

例 给定可简约 $\overline{N}(s)\overline{D}^{-1}(s)$ ，其中
