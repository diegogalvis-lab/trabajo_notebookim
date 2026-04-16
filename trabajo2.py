#programar de "EL JEFE FINAL"
compañeros = ["daniel", "pinilla","ivdejel","robinson","maicol"]

edades = [15, 15, 15, 16, 14]

musica = ["pop", "salsa","salsa","vallenato","vallenato"]

# promedio d edades

promedio = sum(edades) / len(compañeros)
print ("tu promedio de edades es:", promedio)

# mayores de 15

mayores = [edad for edad in edades if edad if edad > 15]
print ("edades > 15:",mayores)

# fans del rock

fans_rock = [gen for gen in musica if gen == "salsa"]
print("total de gente que les gusta la salsa es:", len(fans_rock))