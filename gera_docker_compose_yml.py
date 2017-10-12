
def gera_compose_file(num_server=4):
    conteudo = "version: '3'\n"
    conteudo += "services:\n"
    for i in range(num_server):
        print(i+1)
        conteudo += '\
  server{0}:\n\
    build: .\n\
    image: server\n\
    container_name: server{0}\n\
    ports:\n\
      - "500{0}:5000"\n\
    environment:\n\
      - ID={0}\n\
    volumes:\n\
      - .:/server\n'.format(i+1)
        print(conteudo)
    with open("docker-compose2.yml", "w") as compose:
        compose.write(conteudo)


if __name__ == '__main__':
    gera_compose_file()
