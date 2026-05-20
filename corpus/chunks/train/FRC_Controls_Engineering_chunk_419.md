# 15.1.2 Profile selection

Since trapezoid profiles spend their time at full acceleration or full deceleration, they are, from the standpoint of profile execution, faster than S-curve profiles. However, if this “all on”/“all off” approach causes an increase in settling time, the advantage is lost. Often, only a small amount of “S” (transition between acceleration and no acceleration) can substantially reduce induced vibration. Therefore to optimize throughput, the Scurve profile must be tuned for each a given load and given desired transfer speed.

What S-curve form is right for a given system? On an application by application basis, the specific choice of the form of the S-curve will depend on the mechanical nature of the system and the desired performance specifications. For example, in medical applications which involve liquid transfers that should not be jostled, it would be appropriate to choose a profile with no phase II and VI segment at all. Instead the acceleration transitions would be spread out as far as possible, thereby maximizing smoothness.

In other applications involving high speed pick and place, overall transfer speed is most important, so a good choice might be an S-curve with transition phases (phases I, III, V, and VII) that are five to fifteen percent of phase II and VI. In this case, the S-curve profile will add a small amount of time to the overall transfer time. However, the reduced load oscillation at the end of the move considerably decreases the total effective transfer time. Trial and error using a motion measurement system is generally the best way to determine the right amount of “S” because modeling high frequency dynamics is difficult to do accurately.

Another consideration is whether that “S” segment will actually lead to smoother control of the system. If the high frequency dynamics at play are negligible, one can use the simpler trapezoid profile.

![](image/d92793a5ef256336c0115944cf2a92b74bcd2146148c7b317bb36b77c70a281f.jpg)

S-curve profiles are unnecessary for FRC mechanisms. Motors in FRC effectively have first-order velocity dynamics because the inductance effects are on the order of microseconds; FRC dynamics operate on the order of milliseconds. First-order motor models can achieve the instantaneous acceleration changes of trapezoid profiles because voltage is electromotive force, which is analogous to acceleration. That is, we can instantaneously achieve any desired acceleration with a finite voltage, and we can follow any trapezoid profile perfectly with only feedforward control.
