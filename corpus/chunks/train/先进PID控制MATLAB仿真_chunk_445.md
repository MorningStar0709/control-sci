# 2. 变异操作

从群体中随机选择3个个体 $x_{p1}$ 、 $x_{p2}$ 和 $x_{p3}$ ，且 $i\neq p_{1}\neq p_{2}\neq p_{3}$ ，则基本的变异操作为

$$h _ {i j} (t + 1) = x _ {\mathrm{plj}} (t) + F \left(x _ {\mathrm{p2j}} (t) - x _ {\mathrm{p3j}} (t)\right) \tag {10.2}$$

如果无局部优化问题，变异操作可写为

$$h _ {i j} (t + 1) = x _ {\mathrm{bj}} (t) + F \left(x _ {\mathrm{p2j}} (t) - x _ {\mathrm{p3j}} (t)\right) \tag {10.3}$$

式中， $x_{\mathrm{p2j}}(t)-x_{\mathrm{p3j}}(t)$ 为差异化向量，此差分操作是差分进化算法的关键；F 为缩放因子； $p_{1}$ 、 $p_{2}$ 、 $p_{3}$ 为随机整数，表示个体在种群中的序号； $x_{\mathrm{bj}}(t)$ 为当前代中种群中最好的个体。由于式（10.3）借鉴了当前种群中最好的个体信息，可加快收敛速度。
