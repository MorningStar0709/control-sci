# 第7章

下面这些问题都是基于一个以状态变量形式描述的系统，系统矩阵为 A, B, C, D，输入为 u，输出为 y，状态为 x。

7.1 它提供了一个标准的方法来描述任意动态系统的微分方程，因此可以更方便地进行计算机辅助分析。它也更方便于分析以标准矩阵描述的线性系统。

7.2 $G(s) = C(sI - A)^{-1}B + D$

7.3 (a) $p=\mathrm{eig}(A)$ ;

(b) $p=\det[sI-A]$ 的根 =a(s)=0。

7.4 $z = \operatorname{det}\left[ \begin{array}{cc}sI - A & -B\\ C & D \end{array} \right]$

的根 $b(s)=0$ 。

7.5 (a) 如果矩阵对 $(A, B)$ 是可控的，即如果矩阵

$$
C = \left[ \begin{array}{l l l l} B & A B & \dots & A ^ {n - 1} B \end{array} \right]
$$

是满秩的。

(b) 如果系统可以写成能控标准形。

7.6 (a) 如果矩阵对 $(A, C)$ 是可观测的，即如果矩阵

$$
\mathcal {O} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {(n - 1)} \end{array} \right]
$$

是满秩的。

(b) 如果系统可以写成能观标准形。

7.7 (a) $p_{c}=\mathrm{eig}(A-B*K)$

(b) $p_{c}=\det(sI-A+BK)$ 的根 $=\alpha_{c}(s)=0$ 。

7.8 如果系统是可控的。

7.9 使用 LQR，闭环系统对参数改变将有更强的鲁棒性，并且设计者可以获得一些比闭环系统控制效果更好的控制。

7.10 当状态不可得到时(通常由于这样做花费很大或用传感器得到每一个状态变量是不切实际的)，那么一个仅用输出 y 的估计器可以给出用于代替实际状态的估计。

7.11 (a) $p_{e}=\mathrm{eig}(A-L*C)$

(b) $p_{e}=\det(sI-A+LC)$ 的根 $\alpha_{e}(s)=0$ 。

7.12 如果系统是可观测的。

7.13 $T(s)=K_{s}\frac{b(s)}{\alpha_{c}(s)}$

7.14 $T(s)=K_{s}\frac{\gamma(s)b(s)}{\alpha_{c}(s)\alpha_{c}(s)}$

通常 $\gamma(s)=\alpha_{e}(s)$ 。

7.15 (a) 通过增广过程状态来包括状态变量的积分器。

(b) 通过内模方法。

(c) 通过使用扩展估计器方法。
