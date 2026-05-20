<table><tr><td>System Parameter</td><td>Value</td></tr><tr><td>Coil resistance, R</td><td>3 Ω</td></tr><tr><td>Coil inductance, L</td><td>0.005 H</td></tr><tr><td>Force/back-emf constant, K</td><td>6 N/A2</td></tr><tr><td>Armature-valve mass, m</td><td>0.03 kg</td></tr><tr><td>Viscous friction coefficient, b</td><td>12 N-s/m</td></tr><tr><td>Spring constant, k</td><td>6000 N/m</td></tr><tr><td>Dry friction force, Fdry</td><td>0.5 N</td></tr></table>

MATLAB M-file 6.3   
```matlab
%
% run_EMA.m
%
% This M-file sets the modeling parameters for the
% electromagnetic actuator (EMA), executes the
% Simulink model, and plots the dynamic variables
%
% Solenoid electrical circuit parameters
e_in = 10;    % step input voltage
R = 3;    % coil resistance, Ohms
L = 0.005;    % coil inductance, H
K = 6;    % dL/dx (back-emf and force constant), N/A^2
% Mechanical parameters
m = 0.03;    % armature-valve mass, kg
b = 12;    % viscous friction coefficient, N-s/m
k = 6000;    % return spring constant, N/m
F_dry = 0.5;    % dry friction force, N
% run Simulink model
sim integrated_EMA
% plots
figure(1)
plot(t,1e3*x)
grid
xlabel('Time, s')
ylabel('Armature-valve position, x(t), mm')
figure(2)
plot(t,I)
grid
xlabel('Time, s')
ylabel('Solenoid current, I(t), A') 
```

Figure 6.29a presents the armature–valve position x(t) (in mm) for the 10-V step voltage input. Note that the valve rises from its seat at time t = 0.05 s when the voltage input is applied, and reaches a steady (constant)

![](image/824189aaf43fdb7780db4332447b0496006ae1d2ea2b0a1fcf8fddbae551cc6c.jpg)

<details>
<summary>line</summary>

| Time, s | Armature-valve position, x(t), mm |
| --- | --- |
| 0.00 | 0.0 |
| 0.05 | 0.0 |
| 0.10 | 4.5 |
| 0.15 | 5.3 |
| 0.20 | 5.5 |
| 0.25 | 5.5 |
</details>

(a)

![](image/95b6680fe44b63aa54ca8d7e6894cee41c176a16b09963366f0962a27f3709ff.jpg)

<details>
<summary>line</summary>

| Time, s | Solenoid current, I(t), A |
| --- | --- |
| 0.00 | 0.0 |
| 0.05 | 2.0 |
| 0.10 | 3.2 |
| 0.15 | 3.4 |
| 0.20 | 3.4 |
| 0.25 | 3.4 |
</details>

(b)   
Figure 6.29 Response of the integrated solenoid actuator–valve system (Example 6.9): (a) armature–valve position and (b) solenoid current.
