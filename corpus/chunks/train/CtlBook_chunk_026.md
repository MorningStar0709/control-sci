# Example 1.2

Find the inverse Laplace transform of the following functions

$$\mathcal {L} ^ {- 1} \{\frac {1 0}{s + 3 . 7} \}$$

Consulting the table and using the linearity property of the Laplace Transform integral:

$$\mathcal {L} ^ {- 1} \{\frac {1 0}{s + 3 . 7} \} = 1 0 e ^ {- 3. 7 t}$$

similarly

$$\mathcal {L} ^ {- 1} \{\frac {1 4 4 s}{s ^ {2} + 1 4 4} \} = 1 4 4 \cos (1 2 t)\mathcal {L} ^ {- 1} \{X (s) (s ^ {3} + a s ^ {2} + b s + c) \} = \frac {d ^ {3}}{d t ^ {3}} x + a \ddot {x} + b \dot {x} + c x$$

Here we have implicitly assumed zero initial conditions.

Let's apply the Laplace Transform to the initial LODE above. First, we will modify the LODE to include a Forcing Function on the right hand side. A forcing function is typically a physical input to the system such as an applied voltage or force.

$$\dot {x} + P x = f (t)$$

Assuming zero initial conditions and taking the Laplace Transform of both sides (see the second to last line of Table 1.1).

$$s X (s) + P X (s) = F (s)X (s) (s + P) = F (s)\frac {X (s)}{F (s)} = \frac {1}{(s + P)}$$

Here we have derived a ratio called the Transfer Function between position and the forcing function. Our solution to the LODE was

$$x (t) = e ^ {p t} = e ^ {- P t}$$

If we rewrite this using the solution, $p = - P$ , then our transfer function becomes

$$\frac {X (s)}{F (s)} = \frac {1}{(s - p)}$$

We call p the pole of this transfer function because the transfer function goes to innity when $s = p$ .
