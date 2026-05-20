We overcome the potentially expensive MHE optimization by using PF to process the measurements and provide rapid online estimates while an MHE computation is underway. We position the samples in regions of high conditional density after every run of the MHE optimization, which allows recovery from unmodeled disturbances as soon as an MHE computation completes. A challenge that is not addressed is the appearance of multiple peaks in the conditional density when using nonlinear models. Handling the multimodal conditional density remains a challenge for any online, and indeed offline, state estimation procedure.

Next we propose a specific state estimator in this general MHE/PF class and examine its performance with some simple computational examples. Because this class of estimators is new, we fully expect significant modifications and improvements to come along. At this early juncture we expect only to be able to illustrate some of the new capabilities of the approach.

Let $\hat { Z } _ { k } ( x )$ denote the MHE arrival cost function given in Definition 4.16. We let $\hat { V } _ { k } ^ { 0 }$ denote the optimal cost and x(k) ˆ the optimal estimate of the last stage at time k. We consider the quadratic approximation of

$\hat { Z } _ { k } ( \cdot )$ at the optimum x(k) ˆ

$$V (x) = V _ {k} ^ {0} (\hat {x} (k)) + (1 / 2) (x - \hat {x} (k)) ^ {\prime} H (x - \hat {x} (k))$$

in which H is the Hessian of $\hat { Z } _ { k } ( x )$ evaluated at the optimum ${ \hat { x } } ( k )$ . We use this function as an importance function for sampling the conditional density. Notice that this procedure is not the same as assuming the conditional density itself is a normal distribution. We are using $N ( \hat { x } ( k ) , H ^ { - 1 } )$ strictly as an importance function for sampling the unknown conditional density. The samples $x _ { i } ( k )$ are drawn from $N ( \hat { x } ( k ) , H ^ { - 1 } )$ ). The weights are given by

$$w _ {i} (k) = V (x _ {i} (k)) \quad \overline {{{w}}} _ {i} (k) = \frac {w _ {i} (k)}{\sum_ {j} w _ {j} (k)} \tag {4.61}$$

and the sampled density is given by

$$p _ {s} (x) = \{x _ {i} (k), \overline {{w}} _ {i} (k) \}$$

If the conditional density is well represented by the normal approximation, then the normalized weights are all nearly equal to 1/s. The MHE cost function modifies these ideal weights as shown in (4.61).
