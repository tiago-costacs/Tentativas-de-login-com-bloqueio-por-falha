# Em sistemas de autenticação segura, é comum bloquear contas devido a múltiplas tentativas de login inválidas consecutivas. Esse codigo evita ataques de força bruta e protege a conta do usuário.

Verificar tentativas de login e identificar se a conta deve ser bloqueada com base em tentativas falhas seguidas.

Uma conta deve ser bloqueada se houver 3 ou mais tentativas consecutivas de falha.
