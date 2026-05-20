# Example 2.8

Let's continue the electrical example of Example 2.5 by turning the EOM's into the transfer function

$$G (s) = \frac {I _ {2} (s)}{V (s)}$$

With equations 2.7 and 2.8, we can solve for $I _ { 2 } ( s )$ as follows:

Using eqn 2.8,

$$I _ {1} (s) \left(R + \frac {1}{C _ {1} s}\right) = I _ {2} (s) \left(R + \left(\frac {C _ {1} C _ {2}}{C _ {1} + C _ {2}}\right) ^ {- 1} \frac {1}{s}\right)$$

for more compact notation, let

$$C _ {1 2} = \frac {C _ {1} C _ {2}}{C _ {1} + C _ {2}}$$

giving

$$I _ {1} (s) \left(R + \frac {1}{C _ {1} s}\right) = I _ {2} (s) \left(R + \frac {1}{C _ {1 2} s}\right) \quad \rightarrow \quad I _ {1} (s) = I _ {2} (s) \frac {(R + \frac {1}{C _ {1 2} s})}{(R + \frac {1}{C _ {1} s})}$$

Substituting into equation 2.7,

$$I _ {2} (s) \left[ \frac {(1 + \frac {1}{R C _ {1 2} s}) (L s + R + \frac {1}{C _ {1} s})}{(1 + \frac {1}{C _ {1} s})} - R - \frac {1}{C _ {1} s} \right] = V (s)$$

Getting the desired ratio:

$$\frac {I _ {2} (s)}{V (s)} = \frac {1}{\frac {(R + \frac {1}{C _ {1 2} s}) (L s + R + \frac {1}{C _ {1} s})}{(R + \frac {1}{C _ {1} s}))} - R - \frac {1}{C _ {1} s}}$$

... skipping a few steps ...

$$
\begin{array}{l} = \frac {(1 + \frac {1}{R C _ {1} s})}{L s + R + \frac {1}{C _ {1} s} + \frac {L}{C _ {1 2} s} + \frac {1}{R C _ {1 2} C _ {1} s ^ {2}} - R - \frac {2}{C _ {1} s} - \frac {1}{R C _ {1} ^ {2} s ^ {2}}} \\ = \frac {\frac {1}{s} (s + \frac {1}{R C _ {1}})}{L s + \frac {1}{s} (\frac {1}{C _ {1 2}} - \frac {1}{C _ {1}}) + \frac {L}{R C _ {1 2}} + \frac {1}{s ^ {2}} (\frac {1}{R C _ {1 2} C _ {1}} - \frac {1}{R C _ {1} ^ {2}})} \\ \end{array}
$$

multiply top and bottom by $s ^ { 2 } { \mathrm { : } }$

$$= \frac {s \left(s + \frac {1}{R C _ {1}}\right)}{L s ^ {3} + \frac {L}{R C _ {1 2}} s ^ {2} + \frac {1}{C _ {1 2}} s + \frac {1}{R C _ {1 2} C _ {1}} - \frac {1}{R C _ {1} ^ {2}}}$$

Finally:

$$\frac {I _ {2} (s)}{V (s)} = \left(\frac {1}{L}\right) \frac {s ^ {2} + \frac {1}{R C _ {1}} s}{s ^ {3} + \frac {1}{R C _ {1 2}} s ^ {2} + \frac {1}{L C _ {1 2}} s + \frac {C _ {1} - C _ {1 2}}{L R C _ {1 2} C _ {1} ^ {2}}}$$

Where the transfer function is now expressed as a ratio of monic polynomials times the constant 1/L. At this point we can just implement this in our favorite software based on our known numerical parameter values.
