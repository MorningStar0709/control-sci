# (3) 综合应用(系统时域动态性能分析)

例 B-2 已知系统的闭环传递函数为 $\Phi(s)=\frac{16}{s^{2}+8\zeta s+16}$ ，其中 $\zeta=0.707$ 。求二阶系统的单位脉冲响应、单位阶跃响应和单位斜坡响应。

解 MATLAB 程序: example2. m

```matlab
zeta=0.707;
num=[16];den=[18*zeta 16];
sys=tf(num, den); %建立闭环传递函数模型
p=roots(den) %计算系统特征根判断系统稳定性
t=0:0.01:3; %设定仿真时间为3s
figure(1)
impulse(sys, t); grid %求取系统的单位脉冲响应
xlabel('t'); ylabel('c(t)'); title('impulse response');
figure(2)
step(sys, t); grid %求取系统的单位阶跃响应
xlabel('t'); ylabel('c(t)'); title('step response');
figure(3)
u=t; %定义输入为斜坡信号
lsim(sys, u, t, 0); grid %求取系统的单位斜坡响应
xlabel('t'); ylabel('c(t)'); title('ramp response');
```

在 MATLAB 中运行 M 文件 example2 后, 得系统特征根为 -2.8280±j2.8289, 系统稳定。系统的单位脉冲响应、单位阶跃响应、单位斜坡响应分别如图 B-3, 图 B-4 和图 B-5 所示。在图 B-4 中, 点击鼠标右键可得系统超调量 $\sigma = 4.33\%$ , 上升时间 $t_r = 0.537\mathrm{s}$ , 调节时间 $t_s = 1.49\mathrm{s}$ ( $\Delta = 2\%$ )。若例题中 $\zeta = 0.5$ , 系统性能又将如何变化, 读者不妨一试。

![](image/52b65997109020ff5bb4bbb6e42b37e4171c5bff5c001f7f0d670352d8a4aa92.jpg)

<details>
<summary>line</summary>

| t/s | c(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.25 | 1.8 |
| 0.5 | 1.5 |
| 0.75 | 0.8 |
| 1.0 | 0.2 |
| 1.25 | -0.1 |
| 1.5 | -0.1 |
| 1.75 | -0.05 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
</details>

图 B-3 单位脉冲响应图

![](image/39295122f9f08866bb4d77b4ec6e1d4a3546528c5fef7980f730f90333f1936e.jpg)

<details>
<summary>line</summary>

| t/s | c(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.8 |
| 1.0 | 1.05 |
| 1.5 | 1.02 |
| 2.0 | 1.01 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
</details>

图 B-4 单位阶跃响应
