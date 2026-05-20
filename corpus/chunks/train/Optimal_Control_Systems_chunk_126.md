```matlab
1+2*t-2*t^2+1/2*t^3
S.x2
ans =
2-4*t+3/2*t^2
S.lambda1
ans =
3
S.lambda2
ans =
4-3*t
Plot command is used for which we need to
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
plot(t1,x1p,'k',t1,x2p,'k',t1,up,'k:')
xlabel('t')
gtext('x_1(t)')
gtext('x_2(t)')
gtext('u(t)')
************************** 
```

It is easy to see that the previous solutions for $x_{1}^{*}(t)$ , $x_{2}^{*}(t)$ , $\lambda_{1}^{*}(t)$ , $\lambda_{2}^{*}(t)$ , and $u^{*}(t) = -\lambda_{2}^{*}(t)$ obtained by using MATLAB $^{©}$ are the same as those given by the analytical solutions (2.7.57). The optimal control and state are plotted (using MATLAB $^{©}$ ) in Figure 2.11.

Next, we consider the fixed-final time and free-final state case (Fig-

![](image/19bbe4baedd313d09177d53f03f053592ccdf2c755f86a52b7fdc5d4ef9151b1.jpg)

<details>
<summary>line</summary>

| t | x₁(t) | x₂(t) | u(t) |
| --- | --- | --- | --- |
| 0.0 | 2.0 | 1.0 | -4.0 |
| 0.2 | 1.5 | 0.8 | -3.0 |
| 0.4 | 1.2 | 0.6 | -2.0 |
| 0.6 | 1.0 | 0.4 | -1.0 |
| 0.8 | 0.8 | 0.2 | -0.5 |
| 1.0 | 0.6 | 0.0 | -0.2 |
| 1.2 | 0.4 | -0.2 | 0.0 |
| 1.4 | 0.2 | -0.4 | 0.5 |
| 1.6 | 0.0 | -0.6 | 1.0 |
| 1.8 | -0.2 | -0.8 | 1.5 |
| 2.0 | -0.4 | -1.0 | 2.0 |
</details>

Figure 2.11 Optimal Control and States for Example 2.12

ure 2.9(b), Table 2.1, Type (c)) of the same system.
