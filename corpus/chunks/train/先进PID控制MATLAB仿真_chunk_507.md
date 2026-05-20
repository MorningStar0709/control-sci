# 12.4.2 控制器设计

采用三种基于反馈的迭代学习控制律：

(1) 闭环 D 型

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \boldsymbol {K} _ {\mathrm{d}} (\dot {\boldsymbol {q}} _ {\mathrm{d}} (t) - \dot {\boldsymbol {q}} _ {k + 1} (t)) \tag {12.9}$$

(2) 闭环 PD 型

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \boldsymbol {K} _ {\mathrm{p}} (\boldsymbol {q} _ {\mathrm{d}} (t) - \boldsymbol {q} _ {k + 1} (t)) + \boldsymbol {K} _ {\mathrm{d}} (\dot {\boldsymbol {q}} _ {\mathrm{d}} (t) - \dot {\boldsymbol {q}} _ {k + 1} (t)) \tag {12.10}$$

(3) 指数变增益 D 型

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \boldsymbol {K} _ {\mathrm{p}} (\boldsymbol {q} _ {\mathrm{d}} (t) - \boldsymbol {q} _ {k + 1} (t)) + \boldsymbol {K} _ {\mathrm{d}} (\dot {\boldsymbol {q}} _ {\mathrm{d}} (t) - \dot {\boldsymbol {q}} _ {k + 1} (t)) \tag {12.11}$$

上述控制算法的收敛性分析可参见相关文献[1～4]。

![](image/a8faa5fd61d731ccbae686af05b26b4748bfbd283d0b28f129243ac7b689699b.jpg)
