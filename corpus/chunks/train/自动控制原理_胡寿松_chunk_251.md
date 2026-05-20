(1) 概略绘出 $0 < K_{a} < \infty$ 时系统的根轨迹图；  
(2) 确定增益 $K_{a}$ 的取值, 使系统闭环极点的阻尼比 $\zeta \geqslant 0.707$ 。

4-23 图 4-47(a) 是 V-22 鱼鹰型倾斜旋翼飞机示意图。V-22 既是一种普通飞机，又是一种直升机。当飞机起飞和着陆时，其发动机位置可以如图示那样，使 V-22 像直升机那样垂直起降；而在起飞后，它又可以将发动机旋转 $90^{\circ}$ ，切换到水平位置，像普通飞机一样飞行。在直升机模式下，飞机的高度控制系统如图 4-47(b) 所示。要求：

(1) 概略绘出当控制器增益 $K_{1}$ 变化时的系统根轨迹图, 确定使系统稳定的 $K_{1}$ 值范围;  
(2) 当取 $K_{1}=280$ 时, 求系统对单位阶跃输入 $r(t)=1(t)$ 的实际输出 $h(t)$ , 并确定系统的超调量和调节时间 ( $\Delta=2\%$ );  
(3) 当 $K_{1}=280, r(t)=0$ 时，求系统对单位阶跃扰动 $N(s)=1/s$ 的输出 $h_{n}(t)$ ;

![](image/8302567049738389d47c451ac40906d9731f64fc5b6fbf75546a2739aed39fe4.jpg)  
图 4-46 轧钢机控制系统

![](image/3acd5bf75e908cfd33b97984e041d37e8003c7bcf02e6909c2ce8abbd77060d3.jpg)

<details>
<summary>natural_image</summary>

Illustration of a propeller aircraft in flight, showing fuselage, wings, and propeller (no text or symbols)
</details>

(a) V-22鱼鹰型倾斜旋翼(飞机)

![](image/093361417ef7f16e658a2928bfad423bac20056fa3ece3074e09f5d06789cab8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["控制器"]
    C --> D["N(s)"]
    D --> E["+"]
    E --> F["飞机动力学模型"]
    F --> G["H(s)"]
    G --> H["高度"]
    H --> I["-"]
    I --> B
    C --> J["K₁(s²+1.5s+0.5)/s"]
    J --> E
    F --> K["1/(20s+1)(10s+1)(0.5s+1)"]
```
</details>

(b) 控制系统  
图 4-47 V-22 鱼鹰型倾斜旋翼机的高度控制系统

(4) 若在 $R(s)$ 和第一个比较点之间增加一个前置滤波器

$$G _ {p} (s) = \frac {0 . 5}{s ^ {2} + 1 . 5 s + 0 . 5}$$

试重解问题(2)。

4-24 在未来的智能汽车-高速公路系统中，汇集了各种电子设备，可以提供事故、堵塞、路径规划、路边服务和交通控制等实时信息。图 4-48(a) 所示为自动化高速公路系统，图 4-48(b) 给出的是保持车辆间距的位置控制系统。要求选择放大器增益 $K_a$ 和速度反馈系数 $K_t$ 的取值，使系统响应单位斜坡输入 $R(s) = 1/s^2$ 的稳态误差小于 0.5，单位阶跃响应的超调量小于 10%，调节时间小于 $2s(\Delta = 5\%)$ 。

![](image/35be0f7825fe2dad46d42110bbadcadccb7d7f32b470a32b2c81f021ed8e05ca.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["侧向系统信息"] --> B["车辆间的通信"]
    B --> C["带有内置设备的车辆"]
    C --> D["协同引导路面"]
    D --> E["用于纵向控制的被动式路标"]
    E --> F["地段控制器"]
    F --> G["网络控制器"]
    G --> H["通信"]
    H --> I["通信"]
```
</details>

(a) 自动化高速公路系统

![](image/79d9aa18b49632bb56f2d3795623feb9e409c32c8ee09513b8dadc77d289f000.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["Kₙ"]
    C --> D["1/(s+3)(s+7)"]
    D --> E["速度"]
    E --> F["1/s"]
    F --> G["C(s) 位置"]
    G --> H["Kᵢ"]
    H --> I["-"]
    I --> B
```
</details>

(b) 车辆间距控制系统  
图 4-48 智能汽车-高速公路系统
