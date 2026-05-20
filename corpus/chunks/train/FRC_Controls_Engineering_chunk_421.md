# Trapezoid profile

The trapezoid profile uses the following equations.

$$x (t) = x _ {0} + v _ {0} t + \frac {1}{2} a t ^ {2}v (t) = v _ {0} + a t$$

where $x ( t )$ is the position at time t, $x _ { 0 }$ is the initial position, $v _ { 0 }$ is the initial velocity, and a is the acceleration at time t.

Snippet 15.1 shows a Python implementation.

"""Function for generating a trapezoid profile."""

import math

def generate\_trapezoid\_profile(max\_v, time\_to\_max\_v, dt, goal):

Creates a trapezoid profile with the given constraints.

Parameter \`\`max\_v\`\`: Maximum velocity of profile.

Parameter \`\`time\_to\_max\_v\`\`: Time from rest to maximum velocity.

Parameter \`\`dt\`\`: Timestep.

Parameter \`\`goal\`\`: Final position when the profile is at rest.

Returns: t\_rec List of timestamps. x\_rec List of positions at each timestep. v\_rec - List of velocities at each timestep. a\_rec List of accelerations at each timestep.

t\_rec = [0.0] x\_rec = [0.0] v\_rec = [0.0] a\_rec = [0.0]

a = max\_v / time\_to\_max\_v time\_at\_max\_v = goal / max\_v - time\_to\_max\_v

\# If profile is short if max\_v \* time\_to\_max\_v > goal: time\_to\_max\_v = math.sqrt(goal / a) time\_from\_max\_v = time\_to\_max\_v time\_total = 2.0 \* time\_to\_max\_v profile\_max\_v = a \* time\_to\_max\_v else:

```python
time_from_max_v = time_to_max_v + time_at_max_v
time_total = time_from_max_v + time_to_max_v
profile_max_v = max_v

while t_rec[-1] < time_total:
    t = t_rec[-1] + dt
    t_rec.append(t)
    if t < time_to_max_v:
    # Accelerate up
    a_rec.append(a)
    v_rec.append(a * t)
    elif t < time_from_max_v:
    # Maintain max velocity
    a_rec.append(0.0)
    v_rec.append(profile_max_v)
    elif t < time_total:
    # Accelerate down
    decel_time = t - time_from_max_v
    a_rec.append(-a)
    v_rec.append(profile_max_v - a * decel_time)
    else:
    a_rec.append(0.0)
    v_rec.append(0.0)
    x_rec.append(x_rec[-1] + v_rec[-1] * dt)
return t_rec, x_rec, v_rec, a_rec 
```  
Snippet 15.1. Trapezoid profile implementation in Python
