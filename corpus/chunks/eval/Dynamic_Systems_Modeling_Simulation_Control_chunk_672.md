In all other scenarios (differential pressure force exceeds preload, or $x > 0 )$ , the contact force is zero. The load force required to actuate the S-cam is modeled as a nonlinear function of push-rod displacement

$$F _ {\text { load }} = k _ {1} x - k _ {2} x ^ {2} \tag {11.26}$$

where constants $k _ { 1 }$ and $k _ { 2 }$ are the linear and quadratic stiffness terms. We choose $k _ { 2 } > 0$ so that the force required to engage the S-cam mechanism decreases with large displacement x. Equations (11.24)–(11.26) constitute the mathematical model of the mechanical subsystem.

Figure 11.24 shows the pneumatic subsystem, which consists of a single chamber (pressure P), the supply pressure $P _ { S } ,$ , and the valve. Brake chamber pressure will vary because of the input mass flow w and change in volume. Using the basic modeling equation for pneumatic systems derived in Chapter 4, the chamber pressure equation is

$$\dot {P} = \frac {n R T}{V} \left(w - \frac {P}{R T} \dot {V}\right) \tag {11.27}$$

where R is the gas constant, T is the air temperature, n is the exponent of the polytropic expansion process, and V is the volume of the brake chamber. We assume an isothermal process, and therefore $n = 1$ . Brake chamber volume is a function of piston position x

$$V = V _ {0} + A _ {b} x \tag {11.28}$$

where $V _ { 0 }$ is the volume when the diaphragm is seated $( \mathrm { i . e . , } x = 0 )$ ). The time derivative of the chamber volume is simply a function of piston velocity, or $\dot { V } = A _ { b } \dot { x }$ . Clearly, the pressure dynamics of the brake chamber are nonlinear.

Input mass-flow rate w through the valve is modeled by the orifice-flow equations for pneumatic systems, which we presented in Chapter 4 and are repeated below

$$w = C _ {d} A _ {v} P _ {S} \sqrt {\frac {2 \gamma}{(\gamma - 1) R T} \left[ \left(\frac {P}{P _ {S}}\right) ^ {\frac {2}{\gamma}} - \left(\frac {P}{P _ {S}}\right) ^ {\frac {\gamma + 1}{\gamma}} \right]} \quad \text { if } \quad \frac {P}{P _ {S}} > C _ {r} \tag {11.29}$$

![](image/0bcaf5fb1e02194d8e979f1c9e0bf6b73180318f6ba768e47694a331cfe2a86e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Supply tank P_S"] --> B["Treadle valve"]
    B --> C["Mass-flow rate, w"]
    C --> D["Diaphragm-piston area, A_b"]
    D --> E["Brake chamber, P and V"]
    E --> F["x"]
```
</details>

Figure 11.24 Air-brake pneumatic subsystem.
