def creating_matrix(mutant_matrix,string_mutant):
    #Se crea la matriz haciendo las validaciones respectivas para que los strings sean validos
    for i in range(6):
        string_mutant_coincidence = False
        string = input(f"Ingresa el string {i + 1} conformado por bases nitrogenadas: ")
        string_mutant = string_mutant.upper()
        while len(string) != 6:
            string = input("La secuencia debe contener 6 caracteres seguidos, ingresa de vuelta: ")
            string = string.upper()
        while True:
            for i in string:
                if (i in string_mutant):
                    string_mutant_coincidence = True
                else:
                    string_mutant_coincidence = False
                    break
            if (string_mutant_coincidence == True):
                break
            else:
                string = input("Uno de las bases nitrogenadas no es correcta, ingrese de vuelta: ")
                string = string.upper()
                while len(string) != 6:
                    string = input("La secuencia debe contener 6 caracteres seguidos, ingresa bien: ")
                    string = string.upper()
                continue    
        mutant_matrix.append(string)
        
def is_mutant(dna):
    #Iniciamos en 0 el contador de las secuencias mutantes
    #Primero chequeamos horizontalmente las secuencias iterando sobre las 6 filas en los primeros 3 elementos viendo si 3 posiciones para adelante se puede encontrar una secuencia
    mutant_secuence = 0
    for i in range(6):
        for j in range(3):
            coincidences = 0
            auxiliar_variablej = j
            for k in range(3):
                if (dna[i][auxiliar_variablej + 1] == dna[i][auxiliar_variablej]):
                    coincidences += 1
                else:
                    pass
                auxiliar_variablej += 1
            if (coincidences == 3):
                mutant_secuence += 1
            else:
                pass
    #De manera similar buscamos las secuencias en posicion vertical iterando sobre las 6 columnas de la matriz de ADN, iterando sobre los primeros 3 elementos de cada columna y en cada uno de los elementos vemos si 3 posiciones adelante se encuentran coincidencias para confirmar secuencias mutantes
    for i in range(6):
        for j in range(3):
            coincidences = 0
            auxiliar_variablej = j
            for k in range(3):
                if (dna[auxiliar_variablej + 1][i] == dna[auxiliar_variablej][i]):
                    coincidences += 1
                else:
                    pass
                auxiliar_variablej += 1
            if (coincidences == 3):
                mutant_secuence += 1
            else:
                pass
    #Ahora veremos si existen secuencias de ADN mutantes diagonalmente iterando sobre las mismas y viendo si existen secuencias similarmente a las busquedas anteriores
    #buscaremos secuencias en todas las diagonales de la matriz
    for i in range(6):
        for j in range(6):
            coincidences = 0
            auxiliar_variablei, auxiliar_variablej = i, j

            # Diagonal principal (izquierda a derecha)
            for k in range(4):
                if auxiliar_variablei < 6 and auxiliar_variablej < 6 and dna[auxiliar_variablei][auxiliar_variablej] == dna[i][j]:
                    coincidences += 1
                    auxiliar_variablei += 1
                    auxiliar_variablej += 1
                else:
                    break
            if coincidences == 4:
                mutant_secuence += 1

            # Diagonal secundaria (derecha a izquierda)
            coincidences = 0
            auxiliar_variablei, auxiliar_variablej = i, j
            for k in range(4):
                if auxiliar_variablei < 6 and auxiliar_variablej >= 0 and dna[auxiliar_variablei][auxiliar_variablej] == dna[i][j]:
                    coincidences += 1
                    auxiliar_variablei += 1
                    auxiliar_variablej -= 1
                else:
                    break
            if coincidences == 4:
                mutant_secuence += 1

            # Diagonal superior izquierda a inferior derecha
            coincidences = 0
            auxiliar_variablei, auxiliar_variablej = i, j
            for k in range(4):
                if auxiliar_variablei < 6 and auxiliar_variablej < 6 and dna[auxiliar_variablei][auxiliar_variablej] == dna[i][j]:
                    coincidences += 1
                    auxiliar_variablei += 1
                    auxiliar_variablej += 1
                else:
                    break
            if coincidences == 4:
                mutant_secuence += 1

            # Diagonal superior derecha a inferior izquierda
            coincidences = 0
            auxiliar_variablei, auxiliar_variablej = i, j
            for k in range(4):
                if auxiliar_variablei < 6 and auxiliar_variablej >= 0 and dna[auxiliar_variablei][auxiliar_variablej] == dna[i][j]:
                    coincidences += 1
                    auxiliar_variablei += 1
                    auxiliar_variablej -= 1
                else:
                    break
            if coincidences == 4:
                mutant_secuence += 1

            # Diagonales superiores izquierda a derecha
            for k in range(4):
                auxiliar_variablei, auxiliar_variablej = i, j
                coincidences = 0
                for l in range(4):
                    if auxiliar_variablei >= 0 and auxiliar_variablei < 6 and auxiliar_variablej >= 0 and auxiliar_variablej < 6:
                        if dna[auxiliar_variablei][auxiliar_variablej] == dna[i][j]:
                            coincidences += 1
                        else:
                            break
                        auxiliar_variablei -= 1
                        auxiliar_variablej += 1
                    else:
                        break
                if coincidences == 4:
                    mutant_secuence += 1

            # Diagonales superiores derecha a izquierda
            for k in range(4):
                auxiliar_variablei, auxiliar_variablej = i, j
                coincidences = 0
                for l in range(4):
                    if auxiliar_variablei >= 0 and auxiliar_variablei < 6 and auxiliar_variablej >= 0 and auxiliar_variablej < 6:
                        if dna[auxiliar_variablei][auxiliar_variablej] == dna[i][j]:
                            coincidences += 1
                        else:
                            break
                        auxiliar_variablei -= 1
                        auxiliar_variablej -= 1
                    else:
                        break
                if coincidences == 4:
                    mutant_secuence += 1

            # Diagonales inferiores izquierda a derecha
            for k in range(4):
                auxiliar_variablei, auxiliar_variablej = i, j
                coincidences = 0
                for l in range(4):
                    if auxiliar_variablei >= 0 and auxiliar_variablei < 6 and auxiliar_variablej >= 0 and auxiliar_variablej < 6:
                        if dna[auxiliar_variablei][auxiliar_variablej] == dna[i][j]:
                            coincidences += 1
                        else:
                            break
                        auxiliar_variablei += 1
                        auxiliar_variablej += 1
                    else:
                        break
                if coincidences == 4:
                    mutant_secuence += 1

            # Diagonales inferiores derecha a izquierda
            for k in range(4):
                auxiliar_variablei, auxiliar_variablej = i, j
                coincidences = 0
                for l in range(4):
                    if auxiliar_variablei >= 0 and auxiliar_variablei < 6 and auxiliar_variablej >= 0 and auxiliar_variablej < 6:
                        if dna[auxiliar_variablei][auxiliar_variablej] == dna[i][j]:
                            coincidences += 1
                        else:
                            break
                        auxiliar_variablei += 1
                        auxiliar_variablej -= 1
                    else:
                        break
                if coincidences == 4:
                    mutant_secuence += 1


    return mutant_secuence
                                







    



        
                
