<details>
<summary>line</summary>

| time-s | response |
| --- | --- |
| 0 | -0.25 |
| 10 | 0.05 |
| 20 | 0.04 |
| 30 | 0.01 |
| 40 | 0.00 |
| 50 | 0.00 |
| 60 | 0.00 |
</details>

(b)   
图12-3 状态响应曲线及控制输入响应曲线

所以根据实际的系统允许,应该适当选择 Q 和 R。

$$
\% * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
\mathrm{a} = \left[ \begin{array}{l l l l l l l l} 0 & 1 & 0; 0 & 0 & 1; 0 & 0 & - 1 / 2 \end{array} \right]; \mathrm{b} = \left[ \begin{array}{l l l l l l l l} 0; 0; 1 / 2 \end{array} \right]; \mathrm{c} = \left[ \begin{array}{l l l l l l l l} 1 & 0 & 0; 0 & 1 & 0; 0 & 0 & 1 \end{array} \right];
\mathrm{d} = [ 0; 0; 0 ];
$$

figure(1)

$$
\mathbf {q} = \left[ \begin{array}{l l l l l l l l} 1 & 0 & 0; 0 & 0 & 0; 0 & 0 & 0 \end{array} \right];
\mathbf {r} = 2;[ \mathbf {k}, \mathbf {p}, \mathbf {e} ] = \operatorname{lqr} (\mathbf {a}, \mathbf {b}, \mathbf {q}, \mathbf {r})\mathrm{x} 0 = [ 1 0; 0; 0 ];\mathbf {a} \mathbf {1} = \mathbf {a} - \mathbf {b} * \mathbf {k};[ \mathrm{y}, \mathrm{x} ] = \text { initial } (\mathrm{a1,b,c,d,x0,20});\mathrm{n} = \text { length } (\mathrm{x} (:, 3));
$$

![](image/e3ea022f1f34aa72695bee4dbad8c3b50d162161066ed56140d9a28d9cda7ea3.jpg)

<details>
<summary>line</summary>

| time-s | x1 | x2 | x3 |
| --- | --- | --- | --- |
| 0 | 10.0 | 0.0 | 0.0 |
| 2 | 5.0 | -3.0 | -2.0 |
| 4 | 0.0 | -1.0 | 2.0 |
| 6 | 0.0 | 0.0 | 0.0 |
| 8 | 0.0 | 0.0 | 0.0 |
| 10 | 0.0 | 0.0 | 0.0 |
| 12 | 0.0 | 0.0 | 0.0 |
| 14 | 0.0 | 0.0 | 0.0 |
| 16 | 0.0 | 0.0 | 0.0 |
| 18 | 0.0 | 0.0 | 0.0 |
| 20 | 0.0 | 0.0 | 0.0 |
</details>

(a)   
![](image/faaa5713731eba89a1fb23a28a7804c2535219ea82d8a971707dbca72eff2b25.jpg)

<details>
<summary>line</summary>

| time-s | response |
| --- | --- |
| 0 | -25 |
| 2 | 5 |
| 4 | 0 |
| 6 | -1 |
| 8 | 0 |
| 10 | 0 |
| 12 | 0 |
| 14 | 0 |
| 16 | 0 |
| 18 | 0 |
| 20 | 0 |
</details>

(b)

图12-4 状态响应曲线及控制输入响应曲线  
```matlab
T = 0:20/n:20 - 20/n;
plot(T, x(:,1), 'black', T, x(:,2), 'red', T, x(:,3), 'green');
xlabel('time - s'); ylabel('response');
title('图(1.a) Q = diag(1,0,0), R = 2时状态响应曲线')
grid, hold on
for j = 1:n
    u(j,:) = -k * (x(j,:))';
end
figure(2)
plot(T,u); xlabel('time - s'); ylabel('response');
title('图(1.b) Q = diag(1,0,0), R = 2时控制输入u的响应曲线')
grid, hold on 
```

![](image/484794cfefc82e1369bd0e2d1089fc6fcb3adc38b62df38ef3d33dcd9cc21c69.jpg)

<details>
<summary>line</summary>

| time-s | x1 | x2 | x3 |
| --- | --- | --- | --- |
| 0 | 10.0 | -1.0 | 0.0 |
| 5 | 6.0 | -0.5 | 0.0 |
| 10 | 4.0 | -0.2 | 0.0 |
| 15 | 2.5 | 0.0 | 0.0 |
| 20 | 1.5 | 0.0 | 0.0 |
| 25 | 1.0 | 0.0 | 0.0 |
| 30 | 0.5 | 0.0 | 0.0 |
| 35 | 0.2 | 0.0 | 0.0 |
| 40 | 0.1 | 0.0 | 0.0 |
| 45 | 0.05 | 0.0 | 0.0 |
| 50 | 0.0 | 0.0 | 0.0 |
</details>

(a)
