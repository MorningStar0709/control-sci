$$\mathbf {y} (s) = H _ {d} (s) \mathbf {y} _ {d} (s) + H _ {w d} (s) \mathbf {d} (s) + H _ {v} (s) \mathbf {v} (s) \tag {4.7}$$

with a corresponding change in Equation 4.6.

Ideally, the error would be zero; i.e., the output would track $y_{d}$ exactly. To achieve this for all possible signals $y_{d}$ , w, and v, we would require $H_{d}(s) = I$ and $H_{w}(s)[H_{wd}(s)] = H_{v}(s) = 0$ . That is not possible, unfortunately, so we are forced to choose between a number of nonideal solutions. In order to do that, we must be able to discriminate between acceptable and unacceptable departures from the ideal; i.e., we must have performance specifications.

The object of this chapter is the study of control systems specifications and factors that limit performance for a few control structures. The material is presented in terms of single-input, single-output (SISO) systems.
