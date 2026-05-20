# Example 5.5

Consider the same Example 5.3 to use analytical solution of matrix Riccati difference equation based on [138]. The results are obtained using Control System Toolbox of MATLAB $^{©}$ , Version 6 as shown below. The solution of matrix DRE is not readily available with MATLAB $^{©}$ and hence a program was developed based on the analytical solution of the matrix DRE [138]. The following MATLAB $^{©}$ m file for Example 5.5 requires two additional MATLAB $^{©}$ files lqrdnss.m and lqrdnssf.m given in Appendix C. The solutions are shown in Figure 5.9. Using these Riccati gains, the optimal states $x_{1}^{*}(k)$ and $x_{2}^{*}(k)$ are shown in Figure 5.10 and the optimal control $u^{*}(k)$ is shown in Figure 5.11.

![](image/7b360a04e1b4912017cb305532121c68a0eb6691b497986556504307f63ba028.jpg)

<details>
<summary>line</summary>

| k | p22(k) | p11(k) | p12(k) |
| --- | --- | --- | --- |
| 0 | 2 | 1.5 | 0 |
| 9 | 2 | 1.5 | 0 |
| 10 | 4 | 2 | 0 |
</details>

Figure 5.9 Riccati Coefficients for Example 5.5

![](image/afc8d0bc7eed88103cd5f2fc49190ac853ae2793774ec998bf513ad93c3816e8.jpg)

<details>
<summary>line</summary>

| k | x₁(k) | x₂(k) |
| --- | --- | --- |
| 0 | 5.0 | 3.0 |
| 1 | 3.0 | -0.5 |
| 2 | 1.0 | -0.8 |
| 3 | 0.3 | -0.2 |
| 4 | 0.0 | 0.0 |
| 5 | 0.0 | 0.0 |
| 6 | 0.0 | 0.0 |
| 7 | 0.0 | 0.0 |
| 8 | 0.0 | 0.0 |
| 9 | 0.0 | 0.0 |
| 10 | 0.0 | 0.0 |
</details>

Figure 5.10 Optimal States for Example 5.5   
```matlab
%% the MATLAB. Version 6
%% The following file example.m requires
%% two other files lqrnss.m and lqrnssf.m
%% which are given in Appendix C
clear all
A=[.8,1;0,.6];
B=[1;.5];
F=[2,0;0,4];
Q=[1,0;0,1];
R=1;
kspan=[0 10];
x0(:,1)=[5.;3.];
[x,u]=lqrdnss_dsn(A,B,F,Q,R,x0,kspan);
************************** 
```
