# Computer Code

A typical computer code for a discrete PID-controller is given in Listing 8.1 on page 318. The discretization of the integral term is made using a forward difference. The derivative term is approximated using a backward difference. The calculation PID\_Init is made initially only. This saves computing time. In a real system these calculations have to be made each time the parameters are changed. The code given admits bumpless parameter changes if $b = 1$ . When $b \neq 1$ the proportional term (P) is different from zero in steady state. To ensure bumpless parameter changes it is necessary that the quantity P + I is invariant to parameter changes. This means that the state I has to be changed as follows:

$$I _ {\text { new }} = I _ {\text { old }} + K _ {\text { old }} (b _ {\text { old }} u _ {c} - y) - K _ {\text { new }} (b _ {\text { new }} u _ {c} - y) \tag {8.28}$$

Word length and integration offset. The integral part in digital PID-controllers is approximated as a sum. Computational problems, such as integration offset, may then occur due to the finite precision in the representation in the computer. Assume that there is an error, $e(kh)$ . The integrator term is then increased at each sampling time with [see (8.23)]

$$\frac {K h}{T _ {i}} e (k h)$$

Listing 8.1 C code for PID-controller based on Tustin discretization.   
```c
#include<Kernel.h>    /* Import real-time primitives */
/* PID controller based on Tustin discretization */

struct PID_Data {

struct {
    double uc;    /* Input : Set point    */
    double y;    /* Input : Measured variable  */
    double u;    /* Output : Controller output  */
    double v;    /* Output : Limited controller output */
} Signals;

struct {
    double I;    /* Integral part    */
    double D;    /* Derivative part  */
    double yold;    /* Delayed measured variable  */
} States;

struct {
    double K;    /* Controller gain    */
    double Ti;    /* Integral time    */
    double Td;    /* Derivative time  */
    double Tt;    /* Reset time    */
    double N;    /* Maximum derivative gain  */
    double b;    /* Fraction of setpoint in prop. term */
    double ulow;    /* Low output limit  */
    double uhigh;    /* High output limit  */
    double h;    /* Sampling period  */
    double bi, ar, bd, ad;
} Par;
} pid_data;
