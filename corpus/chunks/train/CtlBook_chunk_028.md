# Single Poles Case

For example,

$$G (s) = \frac {s + 5}{s ^ {3} + 6 s ^ {2} + 3 5 8 s + 4 0 0}$$

does not have an obvious inverse Laplace transform. However if we can factor it to get

$$G (s) = \frac {(s + 5)}{(s + 2) (s + 4) (s + 5 0)}$$

then we can use the Partial Fraction expansion to get it into the form

$$G (s) = \frac {A _ {1}}{(s + 2)} + \frac {A _ {2}}{(s + 4)} + \frac {A _ {3}}{(s + 5 0)}$$

then we can immediately write

$$g (t) = A _ {1} e ^ {- 2 t} + A _ {2} e ^ {- 4 t} + A _ {3} e ^ {- 5 0 t}$$

It is not obvious that the partial fraction expansion is always possible but we will derive a class of cases and then perform some examples. Let's call the exponential time constants

$$p _ {1} = - 2, p _ {2} = - 4, p _ {3} = - 5 0$$

and assume

$$G (s) = \frac {(s - z)}{(s - p _ {1}) (s - p _ {2}) (s - p _ {3})} = \frac {A _ {1}}{(s - p _ {1})} + \frac {A _ {2}}{(s - p _ {2})} + \frac {A _ {3}}{(s - p _ {3})}$$

Here we write $\left( s - p _ { 1 } \right)$ because we usually are dealing with negative real poles. In other words: $( s + 5 ) =$ $( s - - 5 )$ . The real pole $\mathrm { i s } - 5$ and the term we are writing is $( s - p )$ , where $p = - 5$ .

Now we multiply through by $\left( s - p _ { 1 } \right)$ :

$$G (s) = \frac {(s - p _ {1}) (s - z)}{(s - p _ {1}) (s - p _ {2}) (s - p _ {3})} = \frac {A _ {1} (s - p _ {1})}{(s - p _ {1})} + \frac {A _ {2} (s - p _ {1})}{(s - p _ {2})} + \frac {A _ {3} (s - p _ {1})}{(s - p _ {3})}$$

Now we do two things: 1) cancel terms where possible, 2) solve for the special case $s = p _ { 1 }$ 1)

$$\frac {(s - z)}{(s - p _ {2}) (s - p _ {3})} = \frac {A _ {1}}{1} + \frac {A _ {2} (s - p _ {1})}{(s - p _ {2})} + \frac {A _ {3} (s - p _ {1})}{(s - p _ {3})}$$

2) let $s = p _ { 1 } \colon$

$$\left. \frac {(s - z)}{(p _ {1} - p _ {2}) (p _ {1} - p _ {3})} \right| _ {s = p _ {1}} = \frac {A _ {1}}{1} + \frac {A _ {2} (p _ {1} - p _ {1})}{(p _ {1} - p _ {2})} + \frac {A _ {3} (p _ {1} - p _ {1})}{(p _ {1} - p _ {3})}$$

We can eliminate the $A _ { 2 } , A _ { 3 }$ terms! Giving:

$$\frac {(p _ {1} - z)}{(p _ {1} - p _ {2}) (p _ {1} - p _ {3})} = A _ {1}$$

Since everything on the left hand side is known, we have just solved $A _ { 1 }$ . If we multiply through by each denominator in turn, we can get all the $A _ { i }$ .
