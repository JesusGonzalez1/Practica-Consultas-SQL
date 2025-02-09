Buenos dias, tardes o noches compañero.
Esta es una corta practica que realice, en un curso de SQLite.

Este código combina SQLite, Pandas y Matplotlib para analizar datos de una base de datos (Nortwith.db). Extrae información clave sobre productos y empleados, y la visualiza en
gráficos de barras. Primero, se importan las librerías necesarias: sqlite3 para conectarse a la base de datos, pandas para manejar los datos de manera eficiente y matplotlib.pyplot
para graficar los resultados. Luego, se establece la conexión con la base de datos usando sqlite3.connect(), almacenándola en la variable comm.

Para obtener los 10 productos más rentables, se ejecuta una consulta SQL que combina la tabla OrderDetails con Products mediante JOIN, 
calculando los ingresos (revenue) como la suma de Price * Quantity para cada producto. La consulta agrupa los datos por ProductID, los ordena en orden descendente y selecciona solo 
los 10 más rentables.

Después, se obtiene a los 10 empleados más eficientes con otra consulta SQL. Esta consulta combina las tablas Orders y Employees, concatenando FirstName y LastName para obtener
el nombre completo de cada empleado. Luego, se cuenta cuántas órdenes ha gestionado cada uno, agrupándolos por EmployeeID y ordenando los resultados de mayor a menor.
