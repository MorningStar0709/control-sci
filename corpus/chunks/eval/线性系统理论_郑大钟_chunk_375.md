$$
\begin{array}{l} \left[ \begin{array}{l l} U (s) & 0 \\ X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c c} P _ {1} (s) & Q _ {1} (s) \\ - R _ {1} (s) & W _ {1} (s) \end{array} \right] \left[ \begin{array}{l} \hat {\zeta} _ {1} (s) \\ - \hat {\boldsymbol {u}} (s) \end{array} \right] \\ = \left[ \begin{array}{c c} P _ {2} (s) & Q _ {2} (s) \\ - R _ {2} (s) & W _ {2} (s) \end{array} \right] \left[ \begin{array}{c c} V ^ {- 1} (s) & - V ^ {- 1} (s) Y (s) \\ \mathbf {0} & I _ {p} \end{array} \right] \left[ \begin{array}{l} \hat {\xi} _ {1} (s) \\ - \hat {\boldsymbol {u}} (s) \end{array} \right] \tag {10.119} \\ \end{array}
$$

进而，利用(10.114)和(10.115)，还可由上式得到

$$
\begin{array}{l} \left[ \begin{array}{l l} U (s) & 0 \\ X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c} 0 \\ - \hat {\mathcal {Y}} (s) \end{array} \right] = \left[ \begin{array}{c} 0 \\ - \hat {\mathcal {Y}} (s) \end{array} \right] = \left[ \begin{array}{c c} P _ {2} (s) & Q _ {2} (s) \\ - R _ {2} (s) & W _ {2} (s) \end{array} \right] \left[ \begin{array}{l} \hat {\zeta} _ {2} (s) \\ - \hat {\boldsymbol {u}} (s) \end{array} \right] \\ = \left[ \begin{array}{c c} P _ {2} (s) & Q _ {2} (s) \\ - R _ {2} (s) & W _ {2} (s) \end{array} \right] \left[ \begin{array}{c} V ^ {- 1} (s) \hat {\zeta} _ {1} (s) + V ^ {- 1} (s) Y (s) \hat {\boldsymbol {u}} (s) \\ - \hat {\boldsymbol {u}} (s) \end{array} \right] \tag {10.120} \\ \end{array}
$$

考虑到 $S_{2}(s)$ 为任意，所以由(10.120)即可证得

$$\hat {\xi} _ {2} (s) = V ^ {- 1} (s) \hat {\xi} _ {1} (s) + V ^ {- 1} (s) Y (s) \hat {\boldsymbol {u}} (s) \tag {10.121}$$

再将上式左乘 $V(s)$ ，并加整理，又可证得

$$\hat {\zeta} _ {1} (s) = V (s) \hat {\zeta} _ {2} (s) - Y (s) \hat {u} (s) \tag {10.122}$$

从而，就完成了证明。

结论3 给定两个多项式矩阵描述如(10.114)和（10.115）所示，令 $(A_{1}, B_{1}, C_{1}, E_{1}(p))$ 和 $(A_{2}, B_{2}, C_{2}, E_{2}(p))$ 分别为它们的属于能控类和能观测类实现中的任意两个实现，则当系统矩阵 $S_{1}(s)$ 和 $S_{2}(s)$ 为严格系统等价时，两个实现具有相同的维数和相同的特征多项式，即成立

$$\dim \left(A _ {1}\right) = \dim \left(A _ {2}\right) \tag {10.123}\det (s I - A _ {1}) = \det (s I - A _ {2}) \tag {10.124}$$

证 已知 $S_{2}(s)$ 严格等价于 $S_{1}(s)$ ，故由结论1知，两者具有同一传递函数矩阵，且 $\operatorname{det} P_{2}(s) = \beta_{0} \operatorname{det} P_{1}(s)$ 。于是，由此即可导出

$$\dim \left(A _ {2}\right) = \deg \det P _ {2} (s) = \deg \det P _ {1} (s) = \dim \left(A _ {1}\right) \tag {10.125}$$

和

$$\det (s I - A _ {2}) = \beta_ {2} \det P _ {2} (s) = \beta_ {0} \beta_ {2} \det P _ {1} (s) = \frac {\beta_ {0} \beta_ {2}}{\beta_ {1}} \det (s I - A _ {1})= \det (s I - A _ {1}) \tag {10.126}$$
