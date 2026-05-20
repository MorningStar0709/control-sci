# 16.1 1-DOF systems

1-DOF systems are straightforward. We define the minimum and maximum position constraints for the arm, elevator, etc. and ensure we stay between them. To do so, we might use some combination of:

1. Rejecting, coercing, or clamping setpoints so that they are always within the valid range   
2. Soft limits on the speed controller   
3. Limit switches, and/or physical hard stops
