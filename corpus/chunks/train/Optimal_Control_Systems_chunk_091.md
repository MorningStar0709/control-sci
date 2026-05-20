# Example 2.10

A manufacturer wants to maximize the volume of the material stored in a circular tank subject to the condition that the material used for the tank is limited (constant). Thus, for a constant thickness of the material, the manufacturer wants to minimize the volume of the material used and hence part of the cost for the tank.

Solution: If a fixed metal thickness is assumed, this condition implies that the cross-sectional area of the tank material is constant. Let $d$ and $h$ be the diameter and the height of the circular tank. Then the volume contained by the tank is

$$V (d, h) = \pi d ^ {2} h / 4 \tag {2.5.1}$$

and the cross-sectional surface area (upper, lower and side) of the tank is

$$A (d, h) = 2 \pi d ^ {2} / 4 + \pi d h = A _ {0}. \tag {2.5.2}$$

Our intent is to maximize $V(d, h)$ keeping $A(d, h) = A_0$ , where $A_0$ is a given constant. We discuss two methods: first one is called the Direct Method using simple calculus and the second one is called Lagrange Multiplier Method using the Lagrange multiplier method.

1 Direct Method: In solving for the optimum value directly, we eliminate one of the variables, say $h$ , from the volume relation (2.5.1) using the area relation (2.5.2). By doing so, the condition is embedded in the original function to be extremized. From (2.5.2),

$$h = \frac {A _ {0} - \pi d ^ {2} / 2}{\pi d}. \tag {2.5.3}$$

Using the relation $(2.5.3)$ for height in the relation $(2.5.1)$ for volume

$$V (d) = A _ {0} d / 4 - \pi d ^ {3} / 8. \tag {2.5.4}$$

Now, to find the extrema of this simple calculus problem, we differentiate (2.5.4) w.r.t. $d$ and set it to zero to get

$$\frac {A _ {0}}{4} - \frac {3}{8} \pi d ^ {2} = 0. \tag {2.5.5}$$

Solving, we get the optimal value of $d$ as

$$d ^ {*} = \sqrt {\frac {2 A _ {0}}{3 \pi}}. \tag {2.5.6}$$

By demanding that as per the Definition 2.3 for optimum of a function, the second derivative of V w.r.t. d in (2.5.4) be negative for maximum, we can easily see that the positive value of the square root function corresponds to the maximum value of the function. Substituting the optimal value of the diameter (2.5.6) in the original cross-sectional area given by (2.5.2), and solving for the optimum $h^{*}$ , we get

$$h ^ {*} = \sqrt {\frac {2 A _ {0}}{3 \pi}}. \tag {2.5.7}$$

Thus, we see from $(2.5.6)$ and $(2.5.7)$ that the volume stored by a tank is maximized if the height of the tank is made equal to its diameter.
