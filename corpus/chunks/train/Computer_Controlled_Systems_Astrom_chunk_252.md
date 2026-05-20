This solution to the pole-placement problem has many nice symmetries. The solution to the state feedback and the observer are dual problems. The same numerical algorithm can be used to find the feedback gain L and the observer gain K. It is also attractive that the solution of the full problem can be split into two smaller problems. The separation of the problem is very useful. It also justifies that the closed-loop poles are separated into two groups, one is associated with the state feedback and the other with the observer.

Notice that the observer contains a model of the process internally. This is a special case of the internal-model principle, which says that a good controller contains a model of the controlled system.

The controller can also be viewed as a black box that generates the control signal from the process output. The controller described by (4.34) and (4.35) can be represented by the nth-order pulse-transfer function from measured output y to control signal u:

$$H _ {c} (z) = - L (z I - \Phi + \Gamma L + K C) ^ {- 1} K \tag {4.37}$$
