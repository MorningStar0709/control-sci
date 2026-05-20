# 2.7 Variational Approach to Optimal Control Systems

(2.7.65) and (2.7.69) as

$$x _ {1} ^ {*} (t) = \frac {4}{5 4} t ^ {3} - \frac {2}{3} t ^ {2} + 2 t + 1,x _ {2} ^ {*} (t) = \frac {4}{1 8} t ^ {2} - \frac {4}{3} t + 2,\lambda_ {1} ^ {*} (t) = \frac {4}{9},\lambda_ {2} ^ {*} (t) = - \frac {4}{9} t + \frac {4}{3},u ^ {*} (t) = \frac {4}{9} t - \frac {4}{3}. \tag {2.7.70}$$

The solution for the set of differential equations (2.7.53) with the boundary conditions (2.7.68) for Example 2.14 using Symbolic Toolbox of the MATLAB $^{©}$ , Version 6 is shown below.

```matlab
**********************************************************************
%% Solution Using Symbolic Toolbox (STB) in
%% of MATLAB Version 6
%%
clear all
S=dsolve('Dx1=x2,Dx2=-lam2,Dlam1=0,Dlam2=-lam1,x1(0)=1,
    x2(0)=2,x1(tf)=3,lam2(tf)=0')
t='tf';
eq1=subs(S.x1)-'x1tf';
eq2=subs(S.x2)-'x2tf';
eq3=S.lam1-'lam1tf';
eq4=subs(S.lam2)-'lam2tf';
eq5='lam1tf*x2tf-0.5*lam2tf^2';
S2=solve(eq1,eq2,eq3,eq4,eq5,'tf,x1tf,x2tf,lam1tf,
    lam2tf','lam1tf<>0')
%% lam1tf<>0 means lam1tf is not equal to 0;
%% This is a condition derived from eq5.
%% Otherwise, without this condition in the above
%% SOLVE routine, we get two values for tf (1 and 3 in this case)
%%
tf=S2.tf
x1tf=S2.x1tf;
x2tf=S2.x2tf;
clear t
x1=subs(S.x1)
x2=subs(S.x2)
lam1=subs(S.lam1) 
```

```matlab
lam2=subs(S.lam2)
%% Convert the symbolic values to
%% numerical values as shown below.
j=1;
tf=double(subs(S2.tf))
%% coverts tf from symbolic to numerical
for tp=0:0.05:tf
t=sym(tp);
%% coverts tp from numerical to symbolic
x1p(j)=double(subs(S.x1));
%% subs substitutes S.x1 to x1p
x2p(j)=double(subs(S.x2));
%% double converts symbolic to numeric
up(j)=-double(subs(S.lam2));
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

The optimal control and states for Example 2.14 are plotted in Figure 2.13.

Finally, we consider the fixed-final time and free-final state system with a terminal cost (Figure 2.9 (b), Table 2.1, Type (b)).
