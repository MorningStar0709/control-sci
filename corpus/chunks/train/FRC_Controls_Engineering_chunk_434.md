# 16.3 Waypoint planning

Our first example has 2 DOFs where all of the constraints are independent (minimum/maximum limits on each axis), as shown in figure 16.1.

Motion planning and control in this example is simple; just make sure all controller references are always inside the box of valid states.

Now let’s make it more interesting. Say that if the arm is near the middle of travel (pointing straight down), the elevator must be above a certain height. Otherwise, the arm intersects the robot chassis. This configuration space would look like figure 16.2.

Let’s consider motion planning in the second example. Say the current state of our system is x and our goal state is r as shown in figure 16.3.

Notice that the elevator height at the current state and the goal is identical. Do we just have to move the arm? Moving this way will sweep the system into the constraint we defined for preventing self-intersection with the chassis. Instead, we need to plan a sequence of references to execute that only pass through valid states. Figure 16.4 shows an example.

a and b are intermediate waypoints we added to ensure that the whole system moves in a safe manner. Considering again our toy example, the elevator goes up, then the arm rotates underneath, then the elevator goes back down. There are many possible ways to generate this path (or other valid paths), including some sort of search (discretize the plot into a grid and find a valid path using breadth-first search or A\*) or hard-coded rules to handle different regions of the constraint space.

![](image/d6a38689ba69c78756b0041c753c40c80455d9774c3d5ea113b5c192b7b0680f.jpg)

<details>
<summary>scatter</summary>

| Arm angle (rad) | Elevator height (m) | Status        |
| --------------- | ------------------- | ------------- |
| -2.5            | 5                   | Valid states  |
| 2.5             | 5                   | Valid states  |
| -2.5            | 0                   | Valid states  |
| 2.5             | 0                   | Valid states  |
</details>

Figure 16.1: Elevator-arm configuration space with independent constraints

![](image/7f967276ee7d45e0e565a63df1044fde1c8e674fd1b3e9e997763e32501f4ad4.jpg)

<details>
<summary>heatmap</summary>

| Arm angle (rad) | Elevator height (m) | Status        |
| --------------- | ------------------- | ------------- |
| -2.5            | 5                   | Valid states  |
| -1.5            | 0                   | Valid states  |
| -0.5            | 2                   | Invalid states|
| 0.5             | 0                   | Valid states  |
| 1.5             | 0                   | Valid states  |
| 2.5             | 5                   | Invalid states|
| 3.0             | 0                   | Valid states  |
</details>
