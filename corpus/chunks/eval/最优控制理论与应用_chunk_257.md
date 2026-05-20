![](image/c7b8877b9b890d13fa62101b52a9aef6b84056ba318b3b9fda1a3c9a950d11c5.jpg)

<details>
<summary>line</summary>

| time-s | response |
| --- | --- |
| 0 | 1.0 |
| 5 | 0.0 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
| 35 | 0.0 |
| 40 | 0.0 |
| 45 | 0.0 |
| 50 | 0.0 |
</details>

(b)

图12-5 状态响应曲线及控制输入响应曲线  
```matlab
% * * * * * * * * * * * * * * * * * * * * * * * * * * * *
figure(3)
qa = [1 0 0; 0 0 0; 0 0 0];
ra = 2 000;
[ka, pa, ea] = lqr(a, b, qa, ra)
x0 = [10; 0; 0];
aal = a - b * ka;
[ya, xa] = initial(aa1, b, c, d, x0, 60);
na = length(xa(:, 3));
Ta = 0:60/na:60 - 60/na;
plot(Ta, xa(:, 1), 'black', Ta, xa(:, 2), 'red', Ta, xa(:, 3), 'green');
xlabel('time - s'); ylabel('response');
title('图(2. a) Q = diag(1, 0, 0), R = 2 000 时状态响应曲线') 
```

```matlab
grid, hold on
for j = 1:na
    ua(j,:) = -ka * (xa(j,:))';
end
figure(4)
plot(Ta, ua); xlabel('time-s'); ylabel('response');
title('图(2.b) Q = diag(1,0,0), R = 2000时控制输入u的响应曲线')
grid, hold on
% % % * * * * * * * * * * * * * * * * * * * * * * * * * *
figure(5)
qb = [10 0 0; 0 0 0; 0 0 0];
rb = 2;
[kb, pb, eb] = lqr(a, b, qb, rb)
x0 = [10; 0; 0];
ab1 = a - b * kb;
[yb, xb] = initial(ab1, b, c, d, x0, 20);
nb = length(xb(:,3));
Tb = 0:20 / nb:20 - 20 / nb;
plot(Tb, xb(:,1), 'black', Tb, xb(:,2), 'red', Tb, xb(:,3), 'green');
xlabel('time-s'); ylabel('response');
title('图(3.a) Q = diag(10,0,0), R = 2时状态响应曲线')
grid, hold on
for j = 1:nb
    ub(j,:) = -kb * (xb(j,:))';
end
figure(6)
plot(Tb, ub); xlabel('time-s'); ylabel('response');
title('图(3.b) Q = diag(10,0,0), R = 2时控制输入u的响应曲线')
grid, hold on
% % % * * * * * * * * * * * *
figure(7)
qc = [1 0 0; 0 100 0; 0 0 0];
rc = 2;
[kc, pc, ec] = lqr(a, b, qc, rc)
x0 = [10; 0; 0]; 
```

```matlab
ac1 = a - b * kc;
[yc, xc] = initial(ac1, b, c, d, x0, 50);
nc = length(xc(:, 3));
Tc = 0:50/nc:50 - 50/nc;
plot(Tc, xc(:, 1), 'black', Tc, xc(:, 2), 'red', Tc, xc(:, 3), 'green');
xlabel('time - s'); ylabel('response');
title('图(4. a) Q = diag(1, 100, 0), R = 2 时状态响应曲线')
grid, hold on
for j = 1:nc
    uc(j,:) = -kc * (xc(j,:))';
end
figure(8)
plot(Tc, uc); xlabel('time - s'); ylabel('response');
title('图(4. b) Q = diag(1, 100, 0), R = 2 时控制输入 u 的响应曲线')
grid, hold on 
```
