其中，待定系数矩阵 $F, G, H$ 和 $T$ 分别为 $n \times n, n \times q, n \times p$ 和 $n \times n$ 的实常阵。

在给出确定全维观测器（5.313）的计算方法之前，我们首先要讨论使（5.313）成为给定被估计系统（5.312）的全维观测器的一些有关理论问题。

结论1 对任意的 $x_0, z_0$ 和 $\pmb{u}$ , 使系统 (5.313) 成为被估计系统 (5.312) 的全维状态观测器的充分必要条件为:

(1) $TA - FT = GC, T$ 为非奇异   
(2) $H = TB$   
(3) F 的全部特征值 $\lambda_{i}(F), i = 1, 2, \cdots, n$ ，均具有负实部。

证 表 $e \triangleq z - Tx$ ，则利用 (5.312) 和 (5.313) 可导出：

$$
\begin{array}{l} \dot {\boldsymbol {e}} = \dot {\boldsymbol {z}} - T \dot {\boldsymbol {x}} = F \boldsymbol {z} + G \boldsymbol {y} + H \boldsymbol {u} - T A \boldsymbol {x} - T B \boldsymbol {u} \\ = F \boldsymbol {e} + (F T - T A + G C) \boldsymbol {x} + (H - T B) \boldsymbol {u} \tag {5.314} \\ \end{array}
$$

现来证明充分性。由条件(1)-(3)成立，意味着上述方程可表为 $\dot{\pmb{e}} = \pmb{Fe}$ ，且对任意 $x_0, z_0$ 和 $\pmb{u}$ 有

$$\lim _ {t \rightarrow \infty} e (t) = \lim _ {t \rightarrow \infty} \exp (F t) \left(z _ {0} - T x _ {0}\right) = 0 \tag {5.315}$$

这表明， $z(t)$ 是 $Tx(t)$ 的渐近估计，也即 $\hat{x}(t)$ 是 $x(t)$ 的渐近估计。充分性得证。

再来证明必要性。若条件(3)不成立，则对于 $x_{0}\neq0$ 和 $u(t)\equiv0$ ，当 $t\to\infty$ 时有 $e(t)$ 不趋于零。若条件(2)不成立即 $H\neq TB$ ，则可找到一个 $u(t)$ 使当 $t\to\infty$ 时， $e(t)$ 将不趋于零。而若条件(1)不成立即 $TA-FT\neq GC$ ，但 $\{A,B\}$ 为能控，则必可找到一个 $u(t)$ 而产生相应的一个 $x(t)$ ，使得当 $t\to\infty$ 时 $e(t)$ 不趋于零。从而，欲 $\hat{x}(t)$ 为 $x(t)$ 的渐近估计，必须使条件(1)—(3)成立。必要性得证。整个证明完成。

结论2 设 $A$ 和 $F$ 不具有公共的特征值，则方程 $TA - FT = GC$ 存在一个非奇异解 $T$ 的必要条件是 $\{A, C\}$ 为能观测和 $\{F, G\}$ 为能控。对于单输出 $(q = 1)$ 情形，这个条件也是充分条件。

证 先考虑 $q \neq 1$ 的情况。表 $A$ 的特征多项式为

$$\alpha (s) = \det (s I - A) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {5.316}$$

则据凯莱一哈密顿定理有 $\alpha(A) = 0$ 。再设 $\lambda_i$ 为 $F$ 的一个特征值，则 $\alpha(\lambda_i)$ 为 $\alpha(F)$ 的一个特征值。现知 $A$ 和 $F$ 不具有公共特征值，故对于 $F$ 的所有特征值 $\lambda_i$ 必有：

$$\alpha \left(\lambda_ {i}\right) \neq 0 \tag {5.317}$$

和

$$\det \alpha (F) = \prod_ {i = 1} ^ {n} \alpha \left(\lambda_ {i}\right) ^ {*} \neq 0 \tag {5.318}$$

这表明 $a(F)$ 为非奇异。进而，利用 $TA = FT + GC$ ，可得到

$$
\begin{array}{l} T A ^ {2} - F ^ {2} T = (F T + G C) A - F ^ {2} T \\ = F (T A - F T) + G C A = F G C + G C A \\ T A ^ {3} - F ^ {3} T = \left(T A ^ {2} - F ^ {2} T\right) A + F ^ {2} (T A - F T) \\ \end{array}
= G C A ^ {2} + F G C A + F ^ {2} G C
$$

● ● ● ● ●

于是，将上述结果整理之，并增补入显等式，可得到如下的一组方程：

$$T I - I T = 0T A - F T = G CT A ^ {2} - F ^ {2} T = G C A + F G CT A ^ {3} - F ^ {3} T = G C A ^ {2} + F G C A + F ^ {2} G C \tag {5.319}$$

● ● ● ● ● ●

$$T A ^ {n} - F ^ {n} T = G C A ^ {n - 1} + F G C A ^ {n - 2} + \dots + F ^ {n - 2} G C A + F ^ {n - 1} G C$$
