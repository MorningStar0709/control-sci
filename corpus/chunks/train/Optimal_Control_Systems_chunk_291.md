# 5.4 Steady-State Regulator System

```matlab
%
for k=1:N,
    xk = [x1(k);x2(k)];
    u(k) = -L*xk;
end
%
k=0:10;
plot(k,x1,'k:o',k,x2,'k:+')
xlabel('k')
ylabel('Optimal States')
gtext('x_1(k)')
gtext('x_2(k)')
plot(k,u,'k:*')
xlabel('k')
ylabel('Optimal Control')
gtext('u(k)')
%
% end of the program
% 
```

Note that the value obtained for P previously is the same as the steady-state value for the Example 5.3 (see Figure 5.3). The optimal states are shown in Figure 5.7 and the optimal control is shown in Figure 5.8.
