# Plot phase trajectory
plt.figure(2)
plt.plot(y1[0][0], y1[1][0])
plt.grid(True)
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.title("Phase" Plot (x vs xdot)') 
```

Recall the second state space equation is

$$y = C x + D u$$

to get the data for our subspace plot let

$$
C = \left[ \begin{array}{l} 0, 0, 1, 0 \\ 0, 0, 0, 1 \end{array} \right]
$$

Recall that $x _ { 1 }$ is the road surface height, $x _ { 2 }$ is the wheel axis height, and $x _ { 3 }$ is the car body height. This C matrix selects out the last two elements of X, $Y = [ x _ { 3 } , \dot { x } _ { 3 } ]$ (line 42,43). Then using the same system (lines 12-41) and simulation output (line 45), we plot the two elements of Y against each other (line 106) on a new gure.
