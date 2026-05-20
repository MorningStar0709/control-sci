# 例2.4 柔性：磁盘驱动的柔性读/写装置

在图 2.11 中，假设读磁头和驱动机之间存在一定柔性，推导施加在基座上的力矩与读磁头之间关系的运动方程。

解答。本例的动态模型原理图如图 2.12 所示。这个模型与图 2.5 所示的谐振系统动态类似，因此运动方程的形式也与式(2.10)和式(2.11)相似。图 2.13 所示的受力图给出了作用在每一部分上的力矩。这里讨论的力矩实质上与例 2.2 是相同的，只不过在例 2.2 中，弹簧和阻尼器产生力的作用，而不是作用在每个惯性体上的力矩。

33

![](image/7fe1c45e1f90bff5c51f234dd044e2b5f4b2dbe27801aaed450f717298954ad0.jpg)

<details>
<summary>natural_image</summary>

Close-up of a mechanical device with gears and housing (no visible text or symbols)
</details>

图 2.11 磁盘读/写装置  
(图片来源：作者)

![](image/25c51cb2c14678ce3e5d5f4149febe1ca8229213ab902899a73715dff3c59cce.jpg)

<details>
<summary>text_image</summary>

磁盘
读磁头以及
磁道传感器
θ₂
磁头惯量
I₂
柔性轴
k,b
θ₁
电机惯量
I₁
Mc+MD
</details>

图 2.12 磁盘读/写磁头简图

![](image/00d77ca8adda768f1f6cbca4bc7d922180cf45581cdc6df27ab581b95629352b.jpg)

<details>
<summary>text_image</summary>

M_c + M_D
\ddot{\theta}_1
\theta_1
k(\theta_1 - \theta_2)
I_1
b(\dot{\theta}_1 - \dot{\theta}_2)
</details>

![](image/2d24b5a5d15d490204642381de9463a22ec306086881285bdcdec47a72f1021a.jpg)

<details>
<summary>text_image</summary>

k(\theta₁-θ₂)
b(\dot{\theta}_1-\dot{\theta}_2)
I₂
θ₂
θ̇₂
</details>

图 2.13 磁盘读/写磁头的受力图

根据式 $(2.14)$ 力矩求和，联立加速度，整理结果为

$$I _ {1} \ddot {\theta} _ {1} + b (\dot {\theta} _ {1} - \dot {\theta} _ {2}) + k (\theta_ {1} - \theta_ {2}) = M _ {\mathrm{c}} + M _ {\mathrm{D}} \tag {2.17}I _ {2} \ddot {\theta} _ {2} + b (\dot {\theta} _ {2} - \dot {\theta} _ {1}) + k (\theta_ {2} - \theta_ {1}) = 0 \tag {2.18}$$

为简单起见，忽略扰动转矩 $M_{D}$ 和阻尼 b，得到读磁头的运动相对于施加的力矩 $M_{c}$ 的传递函数为

$$\frac {\Theta_ {2} (s)}{M _ {\mathrm{c}} (s)} = \frac {k}{I _ {1} I _ {2} s ^ {2} \left(s ^ {2} + \frac {k}{I _ {1}} + \frac {k}{I _ {2}}\right)} \tag {2.19}$$

也可能测量在转矩作用下惯性体的运动，此时传递函数同样简化为

$$\frac {\Theta_ {1} (s)}{M _ {\mathrm{c}} (s)} = \frac {I _ {2} s ^ {2} + k}{I _ {1} I _ {2} s ^ {2} \left(s ^ {2} + \frac {k}{I _ {1}} + \frac {k}{I _ {2}}\right)} \tag {2.20}$$

这两种情况比较典型，在柔性体中传感器和执行机构可能在同一位置，也可能不在同一位置。式(2.19)表示的传感器和执行机构间的情形是单体(noncollocated)的情况，而方程(2.20)描述的是合体(collocated)的情况。在第5章中，就会发现系统传感器和执行机构之间存在柔性(单体情况)比它们之间是刚性(合体情况)时要难控制得多。

另一种特殊情形，旋转体的某一点相对于惯性参考系是固定的，例如下面要列举的摆，同样也可以应用式(2.14)，M为相对于固定点的所有力矩之和，I为折合到固定点的转动惯量。
