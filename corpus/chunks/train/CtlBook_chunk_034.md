# Example 1.6

Apply the Partial Fraction Expansion to

$$G (s) = \frac {(s + 5)}{s ^ {2} (s + 3)}$$

(note that there is a repeated root in the demoninator (repeated pole at s = 0)).

We start by setting up the problem with two terms for the repeated pole:

$$G (s) = \frac {A _ {1}}{s ^ {2}} + \frac {A _ {2}}{s} + \frac {A _ {3}}{(s + 3)}$$

A1:

$$\left. \frac {s ^ {2} (s + 5)}{s ^ {2} (s + 3)} \right| _ {s = 0} = \frac {s ^ {2} A _ {1}}{s ^ {2}} + \frac {s ^ {2} A _ {2}}{s} + \frac {s ^ {2} A _ {3}}{(s + 3)} \tag {1.1}$$

giving

$$A _ {1} = 5 / 3$$

A3 is also straightforward, giving $A _ { 3 } = 2 / 9 .$ . But working through $A _ { 2 }$ we nd:

$$\left. \frac {s (s + 5)}{s ^ {2} (s + 3)} \right| _ {s = 0} = \frac {s A _ {1}}{s ^ {2}} + A _ {2} + \frac {s A _ {3}}{(s + 3)}$$

We now have the problem that we cannot cancel the $s ^ { 2 }$ in the denominator of the $A _ { 2 }$ term (which we need to do!). Instead dierentiate the $A _ { 1 }$ expression (Eqn. 1.1 with respect to s:

$${\frac {d}{d s}} {\frac {(s + 5)}{(s + 3)}} = 0 + A _ {2} + {\frac {d}{d s}} {\frac {s ^ {2}}{(s + 3)}} A _ {3}$$

Using an advanced dierentiation rule (below) $\mathrm { g i } \mathfrak { r }$ ves:

$$\frac {- 2}{(s + 3) ^ {2}} = A _ {2} + \frac {s (s + 6)}{(s + 3) ^ {2}} A _ {3}$$

evaluating at s = 0,

$$A _ {2} = - 2 / 9$$

The tricks we used used:

$$\frac {d}{d x} \frac {(x + a)}{(x + b)} = \frac {1}{(x + b)} - \frac {(x + a)}{(x + b) ^ {2}}$$

and

$$\frac {d}{d x} \frac {x ^ {2}}{(x + a)} = \frac {2 x}{(x + a)} - \frac {x ^ {2}}{(x + a) ^ {2}}$$

This gets even more unwieldy when the repeated pole is non-zero, but fortunately we rarely need this technique or can fall back on numerical or AI-based symbolic methods.
