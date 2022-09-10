# Assistente_Pessoal
Um assistente pessoal em python!<br>
 :construction: Projeto em construção :construction:
 
Olá, fiz este projeto para aprender e mexer com diferentes bibliotecas do python e com a funcionalidade de ler e modificar arquivos .txt . 
 
 
 
 ## :hammer: Funcionalidades do projeto
- `Pesquisar pessoas`: Pesquisa por pessoas utilizando a bilbioteca da wikipedia.  
- `Pesquisar definições`: Pesquisa a definição de objetos e diferentes coisas utilizando a biblioteca da wikipedia.
- `Tocar músicas`:Pesquisa e toca musicas do youtube.
- `Interações`: Interage com o usuário a partir de respostas pre-programadas.
 
 ## Caso você queira testar este projeto, precisa estar ciente de certas coisas:
 - Este código foi feito utilizando algumas bibliotecas, então problemas e bugs podem acontecer.
 - Dependendo da maneira que você utilizar o código os arquivos .txt podem aumentar de tamanho ,mas não se preocupe, o programa é feito para armazenar o resultado de pesquisas não feitas anteriormente.
 - Na hora de testar, não fique frustrado caso o seu microfone não funcione, a biblioteca utilizada possui problema com o reconhecimento de voz caso o seu microfone possua algum ruído ou o mesmo seja de baixa qualidade.A parte `Utilização` pode ajudar você.
 - Como o projeto está em contrução, o projeto possui pouco conteúdo e funcionalidades ,mas estarei modificando. Caso você possua dicas para implementações, ou dúvidas, pode entrar em contato comigo através dos meios de comunicação abaixo que também se encontram no meu perfil.<br>
 📧durt.deve@gmail.com<br>
 🐦@dolar_boot (Sim, isso era pra ser o pássaro do twitter)
 
  
 ## ✔️ Utilização 
 - Para utilizar o assistente, você deve baixar os arquivos os arquivos, os únicos _NÃO_ nescessários são:<BR>
 ° txt_UTF-8.md<BR>
 ° README.md<BR>
 - Para começar a dar comandos para o assistente você deve chama-lo:<br>
 ° Rode o código e então chame seu assistente pelo nome, neste caso está 'Cleiton' ,mas você pode modificar na linha 126.<br>
 ° Por algum acaso a biblioteca escolhida possui dificuldade em ouvir o nome Cleiton, então recomendo que você mude
 
 
 
 ## 🛠️Alteração
 - Adicionar músicas a uma playlist:<br>
 ° Para você adicionar músicas, primeiro você deve entender como funciona:<br>
 Quando a função de tocar alguma música é chamada, o algoritmo testa se você falou o gênero musical desejado, neste acaso só adicionei o gênero phonk. Então caso você peça para ele "tocar phonk", ele irá abrir o arquivo phonk_storage_music.txt e sortear uma das músicas.<br><p>
 ° Para você adicionar mais músicas você deve modificar o arquivo .txt:<br>
  Para adicionar mais músicas a playlist já existente, entre no arquivo de musicas e então salve o nome da música, seguido pela chave "/&*" e então o link da música.Sempre em linhas diferentes, salve a nova música logo a baixa da outra, assim como no arquivo phonk_storage_music.txt .<br>
  EX:warning/&*https://www.youtube.com/watch?v=Z7BByo2V-HA<br><p>
 ° Não esqueça de modificar o script:<br>
  Na linha 92, você verá o seguinte código:<br>
 a = random.randint(1,3)<br>
  É ele que sorteia a música que será tocada, então você precisa modificar a posição que se encontra o número "3" para a quantidade total de músicas que você tem na sua playlist.
 
 - Adicionar nova playlist:
 ° Para você adiconar uma nova playlist você deve entender como funciona:<br>
 Quando a função de tocar alguma música é chamada, o algoritmo testa se você falou o gênero musical desejado, neste acaso só adicionei o gênero phonk.Então caso você peça para ele "tocar phonk", ele irá abrir o arquivo phonk_storage_music.txt e sortear uma das músicas.<br><p>
 ° Para adicionar uma nova playlist você deve criar um novo arquivo:<br>
 Para criar uma nova playlist você deve criar um arquivo .txt, recomendo que siga um padrão, por exemplo:nomeplaylist_storage_music.txt, assim você saberá o que é este arquivo sem precisar entrar nele.<br>
 Nele você deve salvar as músicas assim como dito anteiormente em 'Adicionar música a uma playlist'.<br>
 Para que o python entenda o que está escrito neste arquivo, ele deve estar salvo como UTF-8, recomendo que veja o passo a passo em: <a href='https://github.com/dudrt/Assistente_Pessoal/blob/main/txt_UTF-8.md'>txt_UTF-8.md</a>
 
 
 ## 📁
 Acesso ao projeto

**Indique como é possível baixar ou acessar o código fonte do projeto, seja projeto inicial ou final**
