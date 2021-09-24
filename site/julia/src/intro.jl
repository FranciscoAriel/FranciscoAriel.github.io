# Lectura de datos

using CSV, DataFrames

bd = CSV.read("C:\\Users\\Francisco\\fake_db.csv",DataFrame)
# Exploración de la base
summary(bd)
first(bd,5)
last(bd,5)
# Accede a las columnas
bd[:,"GivenName"]
bd[:,5]

# Accede a los renglones
bd[1:3,:]
mini_bd =bd[[2,4,6],[2,5]]

# buscar elementos

getindex(bd,3,"GivenName")