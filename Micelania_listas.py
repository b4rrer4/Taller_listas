def Mostrarmenu():
    print('Menu: ')
    print('===LISTAS===')
    print('1. suma de lists')
    print('2. promedio de lists')
    print('3. eliminar secuencia repetida')
    print('4. ordenar list')
    print('===TUPLAS===')
    print('5. ordenar por palabra mas larga')
    print('6. producto de tuplas')
    print('7. mayor y menor de una tupla')
    print('8. diccionario de tupla')
    print('9. buscar indices')
    print('10. separar elementos')
    print('===DICCIONARIOS')
    print('11. contar palabras')
    print('12. promedio de alumnos')
    print('13. SALIR')

while True:
    Mostrarmenu()
    option=int(input('Seleccione alguna opcion: '))
    #lists
    if option==1:
        #suma de list
      def sum_list (list):
         sumar = sum(list)
         return sumar
      inicial_enter=input('ingrese una serie de numeros separado por espacios: ')
      list1= inicial_enter.split()
      list1=[int(num)for num in list1]
      result=sum_list(list1)
      print(result)
    if option==2:
       def promedio (list2):
          suma2= sum(list2)
          cant_datos=len(list2)
          promed=suma2/cant_datos
          return promed
       inicial_enter=input('ingrese una serie de numeros separado por espacios: ')
       list2= inicial_enter.split()
       list2=[int(num)for num in list2]       
       result_pro=promedio(list2)
       print(result_pro)
    if option==3:
       #eliminar secuencias repetidas
       inicial_enter=input('ingrese una serie separado por espacios: ')
       list3= inicial_enter.split()
       list3=[num for num in list3]
       for num in list3:
          if list3.count(num)>1:
             list3.remove(num)
       print(list3)
    if option==4:
       #ordenar list
       inicial_enter=input('ingrese una serie de numeros separado por espacios: ')
       list4= inicial_enter.split()
       list4=[int(num) for num in list4]
       list_ordenada=[]
       while list4:
          first=min(list4)
          list_ordenada.append(first)
          list4.remove(first)
       print(list_ordenada)
#tuplas
    if option==5:
       #ordenar por palabra mas larga
       def major(tupla1):
          elements = ''
          max_long=0
          for w in tupla1:
             word=len(w)
             if word > max_long:
                max_long  = word
                elements = w
          return elements
          
       inicial_enter=input('ingrese una serie de palabras separado por espacios: ')
       elements=inicial_enter.split()
       tupla1=(elements)
       result2=major(tupla1)
       print(result2)
    if option==6:
       #producto de tuplas
       def product(tupla2):
          mul= 1
          for num in tupla2:
             mul *= num
          return mul
       tupla2=(3,5,6,7,8,9)
       result3= product(tupla2)
       print('la tupla es: ', tupla2 )
       print('el resultado es: ',result3)
    if option==7:
       #mayor y menor de una tupla
       tupla3=(74,57,21,96,50,23)
       print('la tupla es: ', tupla3)
       print('el valor minimo es: ',min(tupla3))
       print('el valor maximo es: ',max(tupla3))
    if option==8:
       #diccionario de tupla
       def reply (tupla4):
          diccionary={}
          for word in tupla4:
             if word in diccionary:
                diccionary[word]+=1
             else:
                diccionary[word]=1
          return diccionary
       inicial_enter=input('ingrese una serie de palabras separado por espacios: ')
       elements=inicial_enter.split()
       tupla4=(elements)
       result4=reply(tupla4)
       print(result4)
    if option==9:
       #buscar indices
       def search(tupla5,element):
          list5=[]
          for index in range(len(tupla5)):
             if tupla5[index]==element:
                list5.append(index)
          return list5
       tupla5=(5,7,8,9,2,6,2,7,0,2,4,1,5,2)
       element=2
       result5=search(tupla5,element)
       print('la tupla es:', tupla5)
       print(result5)
    if option==10:
       #separar elementos
       def chains (tupla6):
          volwels=('a','e','i','o','u')
          chain1=[]
          chain2=[]
          for chain in tupla6:
             if chain[0].lower() in volwels:
                chain1.append(chain)
             else:
                chain2.append(chain)
          return tuple(chain1) , tuple(chain2)
       inicial_enter=input('ingrese una serie de palabras separado por espacios: ')
       elements=inicial_enter.split()
       tupla6=(elements)
       first_,first_no=chains(tupla6)
       print(first_)
       print(first_no)
#diccionarios
    if option ==11:
       #contar palabras 
       def count (listas):
          diccionary2={}
          for word in listas:
             if word in diccionary2:
                diccionary2[word]+=1
             else:
                diccionary2[word]=1
          return diccionary2
       inicial_enter=input('ingrese una serie separado por espacios: ')
       listas= inicial_enter.split()
       listas=[word for word in listas]
       print(count(listas))
    if option == 12:
       #promedio de alumnos
       def average (qualifications):
          total=0
          cant_estudents=len(qualifications)
          for estudents, qualification in qualifications.items():
             total+=qualification
          promed=total/cant_estudents
          return promed
       estudents={
          'Juan':5.0,
          'Laura':3.0,
          'Andres':4.5,
          'Sofia':2.0
       }
       prom=average(estudents)
       print(estudents)
       print(prom)
    if option ==13:
       break
