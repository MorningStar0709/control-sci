$$
\left[ \begin{array}{c} \mathbf {x} (0) \\ \mathbf {e} (0) \end{array} \right] = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \\ 1 \\ 0 \end{array} \right]
$$

MATLAB Program 10–15 produces the response to the given initial condition. The response curves are shown in Figure 10–21.They seem to be acceptable.

```matlab
MATLAB Program 10–15
% Response to initial condition.
A = [0 1 0;0 0 1;0 -24 -10];
B = [0;10;-80];
K = [1.25 1.25 0.19375];
Kb = [1.25 0.19375];
Ke = [-1;6.25];
Aab = [1 0]; Abb = [0 1;-24 -10];
AA = [A-B*K B*Kb; zeros(2,3) Abb-Ke*Aab];
sys = ss(AA,eye(5),eye(5),eye(5));
t = 0:0.01:8;
x = initial(sys,[1;0;0;1;0],t);
x1 = [1 0 0 0 0]*x';
x2 = [0 1 0 0 0]*x';
x3 = [0 0 1 0 0]*x';
e1 = [0 0 0 1 0]*x';
e2 = [0 0 0 0 1]*x';
subplot(3,2,1); plot(t,x1); grid
xlabel('t (sec)'); ylabel('x1')
subplot(3,2,2); plot(t,x2); grid
xlabel('t (sec)'); ylabel('x2')
subplot(3,2,3); plot(t,x3); grid
xlabel('t (sec)'); ylabel('x3')
subplot(3,2,4); plot(t,e1); grid
xlabel('t (sec)'); ylabel('e1')
subplot(3,2,5); plot(t,e2); grid
xlabel('t (sec)'); ylabel('e2') 
```

Figure 10–21

Response to the given initial

$$\text { condition }; x _ {1} (0) = 1,x _ {2} (0) = 0, x _ {3} (0) = 0,e _ {1} (0) = 1, e _ {2} (0) = 0.$$

![](image/5b2e111eb7270bd890f4ad03caa432865b8a47d3b21cefcfea70d269899c6c37.jpg)

Next, we shall check the frequency-response characteristics.The Bode diagram of the open-loop system just designed is shown in Figure 10–22.The phase margin is about 40° and the gain margin is ±q dB.The Bode diagram of the closed-loop system is shown in Figure 10–23. The bandwidth of the system is approximately 3.8 rad/sec.

![](image/ec4e78e14cc6326f6aa1b40ecb2180d3307523162b02c4e651eae9465258f010.jpg)  
Figure 10–22

Bode diagram for the open-loop transfer function of System 2.

Figure 10–23 Bode diagram for the closed-loop transfer function of System 2.   
![](image/668e6712ffeb2b572b4188318aa2970f6ec3cb3f3ea6b82661e5ee8aa36aac0d.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.1 | 0 | 0 |
| 1 | 0 | 0 |
| 10 | -150 | -150 |
| 100 | -60 | -200 |
</details>
