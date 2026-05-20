Therefore, inductor voltage drop is $e _ { L } = e _ { C } - e _ { R _ { 7 } }$ . Voltage drop across resistor $R _ { 2 }$ is determined by Ohm’s law, $e _ { R _ { 2 } } = R _ { 2 } I _ { L }$ , and, therefore, Eq. (3.53) becomes

$$L \dot {I} _ {L} = e _ {C} - R _ {2} I _ {L} \tag {3.60}$$

Finally, we can multiply Eq. (3.58) by $R _ { 1 }$ and place all dynamic variables $( e _ { C }$ and $I _ { L } )$ in Eqs. (3.58) and (3.60) on the left-hand sides and the system input $e _ { \mathrm { i n } } ( t )$ on the right-hand sides to yield

$$R _ {1} C \dot {e} _ {C} + e _ {C} + R _ {1} I _ {L} = e _ {\text { in }} (t) \tag {3.61}L \dot {I} _ {L} + R _ {2} I _ {L} - e _ {C} = 0 \tag {3.62}$$

Equations (3.61) and (3.62) are the mathematical modeling equations for the dual-loop electrical system. The complete system is linear and second order because it consists of two first-order, linear, coupled ODEs. The reader should note that all terms in Eqs. (3.61) and (3.62) are voltages.

![](image/e221535149fc7bb098c0f22499dd120d18427f41e2a41488ed472c51069b71d2.jpg)

<details>
<summary>text_image</summary>

eA ○─●─K─○eO
          │
          +   ○
          eB ○─●─
</details>

Figure 3.12 Operational amplifier.
