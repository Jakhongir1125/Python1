# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# ism="jahongir"
# familiya="abdumalikov"
# familiya=familiya.upper()
# yosh=25
# print("Mening ismim",ism.capitalize(),"familiyam",familiya.capitalize(),"yoshim", yosh,"da.")
# .upper()- Katta harflar
# .lower()- Kichik harflar
# .title()- 1-harf katta
# .capitalize()- abzas boshi Katta harf
# .lstrip()- Chapdagi bo'shliqni olib tashlash
# .rstrip()- O'ngdagi bo'shliqni olib tashlash
# .strip()- Chap va o'ngdagi bo'shliqni olib tashlash


# ####  /////// INPUT ////// INPUT /////
# ism=input("Ismingiz nima ")
# print("Salom "+ism)
# print("Yaramas, nomard "+ism.upper())
# yosh=input("Yoshingiz nechida ")
# print("Qarib ketibsanu qachon uylanasan yoshing ham",int(yosh),"da ekan. ")
# print("Sen tengilarni allaqachon sen tengi ikkitadan bollari bor")

# imya=input("Ваше имя: ")
# familiya=input("Ваша Фамилия "+imya.title()+": ")
# ish=input("Ваша профессия "+imya.title()+": ")
# yosh=int(input("Ваш возраст: "))
# print("\n\nПодвидём итог: ")
# yosh1=2021-yosh
# print("Значит Вы "+str(yosh1)+" года")
# print("Приветствую Вас "+ish+" "+imya.title()+" "+familiya.title()+" Ваш возраст "+str(yosh))
# print("Какой же Вы старый уже,пора на пенсию (o_o)")
# print("\n")
# print(imya.title())
# print(familiya.title())
# print(str(yosh1)+" года")
# print(str(yosh)+" леть")
# print("Какой же Вы старый уже,пора на пенсию (o_o)")


# ####  /////// LIST ////// LIST /////

# sport=['boks','futbol','karate','dyuzdo']
# natijalar=[100,90,50,70,85]
# aralash=['ellik',20,90,'uch',8,'yetti']
# print(sport[2])       #karate
# print(sport[-1])      #dyuzdo
# print(natijalar[1])   #90
# print(natijalar[-2])  #70
# print(aralash[0])     #ellik
# print(aralash[1])     #20

# sport=['boks','futbol','karate','dyuzdo']
# natijalar=[100,90,50,70,85]
# aralash=['ellik',20,90,'uch',8,'yetti']
# sport.append('kurash')   # .append element qo'shish funksiyasi
# print(sport)             #['boks', 'futbol', 'karate', 'dyuzdo', 'kurash']
# print(sport[-1])         #kurash
# sport.insert(2, "regbi") # .insert(index, object) indeks bo'yicha qo'shish
# print(sport)             #['boks', 'futbol', 'regbi', 'karate', 'dyuzdo', 'kurash']

# mashinalar=[]
# mashinalar.append('Nexia')
# mashinalar.append('Lasette')
# mashinalar.append('Malibu')     # indexsi 2
# mashinalar.append('Tracker')
# print(mashinalar)
# del mashinalar[0]               # list elementini index bo'yicha o'chirish
# mashinalar.insert(0, 'Nexia 3')
# mashinalar.remove('Nexia 3')    # Qiymat bo'yicha o'chirish
# print(mashinalar)

# bozorlik=["un","yog'","go'sht","karam","guruch"]
# print(bozorlik)           #['un', "yog'", "go'sht", 'karam'], 'guruch']
# bozorlik.pop(2)           #berilgan indexdagi elementni ajratib oladi
# print(bozorlik)           #['un', "yog'", 'karam', 'guruch']
# bozorlik.pop()            # Oxirgi elementni o'chiradi index berilmasa
# print(bozorlik)           #['un', "yog'", 'karam']

# bozorlik=["un","yog'","go'sht","karam","guruch"]
# mahsulot=bozorlik.pop(2)
# print("Men "+mahsulot+" sotib oldim")
# print("Olinmagan mahsulotlar",bozorlik)
# ## natija    Men go'sht sotib oldim
# ##           Olinmagan mahsulotlar ['un', "yog'", 'karam', 'guruch']
 
# cars=['BMW','Audi','Jep','Mazda','Lada']
# print(cars)       #['BMW', 'Audi', 'Jep', 'Mazda', 'Lada']
# cars.sort()     # Alfavit bo'yicha tartiblaydi
# print(cars)     #['Audi', 'BMW', 'Jep', 'Lada', 'Mazda']
# cars.sort(reverse=True) #Teskari tartibda tartiblash
# print(cars)     #['Mazda', 'Lada', 'Jep', 'BMW', 'Audi']
# print(sorted(cars)) #['Audi', 'BMW', 'Jep', 'Lada', 'Mazda']
# cars.reverse()  #elementlarni teskari joylashtiradi
# print(cars)     #['Lada', 'Mazda', 'Jep', 'Audi', 'BMW']
# print(len(cars))# 5 #LEN ro'yxat elementlari sonini chiqaradi

# ###/////  RANGE funksiyasi ////// #a dan b gacha bo'lgan sonlarni shakllantiradi

# sonlar=list(range(0, 15)) #0 dan 15 gacha bo'lgan sonlarni ro'yxatga o'tkazadi
# print(sonlar)             #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# toq_sonlar=list(range(1, 25,2))
# print(toq_sonlar)         #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
# onlik_sonlar=list(range(0, 111 ,10))
# print(onlik_sonlar)       #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

# ###/////  MAX va MIN funksiyalar //////
# qiymatlar=[1,67,98,35,75,225,3,0,-5,-8,10]
# # max_qiymat=max(qiymatlar)
# # min_qiymat=min(qiymatlar)
# # print(max_qiymat)         # 225
# # print(min_qiymat)         # -8
# # yigindisi=sum(qiymatlar)
# # print(yigindisi)          # 501
# # print("Eng arzon narx ",min_qiymat,"\nEng qimmat narx ",max_qiymat,"\nUmumiy summa ",yigindisi)
# # #### Eng arzon narx  -8 // Eng qimmat narx  225 // Umumiy summa  501
# # beshta_element=qiymatlar[0:5]
# # print(beshta_element)     # [1, 67, 98, 35, 75]
# # print(qiymatlar[6:11])    #[3, 0, -5, -8, 10]
# # print(qiymatlar[-6:-1])   #[225, 3, 0, -5, -8]
# # my_qiymatlar=qiymatlar[:]   # Kesib olish
# # print(my_qiymatlar)         #[1, 67, 98, 35, 75, 225, 3, 0, -5, -8, 10]
# # my_qiymatlar.remove(-5)
# # my_qiymatlar.remove(-8)
# # print(my_qiymatlar)         #[1, 67, 98, 35, 75, 225, 3, 0, 10]
# # print(qiymatlar)            #[1, 67, 98, 35, 75, 225, 3, 0, -5, -8, 10]


#### /////  TUPLE funksiyalar //////
# cars=('Tiko','Matiz','Damas','Cobalt','Malibu')  #o'zgarmaydigan ro'yxat
# print(cars[3])       # Cobalt chiqaradi 
# # cars.remove='Matiz'  #Xatolik Beradi
# print(cars)
# print(type(cars))    # <class 'tuple'>  #TUPLE -- o'zgarmas
# ### /// O'zgartiramiz
# cars=list(cars)      # listga o'tkazamiz
# cars.remove('Matiz') # Matizni o'chiramiz
# print(cars)          #['Tiko', 'Damas', 'Cobalt', 'Malibu']


# #### FOR  ////  FOR  //// FOR //// ##
# #### FOR  ////  FOR  //// FOR //// ##
# #### FOR  ////  FOR  //// FOR //// ##

# mehmon=['Ali','Vali','Anvar','Olim','Hasan','Farhod']
# for meh in mehmon:
#     print("Salom",meh) #Salom Ali Salom Vali Salom Anvar Salom Olim Salom Hasan Salom Farhod
    
# mehmon=['Ali','Vali','Anvar','Olim','Hasan','Farhod']
# for meh in mehmon:
#     print("Salom",meh) 
#     print("Hayr",meh)

###Salom Ali Hayr Ali Salom Vali Hayr Vali Salom Anvar Hayr Anvar
###Salom Olim Hayr Olim Salom Hasan Hayr Hasan Salom Farhod Hayr Farhod

# sonlar=list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar=list(range(11))
# sonlar_kvadrati=[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)            ## [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sonlar_kvadrati)   ## [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
# dostlar=[]
# print("5 taga yaqin do'stingizni kiriting! ")
# for n in range(5):
#     dostlar.append(input(f" {n+1}- do'stingizni ismini kiriting: "))
# print(dostlar)

# avtolar=['Tiko','Matiz','Damas','Cobalt','Malibu'] 
# for avto in avtolar:
#     if avto=='Damas':
#         print(avto.upper())
#     else:
#         print(avto.title())
  

# avtolar=['tiko','matiz','damas','cobalt','malibu'] 
# for avto in avtolar:
#     print(avto.title())

# login=input("Loginni kiriting")
# if len(login)<8:
#     print("Login 8 ta simvoldan kam bo'lmasligi kerak")
# else:
#     print(login," login qabul qilindi")

# menu=['osh','tandir','jiz','manti','shurva']
# ovqat=input("Nima ovqat tanladingiz: ")
# if ovqat.lower() in menu:
#     print("buyurtma qabul qilindi")
# else:
#     print("Menuda bunaqa ovqat yo'q")

# menu=['osh','tandir','jiz','manti','shurva']
# buyurtmalar=["osh","norin","somsa","jiz","tandir","kabob"]
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz {taom} menuda yo'q")
# else:
#     print("Buyurtma yo'q")



# print("<<<.:.registratsiyadan o'tish.:.>>>")
# login=input("Loginni kiriting: ")
# parol=input(int("Parolni kiriting: "))
# if len(login)>=8 && len(parol)>=6:
#     print("<<<.:.Shaxsiy ma'lumotlaringizni kiriting.:.>>>")
# else:
#     print("Login yoki parol")


























































