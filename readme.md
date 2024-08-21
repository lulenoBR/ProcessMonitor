# Monitor de Processos (Versão 6)

Este programa monitora um processo específico e tenta reiniciá-lo caso ele não esteja em execução. Ele também possui uma interface gráfica do usuário (GUI) que permite ao usuário alterar as configurações do processo a ser monitorado.

## Alterações na Versão 6

Na versão 6 do programa, as seguintes alterações foram feitas em relação à versão 5:

- Foi adicionada uma nova função `open_settings()` que abre uma janela de configurações onde o usuário pode alterar as configurações do processo a ser monitorado.
- Foi adicionada uma nova função `save_config(process_name, executable_path, sleep_time_seconds)` que salva as configurações alteradas pelo usuário no arquivo de configuração.
- Foi adicionada uma nova função `close_program(icon, item)` que encerra o programa quando chamada.
- Foi adicionada uma nova opção "Close Program" ao ícone da bandeja do sistema. Quando clicada, essa opção encerra o programa.
- A função `main()` agora é executada em uma nova thread, permitindo que o ícone da bandeja do sistema seja exibido simultaneamente.
- O programa agora cria seu próprio arquivo `config.cfg` se ele não existir, com algumas informações padrão.

## Funções

O programa contém as seguintes funções:

- `setup_logger()`: Esta função configura o logger que é usado para registrar mensagens de status e erros.
- `is_process_running(process_name)`: Esta função verifica se um processo específico está em execução. Ela retorna `True` se o processo estiver em execução e `False` caso contrário.
- `restart_process(executable_path, process_name)`: Esta função tenta reiniciar um processo específico a partir do caminho do executável fornecido.
- `read_config(config_file)`: Esta função lê um arquivo de configuração e retorna o nome do processo, o caminho do executável e o intervalo de tempo que o programa aguarda antes de verificar novamente o status do processo.
- `open_settings()`: Esta nova função abre uma janela de configurações onde o usuário pode alterar as configurações do processo a ser monitorado.
- `save_config(process_name, executable_path, sleep_time_seconds)`: Esta nova função salva as configurações alteradas pelo usuário no arquivo de configuração.
- `close_program(icon, item)`: Esta nova função encerra o programa quando chamada.
- `main()`: Esta é a função principal que monitora continuamente o processo e tenta reiniciá-lo se ele não estiver em execução.

## Uso

Ao executar o programa, ele irá criar 2 arquivos, 1 arquivo .cfg e outro arquivo .log.

Deve ser feita alteração no arquivo de configuração ou através do ícone na bandeja de aplicativos, definindo o programa a ser monitorado.