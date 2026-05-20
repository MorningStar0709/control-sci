# Example 4.1

Figure 4.8 shows a single hydraulic tank with input volumetric-flow rate $Q _ { \mathrm { i n } }$ .

(a) Derive the mathematical model of the hydraulic system assuming laminar flow through the valve.   
(b) Derive the mathematical model of the hydraulic system assuming turbulent flow through the valve.   
(c) Repeat problems (a) and (b) with the model expressed in terms of liquid height h.

![](image/2e37b9a6312fb6e3c45c26c9a79c41c82bf85d2f37cf58a32debf7c5d667fcbe.jpg)

<details>
<summary>text_image</summary>

Input flow, Qin
Height, h
Base pressure, P
Atmospheric pressure, Patm
Valve
Qout
</details>

Figure 4.8 Hydraulic tank system for Example 4.1.

(a) Because the hydraulic system consists of a single tank, the mathematical model is derived from the conservation of mass (4.23) for a single CV

$$C \dot {P} = Q _ {\text { in }} - Q _ {\text { out }} \tag {4.24}$$

where P is the pressure at the base of the tank, $Q _ { \mathrm { i n } }$ is the (given) input volumetric flow, and $Q _ { \mathrm { o u t } }$ is the output volumetric flow through the valve. We use Eq. (4.2) to represent the laminar output flow rate

$$Q _ {\text { out }} = \frac {\Delta P}{R _ {L}} \tag {4.25}$$

where $R _ { L }$ is the laminar fluid resistance, and the pressure drop across the valve is $\Delta P = P - P _ { \mathrm { a t m } }$ because the pressure at the outlet of the valve is atmospheric pressure $P _ { \mathrm { a t m } }$ . Using Eq. (4.25) in Eq. (4.24) yields

$$C \dot {P} = Q _ {\text { in }} - \frac {P - P _ {\text { atm }}}{R _ {L}} \tag {4.26}$$

Multiplying Eq. (4.26) by $R _ { L }$ and grouping terms involving the dynamic variable P on the left-hand side yields

$$R _ {L} C \dot {P} + P = R _ {L} Q _ {\text { in }} + P _ {\text { atm }} \tag {4.27}$$

Equation (4.27) is the mathematic model of the hydraulic tank system with laminar flow through the valve. The system is modeled by a single first-order linear ODE because we have a single fluid capacitance that can store energy. The fluid capacitance of the tank is a constant: $C = A / ( \rho g )$ ). The system inputs are $Q _ { \mathrm { i n } }$ and $P _ { \mathrm { a t m } }$ and consequently they are grouped on the right-hand side of Eq. (4.27).

(b) For turbulent flow through the valve, we use Eq. (4.5) for the output volumetric-flow rate

$$Q _ {\text { out }} = K _ {T} \sqrt {P - P _ {\text { atm }}} \tag {4.28}$$
