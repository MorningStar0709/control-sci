# 11.3 Discrete Time and Z transform review/intro

A discrete time signal, also known as a sampled data signal, is a series of unit impulses, at regular times $t = n T , n = \{ 0 , \bar { 1 , } 2 , 3 , . . . . \}$ , scaled by the signal values at each sample time (Figure 11.1). If there is a continuous signal, x(t), the discrete time version of that signal is

$$x (n) = \sum_ {n} \delta (t - n T) \times x (n T) \quad n = 0, 1, 2 \dots$$

The unilateral Z-Transform (a discrete time analog of the Laplace Transform) is

$$X (z) = \sum_ {n = 0} ^ {n = \infty} x (n) z ^ {- n}$$

where z is a complex number (like s), usually represented $A e ^ { j \psi }$ .

The Z-Transform can be used like the Laplace transform to analyze systems expressed as digital lters.
