from sys import argv

template = '\
  server{0}:\n\
    build: .\n\
    image: server\n\
    container_name: server{0}\n\
    ports:\n\
      - "500{0}:5000"\n\
    environment:\n\
      - ID={0}\n\
    volumes:\n\
      - .:/server\n\
'


def gera_compose_file(num_server):
    conteudo = "version: '3'\n"
    conteudo += "services:\n"
    for i in range(num_server):
        conteudo += template.format(i + 1)
    with open("docker-compose.yml", "w", newline='\n') as compose:
        compose.write(conteudo)


if __name__ == '__main__':
    if len(argv) > 1:
        n = argv[1]
    else:
        n = 4
    gera_compose_file(n)
