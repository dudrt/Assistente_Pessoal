import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import random

audio = sr.Recognizer()
cleiton = pyttsx3.init()
continuar=True

voices = cleiton.getProperty('voices')
cleiton.setProperty('voice', voices[0].id)


#---------------------Fica ouvindo esperando ser chamado----
def wait():
    try:
        with sr.Microphone() as source:
            print('.')
            #audio.energy_threshold = 1600 Caso seu microfone não capte sua voz, tente modificar esta linha de código e tire a de baixo
            audio.adjust_for_ambient_noise(source, duration=2)

            voz = audio.listen(source)
            frase = audio.recognize_google(voz, language='pt-BR')
            frase = frase.lower()
            return frase
    except:
        print('Não consigo entender!')
        return ''
#---------------------Pega a voz--------------------
def inicial():
    try:
        with sr.Microphone() as source:
            cleiton.say('Ouvindo')
            cleiton.runAndWait()
            print('Ouvindo..')
            audio.adjust_for_ambient_noise(source, duration=2)
            #audio.energy_threshold = 1600 Caso seu microfone não capte sua voz, tente modificar esta linha de código e tire a de cima
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            return comando
    except:
        print('Microfone não está ok')
    
#-------------------procura se tem no armazenamento----------------------------
def storage(procurar):
    tem = ''
    arquivo = open('storage.txt', 'r', encoding="utf8")
    for line in arquivo:
        primeira_palavra = line.split('/&*')
        if primeira_palavra[0] == procurar:
            arquivo.close()
            return primeira_palavra[1]
    if tem == '':
        return ''
#---------------------armazena pesquisas--------------------
def armazenar(procurar, resultado):
    arquivo = open('storage.txt','r',encoding="utf8")
    adicionar = arquivo.readlines()
    adicionar.append(f"\n{procurar}/&*{resultado}")
    arquivo = open('storage.txt' , 'w' ,encoding="utf8")
    arquivo.writelines(adicionar)
    arquivo.close()
#----------------trata oque foi dito em diferentes funções------------------
def funcoes():
    comando = inicial()
#--------------------------procurar pessoa/coisas-------------------
    if 'procure por ' in comando or 'procurar por' in comando:
        if 'procure por ' in comando:
            procurar = comando.replace('procure por ','')
        elif 'procurar por' in comando:
            procurar = comando.replace('procurar por ','')
        tem = storage(procurar)#----procura no armazenamento----
        if tem != '':
            cleiton.say(tem)
            cleiton.runAndWait()
        else:
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar,sentences = 2)
            print(resultado)
            cleiton.say(resultado)
            cleiton.runAndWait()
            armazenar(procurar,resultado)
#--------------------------fim procurar pessoa/coisas-------------------
#--------------------------procura musica-------------------------------
    elif 'toque ' in comando or 'toc' in comando:
        if 'funk' in comando:
            arquivo = open('phonk_storage_music.txt', 'r', encoding="utf8")
            cleiton.say('Tocando Phonk')
            cleiton.runAndWait()
            a = random.randint(1,3)
            musica=''
            b=0
            for line in arquivo:
                b+=1
                if a == b:
                    musica = line.split('/&*')
                    print(musica[1])
                    pywhatkit.playonyt(musica[1])
        else:
            musica = comando.replace('toque ','')
            cleiton.say(f'tocando {musica}')
            cleiton.runAndWait()
            pywhatkit.playonyt(musica)
    else:
        arquivo = open('interactions.txt', 'r', encoding="utf8")
        for line in arquivo:
            primeira_palavra = line.split('/&*')
            if primeira_palavra[0] == procurar:
                arquivo.close()
                return primeira_palavra[1]
        if tem == '':
            return ''


cleiton.say('Olá, eu sou o Cleiton, seu assistente!')
cleiton.runAndWait()
#----Deixa o bot rodando até você falar 'fechar'----
while continuar:
    frase=wait()
    print(frase)
    if 'fechar' in frase:
        continuar=False
    elif 'cleiton' in frase:
        funcoes()
#-------------------------Fim-----------------------

