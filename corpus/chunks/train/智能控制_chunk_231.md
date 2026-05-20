# 4.7.1 T-S 模糊系统的设计

针对n个状态变量m个控制输入的连续非线性系统,其T-S模糊模型可描述为以下r条模糊规则。

规则 i: If $x_{1}(t)$ is $M_{1}^{i}$ and $x_{2}(t)$ is $M_{2}^{i}$ and $\cdots x_{n}(t)$ is $M_{n}^{i}$

$$\text { Then } \dot {\boldsymbol {x}} (t) = \boldsymbol {A} _ {i} \boldsymbol {x} (t) + \boldsymbol {B} _ {i} \boldsymbol {u} (t), i = 1, 2, \dots , r \tag {4.12}$$

式中， $x_{j}$ 为系统的第 j 个状态变量， $M_{j}^{i}$ 为第 i 条规则的第 j 个隶属函数， $\boldsymbol{x}(t)$ 为状态向量， $\boldsymbol{x}(t)=\left[x_{1}(t)\cdots x_{n}(t)\right]^{\mathrm{T}}\in R^{n},\boldsymbol{u}(t)$ 为控制输入向量， $\boldsymbol{u}(t)=\left[u_{1}(t)\cdots u_{m}(t)\right]^{\mathrm{T}}\in\boldsymbol{R}^{m},\boldsymbol{A}_{i}\in\boldsymbol{R}^{n\times n},\boldsymbol{B}_{i}\in\boldsymbol{R}^{n\times m}$ 。

根据模糊系统的反模糊化定义,由模糊规则式(4.12)构成的模糊模型总的输出为

$$\dot {\pmb {x}} (t) = \frac {\sum_ {i = 1} ^ {r} w _ {i} [ A _ {i} x (t) + B _ {i} u (t) ]}{\sum_ {i = 1} ^ {r} w _ {i}} \tag {4.13}$$

式中， $w_{i}$ 为规则 i 的隶属函数， $w_{i}=\prod_{k=1}^{n}M_{k}^{i}(x_{k}(t))$ 。以 4 条规则为例，规则前提为 $x_{1}$ ，则 k=1，i=1,2,3,4，则 $w_{1}=M_{1}^{1}(x_{1})$ ， $w_{2}=M_{1}^{2}(x_{1})$ ， $w_{3}=M_{1}^{3}(x_{1})$ ， $w_{4}=M_{1}^{4}(x_{1})$ 。

针对每条 T-S 模糊规则,采用状态反馈方法,可设计 r 条模糊控制规则。

控制规则 i: If $x_{1}(t)$ is $M_{1}^{i}$ and $x_{2}(t)$ is $M_{2}^{i}$ and $\cdots x_{n}(t)$ is $M_{n}^{i}$

$$\text { Then } u (t) = \mathbf {K} _ {i} \mathbf {x} (t), i = 1, 2, \dots , r \tag {4.14}$$

并行分布补偿(Parallel Distributed Compensation, PDC) 方法是一种基于模型的模糊控制器设计方法[11], 适用于解决基于 T-S 模糊建模的非线性系统控制问题。

根据模糊系统的反模糊化定义,针对连续非线性系统,根据模糊控制规则式(4.14),采用PDC方法设计T-S模糊控制器为

$$\pmb {u} (t) = \frac {\sum_ {j = 1} ^ {r} w _ {j} K _ {j} \pmb {x} (t)}{\sum_ {j = 1} ^ {r} w _ {j}} \tag {4.15}$$
