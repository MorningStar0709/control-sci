FS1 = 0;
for l1 = 1:1:5
    gs1 = -[(x1+pi/3-(l1-1)* pi/6)/(pi/12)]^2;
    u1(l1) = exp(gs1);
end 
```

```matlab
for l2 = 1:1:5
    gs2 = -[(x2 + pi/3 - (l2 - 1) * pi/6)/(pi/12)]^2;
    u2(l2) = exp(gs2);
end

for l1 = 1:1:5
    for l2 = 1:1:5
    FS2(5*(l1 - 1) + l2) = u1(l1) * u2(l2);
    FS1 = FS1 + u1(l1) * u2(l2);
    end
end

FS = FS2/(FS1 + 0.001);

for i = 1:1:25
    thta(i,1) = x(i);
end

gama = 5000;
S = gama * s * FS;

for i = 1:1:25
    sys(i) = S(i);
end

function sys = mdlOutputs(t,x,u)
xd = sin(t);
dxd = cos(t);
ddxd = -sin(t);

x1 = u(2);
x2 = u(3);
e = x1 - xd;
de = x2 - dxd;
c = 15;
s = c * e + de;

xi = [x1;x2];

FS1 = 0;
for l1 = 1:1:5
    gs1 = -[(x1 + pi/3 - (l1 - 1) * pi/6)/(pi/12)]^2;
    u1(l1) = exp(gs1);
end

for l2 = 1:1:5
    gs2 = -[(x2 + pi/3 - (l2 - 1) * pi/6)/(pi/12)]^2;
    u2(l2) = exp(gs2);
end

for l1 = 1:1:5
    for l2 = 1:1:5
    FS2(5*(l1 - 1) + l2) = u1(11) * u2(12);
    FS1 = FS1 + u1(11) * u2(12);
    end
end

FS = FS2/(FS1 + 0.001); 
```

```matlab
for i = 1:1:25
    thta(i,1) = x(i);
end
fxp = thta'* FS';
xite = 0.50;
ut = -c* de + ddxd - fxp - xite* sign(s);
sys(1) = ut;
sys(2) = fxp; 
```

(5) 作图程序: chap5\_3plot  
```matlab
close all;

figure(1);
subplot(211);
plot(t,x(:,1),'r',t,x(:,2),'b');
xlabel('time(s)');ylabel('position tracking');
subplot(212);
plot(t,cos(t),'r',t,x(:,3),'b');
xlabel('time(s)');ylabel('speed tracking');

figure(2);
plot(t,f(:,1),'r',t,f(:,3),'b');
xlabel('time(s)');ylabel('f approximation'); 
```
