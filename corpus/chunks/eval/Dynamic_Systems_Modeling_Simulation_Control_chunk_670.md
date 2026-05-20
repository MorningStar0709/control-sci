# 11.4 PNEUMATIC AIR-BRAKE SYSTEM

Our third case study analyzes a pneumatic actuator for an air-brake system for large commercial vehicles such as tractor-trailers and buses. Most commercial vehicles in the United States use an “S-cam” drum brake mechanism that is actuated by compressed air [5]. Figure 11.22 shows a schematic diagram of the air-brake system, which is composed of pneumatic and mechanical subsystems. The pneumatic subsystem includes the supply pressure $P _ { S }$ (charged by a compressor), which is connected to the brake chamber. Pressing the brake pedal opens the treadle valve. The valve modulates the high-pressure air flow from the supply tank to the brake chamber. The mechanical subsystem includes the diaphragm (piston) and push-rod, return spring, and S-cam drum brake mechanism. As compressed air flows into the brake chamber, the increase in air pressure provides a force on the diaphragm-piston and moves the push-rod to the right. The transmitted force from the push-rod rotates the S-cam, which presses the brake lining against the inside of the drum, thus providing the braking friction for the wheel.

Our objective is to accurately model the air-brake system and simulate its response to a step input (opening) of the treadle valve. An accurate integrated model would allow brake designers to predict pressure transients in the brake chamber over a range of partial brake applications. This capability may be used as a diagnostic tool for inspecting the health of the air-brake system [5].

![](image/51e155d056c758b9225957e362bd099df3e8dd551f2f17970b87275907cbb3c7.jpg)

<details>
<summary>text_image</summary>

Brake pedal force
P_S
Supply tank
Treadle valve
Brake chamber
Diaphragm-piston
Return spring
Push-rod
Brake drum
S-cam
Brake lining
</details>

Figure 11.22 Schematic of the pneumatic air-brake system.
