# 5.2.2 模糊逼近原理

由于模糊系统具有万能逼近特性 $^{[12]}$ ，以 $f(x|\theta)$ 来逼近 $f(x)$ 。针对模糊系统输入 $x_{1}$ 和 $x_{2}$ 分别设计5个模糊集，即取n=2,i=1,2, $p_{1}=p_{2}=5$ ，则共有 $p_{1}\times p_{2}=25$ 条模糊规则。

采用以下两步构造模糊系统 $\hat{f} (x\mid \theta)$

步骤1：对变量 $x_{i}(i = 1,2)$ ，定义 $p_i$ 个模糊集合 $A_{i}^{l_{i}}(l_{i} = 1,2,3,4,5)$ 。

步骤2:采用 $\prod_{i=1}^{n}p_{i}=p_{1}\times p_{2}=25$ 条模糊规则来构造模糊系统 $\hat{f}(x|\boldsymbol{\theta})$ ，则第j条模糊规则为：

$$\mathrm{R} ^ {(j)}: \text {IF} x _ {1} \text {is} A _ {1} ^ {l _ {1}} \text {and} x _ {2} \text {is} A _ {1} ^ {l _ {2}} \text {THEN} \hat {f} \text {is} B _ {1} ^ {l _ {1} l _ {2}} \tag {5.10}$$

式中， $l_{i}=1,2,3,4,5,i=1,2,j=1,2,\cdots,25,B^{l_{1}l_{2}}$ 为结论的模糊集。

则第 1 条、第 i 条和第 25 条模糊规则表示为

$$R ^ {(1)}: \text { IF } x _ {1} \text { is } A _ {1} ^ {1} \text { and } x _ {2} \text { is } A _ {2} ^ {1} \text { THEN } \hat {f} \text { is } B ^ {1}R ^ {(i)}: \text { IF } x _ {1} \text { is } A _ {1} ^ {i} \text { and } x _ {2} \text { is } A _ {2} ^ {i} \text { THEN } \hat {f} \text { is } B ^ {i}R ^ {(2 5)}: \text { IF } x _ {1} \text { is } A _ {1} ^ {5} \text { and } x _ {2} \text { is } A _ {1} ^ {5} \text { THEN } f \text { is } B ^ {2 5}$$

模糊推理过程采用如下 4 个步骤：

(1) 采用乘积推理机实现规则的前提推理, 推理结果为 $\prod_{i=1}^{2}\mu_{A_{i}^{l_{i}}}(x_{i})$ ;   
（2）采用单值模糊器求 $\overline{y}_{f}^{l_{1}l_{2}}$ ，即隶属函数最大值(1.0)所对应的横坐标值 $(x_{1},x_{2})$ 的函数值 $f(x_{1},x_{2})$ ;  
(3) 采用乘积推理机实现规则前提与规则结论的推理, 推理结果为 $\overline{y_{f}^{l_{1}l_{2}}}(\prod_{i=1}^{2}\mu_{A_{i}^{l_{i}}}(x_{i}))$ ; 对所

有的模糊规则进行并运算,则模糊系统的输出为 $\sum_{l_{1}=1}^{5}\sum_{l_{2}=1}^{5}\overline{y}_{f}^{l_{1}l_{2}}\left(\prod_{i=1}^{2}\mu_{A_{i}^{l_{i}}}(x_{i})\right)$ ;

(4) 采用平均解模糊器, 得到模糊系统的输出为

$$\hat {f} (x \mid q) = \frac {\sum_ {l _ {1} = 1} ^ {5} \sum_ {l _ {2} = 1} ^ {5} \overline {{y}} _ {f} ^ {l _ {1} l _ {2}} \left(\prod_ {i = 1} ^ {2} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})\right)}{\sum_ {l _ {1} = 1} ^ {5} \sum_ {l _ {2} = 1} ^ {5} \left(\prod_ {i = 1} ^ {2} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})\right)} \tag {5.11}$$

式中， $\mu_{A^{j}}(x_{i})$ 为 $x_{i}$ 的隶属函数。

令 $\bar{y}_{f}^{l_{1}l_{2}}$ 是自由参数，放在集合 $\theta\in R^{(25)}$ 中，则可引入模糊基向量 $\xi(x)^{[12]}$ ，式(5.11)变为

$$\hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta}) = \hat {\boldsymbol {\theta}} ^ {\mathrm{T}} \boldsymbol {\xi} (\boldsymbol {x}) \tag {5.12}$$

式中， $\pmb{\xi}(\pmb{x})$ 为 $\prod_{i=1}^{n} p_i = p_1 \times p_2 = 25$ 维模糊基向量，其第 $l_1 l_2$ 个元素为

$$\xi_ {l _ {1} l _ {2}} (\boldsymbol {x}) = \frac {\prod_ {i = 1} ^ {2} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})}{\sum_ {l _ {1} = 1} ^ {5} \sum_ {l _ {2} = 1} ^ {5} (\prod_ {i = 1} ^ {2} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i}))} \tag {5.13}$$
