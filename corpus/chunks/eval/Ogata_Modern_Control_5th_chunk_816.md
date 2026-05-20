# MATLAB Program 10–21

% Response to initial condition.

```matlab
A = [0 1 0;0 0 0 1;-35 -27 -9];
B = [0;0;1];
K = [0.0143 0.1107 0.0676];
sys = ss(A-B*K, eye(3),eye(3),eye(3));
t = 0:0.01:8;
x = initial(sys,[1;0;0],t);
x1 = [1 0 0]*x';
x2 = [0 1 0]*x';
X3 = [0 0 1]*x';
subplot(2,2,1); plot(t,x1); grid
xlabel('t (sec)'); ylabel('x1')
subplot(2,2,2); plot(t,x2); grid
xlabel('t (sec)'); ylabel('x2)
subplot(2,2,3); plot(t,x3); grid
xlabel('t (sec)'); ylabel('x3') 
```

EXAMPLE 10–13 Consider the system shown in Figure 10–39. The plant is defined by the following state-space equations:

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x} + D u$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & - 2 & - 3 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {C} = [ 1 \quad 0 \quad 0 ], \quad D = [ 0 ]
$$

The control signal u is given by

$$u = k _ {1} \left(r - x _ {1}\right) - \left(k _ {2} x _ {2} + k _ {3} x _ {3}\right) = k _ {1} r - \left(k _ {1} x _ {1} + k _ {2} x _ {2} + k _ {3} x _ {3}\right)$$

Figure 10–38 Response curves to initial condition.   
![](image/11a4cbcf3a6645d6c806031a096d0f03c0c78c1ea747d256a1c96cf210784acc.jpg)

<details>
<summary>line</summary>

| t (sec) | x₁ |
| --- | --- |
| 0 | 1.0 |
| 1 | 0.4 |
| 2 | 0.0 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
</details>

![](image/95344830b6cf099c444b511effe415bd8722edcb34fdbad1ad9912c198f4a93a.jpg)

<details>
<summary>line</summary>

| t (sec) | x₂ |
| --- | --- |
| 0 | 0.2 |
| 1 | -1.0 |
| 2 | 0.0 |
| 4 | 0.0 |
| 6 | 0.0 |
| 8 | 0.0 |
</details>

![](image/294c38d18927226bc33bcb158431aaf1ea67b0125f32b9f752556aca66003e20.jpg)

<details>
<summary>line</summary>

| t (sec) | x₃ |
| --- | --- |
| 0 | -2.8 |
| 1 | 1.0 |
| 2 | 0.0 |
| 4 | 0.0 |
| 6 | 0.0 |
| 8 | 0.0 |
</details>

In determining an optimal control law, we assume that the input is zero, or $r = 0 .$ Let us determine the state-feedback gain matrix K, where

$$
\mathbf {K} = \left[ \begin{array}{c c c} k _ {1} & k _ {2} & k _ {3} \end{array} \right]
$$

such that the following performance index is minimized:

$$J = \int_ {0} ^ {\infty} \left(\mathbf {x} ^ {\prime} \mathbf {Q x} + u ^ {\prime} R u\right) d t$$

where
