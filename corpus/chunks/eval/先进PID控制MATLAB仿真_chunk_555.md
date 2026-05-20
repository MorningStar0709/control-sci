# 14.2.2 机械手在工作空间的建模

考虑一个刚性 n 关节机械手，其动态特性为

$$D (q) \ddot {q} + C (q, \dot {q}) \dot {q} + G (q) = \tau \tag {14.8}$$

式中， $q \in R^{n}$ 是表示关节变量的向量； $\tau \in R^{n}$ 是执行机构施加的关节扭矩向量； $D(q) \in R^{n \times n}$ 为对称正定惯性矩阵； $C(q, \dot{q}) \in R^{n \times n}$ 为哥氏力和离心力向量； $G(q) \in R^{n}$ 为重力向量。

为了实现末端位置的控制，需要将关节角度动力学方程转换为基于末端位置的动力学方程。

在静态平衡状态下，传递到机械手末端力的 $F_{x}$ 与关节扭矩 $\pmb{\tau}$ 之间存在线性映射关系，通过虚功原理可得[5]

$$\boldsymbol {F} _ {x} = \boldsymbol {J} ^ {- \mathrm{T}} (\boldsymbol {q}) \tau \tag {14.9}$$

由于 $\dot{x}=J\cdot\dot{q}$ ，则 $\dot{q}=J^{-1}\dot{x}$ ， $\ddot{x}=\dot{J}\dot{q}+J\ddot{q}=\dot{J}J^{-1}\dot{x}+J\ddot{q}$ ，从而

$$\ddot {q} = J ^ {- 1} \left(\ddot {x} - \dot {J} J ^ {- 1} \dot {x}\right)$$

将上式代入式（14.8），可得

$$D (q) J ^ {- 1} (\ddot {x} - \dot {J} J ^ {- 1} \dot {x}) + C (q, \dot {q}) J ^ {- 1} \dot {x} + G (q) = \tau$$

即 $D(q)J^{-1}\ddot{x}-D(q)J^{-1}\dot{J}J^{-1}\dot{x}+C(q,\dot{q})J^{-1}\dot{x}+G(q)=\tau$ ，整理得

$$D (q) J ^ {- 1} \ddot {x} + (C (q, \dot {q}) - D (q) J ^ {- 1} \dot {J}) J ^ {- 1} \dot {x} + G (q) = \tau$$

则

$$J ^ {- \mathrm{T}} (q) (D (q) J ^ {- 1} \ddot {x} + (C (q, \dot {q}) - D (q) J ^ {- 1} \dot {J}) J ^ {- 1} \dot {x} + G (q)) = J ^ {- \mathrm{T}} (q) \tau$$

从而

$$\boldsymbol {D} _ {x} (\boldsymbol {q}) \ddot {\boldsymbol {x}} + \boldsymbol {C} _ {x} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {x}} + \boldsymbol {G} _ {x} (\boldsymbol {q}) = \boldsymbol {F} _ {x} \tag {14.10}$$

式中， $D_{x}(q)=J^{-\mathrm{T}}(q)D(q)J^{-1}(q)$ ； $C_{x}(q,\dot{q})=J^{-\mathrm{T}}(q)\left(C(q,\dot{q})-D(q)J^{-1}(q)\dot{J}(q)\right)J^{-1}(q)$ ； $G_{x}(q)=J^{-\mathrm{T}}(q)G(q)$ 。

机械手动态方程具有下面特性 $^{[3,6]}$ :

特性 1：惯性矩阵 $D_{x}(q)$ 对称正定。

特性 2：矩阵 $\dot{D}_{x}(q)-2C_{x}(q,\dot{q})$ 是斜对称的。

![](image/0638aa445c3859b7051290ca2e39485645322741b438ccc03cf847694ace095a.jpg)
