# 2.12.2 仿真实例

取模型为

$$G _ {\mathrm{p}} (s) = \frac {1 3 3}{s ^ {2} + 2 5 s + 1 0}$$

采样周期取 1ms，即 h=0.001。输入信号为幅度为正弦信号 $u(t)=0.5\sin(2\pi Ft)$ ，频率 F 的起始频率为 1Hz，终止频率为 10Hz，步长为 0.5Hz，对每个频率点，运行 20000 个采样时间，并记录采样区间为 [10000, 15000] 的数据。

求出实际模型在各个频率点的相频和幅频后，可写出开环传递函数频率特性的复数表示，即 $h_{\mathrm{p}} = M \left( \cos \varphi_{\mathrm{e}} + j \sin \varphi_{\mathrm{e}} \right)$ 。由于 $w = 2\pi F$ ，利用 MATLAB 函数 invfreqs $(h_{\mathrm{p}}, w, nb, na)$ ，可得到与复频特性 $h_{p}$ 相对应的、分子分母阶数分别为 nb 和 na 的传递函数的分子分母系数 bb 和 aa，从而得到逼近的开环传递函数，表示为

$$\hat {G} _ {\mathrm{p}} (s) = \frac {1 3 1 . 3}{s ^ {2} + 2 4 . 2 8 s + 1 0 . 0 8}$$

拟合对象传递函数 Bode 图和实际对象 Bode 图的比较如图 2-41 所示。可见，采用该算法能精确地求出对象的传递函数。

![](image/432c1a0d63c85970f2652b83c0038a78ed41337392535b3c9f7787833bc95b77.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Magnitude(dB) practical model | Magnitude(dB) estimate model | Phase(deg) practical model | Phase(deg) estimate model |
| --- | --- | --- | --- | --- |
| 0.01 | 20 | 20 | 0 | 0 |
| 0.1 | 15 | 15 | -30 | -30 |
| 1 | 5 | 5 | -60 | -60 |
| 10 | -10 | -10 | -90 | -90 |
| 100 | -40 | -40 | -130 | -130 |
| 1000 | -80 | -80 | -180 | -180 |
</details>

图 2-41 实际传递函数与拟合传递函数的 Bode 图比较

〖仿真程序〗 chap2\_14.m  
```matlab
%Transfer function identification with frequency test
clear all;
close all;

ts=0.001;
a=25;b=133;c=10;
sys=tf(b,[1,a,c]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

Am=0.5;
kk=0;

for F=1:0.5:10
kk=kk+1;
FF(kk)=F;

u_1=0.0;u_2=0.0; 
```

```matlab
y_1=0;y_2=0;

for k=1:1:20000
time(k)=k*ts;

u(k)=Am*sin(1*2*pi*F*k*ts); % Sine Signal with different frequency
y(k)=-den(2)*y_1-den(3)*y_2+num(2)*u_1+num(3)*u_2;

u_2=u_1;u_1=u(k);
y_2=y_1;y_1=y(k);
end

plot(time,u,'r',time,y,'b'); %Dynamic Simulation
pause(0.2);

for i=10001:1:15000
    fai(1,i-10000)=sin(2*pi*F*i*ts);
    fai(2,i-10000)=cos(2*pi*F*i*ts);
end

Fai=fai';

fai_in(kk)=0;

Y_out=y(10001:1:15000)';
cout=inv(Fai'*Fai)*Fai'*Y_out;
fai_out(kk)=atan(cout(2)/cout(1)); % Phase Frequency(Deg.)

if fai_out(kk)>0
    fai_out(kk)=fai_out(kk)-pi;
end

Af(kk)=sqrt(cout(1)^2+cout(2)^2); % Magnitude Frequency(dB)
mag_e(kk)=20*log10(Af(kk)/Am); % in dB.
ph_e(kk)=(fai_out(kk)-fai_in(kk))*180/pi; % in Deg.

if ph_e(kk)>0
    ph_e(kk)=ph_e(kk)-360;
end

end

FF=FF';
%%%,%%,%%,%%,%%% Closed system modelling
mag_e1=Af/Am; %From dB.to ratio
ph_e1=fai_out'-fai_in'; %From Deg. to rad

hp=mag_e1.*(cos(ph_e1)+j*sin(ph_e1)); %Practical frequency response vector
na=2; % Second order transfer function
nb=0; 
```

```matlab
w=2*pi*FF; % in rad./s
% bb and aa gives real numerator and denominator of transfer function
[bb,aa]=invfreqs(hp,w,nb,na); % w(in rad./s) contains the frequency values
G=tf(bb,aa) % Transfer function fitting
Figure(1);
bode(sys,'r',G,'k:');
legend('practical model','estimate model'); 
```
