# 16.2 Multi-DOF systems

Multi-DOF systems are more complex. In the 2-DOF case (e.g., an arm with a shoulder and a wrist, or an elevator and an arm), each DOF has some limits that are independent of the rest of the system (e.g., min and max angles), but there are also dependent constraints (e.g., if the shoulder is angled down, the wrist must be angled up to avoid hitting the ground). Examples of such constraints could include:

• Minimum/maximum angles   
• Maximum extension rules   
• Robot chassis

• Angles that require an infeasible amount of holding torque

One intuitive way to think about this is to envision an N-D space (2D for 2 DOFs, etc.) where the x and y axes are the positions of the degrees of freedom. A given point (x, y) can either be a valid configuration or an invalid configuration (meaning it violates one or more constraints). So, our 2D plot may have regions (half-planes, rectangles, etc.) representing constraints.
