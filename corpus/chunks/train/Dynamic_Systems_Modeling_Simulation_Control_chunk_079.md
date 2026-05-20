Rearranging these equations with the dynamic variables $( \theta _ { 1 }$ and $\theta _ { 2 } )$ on the left-hand side and the input variable $T _ { \mathrm { i n } } ( t )$ on the right-hand side, we have

$$J _ {1} \ddot {\theta} _ {1} + b \dot {\theta} _ {1} + k (\theta_ {1} - \theta_ {2}) = - T _ {\mathrm{in}} (t) \tag {2.47a}J _ {2} \ddot {\theta} _ {2} + b \dot {\theta} _ {2} + k (\theta_ {2} - \theta_ {1}) = T _ {\mathrm{in}} (t) \tag {2.47b}$$

Equations (2.47a) and (2.47b) represent the mathematical model of the dual-disk generator system. Because we have two inertia elements, the complete model consists of two coupled, second-order ODEs. The model is linear, as we have assumed linear stiffness and damper elements. Note that all terms pertaining to the angular acceleration, velocity, and position of disk $J _ { 1 }$ in Eq. (2.47a) have the same sign; similarly, all terms associated with $\theta _ { 2 }$ (and its derivatives) in Eq. (2.47b) have the same sign. This characteristic holds for inherently stable systems, and the reader is encouraged to use this sign check to verify that their FBD and algebra steps have led to the correct mathematical model.

We may rewrite the mathematical model in terms of the relative angular displacement between the cylinder disk $J _ { 2 }$ and the piston disk $J _ { 1 }$ , that is, $\Delta \theta = \theta _ { 2 } - \theta _ { 1 }$ . Subtracting Eq. (2.47a) from Eq. (2.47b) yields

$$J _ {2} \ddot {\theta} _ {2} - J _ {1} \ddot {\theta} _ {1} + b (\dot {\theta} _ {2} - \dot {\theta} _ {1}) + 2 k (\theta_ {2} - \theta_ {1}) = 2 T _ {\mathrm{in}} (t)$$

Because the piston and cylinder inertias are equal (the dual-disk system is balanced), we can substitute $J = J _ { 1 } = J _ { 2 }$ . Furthermore, we can substitute the relative angular displacement variable $\Delta \theta = \theta _ { 2 } - \theta _ { 1 }$ and its derivatives $\dot { \Delta \theta } = \dot { \theta } _ { 2 } - \dot { \theta } _ { 1 }$ and $\Delta \ddot { \theta } = \ddot { \theta } _ { 2 } - \ddot { \theta } _ { 1 }$ to yield

$$J \Delta \ddot {\theta} + b \Delta \dot {\theta} + 2 k \Delta \theta = 2 T _ {\mathrm{in}} (t) \tag {2.48}$$
