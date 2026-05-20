```txt
L1 = -pi; L2 = pi;
L = L2 - L1; 
```

```txt
h = pi/2;
N = L/h; 
```

```matlab
for i = 1:N + 1
    e(i) = L1 + L/N* (i - 1);
end 
```

```matlab
% w1
w1 = trimf(x(1), [e(2), e(3), e(4)]); % Rule 1: x1 is to zero 
```

```matlab
% w2, Rule 2: x1 is about +- pi/2, but smaller if x(1) <= 0
    w2 = trimf(x(1), [e(2), e(2), e(3)]);
else
    w2 = trimf(x(1), [e(3), e(4), e(4)]);
end 
```

```matlab
% w3, Rule 3: x1 is about +-pi/2, but bigger if x(1) < 0
    w3 = trimf(x(1), [e(1), e(2), e(2)]);
else
    w3 = trimf(x(1), [e(4), e(4), e(5)]);
end 
```

```matlab
% w4, Rule 4: x1 is about +- pi
if x(1) < 0
    w4 = trimf(x(1), [e(1), e(1), e(2)]);
else
    w4 = trimf(x(1), [e(4), e(5), e(5)]);
end
w1 + w2 + w3 + w4;
ut = (w1* ut1 + w2* ut2 + w3* ut3 + w4* ut4) / (w1 + w2 + w3 + w4); 
```

```txt
sys(1) = ut; 
```

(5) 作图程序: chap4\_10plot.m

close all;

```matlab
figure(1);
plot(t,x(:,1),'r',t,x(:,2),'b');
xlabel('time(s)');ylabel('angle and angle speed response'); 
```

```matlab
figure(2);
plot(t,u(:,1),'r');
xlabel('time(s)');ylabel('control input'); 
```
