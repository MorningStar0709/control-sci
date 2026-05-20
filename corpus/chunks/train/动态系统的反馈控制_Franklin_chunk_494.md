# 例 7.39 卫星姿态控制系统的回路传递恢复设计

考虑如下状态空间描述的卫星系统：

$$
\mathbf {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right], \quad D = 0
$$

（1）设计一个LQR控制器，其中， $Q = \rho C^{\mathrm{T}}C$ ， $R = 1$ ， $\rho = 1$ ，并确定回路增益。

（2）设计一个补偿器，当取 q=1，10，100 时，用回路传递恢复法来恢复(a)问中的 LQR 回路增益。  
（3）相对于外加白色高斯传感器噪声引起的执行器行为，将（b）问中的几种备选设计进行比较。

解答。用 lqr() 函数，由选定的 LQR 权值得到反馈增益 K = [1 1.414]。回路传递函数为

$$\mathbf {K} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} = \frac {1 . 4 1 4 (s + 0 . 7 0 7)}{s ^ {2}}$$

该 LQR 回路增益的幅值频率响应如图 7.73 所示。用 lqe() 函数设计估计器，令 $\Gamma = qB$ ， $R_{w} = \Gamma^{T}\Gamma$ ， $R_{v} = 1$ ，并取 q = 10，得到估计器的增益为

![](image/ede4ffe25650167b707fc09be914908ff0a7f172c0bbe68914739625962bc0c4.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | GM₁ | GM₂ | LQR |
| --- | --- | --- | --- |
| 10⁻¹ | ~10⁰ | ~10⁰ | ~10⁰ |
| 10⁰ | ~10⁻¹ | ~10⁻¹ | ~10⁻¹ |
| 10¹ | ~10⁻² | ~10⁻² | ~10⁻² |
| 10² | ~10⁻³ | ~10⁻³ | ~10⁻³ |
| 10³ | ~10⁻⁴ | ~10⁻⁴ | ~10⁻⁴ |
</details>

![](image/bba764f0321a186b58768d4505b9078d9604f3f03199b3283cedf7e11e6d7452.jpg)

<details>
<summary>line</summary>

| ω (rad/s) | 相位 (°) for PM₁ | 相位 (°) for PM | 相位 (°) for q=10 | 相位 (°) for q=100 |
| --- | --- | --- | --- | --- |
| 10⁻¹ | -150 | -180 | -90 | -90 |
| 10⁰ | -210 | -240 | -90 | -90 |
| 10¹ | -240 | -270 | -90 | -90 |
| 10² | -270 | -270 | -90 | -90 |
| 10³ | -270 | -270 | -90 | -90 |
</details>

图 7.73 回路传递恢复法设计的频率响应图

$$
\pmb {L} = \left[ \begin{array}{c} 1 4. 1 4 2 \\ 1 0 0 \end{array} \right]
$$

补偿器传递函数为

$$
\begin{array}{l} D _ {\mathrm{c}} (s) = \mathbf {K} (s \mathbf {I} - \mathbf {A} + \mathbf {B K} + \mathbf {L C}) ^ {- 1} \mathbf {L} \\ = \frac {1 5 5 . 5 6 (s + 0 . 6 4 2 8)}{(s ^ {2} + 1 5 . 5 5 6 s + 1 2 1)} = \frac {1 5 5 . 5 6 (s + 0 . 6 4 2 8)}{(s + 7 . 7 7 + 7 . 7 7 j) (s + 7 . 7 7 - 7 . 7 7 j)} \\ \end{array}
$$

回路传递函数为

$$D _ {c} (s) G (s) = \frac {1 5 5 . 5 6 (s + 0 . 6 4 2 8)}{s ^ {2} (s + 7 . 7 7 + 7 . 7 7 j) (s + 7 . 7 7 - j 7 . 7 7)}$$

图 7.73 给出了 q 取几个不同值 $(q=1, 10, 100)$ 时回路传递函数的频率响应和理想的 LQR 回路传递函数的频率响应。从图中还可以看出，随着 q 值的增大，回路增益越来越接近 LQR 的回路增益。当 q=10 时，“恢复后”的增益裕度为 GM=11.1=20.9dB，PM=55.06°。下面，给出实现上述回路传递恢复法设计步骤的 Matlab 语句：

```matlab
A=[0 1; 0 0];
B=[0;1];
C=[1 0];
D=[0];
sys0=ss(A,B,C,D);
C1=[1 0];
sys=ss(A,B,C1,D);

w=logspace(-1,3,1000);
rho=1.0;
Q=rho*C1'*C1;
r=1;
[K]=lqr(A,B,Q,r)
sys1=ss(A,B,K,0);
[maggk1,phasgk1]=bode(sys1,w);
```

```matlab
q=10;
gam=q*B;
Q1=gam'*gam;
rv=1;
[L]=lqe(A,gam,C,Q1,rv)
