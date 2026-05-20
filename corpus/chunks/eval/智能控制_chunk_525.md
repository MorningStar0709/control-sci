# (1) 生成初始群体

在 n 维空间里随机产生满足约束条件的 M 个个体, 实施措施如下:

$$x _ {i j} (0) = \operatorname{rand} _ {i j} (0, 1) \left(x _ {i j} ^ {U} - x _ {i j} ^ {L}\right) + x _ {i j} ^ {L} \tag {10.13}$$

式中， $x_{ij}^{U}$ 和 $x_{ij}^{L}$ 分别是第 $j$ 个染色体的上界和下界， $\mathrm{rand}_{ij}(0,1)$ 是[0,1]之间的随机小数。
