MATLAB M-file 11.4   
```matlab
% flow_Q1.m
%
% This M-file models the volumetric-flow rate of fluid
% in/out of chamber 1. Assumes valve flow is modeled
% by flow through a sharp-edged orifice
%
% Inputs: u (4x1 vector) = [ P_s P_r y P1 ]'
%
P_s = supply pressure, Pa
%
P_r = reservoir pressure (drain), Pa
y = valve displacement, m
%
P1 = pressure of chamber 1, Pa
%
% Output: Q1 = in/out volumetric-flow rate, m^3/s
%
function Q1 = flow_Q1(u)
% system parameter
h = 0.008; % height of valve opening, m
% hydraulic constants
Cd = 0.62; % discharge coefficient
rho = 875; % fluid density, kg/m^3
% System inputs
P_s = u(1); % supply pressure, Pa
P_r = u(2); % reservoir pressure, Pa
y = u(3); % valve displacement, m
P1 = u(4); % pressure in chamber 1, Pa
% Compute valve orifice area
Av = abs(y)*h; % valve orifice area, m^2
% Determine if flow is from supply (y > 0), or if flow
% is out to reservoir pressure (y < 0)
if y >= 0
    % Chamber 1 is connected to the supply, P_s
    % (flow is positive if P_s > P1)
    Q1 = Cd*Av*sign(P_s - P1)*sqrt( 2*abs(P_s - P1)/rho );
else
    % Chamber 1 is connected to the reservoir, P_r
    % (flow is negative if P1 > P_r)
    Q1 = -Cd*Av*sign(P1 - P_r)*sqrt( 2*abs(P1 - P_r)/rho );
end 
```

![](image/76176b9bb697dd915deebf2d5e7b85d64ea6354283fb719b3bdc3d04a4ac90af.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1 Q1"] --> B["+"]
    C["2 xdot"] --> D["A Piston area A1"]
    D --> E["V1 dot"]
    E --> F["Q1 - V1 dot"]
    G["3 x"] --> H["A Area A1"]
    H --> I["+"]
    I --> J["V1 Invert"]
    J --> K["1/u"]
    K --> L["1/V1"]
    L --> M["Bulk modulus"]
    M --> N["beta"]
    N --> O["× Product"]
    O --> P["P1 dot"]
    P --> Q["1/s ∫ Integrator"]
    Q --> R["P1 To Workspace"]
    S["V0 Vol1 at x = 0"] --> H
    T["P1"] --> Q
    U["1 P1"] --> R
```
</details>

Figure 11.35 Cylinder pressure subsystem (chamber 1) for the EHA.

![](image/216c9474772c27b317d6128ee9b24d75a23d05562408c30b3c9ca9ffcfd06bb2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    P1["1"] -->|Pressure P1| A["A"]
    P2["2"] -->|Pressure P2| A["A"]
    A -->|Piston area 1| +[+]
    P2 -->|Piston area 2| -["-"]
    - -->|Net force| 1/m["1/m"]
    1/m -->|x-ddot| Integrator["1/s"]
    Integrator -->|xdot| Integrator1["1/s"]
    Integrator1 -->|x| 1["x"]
    Integrator1 -->|xdot| b["b"]
    b -->|xdot| 2["xdot"]
    b -->|Viscous friction coefficient| -b
    style P1 fill:#f9f,stroke:#333
    style P2 fill:#f9f,stroke:#333
    style A fill:#ccf,stroke:#333
    style B fill:#ccf,stroke:#333
```
</details>

Figure 11.36 Mechanical subsystem for the EHA.
