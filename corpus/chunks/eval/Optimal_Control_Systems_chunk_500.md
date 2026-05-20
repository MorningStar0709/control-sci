C.2.7 MATLAB File for Example 4.2(example4\_2g.m)   
```matlab
function dg = example4_2g(t,g)
% Function for g
%
%Define variables to use in external functions
%
global tp p
%
%Definition of differential equations
%
dg=[(25*interp1(tp,p(:,2),t)+2)*g(2)-4*t -g(1)+(25*interp1(tp,p(:,3),t)+3)*g(2)];
%% 
```

C.2.8 MATLAB File for Example 4.2(example4\_2x.m)   
```matlab
function dx = example4_2x(t,x)
% Function for x
%
%Define variables to use in external functions
global tp p tg g
%
%Definition of differential equations
%
dx=[x(2)
-2*x(1)-3*x(2)-25*(interp1(tp,p(:,2),t)*x(1)+...
interp1(tp,p(:,3),t)*x(2)-interp1(tg,g(:,2),t))];
%% 
```
