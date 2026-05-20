# 7. Discrete state-space control

The complex plane discussed so far deals with continuous systems. In decades past, plants and controllers were implemented using analog electronics, which are continuous in nature. Nowadays, microprocessors can be used to achieve cheaper, less complex controller designs. Discretization converts the continuous model we’ve worked with so far from a differential equation like

$$\dot {x} = x - 3 \tag {7.1}$$

to a difference equation like

$$\frac {x _ {k + 1} - x _ {k}}{\Delta T} = x _ {k} - 3x _ {k + 1} - x _ {k} = (x _ {k} - 3) \Delta Tx _ {k + 1} = x _ {k} + (x _ {k} - 3) \Delta T \tag {7.2}$$

where $x _ { k }$ refers to the value of x at the $k ^ { t h }$ timestep. The difference equation is run with some update period denoted by T , by $\Delta T$ , or sometimes sloppily by dt.[1]

While higher order terms of a differential equation are derivatives of the state variable (e.g., x¨ in relation to equation (7.1)), higher order terms of a difference equation are delayed copies of the state variable $( \mathrm { e } . \mathrm { g } . , x _ { k - 1 }$ with respect to $x _ { k }$ in equation (7.2)).
