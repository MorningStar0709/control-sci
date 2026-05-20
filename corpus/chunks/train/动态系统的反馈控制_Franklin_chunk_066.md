# 例2.7 旋转及平移运动：悬吊式起重机

写出图 2.20 所示悬吊式起重机的运动方程在 $\theta=0$ 附近对方程进行线性化，这对悬吊式起重机而言是有效的；并在 $\theta=\pi$ 附近采取线性化处理，表示图 2.21 所示的倒立摆情况。小车的质量为 $m_{t}$ ，悬吊式起重机（摆锤）的质量是 $m_{p}$ ，质心处转动惯量为 I。摆锤枢轴点到质心的距离为 l；此时，摆关于枢轴点的转动惯量为 $(I+m_{p}l^{2})$ 。

![](image/71d629802d35d2efbbc404fafcc8737af2cd85118a9525ff99358c191d7c3d8b.jpg)

<details>
<summary>text_image</summary>

u
m_t
I, m_p
θ
</details>

图 2.20 悬挂负载的起重机简图

![](image/c0a6de96693a5603cf20610a027fd7c4141958b43721e1108217119c881ba43a.jpg)

<details>
<summary>text_image</summary>

θ′
l, mp
u → m₁
x
</details>

图 2.21 倒立摆

解答。建立小车及摆的受力图，并考虑两者之间的作用力。附录W2.1.3中我们给出了详细的过程。对小车的平移运动和摆的旋转运动应用牛顿定律，很容易发现两受力体之间的作用力可以忽略不计， $\theta$ 和 $x$ 未知。系统的建模结果是以小车所受力 $u$ 为输入，以 $\theta$ 和 $x$ 为状态变量的两个耦合的二阶非线性微分方程。在 $\theta = 0$ 附近的小范围内对运动方程进行线性化，即 $\cos \theta \approx 1$ ， $\sin \theta \approx \theta$ ， $\dot{\theta}^2 \approx 0$ ；因此，方程可近似为

$$\left(I + m _ {\mathrm{p}} l ^ {2}\right) \ddot {\theta} + m _ {\mathrm{p}} g l \theta = - m _ {\mathrm{p}} l \ddot {x}\left(m _ {\mathrm{t}} + m _ {\mathrm{p}}\right) \ddot {x} + b \dot {x} + m _ {\mathrm{p}} l \ddot {\theta} = u \tag {2.28}$$

注意到第一个方程与式(2.21)表征单摆的方程非常相似，其中，外加力矩由小车的加速度产生。同样地，表征小车运动 $x$ 的第二个方程，与汽车平移式(2.3)也很相似，其中，外加力由摆的角加速度产生。消去上述等式中的 $x$ ，可以得到传递函数。忽略摩擦项 $b$ 简化代数式，得控制输入 $u$ 到悬吊式起重机角度 $\theta$ 之间的传递函数为

$$\frac {\Theta (s)}{U (s)} = \frac {- m _ {\mathrm{p}} l}{((I + m _ {\mathrm{p}} l ^ {2}) (m _ {\mathrm{t}} + m _ {\mathrm{p}}) - m _ {\mathrm{p}} ^ {2} l ^ {2}) s ^ {2} + m _ {\mathrm{p}} g l (m _ {\mathrm{t}} + m _ {\mathrm{p}})} \tag {2.29}$$

对于图 2.21 所示的倒立摆，其中， $\theta\approx\pi$ ，假设 $\theta=\pi+\theta'$ ，其中 $\theta'$ 表示偏离竖直向上方向的运动量。此时， $\sin\theta\approx-\theta'$ ， $\cos\theta\approx-1$ ，则非线性方程变为 $^{\ominus}$

$$\left(I + m _ {\mathrm{p}} l ^ {2}\right) \ddot {\theta} ^ {\prime} - m _ {\mathrm{p}} g l \theta^ {\prime} = m _ {\mathrm{p}} l \ddot {x}\left(m _ {\mathrm{t}} + m _ {\mathrm{p}}\right) \ddot {x} + b \dot {x} - m _ {\mathrm{p}} l \ddot {\theta} ^ {\prime} = u \tag {2.30}$$

如例 2.2 指出，稳定系统中每个变量总是具有相同的符号，通过式(2.28)建立的悬吊式起重机的模型就是这样的例子。而式(2.30)中的第一个方程的 $\theta$ 和 $\ddot{\theta}$ 的符号是相反的，表明系统是不稳定的，这也正是倒立摆的特性。

忽略摩擦，得传递函数为
