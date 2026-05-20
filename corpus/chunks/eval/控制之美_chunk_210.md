# 10.4.4 观测器与控制器的结合

回到本章开始时提出的指尖平衡系统,此时增加一个限制条件,即连杆小球的角速度 $\frac{\mathrm{d}\phi(t)}{\mathrm{d}t}$ 不可测量。

沿用式(10.3.1)，即

$$
\frac {\mathrm{d} z (t)}{\mathrm{d} t} = A z (t) + B u (t), \quad \text {其中}, A = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right], B = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \tag {10.4.16a}
$$

$$
\mathbf {y} (t) = \mathbf {C} \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] + \mathbf {D u} (t), \quad \text {其中}, \mathbf {C} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right], \mathbf {D} = [ \mathbf {0} ] \tag {10.4.16b}
$$

控制目标和10.3.1节相同,设计控制器使得系统状态从初始值回到平衡点 $z_{f}(t)=[0,0]^{T}$ ，在10.3.1节中已经找到了这样的控制器，即 $u(t)=-Kz(t)$ 。但是，这一次无法直接使用它，因为 $z_{2}(t)=\frac{\mathrm{d}\phi(t)}{\mathrm{d}t}$ 不可测量。

因此,需要设计观测器来估计系统状态,之后再使用估计值 $\hat{z}(t)$ 来设计控制器。根据10.4.2节,观测误差 $\tilde{z}(t)=z(t)-\hat{z}(t)$ 的动态方程为

$$
\frac {\mathrm{d} \tilde {z} (t)}{\mathrm{d} t} = (A - L C) \tilde {z} (t) \tag {10.4.17}
$$

此时，令系统输入

$$
\pmb {u} (t) = - \pmb {K} \hat {\pmb {z}} (t) \tag {10.4.18}
$$

即使用估计值 $\hat{z}(t)$ 作为反馈信号进行控制器设计。将式(10.4.18)代入式(10.4.16a)，得到

$$
\begin{array}{l} \frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) - \boldsymbol {B} \boldsymbol {K} \hat {\boldsymbol {z}} (t) = \boldsymbol {A} \boldsymbol {z} (t) - \boldsymbol {B} \boldsymbol {K} (\boldsymbol {z} (t) - \bar {\boldsymbol {z}} (t)) \\ = (\mathbf {A} - \mathbf {B K}) \mathbf {z} (t) + \mathbf {B K} \tilde {\mathbf {z}} (t) \tag {10.4.19} \\ \end{array}
$$

将式(10.4.17)和式(10.4.19)结合起来得到状态空间方程增广矩阵,即

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{c} \tilde {z} (t) \\ z (t) \end{array} \right] = \left[ \begin{array}{c c} (A - L C) & 0 \\ B K & (A - B K) \end{array} \right] \left[ \begin{array}{c} \tilde {z} (t) \\ z (t) \end{array} \right] \tag {10.4.20}
$$
