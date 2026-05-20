# EXAMPLE 1.12 An adaptive autopilot for ship steering

This is an example of a dedicated system for a special application. The adaptive autopilot is superior to a conventional autopilot for two reasons: It gives better performance, and it is easier to operate. A conventional autopilot has three dials, which have to be adjusted over a continuous scale. The adaptive autopilot has a performance-related switch with two positions (tight steering and economic propulsion). In the tight steering mode the autopilot gives good, fast response to commands with no consideration for propulsion efficiency. In the economic propulsion mode the autopilot attempts to minimize the steering loss. The control performance is significantly better than that of a well-adjusted conventional autopilot, as shown in Fig. 1.24. The figure shows heading deviations and rudder motions for an adaptive autopilot and a conventional autopilot. The experiments were performed under the same weather conditions. Notice that the heading deviations for the adaptive autopilot are much smaller than those for the conventional autopilot but that the rudder motions are of the same magnitude. The adaptive autopilot is better because it uses a more complicated control law, which has eight parameters instead of three for the conventional autopilot. For example, the adaptive autopilot has an internal model of the wave motion. If the adaptation mechanism is switched off, the constant parameter controller obtained will perform well for a while, but its performance will deteriorate as the conditions change. Since it is virtually impossible to adjust eight parameters manually, adaptation is a necessity for using such a controller. The adaptive autopilot is discussed in more detail in Chapter 12.

![](image/333928824cacaf9df6b3d960d0b4b87c925bcda3e930b04b661b388d0fb425c3.jpg)

<details>
<summary>line</summary>

| Time (min) | Heading error |
| --- | --- |
| 0 | 0 |
| 80 | ~0 |
</details>

![](image/9230d3919a7e3f2c9983f92b666bf76b2de401858b2f0abd8efd7e137a380514.jpg)

<details>
<summary>line</summary>

| Time (min) | Value |
| --- | --- |
| 0 | 0 |
| 10 | 2 |
| 20 | -2 |
| 30 | 4 |
| 40 | 2 |
| 50 | -4 |
| 60 | 3 |
| 70 | 1 |
| 80 | 2 |
</details>

![](image/d4521ce8bb8179d8553dec6d23d5052aee6893fa912afea041599aad8a248539.jpg)

<details>
<summary>line</summary>

| Time (min) | Rudder angle |
| --- | --- |
| 0 | 0 |
| 80 | -10 |
</details>

![](image/c71db359a8610c34797e08cc6bb7cd02cc47e863daaeddf259ce7ba949241b23.jpg)

<details>
<summary>line</summary>

| Time (min) | Value |
| --- | --- |
| 0 | 0 |
| 10 | 5 |
| 20 | -5 |
| 30 | 10 |
| 40 | -10 |
| 50 | 15 |
| 60 | -20 |
| 70 | 20 |
| 80 | -10 |
</details>

Figure 1.24 The figure shows the variations in heading and the corresponding rudder motions of a ship. (a) Adaptive autopilot. (b) Conventional autopilot based on a PID-like algorithm.

The next example illustrates a general-purpose adaptive system.
