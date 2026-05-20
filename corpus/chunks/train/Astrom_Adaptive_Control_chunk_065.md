# PROBLEMS

1.1 Look up the definitions of "adaptive" and "learning" in a good dictionary. Compare the uses of the words in different fields.   
1.2 Find descriptions of adaptive controllers from some manufacturers and browse through them.   
1.3 Give some situations in which adaptive control may be useful. What factors would you consider when judging the need for adaptive control?   
1.4 Make an assessment of the field of adaptive control by making a literature search. Look for the distribution of publications on adaptive control over the years. Can you see some pattern in the publications concerning uses of different methods, emphasis on theory and applications, and so on?

1.5 The system in Example 1.4 has the following characteristics:

$$G _ {0} (s) = \frac {1}{(s + 1) ^ {3}}f (u) = u ^ {4}$$

The PI controller has the gain K = 0.15 and the reset time $T_{i} = 1$ . Linearize the equations when the reference values are $u_{c} = 0.3, 1.1$ , and 5.1. Determine the roots of the characteristic equation in the different cases. Determine a reference value such that the linearized equations just become unstable.

1.6 Consider the concentration control system in Example 1.5. Assume that $V_{d} = V_{m} = 1$ and that the nominal flow is q = 1. Determine PI controllers with the transfer function

$$K _ {c} \left(1 + \frac {1}{T _ {i} s}\right)$$

that give good closed-loop performance for the flows q = 0.5, 1, and 2. Test the controllers for the nominal flow.

1.7 Consider the following system with two inputs and two outputs:

$$
\frac {d x}{d t} = \left( \begin{array}{r r r} - 1 & 0 & 0 \\ 0 & - 3 & 0 \\ 0 & 0 & - 1 \end{array} \right) x + \left( \begin{array}{l l} 1 & 0 \\ 0 & 2 \\ 0 & 1 \end{array} \right) u

y = \left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & 1 \end{array} \right) x
$$

Assume that proportional feedback is introduced around the second loop:

$$u _ {2} = - k _ {2} y _ {2}$$

(a) Determine the transfer function from $u_{1}$ to $y_{1}$ , and determine how the steady-state gain depends on $k_{2}$ .

(b) Simulate the response of $y_{1}$ and $y_{2}$ when $u_{1}$ is a step for different values of $k_{2}$ .

1.8 A block diagram of a system used for metal cutting on a numerically controlled machine is shown in Fig. 1.25. The machine is equipped with a force sensor, which measures the cutting force. A controller adjusts the feedback to maintain a constant cutting force. The cutting force is approximately given by

$$F = k a \left(\frac {v}{N}\right) ^ {\alpha}$$
