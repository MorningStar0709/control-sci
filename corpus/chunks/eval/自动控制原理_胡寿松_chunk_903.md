# (1) 综合运用(串联校正)

例 B-5 设单位负反馈系统的开环传递函数为

$$G (s) = \frac {K}{s (s + 1)}$$

若要求系统在单位斜坡输入信号作用时，位置输出稳态误差 $e_{s}(\infty)\leqslant0.1\mathrm{rad}$ ，开环系统截止频率 $\omega_{c}^{\prime\prime}\geqslant4.4\mathrm{rad/s}$ ，相角裕度 $\gamma^{\prime\prime}\geqslant45^{\circ}$ ，幅值裕度 $h^{\prime\prime}\mathrm{dB}\geqslant10\mathrm{dB}$ ，试设计串联无源超前网络。

解 本题利用频域法设计无源超前网络的设计步骤如下：

1）根据稳态误差要求，确定开环增益 K；  
2）利用已确定的开环增益，计算待校正系统的幅值裕度、相角裕度及其对应的截止频率、穿

越频率；

3）根据截止频率 $\omega_{c}^{\prime\prime}$ 的要求，计算超前网络参数 a 和 T。为保证系统的响应速度，并充分利用网络的相角超前特性，可选择最大超前角频率等于截止频率，即 $\omega_{m}=\omega_{c}^{\prime\prime}$ 。其中 a 由

$$- L ^ {\prime} \left(\omega_ {c} ^ {\prime \prime}\right) = L _ {c} \left(\omega_ {m}\right) = 1 0 \lg a$$

确定,然后再由

$$T = \frac {1}{\omega_ {m} \sqrt {a}}$$

确定 $T$ 值。

4）确定无源超前网络和最大超前角 $\varphi_{m}$ 。

$$a G _ {c} (s) = \frac {1 + a T s}{1 + T s}, \quad \varphi_ {m} = \arcsin \frac {a - 1}{a + 1}$$

5) 验算已校正系统的幅值裕度、相角裕度及其对应的截止频率、穿越频率。若验算结果不满足指标要求，需重新选择 $\omega_{m}(=\omega_{c}^{\prime\prime})$ ，然后重复以上设计步骤。

MATLAB 程序：example5.m

K=1/0.1; %由稳态误差要求计算开环增益
G0=zpk([], [0-1], K); %建立开环系统模型
[h0, r, wx, wc]=margin(G0) %计算校正前系统的幅值裕度、相角裕度
%及其对应的截止频率、穿越频率
wm=4.4; %试取校正系统的截止频率
L=bode(G0, wm);
Lwc=20*log10(L)
a=10^(-0.1*Lwc) %确定超前校正网络参数a
T=1/(wm*sqrt(a)); %确定超前校正网络参数T
phi=asin((a-1)/(a+1)) %phi表示最大超前角φm
Gc=(1/a)*tf([a*T1], [T1]); %确定超前网络传递函数
Gc=a*Gc; %补偿无源超前网络产生的增益衰减，
%放大器增益提高a倍
G=Gc*G0; %计算已校正系统的开环传递函数
bode(G,'r',G0,'b-'); grid; %绘制系统校正前后的伯德图
[h,r, wx, wc]=margin(G) %计算已校正系统的幅值裕度、相角裕度
%及其对应的截止频率、穿越频率

在 MATLAB 中运行 M 文件 example5, 得系统校正前的截止频率为 $\omega_{c}^{\prime}=3.0849rad/s$ , 相角裕度 $\gamma^{\prime}=17.9642^{\circ}$ , 而二阶系统的幅值裕度必为 $+\infty dB$ 。由于截止频率和相角裕度均低于指标要求, 故采用串联超前校正是合适的。

校正后系统截止频率 $\omega_{c}^{\prime\prime}=4.4rad/s$ ，相角裕度 $\gamma^{\prime\prime}=49.3369^{\circ}\geqslant45^{\circ}$ ，而二阶系统的幅值裕度仍为 $+\infty dB$ ，全部满足设计指标要求。因此，超前网络传递函数为

$$3. 9 4 1 7 G _ {c} (s) = \frac {1 + 0 . 4 5 1 2 s}{1 + 0 . 1 1 4 5 s}$$

图 B-11 中虚线部分为系统校正前的对数幅频特性曲线, 实线部分为系统校正后的对数幅频特性曲线。若不满足设计指标要求，可重新选取截止频率 $\omega_{c}^{\prime \prime}$ ，直到满意为止。读者不妨重选 $\omega_{c}^{\prime \prime} = 5\mathrm{rad / s}$ ，可得 $\gamma^{\prime \prime} = 58.4765^{\circ} \geqslant 45^{\circ}$ ，幅值裕度为 $+\infty$ dB，仍然满足设计指标要求。

![](image/4c0a977a421bb0040b324202952208341ed9606786cd909fb2237a010b067d96.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | Amplitude/dB (Solid Line) | Amplitude/dB (Dashed Line) | Phase/(°) (Solid Line) | Phase/(°) (Dashed Line) |
| --- | --- | --- | --- | --- |
| 0.01 | 60 | 60 | -90 | -90 |
| 0.1 | 40 | 40 | -100 | -100 |
| 1 | 20 | 20 | -135 | -135 |
| 10 | -20 | -20 | -175 | -175 |
| 100 | -60 | -60 | -180 | -180 |
| 1000 | -100 | -100 | -180 | -180 |
</details>

图 B-11 对数幅频特性曲线
