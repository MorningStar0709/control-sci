# 1. 生成初始群体

在n维空间里随机产生满足约束条件的M个个体，实施措施如下：

$$x _ {i j} (0) = \operatorname{rand} _ {i j} (0, 1) \left(x _ {i j} ^ {\mathrm{U}} - x _ {i j} ^ {\mathrm{L}}\right) + x _ {i j} ^ {\mathrm{L}} \tag {10.1}$$

式中， $x_{ij}^{U}$ 和 $x_{ij}^{L}$ 分别为第 j 个染色体的上界和下界； $\operatorname{rand}_{ij}(0,1)$ 为 [0,1] 之间的随机小数。
