```matlab
kp(k) = kp0 + k_pid(1);
ki(k) = ki0 + k_pid(2);
u(k) = kp(k) * e_1 + ki(k) * ei;

y(k) = -den(2) * y_1 - den(3) * y_2 + num(2) * u_1 + num(3) * u_2;
e(k) = r(k) - y(k);
% % % % % % % % % % % Return of parameters % % % % % % % % % % % % u_2 = u_1; u_1 = u(k);
y_2 = y_1; y_1 = y(k);

ei = ei + e(k) * ts;    % Calculating I

ec(k) = e(k) - e_1;
e_1 = e(k);
ec_1 = ec(k);
end

figure(1);
plot(time, r, 'r', time, y, 'b:', 'linewidth', 2);
xlabel('time(s)'); ylabel('r, y');
legend('Ideal position', 'Practical position');
figure(2);
subplot(211);
plot(time, kp, 'r', 'linewidth', 2);
xlabel('time(s)'); ylabel('kp');
subplot(212);
plot(time, ki, 'r', 'linewidth', 2);
xlabel('time(s)'); ylabel('ki');
figure(3);
plot(time, u, 'r', 'linewidth', 2);
xlabel('time(s)'); ylabel('Control input'); 
```

Sugeno 模糊模型的设计: chap4\_8. m   
```matlab
% Sugeno type fuzzy model
clear all;
close all;
ts2 = newfis('ts2', 'sugeno');
ts2 = addvar(ts2, 'input', 'X', [0 5]);
ts2 = addmf(ts2, 'input', 1, 'little', 'gaussmf', [1.8 0]);
ts2 = addmf(ts2, 'input', 1, 'big', 'gaussmf', [1.8 5]);

ts2 = addvar(ts2, 'input', 'Y', [0 10]);
ts2 = addmf(ts2, 'input', 2, 'little', 'gaussmf', [4.4 0]);
ts2 = addmf(ts2, 'input', 2, 'big', 'gaussmf', [4.4 10]);

ts2 = addvar(ts2, 'output', 'Z', [-3 15]);
ts2 = addmf(ts2, 'output', 1, 'first area', 'linear', [-1 1 - 3]);
ts2 = addmf(ts2, 'output', 1, 'second area', 'linear', [1 1 1]);
ts2 = addmf(ts2, 'output', 1, 'third area', 'linear', [0 - 2 2]);
ts2 = addmf(ts2, 'output', 1, 'fourth area', 'linear', [2 1 - 6]); 
```

```matlab
rulelist = [1 1 1 1 1;
    1 2 2 1 1;
    2 1 3 1 1;
    2 2 4 1 1];
ts2 = addrule(ts2, rulelist);
showrule(ts2);

figure(1);
subplot 211;
plotmf(ts2, 'input', 1);
xlabel('x'), ylabel('MF Degree of input 1');
subplot 212;
plotmf(ts2, 'input', 2);
xlabel('x'), ylabel('MF Degree of input 2');

figure(2);
gensurf(ts2);
xlabel('x'), ylabel('y'), zlabel('z'); 
```
