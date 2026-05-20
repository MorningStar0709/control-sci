# 椭圆边值问题解的正则性

为了第10章中讨论偏微分方程镇定的需要，这里我们简单介绍椭圆型边值问题解的存在性、唯一性和正则性，详见文献[9].设 $\Omega \subset \mathbb{R}^N$ 为单连通有界开区域，具有充分光滑边界 $\Gamma = \partial \Omega$ ，设 $\nu = \nu (x)$ 为 $\pmb{\Gamma}$ 上外法向单位向量.

考虑 Dirichlet 椭圆边值问题

$$
\left\{ \begin{array}{l l} \triangle y (x) = f (x), & x \in \Omega , \\ y (s) = g (s), & s \in \Gamma . \end{array} \right. \tag {5.4.1}
$$

对于 $\varphi \in \mathcal{D}(\Omega)$ , 若 $f$ 和 $g$ 充分光滑, 则从方程 (5.4.1) 通过分部积分可得

$$\int_ {\Omega} \nabla y \cdot \nabla \varphi \mathrm{d} x = \int_ {\Omega} f \varphi \mathrm{d} x, \quad \forall \varphi \in \mathcal {D} (\Omega).$$

可以减弱对于 $f$ 和 $g$ 的正则性要求。于是上述边值问题化成

$$
\left\{ \begin{array}{l l} {\text {给定} f \in H ^ {r _ {1}} (\varOmega), \qquad r _ {1} \geqslant - 1. g \in H ^ {r _ {2}} (\varGamma), r _ {2} \geqslant 1 / 2,} \\ {\text {求} y \in H ^ {1} (\varOmega) \text {满足} y | _ {\Gamma} = g \text {和}} \\ {\int_ {\varOmega} \nabla y \cdot \nabla \varphi \mathrm{d} x = \int_ {\varOmega} f \varphi \mathrm{d} x, \qquad \forall   \varphi \in H _ {0} ^ {1} (\varOmega).} \end{array} \right. \tag {5.4.2}
$$

问题 (5.4.2) 叫做方程 (5.4.1) 的变分形式或弱形式. 问题 (5.4.2) 的解叫做方程 (5.4.1) 的弱解.

从弱解的存在唯一性，通过现代偏微分方程理论的一套技巧，可以得到如下解的正则性结果：

定理5.4.7 设 $f \in H^{r_1}(\Omega)$ , $r_1 \geqslant -1$ . $g \in H^{r_2}(\Gamma)$ , $r_2 \in \mathbb{R}$ , 那么Dirichlet问题(5.4.1)有唯一(弱)解 $y \in H^s(\Omega)$ , 其中 $s = \min\{r_1 + 2, r_2 + 1/2\}$ , 满足

$$\left\| y \right\| _ {H ^ {s} (\Omega)} \leqslant C \left(\left\| f \right\| _ {H ^ {r _ {1}} (\Omega)} + \left\| g \right\| _ {H ^ {r _ {2}} (\Gamma)}\right), \tag {5.4.3}$$

式中 $C$ 为仅依赖于 $r_1, r_2$ 而与 $f \in H^{r_1}(\Omega)$ 和 $g \in H^{r_2}(\Gamma)$ 无关的正常数.

特别当 $r_1 \geqslant 0$ 和 $r_2 \geqslant 3/2$ 时，我们有 $s \geqslant 2, \triangle y = f \in L^2(\Omega)$ ，从而在这种情形下方程 (5.4.1) 的弱解在经典意义下满足。

若 $g = 0$ ，则当 $f\in H^{r_1}(\varOmega),r_1\geqslant -1$ 时，方程(5.4.1)的解 $y\in H^{r_1 + 2}(\varOmega)$ ；而若 $f = 0,$ 则当 $g\in H^{r_2}(\varGamma),r_2\in \mathbb{R}$ 时，方程(5.4.1)的解 $y\in H^{r_2 + 1 / 2}(\varOmega).$

设 $a > 0$ 为常数，对于Dirichlet椭圆边值问题

$$
\left\{ \begin{array}{l l} \triangle y (x) - a y (x) = f (x), & x \in \Omega , \\ y (s) = g (s), & s \in \Gamma , \end{array} \right. \tag {5.4.4}
$$

我们有类似的结果：

定理5.4.8 设 $f \in H^{r_1}(\Omega)$ , $r_1 \geqslant -1$ , $g \in H^{r_2}(\Gamma)$ , $r_2 \in \mathbb{R}$ , 那么问题 (5.4.4) 有唯一 (弱) 解 $y \in H^s(\Omega)$ , 其中 $s = \min\{r_1 + 2, r_2 + 1/2\}$ , 满足
