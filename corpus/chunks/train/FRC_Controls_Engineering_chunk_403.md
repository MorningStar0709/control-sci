# 14.2.1 Simple system identification

This system identification method is easier but less accurate than OLS. It requires two tests.

1. Starting from rest, slowly increase the voltage from zero until the robot moves.   
2. Starting from rest, apply a constant voltage u sufficiently larger than $K _ { s }$ until the steady-state velocity v is reached, and measure the instantaneous acceleration from rest a.

The feedforward gains from equation (14.2) are given by

$$K _ {s} = \text { minimum voltage causing movement in test } 1K _ {v} = \frac {u - K _ {s}}{v}K _ {a} = \frac {u - K _ {s} - K _ {v} v}{a}$$

Acceleration may be difficult to accurately measure in test 2. A reasonable estimate is the largest observed value of $\frac { v _ { k } - v _ { k - 1 } } { \Delta T }$ where $v _ { k }$ and $v _ { k - 1 }$ are adjacent velocity samples and $\Delta T$ is the sample period. Systems with very high accelerations may have a negligibly small $K _ { a }$ .
