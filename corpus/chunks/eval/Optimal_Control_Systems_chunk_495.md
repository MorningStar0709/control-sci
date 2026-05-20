C.1 MATLAB© for Matrix Differential Riccati Equation

```matlab
u(:,i)=us';
us=0;
j=1;
end
%
%Provide final steady-state K
%
P=W21/W11;
K=real(inv(R)*B'*P);
%
%Plotting Section, if desired
%
if plotflag~=1
%
%Plot diagonal Riccati coefficients using a
% flag variable to hold and change colors
%
fig=1; %Figure number
cflag=1; %Variable used to change plot color
j=1;
Ps=0.; %Initialize P matrix plot variable
for i=1:1:n*n
    for t1a=t0:.1:tf
    Tt=-inv(W22-F*W12)*(W21-F*W11);
    P=real((W21+W22*expm(-Md*(tf-t1a))*Tt*expm(-Md*...
(tf-t1a)))*inv(W11+W12*expm(-Md*(tf-t1a))*Tt...
*expm(-Md*(tf-t1a)));
    Ps(j)=P(i);
    t1(j)=t1a;
    j=j+1;
    end
    if cflag==1;
    figure(fig)
    plot(t1,Ps,'b')
    title('Plot of Riccati Coefficients')
    xlabel('t')
    ylabel('P Matrix')
    hold
    cflag=2; 
```

```matlab
elseif cflag==2
    plot(t1, Ps, 'm:')
    cflag=3;
elseif cflag==3
    plot(t1, Ps, 'g-.')
    cflag=4;
elseif cflag==4
    plot(t1, Ps, 'r--')
    cflag=1;
    fig=fig+1;
end

Ps=0.;
j=1;
end

if cflag==2|cflag==3|cflag==4
    hold
    fig=fig+1;
end

%
%Plot Optimized x
%
if n>2
    for i=1:3:(3*fix((n-3)/3)+1)
    figure(fig);
    plot(tx, real(x(:,i)), 'b', tx, real(x(:,i+1)), 'm:', tx, ...
    real(x(:,i+2)), 'g-.')
    title('Plot of Optimized x')
    xlabel('t')
    ylabel('x vectors')
    fig=fig+1;
end

end

if (n-3*fix(n/3))==1
    figure(fig);
    plot(tx, real(x(:,n)), 'b')
elseif (n-3*fix(n/3))==2
    figure(fig);
    plot(tx, real(x(:,n-1)), 'b', tx, real(x(:,n)), 'm:')
end 
```

C.1 MATLAB $^{©}$ for Matrix Differential Riccati Equation

```matlab
title('Plot of Optimized x')
xlabel('t')
ylabel('x vectors')
fig=fig+1;
%
%Plot Optimized u
%
if mb>2
    for i=1:3:(3*fix((mb-3)/3)+1)
    figure(fig);
    plot(tu,real(u(:,i)),'b',tu,real(u(:,i+1)),'m:',...
tu,real(u(:,i+2)),'g-.')
    title('Plot of Optimized u')
    xlabel('t')
    ylabel('u vectors')
    fig=fig+1;
%
end
end
if (mb-3*fix(mb/3)==1
    figure(fig);
    plot(tu,real(u(:,mb)),'b')
elseif (mb-3*fix(mb/3)==2
    figure(fig);
    plot(tu,real(u(:,mb-1)),'b',tu,real(u(:,mb)),'m:')
end
title('Plot of Optimized u')
xlabel('t')
ylabel('u vectors')
%
end
%%
%%% 
```
