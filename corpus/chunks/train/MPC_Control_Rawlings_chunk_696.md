$$
\begin{array}{l} \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] ^ {+} = \left\{\left[ \begin{array}{c c} A _ {1} & \\ & A _ {2} \end{array} \right] + \left[ \begin{array}{c c} \overline {{B}} _ {1 1} & \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 1} & \overline {{B}} _ {2 2} \end{array} \right] \left[ \begin{array}{c c} K _ {1 1} & K _ {1 2} \\ K _ {2 1} & K _ {2 2} \end{array} \right] \right\} \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] + \\ \left[ \begin{array}{c c} L _ {1} C _ {1} & \\ & L _ {2} C _ {2} \end{array} \right] \left[ \begin{array}{c} e _ {1} \\ e _ {2} \end{array} \right] \\ \end{array}
$$

The A+BK term is stable because this term is the same as in the stabilizing centralized controller. The perturbation is exponentially decaying because the distributed estimators are stable. Therefore xˆ goes to zero exponentially, which, along with e going to zero exponentially, implies x goes to zero exponentially.

Finite iterations. Here we use the state plus input sequence description given in (6.16), which, as we have already noted, is a linear timeinvariant system. With estimate error, the system equation is

$$
\left[ \begin{array}{c} \hat {x} _ {1} ^ {+} \\ \hat {x} _ {2} ^ {+} \\ \mathbf {u} _ {1} ^ {+} \\ \mathbf {u} _ {2} ^ {+} \end{array} \right] = \left[ \begin{array}{c} A _ {1} \hat {x} _ {1} + \overline {{B}} _ {1 1} u _ {1} + \overline {{B}} _ {1 2} u _ {2} \\ A _ {2} \hat {x} _ {2} + \overline {{B}} _ {2 1} u _ {1} + \overline {{B}} _ {2 2} u _ {2} \\ g _ {1} ^ {p} (\hat {x} _ {1}, \hat {x} _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) \\ g _ {2} ^ {p} (\hat {x} _ {1}, \hat {x} _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) \end{array} \right] + \left[ \begin{array}{c} L _ {1} C _ {1} e _ {1} \\ L _ {2} C _ {2} e _ {2} \\ 0 \\ 0 \end{array} \right]
$$

Because there is again only one-way coupling between the estimate error evolution, (6.18), and the system evolution given above, the composite system is exponentially stable.
