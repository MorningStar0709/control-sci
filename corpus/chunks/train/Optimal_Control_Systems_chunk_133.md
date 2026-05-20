$$x _ {1} ^ {*} (t) = \frac {1}{1 4} t ^ {3} - \frac {2}{7} t ^ {2} + 2 t + 1,x _ {2} ^ {*} (t) = \frac {3}{1 4} t ^ {2} - \frac {4}{7} t + 2,\lambda_ {1} ^ {*} (t) = \frac {3}{7},\lambda_ {2} ^ {*} (t) = - \frac {3}{7} t + \frac {4}{7},u ^ {*} (t) = \frac {3}{7} t - \frac {4}{7}. \tag {2.7.78}$$

The previous results can also obtained using Symbolic Math Toolbox of the MATLAB©, Version 6, as shown below.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   
%% Solution Using Symbolic Math Toolbox (STB) in
%% MATLAB Version 6
%%
S=dsolve('Dx1=x2,Dx2=-lambda2,Dlambda1=0,Dlambda2=-lambda1,
x1(0)=1,x2(0)=2,lambda1(2)=x12-4,lambda2(2)=x22-2')
t='2';
S2=solve(subs(S.x1)-'x12',subs(S.x2)-'x22','x12,x22');
%% solves for x1(t=2) and x2(t=2)
x12=S2.x12;
x22=S2.x22;
clear t

2.7 Variational Approach to Optimal Control Systems

```matlab
lambda1: [1x1 sym]
lambda2: [1x1 sym]
x1: [1x1 sym]
x2: [1x1 sym]

x1=subs(S.x1)

x1 =
1-2/7*t^2+1/14*t^3+2*t

x2=subs(S.x2)

x2 =
-4/7*t+3/14*t^2+2

lambda1=subs(S.lambda1)

lambda1 =
3/7

lambda2=subs(S.lambda2)

lambda2 =
4/7-3/7*t

%% Plot command is used for which we need to
%% convert the symbolic values to numerical values.
j=1;
for tp=0:.02:2
t=sym(tp);
x1p(j)=double(subs(S.x1));
%% subs substitutes S.x1 to x1p
x2p(j)=double(subs(S.x2));
%% double converts symbolic to numeric
up(j)=-double(subs(S.lambda2));
%% optimal control u = -lambda_2
t1(j)=tp;
j=j+1;
end 
```

```javascript
plot(t1,x1p,'k',t1,x2p,'k',t1,up,'k:')
xlabel('t')
gtext('x_1(t)')
gtext('x_2(t)')
gtext('u(t)') 
```

```txt
****************************************************************************************** 
```

It is easy to see that the previous solutions for $x_1^*(t), x_2^*(t), \lambda_1^*(t), \lambda_2^*(t)$ , and $u^*(t) = -\lambda_2^*(t)$ obtained by using MATLAB© are the same as those given by (2.7.78) obtained analytically.

The optimal control and states for Example 2.15 are plotted in Figure 2.14.

![](image/90ef651bb7e3a8a1e59316f23f7e64f514ea43052cc2e63cf9a5424e2b8f3672.jpg)

<details>
<summary>line</summary>

| t | x₁(t) | x₂(t) | u(t) |
| --- | --- | --- | --- |
| 0.0 | 1.0 | 2.0 | -0.5 |
| 0.2 | 1.5 | 1.9 | -0.4 |
| 0.4 | 2.0 | 1.8 | -0.3 |
| 0.6 | 2.5 | 1.7 | -0.2 |
| 0.8 | 3.0 | 1.6 | -0.1 |
| 1.0 | 3.5 | 1.6 | 0.0 |
| 1.2 | 4.0 | 1.6 | 0.1 |
| 1.4 | 4.5 | 1.6 | 0.2 |
| 1.6 | 5.0 | 1.6 | 0.3 |
| 1.8 | 5.5 | 1.6 | 0.4 |
| 2.0 | 6.0 | 1.6 | 0.5 |
</details>

Figure 2.14 Optimal Control and States for Example 2.15
