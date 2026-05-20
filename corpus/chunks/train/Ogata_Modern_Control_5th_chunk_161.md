which may be rewritten as

$$R C \frac {d \theta}{d t} + \theta = R h _ {i}$$

Note that the time constant of the system is equal to RC or $M / G$ seconds. The transfer function relating u and $h _ { i }$ is given by

$$\frac {\Theta (s)}{H _ {i} (s)} = \frac {R}{R C s + 1}$$

where $\Theta ( s ) = \mathcal { L } { \big [ } \theta ( t ) { \big ] }$ and $H _ { i } ( s ) = \mathscr { L } { \big [ } h _ { i } ( t ) { \big ] }$ .

In practice, the temperature of the inflowing liquid may fluctuate and may act as a load disturbance. (If a constant outflow temperature is desired, an automatic controller may be installed to adjust the heat inflow rate to compensate for the fluctuations in the temperature of the inflowing liquid.) If the temperature of the inflowing liquid is suddenly changed from $\overline { { \theta } } _ { i }$ to $\bar { \vec { \Theta } } _ { i } + \hat { \boldsymbol { \theta } } _ { i }$ while the heat input rate H and the liquid flow rate G are kept constant, then the heat outflow rate will be changed from $\bar { H }$ to $\boldsymbol { \bar { H } } + \boldsymbol { h _ { o } }$ and, the temperature of the outflowing liquid will be changed from $\overline { { \theta } } _ { o }$ to $\boldsymbol { \overline { { \Theta } } } _ { o } + \boldsymbol { \theta }$ The heat-. balance equation for this case is

$$C d \theta = (G c \theta_ {i} - h _ {o}) d t$$

or

$$C \frac {d \theta}{d t} = G c \theta_ {i} - h _ {o}$$

which may be rewritten

$$R C \frac {d \theta}{d t} + \theta = \theta_ {i}$$

The transfer function relating u and $\theta _ { i }$ is given by

$$\frac {\Theta (s)}{\Theta_ {i} (s)} = \frac {1}{R C s + 1}$$

where $\Theta ( s ) = \mathcal { L } { \big [ } \theta ( t ) { \big ] }$ and $\Theta _ { i } ( s ) = \mathcal { L } \big [ \theta _ { i } ( t ) \big ]$ .

If the present thermal system is subjected to changes in both the temperature of the inflowing liquid and the heat input rate, while the liquid flow rate is kept constant, the change u in the temperature of the outflowing liquid can be given by the following equation:

$$R C \frac {d \theta}{d t} + \theta = \theta_ {i} + R h _ {i}$$

A block diagram corresponding to this case is shown in Figure 4–26(b). Notice that the system involves two inputs.
