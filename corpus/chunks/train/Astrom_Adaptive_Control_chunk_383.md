# Analysis of a Simple Discrete-Time System

To illustrate how the analysis can be done, we discuss a simple example. Consider a discrete-time adaptive controller that is based on estimation of the parameter $\theta$ in the model

$$y (t + 1) = \theta y (t) + u (t) \tag {6.4}$$

Let the controller be

$$u (t) = - \hat {\theta} (t) y (t) + y _ {0} \tag {6.5}$$

where $\hat{\theta}$ is an estimate of $\theta$ and $y_{0}$ the setpoint. If the process is indeed described by Eq. (6.4) and if the estimate $\hat{\theta}$ is correct, the controller gives a deadbeat response. The parameter is estimated by using a normalized gradient algorithm

$$\hat {\theta} (t + 1) = \hat {\theta} (t) + \gamma \frac {y (t) \left(y (t + 1) - \hat {\theta} (t) y (t) - u (t)\right)}{\alpha + y ^ {2} (t)} \tag {6.6}$$

where $\gamma$ and $\alpha$ are parameters. This is equal to Kaczmarz's projection algorithm if $\gamma = 1$ and $\alpha = 0$ .

To analyze the closed-loop system, we must also have a description of the actual process. We assume that this is given by

$$y (t + 1) = \theta_ {0} y (t) + a + u (t) \tag {6.7}$$

Notice that, because of the presence of the parameter $a$ on the right-hand side, this model is different from the model (6.4) used to design the adaptive controller. Equations (6.4), (6.5), (6.6), and (6.7) thus describe a very simple case of adaptive control of a process with a constant unmodeled disturbance. Using Eq. (6.5) to eliminate $u$ in Eqs. (6.6) and (6.7), we find that the closed-loop system can be described by the equations

$$y (t + 1) = \left(\theta_ {0} - \hat {\theta} (t)\right) y (t) + a + y _ {0}\hat {\theta} (t + 1) = \hat {\theta} (t) + \gamma \frac {y (t) \left(\left(\theta_ {0} - \hat {\theta} (t)\right) y (t) + a\right)}{\alpha + y ^ {2} (t)} \tag {6.8}$$

This is a second-order nonlinear system. To explore the behavior of this system, we follow the procedure of nonlinear analysis.

Equilibrium Analysis Equations (6.8) have the equilibrium solution

$$\mathbf {y} = \mathbf {y} _ {0}\hat {\theta} = \theta_ {0} + \frac {a}{y _ {0}} \tag {6.9}$$

Notice that the equilibrium value of the output is always equal to the setpoint in spite of the disturbance. This is a phenomenon that we have observed before in adaptive systems. (Compare with Example 3.5 and Example 5.2.) Unmodeled dynamics, however, give a parameter error.

Linearizing Eqs. (6.8) around the equilibrium equations (6.9), we find that the system matrix is
