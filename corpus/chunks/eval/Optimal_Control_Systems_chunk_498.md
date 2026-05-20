# C.2.1 MATLAB File for Example 4.1(example4\_1.m)

```matlab
clear all
%
%Define variables to use in external functions
global tp p tg g
%
%Define Initial Conditions for numerical solution 
```

C.2 MATLAB $^{©}$ for Continuous-Time Tracking System

```matlab
% of g and x states
%
tf=20;
tspan=[tf 0];
tp=0.;
tg=0.;
tx=0.;
pf=[2.,0.,0.];
gf=[2.,0.]；
x0=[-0.5,0.]；
%
%Calculation of P
%
[tp,p]=ode45('example4_1p',tspan,pf,odeset('refine',2,...
'RelTol',1e-4,'AbsTol',1e-6));
%
%Calculation of g
%
[tg,g]=ode45('example4_1g',tp,gf,odeset('refine',2,...
'RelTol',1e-4,'AbsTol',1e-6));
%
%Calculation of optimized x
%
[tx,x]=ode45('example4_1x',flipud(tg),x0,...
odeset('refine',2,'RelTol',1e-4,'AbsTol',1e-6));
%
%Plot Riccati coefficients
%
fig=1;    %Figure number
figure(fig)
plot(tp,real(p(:,1)),'k',tp,real(p(:,2)),'k',tp,...
real(p(:,3)),'k')
grid on
xlabel('t')
ylabel('Riccati Coefficients')
hold
%
fig=fig+1;
% 
```

```matlab
%Plot g values
%
figure(fig);
plot(tg,real(g(:,1)),'k',tg,real(g(:,2)),'k')
grid on
xlabel('t')
ylabel('g vector')
%%
% 
fig=fig+1;
%
%Plot Optimal States x
%
figure(fig);
plot(tx,real(x(:,1)),'k',tx,real(x(:,2)),'k')
grid on
xlabel('t')
ylabel('Optimal States')
%
fig=fig+1;
%
%Plot Optimal Control u
%
[n,m]=size(p);
p12=p(:,2);
p22=p(:,3);
x1=x(:,1);
x2=x(:,2);
g2=flipud(g(:,2));
for i=1:1:n
    u(i) = -250*(p12(i)*x1(i) + p22(i)*x2(i) - g2(i));
end
figure(fig);
plot(tp,real(u),'k')
grid on
xlabel('t')
ylabel('Optimal Control') 
```

C.2.2 MATLAB File for Example 4.1(example4\_1p.m)   
```matlab
function dp = example4_1p(t,p)
% Function for P
%
%Define variables to use in external functions
%
%Definition of differential equations
%
dp=[250*p(2)^2+4*p(2)-2
    250*p(2)*p(3)-p(1)+3*p(2)+2*p(3)
    250*p(3)^2-2*p(2)+6*p(3)];
% 
```

C.2.3 MATLAB File for Example 4.1(example4\_1g.m)   
```matlab
function dg = example4_1g(t,g)
% Function for g
%
%Define variables to use in external functions
%
global tp p
%
%Definition of differential equations
%
dg=[(250*interp1(tp,p(:,2),t)+2)*g(2)-2 -g(1)+(250*interp1(tp,p(:,3),t)+3)*g(2)]; 
```
