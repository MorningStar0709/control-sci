# 15.2.2 位置控制律设计

首先通过设计位置控制律 $u_{1}$ ，实现 $x\to0,\quad y\to0,\quad z\to z_{d}$ 。由式（15.11），定义

$$u _ {1 x} = u _ {1} \left(\cos \phi \sin \theta \cos \psi + \sin \phi \sin \psi\right)u _ {1 y} = u _ {1} \left(\sin \phi \sin \theta \cos \psi - \cos \phi \sin \psi\right) \tag {15.12}u _ {1 z} = u _ {1} \cos \phi \cos \psi$$

则用来描述位置状态的模型为

$$\ddot {x} = u _ {1 x} - \frac {K _ {1}}{m} \dot {x}\ddot {y} = u _ {1 y} - \frac {K _ {2}}{m} \dot {y} \tag {15.13}\ddot {z} = u _ {1 z} - g - \frac {K _ {3}}{m} \dot {z}$$

首先针对第一个位置子系统，采用 PD 控制方法设计控制律为

$$u _ {1 x} = - k _ {\mathrm{px}} x - k _ {\mathrm{dx}} \dot {x} \tag {15.14}$$

则 $\ddot{x}+(k_{\mathrm{dx}}+K_{1}/m)\dot{x}+k_{\mathrm{px}}x=0$ 。根据二阶系统 Hurwitz 判据，需要满足 $k_{px}>0$ ， $k_{dx}+K_{1}/m>0$ ，可取 $k_{px}=5.0$ ， $k_{dx}=5.0$ 。

同理，针对第二个位置子系统，设计 PD 控制律为

$$u _ {1 y} = - k _ {\mathrm{py}} y - k _ {\mathrm{dy}} \dot {y} \tag {15.15}$$

则 $\ddot{y}+\left(k_{dy}+K_{2}/m\right)\dot{y}+k_{py}.y=0$ 。根据二阶系统 Hurwitz 判据，需要满足 $k_{py}>0$ ， $k_{dy}+K_{2}/m>0$ ，可取 $k_{py}=5.0$ ， $k_{dy}=5.0$ 。

针对第三个位置子系统，设计基于前馈和重力补偿的 PD 控制律为

$$u _ {1 z} = - k _ {\mathrm{pz}} z _ {\mathrm{e}} - k _ {\mathrm{dz}} \dot {z} _ {\mathrm{e}} + g + \ddot {z} _ {\mathrm{d}} + \frac {K _ {3}}{m} \dot {z} _ {\mathrm{d}} \tag {15.16}$$

式中， $z_{e}=z-z_{d}$ 。

则 $\ddot{z} = -k_{\mathrm{pz}}z_{\mathrm{e}} - k_{\mathrm{dz}}\dot{z}_{\mathrm{e}} + \ddot{z}_{\mathrm{d}} - \frac{K_3}{m}\dot{z}_{\mathrm{e}}$ ，即 $\ddot{z}_{\mathrm{e}} + \left(k_{\mathrm{dz}} + \frac{K_3}{m}\right)\dot{z}_{\mathrm{e}} + k_{\mathrm{pz}}z_{\mathrm{e}} = 0$ 。

根据二阶系统 Hurwitz 判据，需要满足 $k_{pz} > 0$ ， $k_{dz} + \frac{K_{3}}{m} > 0$ ，可取 $k_{pz} = 5.0$ ， $k_{dz} = 5.0$ 。

![](image/0ddf4db7f48b4a4317818cf032482c9ca6da9f169d0564b706ca2163471e1f6e.jpg)
