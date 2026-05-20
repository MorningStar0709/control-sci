$$
\begin{array}{l} \left[ \begin{array}{c c c c} \bar {d} _ {1 1} (s) & & & \\ \bar {d} _ {2 1} (s) & \bar {d} _ {2 2} (s). & & \\ \vdots & & \ddots & \\ \bar {d} _ {p 1} (s) & \dots \dots \dot {\bar {d}} _ {p p} (s) \end{array} \right] = \left[ \begin{array}{c c c c} d _ {1 1} (s) & & & \\ d _ {2 1} (s) & d _ {2 2} (s). & & \\ \vdots & & \ddots & \\ d _ {p 1} (s) & \dots \dots \dot {d} _ {p p} (s) \end{array} \right] \\ \times \left[ \begin{array}{c c c c} c _ {1} & & & \\ w _ {2 1} (s) & c _ {2} \cdot & & \\ \vdots & & \ddots & \\ w _ {p 1} (s) & \dots \dots & c _ {p} \end{array} \right] \tag {6.15} \\ \end{array}
$$

由上式即可导出

$$\bar {d} _ {i i} (s) = d _ {i i} (s) c _ {i}, i = 1, 2, \dots , p \tag {6.16}$$

考虑到 $\bar{d}_{ii}(s)$ 和 $d_{ii}(s)$ 都是首1的，因此要(6.16)成立，当且仅当有

$$c _ {i} = 1, i = 1, 2, \dots , p \tag {6.17}$$

下面再来证明 $w_{ik}(s) = 0, i \neq k$ 。为此，可通过式(6.15)中非对角元间的对应关系式，来逐个地进行证明。如由

$$
\left\{ \begin{array}{l} \bar {d} _ {2 1} (s) = w _ {2 1} (s) d _ {2 2} (s) + d _ {2 1} (s) \\ \deg \bar {d} _ {2 1} (s) <   \deg \bar {d} _ {2 2} (s) = \deg d _ {2 2} (s) \end{array} \right. \tag {6.18}
$$

可导出 $w_{21}(s) = 0$ 。而由

$$
\left\{ \begin{array}{l} \bar {d} _ {3 1} (s) = w _ {3 1} (s) d _ {3 3} (s) + d _ {3 1} (s) \\ \deg \bar {d} _ {3 1} (s) <   \deg \bar {d} _ {3 3} (s) = \deg d _ {3 3} (s) \end{array} \right. \tag {6.19}
$$

可导出 $w_{31}(s)=0$ 。按此方式，最后即可证得

$$w _ {i k} (s) = 0, i \neq k \tag {6.20}$$

这样，就证明了 $W(s) = I$ 。从而，再由(6.13)，即得 $\overline{D}_H(s) = D_H(s)$ 。于是证明完成。

很自然，由上述结论，还可得出如下的推论。

推论 设 $A(s)$ 为 $q$ 维非奇异多项式矩阵， $\widetilde{A}(s) = \widetilde{U}(s)A(s)$ ， $\widetilde{U}(s)$ 为任一 $q$ 维单模阵，则多项式矩阵 $A(s)$ 和 $\widetilde{A}(s)$ 具有相同的行埃尔米特形。

上面指出的结论和推论在直观上反映了一个重要的事实，非奇异多项式矩阵的埃尔米特形具有强唯一性，即这个非奇异多项式矩阵连同由它通过右乘(或左乘)单模阵派生出来的一类多项式矩阵具有等同的埃尔米特形。从另一个角度看，则说明对非奇异多项式矩阵进行单模变换，将不改变它的埃尔米特形。
