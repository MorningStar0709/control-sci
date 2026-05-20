# E.6 Phase loss

Implementing a discrete control system is easier than implementing a continuous one, but discretization has drawbacks. A microcontroller updates the system input in discrete intervals of duration $T ;$ it’s held constant between updates. This introduces an average sample delay of $\textstyle { \frac { T } { 2 } }$ that leads to phase loss in the controller. Phase loss is the reduction of phase margin that occurs in digital implementations of feedback controllers from sampling the continuous system at discrete time intervals. As the sample rate of the controller decreases, the phase margin decreases according to $- \frac { T } { 2 } \omega$ where $T$ is the sample period and $\omega$ is the frequency of the system dynamics. Instability occurs if the phase margin of the system reaches zero. Large amounts of phase loss can make a stable controller in the continuous domain become unstable in the discrete domain. Here are a few ways to combat this.

• Run the controller with a high sample rate.   
• Designing the controller in the analog domain with enough phase margin to compensate for any phase loss that occurs as part of discretization.   
• Convert the plant to the digital domain and design the controller completely in the digital domain.
