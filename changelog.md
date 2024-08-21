# Changelog do Monitor de Processos

## Versão 1
- Lançamento inicial.
- Monitora um processo específico e tenta reiniciá-lo caso ele não esteja em execução.
- O nome do processo e o caminho do executável são definidos diretamente no código.

## Versão 2
- O nome do processo e o caminho do executável agora são lidos de um arquivo de configuração. Isso permite uma maior flexibilidade, pois você pode alterar o processo que deseja monitorar simplesmente modificando o arquivo de configuração, sem precisar alterar o código do programa.

## Versão 3
- Adicionado um sistema de log. Agora, todas as mensagens de status e erros são registradas em um arquivo de log que é rotacionado diariamente.
- A função `is_process_running(process_name)` agora registra uma mensagem de log quando o processo está em execução.

## Versão 4
- O intervalo de tempo que o programa aguarda antes de verificar novamente o status do processo agora é lido do arquivo de configuração. Isso permite que você ajuste facilmente o intervalo de tempo sem precisar alterar o código do programa.

## Versão 5
- O manipulador de log rotativo foi substituído por um manipulador de arquivo (`FileHandler`). Agora, todas as mensagens de log são salvas em um único arquivo (`process_monitor.log`), em vez de serem rotacionadas diariamente.
- A função `is_process_running(process_name)` não registra mais uma mensagem de log quando o processo está em execução. Isso reduz a quantidade de logs gerados quando o processo está funcionando normalmente.

## Versão 6
- Adicionada uma nova função `open_settings()` que abre uma janela de configurações onde o usuário pode alterar as configurações do processo a ser monitorado.
- Adicionada uma nova função `save_config(process_name, executable_path, sleep_time_seconds)` que salva as configurações alteradas pelo usuário no arquivo de configuração.
- Adicionada uma nova função `close_program(icon, item)` que encerra o programa quando chamada.
- Adicionada uma nova opção "Close Program" ao ícone da bandeja do sistema. Quando clicada, essa opção encerra o programa.
- A função `main()` agora é executada em uma nova thread, permitindo que o ícone da bandeja do sistema seja exibido simultaneamente.
- Adicionado um ícone para o programa.
- Adicionada uma interface gráfica do usuário (GUI) para o programa.
- O programa agora cria seu próprio arquivo `config.cfg` se ele não existir, com algumas informações padrão.
