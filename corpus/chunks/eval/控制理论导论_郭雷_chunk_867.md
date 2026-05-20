由定理 11.7.3 可知 FMS 一般已是稳定的。由于控制理论中镇定可用极点配置来实现的，因此对 DEDS 可用“周期配置”来代替“稳定”的地位。在这个意义下，我们研究了稳定的干扰解耦问题 (DDPS) 在 DEDS 中对应的问题，得到了能解的充要条件，这个条件是定理 11.7.7 与定理 11.6.2 的条件的结合。在线性多变量控制的几何方法中，还有输出稳定化问题 (OSP)。有限制的调节器问题 (RRP)，带内部稳定的调节器问题 (RPIS) 等。把“周期配置”或“周期合并配置”来代替“稳定”的地位后，可研究上述几个问题在 DEDS 中对应的问题，得到能解的充要条件。有兴趣的读者可参阅文献 [10] 的引文。

综上所述，几何方法在 DEDS 中对应的问题，有些变得困难了，如 $[1, N]$ 上能达子模问题；有些变得容易了，如干扰解耦问题。许多问题可以有不同的提法。

实现理论是传统线性控制系统理论的一个重要组成部分，环上实现理论比域上的困难得多。我们可类似地在 DEDS 中引入实现理论中的有关定义。

定义11.7.4 设 $\{G(k)\}_{k=1}^{\infty}$ 是一个矩阵序列， $G(k) \in D^{m \times p}$ ，且

$$
\boldsymbol {G} (k) = \left[ \begin{array}{c c c c} g _ {1 1} (k) & g _ {1 2} (k) & \dots & g _ {1 p} (k) \\ g _ {2 1} (k) & g _ {2 2} (k) & \dots & g _ {2 p} (k) \\ \vdots & \vdots & & \vdots \\ g _ {m 1} (k) & g _ {m 2} (k) & \dots & g _ {m p} (k) \end{array} \right].
$$

如果存在矩阵 $\pmb{A} \in D^{n \times n}, \pmb{B} \in D^{m \times n}, \pmb{C} \in D^{n \times p}$ . 满足

$$\boldsymbol {B} \boldsymbol {A} ^ {k - 1} \boldsymbol {C} = \boldsymbol {G} (k), \quad k = 1, 2, \dots , \tag {11.7.4}$$

则称 $\{G(k)\}_{k=1}^{\infty}$ 是能实现的，系统

$$
\Sigma : \left\{ \begin{array}{l} \boldsymbol {X} (k) = \boldsymbol {X} (k - 1) \boldsymbol {A} \oplus \boldsymbol {U} (k) B, \\ \boldsymbol {Y} (k) = \boldsymbol {X} (k) C \end{array} \right. \tag {11.7.5}
$$

称为 $\{G(k)\}_{k=1}^{\infty}$ 的一个实现， $\Sigma$ 也可记为 $(A, B, C)$ . 如果 $(A, B, C)$ 在所有实现中 $A$ 的阶数 $n$ 是最低的，则称它为一个最小实现、维数为 $n$ .

文献[10]用图论方法证明了以下两定理：

定理11.7.9 $\{G(k)\}_{k=1}^{\infty}$ 能实现的充要条件是，对每个 $\{g_{ij}(k)\}_{k=1}^{\infty}, 1 \leqslant i \leqslant m, 1 \leqslant j \leqslant p$ ，存在 $\lambda_{ij}(h), d_{ij}, k_{ij_0}$ ，使得对所有 $k > k_{ij_0}$ ，有

$$g _ {i j} (k + d _ {i j}) = \lambda_ {i j} (h) ^ {d _ {i j}} g _ {i j} (k), \tag {11.7.6}$$

这里 $h \equiv k - k_{ij_0} (\bmod d_{ij})$ ，乘表示通常的加.

定理 11.7.10 最小实现一定是结构能达能观测的.

反之，结构能达能观测的实现却不一定是最小实现，有以下反例：

例11.7.3 设 $\{g(k)\}_{k=1}^{\infty} = \{\varepsilon, 1, 2, 3, \varepsilon, 5, \varepsilon, 7, 8, 9, \varepsilon, 11, \cdots\}$ , 则

$$
\boldsymbol {A} _ {1} = \left[ \begin{array}{c c c c c} \cdot & 1 & \cdot & \cdot & \cdot \\ \cdot & \cdot & 1 & \cdot & \cdot \\ \cdot & \cdot & \cdot & 1 & \cdot \\ \cdot & \cdot & \cdot & \cdot & 1 \\ 1 & \cdot & \cdot & \cdot & \cdot \\ \end{array} \right], \quad \boldsymbol {B} _ {1} = [ 0 \dots \dots ], \quad \boldsymbol {C} _ {1} = \left[ \begin{array}{l} \cdot \\ 0 \\ 0 \\ 0 \\ \cdot \\ 0 \end{array} \right]
$$

是一个结构能达能观测的实现，但不是最小，因为还有更小的实现：

$$
\boldsymbol {A} = \left[ \begin{array}{c c c c c} \cdot & 1 & \cdot & \cdot & \cdot \\ 1 & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & 1 & \cdot \\ \cdot & \cdot & \cdot & \cdot & 1 \\ \cdot & \cdot & 1 & \cdot & \cdot \end{array} \right], \quad \boldsymbol {B} _ {1} = [ 0 \cdot 0 \cdot - ], \quad \boldsymbol {C} _ {1} = \left[ \begin{array}{c} \cdot \\ 0 \\ \cdot \\ \cdot \\ 0 \end{array} \right],
$$

这里 $\varepsilon$ 与·都表示 $-\infty$ .

许多文献都探讨了最小实现的构造方法，但只在一些特殊的情况与条件下得到了构造方法。在一般情况下，多输入多输出系统最小实现的构造问题至今尚未彻底解决。这个历时近20年而尚未解决的难题说明了没有减法的极大代数上实现理论的艰深！
