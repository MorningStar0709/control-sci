# S-curve profile

The S-curve profile equations also include jerk.

$$x (t) = x _ {0} + v _ {0} t + \frac {1}{2} a t ^ {2} + \frac {1}{6} j t ^ {3}v (t) = v _ {0} + a t + \frac {1}{2} j t ^ {2}a (t) = a _ {0} + j t$$

where j is the jerk at time t, a(t) is the acceleration at time t, and a is the initial acceleration.

Snippet 15.2 shows a Python implementation.

```python
"""Function for generating an S-curve profile."""
import math

def generate_s_curve_profile(max_v, max_a, time_to_max_a, dt, goal):
    """
    Returns an s-curve profile with the given constraints.

    Parameter ``max_v``:
    Maximum velocity of profile. 
```

```txt
Parameter `max_a`:
Maximum acceleration of profile.

Parameter `time_to_max_a`:
Time from rest to maximum acceleration.

Parameter `dt`:
Timestep.

Parameter `goal`:
Final position when the profile is at rest.

Returns:
t_rec -- List of timestamps.
x_rec -- List of positions at each timestep.
v_rec -- List of velocities at each timestep.
a_rec -- List of accelerations at each timestep.

```
t_rec = [0.0]
x_rec = [0.0]
v_rec = [0.0]
a_rec = [0.0]

j = max_a / time_to_max_a
short_profile = max_v * (time_to_max_a + max_v / max_a) > goal

if short_profile:
    profile_max_v = max_a * (
    math.sqrt(goal / max_a - 0.75 * time_to_max_a**2) - 0.5 * time_to_max_a
)
else:
    profile_max_v = max_v
