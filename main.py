import streamlit as st
import streamlit_authenticator as stauth
# Criando Função de autenticação

<<<<<<< HEAD
# Tempo de expiração de login em dias
COOKIE_EXPIRY_DAYS = 30

# Criando função main de autenticação
def main():
    # Classe 'auth.authenticator' da biblioteca 'streamlit' para fazer a autenticação
    authenticator = stauth.Authenticate(
        # Montar um place ordem para mostrar o formato que os dados serão salvas no banco de dados
        {'username': {'teste': {'name': 'testando', 'password': 'blabla'}}},
        # Responsável por definir o placeholder do login
        'random_cookie_name',
        'random_signature_key',

        COOKIE_EXPIRY_DAYS,
    )

    # Se o botão 'clicou_registrar' ainda não estiver dentro da session_state
    if 'clicou_registrar' not in st.session_state:
        # deixar como padrão false
        st.session_state['clicou_registrar'] = False

    # Realizando a validação do session_state do 'clicou_registrar'
    if st.session_state['clicou_registrar'] == False:
        # Se o usuário não clicou no botão registrar, deve ser mostrado o formulário de login
        login_form(authenticator=authenticator)




# Criando funcao login_form que será a função de login
# será passado como varivel authenticator, pois está função será chamada para autenticar o usuário
def login_form(authenticator):
    name, authenticator_status, username = authenticator.login('Login', 'main')
    # Mostrar o botão de lought out caso for autenticado
    if authenticator_status:
        # Dentro deste 'if' seria o local onde a aplicação que quero proteger ficaria
        authenticator.logout('Logout', main)
        # exemplo de titulo
        st.title(f'Area do Dashboard')
        # mensagem para o usuário saber que está logado
        st.write(f'*{name} está logado(a)!')
    # Se caso a autenticação falhar
    elif authenticator_status == False:
        st.error('Usuário/Senha incorretos')
    # Se não for preenchido nada no formulário
    elif authenticator_status == None:
        st.warning('Por favor informe um usuário e senha')
        # Sempre que um novo usuário entrar na aplicação ele deve ter a opção de criar um nova conta
        cliclou_registrar = st.button('registrar')
        # Validando o clique do botão registrar
        if cliclou_registrar:
            # usando st.session_state para armazenar  o estado da sessão
            st.session_state['clicou_registrar'] = True
            # Se clicado deve ser feito um 'reload'
            st.rerun()

# Função para confirmar o registro do usuário
def confirm_msg():
    # Criando função 'hashed_password' para criptografar a senha
    hashed_password = stauth.Hasher([st.session_state.pwswd]).generate()
    # Verificando se confirmação de senha está correto
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning('Senhas não conferem')
    # Vericiar se o nome de usuário já existe
    # ainda não temos a função consulta_nome() implementada
    elif 'consulta_nome()':
        st.warning('Nome de usuário já existe')
    else:
        # Função para adicionado registro 'add_registro()' ainda não implementada
        'add_registro()'
        st.success('Registro efetuado')


# Criando função de registro
def usuario_form():
    # usando 'with' para criar um formulário
    with st.form(key="formulario", clear_on_submit=True):
        # criando viáveis para armazenar dados do usuario usando 'st.text_input'
        nome = st.text_input('Nome', key = 'nome')
        usuario = st.text_input('Usuario', key='user')
        # usar type='password' para esconder a senha
        password = st.text_input('Senha', key='pswrd', type='password')
        confirm_password = st.text_input('Confirmar Senha', key='confirm_pswrd', type='confirm_pswrd')
        # botao de sumit
        submit = st.form_submit_button(
            # usar on_click para chamar a função de salvar
            "Salvar", on_click=confirm_msg,
        )
        # Botão para voltar a tela de registro
        clicou_em_fazer_login = st.button('Fazer login')
        if clicou_em_fazer_login:
            st.session_state['clicou_registrar'] = False
            st.rerun()

# Base do Programa
if __name__ == '__main__':
    main()
=======
print('teste')
print('teste')
print('teste')
print('teste')
print('teste')
print('teste')
print('teste')


# escreva algo para mostrar no streamlit
st.title('Teste de autenticação com Streamlit')
>>>>>>> 7761a26f855bf1878a3a331df36979f5826ad4a7
