from os import kill
import requests
import subprocess

x = int(input('deseja remover o fundo por um arquivo(1) ou link(2)?'))

if x == 1:
    arquivo = input('digite o nome do arquivo:')
    path = subprocess.run(['pwd'], capture_output=True, text=True)
    resposta = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files= {'image_file': open(path.stdout.replace('\n', '') + '/' + arquivo, 'rb')},
        data= {'size': 'auto'},
        headers= {'X-Api-Key': 'tx12P3VA768nyXJBDWAAU8Ui'}
    )

elif x == 2:
    link = input('insira o link da imagen')
    resposta = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data = {'image_url': link,
        'size': 'auto'},
        headers= {'X-Api-Key': 'tx12P3VA768nyXJBDWAAU8Ui'}
    )

else:
    print('erro, escolha uma alternativa valida!')
    exit()

if resposta.status_code == requests.codes.ok:
    nome = input('qual nome quer dar para a imagem? lembre-se de colocar a extensão (example.png)')
    with open(nome, 'wb') as out:
        out.write(resposta.content)
    
    if x == 1:
        deletar = int(input('deseja apagar a imagem original? sim(1) não(2)'))
        if deletar == 1:
            subprocess.run(['rm', path.stdout.replace('\n', '') + '/' + arquivo])
else:print('erro', resposta.status_code, resposta.text)

