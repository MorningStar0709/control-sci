# Unmodeled Dynamics

So far, it has been assumed that the true process is compatible with the model used in parameter estimation. It frequently happens that the true process is more complex than the estimated model. This is often referred to as unmodeled dynamics. The problem is complex, and a careful analysis is lengthy; roughly speaking, the parameters will converge to a value that minimizes the least-squares criterion:

$$V (\theta) = \frac {1}{T} \sum_ {0} ^ {T} (A y _ {f} (t) - B u _ {f} (t)) \tag {6.30}$$

where $y_{f}$ and $u_{f}$ are the filtered process input and output, that is,

$$\mathbf {y} _ {f} = \boldsymbol {H} _ {f} \mathbf {y}u _ {f} = H _ {f} u$$

and the parameter $\theta$ represents the coefficients of the polynomials A and B. The minimum exists under certain regularity conditions, and the minimizing $\theta$ is unique under the condition of persistency of excitation. The minimizing value will depend on the data filter $H_{f}$ and the spectrum of the reference signal and the disturbances.
