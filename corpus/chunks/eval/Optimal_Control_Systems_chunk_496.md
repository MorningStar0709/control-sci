# C.1.2 MATLAB File lqrnssf.m

This file lqrnssf.m is used along with the other two files example.m and lqrnss.m given above.

```txt
%%% 
```

```matlab
%% The following is lqrnssf.m
%%
function dx = lqrnssf(t,x)
% Function for x
%
global A E F Md tf W11 W12 W21 W22 n
%Calculation of P, Riccati Analytical Solution
Tt=-inv(W22-F*W12)*(W21-F*W11);
P=(W21+W22*expm(-Md*(tf-t))*Tt*expm(-Md*(tf-t)))*...
inv(W11+W12*expm(-Md*(tf-t))*Tt*expm(-Md*(tf-t)));
%
xa=[A-E*P];
%
%Definition of differential equations
%
dx=[xa*x];
%%% 
```
