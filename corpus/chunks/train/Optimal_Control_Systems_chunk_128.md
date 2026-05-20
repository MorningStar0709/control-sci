# 2.7 Variational Approach to Optimal Control Systems

(2.7.58), we have $t_f$ specified to be 2 and hence $\delta t_f$ is zero in the general boundary condition (2.7.32).

Also, since $x_{2}(2)$ is free, $\delta x_{2f}$ is arbitrary and hence the corresponding final condition on the costate becomes

$$\lambda_ {2} (t _ {f}) = \left(\frac {\partial S}{\partial x _ {2}}\right) _ {* t _ {f}} = 0 \tag {2.7.60}$$

(since $S = 0$ ). Thus we have the four boundary conditions as

$$x _ {1} (0) = 1; \quad x _ {2} (0) = 2; \quad x _ {1} (2) = 0; \quad \lambda_ {2} (2) = 0. \tag {2.7.61}$$

With these boundary conditions substituted in (2.7.59), the constants are found to be

$$C _ {1} = 1; \quad C _ {2} = 2; \quad C _ {3} = 1 5 / 8; \quad C _ {4} = 1 5 / 4. \tag {2.7.62}$$

Finally the optimal states, costates and control are given from (2.7.59) and (2.7.62) as

$$
\begin{array}{l} x _ {1} ^ {*} (t) = \frac {5}{1 6} t ^ {3} - \frac {1 5}{8} t ^ {2} + 2 t + 1, \\ x _ {2} ^ {*} (t) = \frac {1 5}{1 6} t ^ {2} - \frac {1 5}{4} t + 2, \\ \lambda_ {1} ^ {*} (t) = \frac {1 5}{8}, \\ \lambda_ {2} ^ {*} (t) = - \frac {1 5}{8} t + \frac {1 5}{4}, \\ u ^ {*} (t) = \frac {1 5}{8} t - \frac {1 5}{4}. \tag {2.7.63} \\ \end{array}
$$

The solution for the set of differential equations (2.7.53) with the boundary conditions (2.7.58) for Example 2.13 using Symbolic Toolbox of the MATLAB $^{©}$ , Version 6, is shown below.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

%% Solution Using Symbolic Toolbox (STB) in

%% MATLAB Version 6.0

%%

S=dsolve('Dx1=x2,Dx2=-lambda2,Dlambda1=0,Dlambda2=-lambda1,

x1(0)=1,x2(0)=2,x1(2)=0,lambda2(2)=0')

S =

```matlab
lambda1: [1x1 sym]
lambda2: [1x1 sym]
x1: [1x1 sym]
x2: [1x1 sym]

S.x1

ans =

5/16*t^3+2*t+1-15/8*t^2

S.x2

ans =

15/16*t^2+2-15/4*t

S.lambda1

ans =

15/8

S.lambda2

ans =

-15/8*t+15/4

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

plot(t1,x1p,'k',t1,x2p,'k',t1,up,'k:')
xlabel('t')
gtext('x_1(t)') 
```
