# 13.4.1 模型描述

在 13.3.2 节的基础上，考虑在机械臂的末端同时边界进行控制，根据 Hamilton 原理，此时柔性机械手动力学模型式（13.34）至式（13.37）包括以下 3 部分：

(1) 考虑分布式力平衡可得

$$\rho \ddot {z} (x) = - \mathrm{EI} z _ {x x x x} (x) \tag {13.38}$$

(2) 由边界点力平衡可得

$$I _ {\mathrm{h}} \ddot {\theta} = \tau + \mathrm{EIy} _ {x x} (0) \tag {13.39}m \ddot {z} (L) = \mathrm{EI} z _ {x x x} (L) + F \tag {13.40}$$

(3) 边界条件:

$$y (0) = 0 \tag {13.41}y _ {x} (0) = 0y _ {x x} (L) = 0 \tag {13.42}$$

上面几个公式的物理量说明见表 13-1。

控制目标： $\theta\rightarrow\theta_{d}$ ， $\dot{\theta}\rightarrow\dot{\theta}_{d}$ ， $y(x)\rightarrow0$ ， $\dot{y}(x)\rightarrow0$ ，其中 $\theta_{d}$ 为理想的角度信号， $\theta_{d}$ 为常值。

![](image/95b5fcfe79d5aa1142d33f47005d0afc04b8948e693202d0ead5411de988545c.jpg)
