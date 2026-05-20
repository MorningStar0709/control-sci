# DDC-Packages

Special techniques are used to program control systems consisting of a large number of identical control loops. The code is often structured as follows:

Read all analog inputs and store in a table.

Convert all signals to engineering units and store results in a table.

Apply the control algorithm sequentially to all values in the table using controller parameters stored in a parameter table.

Perform D-A conversion to all variables stored in the output table.

Programs of this type are called DDC-packages. The control algorithms are typically of the PID-type. Modules for gain scheduling, logic, supervision, and adaptation may also be available. The packages are easy to use because all programming is reduced to entering the appropriate data in the tables. Programs of this type are called table-driven.

DDC-packages usually also contain modules, that make it possible to make startup, shutdown, and alarm handling. Today these descriptions are often based on the standard IEC 1131-3 for function-block languages.
