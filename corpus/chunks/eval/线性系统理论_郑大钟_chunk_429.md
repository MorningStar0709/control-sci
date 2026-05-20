$$
\begin{array}{l} G _ {c, v} (s) = [ I + D ^ {- 1} (s) N (s) N _ {c} (s) D _ {c} ^ {- 1} (s) \phi^ {- 1} (s) ] ^ {- 1} \\ = \phi (s) D _ {c} (s) [ \phi (s) D (s) D _ {c} (s) + N (s) N _ {c} (s) ] ^ {- 1} D (s) \tag {11.240} \\ \end{array}
$$

而当考虑 $\pmb{v}(t) = 0$ 时，有

$$\hat {\boldsymbol {e}} (s) = - D ^ {- 1} (s) N (s) N _ {c} (s) D _ {c} ^ {- 1} (s) \phi^ {- 1} (s) I _ {q} \hat {\boldsymbol {e}} (s) - D ^ {- 1} (s) \hat {\boldsymbol {w}} (s) \tag {11.241}$$

于是就可导出

$$
\begin{array}{l} G _ {c w} (s) = - [ I + D ^ {- 1} (s) N (s) N _ {c} (s) D _ {c} ^ {- 1} (s) \phi^ {- 1} (s) ] ^ {- 1} D ^ {- 1} (s) \\ = - \phi (s) D _ {c} (s) [ \phi (s) D (s) D _ {c} (s) + N (s) N _ {c} (s) ] ^ {- 1} \tag {11.242} \\ \end{array}
$$

由此结论得证。

结论2 考虑图11.23所示的输出反馈系统，其中受控系统可由 $q \times p$ 的真有理分式矩阵 $G_{o}(s)$ 完全表征， $G_{o}(s) = D^{-1}(s)N(s)$ 为左互质矩阵分式描述。再假定参考输入信号 $\pmb{v}(t)$ 和外部扰动信号 $\pmb{w}(t)$ 可由相应的模型 $\hat{\pmb{v}}(s) = D_{\nu}^{-1}(s)N_{\nu}(s)$ 和 $\hat{\pmb{w}}(s) = D_{\omega}^{-1}(s)N_{\omega}(s)$ 表征，且表 $D_{\nu}^{-1}(s)$ 和 $D_{\omega}^{-1}(s)$ 的诸元的不稳定极点的最小公分母为 $\phi(s)$ ，而 $N_{\nu}(s)$ 和 $N_{\omega}(s)$ 为任意。则当满足如下两个条件时：

(i) $\phi(s) = 0$ 没有一个根是 $G_{o}(s)$ 的传输零点，  
(ii) $p \geqslant q, p$ 和 $q$ 分别为受控系统的输入和输出维数，

必存在 $p \times q$ 的补偿器 $C(s)$ ，且 $C(s) = N_{c}(s)D_{c}^{-1}(s)$ 为真的有理分式矩阵，使得此输出反馈系统为渐近稳定并实现无静差跟踪。

证（i）先来证明按顺序 $G_{o}(s) - \phi^{-1}(s)I_{\bullet}$ 联接的串联系统是完全能控和完全能观测的。

容易看出， $G_{o}(s)-\phi^{-1}(s)I_{q}$ 串联可等价地表为 $N_{r}(s)D_{r}^{-1}(s)-(\phi(s)I_{q})^{-1}I_{q}$ 串联，其中 $D_{r}(s)$ 和 $N_{r}(s)$ 为右互质。而据串联系统的能控性和能观测性的基本结论知， $N_{r}(s)D_{r}^{-1}(s)-(\phi(s)I_{q})^{-1}I_{q}$ 是能观测的，当且仅当 $D_{r}(s)$ 和 $I_{q}N_{r}(s)$ 为右互质。但据假定知 $\{D_{r}(s), N_{r}(s)\}$ 为右互质，所以 $G_{o}(s)-\phi^{-1}(s)I_{q}$ 串联系统总是能观测的。再之， $N_{r}(s)D_{r}^{-1}(s)-(\phi(s)I_{q})^{-1}I_{q}$ 串联为能控当且仅当 $\phi(s)I_{q}$ 和 $I_{q}N_{r}(s)$ 为左互质，或者等价地为

$$\operatorname{rank} M (s) \triangleq \operatorname{rank} [ \phi (s) I _ {q} N _ {r} (s) ] = q, \forall s \in \mathscr {C} \tag {11.243}$$

再表 $\lambda$ 为 $G_{o}(s)$ 的任一传输零点，也即 $G_{o}(s) = N_{r}(s)D_{r}^{-1}(s)$ 为互质MFD下使 $N_{r}(s)$ 降秩的 $s$ 值。那么注意到 $\lambda$ 不是 $\phi (s) = 0$ 的根，因而成立

$$\operatorname{rank} M (s) = \operatorname{rank} \phi (s) I _ {q} = q, \forall s = \lambda \tag {11.244}$$

若表 $\beta$ 为 $\phi(s) = 0$ 的任一根, 则由于 $\beta$ 不是使 $N_r(s)$ 降秩的 $s$ 值, 且 $p \geqslant q$ , 所以又成立

$$\operatorname{rank} M (s) = \operatorname{rank} N _ {r} (s) = q, \forall s = \beta \tag {11.245}$$
