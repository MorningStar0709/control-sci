$$\delta \dot {x} = A \delta x + B \delta u + (A M - M A _ {\mathrm{m}} + B N) z - M B _ {\mathrm{m}} \delta (t) \tag {7.232}\delta y = C \delta x + (C M - C _ {\mathrm{m}}) z \tag {7.233}$$

若选择矩阵 M 和 N 使得上述矩阵乘以式(7.232)和式(7.233)中的模型状态 z 消失，那么我们有如下两个矩阵方程 $^{①}$ ：

$$\boldsymbol {A} \boldsymbol {M} - \boldsymbol {M} \boldsymbol {A} _ {\mathrm{m}} + \boldsymbol {B} \boldsymbol {N} = 0 \tag {7.234}\boldsymbol {C M} = \boldsymbol {C} _ {\mathrm{m}} \tag {7.235}$$

式(7.234)称为西尔维斯特(Sylvester)方程。式(7.234)和式(7.235)中，有 $n_{\mathrm{m}}(n+1)$ 个线性方程组，矩阵M和N中有 $n_{\mathrm{m}}(n+1)$ 个未知元素。方程组式(7.234)和式(7.235)的解存在的一个充要条件是被控对象的传递零点与模型 $A_{m}$ 的特征值不匹配。令控制律为

$$u = N z - K (x - M z) \tag {7.236}$$

其中：K 按通常的方法设计，使得 A-BK 具有满意的稳态控制。我们观察到，

$$\delta u = u - N z = N z - K (x - M z) - N z = - K \delta x \tag {7.237}$$

在给定控制律作用下，式(7.236)即被控对象方程变为

$$\dot {x} = A x + B (N z - K (x - M z))= (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {B} (\mathbf {N} + \mathbf {K M}) \mathbf {z} \tag {7.238}$$

在频域中，注意到 $\mathbf{Z}(s)=(s\mathbf{I}-\mathbf{A}_{\mathrm{m}})^{-1}\mathbf{B}_{\mathrm{m}}$ ，可以写为

$$\boldsymbol {X} (s) = (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) ^ {- 1} \boldsymbol {B} (\boldsymbol {N} + \boldsymbol {K M}) (s \boldsymbol {I} - \boldsymbol {A} _ {\mathrm{m}}) ^ {- 1} \boldsymbol {B} _ {\mathrm{m}} \tag {7.239}$$

现在，将式(7.234)中的 BN 代入上式，并加减 sM，可以写为

$$\boldsymbol {X} (s) = \left(s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}\right) ^ {- 1} \left[ \boldsymbol {M A} _ {\mathrm{m}} - \boldsymbol {A M} + \boldsymbol {B K M} \right] \left(s \boldsymbol {I} - \boldsymbol {A} _ {\mathrm{m}}\right) ^ {- 1} \boldsymbol {B} _ {\mathrm{m}} \tag {7.240}\boldsymbol {X} (s) = (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) ^ {- 1} [ (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}) \boldsymbol {M} - \boldsymbol {M} (s \boldsymbol {I} - \boldsymbol {A} _ {\mathrm{m}}) ] (s \boldsymbol {I} - \boldsymbol {A} _ {\mathrm{m}}) ^ {- 1} \boldsymbol {B} _ {\mathrm{m}} \tag {7.241}$$

若乘开，则结果为

$$\boldsymbol {X} (s) = \boldsymbol {M} \left(s \boldsymbol {I} - \boldsymbol {A} _ {\mathrm{m}}\right) ^ {- 1} \boldsymbol {B} _ {\mathrm{m}} - \left(s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K}\right) ^ {- 1} \boldsymbol {M B} _ {\mathrm{m}} \tag {7.242}$$

因此，输出 $Y(s)=CX(s)$ 为
