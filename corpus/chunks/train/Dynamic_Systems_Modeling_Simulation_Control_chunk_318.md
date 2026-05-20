MATLAB M-file 6.2   
```matlab
%
% run_tank_linear.m
%
% This M-file sets the parameters for
% the hydraulic tank system, executes
% the linear Simulink model, and plots
% the results
%
% tank parameters
P_atm = 1.0133e5; % atmospheric pressure, N/m^2
K_T = 4e-4; % turbulent flow coefficient
% nominal values (linearization point)
Q_in_star = 0.05;
P_star = Q_in_star^2/K_T^2 + P_atm;
% tank system parameters
Q_in = 0.052; % constant in-flow volumetric rate, m^3/s
P0 = 1.15e5; % initial tank base pressure, N/m^2
dP0 = P0 - P_star; % initial perturbation pressure, N/m^2
% execute linear Simulink model
sim tank_linear
% plot the tank pressure
plot(t,P)
grid
title('Linear model: tank pressure vs. time')
xlabel('Time, s')
ylabel('Tank pressure, P(t), N/m^2') 
```

![](image/68efe2f484595fa9ef4e896b0020b42aa877449a8ab767ba78c52a16ca2a10a6.jpg)

<details>
<summary>line</summary>

| Time, s | Nonlinear solution P(t) (N/m² × 10⁵) | Linear solution P(t) (N/m² × 10⁵) |
| --- | --- | --- |
| 0 | 1.15 | 1.15 |
| 200 | 1.175 | 1.175 |
| 400 | 1.18 | 1.18 |
| 600 | 1.182 | 1.182 |
| 800 | 1.183 | 1.183 |
| 1000 | 1.1835 | 1.1835 |
| 1200 | 1.184 | 1.184 |
| 1400 | 1.184 | 1.184 |
</details>

Figure 6.20 Pressure responses for nonlinear and linear hydraulic tank models (Example 6.8).
