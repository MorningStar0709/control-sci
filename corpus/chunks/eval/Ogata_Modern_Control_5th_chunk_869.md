MATLAB Program 10–35 gives the unit-step response of the system given by Equation (10–179). The resulting response curves are presented in Figure 10–55. It shows response curves# $\theta \left[ = x _ { 1 } ( t ) \right]$ versus $t , \dot { \theta } [ = \dot { x } _ { 2 } ( t ) \bar { ( t ) } ]$ versus t, $, y \left[ = x _ { 3 } ( t ) \right]$ versus $t , \dot { y } \big [ = x _ { 4 } ( t ) \big ]$ versus t, andD $\xi \left[ = x _ { 5 } ( t ) \right]$ versus t, where the input $r ( t )$ to the cart is a unit-step function $[ r ( t ) = 1 \mathrm { m } ]$ All initial conditions are set equal. to zero. Figure 10–56 is an enlarged version of the cart position $y \left[ = x _ { 3 } ( t ) \right]$ versus t. The cart moves backward a very small amount for the first 0.6 sec or so. (Notice that the cart velocity is negative for the first 0.4 sec.) This is due to the fact that the inverted-pendulum-on-the-cart system is a nonminimum-phase system.

```matlab
MATLAB Program 10–35
% Unit-step response
A = [0 1 0 0;20.601 0 0 0;0 0 0 1;-0.4905 0 0 0];
B = [0;-1;0;0.5];
C = [0 0 1 0];
D = [0];
K = [-188.0799 -37.0738 -26.6767 -30.5824];
kl = -10.0000;
AA = [A-B*K B*kl; -C 0];
BB = [0;0;0;0;1];
CC = [C 0];
DD = D;
t = 0:0.01:10;
[y,x,t] = step(AA,BB,CC,DD,1,t);
x1 = [1 0 0 0 0]*x';
x2 = [0 1 0 0 0]*x';
x3 = [0 0 1 0 0]*x';
x4 = [0 0 0 1 0]*x';
x5 = [0 0 0 0 1]*x';
subplot(3,2,1); plot(t,x1); grid;
xlabel('t (sec)'); ylabel('x1')
subplot(3,2,2); plot(t,x2); grid;
xlabel('t (sec)'); ylabel('x2')
subplot(3,2,3); plot(t,x3); grid;
xlabel('t (sec)'); ylabel('x3')
subplot(3,2,4); plot(t,x4); grid;
xlabel('t (sec)'); ylabel('x4')
subplot(3,2,5); plot(t,x5); grid;
xlabel('t (sec)'); ylabel('x5') 
```

Comparing the step-response characteristics of this system with those of Example 10–5, we notice that the response of the present system is less oscillatory and exhibits less maximum overshoot in the position response $\left( x _ { 3 } \right.$ versus tB. The system designed by use of the quadratic optimal regulator approach generally gives such characteristics—less oscillatory and well damped.

![](image/13d32a468f37dd7df591860faca678dc64f16ea17471c13cd46b07042ac3a85f.jpg)

<details>
<summary>line</summary>

| t (sec) | x₁ |
| --- | --- |
| 0 | 0.0000 |
| 1 | 0.0250 |
| 2 | 0.0100 |
| 3 | -0.0150 |
| 4 | -0.0180 |
| 5 | -0.0120 |
| 6 | -0.0050 |
| 7 | 0.0000 |
| 8 | 0.0020 |
| 9 | 0.0030 |
| 10 | 0.0035 |
</details>

![](image/efa758b25fd9e53f190225dd63ef25d8507be34c7b4201d0265351fcd1d996b6.jpg)
