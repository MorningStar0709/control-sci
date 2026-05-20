i.e., we are sure the die is odd if it is 1. Notice that the arguments to the conditional density do not commute as they do in the joint density.

This fact leads to a famous result. Consider the definition of conditional density, which can be expressed as

$$p _ {\xi , \eta} (x, y) = p _ {\xi | \eta} (x | y) p _ {\eta} (y)$$

or

$$p _ {\eta , \xi} (y, x) = p _ {\eta | \xi} (y | x) p _ {\xi} (x)$$

Because $p _ { \xi , \eta } ( x , y ) \ = \ p _ { \eta , \xi } ( y , x )$ , we can equate the right-hand sides and deduce

$$p _ {\xi | \eta} (x | y) = \frac {p _ {\eta | \xi} (y | x) p _ {\xi} (x)}{p _ {\eta} (y)}$$

which is known as Bayes’s theorem (Bayes, 1763). Notice that this result comes in handy whenever we wish to switch the variable that is known in the conditional density, which we will see is a key step in state estimation problems.
