# Example 4.1 cont.

You can verify that rows 2 and 4 of the matrix equation above are equivalent to the two EOMS. For example, row 2 is:

$$\ddot {x} _ {2} = \frac {- (K _ {T} + K _ {s})}{M _ {w}} x _ {2} + \frac {- B _ {s}}{M _ {w}} \dot {x} _ {2} + \frac {K _ {s}}{M _ {w}} x _ {3} \frac {B _ {s}}{M _ {w}} \dot {x} _ {3}$$

Also note that we have two trivial equations: rows 1 and 3:

$$\dot {x} _ {2} = \dot {x} _ {2} \qquad \dot {x} _ {3} = \dot {x} _ {3}$$

These are just part of the formal denition of the system matrices. Once your parameter values are known, you can plug them in and it is easy to evaluate the response to any input using the computer. As a formal matter, let's do an output equation. Assume that for some reason our system output is a mixture of the states, namely

$$y (t) = 0. 5 x _ {2} + 0. 0 1 \dot {x} _ {3}$$

then our output equation, Y = CX + DU would be

$$[ y (t) ] = [ 0. 5, 0, 0, 0. 0 1 ] X + [ 0 ] x _ {1}$$

(also following the p, q, r dimensioning scheme). D is zero because we have no x1 term in our output. For most of our examples though, the output equation will be trivial. In this example, the output is x3(t) (car body height) and thus

$$[ y (t) ] = [ 0, 0, 1, 0 ] X + [ 0 ] x _ {1}$$
