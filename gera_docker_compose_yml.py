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
      - NUM_SERVERS={1}\n\
'
# '    volumes:\n\
#       - .:/usr/src/app\n\
# '


def gera_compose_file(num_servers):
    conteudo = "version: '3'\n"
    conteudo += "services:\n"
    for i in range(num_servers):
        conteudo += template.format(i + 1, num_servers)
    with open("docker-compose.yml", "w", newline='\n') as compose:
        compose.write(conteudo)


if __name__ == '__main__':
    if len(argv) > 1:
        n = argv[1]
    else:
        n = 4
    gera_compose_file(n)
