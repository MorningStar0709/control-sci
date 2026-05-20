# 7.2.1 Sample delay

Implementing a discrete control system is easier than implementing a continuous one, but discretization has drawbacks. A microcontroller updates the system input in discrete intervals of duration T ; it’s held constant between updates. This introduces an average sample delay of $\textstyle { \frac { T } { 2 } }$ . Large delays can make a stable controller in the continuous domain become unstable in the discrete domain since it can’t react as quickly to output changes. Here are a few ways to combat this.

• Run the controller with a high sample rate.   
• Designing the controller in the analog domain with enough phase margin to compensate for any phase loss that occurs as part of discretization.   
• Convert the plant to the digital domain and design the controller completely in the digital domain.
