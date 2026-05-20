# 5.4.2 控制器的设计

直接自适应模糊控制器为 $^{[12]}$

$$u = u _ {\mathrm{D}} (\boldsymbol {x} \mid \boldsymbol {\theta}) \tag {5.48}$$

式中， $u_{D}$ 是一个模糊系统， $\theta$ 是可调参数集合。

模糊系统 $u_{D}$ 可由以下两步来构造。

步骤 1: 对变量 $x_{i}(i=1,2,\cdots,n)$ ，定义 $m_{i}$ 个模糊集合 $A_{i}^{l_{i}}(l_{i}=1,2,\cdots,m_{i})$ 。

步骤2:用以下 $\prod_{i=1}^{n}m_{i}$ 条模糊规则来构造模糊系统 $u_{\mathrm{D}}(\boldsymbol{x}\mid\boldsymbol{\theta})$ ，即

如果 $x_{1}$ 是 $A_{1}^{l_{1}}$ 且 $\cdots$ 且 $x_{n}$ 是 $A_{n}^{l_{n}}$ ，则 $u_{D}$ 是 $S^{l_{1}\cdots l_{n}}$ (5.49)

式中， $l_{1}=1,2,\cdots,m_{i};i=1,2,\cdots,n$ 。

采用乘积推理机、单值模糊器和中心平均解模糊器来设计模糊控制器，即

$$u _ {\mathrm{D}} = (\boldsymbol {x} \mid \boldsymbol {\theta}) = \frac {\sum_ {l _ {1} = 1} ^ {m _ {1}} \cdots \sum_ {l _ {n} = 1} ^ {m _ {n}} \overline {{y}} _ {u} ^ {l _ {1} \cdots l _ {n}} \left(\prod_ {i = 1} ^ {n} \mu_ {A _ {i}} ^ {l _ {i}} (x _ {i})\right)}{\sum_ {l _ {1} = 1} ^ {m _ {1}} \cdots \sum_ {l _ {n} = 1} ^ {m _ {n}} \left(\prod_ {i = 1} ^ {n} \mu_ {A _ {i}} ^ {l _ {i}} (x _ {i})\right)} \tag {5.50}$$

令 $\overline{y_{u}^{l_{1}\cdots l_{n}}}$ 是自由参数,放在集合 $\theta\in R^{\prod_{i=1}^{n}m_{i}}$ 中,则模糊控制器为

$$u _ {\mathrm{D}} = (\boldsymbol {x} \mid \boldsymbol {\theta}) = \boldsymbol {\theta} ^ {\mathrm{T}} \boldsymbol {\xi} (\boldsymbol {x}) \tag {5.51}$$

式中， $\xi(x)$ 为 $\prod_{i=1}^{n} m_{i}$ 维向量，其第 $l_{1}, \cdots, l_{n}$ 个元素为

$$\xi_ {l _ {1} \dots l _ {n}} (\boldsymbol {x}) = \frac {\prod_ {i = 1} ^ {n} \mu_ {A _ {i}} ^ {l _ {i}} \left(x _ {i}\right)}{\sum_ {l _ {1} = 1} ^ {m _ {1}} \cdots \sum_ {l _ {n} = 1} ^ {m _ {n}} \left(\prod_ {i = 1} ^ {n} \mu_ {A _ {i}} ^ {l _ {i}} \left(x _ {i}\right)\right)} \tag {5.52}$$

模糊控制规则式(5.44)是通过设置其初始参数而被嵌入到模糊控制器中的。
