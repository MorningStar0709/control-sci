# 5.5 机器人关节数学模型

在许多生产场合,利用机器人取代人操作,不仅提高了生产效率,而且还能完成一些人所不能完成的高强度、危险作业。机械臂是工业机器人中常见的一类被控对象。

一个典型的多关节机器人如图 5-22 所示。

考虑一个 n 关节机器人, 其动态性能可由二阶非线性微分方程描述

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) + \boldsymbol {F} (\dot {\boldsymbol {q}}) + \tau_ {\mathrm{d}} = \tau \tag {5.66}$$

式中， $q \in R^{n}$ 为关节角位移量， $D(q) \in R^{n \times n}$ 为机器人的惯性力矩阵， $C(q, \dot{q}) \in R^{n}$ 表示离心力和哥氏力， $G(q) \in R^{n}$ 为重力项， $F(\dot{q}) \in R^{n}$ 表示摩擦力矩， $\tau \in R^{n}$ 为控制力矩， $\tau_{d} \in R^{n}$ 为外加扰动。

机械手动力学模型的特点：

① 动力学模型包含的项数多,随着机器人关节数的增加,方程中包含的项数也增加;   
②高度非线性,方程的每一项都含有正弦、余弦等非线性因素;   
③高度耦合；  
④ 模型不确定性和时变性。当机器人搬运物体时，由于所持物件不同，负载会发生变化，另外，关节的摩擦力矩也会随时间变化。

机械手动力学模型有以下几个特性：

① $D(q)$ 为一个正定对称矩阵，且是有界的，即存在已知正常数 $m_{1}$ 和 $m_{2}$ ，使得 $m_{1}I \leqslant D(q) \leqslant m_{2}I$ ;  
② $C(q,\dot{q})$ 有界，即存在已知 $c_{b}(q)$ ，使得 $|C(q,\dot{q})| \leqslant c_{b}(q)\|\dot{q}\|$ 成立；  
③ 矩阵 $\dot{D}-2C$ 为斜对称矩阵，即满足 $x^{\mathrm{T}}(\dot{D}-2C)x=0,x$ 为向量；  
④ 未知扰动满足 $\| \tau_{\mathrm{d}} \| \leqslant \tau_{M}, \tau_{M}$ 为一个已知正常数。

一个典型的双关节刚性机械手示意图如图 5-23 所示。

![](image/e8c07b670a43892db400afdd8dd02cc87f5d1ebb4c0f542dd8fad87416cf0aef.jpg)

<details>
<summary>natural_image</summary>

Mechanical robotic arm with articulated joints, shown in grayscale (no text or symbols visible)
</details>

图 5-22 一个 8 关节机器人

![](image/43f1d2c6cbbb05e700f456c978e5f6c667515175e6faa103ee340be805505d62.jpg)

<details>
<summary>text_image</summary>

m₂
l₂
q₂
m₁
l₁
q₁
g
</details>

图 5-23 双关节刚性机械手示意图
