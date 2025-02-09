import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

comm = sqlite3.connect("Nortwith.db")

#Obteniendo los 10 productos mas rentables
query = """SELECT ProductName, SUM(Price * Quantity) as revenue 
        FROM OrderDetails od
        JOIN Products p ON p.ProductID = od.ProductID
        GROUP BY od.ProductID
        ORDER BY Revenue DESC 
        LIMIT 10"""

top_product = pd.read_sql_query(query, comm)

top_product.plot(x = "ProductName", y = "revenue", kind = "bar", figsize = (10,5), legend = False)

plt.title("10 Productos mas rentables")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation = 90)
plt.show()


#obteniendo los 10 empleados mas eficientes
query2 = """ 
    SELECT FirstName || " " || LastName as Employee, Count(*) as Total
    FROM Orders o
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    """

top_employee = pd.read_sql_query(query2, comm)

top_employee.plot(x = "Employee", y = "Total", kind = "bar", figsize = (10,5), legend = False)

plt.title("10 empleados mas eficientes")
plt.xlabel("Nombre de empleados")
plt.ylabel("Total vendido")
plt.xticks(rotation = 90)
plt.show()
