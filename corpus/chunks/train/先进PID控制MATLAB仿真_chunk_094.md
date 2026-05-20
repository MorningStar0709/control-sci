# 【仿真之二】指令为三角波、锯齿波和随机信号

设计离散 PID 控制器，各信号的跟踪结果如图 1-16～图 1-18 所示，其中 S 代表输入指令信号的类型。通过取余指令 mod 实现三角波和锯齿波。当 S=1 时为三角波，S=2 时为锯齿波，S=3 时为随机信号。在仿真过程中，如果 D=1，则通过 pause 命令实现动态演示仿真。在随机信号跟踪中，对随机信号的变化速率进行了限制。

![](image/dbc9b43466041a9279e84e098ebf9feb13bd261953d6f1785b12b42e0e369f6c.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | -0.4 | -0.4 |
| 1.0 | 0.5 | 0.5 |
| 2.0 | -0.5 | -0.5 |
| 3.0 | 0.5 | 0.5 |
</details>

图 1-16 PID 三角波跟踪 (S=1)

![](image/9b556e96dd78e2b5a1f46180d82a0e672965087867b27d43bc6e336a4ec9682f.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 1.0 | 1.0 | 0.0 |
| 2.0 | 1.0 | 0.0 |
| 3.0 | 1.0 | 0.0 |
</details>

图 1-17 PID 锯齿波跟踪 (S=2)

![](image/373770438b06d8bb5de135c065360898b298777ba247ef6eec0befb826481a19.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.65 | 0.65 |
| 0.5 | 0.50 | 0.50 |
| 1.0 | 0.55 | 0.55 |
| 1.5 | 0.50 | 0.50 |
| 2.0 | 0.45 | 0.45 |
| 2.5 | 0.40 | 0.40 |
| 3.0 | 0.35 | 0.35 |
</details>

图 1-18 PID 随机信号跟踪（S=3）

〖仿真程序〗 chap1\_10.m

```txt
%PID Controller
clear all;
close all;
```

```matlab
ts=0.001;
sys=tf(5.235e005,[1,87.35,1.047e004,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0.0;u_2=0.0;u_3=0.0;
yd_1=rand;
y_1=0;y_2=0;y_3=0;

x=[0,0,0]';
error_1=0;

for k=1:1:3000
time(k)=k*ts;

kp=1.0;ki=2.0;kd=0.01;

S=3;
if S==1 %Triangle Signal
    if mod(time(k),2)<1
    yd(k)=mod(time(k),1);
    else
    yd(k)=1-mod(time(k),1);
    end
    yd(k)=yd(k)-0.5;
end
if S==2 %Sawtooth Signal
    yd(k)=mod(time(k),1.0);
end
if S==3 %Random Signal
    yd(k)=rand;
    dyd(k)=(yd(k)-yd_1)/ts; %Max speed is 5.0
    while abs(dyd(k))>=5.0
    yd(k)=rand;
    dyd(k)=abs((yd(k)-yd_1)/ts);
    end
end

u(k)=kp*x(1)+kd*x(2)+ki*x(3); %PID Controller

%Restricting the output of controller
if u(k)>=10
    u(k)=10;
end
if u(k)<=-10
    u(k)=-10;
end

%Linear model 
```

```matlab
y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(2)*u_1+num(3)*u_2+num(4)*u_3;
error(k)=yd(k)-y(k);

yd_1=yd(k);

u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);

x(1)=error(k); %Calculating P
x(2)=(error(k)-error_1)/ts; %Calculating D
x(3)=x(3)+error(k)*ts; %Calculating I
xi(k)=x(3);

error_1=error(k);
D=0;
if D==1 %Dynamic Simulation Display
    plot(time,yd,'b',time,y,'r');
    pause(0.00000000000000000);
end
end
figure(1);
plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking'); 
```

上述 PID 控制算法的缺点是，由于采用全量输出，所以每次输出均与过去的状态有关，计算时要对 error(k) 量进行累加，计算机输出控制量 $u(k)$ 对应的是执行机构的实际位置偏差，如果位置传感器出现故障， $u(k)$ 可能会出现大幅度变化。 $u(k)$ 的大幅度变化会引起执行机构位置的大幅度变化，这种情况在生产中是不允许的，在某些重要场合还可能造成重大事故。为避免这种情况的发生，可采用增量式 PID 控制算法。
