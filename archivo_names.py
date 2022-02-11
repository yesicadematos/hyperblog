palabras=[]



def  convertir_palabra():
    with open("./palabras.txt", "r", encoding="utf-8") as f:
        for  list in f:     
        # palabras:palabras.upper()
            palabras.append(list)
            # return(palabras)  
        # print(palabras)
    for line in palabras:
        print(line.upper())

# def run():
#   print(palabras_mayuscula)

if __name__ == '__main__':
    convertir_palabra()   







    


