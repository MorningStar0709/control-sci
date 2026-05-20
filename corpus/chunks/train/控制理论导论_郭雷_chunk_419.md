$$\| y \| _ {H ^ {s} (\Omega)} \leqslant C \left(\| f \| _ {H ^ {r _ {1}} (\Omega)} + \| g \| _ {H ^ {r _ {2}} (\Gamma)}\right), \tag {5.4.5}$$

式中 $C$ 为仅依赖于 $r_1, r_2$ 而与 $f \in H^{r_1}(\Omega)$ 和 $g \in H^{r_2}(\Gamma)$ 无关的正常数.

现在我们考虑 Neuman 边值问题

$$
\left\{ \begin{array}{l} \Delta y = f \in H ^ {r _ {1}} (\Omega). \\ \left. \frac {\partial y}{\partial \nu} \right| _ {\Gamma} = g \in H ^ {r _ {2}} (\Gamma). \end{array} \right. \tag {5.4.6}
$$

注意在目前情形下

$$\int_ {\Omega} \triangle y \mathrm{d} x = \int_ {\Omega} f \mathrm{d} x = \int_ {\Gamma} \frac {\partial y}{\partial \nu} \mathrm{d} \sigma = \int_ {\Gamma} g \mathrm{d} \sigma .$$

但对于任意的 $f \in H^{r_1}(\Omega)$ 和 $g \in H^{r_2}(\Gamma)$ , 上式未必能满足, 从而问题 (5.4.6) 不一定有解. 为了问题 (5.4.6) 有解, 必须满足

$$\int_ {\Omega} f \mathrm{d} x = \int_ {\Gamma} g \mathrm{d} \sigma , \tag {5.4.7}$$

叫做相容性条件．实际上，我们有

定理 5.4.9 假定相容性条件式 (5.4.7) 满足，那么问题 (5.4.6) 至少有一个解 $y_{p} \in H^{s}(\Omega)$ ，其中 $s = \min\{r_{1} + 2, r_{2} + 3/2\}$ 。式 (5.4.5) 的通解可写成 $y = y_{p} + c$ ，其中 $c \in R$ 为任意常数。此外我们有估计

$$\inf _ {c \in \mathbb {R}} \| y _ {p} + c \| _ {H ^ {*} (\Omega)} \leqslant C \left(\| f \| _ {H ^ {r _ {1}} (\Omega)} + \| g \| _ {H ^ {r _ {2}} (\Gamma)}\right), \tag {5.4.8}$$

式中 $C$ 为仅依赖于 $r_1, r_2$ 而与 $f \in H^{r_1}(\Omega)$ 和 $g \in H^{r_2}(\Gamma)$ 无关的正常数.

类似地，对于 $a > 0$ ，考虑Neuman边值问题

$$
\left\{ \begin{array}{l} \triangle y - a y = f \in H ^ {r _ {1}} (\Omega), \\ \left. \frac {\partial y}{\partial \nu} \right| _ {\Gamma} = g \in H ^ {r _ {2}} (\Gamma). \end{array} \right. \tag {5.4.9}
$$

我们有

定理 5.4.10 Neuman 边值问题 (5.4.9) 有唯一解 $y \in H^{s}(\Omega)$ ，其中 $s = \min\{r_{1} + 2, r_{2} + 3/2\}$ ，满足估计

$$\| y \| _ {H ^ {s} (\Omega)} \leqslant C \left(\| f \| _ {H ^ {r _ {1}} (\Omega)} + \| g \| _ {H ^ {r _ {2}} (\Gamma)}\right), \tag {5.4.10}$$

式中 $C$ 为仅依赖于 $r_1, r_2$ , 而与 $f \in H^{r_1}(\Omega)$ 和 $g \in H^{r_2}(\Gamma)$ 无关的正常数.
