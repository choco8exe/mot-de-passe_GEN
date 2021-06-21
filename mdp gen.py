from random import*

ltr=['&','a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','z','0','1','2','3','4','5','6','7','8','9','/',',','*','!','é','^','?','+','-','(','','@','ç','_','-','=',]

print("""
• ▌ ▄ ·.       ▄▄▄▄▄    ·▄▄▄▄  ▄▄▄ .     ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▄ .     ▄▄ • ▄▄▄ . ▐ ▄ 
·██ ▐███▪▪     •██      ██▪ ██ ▀▄.▀·    ▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ▀▄.▀·    ▐█ ▀ ▪▀▄.▀·•█▌▐█
▐█ ▌▐▌▐█· ▄█▀▄  ▐█.▪    ▐█· ▐█▌▐▀▀▪▄     ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄▐▀▀▪▄    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
██ ██▌▐█▌▐█▌.▐▌ ▐█▌·    ██. ██ ▐█▄▄▌    ▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌    ▐█▄▪▐█▐█▄▄▌██▐█▌
▀▀  █▪▀▀▀ ▀█▄▀▪ ▀▀▀     ▀▀▀▀▀•  ▀▀▀     .▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ 

                                                                                       by choco""")



longueur=int(input('Entrez la longueur de votre mot de passe: '))

nb_mdp=int(input('Combient de mot de passe voulez-vous ? :'))

def mdp(longueur):
    mdp=str()
    shuffle(ltr)
    for x in range(longueur):
        mdp+=ltr[x]
    
    print(mdp)

for x in range(nb_mdp):
    mdp(longueur)

input()




