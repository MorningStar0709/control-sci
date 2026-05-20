# 〖仿真程序〗

(1) 优化主程序: chap10\_6.m   
```matlab
clear all;
close all;
global TE G ts
Size=50;    %样本个数
D=4;    %每个样本有4个固定点，即分成4段
F=0.5;    %变异因子
CR=0.9;    %交叉因子

Nmax=30;    %DE优化次数
TE=1;    %参考轨迹参数TE
thd=0.50;
aim=[TE;thd];    %摆线路径终点
start=[0;0];    %路径起点
tmax=3*TE;    %仿真时间
ts=0.001;    %Sampling time
G=tmax/ts;    %仿真时间为G=3000
%**************************摆线参考轨迹**************************
th0=0;
dT=TE/1000; %将TE分为1000个点，每段长度（步长）为dT
for k=1:1:G
t(k)=k*dT;    %t(1)=0.001;t(2)=0.002;......
if t(k)<TE
thr(k)=(thd-th0)*(t(k)/TE-1/(2*pi)*sin(2*pi*t(k)/TE))+th0;    %不含原点的参考轨迹(1)
else
thr(k)=thd;
end
end
%**************************初始化路径**************************
for i=1:Size
for j=1:D
Path(i,j)=rand*(thd-th0)+th0;
end
end
%**************************差分进化计算**************************
for N=1:Nmax
%**************************变异**************************
for i=1:Size
    r1=ceil(Size*rand);
    r2=ceil(Size*rand);
    r3=ceil(Size*rand);
```

```matlab
while(r1==r2||r1==r3||r2==r3||r1==i||r2==i||r3==i) %选取不同的 r1,r2,r3，且不等于 i
    r1=ceil(Size*rand);
    r2=ceil(Size*rand);
    r3=ceil(Size*rand);

end

for j=1:D

mutate_Path(i,j)=Path(r1,j)+F.*(Path(r2,j)-Path(r3,j)); %选择前半部分产生变异个体
end

%**********交叉**********%

for j=1:D

if rand<=CR

cross_Path(i,j)=mutate_Path(i,j);
else

cross_Path(i,j)=Path(i,j);
end

end

%先进行三次样条插值，此为 D=4 时的特殊情况%
XX(1)=0;XX(2)=200*dT;XX(3)=400*dT;XX(4)=600*dT;XX(5)=800*dT;XX(6)=1000*dT;
YY(1)=th0;YY(2)=cross_Path(i,1);YY(3)=cross_Path(i,2);YY(4)=cross_Path(i,3);YY(5)=cross_Path(i,4);YY(6)=thd;
dY=[0 0];
cross_Path_spline=spline(XX,YY,linspace(0,1,1000));%输出插值拟合后的曲线，注意步长 nt 的一致，此时输出 1000 个点
YY(2)=Path(i,1);YY(3)=Path(i,2);YY(4)=Path(i,3);YY(5)=Path(i,4);
Path_spline=spline(XX,YY,linspace(0,1,1000));
%*** 计算指标并比较****%
for k=1:1000
distance_cross(i,k)=abs(cross_Path_spline(k)-thr(k)); %计算交叉后的轨迹与参考轨迹的距离值
distance_Path(i,k)=abs(Path_spline(k)-thr(k)); %计算插值后的轨迹与参考轨迹的距离值
end
new_object = chap10_6obj(cross_Path_spline,distance_cross(i,:),0); %计算交叉后的能量消耗
最低及路径逼近最佳值的和
formal_object = chap10_6obj(Path_spline,distance_Path(i,:),0); %计算插值后的能量消耗
最低及路径逼近最佳值的和

%%%%%%%%% 选择算法 %%%%%%%%%%%
if new_object<=formal_object
Fitness(i)=new_object;
Path(i,:)=cross_Path(i,:);
else
Fitness(i)=formal_object;
Path(i,:)=Path(i,:);
end
end
