C.2.4 MATLAB File for Example 4.1 (example4\_1x.m)   
```matlab
function dx = example4_1x(t,x)
% Function for x
%
%Define variables to use in external functions
global tp p tg g
%
%Definition of differential equations
%
dx=[x(2)
-2*x(1)-3*x(2)-250*(interp1(tp,p(:,2),t)*x(1)+... 
```

```matlab
interp1(tp, p(:, 3), t) * x(2) - interp1(tg, g(:, 2), t))]; % 
```

C.2.5 MATLAB File for Example 4.2(example4\_1.m)   
```matlab
clear all
%
%Define variables to use in external functions
global tp p tg g
%
%Define Initial Conditions for numerical solution of
% g and x states
%
tf=20;
tspan=[tf 0];
tp=0.;
tg=0.;
tx=0.;
pf=[0.,0.,0.];
gf=[0.,0.];
x0=[-1.,0.];
%
%Calculation of P 
```

```matlab
[tp,p]=ode45('example4_2p',tspan,pf,...
odeset('refine',2,'RelTol',1e-4,'AbsTol',1e-6));
%Calculation of g
%
[tg,g]=ode45('example4_2g',tp,gf,...
odeset('refine',2,'RelTol',1e-4,'AbsTol',1e-6));
%
%Calculation of optimized x
%
[tx,x]=ode45('example4_2x',flipud(tg),x0,...
odeset('refine',2,'RelTol',1e-4,'AbsTol',1e-6));
%
fig=1; %Figure number
figure(fig)
plot(tp,real(p(:,1)),'k',tp,real(p(:,2)),'k',tp,... 
```

C.2 MATLAB $^{©}$ for Continuous-Time Tracking System

```matlab
real(p(:,3)),'k')
grid on
title('Plot of P')
xlabel('t')
ylabel('Riccati Coefficients')
hold
%
fig=fig+1;
%
%Plot g values
%
figure(fig);
plot(tg,real(g(:,1)),'k',tg,real(g(:,2)),'k')
grid on
title('Plot of g Vector')
xlabel('t')
ylabel('g vector')
%
fig=fig+1;
%
%Plot Optimized x
%
figure(fig);
plot(tx,real(x(:,1)),'k',tx,real(x(:,2)),'k')
grid on
title('Plot of Optimal States')
xlabel('t')
ylabel('Optimal States')
%
fig=fig+1;
%
%Calculate and Plot Optimized u
%
[n,m]=size(p);
p12=flipud(p(:,2));
p22=flipud(p(:,3));
x1=x(:,1);
x2=x(:,2);
g2=flipud(g(:,2)); 
```

```matlab
for i=1:1:n
    u(i) = -25*(p12(i)*x1(i) + p22(i)*x2(i) + g2(i));
end
figure(fig);
plot(tx,real(u),'b')
grid on
title('Plot of Optimal Control')
xlabel('t')
ylabel('Optimal Control')
%%% 
```

C.2.6 MATLAB File for Example 4.2(example4\_2p.m)   
```matlab
function dp = example4_2p(t,p)
% Function for P
%
%Define variables to use in external functions
%
%Definition of differential equations
%
dp=[25*p(2)^2+4*p(2)-2
    25*p(2)*p(3)-p(1)+3*p(2)+2*p(3)
    25*p(3)^2-2*p(2)+6*p(3)];
%% 
```
