# Performance

So far we have concentrated on the influence of modeling errors on the stability of the closed loop. It is also possible to investigate other questions. For example, it is interesting to see how modeling errors will influence the pulse-transfer function from the command signals to the output. The controller obtained by Algorithm 5.1 gives a closed-loop system with the pulse-transfer function

$$H _ {c l} = H _ {m} \frac {1}{1 + (R B / A _ {c l}) (1 / H ^ {0} - 1 / H)} \tag {5.41}$$

This expression shows how errors in the model are reflected in errors in the closed-loop pulse-transfer function. It is clear from the expression that the errors are small when the open-loop pulse-transfer functions H and $H^{0}$ are large.
