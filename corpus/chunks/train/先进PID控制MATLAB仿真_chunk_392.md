# 1. 基本的模糊系统

以 $\hat{f}(x|\theta_{f})$ 来逼近 $f(x)$ 为例，可用以下两步构造模糊系统 $\hat{f}(x|\theta_{f})^{[1]}$ 。

步骤 1：对变量 $x_{i}(i=1,2)$ ，定义 $p_{i}$ 个模糊集合 $A_{i}^{l_{i}}(l_{i}=1,2,\cdots,p_{i})$ 。

步骤 2：采用以下 $\prod_{i=1}^{2}p_{i}$ 条模糊规则来构造模糊系统 $\hat{f}(x|\theta_{f})$ :

$$R ^ {(j)}: \text { IF } x _ {1} \text { is } A _ {1} ^ {l _ {1}} \text { AND } x _ {2} \text { is } A _ {1} ^ {l _ {2}} \text { THEN } \hat {f} \text { is } E ^ {l _ {1} l _ {2}} \tag {8.8}$$

其中 $l_{i}=1,2,\quad i=1,2$ 。

采用乘积推理机、单值模糊器和中心平均解模糊器，则模糊系统的输出为

$$\hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) = \frac {\sum_ {l _ {1} = 1} ^ {p _ {1}} \sum_ {l _ {2} = 1} ^ {p _ {2}} \bar {y} _ {f} ^ {l _ {1} l _ {2}} \left(\prod_ {i = 1} ^ {2} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})\right)}{\sum_ {l _ {1} = 1} ^ {p _ {1}} \sum_ {l _ {2} = 1} ^ {p _ {2}} \left(\prod_ {i = 1} ^ {2} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})\right)} \tag {8.9}$$

式中， $\mu_{A_{i}^{j}}(x_{i})$ 为 $x_{i}$ 的隶属函数。

令 $\overline{y}_{f}^{l_{1}l_{2}}$ 是自由参数，放在集合 $\theta_{f}\in R^{\prod_{i=1}^{2}p_{i}}$ 中。引入列向量 $\xi(x)$ ，式（8.9）变为

$$\hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) = \boldsymbol {\theta} _ {f} ^ {\mathrm{T}} \boldsymbol {\xi} (\boldsymbol {x}) \tag {8.10}$$

式中， $\xi(x)$ 为 $\prod_{i=1}^{2} p_{i}$ 维列向量，其第 $l_{1}, l_{2}$ 个元素为

$$\xi_ {l _ {1} l _ {2}} (\boldsymbol {x}) = \frac {\prod_ {i = 1} ^ {2} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})}{\sum_ {l _ {1} = 1} ^ {p _ {1}} \sum_ {l _ {2} = 1} ^ {p _ {2}} \left(\prod_ {i = 1} ^ {2} \mu_ {A _ {i} ^ {l _ {i}}} (x _ {i})\right)} \tag {8.11}$$
