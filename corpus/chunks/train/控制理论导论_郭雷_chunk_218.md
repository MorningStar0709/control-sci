# 3.4 同伦理论

同伦是代数拓扑的基本工具。它们力图用代数的方法刻画形体的几何特征。基本群和同调群也被用于研究线性系统簇的性质。

定义 3.4.1 设 X, Y 为两个拓扑空间，f, g 为两个从 X 到 Y 的映射，I = [0, 1],

(1) $f$ 和 $g$ 称为同伦的，记作 $f \simeq g$ ，如果存在一个连续映射 $H: X \times I \to Y$ ，称为 $f$ 和 $g$ 的同伦，使得

$$
\left\{ \begin{array}{l} H (x, 0) = f (x), \\ H (x, 1) = g (x); \end{array} \right. \tag {3.4.1}
$$

(2) 设 $A \subset X$ . $f$ 和 $g$ 称为关于 $A$ 的同伦, 记作 $f \simeq_A g$ , 如果除式 (3.4.1) 外我们还有

$$H (x, t) = f (x) = g (x), \quad x \in A. \tag {3.4.2}$$

定义 3.4.2 (1) 两个拓扑空间 X, Y 称为同伦，记作， $X \simeq Y$ ，如果存在映射 $f: X \to Y$ 和映射 $g: Y \to X$ ，使得

$$g \circ f \simeq \mathrm{id} _ {X}; \quad f \circ g \simeq \mathrm{id} _ {Y},$$

这里 $\mathrm{id}_X$ 和 $\mathrm{id}_Y$ 分别为 $X$ 和 $Y$ 上的恒等映射；

(2) 一个拓扑空间 $X$ 称为可收缩的，如果它同伦于一个单点.

例3.4.1 (1) 如果两个拓扑空间 $X$ 与 $Y$ 同胚，则它们同伦；

(2) $\mathbb{R}^2\backslash \{0\} \simeq S^1;$

(3) 一个星形集 $S \subset \mathbb{R}^n$ 是这样一个集合，存在一个点 $c \in S$ 使得对每一点 $x \in S$ , 线段 $[x, c] \in S$ . 特别是，一个凸集一定是一个星形集. $\mathbb{R}^n$ 中的一个星形集是可收缩的.
