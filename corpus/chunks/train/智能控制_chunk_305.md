# 本章附录（程序代码）

一维函数逼近仿真程序: chap5\_1.m  
```matlab
% Fuzzy approaching
clear all;
close all;

L1 = -3; L2 = 3;
L = L2 - L1;

h = 0.2;
N = L/h + 1;
T = 0.01;

x = L1 : T : L2;
for i = 1 : N
    e(i) = L1 + L / (N - 1) * (i - 1);
end

c = 0; d = 0;
for j = 1 : N
    if j == 1
    u = trimf(x, [e(1), e(1), e(2)]); % The first MF
    elseif j == N
    u = trimf(x, [e(N - 1), e(N), e(N)]); % The last MF
    else
    u = trimf(x, [e(j - 1), e(j), e(j + 1)]);
    end
    hold on;
    plot(x, u);
    c = c + sin(e(j)) * u;
    d = d + u;
end

xlabel('x'); ylabel('Membership function');

for k = 1 : L/T + 1
    f(k) = c(k)/d(k);
end

y = sin(x);
figure(2);
plot(x, f, 'b', x, y, 'r');
xlabel('x'); ylabel('Approaching');
figure(3);
plot(x, f - y, 'r');
xlabel('x'); ylabel('Approaching error'); 
```

二维函数逼近仿真程序: chap5\_2.m  
```txt
% Fuzzy approaching clear all; 
```

close all;   
```matlab
T = 0.1;
x1 = -1 : T : 1;
x2 = -1 : T : 1; 
```

```matlab
L = 2;
h = 0.2;
N = L/h + 1; 
```

```matlab
for i = 1 : 1 : N % N MF
    for j = 1 : 1 : N
    e1(i) = -1 + L / (N - 1) * (i - 1);
    e2(j) = -1 + L / (N - 1) * (j - 1);
    gx(i, j) = 0.52 + 0.1 * e1(i)^3 + 0.28 * e2(j)^3 - 0.06 * e1(i) * e2(j);
    end
end 
```

```matlab
df = zeros(L/T+1,L/T+1);
cf = zeros(L/T+1,L/T+1);
for m=1:1:N % ul change from 1 to N
    if m==1
    u1=trimf(x1,-1,-1,-1+L/(N-1)); % First ul
    elseif m==N
    u1=trimf(x1,[1-L/(N-1),1,1]); % Last ul
    else
    u1=trimf(x1,[e1(m-1),e1(m),e1(m+1)]);
    end
figure(1);
hold on;
plot(x1,u1);
xlabel('x1');ylabel('Membership function'); 
```

```matlab
for n = 1 : 1 : N % u2 change from 1 to N
    if n == 1
    u2 = trimf(x2, [-1, -1, -1 + L/(N-1)]; % First u2
    elseif n == N
    u2 = trimf(x2, [1 - L/(N-1), 1, 1]); % Last u2
    else
    u2 = trimf(x2, [e2(n-1), e2(n), e2(n+1)]);
    end
    figure(2);
    hold on;
    plot(x2, u2);
    xlabel('x2'); ylabel('Membership function'); 
```

```matlab
for i = 1:1:L/T+1
    for j = 1:1:L/T+1
    d = df(i,j) + u1(i)*u2(j);
    df(i,j) = d;
    c = cf(i,j) + gx(m,n)*u1(i)*u2(j); 
```

```matlab
cf(i,j) = c;
end
end
end
end

% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %
for i = 1:1:L/T+1
    for j = 1:1:L/T+1
    f(i,j) = cf(i,j)/df(i,j);
    y(i,j) = 0.52 + 0.1 * x1(i)^3 + 0.28 * x2(j)^3 - 0.06 * x1(i) * x2(j);
    end
end
figure(3);
subplot(211);
surf(x1,x2,f);
title('f(x)');
subplot(212);
surf(x1,x2,y);
title('g(x)');
figure(4);
surf(x1,x2,f-y);
title('Approaching error'); 
```
