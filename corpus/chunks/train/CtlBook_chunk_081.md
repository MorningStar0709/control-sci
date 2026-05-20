# Example 2.12

Write the 4 EOMs for the system of Figure 2.5.

Summing forces on each mass:

$$M _ {1} \ddot {x} _ {1} + B _ {3} \dot {x} _ {1} + B _ {2} (\dot {x} _ {1} - \dot {x} _ {2}) + 3 K _ {2} x _ {1} + K _ {3} (x _ {1} - x _ {3}) = 0M _ {2} \ddot {x} _ {2} + B _ {2} (\dot {x} _ {2} - \dot {x} _ {1}) + B _ {1} \dot {x} _ {2} + K _ {1} x _ {2} = 0M _ {3} \ddot {x} _ {3} + B _ {4} \dot {x} _ {3} + K _ {3} (x _ {3} - x _ {1}) + K _ {4} (x _ {3} - x _ {4}) = 0M _ {4} \ddot {x} _ {4} + B _ {5} \dot {x} _ {4} + K _ {4} (x _ {4} - x _ {3}) + K _ {5} x _ {4} = f (t)$$

Now re-organize the equations into tabular form as above (but changing to a vertical table). Each equation (column) is a sum and each row is the coecient of each variable in the rst column.

<table><tr><td>Var</td><td>EOM1</td><td>EOM2</td><td>EOM3</td><td>EOM4</td></tr><tr><td> $M_{j}\ddot{x}_{j}$ </td><td> $M_{1}\ddot{x}_{1}$ </td><td> $M_{2}\ddot{x}_{2}$ </td><td> $M_{3}\ddot{x}_{3}$ </td><td> $M_{4}\ddot{x}_{4}$ </td></tr><tr><td> $\dot{x}_{1}$ </td><td> $(B_{2}+B_{3})$ </td><td> $(-B_{2})$ </td><td>0</td><td>0</td></tr><tr><td> $x_{1}$ </td><td> $(3K_{2}+K3)$ </td><td>0</td><td>0</td><td>0</td></tr><tr><td> $\dot{x}_{2}$ </td><td> $-B_{2}$ </td><td> $B_{2}$ </td><td>0</td><td>0</td></tr><tr><td> $x_{2}$ </td><td>0</td><td> $K_{1}$ </td><td>0</td><td>0</td></tr><tr><td> $\dot{x}_{3}$ </td><td>0</td><td>0</td><td> $B_{3}$ </td><td>0</td></tr><tr><td> $x_{3}$ </td><td> $(-K_{3})$ </td><td>0</td><td> $(K_{3}+K_{4})$ </td><td> $(-K_{4})$ </td></tr><tr><td> $\dot{x}_{4}$ </td><td>0</td><td>0</td><td>0</td><td> $B_{5}$ </td></tr><tr><td> $x_{4}$ </td><td>0</td><td>0</td><td> $(-K_{4})$ </td><td> $(K_{4}+K_{5})$ </td></tr><tr><td>=</td><td>0</td><td>0</td><td>0</td><td> $f(t)$ </td></tr></table>

Remember, each vertical column is an equation. the last line is the right hand side and the rst 9 lines are added to form the right hand side. Taking the rst column as an example:

$$M _ {1} \ddot {x} _ {1} + (B _ {2} + B _ {3}) \dot {x} _ {1} + (3 K _ {2} + K _ {3}) x _ {1} - B _ {2} \dot {x} _ {2} - K _ {3} x _ {3} = 0$$
