# Example 6.13

Find the Gain and Phase Margins for

$$G _ {2} (s) = \frac {4 \times 1 0 ^ {5}}{(s + 1) (s + 3 1 . 6) (s + 1 0 0)}$$

Carefully drawing the Bode gain and phase plots by hand:

![](image/6d915746d3fb6fd112c9d96f70b029ae89959bd69da43d06c13319741acd31c0.jpg)

Using pencil and paper we get Gain and Phase margins of 0. This means the system is right on the edge. Certainly with the limited precision of pencil work, we would be safer to consider this unstable. Using python.control's margin() command we get more precisely:

$$G M = 0. 6 9 d B \quad P M = 2. 0 ^ {\circ}$$

Because we never know the system parameters with high accuracy, these margins would not be considered safe.
