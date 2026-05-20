u=if v<-ulim then -ulim else if v>ulim then ulim else v

```txt
"Parameters
am1:1.4
am2:1
alpha:0
ao:2
ulim:4
END 
```

3.13 Consider the simulation of the continuous-time indirect self-tuning regulator in Example 3.6. Investigate how the transient behavior of the algorithm depends on the initial values of $\theta$ and P.   
3.14 Consider the indirect self-tuning regulator in Example 3.6. Make a simulation, and investigate how the convergence rate depends on the forgetting factor $\alpha$ .   
3.15 Consider the system in Problem 1.9.

(a) Sample the system, and determine a discrete-time controller for the known nominal system such that the specifications are satisfied.   
(b) Use a direct self-tuning controller, and study the transient for different initial conditions and different values of the variable parameters of the system.   
(c) Assume that $e = 0$ and that $u_{c}$ is a square wave. Simulate a self-tuning controller for different prediction horizons.   
(d) Investigate the behavior when the disturbance $d$ is a step. What happens when the controller does not have an integrator?
