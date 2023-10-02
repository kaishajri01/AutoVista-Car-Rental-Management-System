from datetime import date


             #############################################################
             #                CONTROLE DES VOITURES                       #
             #############################################################

def c_matricule(x):
    l=x.split()
    if len(l)==3:
        if l[0].isdigit() and int(l[0])>0 and int(l[0])<10000 and l[1]=="TUN" and int(l[2])>20 and int(l[2])<230 and x.count(" ")==2:
             return True
    return False

               #############################################################

def c_marque(x):
    if x in ["Alfa Romeo","Alpine","Aston Martin","Audi","Bentley","Bestune","BMW","Caterham","Chevrolet","Citroën","Cupra","Dacia","Ferrari","Fiat","Ford","Honda",
"Hummer","Hyundai","Isuzu","Jaguar","Jeep","Lamborghini","Land Rover","Maserati","Mercedes-Benz","Mitsubishi","Nissan","Opel","Peugeot","Porsche",
"Renault","Rolls-Royce","Skoda","Suzuki","Tesla","Toyota","Volkswagen","Volvo"]:
        return True
    return False

                #############################################################


def c_couleur(x):
    if x in  ["Blanc","Noir","Pourpre","Rouge","Orange","Jaune","Vert","Bleu","Violet","Ivoire","Crème","Beige","Rose","Kaki","Brun","Marron"]:
        return True
    return False

                #############################################################

def c_date(x):
    def verif(datee):
        l=datee.split("/")    
        if(len(datee)!=10 or datee[2]!='/' or datee[5]!='/' or l[0].isdigit()==False or l[2].isdigit()==False):
                return False;      
        return True

    if verif(x):
        l=x.split("/")
        jj=l[0]
        mm=l[1]
        aa=l[2]
        jmax=31
        if mm in ["1","3","5","7","8","10","12"]:
            jmax=31
        elif mm in ["4","6","9","11"]:
            jmax=30
        elif mm=="2":
            if int(aa)%4==0 and int(aa)%100!=0 or int(aa)%400==0:
                jmax=29
            else:
                jmax=28
        if int(aa)>1900 and int(aa)<2023 and int(mm)>=1 and int(mm)<=12 and int(jj)>=1 and int(jj)<=jmax:
            return True
        else:
            return False
    else:
        return False
                    #############################################################


def c_prix(x):
    if int(x)<5000 and int(x)>80 :
        return True
    return False    

                    #############################################################

def mat_existe(x,l):
    for i in l:
        if i.matricule ==x:
            return True
    return False
                    
                    #############################################################
def age_voit(x):
    l=x.split("/")
    d1=date(int(l[2]),int(l[1]),int(l[0]))
    d2=date.today()
    s=d2-d1
    return s.days
                     #############################################################

def indice_matricule(mat,l):
    if mat_existe(mat,l)==False:
        return -1
    else:
        for i in range(len(l)):
            if l[i].matricule==mat:
                return i

                 #############################################################

def entre_deux_date(d,d1,d2):
    l=d.split("/")
    l1=d1.split("/")
    l2=d2.split("/")
    dd=date(int(l[2]),int(l[1]),int(l[0]))
    dd1=date(int(l1[2]),int(l1[1]),int(l1[0]))
    dd2=date(int(l2[2]),int(l2[1]),int(l2[0]))
    s1=dd-dd1
    s2=dd-dd2
    if int(s1.days)>=0 and int(s2.days)<=0:
        return True
    return False

def compare_date(d1,d2):
    l1=d1.split("/")
    l2=d2.split("/")
    dd1=date(int(l1[2]),int(l1[1]),int(l1[0]))
    dd2=date(int(l2[2]),int(l2[1]),int(l2[0]))
    s1=dd2-dd1
    if int(s1.days)>=0:
        return True
    return False




             #############################################################
             #                CONTROLE DES CLIENTS                       #
             #############################################################


def c_cin(x):
    if x.isdigit() and len(x)==8 and int(x)>700000:
        return True
    return False

            #############################################################

def c_nom(x):
    if x.isalpha() and len(x)>2:
        return True
    return False

            #############################################################
def c_mail(x):
    if len(x)>10  and (("@gmail.com" in x) or ("@outlook.fr" in x) or ("@yahoo.fr" in x)) :
        return True
    return False

             #############################################################

def c_tlf(x):
    if len(x)==8 and x.isdigit() and int(x)>20000:
        return True
    return False    

            #############################################################

def cin_existe(x,l):
    for i in l:
        if i.cin ==x:
            return True
    return False

            #############################################################

def indice_cin(cin,l):
    if cin_existe(cin,l)==False:
        return -1
    else:
        for i in range(len(l)):
            if l[i].cin==cin:
                return i


                    #############################################################
                    #                CONTROLE DES CLIENTS                       #
                    #############################################################

def c_duree(x):
    if x.isdigit() and int(x)>0:
        return True
    return False
                    #############################################################

def contrat_existe(x,l):
    for i in l:
        if i.numero ==x:
            return True
    return False

                    #############################################################
                    
def indice_contrat(c,l):
    if contrat_existe(c,l)==False:
        return -1
    else:
        for i in range(len(l)):
            if l[i].numero==c:
                return i


                    #############################################################

def c_numcont(c):
    if c.isdigit()==False or int (c)<10000:
        return False 
    return True



                    #############################################################

def c_louee(x,listevoit):
    if listevoit.parc[indice_matricule(x,listevoit.parc)].etat=="Louée":
        return True
    return False