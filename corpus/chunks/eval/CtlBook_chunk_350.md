# 10.2 Overview

We will use two python scripts to search the three dimensional space dened by

$$K _ {P}, K _ {I}, K _ {D}$$

for the best design. We can dene the best design according to various Performance Criteria. We will look at the most common performance criteria, and one additional criterion: control eort which has large practical eects on system designs. s

 Settling Time, $T _ { S }$   
 Percent Overshoot, %OS   
 Steady State Error, SSE.   
 Control Eort, cu.   
 Gain Margin, gm.

We supply a set of python methods or code which can analyze a step response and determine $T _ { S }$ and %OS. The functions are

 ts = settletime(t,y)

 o = PCTovershoot(t,y)   
 sse =steady\_state\_error(t, y)   
 Cu = ctl\_eff(sys)

 Gain margin is computed by the python function margin().

Steady state error is approximated by the nal value in the step response, and we compute maximum control eort by simulating the system again using the equation in Section 9.4.
