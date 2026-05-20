# Example 2.10 cont.

Note what we have done under Collect Variables above is to simply collect terms according to the motion variables in a systematic way. Specically we can stay organized by lling out a table re-arranging the EOMs as follows:

<table><tr><td>Eqn#</td><td> $\ddot{x}_{j}$ </td><td> $\dot{x}_{1}$ </td><td> $x_{1}$ </td><td> $\dot{x}_{2}$ </td><td> $x_{2}$ </td><td> $\dot{x}_{3}$ </td><td> $x_{3}$ </td><td>=</td></tr><tr><td>(1)</td><td> $M_{w}\ddot{x}_{2}$ </td><td>0</td><td> $(-K_{T})$ </td><td> $B_{S}$ </td><td> $(K_{T}+K_{S})$ </td><td> $(-B_{S})$ </td><td> $(-K_{S})$ </td><td>0</td></tr><tr><td>(2)</td><td> $M_{v}\ddot{x}_{3}$ </td><td>0</td><td>0</td><td> $(-B_{S})$ </td><td> $(-K_{S})$ </td><td> $B_{S}$ </td><td> $K_{S}$ </td><td>0</td></tr></table>

Note that our system equations seem to lack an input (which would be on the right-hand-side i.e. the last column of our tabular form). Thinking back to cars, the input would be changes in road height, x1 (which is not attached to a mass). We can thus re-do the table to move x1 terms to the right hand side:

<table><tr><td>Eqn#</td><td> $\ddot{x}_{j}$ </td><td> $\dot{x}_{1}$ </td><td> $x_{1}$ </td><td> $\dot{x}_{2}$ </td><td> $x_{2}$ </td><td> $\dot{x}_{3}$ </td><td> $x_{3}$ </td><td>=</td></tr><tr><td>(1)</td><td> $M_{w}\ddot{x}_{2}$ </td><td>0</td><td>0</td><td> $B_{S}$ </td><td> $(K_{T}+K_{S})$ </td><td> $(-B_{S})$ </td><td> $(-K_{S})$ </td><td> $K_{T}x_{1}$ </td></tr><tr><td>(2)</td><td> $M_{v}\ddot{x}_{3}$ </td><td>0</td><td>0</td><td> $(-B_{S})$ </td><td> $(-K_{S})$ </td><td> $B_{S}$ </td><td> $K_{S}$ </td><td>0</td></tr></table>

This tabular method will be useful later when we derive state space system equations.

Getting back to the transfer function:

$$
\begin{array}{l} M _ {w} M _ {v} s ^ {4} + M _ {w} B _ {s} s ^ {3} + M _ {w} K _ {s} s ^ {2} \\ + M _ {v} B _ {s} s ^ {2} + \frac {B _ {s} ^ {2} s ^ {2}}{B _ {s} k _ {s} s} + B _ {s} k _ {s} s \\ + (K _ {T} + K _ {S}) \mu_ {v} s ^ {2} + B _ {s} (K _ {T} + K _ {S}) s + K _ {S} (K _ {T} + K _ {S}) \\ \frac {- B _ {s} ^ {2} S ^ {2}}{- \frac {B _ {s} K _ {0} S}{B _ {s} K _ {0} S}} - \frac {K _ {0} ^ {2}}{K _ {0} S} \\ \end{array}

\begin{array}{r l} {M _ {\omega} M _ {\nu} s ^ {4} + B _ {s} (M _ {\omega} + M _ {\nu}) s ^ {3} + [ M _ {\omega} k _ {s} + M _ {\nu} (k _ {T} + k _ {s}) ] s ^ {2} + B _ {T} k _ {s} s + K _ {s} k _ {T}} \\ {X _ {3} (s)} & {= K _ {T} X _ {1} (s) (B _ {s} s + K _ {s})} \end{array}
\frac {X _ {3} (s)}{X _ {1} (s)} = \frac {K _ {T} B _ {S}}{M _ {w} M _ {v}} \frac {(s + \frac {K _ {S}}{B _ {S}})}{s ^ {4} + (\frac {B _ {S}}{M _ {w}} + \frac {B _ {S}}{M _ {w}}) s ^ {3} + (\frac {K _ {S}}{M _ {v}} + \frac {(K _ {T} + K _ {S})}{M _ {w}}) s ^ {2} + \frac {B _ {T} K _ {S}}{M _ {1} M _ {2}} s + \frac {K _ {S} K _ {T}}{M _ {w} M _ {v}}}
$$
