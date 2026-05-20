D11 = (m1 + m2) * r1^2 + m2 * r2^2 + 2 * m2 * r1 * r2 * cos(q2);
D22 = m2 * r2^2;
D21 = m2 * r2^2 + m2 * r1 * r2 * cos(q2);
D12 = D21;
D = [D11 D12; D21 D22];

C12 = m2 * r1 * sin(q2);
C = [-C12 * dq2 - C12 * (dq1 + dq2); C12 * q1 0];

g1 = (m1 + m2) * r1 * cos(q2) + m2 * r2 * cos(q1 + q2);
g2 = m2 * r2 * cos(q1 + q2);
G = [g1; g2];

qd1 = u(1);
qd2 = u(2);
dqd1 = 0.3 * cos(t);
dqd2 = 0.3 * cos(t);
dqd = [dqd1 dqd2]';
ddqd1 = -0.3 * sin(t);
ddqd2 = -0.3 * sin(t);
ddqd = [ddqd1 ddqd2]';
e1 = q1 - qd1;
e2 = q2 - qd2;
e = [e1 e2]';
de1 = dq1 - dqd1;
de2 = dq2 - dqd2;
de = [de1 de2]';
s = de + Fai * e;

dqr = dqd - Fai * e;
ddqr = ddqd - Fai * de;

for i = 1 : 1 : 5
    thtal(i, 1) = x(i);
end

for i = 1 : 1 : 5
    thta2(i, 1) = x(i + 5); 
```

end

```matlab
fsd1 = 0;
for l1 = 1 : 1 : 5
    gs1 = - [(dq1 + pi / 6 - (l1 - 1) * pi / 12) / (pi / 24)]^2;
    u1(l1) = exp(gs1);
end

fsd2 = 0;
for l2 = 1 : 1 : 5
    gs2 = - [(dq2 + pi / 6 - (l2 - 1) * pi / 12) / (pi / 24)]^2;
    u2(l2) = exp(gs2);
end 
```

```matlab
for l1 = 1 : 1 : 5
    fsu1(l1) = u1(l1);
    fsd1 = fsd1 + u1(l1);
end

for l2 = 1 : 1 : 5
    fsu2(l2) = u2(l2);
    fsd2 = fsd2 + u2(l2);
end

fs1 = fsu1 / (fsd1 + 0.001);
fs2 = fsu2 / (fsd2 + 0.001); 
```

```javascript
Fp(1) = thta1'* fs1';
Fp(2) = thta2'* fs2'; 
```

```matlab
KD = 20* eye(2);
W = [1.5 0; 0 1.5]; 
```

```matlab
tol = D* ddqr + C* dqr + G + 1* Fp' - KD* s - W* sign(s);
sys(1) = tol(1);
sys(2) = tol(2);
sys(3) = Fp(1);
sys(4) = Fp(2); 
```
