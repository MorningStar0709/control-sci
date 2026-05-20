```matlab
for j=1:1:m
    h(j)=exp(-norm(x-c(:,j))^2/(2*bj^2));
end

ym(k)=w'*h';
em(k)=y(k)-ym(k);

d_w=xite*em(k)*h';
w=w_1+d_w+alfa*(w_1-w_2);

y_1=y(k);
w_2=w_1;w_1=w;

x1(k)=x(1);
for j=1:1:m
    H(j,k)=h(j);
end

if k==5000
    figure(1);
    for j=1:1:m
    plot(x1,H(j,:), 'linewidth',2);
    hold on;
    end
    xlabel('Input value of Redial Basis Function');ylabel('Membership function degree');
end
end

figure(2);
subplot(211);
plot(time,y,'r',time,ym,'b:','linewidth',2);
xlabel('time(s)');ylabel('y and ym');
legend('Ideal value','Approximation value');
subplot(212);
plot(time,y-ym,'r','linewidth',2);
xlabel('time(s)');ylabel('Approximation error'); 
```
