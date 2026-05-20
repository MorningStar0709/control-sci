x=x';
if n>2
    for i=1:3:(3*fix((n-3)/3)+1)
    figure(fig);
    plot(k1,real(x(:,i)),'b',k1,real(x(:,i+1)),'b',k1,...
    real(x(:,i+2)),'b')
    grid on
    title('Plot of Optimal States')
    xlabel('k')
    ylabel('Optimal States')
    fig=fig+1;
    %
    end
end
if (n-3*fix(n/3))==1
    figure(fig);
    plot(k1,real(x(:,n)),'b')
elseif (n-3*fix(n/3))==2
    figure(fig);
    plot(k1,real(x(:,n-1)),'b',k1,real(x(:,n)),'b')
end
grid on
title('Plot of Optimal States')
xlabel('k')
ylabel('Optimal States')
fig=fig+1;
%
%Plot Optimized u
%
u=u';
if mb>2
    for i=1:3:(3*fix((mb-3)/3)+1)
    figure(fig);
    plot(k1,real(u(:,i)),'b',k1,real(u(:,i+1)),...
'm:',k1,real(u(:,i+2)),'g-.') 
```

C.4 MATLAB $^{©}$ for Discrete-Time Tracking System

```matlab
grid on
title('Plot of Optimal Control')
xlabel('k')
ylabel('Optimal Control')
fig=fig+1;
end
end
if (mb-3*fix(mb/3)==1
    figure(fig);
    plot(k1,real(u(:,mb)),'b')
elseif (mb-3*fix(mb/3)==2
    figure(fig);
    plot(k1,real(u(:,mb-1)),'b',k1,real(u(:,mb)),'m:')
end
grid on
title('Plot of Optimal Control')
xlabel('k')
ylabel('Optimal Control')
gtext('u')
end
%%% 
```
