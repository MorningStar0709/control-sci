# Example 4.7

Figure 4.18 shows an interior office room with a baseboard heater, which can be modeled by a lumped-capacitance thermal system (e.g., see Reference 2). The air in the room has total thermal capacitance C and temperature T and the baseboard heater provides heat input $q _ { \mathrm { B H } }$ . The four walls and ceiling and floor surfaces are modeled by six different thermal resistances $( R _ { i } , i = 1 , 2 , . . . \widetilde { 6 } )$ ) due to the different materials, dimensions, and existence of a window or door for that surface. Derive the model of the thermal system.

Figure 4.19 shows the boundary of the thermal system and the heat flow rates. The system boundary is the rectangular volume enclosed by the four walls and ceiling and floor surfaces. Because the rectangular room has six surfaces (each modeled by a discrete thermal resistance) we show six outgoing heat flow rates $q _ { i } , i = 1 , 2 , \ldots , 6$ that are normal to each surface. The input heat from the baseboard heater is $q _ { \mathrm { B H } }$ . Because there is no mass crossing the system boundary, we use the energy balance equation (4.85) without the enthalpy-rate terms

$$C \dot {T} = \sum q _ {\text { in }} - \sum q _ {\text { out }} \tag {4.86}$$

![](image/8212626a11044b139d910c4dffcb43133c2ffb8a6089bfc060d337f5ac8cd5ca.jpg)

<details>
<summary>text_image</summary>

North
door
window
Thermal resistance, R₁
Baseboard heater
q_BH
R₃
Temperature, T
Thermal capacitance, C
door
R₂
Top view
</details>

![](image/540b7429fa516cf8192549bb24dbb009d8087fcdd5fa06aad9a0752e6063a758.jpg)

<details>
<summary>text_image</summary>

ceiling, R₅
door
East view
floor, R₆
</details>

Figure 4.18 Thermal system: interior room with baseboard heater (Example 4.7).

![](image/321475279832aade0ea1b0d6ea1f185d27d63b3878400de2ddcace34904cc158.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Baseboard heater"] -->|q_BH| B["Temperature, T Thermal capacitance, C"]
    B -->|q_1| C["Ambient temperature, T_a"]
    C -->|q_3| D["ceiling"]
    D -->|q_5| E["Temperature, T Capacitance, C"]
    E -->|q_6| F["floor"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
```
</details>

Figure 4.19 Thermal system boundary and heat flow rates (Example 4.7).
