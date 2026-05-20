# MATLAB Program 10–29

% Response to initial condition ---- full-order observer

```matlab
A = [0 1;0 -2];
B = [0;4];
C = [1 0];
K = [4 0.5];
Ke = [14;36];
AA = [A-B*K B*K; zeros(2,2) A-Ke*C];
sys = ss(AA, eye(4), eye(4), eye(4));
t = 0:0.01:8;
x = initial(sys, [1;0;1;0],t);
x1 = [1 0 0 0]*x';
x2 = [0 1 0 0]*x';
e1 = [0 0 1 0]*x';
e2 = [0 0 0 1]*x';
subplot(2,2,1); plot(t,x1); grid
xlabel('t (sec)'); ylabel('x1')
subplot(2,2,2); plot(t,x2); grid
xlabel('t (sec)'); ylabel('x2')
subplot(2,2,3); plot(t,e1); grid
xlabel('t (sec)'); ylabel('e1')
subplot(2,2,4); plot(t,e2); grid
xlabel('t (sec)'); ylabel('e2') 
```

![](image/c8189b82c3790525eec8720ce98a36438850418a839637a92974caed5a39bd7d.jpg)

<details>
<summary>line</summary>

| t (sec) | x₁ |
| --- | --- |
| 0 | 1.0000 |
| 1 | -0.2500 |
| 2 | 0.0000 |
| 3 | 0.0000 |
| 4 | 0.0000 |
| 5 | 0.0000 |
| 6 | 0.0000 |
| 7 | 0.0000 |
| 8 | 0.0000 |
</details>

![](image/e8144c914d231815f8c6c12633046754fa6c710e584c89746b86df7c4f89d705.jpg)

<details>
<summary>line</summary>

| t (sec) | x₂ |
| --- | --- |
| 0 | -2.8 |
| 1 | 0.5 |
| 2 | 0.0 |
| 4 | 0.0 |
| 6 | 0.0 |
| 8 | 0.0 |
</details>

![](image/abae0b75f1e034ab59345a0cfe46216af200270d92c276c4f2e6cc53da14eb53.jpg)

<details>
<summary>line</summary>

| t (sec) | e1 |
| --- | --- |
| 0 | 1.2 |
| 1 | 0.0 |
| 2 | 0.0 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
</details>

![](image/2c61dc59bbe34ba3e83e501bbaf1b0bd50553755c46ce39d40e738d8824b69b2.jpg)

<details>
<summary>line</summary>

| t (sec) | e² |
| --- | --- |
| 0 | -1.5 |
| 1 | -0.5 |
| 2 | 0 |
| 4 | 0 |
| 6 | 0 |
| 8 | 0 |
</details>

Figure 10–52 Response curves to initial condition.

To obtain the transfer function of the observer controller, we use MATLAB. MATLAB Program 10–30 produces this transfer function. The result is

$$\frac {\mathrm{num}}{\mathrm{den}} = \frac {7 4 s + 2 5 6}{s ^ {2} + 1 8 s + 1 0 8} = \frac {7 4 (s + 3 . 4 5 9 5)}{(s + 9 + j 5 . 1 9 6 2) (s + 9 - j 5 . 1 9 6 2)}$$

<table><tr><td>MATLAB Program 10-30</td></tr><tr><td>% Determination of transfer function of observer controller ---- full-order observer</td></tr><tr><td>A = [0 1;0 -2];</td></tr><tr><td>B = [0;4];</td></tr><tr><td>C = [1 0];</td></tr><tr><td>K = [4 0.5];</td></tr><tr><td>Ke = [14;36];</td></tr><tr><td>[num,den] = ss2tf(A-Ke*C-B*K, Ke,K,0)</td></tr><tr><td>num =</td></tr><tr><td>0 74.0000 256.0000</td></tr><tr><td>den =</td></tr><tr><td>1 18 108</td></tr></table>
