[iteraion_fitness(N),flag]=min(Fitness); %记下第 NC 次迭代的最小数值及其维数

lujing(N,:)=Path(flag,:) %第 NC 次迭代的最佳路径
fprintf('N=%d Jmin=%g\n',N,iteraion_fitness(N));
end
```

```matlab
[Best_fitness,flag1]=min(iteraion_fitness);
Best_solution=lujing(flag1,:);
YY(2)=Best_solution(1);YY(3)=Best_solution(2);YY(4)=Best_solution(3);YY(5)=Best_solution(4);

Finally_spline=spline(XX,YY,linspace(0,1,1000));
chap10_6obj(Finally_spline,distance_Path(Size,:),1);

figure(3);
plot((0:0.001:1),[0,thr(1:1:1000)],'k','linewidth',2);
xlabel('Time (s)');ylabel('Ideal Path');
hold on;
plot((0:0.2:1),YY,'ko','linewidth',2);
hold on;
plot((0:0.001:1),[0,Finally_spline],'k-','linewidth',2);
xlabel('Time (s)');ylabel('Optimized Path');
legend('Ideal Path','Interpolationpoints','Optimized Path');

figure(4);
plot((1:Nmax),iteraion_fitness,'k','linewidth',2);
xlabel('Time (s)');ylabel('Fitness Change'); 
```

(2) 目标函数程序: chap10\_6obj.m  
```matlab
%**********计算控制输入能量消耗最低及路径逼近最佳值之和的子函数**********%
function Object=object(path,distance,flag) %path,distance 是 2000 维
global TE G ts
w=0.60;
th_1=0;tol_1=0;e_1=0;
tmax=3*TE; %目标函数积分上限为 3TE
thd=0.5;
thop_1=0;dthop_1=0;
x1_1=0;x2_1=0;
for k=1:1:G %Begin th(k)从 2 开始和 thop(1)对应
t(k)=k*ts;
if t(k)<=TE
thop(k)=path(k); %要逼近的最优轨迹
dthop(k)=(thop(k)-thop_1)/ts;
ddthop(k)=(dthop(k)-dthop_1)/ts;
else
thop(k)=thd;
dthop(k)=0;
ddthop(k)=0;
end
%离散模型
I=1/133;b=25/133;
d(k)=1*sin(k*ts);
x2(k)=x2_1+ts*1/I*(tol_1-b*x2_1+d(k));
```

```matlab
x1(k)=x1_1+ts*x2(k);

th(k)=x1(k);
dth(k)=x2(k);

e(k)=thop(k)-th(k);
de(k)=(e(k)-e_1)/ts;

kp=300;kd=0.30;

tol(k)=kp*e(k)+kd*de(k);
energy(k)=abs(tol(k)*dth(k));

tol_1=tol(k);
x1_1=x1(k);
x2_1=x2(k);
e_1=e(k);
thop_1=thop(k);
dthop_1=dthop(k);

end

%**********计算总能量**********%

energy_all=0;
for k=1:1:G
energy_all=energy_all+energy(k);
end

dis=sum(distance);%参考轨迹的逼近误差
%**********计算目标**********%

Object=w*energy_all+(1-w)*dis; %used for main.m
if flag==1
t(1)=0;
    th0=0;
    for k=1:1:G    %>TE 不包含原点
t(k)=k*ts;
if t(k)<TE
thr(k)=(thd-th0)*(t(k)/TE-1/(2*pi)*sin(2*pi*t(k)/TE))+th0;    %不含原点的参考轨迹
else
thr(k)=thd;
end

end

figure(1);
plot(t,thr,'k.-',t,thop,'k',t,th,'k-','linewidth',2);
legend('Ideal trajectory','Optimal trajectory','Trajectory tracking');
xlabel('Time (s)');ylabel('Joint angle tracking');
figure(2);
plot(t,tol,'k','linewidth',2);
xlabel('Time (s)');ylabel('Control input,tol');
end

end 
```
