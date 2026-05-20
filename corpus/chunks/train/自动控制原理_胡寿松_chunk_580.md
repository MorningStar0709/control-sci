![](image/3fdccf116c6fee82e2027dc8ba1548b8f506b69cc27c591a0659f44ce7e5bef8.jpg)

<details>
<summary>line</summary>

| t | Tc |
| --- | --- |
| 0 | 20 |
| 10 | 80 |
| 20 | 120 |
| 30 | 160 |
| 40 | 200 |
| 50 | 205 |
| 60 | 200 |
| 70 | 205 |
| 80 | 200 |
| 90 | 205 |
| 100 | 205 |
</details>

图 8-62 温控系统的相轨迹及其时间响应(MATLAB)

例 8-11 带死区的仪表伺服机构控制。带有弹簧轴的仪表伺服机构的结构如图 8-63 所示。试用描述函数法并应用 MATLAB 确定线性部分为下列传递函数时系统是否稳定？是否存在自振？若有，参数是多少？

1) $G(s) = \frac{4000}{s(20s + 1)(10s + 1)};$   
2) $G(s) = \frac{20}{s(10s + 1)}$

解 应用 MATLAB 仿真法进行求解

![](image/91d6c2030db7d1d3b925b79b4f98509a380843ca60ca3d203204ded2c4882a64.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r=0"] --> B((+))
    B --> C["Block K=1"]
    C --> D["G(s)"]
    D --> E["c"]
    E --> F["Feedback"]
    F --> B
    style C fill:#f9f,stroke:#333
    style D fill:#ccf,stroke:#333
```
</details>

图 8-63 仪表伺服系统

(1) 死区非线性描述函数

由表8-1知

$$N (A) = \frac {2}{\pi} \left[ \frac {\pi}{2} - \arcsin \frac {1}{A} - \frac {1}{A} \sqrt {1 - \left(\frac {1}{A}\right) ^ {2}} \right], A \geqslant 1$$

(2) 稳定性分析基础

非线性系统闭环特征方程为

$$G (\mathrm{j} \omega) = - \frac {1}{N (A)}$$

在复平面上,下列结论成立:

若 $G(\mathrm{j}\omega)$ 曲线 $\Gamma_G$ 与负倒描述函数 $-1 / N(A)$ 曲线不相交，则当 $\Gamma_G$ 曲线不包围 $-1 / N(A)$ 曲线时，非线性系统稳定；当 $\Gamma_G$ 曲线包围 $-1 / N(A)$ 曲线时，非线性系统不稳定。

若 $G(\mathrm{j}\omega)$ 曲线 $\Gamma_G$ 与负倒描述函数 $-1 / N(A)$ 曲线存在交点，则在交点处，当 $-1 / N(A)$ 曲线沿振幅 $A$ 的增加方向由不稳定区域进入稳定区域时，该交点对应的自振是稳定的；当 $-1 / N(A)$ 沿 $A$ 的增加方向由稳定区域进入不稳定区域时，该交点对应的自振是不稳定的。自振振幅 $A$ 由交点处 $-1 / N(A)$ 上振幅确定；自振频率 $\omega_0$ 由交点处 $G(\mathrm{j}\omega)$ 上的频率确定。

(3) MATLAB 程序

1) 绘制系统的 $\Gamma_{G}$ 和 $-\frac{1}{N(A)}$ 曲线

```matlab
clc;clear
G1=tf([4000],[200 30 1 0]);
G2=tf([20],[10 1 0]);
A=1.0001:0.001:1000;
x=real(-1./(((2 * ((pi./2)-asin(1./A)-(1./A).*sqrt(1-(1./A).^2)))/pi+j*0));
y=imag(-1./(((2 * ((pi./2)-asin(1./A)-(1./A).*sqrt(1-(1./A).^2)))/pi+j*0));
%when the system is G1
figure(1)
w=0.001:0.001:1;
nyquist(G1,w);hold on
plot(x,y);hold off
axis([-60000 0 -40000 40000])
%when the system is G2
figure(2)
w=0.001:0.001:20;
nyquist(G2,w);hold on 
```

```txt
plot(x,y); hold off
axis([-3 0 -0.1 0.1]) 
```

2) 当初始条件 $c(0)=2$ 时，绘制系统的零输入响应曲线

```matlab
t=0:0.01:8;
c01=[2 0 0]';
[t,c1]=ode45('sys1',t,c01);
figure(1)
plot(t,c1(:,1));grid
%
t=0:0.01:120;
c02=[2 0]';
[t,c2]=ode45('sys2',t,c02);
figure(2)
plot(t,c2(:,1));grid 
```

调用函数：当仪表伺服系统 $G(s) = \frac{4000}{s(20s + 1)(10s + 1)}$
