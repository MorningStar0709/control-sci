$$
\begin{array}{l} K _ {i} \approx \frac {1 2 2 \times 1 0 ^ {- 3} - 4 2 \times 1 0 ^ {- 3}}{7 0 0 - 5 0 0} = \frac {8 0 \times 1 0 ^ {- 3} \mathrm{N}}{2 0 0 \mathrm{mA}} \\ \approx 4 0 0 \times 1 0 ^ {- 3} \mathrm{N/A} \\ \approx 0. 4 \mathrm{N/A} \\ \end{array}
$$

将这些值代入式(9.6)，得到平衡点邻域的线性近似方程为

$$f _ {\mathrm{m}} \approx 8 2 \times 1 0 ^ {- 3} + 1 4 \delta x + 0. 4 \delta i$$

将这个表达式代入式(9.5)并利用质量和重力的数值，对于线性化模型，我们得到

$$(8. 4 \times 1 0 ^ {- 3}) \ddot {x} = 8 2 \times 1 0 ^ {- 3} + 1 4 \delta x + 0. 4 \delta i - 8 2 \times 1 0 ^ {- 3}$$

因为 $x=x_{1}+\delta x$ ，所以 $\ddot{x}=\delta\dot{x}$ 。因此，关于 $\delta x$ 的方程为

$$(8. 4 \times 1 0 ^ {- 3}) \delta \ddot {x} = 1 4 \delta x + 0. 4 \delta i \tag {9.7}\delta \ddot {x} = 1 6 6 7 \delta x + 4 7. 6 \delta i$$

这就是我们所要得到的平衡点附近的线性化运动方程。逻辑状态矢量是 $x = [\delta x \quad \delta x]^{\mathrm{T}}$ ，由此可导出标准矩阵为

$$
\mathbf {A} = \left[ \begin{array}{l l} 0 & 1 \\ 1 6 6 7 & 0 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 4 7. 6 \end{array} \right]
$$

且控制量 $u=\delta i$ 。
