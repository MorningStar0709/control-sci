当系统的多项式矩阵描述为可简约时，意味着 $\{P(s), Q(s)\}$ 或/和 $\{P(s), R(s)\}$ 包含非单模阵的最大公因子。因此，通过适当的变换，可以将一个可简约的 PMD 化成为不可简约的 PMD。给定多项式矩阵描述为：

$$
\left\{ \begin{array}{c} P (s) \hat {\zeta} (s) = Q (s) \hat {\boldsymbol {u}} (s) \\ \hat {\boldsymbol {y}} (s) = R (s) \hat {\zeta} (s) + W (s) \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {10.19}
$$

下面分成三种情况来讨论由可简约 PMD（10.19）来导出不可简约的 PMD:

① 设可简约 PMD 中， $\{P(s), R(s)\}$ 为右互质，但 $\{P(s), Q(s)\}$ 不是左互质。于是，通过求出矩阵对 $\{P(s), Q(s)\}$ 的一个最大左公因子 $H(s)$ ，并将 $P(s)$ 和 $Q(s)$ 表为两个多项式矩阵乘积，即

$$P (s) = H (s) \bar {P} (s), Q (s) = H (s) \bar {Q} (s) \tag {10.20}$$

就可知 $\{\overline{P}(s),\overline{Q}(s)\}$ 必是左互质的。进而，将(10.20)代入(10.19)，可得到

$$
\left\{ \begin{array}{c} H (s) \bar {P} (s) \hat {\zeta} (s) = H (s) \bar {Q} (s) \hat {\boldsymbol {u}} (s) \\ \hat {\boldsymbol {y}} (s) = R (s) \hat {\zeta} (s) + W (s) \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {10.21}
$$

这样，将上述第一个方程左乘 $H^{-1}(s)$ ，且考虑到

$$
\operatorname{rank} \left[ \begin{array}{l} P (s) \\ R (s) \end{array} \right] = \operatorname{rank} \left[ \begin{array}{l} \bar {P} (s) \\ R (s) \end{array} \right], \forall s \in \mathcal {C} \tag {10.22}
$$

就导出了(10.19)的可简约 PMD 的一个不可简约 PMD:

$$
\left\{ \begin{array}{c} \widetilde {P} (s) \hat {\zeta} (s) = \widetilde {Q} (s) \hat {\alpha} (s) \\ \hat {y} (s) = R (s) \hat {\zeta} (s) + W (s) \hat {\alpha} (s) \end{array} \right. \tag {10.23}
$$

② 设可简约 PMD 中， $\{P(s), Q(s)\}$ 为左互质，但 $\{P(s), R(s)\}$ 不是右互质的。现求出 $\{P(s), R(s)\}$ 的一个最大右公因子 $F(s)$ ，且可表为

$$P (s) = \widetilde {P} (s) F (s), R (s) = \widetilde {R} (s) F (s) \tag {10.24}$$

其中 $\{\tilde{P}(s),\tilde{R} (s)\}$ 为右互质。这样，通过对(10.19)引入变换 $\xi (s) = F(s)\hat{\xi} (s),F(s)$ 为非奇异，就可得到

$$
\left\{ \begin{array}{c} \tilde {P} (s) \xi (s) = Q (s) \hat {\boldsymbol {u}} (s) \\ \hat {\boldsymbol {y}} (s) = \tilde {R} (s) \xi (s) + W (s) \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {10.25}
$$

再考虑到必有 $\operatorname{rank}[P(s) Q(s)] = \operatorname{rank}[\tilde{P}(s) Q(s)]$ ，所以 $\{\tilde{P}(s), Q(s)\}$ 为左互质。从而，(10.25)即为(10.19)的一个不可简约 $\mathbf{PMD}$ 。

③ 设可简约 PMD 中， $\{P(s), Q(s)\}$ 和 $\{P(s), R(s)\}$ 都不是互质的。这种情况即为前面两种情况的组合。通过求出 $\{P(s), Q(s)\}$ 的最大左公因子 $H(s)$ 和 $\{H^{-1}(s), P(s), R(s)\}$ 的最大右公因子 $\bar{F}(s)$ ，并定义

$$
\left\{ \begin{array}{l} \hat {P} (s) = H ^ {- 1} (s) P (s) \bar {F} ^ {- 1} (s), \quad \hat {Q} (s) = H ^ {- 1} (s) Q (s) \\ \hat {R} (s) = R (s) \bar {F} ^ {- 1} (s) \end{array} \right. \tag {10.26}
$$
