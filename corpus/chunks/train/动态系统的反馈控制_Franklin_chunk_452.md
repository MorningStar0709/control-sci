# 7.7.2 降阶估计器

在 7.7.1 节中介绍了估计器的设计方法，用某些状态矢量的测量值重构整个状态矢量。如果传感器没有噪声干扰，那么全阶估计器就会包含冗余设计，对于估计可直接测量的状态矢量的必要性产生质疑。可以用那些能够直接且精确测量的状态矢量来降低估计器的复杂度吗？答案是肯定的。然而，如果测量结果有严重的噪声干扰，那么最好使用全阶估计器，因为全阶估计器除了对那些不可测的状态进行估计外，还可以对测量结果进行滤波。

降阶估计器通过测量输出数(此处为1)来降低估计器的阶数。为了推导这种降阶估计器，先假设将第一个状态作为输出，例如 $y=x_{a}$ 。如果这样不行，就需要进行预处理。变换为估计器的形式是可行的，但是工作量太大；可以对C进行任意非奇异变换作为第一行。现将状态矢量分为两部分：可直接测得的状态矢量 $x_{a}$ ，以及余下的需要估计的那部分状态矢量 $x_{b}$ 。若将系统矩阵相应的分块，则系统的完整描述为

$$
\left[ \begin{array}{l} \dot {x} _ {\mathrm{a}} \\ \dot {x} _ {\mathrm{b}} \end{array} \right] = \left[ \begin{array}{l l} A _ {\mathrm{aa}} & A _ {\mathrm{ab}} \\ A _ {b a} & A _ {\mathrm{bb}} \end{array} \right] \left[ \begin{array}{l} x _ {\mathrm{a}} \\ x _ {\mathrm{b}} \end{array} \right] + \left[ \begin{array}{l} B _ {\mathrm{a}} \\ B _ {\mathrm{b}} \end{array} \right] u \tag {7.147a}

y = \left[ \begin{array}{l l} 1 & \mathbf {0} \end{array} \right] \left[ \begin{array}{l} x _ {\mathrm{a}} \\ x _ {\mathrm{b}} \end{array} \right] \tag {7.147b}
$$

不可测状态矢量的动态方程为

$$\dot {x} _ {\mathrm{b}} = A _ {\mathrm{bb}} x _ {\mathrm{b}} + \underbrace {A _ {\mathrm{ba}} x _ {\mathrm{a}} + B _ {\mathrm{b}} u} _ {\text {已知输入}} \tag {7.148}$$

其中，最右边的两项为已知项，并且可以看作是进入 $x_{b}$ 动态的输入。因为 $x_{a}=y$ ，所以被测动态由如下标量方程给出

$$\dot {x} _ {\mathrm{a}} = \dot {y} = A _ {\mathrm{aa}} y + A _ {\mathrm{ab}} x _ {\mathrm{b}} + B _ {\mathrm{a}} u \tag {7.149}$$

如果将式(7.149)的已知项移到方程的一侧，得

$$\dot {y} - \underbrace {A _ {\mathrm{aa}} y - B _ {\mathrm{a}} u} _ {\text {已知测量值}} = A _ {\mathrm{ab}} x _ {\mathrm{b}} \tag {7.150}$$

这样就得到了方程左边的已知量，即测量值，与方程右边的未知状态变量之间的关系式。因此，式(7.149)和式(7.150)对状态 $x_{b}$ 与原始方程[式(7.147b)]对状态x有相同的关系。根据这一原因，在原始的估计器方程中进行如下的替换可得到 $x_{b}$ 的一个（降阶）估计器：

$$x \leftarrow x _ {b} \tag {7.151a}\boldsymbol {A} \leftarrow \boldsymbol {A} _ {\mathrm{bb}} \tag {7.151b}\boldsymbol {B} u \leftarrow \boldsymbol {A} _ {\mathrm{ba}} y + \boldsymbol {B} _ {\mathrm{b}} u \tag {7.151c}y \leftarrow \dot {y} - A _ {\mathrm{aa}} y - B _ {\mathrm{a}} u \tag {7.151d}\boldsymbol {C} \leftarrow \boldsymbol {A} _ {\mathrm{ab}} \tag {7.151e}$$

所以，将式(7.151)代入到全阶估计器式(7.130)即可得到降阶估计器方程：
