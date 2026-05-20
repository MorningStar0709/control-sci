7.28 用一根弹簧连接的两个摆，受两个大小相等方向相反的力 u 控制，这两个力分别加到两个摆锤上，如图 7.88 所示。运动方程为

$$m l ^ {2} \ddot {\theta} _ {1} = - k a ^ {2} \left(\theta_ {1} - \theta_ {2}\right) - m g l \theta_ {1} - l u,m l ^ {2} \ddot {\theta} _ {2} = - k a ^ {2} (\theta_ {2} - \theta_ {1}) - m g l \theta_ {2} + l u$$

![](image/e25b954a1c87d05463f4ff7316b9e6674dffaf978ffa59dbd5cf9119f82e326c.jpg)

<details>
<summary>text_image</summary>

k
θ₁
u
m
a
l
θ₂
u
m
</details>

图 7.88 习题 7.28 的耦合摆

(a) 证明该系统是不可控的。能否说出可控状态与不可控状态的物理意义？  
(b) 能否找出一种方法将该系统变为可控系统？

7.29 给出某种应用的状态空间模型，状态描述矩阵为

$$
\boldsymbol {A} = \left[ \begin{array}{c c c c c} 0. 1 7 4 & 0 & 0 & 0 & 0 \\ 0. 1 5 7 & 0. 6 5 4 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{c} - 0. 2 0 7 \\ - 0. 0 0 5 \\ 0 \\ 0 \\ 0 \end{array} \right]

\boldsymbol {C} = \left[ \begin{array}{l l l l l} 1 & 0 & 0 & 0 & 0 \end{array} \right]
$$

(a) 画出一种实现的框图，其每个状态变量对应一个积分器。  
(b) 某学生计算出 $\det C = 2.3 \times 10^{-7}$ ，便说

系统是不可控的。该学生是对是错？为什么？

(c) 这种实现是可观测的吗？

7.30 阶梯算法（范·多伦（Van Dooren）等人，1978年）：任何实现 $(A, B, C)$ 都可通过正交相似变换转化为 $(\overline{A}, \overline{B}, \overline{C})$ ，其中， $\overline{A}$ 为上海森伯格（Hessenberg）矩阵（在主对角线上方有一非零斜行）给出如下：

$$
\begin{array}{l} \overline {{{A}}} = T ^ {\mathrm{T}} A T = \left[ \begin{array}{c c c c} * & \alpha_ {1} & 0 & 0 \\ * & * & \ddots & 0 \\ * & * & \ddots & \alpha_ {n - 1} \\ * & * & \dots & * \end{array} \right], \\ \overline {{{\boldsymbol {B}}}} = \boldsymbol {T} ^ {\mathrm{T}} \boldsymbol {B} = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ g _ {1} \end{array} \right] \\ \end{array}
$$

其中： $g_{1}\neq0$ ;

$$
\overline {{C}} = C T = \left[ \begin{array}{l l l l} \bar {c} _ {1} & \bar {c} _ {2} & \dots & \bar {c} _ {n} \end{array} \right], T ^ {- 1} = T ^ {\mathrm{T}}
$$

正交变换相当于将被变换的矢量(用列矩阵表示)进行旋转而不改变矢量的长度。

(a) 证明：如果对某 i 有 $\alpha_{i}=0$ 且 $\alpha_{i+1},\cdots,\alpha_{n-1}\neq0$ ，则经过该变换就可找出系统的可控模态与不可控模态。  
(b) 如何用这种方法找出 $(A, B, C)$ 的可观测模态和不可观测模态？  
(c) 这种确定可控模态和不可控模态的方法与将系统变换成其他形式有什么优势？  
(d) 如何用这种方法确定可控和不可控子空间的基？(同习题 7.44)

可用这种算法来为极点配置设计一种数值上稳定的算法[见米尼米斯(Minimis)和拜格(Paige)，1982年]。这种算法的名称来源于多输入模型，在这种模型中 $\alpha_{i}$ 是使 $\overline{A}$ 像阶梯形的矩阵块。参考Matlab中ctrbf、obsvf命令。
