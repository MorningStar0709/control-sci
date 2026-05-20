# 15.2.4 姿态控制律设计

下面针对如下姿态子系统设计 PD 控制律，实现 $\theta \rightarrow \theta_{d}$ ， $\psi \rightarrow \psi_{d}$ 和 $\phi \rightarrow \phi_{d}$ 。

$$\ddot {\theta} = u _ {2} - \frac {l K _ {4}}{I _ {1}} \dot {\theta}\ddot {\psi} = u _ {3} - \frac {l K _ {5}}{I _ {2}} \dot {\psi}\ddot {\phi} = u _ {4} - \frac {l K _ {6}}{I _ {3}} \dot {\phi}$$

取 $\theta_{e}=\theta-\theta_{d}$ ，采用基于前馈补偿的 PD 控制方法，设计控制律为

$$u _ {2} = - k _ {\mathrm{p4}} \theta_ {\mathrm{e}} - k _ {\mathrm{d4}} \dot {\theta} _ {\mathrm{e}} + \ddot {\theta} _ {\mathrm{d}} + \frac {l K _ {4}}{I _ {1}} \dot {\theta} _ {\mathrm{d}} \tag {15.22}$$

则 $\ddot{\theta} = -k_{\mathrm{p4}}\theta_{\mathrm{e}} - k_{\mathrm{d4}}\dot{\theta}_{\mathrm{e}} + \ddot{\theta}_{\mathrm{d}} - \frac{lK_4}{I_1}\dot{\theta}_{\mathrm{e}}$ ，从而 $\ddot{\theta}_{\mathrm{e}} + \left(k_{\mathrm{d4}} + \frac{lK_4}{I_1}\right)\dot{\theta}_{\mathrm{e}} + k_{\mathrm{p4}}\theta_{\mathrm{e}} = 0$ ，根据二阶系统Hurwitz判据，需要满足 $k_{\mathrm{p4}} > 0$ ， $k_{\mathrm{d4}} + \frac{lK_4}{I_1} >0$ ，可取 $k_{\mathrm{p4}} = 15$ ， $k_{\mathrm{d4}} = 15$ 。

取 $\psi_{e}=\psi-\psi_{d}$ ，针对第二个姿态角子系统，设计控制律为

$$u _ {3} = - k _ {\mathrm{p5}} \psi_ {\mathrm{e}} - k _ {\mathrm{d5}} \dot {\psi} _ {\mathrm{e}} + \ddot {\psi} _ {\mathrm{d}} + \frac {l K _ {5}}{I _ {2}} \dot {\psi} _ {\mathrm{d}} \tag {15.23}$$

则 $\ddot{\psi}_{e} = -k_{p5}\psi_{e} - k_{d5}\dot{\psi}_{e} - \frac{lK_{5}}{I_{2}}\dot{\psi}_{e}$ ，从而 $\ddot{\psi}_{e} + \left(k_{d5} + \frac{lK_{5}}{I_{2}}\right)\dot{\psi}_{e} + k_{p5}\psi_{e} = 0$ ，根据二阶系统 Hurwitz 判据，需要满足 $k_{p5} > 0$ ， $k_{d5} + \frac{lK_{5}}{I_{2}} > 0$ ，可取 $k_{p5} = 15$ ， $k_{d5} = 15$ 。

取 $\phi_{e}=\phi-\phi_{d}$ ，针对第三个姿态角子系统，设计控制律为

$$u _ {4} = - k _ {\mathrm{p6}} \phi_ {\mathrm{e}} - k _ {\mathrm{d6}} \dot {\phi} _ {\mathrm{e}} + \ddot {\phi} _ {\mathrm{d}} + \frac {l K _ {6}}{I _ {3}} \dot {\phi} _ {\mathrm{d}} \tag {15.24}$$

则 $\ddot{\phi}_{\mathrm{e}} = -k_{\mathrm{p6}}\phi_{\mathrm{e}} - k_{\mathrm{d6}}\dot{\phi}_{\mathrm{e}} - \frac{lK_6}{I_3}\dot{\phi}_{\mathrm{e}}$ ，从而 $\ddot{\phi}_{\mathrm{e}} + \left(k_{\mathrm{d6}} + \frac{lK_6}{I_3}\right)\dot{\phi}_{\mathrm{e}} + k_{\mathrm{p6}}\phi_{\mathrm{e}} = 0$ ，根据二阶系统Hurwitz判据，需要满足 $k_{\mathrm{p6}} > 0$ ， $k_{\mathrm{d6}} + \frac{lK_6}{I_3} >0$ ，可取 $k_{\mathrm{p6}} = 15$ ， $k_{\mathrm{d6}} = 15$ 。

![](image/5aa7974da9f0405f5ced2b8aee9b62f8f80c21fbf44da4f0e5fde42d48c65ae6.jpg)
