# Linear vs. Nonlinear Systems

Suppose we have a system or input-output relationship that is described by the function $y = f ( u )$ where u is the input and y is the output. Linear systems obey the superposition property:

$1 . \ { \mathrm { I f } } \ y _ { 1 } = f ( u _ { 1 } ) , { \mathrm { t h e n } } \ a y _ { 1 } = f ( a u _ { 1 } ) , { \mathrm { w h e r e } } \ a = { \mathrm { a n y ~ c o n s t a n t } } .$   
$2 . \mathrm { ~ I f ~ } y _ { 1 } = f ( u _ { 1 } ) \mathrm { ~ a n d ~ } y _ { 2 } = f ( u _ { 2 } ) , \mathrm { t h e n ~ } y _ { 1 } + y _ { 2 } = f ( u _ { 1 } + u _ { 2 } ) .$

Consider again the DC motor example: suppose we apply 12 volts (V) to a motor and through measurements determine the steady-state (constant) angular velocity to be 1600 revolutions per minute (rpm). Next, if we apply 6 V to the motor and the measured steady-state angular velocity is 800 rpm then the system obeys the first superposition property and the DC motor system is linear. Of course, a physical system that demonstrates linearity (such as the DC motor) has a limited linear range of operation; that is, we cannot increase the input voltage by a factor of 100 and expect the corresponding angular velocity to increase by a factor of 100. Increasing the system input beyond a threshold may cause the output to saturate (i.e., reach a limit) and, therefore, the system is no longer linear.

The second superposition property shows that the total dynamic response of a linear system can be obtained by adding or superimposing the responses (or solutions) to individual input functions. Nonlinear systems do not obey either superposition property.

The following equations are examples of linear ODEs:

$$\ddot {x} + 3 \dot {x} - 4 0 x = 6 u \tag {1.1}2 \ddot {x} + 0. 4 \dot {x} + 0. 6 e ^ {- 2 t} x = - 8 u \tag {1.2}$$

Equation (1.1) is a second-order linear ODE because the dynamic variable x and its derivatives appear as linear combinations (we will use the over-dot notation to denote derivatives with respect to time; hence ${ \dot { x } } =$ $d x / d t , \ddot { x } = d ^ { 2 } x / d t ^ { 2 }$ , etc). Equation (1.1) involves constant coefficients and hence it is a linear time-invariant (LTI) differential equation. Equation (1.2) is linear as x and its derivatives appear in linear combinations. Because the coefficient $0 . 6 e ^ { - 2 t }$ changes with time, Eq. (1.2) is a linear time-varying ODE. The following equation

$$2 \ddot {x} + 3 \dot {x} + 1 6 x ^ {2} = 5 u \tag {1.3}$$

is a nonlinear ODE because of the $x ^ { 2 }$ term.

All physical systems are nonlinear. However, if we confine the input-output variables to a restricted (nominal) range, then we can often replace a nonlinear system with a linear model comprising linear differential equations. This important process is called linearization. Obtaining a linear model is extremely important and advantageous in system analysis because it is possible to obtain the analytical (closed-form) solution to linear ODEs. Nonlinear systems must be solved by using numerical methods to integrate the ODEs.
