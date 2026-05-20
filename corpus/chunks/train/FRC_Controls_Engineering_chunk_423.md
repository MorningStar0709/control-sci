# Find times at critical points
t2 = profile_max_v / max_a
t3 = t2 + time_to_max_a
if short_profile:
    t4 = t3
else:
    t4 = goal / profile_max_v
t5 = t4 + time_to_max_a
t6 = t4 + t2
t7 = t6 + time_to_max_a
time_total = t7

while t_rec[-1] < time_total:
    t = t_rec[-1] + dt
    t_rec.append(t)
    if t < time_to_max_a:
    # Ramp up acceleration
    a_rec.append(j * t)
    v_rec.append(0.5 * j * t**2)
    elif t < t2:
    # Increase speed at max acceleration
    a_rec.append(max_a)
    v_rec.append(max_a * (t - 0.5 * time_to_max_a))
    elif t < t3:
    # Ramp down acceleration 
```

```python
a_rec.append(max_a - j * (t - t2))
v_rec.append(max_a * (t - 0.5 * time_to_max_a) - 0.5 * j * (t - t2) ** 2)

elif t < t4:
    # Maintain max velocity
    a_rec.append(0.0)
    v_rec.append(profile_max_v)

elif t < t5:
    # Ramp down acceleration
    a_rec.append(-j * (t - t4))
    v_rec.append(profile_max_v - 0.5 * j * (t - t4) ** 2)

elif t < t6:
    # Decrease speed at max acceleration
    a_rec.append(-max_a)
    v_rec.append(max_a * (t2 + t5 - t - 0.5 * time_to_max_a))

elif t < t7:
    # Ramp up acceleration
    a_rec.append(-max_a + j * (t - t6))
    v_rec.append(
    max_a * (t2 + t5 - t - 0.5 * time_to_max_a) + 0.5 * j * (t - t6) ** 2

else:
    a_rec.append(0.0)
    v_rec.append(0.0)
x_rec.append(x_rec[-1] + v_rec[-1] * dt)

return t_rec, x_rec, v_rec, a_rec 
```  
Snippet 15.2. S-curve profile implementation in Python
