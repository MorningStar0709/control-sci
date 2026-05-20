# 15.2.3 虚拟姿态角度的求解

假设满足控制律式（15.14）～式（15.16）所需要的姿态角度为 $\theta_{d}$ 和 $\psi_{d}$ ，为了实现 $\theta$ 对 $\theta_{d}$ 的跟踪， $\psi$ 对 $\psi_{d}$ 的跟踪，需要 $\theta_{d}$ 和 $\psi_{d}$ 进行求解。

由式（15.12）可知

$$
\left[ \begin{array}{l} u _ {1 x} \\ u _ {1 y} \end{array} \right] = \left[ \begin{array}{l} \cos \phi \sin \theta_ {\mathrm{d}} \cos \psi_ {\mathrm{d}} + \sin \phi \sin \psi_ {\mathrm{d}} \\ \sin \phi \sin \theta_ {\mathrm{d}} \cos \psi_ {\mathrm{d}} - \cos \phi \sin \psi_ {\mathrm{d}} \end{array} \right] u _ {1} = \left[ \begin{array}{c c} \cos \phi & \sin \phi \\ \sin \phi & - \cos \phi \end{array} \right] \left[ \begin{array}{c} \sin \theta_ {\mathrm{d}} \cos \psi_ {\mathrm{d}} \\ \sin \psi_ {\mathrm{d}} \end{array} \right] u _ {1}
$$

由于 $\begin{bmatrix}\cos\phi & \sin\phi \\ \sin\phi & -\cos\phi\end{bmatrix}^{-1}=\begin{bmatrix}\cos\phi & \sin\phi \\ \sin\phi & -\cos\phi\end{bmatrix}$ ，则上式变为

$$
\left[ \begin{array}{c c} \cos \phi & \sin \phi \\ \sin \phi & - \cos \phi \end{array} \right] \left[ \begin{array}{c} u _ {1 x} \\ u _ {1 y} \end{array} \right] = \left[ \begin{array}{c} \sin \theta_ {\mathrm{d}} \cos \psi_ {\mathrm{d}} \\ \sin \psi_ {\mathrm{d}} \end{array} \right] u _ {1}
$$

由 $u_{1z}=u_{1}\cos\phi\cos\psi_{d}$ ，可得 $u_{1}=\frac{u_{1z}}{\cos\phi\cos\psi_{d}}$ ，则

$$
\left[ \begin{array}{c c} \cos \phi & \sin \phi \\ \sin \phi & - \cos \phi \end{array} \right] \left[ \begin{array}{l} u _ {1 x} \\ u _ {1 y} \end{array} \right] = \left[ \begin{array}{c} \sin \theta_ {\mathrm{d}} \cos \psi_ {\mathrm{d}} \\ \sin \psi_ {\mathrm{d}} \end{array} \right] \frac {u _ {1 z}}{\cos \phi \cos \psi_ {\mathrm{d}}} \tag {15.17}
$$

由式（15.17）的第二行，可得

$$\frac {\cos \phi (\sin \phi \cdot u _ {1 x} - \cos \phi \cdot u _ {1 y})}{u _ {1 z}} = \frac {\sin \psi_ {\mathrm{d}}}{\cos \psi_ {\mathrm{d}}} = \tan \psi_ {\mathrm{d}}$$

则

$$\psi_ {\mathrm{d}} = \arctan \left(\frac {\sin \phi \cos \phi \cdot u _ {1 x} - \cos^ {2} \phi \cdot u _ {1 y}}{u _ {1 z}}\right) \tag {15.18}$$

由式（15.17）的第一行，可得

$$\frac {\cos \phi (\cos \phi \cdot u _ {1 x} + \sin \phi \cdot u _ {1 y})}{u _ {1 z}} = \sin \theta_ {\mathrm{d}} \tag {15.19}$$

需要注意的是，式（15.19）的左边值如果超出 $[-1 + 1]$ ，则造成 $\theta_{\mathrm{d}}$ 不存在，即无法求解，这是本算法的不足之处。
