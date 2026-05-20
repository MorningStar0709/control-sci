# 8.3.1 基本原理

将跟踪误差和误差变化量作为模糊规则的输入，控制输入作为规则的输出，根据经验构

造模糊规则表，可实现无需模型信息的控制。

以误差和误差变化为前提，第 ij 条模糊控制规则的表达形式为

$$\text { Rule } \quad i j: \text { IF } e = \mu_ {i} \text { and } \Delta e = \mu_ {j} \text { THEN } u = u _ {i j} \tag {8.24}$$

采用乘积推理机，规则前部分的隶属函数为

$$f _ {i j} = \mu_ {i} (e) \cdot \mu_ {j} (\Delta e) \tag {8.25}$$

式中， $\mu_{i}(e)$ 和 $\mu_{j}(\Delta e)$ 分别为 e 和 $\Delta e$ 的隶属度。

采用重心方法进行反模糊化，得到模糊控制器：

$$u = \frac {\sum_ {i , j} f _ {i j} u _ {i j}}{\sum_ {i , j} f _ {i j}} \tag {8.26}$$

式中， $u_{ij}$ 的值由模糊规则表确定。

表 8-1 控制规则表

<table><tr><td rowspan="2" colspan="2"> $u_{ij}$ </td><td colspan="3"> $\Delta e$ </td></tr><tr><td>N</td><td>Z</td><td>P</td></tr><tr><td rowspan="3">e</td><td>N</td><td> $u_{11}$ </td><td> $u_{12}$ </td><td> $u_{13}$ </td></tr><tr><td>Z</td><td> $u_{21}$ </td><td> $u_{22}$ </td><td> $u_{23}$ </td></tr><tr><td>P</td><td> $u_{31}$ </td><td> $u_{32}$ </td><td> $u_{33}$ </td></tr></table>

模糊规则表中每条规则的输出 $u_{ij}$ 值可由模糊推理或根据经验确定。假设e和 $\Delta e$ 各有3个隶属函数，则共有9条规则，模糊规则表的形式见表8-1。

![](image/6495b91549d6e664d94b13b8cf232cf45c70cb4c9c63a4f59b8faf0408d121e0.jpg)
