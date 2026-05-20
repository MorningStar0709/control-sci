# 机械手轨迹跟踪迭代学习控制仿真实例程序

(1) 主程序: chap11\_1main.m  
```matlab
% Adaptive switching Learning Control for 2DOF robot manipulators
clear all;
close all;

t=[0:0.01:3]';
k(1:301)=0;    % Total initial points
k=k';
T1(1:301)=0;
T1=T1';
T2=T1;
T=[T1 T2];
%%%%%
M=20;
for i=0:1:M    % Start Learning Control
i
pause(0.01);

sim('chap11_1sim',[0,3]);

q1=q(:,1);
dq1=q(:,2);
q2=q(:,3);
dq2=q(:,4);

q1d=qd(:,1);
dq1d=qd(:,2);
q2d=qd(:,3);
dq2d=qd(:,4);

e1=q1d-q1;
e2=q2d-q2;
de1=dq1d-dq1;
de2=dq2d-dq2;

figure(1);
subplot(211);
hold on;
plot(t,q1,'b',t,q1d,'r');
xlabel('time(s)');ylabel('q1d,q1(rad)');
subplot(212);
hold on;
plot(t,q2,'b',t,q2d,'r');
xlabel('time(s)');ylabel('q2d,q2(rad)');
```

```matlab
j=i+1;
times(j)=i;
e1i(j)=max(abs(e1));
e2i(j)=max(abs(e2));
deli(j)=max(abs(de1));
de2i(j)=max(abs(de2));
end % End of i
%%%%%
figure(2);
subplot(211);
plot(t,q1d,'r',t,q1,'b');
xlabel('time(s)');ylabel('Position tracking of Link 1');
subplot(212);
plot(t,q2d,'r',t,q2,'b');
xlabel('time(s)');ylabel('Position tracking of Link 2'); 
```

```matlab
figure(3);
plot(times, eli, '* -r', times, e2i, 'o-b');
title('Change of maximum absolute value of error1 and error2 with times i');
xlabel('time(s)');ylabel('error 1 and error 2'); 
```

(2) Simulink 子程序: chap11\_1sim.mdl

![](image/ab30e039068bac1753ed36f8b77a8f6688bfaee7f0e14079170a091aa3143245.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["3 Clock"] --> B["t"]
    B --> C["Mux"]
    C --> D["chap11_1ctrl"]
    D --> E["S-Function2"]
    E --> F["Tj"]
    F --> G["chap11_1plant"]
    G --> H["q"]
    H --> I["To Workspace2"]
    G --> J["T"]
    J --> K["T"]
    K --> L["To Workspace1"]
    M["qd"] --> N["To Workspace7"]
    O["k"] --> P["u+1"]
    P --> Q["Fcn"]
    Q --> R["[tk"]]
    R --> S["From Workspace2"]
    T["u+"] --> U["fcn"]
    U --> V["[tk"]]
    V --> W["From Workspace1"]
    X["[t T"]] --> Y["Switch"]
    Y --> Z["Tj-1"]
    AA["0 Constant"] --> Y
    AB["To Workspace3"] --> AC["To Workspace3"]
    AD["To Workspace2"] --> AE["To Workspace2"]
```
</details>

(3) 指令程序: chap11\_linput.m

```matlab
function [sys,x0,str,ts] = spacemodel(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 3,
    sys=mdlOutputs(t,x,u);
case {2,4,9}
    sys=[];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
) 
```
