$$
\begin{array}{l} C _ {2} (s I - A _ {2}) ^ {- 1} B _ {2} + E _ {2} (s) = C _ {1} (s I - A _ {1}) ^ {- 1} B _ {1} + E _ {1} (s) \\ = C _ {1} \left(s I - T ^ {- 1} A _ {2} T\right) ^ {- 1} T ^ {- 1} B _ {2} + E _ {2} (s) \\ = C _ {1} T ^ {- 1} \left(s I - A _ {2}\right) ^ {- 1} B _ {2} + E _ {2} (s) \tag {10.160} \\ \end{array}
$$

于是，由此就可得到

$$C _ {2} = C _ {1} T ^ {- 1} \tag {10.161}$$

因此，由(10.139)、(10.155)、(10.159)和(10.161)即可看出， $(A_{1}, B_{2}, C_{2}, E_{2}(p))$ 和 $(A_{1}, B_{1}, C_{1}, E_{1}(p))$ 为代数等价，充分性得证。至此，证明完成。

结论6 给定传递函数矩阵 $G(s)$ 为有理分式矩阵，且不要求为真的，则 $G(s)$ 的所有不可简约的MFD都是严格系统等价的。

证 分成如下的三种情况来进行证明。

① $G(s)$ 为严格真有理分式矩阵的情况。设 $N_{1}(s)D_{2}^{-1}(s)$ 和 $N_{2}(s)D_{2}^{-1}(s)$ 为 $G(s)$ 的任意两个不可简约的右MFD，则由 $\{D_1(s), N_1(s)\}$ 和 $\{D_2(s), N_2(s)\}$ 均为右互质可知，必存在单模阵 $T(s)$ 使成立

$$D _ {2} (s) = D _ {1} (s) T (s), N _ {2} (s) = N _ {1} (s) T (s) \tag {10.162}$$

于是，由此即可导出

$$
\left[ \begin{array}{l l} I _ {p} & 0 \\ 0 & I _ {q} \end{array} \right] \left[ \begin{array}{l l} D _ {1} (s) & I _ {p} \\ - N _ {1} (s) & 0 \end{array} \right] \left[ \begin{array}{l l} T (s) & 0 \\ 0 & I _ {p} \end{array} \right] = \left[ \begin{array}{l l} D _ {2} (s) & I _ {p} \\ - N _ {2} (s) & 0 \end{array} \right]. \tag {10.163}
$$

表明， $N_{1}(s)D_{1}^{-1}(s)$ 和 $N_{2}(s)D_{2}^{-1}(s)$ 的系统矩阵 $S_{1}(s)$ 和 $S_{2}(s)$ 是严格系统等价的。类似地也可证得， $G(s)$ 的任意两个不可简约的左MFD的系统矩阵也是严格系统等价的。

② $G(s)$ 为非真有理分式矩阵的情况。现表 $\bar{N}_i(s)D_i^{-1}(s), i = 1,2$ ，为非真 $G(s)$ 的任意两个不可简约的右 MFD，且进而可表为

$$\bar {N} _ {i} (s) D _ {i} ^ {- 1} (s) = N _ {i} (s) D _ {i} ^ {- 1} (s) + E (s), i = 1, 2 \tag {10.164}$$

其中， $N_{i}(s)D_{i}^{-1}(s)$ 为严格真的不可简约右 MFD， $E(s)$ 为多项式矩阵。考虑到由(10.164)可导出

$$\bar {N} _ {i} (s) = N _ {i} (s) + E (s) D _ {i} (s), i = 1, 2 \tag {10.165}$$

于是，就可得到

$$
\begin{array}{l} \left[ \begin{array}{c c} D _ {i} (s) & I _ {p} \\ - \bar {N} _ {i} (s) & 0 \end{array} \right] = \left[ \begin{array}{c c} D _ {i} (s) & I _ {p} \\ - [ N _ {i} (s) + E (s) D _ {i} (s) ] & 0 \end{array} \right] \\ = \left[ \begin{array}{l l} I _ {p} & 0 \\ - E (s) & I _ {q} \end{array} \right] \left[ \begin{array}{l l} D _ {i} (s) & I _ {p} \\ - N _ {i} (s) & E (s) \end{array} \right] \left[ \begin{array}{l l} I _ {p} & 0 \\ 0 & I _ {q} \end{array} \right] \tag {10.166} \\ \end{array}
$$

表明

$$
\left[ \begin{array}{l l} D _ {i} (s) & I _ {p} \\ - \bar {N} _ {i} (s) & 0 \end{array} \right] \sim \left[ \begin{array}{c c} D _ {i} (s) & I _ {p} \\ - N _ {i} (s) & E (s) \end{array} \right], i = 1, 2 \tag {10.167}
$$

再利用 $G(s)$ 为严格真时证得的结论, 又可有
