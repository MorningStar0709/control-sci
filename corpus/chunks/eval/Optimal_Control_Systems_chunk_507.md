# C.4 MATLAB $^{©}$ for Discrete-Time Tracking System

```matlab
ylabel('Vector coefficients')
gtext('g_{1}(k)')
gtext('g_{2}(k)')
%
k=0:1:kf;
figure(3)
plot(k,x1,'k:o',k,x2,'k:+')
grid
xlabel('k')
ylabel('Optimal States')
gtext('x_1(k)')
gtext('x_2(k)')
%
figure(4)
k=0:1:kf-1;
plot(k,u,'k:*')
grid
xlabel('k')
ylabel('Optimal Control')
gtext('u(k)')
%
% end of the program
% 
```
