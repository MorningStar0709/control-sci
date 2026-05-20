# EXAMPLE 9.1 Nonlinear actuator

Consider the system with a nonlinear valve in Example 1.4. The nonlinearity is assumed to be

$$v = f (u) = u ^ {4} \quad u \geq 0$$

Let $\hat{f}^{-1}$ be an approximation of the inverse of the valve characteristic. To compensate for the nonlinearity, the output of the controller is fed through this function before it is applied to the valve (see Fig. 9.2). This gives the relation

$$v = f (u) = f \left(\hat {f} ^ {- 1} (c)\right)$$

where c is the output of the PI controller. The function $f(\hat{f}^{-1}(c))$ should have less variation in gain than f. If $\hat{f}^{-1}$ is the exact inverse, then v = c.

Assume that $f(u) = u^{4}$ is approximated by two lines (see Fig. 9.3): one connecting the points $(0, 0)$ and $(1.3, 3)$ and the other connecting $(1.3, 3)$ and

![](image/ce70713b17c96545b1146bc46c9c558eb1a4011edce68770165f18f73d079487.jpg)

<details>
<summary>line</summary>

| Time | f(u) | f̂(u) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0.5 | ~1 | ~1 |
| 1 | ~2 | ~2 |
| 1.5 | ~6 | ~8 |
| 2 | ~14 | ~16 |
</details>

Figure 9.3 The nonlinear valve characteristic $v = f(u) = u^{4}$ and a two-line approximation $\hat{f}(u)$ .

![](image/8e37920868f3897b8a3f5e5a9fa5d2dd8e7a68ab3e684aba8d1b975ff63e63dc.jpg)  
Figure 9.4 Simulation of the system in Example 9.1 with nonlinear valve and compensation using an approximation of the valve characteristic. Compare Fig. 1.9.

(2, 16). Then

$$
\hat {f} ^ {- 1} (c) = \left\{ \begin{array}{l l} 0. 4 3 3 c & \quad 0 \leq c \leq 3 \\ 0. 0 5 3 8 c + 1. 1 3 9 & \quad 3 \leq c \leq 1 6 \end{array} \right.
$$

Figure 9.4 shows step changes in the reference signal at three different operating conditions when the approximation of the inverse of the valve characteristic is used between the controller and the valve. (Compare with the uncompensated system in Fig. 1.9.) There is considerable improvement in the performance of the closed-loop system. By improving the inverse it is possible to make the process even more insensitive to the nonlinearity of the valve. □

Example 9.1 shows a simple and very useful idea to compensate for known static nonlinearities. In practice it is often sufficient to approximate the nonlinearity by a few line segments. There are several commercial single-loop controllers that can make this kind of compensation. DDC packages usually include functions that can be used to implement nonlinearities.

The resulting controller in Example 9.1 is nonlinear and should (in its basic form) not be regarded as gain scheduling. In Example 9.1 there is no measurement of any operating condition apart from the controller output. In other situations the nonlinearity is determined from measurement of several variables. However, a gain-scheduling controller should contain measurement of a variable that is related to the operating point of the process. Gain scheduling based on an auxiliary signal is illustrated in the following example.
