#Variant 2
#Üliõpilane Kaarel Põldemaa

#Ülesanne 1

def elements_sum(a): #defineerin elements_sum 
    faktoriaal = 0 #määran muutujale algväärtuse
    if a > 0: #kontrollib, kas kasutaja sisestatud number on väiksem kui 0 ning tõese tehte korral jätkatakse if funktsiooniga
        for i in range(1,a + 1): #algab tsükkel, mida korratakse senikaua kuni i võrdub kasutaja poolt sisestatud numbriga
            faktoriaal = faktoriaal + i #siin liidame esimesed kaks numbrit omavahel ning seejärel iga järgnev number eelmise summale
        return(faktoriaal) #tagastan tulemuse
    elif a < 0: #kontrollin, kas arv on väiksem kui null
        return("Palun sisesta nullist suurem number") #tagastan tulemuse, kui kasutaja ei sisesta nullist suuremat numbrit

print(elements_sum(5))

#Ülesanne 2

def time_convert(a): #defineerin time_convert
    tunnid=int(a[0:2]) #defineerin tunnid
    minutit=int(a[3:5]) #defineerin minutid
    arvutus=(tunnid*60+minutit) #teen arvutuse, kus teisendan tunnid minutiteks ning liidan juurde minutid
    return(arvutus) #tagastan tulemuse

print(time_convert("01:02"))

#Ülesanne 3

##Kahjuks ei oska kolmandat ülesannet


def sort_values(x): #defineerin sort_values
    numbrite_list=[] #teen numbrite jaoks uue listi
    alphabet_list=[] #teen tähtede jaoks uue listi
    q=1
    w=0
    if (x[w:q]).isalpha() == True: #siin ma tahan tõsta kõik numbrid numbrite listi
        c=int(x[i])
        q=q+1
        w=w+1
        numbrite_list.append(c)
    elif :
        c=int(x[i])
        q=q+1
        w=w+1
        alphabet_list.append(c)
    x.sort() #sorteerin väärtused
    return(x) #tagastan väärtused


print(sort_values(2,a,54,v,y,8))

##x=input("sisesta parool: ")
##if x.isalpha()== True:
##    print("sisestatud on ainult tähed")
##elif x.isalpha()==False:
##    print("Sisestatud ei ole ainult tähed")
##elif x.isdigit()==True:
##    print("Sisestatud on ainult numbrid")