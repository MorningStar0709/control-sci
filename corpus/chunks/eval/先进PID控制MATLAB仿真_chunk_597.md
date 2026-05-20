取 $X = \frac{\cos\phi(\cos\phi\cdot u_{1x} + \sin\phi\cdot u_{1y})}{u_{1z}}$ ，解决的方法为：当 $X > 1$ 时，取 $\sin \theta_{\mathrm{d}} = 1$ ，即 $\theta_{\mathrm{d}} = \frac{\pi}{2}$ ；当 $X < -1$ 时，取 $\sin \theta_{\mathrm{d}} = -1$ ，即 $\theta_{\mathrm{d}} = -\frac{\pi}{2}$ ；当 $|X|\leqslant 1$ 时，有 $\sin \theta_{\mathrm{d}} = X$ ，即

$$\theta_ {\mathrm{d}} = \arcsin \left(\frac {\cos \phi \left(\cos \phi \cdot u _ {1 x} + \sin \phi \cdot u _ {1 y}\right)}{u _ {1 z}}\right) \tag {15.20}$$

此时，为了使式（15.19）成立，式（15.19）可写为

$$\frac {\cos \phi \left(\cos \phi \cdot \left(u _ {1 x} + \varepsilon_ {1 x}\right) + \sin \phi \cdot \left(u _ {1 y} + \varepsilon_ {1 y}\right)\right)}{u _ {1 z} + \varepsilon_ {1 z}} = \sin \theta_ {\mathrm{d}}$$

式中， $\varepsilon_{1x}$ 、 $\varepsilon_{1y}$ 和 $\varepsilon_{1z}$ 为时变的实数值。 $\varepsilon=\left[\varepsilon_{1x}\quad\varepsilon_{1y}\quad\varepsilon_{1z}\right]$ ，当 $|X|\leqslant1$ 时，可取 $\varepsilon=0$ ，当 $|X|>1$ 时， $\varepsilon$ 为满足上式成立的实数。因此， $\varepsilon$ 相当于加在控制输入 $u_{1x}$ 、 $u_{1y}$ 和 $u_{1z}$ 上的扰动，可通过控制器的鲁棒特性来克服。

求解 $\theta_{d}$ 和 $\psi_{d}$ 后，便可得到位置控制律为

$$u _ {1} = \frac {u _ {1 z}}{\cos \phi \cos \psi_ {\mathrm{d}}} \tag {15.21}$$

![](image/518ffb7b737113056cad58371e906be9fa010ac00faec8a585fd333ebce5cd19.jpg)
