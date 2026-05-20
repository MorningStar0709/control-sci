# 〖仿真程序〗

(1) 模糊系统程序: chap8\_4a.m

```matlab
%Fuzzy Tunning PI Control
clear all;
close all;
a=newfis('fuzzpid');
a=addvar(a,'input','e',[-1,1]); %Parameter e
a=addmf(a,'input',1,'N','zmf',[-1,-1/3]);
a=addmf(a,'input',1,'Z','trimf',[-2/3,0,2/3]); 
```

```matlab
a=addmf(a,'input',1,'P','smf',[1/3,1]);
a=addvar(a,'input','ec',[-1,1]); %Parameter ec
a=addmf(a,'input',2,'N','zmf',[-1,-1/3]); 
a=addmf(a,'input',2,'Z','trimf',[-2/3,0,2/3]); 
a=addmf(a,'input',2,'P','smf',[1/3,1]);
a=addvar(a,'output','kp',1/3*[-10,10]); %Parameter kp
a=addmf(a,'output',1,'N','zmf',1/3*[-10,-3]); 
a=addmf(a,'output',1,'Z','trimf',1/3*[-5,0,5]); 
a=addmf(a,'output',1,'P','smf',1/3*[3,10]);
a=addvar(a,'output','ki',1/30*[-3,3]); %Parameter ki
a=addmf(a,'output',2,'N','zmf',1/30*[-3,-1]); 
a=addmf(a,'output',2,'Z','trimf',1/30*[-2,0,2]); 
a=addmf(a,'output',2,'P','smf',1/30*[1,3]);
rulelist=[1 1 1 2 1 1;
    1 2 1 2 1 1;
    1 3 1 2 1 1;
    2 1 1 3 1 1;
    2 2 3 3 1 1;
    2 3 3 3 1 1;
    3 1 3 2 1 1;
    3 2 3 2 1 1;
    3 3 3 2 1 1];
a=addrule(a,rulelist);
a=setfis(a,'DefuzzMethod','centroid');
writefis(a,'fuzzpid');
a=readfis('fuzzpid');
figure(1);
plotmf(a,'input',1);
figure(2);
plotmf(a,'input',2);
figure(3);
plotmf(a,'output',1);
figure(4);
plotmf(a,'output',2);
figure(5);
plotfis(a);
fuzzy fuzzpid;
showrule(a)
ruleview fuzzpid; 
```

(2) 模糊控制程序: chap8\_4b.m

```txt
%Fuzzy PI Control 
```

```matlab
close all;
clear all;

warning off;
a=readfis('fuzzpid');    %Load fuzzpid.fis

ts=0.001;
sys=tf(133,[1,25,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;
y_1=0;y_2=0;
e_1=0;ec_1=0;ei=0;

kp0=0;ki0=0;
for k=1:1:1000
time(k)=k*ts;

yd(k)=1;
%Using fuzzy inference to tuning PI
k_pid=evalfis([e_1,ec_1],a);
kp(k)=kp0+k_pid(1);
ki(k)=ki0+k_pid(2);
u(k)=kp(k)*e_1+ki(k)*ei;

y(k)=-den(2)*y_1-den(3)*y_2+num(2)*u_1+num(3)*u_2;
e(k)=yd(k)-y(k);
%%%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%,%%,%
y_2=y_1;y_1=y(k);

ei=ei+e(k)*ts;    % Calculating I

ec(k)=e(k)-e_1;
e_1=e(k);
ec_1=ec(k);
end

figure(1);
plot(time,yd,'r','time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('ideal position','position tracking');
figure(2);
subplot(211);
plot(time,kp,'r','linewidth',2);
xlabel('time(s)');ylabel('kp');
subplot(212);
plot(time,ki,'r','linewidth',2);
xlabel('time(s)');ylabel('ki');
figure(3); 
```

```matlab
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input'); 
```

![](image/38b287ae4ab33cf26fe5af743845eecabe6415c142bd032825a00f9b7e9d3ce7.jpg)
