This theory requires considerations based on frequency-response analysis and timedomain analysis. Because of the mathematical complications associated with robust control theory, detailed discussion of robust control theory is beyond the scope of the senior engineering student. In this section, only introductory discussion of robust control theory is presented.

Uncertain Elements in Plant Dynamics. The term uncertainty refers to the differences or errors between the model of the plant and the actual plant.

Uncertain elements that may appear in practical systems may be classified as structured uncertainty and unstructured uncertainty. An example of structured uncertainty is any parametric variation in the plant dynamics, such as variations in poles and zeros of the plant transfer function. Examples of unstructured uncertainty include frequencydependent uncertainty, such as high-frequency modes that we normally neglect in modeling plant dynamics. For example, in the modeling of a flexible-arm system, the model may include a finite number of modes of oscillation.The modes of oscillation that are not included in the modeling behave as uncertainty of the system. Another example of uncertainty occurs in the linearization of a nonlinear plant. If the actual plant is nonlinear and its model is linear, then the difference acts as unstructured uncertainty.

In this section we consider the case where the uncertainty is unstructured. In addition we assume that the plant involves only one uncertainty. (Some plants may involve multiple uncertain elements.)

In the robust control theory, we define unstructured uncertainty as $\Delta ( s )$ . Since the exact description of $\Delta ( s )$ is unknown, we use an estimate of $\Delta ( s )$ (as to the magnitude and phase characteristics) and use this estimate in the design of the controller that stabilizes the control system. Stability of a system with unstructured uncertainty can then be examined by use of the small gain theorem to be given following the definition of the $H _ { \infty }$ norm.

$\pmb { H } _ { \infty }$ Norm. The $H _ { \infty }$ norm of a stable single-input–single-output system is the largest possible amplification factor of the steady-state response to sinusoidal excitation.

For a scalar $\Phi ( s ) , \| \Phi \| _ { \infty }$ gives the maximum value of $| \Phi ( j \omega ) |$ . It is called the- $H _ { \infty }$ norm. See Figure 10–41.
