$$
\dot {x} _ {\mathrm{c}} = A _ {\mathrm{c}} x _ {\mathrm{c}} + B _ {\mathrm{c}} eu = C _ {c} x _ {c} - K _ {0} x
\mathbf {A} _ {\mathrm{c}} = \left[ \begin{array}{l l} 0 & 1 \\ - 1 & 0 \end{array} \right], \quad \mathbf {B} _ {\mathrm{c}} = \left[ \begin{array}{l} - 1 6. 3 9 2 3 \\ - 2. 0 7 1 8 \end{array} \right], \quad \mathbf {C} _ {\mathrm{c}} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right]
$$

相关 Matlab 语句如下。

```matlab
% plant matrices
A=[0 1; 0 -1];
B=[0;1];
C=[1 0];
D=[0];
% form error space matrices
omega=1;
As=[0 1 0 0; -omega*omega 0 1 0; 0 0 0 1; 0 0 0 -1];
Bs=[0;0;B];

% desired closed-loop poles
j=sqrt(-1);
pc=[-1+sqrt(3)*j ;-1-sqrt(3)*j;-sqrt(3)+j;-sqrt(3)-j];
K=place(As,Bs,pc);
% form controller matrices
K1=K(:,1:2);
Ko=K(:,3:4);
Ac=[0 1; -omega*omega 0];
Bc=-[K(2);K(1)];
Cc=[1 0];
Dc=[0];
```

控制器的频率响应如图7.58所示，从该图中看出，在 $\omega_0 = 1\mathrm{rad / s}$ 的转速频率时，增益为正无穷。从 $r$ 到 $e$ 的频率响应[即灵敏度函数 $\mathcal{S}(s)]$ 如图7.59所示，从图中可以看到，在转动频率 $\omega_{0}=rad/s$ 处有一个尖锐凹口。从 w 到 y 的传递函数的频率响应也有相同的凹口。

![](image/4e85e6fd95740eaa1159ca5674bc52626a3adf5f6ba42f869d42d7397f080e96.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | 幅值/dB |
| --- | --- |
| 10⁻² | 0 |
| 10⁻¹ | 0 |
| 10⁰ | 230 |
| 10¹ | 0 |
</details>

![](image/ba8bf845b91a647dc98be2d047349214a940b4901de4e1b004e92adc20748f2f.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | 幅值/dB |
| --- | --- |
| 10^-1 | 0 |
| 10^0 | -200 |
| 10^1 | 0 |
| 10^2 | 0 |
</details>

![](image/5ba0892ff0daf7901fb6c5bddd73201966256f2b8dfaef431db48e566c00934a.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | 相位/(°) |
| --- | --- |
| 10^-2 | -200 |
| 10^-1 | -150 |
| 10^0 | 100 |
| 10^1 | 100 |
</details>

![](image/d0eb6337c447c374084ad5c018d64ebaf656e1e3942afa2a9ea6aec35c1eedb1.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | 相位(°) |
| --- | --- |
| 0.1 | 175 |
| 1 | 120 |
| 10 | 180 |
| 100 | 180 |
</details>

图 7.58 对于鲁棒伺服机构控制器的频率响应  
图 7.59 鲁棒伺服机构频率响应的灵敏度函数

（3）图7.60给出该系统的Simulink仿真图。虽然在Matlab环境下也可以进行仿真，但用Simulink的交互式图解环境更具指导意义。Simulink也提供了追加非线性特性（见第9章)和有效进行鲁棒研究的能力。 $^{①}$ 系统的跟踪性质如图7.61a所示，该图显示了系统的渐近跟踪性质。相应的控制量和跟踪误差信号分别如图7.61b和c所示。系统的干扰抑制性质如图7.62a所示，该图显示了对正弦扰动输入的渐近抑制过程。相应的控制效果如图7.62b所示。鲁棒的伺服机构的闭环频率响应[即互补传递函数 $T(s)$ ]如图7.63所示。由该图可知，从r到y的频率响应在 $\omega_{0}=rad/s$ 处为1，与要求相符。

![](image/faf4607118e2e7bcbf7e342afb2d7391cc1af37d5aa0e06e5edeaeb25fd39b14.jpg)
