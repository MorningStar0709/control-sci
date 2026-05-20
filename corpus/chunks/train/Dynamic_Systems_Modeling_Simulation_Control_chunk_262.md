# Impulse Input

An impulse function is often used to represent an input with a constant magnitude that lasts for a very short duration. We can think of an impulse function as a pulse function where the pulse duration goes to zero in the limit. For example, consider a pulse input that consists of a 150-N force that lasts for 0.1 s as shown in Fig. 5.16a. From engineering mechanics, we know that the impulse of the force is its time integral, and therefore the area (or impulse) is 15 N-s. Figure 5.16b shows a pulse input with double the force (300 N) with half the duration (0.05 s) so that its area remains at 15 N-s. If we maintain the area as we shrink the pulse duration to zero, the magnitude approaches infinity and the input becomes an impulse function with a “strength” or “weight” of 15 N-s.

![](image/19aa723602fac339c602f04cdbbab0ef58aafbb6e34f915a9ef8216a7d59e8e3.jpg)  
Figure 5.16 Pulse force inputs with an impulse of 15 N-s.

In the example shown in Fig. 5.16, the pulse function had an area of 15 N-s. If our original pulse function had an area of unity, we can develop the unit-impulse function by maintaining unity area and shrinking the pulse duration to zero. Mathematically, the unit impulse is represented by the Dirac delta function ??(t), which can be described by

$$\delta (t) = 0 \quad \text { for } \quad t \neq 0 \tag {5.126}\int_ {- \infty} ^ {\infty} \delta (t) d t = 1 \tag {5.127}$$

The impulse function ??(t) cannot exist in nature because of its discontinuous property, and applying an impulse input to a system can cause an instantaneous change in energy. An impulse input A??(t) has “weight” or “strength” A, which might represent a very “skinny” pulse input with area A. For example, the impulsive force input shown in Fig. 5.16 would be represented mathematically as $f ( t ) = 1 5 \delta ( t )$ (in N), where the area (or weight) A = 15 N-s and the Dirac delta function ??(t) has units $\mathbf { s } ^ { - 1 }$ . The impulse input can be graphically represented by an arrow (with its weight value) placed at the appropriate point on the time axis.
