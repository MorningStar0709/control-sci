# 2. 快系统模型的建立

由式（13.13）可得

$$\varepsilon \dot {z} = x ^ {2} - z + 1 + u _ {\mathrm{s}} + u _ {\mathrm{f}} = z _ {\mathrm{s}} - z + u _ {\mathrm{f}}$$

引入新变量 $z_{\mathrm{f}} = z - z_{\mathrm{s}}$ ，则上式变为

$$\varepsilon \dot {z} = - z _ {\mathrm{f}} + u _ {\mathrm{f}} \tag {13.16}$$

由于 $z = z_{s} + z_{f}$ ，当 $\varepsilon \to 0$ 时，则 $\varepsilon \dot{z} = \varepsilon \frac{dz_{s}}{dt} + \varepsilon \frac{dz_{f}}{dt}$ 。由于 $z_{s}$ 是基于慢时变系统的，而 z 是基于快时变系统的，则可取 $\varepsilon \frac{dz_{s}}{dt} = 0$ ，从而 $\varepsilon \dot{z} = \varepsilon \frac{dz_{f}}{dt}$ ，则式（13.16）变为

$$\varepsilon \frac {\mathrm{d} z _ {\mathrm{f}}}{\mathrm{d} t} = - z _ {\mathrm{f}} + u _ {\mathrm{f}}$$

引入伸长时标 $\tau=\frac{t}{\varepsilon}$ ，则在 $\tau$ 时间尺度下，可得快系统模型为

$$\frac {\mathrm{d} z _ {\mathrm{f}}}{\mathrm{d} \tau} = - z _ {\mathrm{f}} + u _ {\mathrm{f}} \tag {13.17}$$

![](image/4838e9cc8e56a720cb6055fccc8f2b6cbdcc9ada6f3d0a63a56e9e5594ecc45f.jpg)
