# Sampling the Process

The poles of the filter and the process and the antialias filter are of the same magnitude. The filter dynamics must thus be taken into account in the design.

Sampling the process and the filter with h = 0.5 gives a discrete-time model model with

$$A (z) = \underbrace {(z ^ {2} - 0 . 7 5 0 5 z + 0 . 2 4 6 6)} _ {\text { filter }} \underbrace {(z ^ {2} - 1 . 7 1 2 4 z + 0 . 9 5 1 2) (z - 1)} _ {\text { process }}B (z) = 0. 1 4 2 0 \cdot 1 0 ^ {- 3} (z + 1 2. 1 3 1 4) (z + 1. 3 4 2 2) (z + 0. 2 2 3 4) (z - 0. 0 0 2 3)$$

The poles and zeros of the sampled system are shown in Fig. 5.24.
