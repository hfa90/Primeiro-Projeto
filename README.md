Criptografia de Imagens

Introdução
O Criptografia de Imagens é um conjunto de programas Python que permite encriptar e desencriptar imagens usando a biblioteca cryptography e uma interface gráfica fornecida pelo Tkinter. Com este conjunto de ferramentas, você pode proteger a privacidade das suas imagens pessoais ou sensíveis por meio de encriptação.

Funcionalidades:
Encriptador de Imagens: Este programa permite encriptar uma imagem selecionada, gerando uma versão encriptada da imagem e salvando-a no disco. 
Além disso, a chave de encriptação é salva em um arquivo separado para desencriptação posterior.

Desencriptador de Imagens: 
Com este programa, é possível desencriptar uma imagem previamente encriptada. Ele solicitará o caminho da imagem encriptada e utilizará a chave de encriptação 
correspondente para restaurar a imagem original.

Pré-requisitos:

Python 3.x instalado
Biblioteca cryptography instalada (você pode instalar usando pip install cryptography)
Biblioteca Pillow instalada (você pode instalar usando pip install pillow)


Como Usar:

Copie este repositório em sua máquina local.
Certifique-se de ter os pré-requisitos instalados.
Execute o programa encrypt_image_gui.py para encriptar uma imagem.
Execute o programa decrypt_image_gui.py para desencriptar uma imagem.


Exemplo de Uso:

Encriptar uma Imagem
Execute o programa encrypt_image_gui.py.
Clique no botão "Procurar" para selecionar a imagem que deseja encriptar.
Clique no botão "Encriptar".

Uma versão encriptada da imagem será gerada e salva no diretório.
Desencriptar uma Imagem
Execute o programa decrypt_image_gui.py.
Clique no botão "Procurar" para selecionar a imagem encriptada que deseja desencriptar.
Clique no botão "Desencriptar". A imagem desencriptada será gerada e salva no diretório.


Notas
Certifique-se de armazenar a chave de encriptação key.key em um local seguro, pois será necessária para desencriptar as imagens.
Este software foi desenvolvido apenas para fins educacionais e de demonstração. Não é garantido para proteger imagens de forma absoluta.
