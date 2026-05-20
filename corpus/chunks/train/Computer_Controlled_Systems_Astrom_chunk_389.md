# Example 6.7 Ship control

When designing an autopilot for a highly maneuverable ship, there are many alternatives for design. One possibility is to design the autopilot so that the captain can order a turn to a new course with a specified turning rate. Another possibility is to specify the turning radius instead of the turning speed. The advantage of specifying the turning radius is that the path of the ship will be independent of the speed of the ship. Control of the turning radius leads to a more complicated system, because it is necessary to measure both turning rate and ship speed.
