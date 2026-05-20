# C. 20 证明定理 12.2

为了分析闭环系统(12.58)\~(12.59)，我们把9.6节中慢变系统的稳定性分析与11.5节中奇异扰动系统的稳定性分析结合起来。由于w在证明中不起作用，可把方程(12.58)和方

程(12.59)写为 $\dot{\mathcal{X}} = g(\mathcal{X},\rho) + N(\rho)[\vartheta -\phi (\mathcal{X},\rho)]$ (C.88)

$$\varepsilon \dot {\vartheta} = - \vartheta + \phi (\mathcal {X}, \rho) \tag {C.89}$$

当 $\varepsilon = 0$ 时，可以得到降阶系统 $\dot{\mathcal{X}} = g(\mathcal{X},\rho)$ ，在定理12.1的证明中已用二次李雅普诺夫函数 $\mathcal{X}_{\delta}^{\mathrm{T}}P_{ms}\mathcal{X}_{\delta}$ 分析过该系统。可以验证 $\phi (\mathcal{X},\rho)$ 在定义域 $D_{\mathcal{X}}\times D_{\rho}$ 内是连续可微的，应用变量代换

$$\mathcal {Y} = \mathcal {X} - \mathcal {X} _ {\mathrm{ss}} (\rho), \quad \mathcal {Z} = \vartheta - \phi (\mathcal {X}, \rho)$$

则系统(C.88)\~(C.89)转换为

$$\dot {\mathcal {Y}} = g (\mathcal {Y} + \mathcal {X} _ {\mathrm{ss}} (\rho), \rho) + N (\rho) \mathcal {Z} - \frac {\partial \mathcal {X} _ {\mathrm{ss}}}{\partial \rho} \dot {\rho} \tag {C.90}\varepsilon \dot {\mathcal {Z}} = - \mathcal {Z} - \varepsilon \frac {\partial \phi}{\partial \mathcal {X}} [ g (\mathcal {Y} + \mathcal {X} _ {\mathrm{ss}} (\rho), \rho) + N (\rho) \mathcal {Z} ] - \varepsilon \frac {\partial \phi}{\partial \rho} \dot {\rho} \tag {C.91}$$

以 $\mathcal{V} = \mathcal{Y}^{\mathrm{T}}P_{ms}\mathcal{Y} + (1 / 2)\mathcal{Z}^{\mathrm{T}}\mathcal{Z}$ 作为系统(C.90)\~(C.91)的李雅普诺夫函数，可得在原点的某个邻域内，有
