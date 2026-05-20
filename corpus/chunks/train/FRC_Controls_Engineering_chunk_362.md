$$
\left[ \begin{array}{c} v _ {1 x} \\ v _ {2 x} \\ v _ {3 x} \\ v _ {4 x} \\ v _ {1 y} \\ v _ {2 y} \\ v _ {3 y} \\ v _ {4 y} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & - r _ {1 y} \\ 1 & 0 & - r _ {2 y} \\ 1 & 0 & - r _ {3 y} \\ 1 & 0 & - r _ {4 y} \\ 0 & 1 & r _ {1 x} \\ 0 & 1 & r _ {2 x} \\ 0 & 1 & r _ {3 x} \\ 0 & 1 & r _ {4 x} \end{array} \right] \left[ \begin{array}{c} v _ {x} \\ v _ {y} \\ \omega \end{array} \right]
$$

Rearrange the rows so the x and y components are in adjacent rows.

$$
\left[ \begin{array}{l} v _ {1 x} \\ v _ {1 y} \\ v _ {2 x} \\ v _ {2 y} \\ v _ {3 x} \\ v _ {3 y} \\ v _ {4 x} \\ v _ {4 y} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & - r _ {1 y} \\ 0 & 1 & r _ {1 x} \\ 1 & 0 & - r _ {2 y} \\ 0 & 1 & r _ {2 x} \\ 1 & 0 & - r _ {3 y} \\ 0 & 1 & r _ {3 x} \\ 1 & 0 & - r _ {4 y} \\ 0 & 1 & r _ {4 x} \end{array} \right] \left[ \begin{array}{l} v _ {x} \\ v _ {y} \\ \omega \end{array} \right] \tag {11.14}
$$

To convert the swerve module x and y velocity components to a velocity and heading, use the Pythagorean theorem and arctangent respectively. Here’s an example for module 1.

$$v _ {1} = \sqrt {v _ {1 x} ^ {2} + v _ {1 y} ^ {2}} \tag {11.15}\theta_ {1} = \tan^ {- 1} \left(\frac {v _ {1 y}}{v _ {1 x}}\right) \tag {11.16}$$
