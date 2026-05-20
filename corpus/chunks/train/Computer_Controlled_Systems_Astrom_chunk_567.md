# 9.7 Realization of Digital Controllers

The previous section illustrated how roundoff and quantization in A-D and D-A converters influence the behavior of the system. Roundoff errors in the computations of the control law also cause quantization, which can be modeled and analyzed in the same way as converter quantization. The quantization arising from the computations depends critically on how the computations are organized, for example, on how the sampled-data controller is realized. This section discusses different realizations. Some advantages and disadvantages of different methods are given.

Assume that we want to realize the controller

$$y (k) = H (q ^ {- 1}) u (k) = \frac {b _ {0} + b _ {1} q ^ {- 1} + \cdots + b _ {m} q ^ {- m}}{1 + a _ {1} q ^ {- 1} + a _ {2} q ^ {- 2} + \cdots + a _ {n} q ^ {- n}} u (k) \tag {9.16}$$

Some different realizations are

- Direct form   
- Companion form   
- Series (Jordan) form   
- Parallel (diagonal) form   
- Ladder form   
- $\delta$ -operator form
