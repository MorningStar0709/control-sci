# MATLAB Program 10–32

% Response to intial condition ---- minimum-order observer

```matlab
A = [0 1;0 -2];
B = [0;4];
K = [4 0.5];
Kb = 0.5;
Ke = 6;
Aab = 1; Abb = -2;
AA = [A-B*K B*Kb; zeros(1,2) Abb-Ke*Aab];
sys = ss(AA,eye(3),eye(3),eye(3));
t = 0:0.01:8;
x = initial(sys,[1;0;1],t);
x1 = [1 0 0]*x';
x2 = [0 1 0]*x';
e = [0 0 1]*x';
subplot(2,2,1); plot(t,x1); grid
xlabel('t (sec)'); ylabel('x1')
subplot(2,2,2); plot(t,x2); grid
xlabel('t (sec)'); ylabel('x2')
subplot(2,2,3); plot(t,e); grid
xlabel('t (sec)'); ylabel('e') 
```

![](image/f3122f4c12844a511fc784577f20d41fb3e8fde01cc07a691adf683f5c887063.jpg)

<details>
<summary>line</summary>

| t (sec) | x₁ |
| --- | --- |
| 0 | 1.0 |
| 1 | -0.2 |
| 2 | 0.0 |
| 4 | 0.0 |
| 6 | 0.0 |
| 8 | 0.0 |
</details>

![](image/b90109b2ee1ca751db94f06b5dc1515589e5ff2b4c39df55d804737727b95e71.jpg)

<details>
<summary>line</summary>

| t (sec) | x₂ |
| --- | --- |
| 0 | -2.2 |
| 1 | 0.4 |
| 2 | 0.0 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
</details>

![](image/42711834c532914fe7c7140f1d1ad3c6ef661c6d7122e670e8421223bdaf0273.jpg)

<details>
<summary>line</summary>

| t (sec) | e |
| --- | --- |
| 0 | 0.9 |
| 1 | 0.1 |
| 2 | 0.05 |
| 3 | 0.02 |
| 4 | 0.01 |
| 5 | 0.005 |
| 6 | 0.002 |
| 7 | 0.001 |
| 8 | 0.0005 |
</details>

Figure 10–53   
Response curves to initial condition.

The transfer function of the observer controller, when the system uses the minimum-order observer, can be obtained by use of MATLAB Program 10–33. The result is

$$\frac {\text { num }}{\text { den }} = \frac {7 s + 3 2}{s + 1 0} = \frac {7 (s + 4 . 5 7 1 4)}{s + 1 0}$$

MATLAB Program 10–33   
% Determination of transfer function of observer controller ---- minimum-order observer
A = [0 1;0 -2];
B = [0;4];
Aaa = 0; Aab = 1; Aba = 0; Abb = -2;
Ba = 0; Bb = 4;
Ka = 4; Kb = 0.5;
Ke = 6;
Ahat = Abb - Ke*Aab;
Bhat = Ahat*Ke + Aba - Ke*Aaa;
Fhat = Bb - Ke*Ba;
Atilde = Ahat - Fhat*Kb;
Btilde = Bhat - Fhat*(Ka + Kb*Ke);
Ctilde = -Kb;
Dtilde = -(Ka + Kb*Ke);
[num,den] = ss2tf(Atilde, Btilde, -Ctilde, -Dtilde)
num =
7 32
den =
1 10

Figure 10–54 Bode diagrams of System 1 (system with full-order observer) and System 2 (system with minimumorder observer). System 1= (296s+1024) $( s ^ { 4 } + 2 0 s ^ { 3 } + 1 4 4 s ^ { 2 }$ +512s+1024); $\mathrm { S y s t e m } 2 = \ : ( 2 8 s + 1 2 8 ) /$ $( s ^ { 3 } + 1 2 s ^ { 2 } + 4 8 s + 1 2 8 ) .$   
![](image/06e6f8d49c4900d16e96427d89b80eb7249909566f022d5e95c9ca7e8a28a0e7.jpg)

<details>
<summary>line</summary>
