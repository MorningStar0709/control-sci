A–4–11. Consider the thin, glass-wall, mercury thermometer system shown in Figure 4–40.Assume that the thermometer is at a uniform temperature $\bar { \Theta }$ (ambient temperature) and that at $t = 0$ it is immersed in a bath of temperature $\bar { \boldsymbol { \Theta } } + \boldsymbol { \theta } _ { b }$ where, $\theta _ { b }$ is the bath temperature (which may be constant or changing) measured from the ambient temperature $\textstyle { \bar { \theta } } .$ Define the instantaneous ther-. mometer temperature by $\bar { \Theta } + \theta .$ so that u is the change in the thermometer temperature satisfying, the condition that $\theta ( 0 ) = 0$ . Obtain a mathematical model for the system. Also obtain an electrical analog of the thermometer system.

Solution. A mathematical model for the system can be derived by considering heat balance as follows:The heat entering the thermometer during dt sec is $q d t ,$ where q is the heat flow rate to the thermometer. This heat is stored in the thermal capacitance C of the thermometer, thereby raising its temperature by du. Thus the heat-balance equation is

$$C d \theta = q d t \tag {4-48}$$

Figure 4–40   
Thin, glass-wall, mercury thermometer system.   
![](image/b618101f5a166b0c8096963f6a89cd8d66ff97912581d8c989be983f5d13fd54.jpg)

<details>
<summary>text_image</summary>

Thermometer
Θ̅ + θ
Θ̅ + θb
Bath
</details>

Figure 4–41

Electrical analog of the thermometer system shown in Figure 4–40.

![](image/2fdc1081ac7cd4e60fe9e392958f1552c69ef1272c1bd6ca579f3ab81b0b9543.jpg)

<details>
<summary>chemical</summary>

Simple RC circuit diagram with resistor and capacitor in series
</details>

Since thermal resistance R may be written as

$$R = \frac {d (\Delta \theta)}{d q} = \frac {\Delta \theta}{q}$$

heat flow rate q may be given, in terms of thermal resistance R, as

$$q = \frac {(\overline {{{\boldsymbol {\Theta}}}} + \theta_ {b}) - (\overline {{{\boldsymbol {\Theta}}}} + \theta)}{R} = \frac {\theta_ {b} - \theta}{R}$$

where $\bar { \Theta } + \theta _ { b }$ is the bath temperature and $\bar { \Theta } + \theta$ is the thermometer temperature. Hence, we can rewrite Equation (4–48) as

$$C \frac {d \theta}{d t} = \frac {\theta_ {b} - \theta}{R}$$

or

$$R C \frac {d \theta}{d t} + \theta = \theta_ {b} \tag {4-49}$$

Equation (4–49) is a mathematical model of the thermometer system.

Referring to Equation (4–49), an electrical analog for the thermometer system can be written as

$$R C \frac {d e _ {o}}{d t} + e _ {o} = e _ {i}$$

An electrical circuit represented by this last equation is shown in Figure 4–41.
