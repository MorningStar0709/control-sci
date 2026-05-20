# 例 4-7 自动平衡秤系统

自动平衡秤能自动完成称重操作, 其示意图如图 4-22 所示。称重时, 由下面一个电动反馈环节控制其自动平衡, 图 4-22 中所示为无重物时的平衡状态。图中, x 是砝码 $W_{c}$ 离枢轴的距离; 待称重物 W 将放置在离枢轴 $l_{w}=5cm$ 处; 重物一方还有一个黏性阻尼器, 其到枢轴的距离 $l_{i}=20cm$ 。平衡秤系统的有关参数如下:

![](image/cc1b4ddfcbc91ff8eff45a7d3299bfc5fd53452aeb956db7af69ceff4065f81c.jpg)

<details>
<summary>text_image</summary>

电池Ebb
Kf
Wc
x
导杆
直流电机
K1
W
枢轴
黏性阻尼器
y
Iw
x
li
</details>

图 4-22 自动平衡秤

枢轴惯量 $J=0.05kg \cdot m \cdot s^{2}$ ,

电池电压 $E_{th}=24V$ ,

黏性阻尼器的阻尼系数 $f=10\sqrt{3}kg\cdot m\cdot s/rad$ ,

反馈电位计增益 $K_{f}=400V/m$ ,

导引螺杆增益 $K_{s}=(1/4000\pi)\mathrm{m}/\mathrm{rad}$

输入电位计增益 $K_{i}=4800V/m$ ,

砝码 $W_{c}$ 的质量依需要的称重范围而定，本例 $W_{c}=2kg$ 。

要求完成以下设计工作：

1) 建立系统的模型及信号流图。  
2）在根轨迹图上确定根轨迹增益 $K^{*}$ 的取值。  
3）确定系统的主导极点。

设计后的系统达到以下性能指标要求：

1) 阶跃输入下： $K_{p}=\infty,e_{s}(\infty)=0$ 。  
2) 欠阻尼响应： $\zeta=0.5$ 。  
3）调节时间： $t_{s}<2s(\Delta=2\%)$ 。

解 首先建立平衡运动方程。设系统略偏其平衡状态，偏差角

$$\theta = \frac {y}{l _ {i}}$$

因 $J\frac{\mathrm{d}^2\theta}{\mathrm{d}t^2} = \Sigma$ 扭矩，故平衡秤关于枢轴的扭转矩方程为

$$J \frac {\mathrm{d} ^ {2} \theta}{\mathrm{d} t ^ {2}} = l _ {w} W - x W _ {c} - f l _ {i} ^ {2} \frac {\mathrm{d} \theta}{\mathrm{d} t}$$

电机输入电压 $v_{m}(t) = K_{i}y - K_{f}x$

电机的传递函数 $\frac{\Theta_m(s)}{V_m(s)} = \frac{K_m}{s(T_ms + 1)}$

式中， $\theta_{m}$ 为输出轴转角； $K_{m}$ 为电机传递系数； $T_{m}$ 为电机机电时间常数，与系统时间常数相比，可略去不计。

根据上述方程可画出系统信号流图,如图4-23所示。由信号流图可见,从物体质量 $W(s)$ 到测量值 $X(s)$ 的前向通路中,在节点测量高度 $Y(s)$ 之前有一个纯积分环节,因此该系统为I型系统,在阶跃输入作用下,能实现静态位置误差系数 $K_{p}=\infty$ 及稳态误差 $e_{s}(\infty)=0$ 的要求。应用梅森增益公式,可得系统闭环传递函数为

$$\frac {X (s)}{W (s)} = \frac {l _ {w} l _ {i} K _ {i} K _ {m} K _ {s} / J s ^ {3}}{1 + \left(f l _ {i} ^ {2} / J s\right) + \left(K _ {m} K _ {s} K _ {f} / s\right) + \left(l _ {i} K _ {i} K _ {m} K _ {s} W _ {c} / J s ^ {3}\right) + \left(f l _ {i} ^ {2} K _ {m} K _ {s} K _ {f} / J s ^ {2}\right)}$$

![](image/f51b4b8db3951a19cd0a16649e75dab4d1fd7559fa1077f5170a0d724e63a3a7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["W(s) 物体质量"] --> B["1/s"]
    B --> C["Y(s)"]
    C --> D["V_m(s)"]
    D --> E["电机"]
    E --> F["θ_m"]
    F --> G["X(s) 测量值"]
    G --> H["-W_c"]
    H --> I["L_3"]
    I --> J["L_i/Js"]
    J --> K["sY(s)"]
    K --> L["-fI_i"]
    L --> M["L_1"]
    M --> N["输入节点"]
    N --> O["K_i"]
    O --> P["电机"]
    P --> Q["K_m/s"]
    Q --> R["-K_f"]
    R --> S["X(s) 测量值"]
    S --> T["K_s"]
    T --> U["导引螺杆"]
    U --> V["-K_f"]
    V --> W["L_2"]
    W --> X["电机"]
    X --> Y["K_m/s"]
    Y --> Z["-W_c"]
    Z --> A
```
</details>

图 4-23 自动平衡秤信号流图
