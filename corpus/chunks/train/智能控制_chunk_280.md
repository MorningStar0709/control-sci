# 1. 基本的模糊系统

以 $\hat{f}(\boldsymbol{x} \mid \boldsymbol{\theta}_{f})$ 来逼近 $f(\boldsymbol{x})$ 为例，可用以下两步构造模糊系统 $\hat{f}(\boldsymbol{x} \mid \boldsymbol{\theta}_{f})^{[12]}$ 。

步骤 1: 对变量 $x_{i}(i=1,2,\cdots,n)$ ，定义 $p_{i}$ 个模糊集合 $A_{i}^{l_{i}}(l_{i}=1,2,\cdots,p_{i})$ 。

步骤2:采用以下 $\prod_{i=1}^{n}p_{i}$ 条模糊规则来构造模糊系统 $\hat{f}(x\mid\boldsymbol{\theta}_{f})$ :

$$R ^ {(j)}: \text {IF} x _ {1} \text {is} A _ {1} ^ {l _ {1}} \quad \text {and} \dots \text {and} x _ {n} \text {is} A _ {n} ^ {l _ {n}} \quad \text {THEN} \hat {f} \text {is} E ^ {l _ {1} \dots l _ {n}} \tag {5.22}$$

式中， $l_{i}=1,2,\cdots,p_{i};i=1,2,\cdots,n$ 。

设模糊集 $E^{l_{1}\cdots l_{n}}$ 的中心值为 $\bar{y}^{l_{1}\cdots l_{n}}$ ，采用乘积推理机、单值模糊器和中心平均解模糊器，则模糊系统的输出为

$$\widehat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) = \frac {\sum_ {l _ {1} = 1} ^ {p _ {1}} \cdots \sum_ {l _ {n} = 1} ^ {p _ {n}} \overline {{y}} _ {f} ^ {l _ {1} \cdots l _ {n}} \left(\prod_ {i = 1} ^ {n} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})\right)}{\sum_ {l _ {1} = 1} ^ {p _ {1}} \cdots \sum_ {l _ {n} = 1} ^ {p _ {n}} \left(\prod_ {i = 1} ^ {n} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})\right)} \tag {5.23}$$

式中， $\mu_{A_{i}^{l_{i}}}(x_{i})$ 为 $x_{i}$ 的隶属函数，其中分子表示规则前提之间、规则前提与结论之间的逻辑“与”运算及规则之间的逻辑“或”运算。

令 $\overline{y_{f}^{l_{1}\cdots l_{n}}}$ 为自由参数，放在集合 $\theta_{f}\in R^{\prod_{i=1}^{n}p_{i}}$ 中。引入向量 $\xi(x)$ ，式(5.23)变为

$$\widehat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) = \boldsymbol {\theta} _ {f} ^ {\mathrm{T}} \boldsymbol {\xi} (\boldsymbol {x}) \tag {5.24}$$

式中， $\xi(x)$ 为 $\prod_{i=1}^{n} p_{i}$ 维向量，其第 $l_{1}, \cdots, l_{n}$ 个元素为

$$\xi_ {l _ {1} \dots l _ {n}} (\boldsymbol {x}) = \frac {\prod_ {i = 1} ^ {n} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})}{\sum_ {l _ {1} = 1} ^ {p _ {1}} \cdots \sum_ {l _ {n} = 1} ^ {p _ {n}} \left(\prod_ {i = 1} ^ {n} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})\right)} \tag {5.25}$$

同理,可构造模糊系统 $g(x \mid \theta_{g})$ 逼近 $g(x)$ 。
