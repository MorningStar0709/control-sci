```matlab
%Single Link Inverted Pendulum Parameters
g=9.8;
M=1.0;
m=0.1;
L=0.5;

I=1/12*m*L^2;
l=1/2*L;
t1=m*(M+m)*g*l/[(M+m)*I+M*m*l^2];
t2=-m^2*g*l^2/[(m+M)*I+M*m*l^2];
t3=-m*l/[(M+m)*I+M*m*l^2];
t4=(I+m*l^2)/[(m+M)*I+M*m*l^2];

A=[0,1,0,0;
    t1,0,0,0;
    0,0,0,1;
    t2,0,0,0];
B=[0;t3;0;t4];
C=[1,0,0,0;
    0,0,1,0];
D=[0;0];

M=2;
if M==1 % LQR
    Q=[100,0,0,0; %100,10,1,1 express importance of theta,dtheta,x,dx
    0,10,0,0;
    0,0,1,0;
    0,0,0,1];
    R=[0.1];
    K=LQR(A,B,Q,R); %LQR Gain
elseif M==2 % Pole point placement
    P=[-10-10i -10+10i -10 -20]; %Stable pole point
    K=place(A,B,P);
end

X=[u(1) u(2) u(3) u(4)]';
ut=-K*X;

sys(1)=ut; 
```

④ 作图子程序：chap17\_2plot.m

```matlab
close all;
figure(1);
subplot(211);
plot(t,x(:,1),'r','linewidth',2);
xlabel('time(s)');ylabel('Pendulum Angle response');
subplot(212);
plot(t,x(:,2),'r','linewidth',2); 
```

xlabel('time(s)');ylabel('Pendulum Angle speed response');   
```matlab
figure(2);
subplot(211);
plot(t,x(:,3),'r','linewidth',2);
xlabel('time(s)');ylabel('Cart position response');
subplot(212);
plot(t,x(:,4),'r','linewidth',2);
xlabel('time(s)');ylabel('Cart speed response');
figure(3);
plot(t,ut,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input'); 
```
