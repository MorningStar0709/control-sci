Of course attempting global optimization is possible, but that exacerbates weakness 1 significantly and no guarantees of finding a global optimum are available for anything but the simplest nonlinear models. Note that for the special case of linear models, MHE finds the global optimum and weakness 2 is removed.

Particle filtering displays quite different characteristics than those of MHE. The main strengths of PF are

1. PF uses the full nonlinear model to propagate the samples.   
2. The PF sampled density can represent a general conditional density.   
3. PF is simple to program and executes quickly for small sample sizes.

As we have illustrated with simple examples, pure PF also demonstrates significant weaknesses, and these are not remedied by any suggestions in the research literature of which we are aware. The weaknesses of PF include

1. PF exhibits significant decrease in performance with increasing state dimension.

2. PF displays poor robustness to unmodeled disturbances.

The lack of robustness is a direct outcome of the sampling strategies. Sampling any of the proposed PF importance functions does not locate the samples close to the true state after a significant and unmodeled disturbance. Once the samples are in the wrong place with respect to the peak in the conditional density, they do not recover. If the samples are in the wrong part of the state space, the weights cannot carry the load and represent the conditional density. Resampling does not successfully reposition the particles if they are already out of place. An appeal to sampled density convergence to the true conditional density with increasing sample number is unrealistic. The number of samples required is simply too large for even reasonably small state dimensions considered in applications; $n > 5 0$ is not unusual in applications.

In constructing a class of combined methods we propose to

1. Use MHE to locate/relocate the samples.

2. Use PF to obtain fast recursive estimation between MHE optimizations.
