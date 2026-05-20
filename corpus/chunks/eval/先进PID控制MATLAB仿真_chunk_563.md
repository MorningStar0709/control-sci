# 14.3.1 问题的提出

工业机械手可以完成的任务可以分为两类：一类是非接触性作业，即机械手在自由空间中搬运、操作目标物等任务，对于这一类作业，仅仅运用位置控制便可以胜任；另一类是接触性作业，如抛光、打磨等，对于这一类任务，单纯的位置控制已经不能胜任了，因为在这类任务中对接触力的大小是有要求的，并且机械手末端微小的位置偏差就可能导致巨大的接触力，会对机械手和目标物造成损害，所以必须添加接触力的控制功能来提高机械手的有效作业精度。

Hongan 提出机械手的阻抗控制方法 $^{[7,8]}$ ，机械手阻抗控制就是间接的控制机械手和环境间的作用力，其设计思想是建立机械手末端作用力与其位置之间的动态关系，通过控制机械手位移而达到控制末端作用力的目的，保证了机械手在受约束的方向保持期望的接触力。自阻抗控制概念被提出以来，涌现出很多不同的具体应用方法。由于工业机械手都匹配有高性能的位置控制器，所以基于位置的阻抗控制策略得到了广泛的应用。

带有阻力约束的双关节机械手示意图如图14-8所示[9]，机械手末端接触到障碍物后，沿着垂直 $x_{1}$ 的方向滑下，然后继续跟踪指令 $\pmb{x}_{\mathrm{d}}$ 。阻抗控制就是在阻力约束下的机械手末端位置控制。

设 x 为机械手末端位置向量，关节角度 q 与机械手末端位置向量 x 关系为

$$\boldsymbol {x} = h (\boldsymbol {q}) \tag {14.13a}$$

且

$$\dot {\boldsymbol {x}} = \boldsymbol {J} (\boldsymbol {q}) \dot {\boldsymbol {q}} \tag {14.13b}$$

式中， $J(q)$ 为机械手末端的Jacobian信息。

![](image/8943e45601a0fdd30b5ecbcfad728a5db3e378304cc940fe28d20c85f401e20a.jpg)

<details>
<summary>text_image</summary>

x₂
q₂
l₂
x_c
l₁
机械手
q₁
x₁
障碍
</details>

图 14-8 带有阻力约束的双关节机械手

机械手末端的接触阻力为 $F_{\mathrm{e}}$ ， $F_{\mathrm{e}}$ 与位置误差 $x_{\mathrm{c}} - x$ 有关，动力学描述为[9]

$$\boldsymbol {M} _ {\mathrm{m}} \left(\ddot {\boldsymbol {x}} _ {\mathrm{c}} - \ddot {\boldsymbol {x}}\right) + \boldsymbol {B} _ {\mathrm{m}} \left(\dot {\boldsymbol {x}} _ {\mathrm{c}} - \dot {\boldsymbol {x}}\right) + \boldsymbol {K} _ {\mathrm{m}} \left(\boldsymbol {x} _ {\mathrm{c}} - \boldsymbol {x}\right) = \boldsymbol {F} _ {\mathrm{e}} \tag {14.14}$$

式中， $x_{c}$ 为接触位置的指令轨迹； $x(0)=x_{c}(0)$ ； $M_{m}$ 、 $B_{m}$ 和 $K_{m}$ 分别为质量、阻尼和刚度系数矩阵。

由于阻尼控制是在笛卡尔坐标系下实现，为了实现理想接触位置 $x_{c}$ 的轨迹跟踪，为此需要通过角度动力学方程求得笛卡尔坐标系下动力学方程。根据14.2节中工作空间中机械手末端轨迹控制问题的描述，式（14.10），带有阻力 $F_{e}$ 的笛卡尔坐标系下双关节动力学方程为

$$\boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {x}} + \boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {x}} + \boldsymbol {G} _ {x} (\boldsymbol {q}) + \boldsymbol {F} _ {\mathrm{e}} = \boldsymbol {F} _ {x} \tag {14.15}$$

式中， $D_{x}(q) = J^{-\mathrm{T}}(q)D(q)J^{-1}(q)$ ； $C_x(q,\dot{q}) = J^{-\mathrm{T}}(q)(C(q,\dot{q}) - D(q)J^{-1}(q)\dot{J}(q))J^{-1}(q)$ ； $G_{x}(q) = J^{-\mathrm{T}}(q)G(q)$ 。

![](image/f4fe62097e64af37006c96a40b12700f87ee1a6701fb45c5880a297d4853a8e4.jpg)
