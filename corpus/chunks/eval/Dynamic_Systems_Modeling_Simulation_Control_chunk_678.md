Figure 11.27 shows the inner details of the chamber pressure subsystem block, which also utilizes a userdefined M-file. MATLAB M-file 11.3 shows the customized M-file Pdot.m, which contains the pressure-rate equation (11.27) with the appropriate calculations for volume V and the time rate of volume, V̇ . Note that the single integrator in Fig. 11.27 contains the “limit” symbol, which indicates that limits have been imposed on the output of the integrator, which in this case is chamber pressure. A lower limit of zero has been set to the integrator output so that pressure can never be negative. This limit is simply a safeguard, because normal simulations never result in negative chamber pressure.

MATLAB M-file 11.3   
```matlab
%
% M-file for computing the pressure-rate (P-dot)
% for the air-brake chamber
%
% Inputs: u (4x1 vector) = [w x xdot P ]'
%    w = mass-flow rate in/out chamber (kg/s)
%    x = diaphragm-piston position, m
%    xdot = diaphragm-piston velocity, m/s
%    P = brake chamber pressure, Pa
%
% Output: dPdt = dP/dt, Pa/s
%
function dPdt = Pdot(u)

% brake chamber parameters
Ab = 0.0129;    % area of diaphragm, m^2
V0 = 1.64e-4;    % volume of brake chamber when x=0, m^3

R = 287;    % gas constant (air), N-m/kg-K
n = 1;    % polytropic expansion index
T = 298;    % air temperature, K

% system inputs
w    = u(1);    % in/out mass-flow rate of air(+ or -), kg/s
x    = u(2);    % diaphragm-piston position, m
xdot = u(3);    % diaphragm-piston velocity, m/s
P    = u(4);    % pressure of brake chamber, Pa

% compute chamber volume and dV/dt
V = V0 + Ab*x;    % volume of brake chamber, m^3
Vdot = Ab*xdot;    % time-rate of volume, m^3/s

% pressure-rate for brake chamber, Pa/s
dPdt = ((n*R*T)/V)*(w - P*Vdot/(R*T)); 
```
