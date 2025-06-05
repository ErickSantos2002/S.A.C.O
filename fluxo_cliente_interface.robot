*** Settings ***
Library    SeleniumLibrary
Suite Setup    Abrir Navegador E Login
Suite Teardown    Fechar Navegador

*** Variables ***
${URL_LOGIN}    http://127.0.0.1:5500/app/HTMLS%20e%20CSS/login.html
${EMAIL}        ericksantosdantas@gmail.com
${SENHA}        123456
${NOME_USUARIO}    Teste Selenium
${EMAIL_USUARIO}   teste-selenium@saco.com
${SENHA_USUARIO}   1234567
${DATA}        2025-07-15
${HORA}        14:00
${LOCAL}       Sala 203
${DESCRICAO}   Teste automatizado de agendamento

*** Test Cases ***
Fluxo Completo SACO - Agendamento e Usuário
    [Documentation]    Faz login, cria agendamento, cadastra usuário, volta e faz logout.
    Criar Agendamento
    Criar Novo Usuario
    Voltar Ao Dashboard E Fazer Logout

*** Keywords ***
Abrir Navegador E Login
    Open Browser    ${URL_LOGIN}    chrome
    Maximize Browser Window
    Wait Until Element Is Visible    id=email    5s
    Input Text    id=email    ${EMAIL}
    Input Text    id=senha    ${SENHA}
    Click Button    xpath=//button[contains(text(), 'Entrar')]
    Wait Until Location Contains    dashboard.html    5s

Criar Agendamento
    Click Link    xpath=//a[contains(@href, 'agendamentos.html')]
    Wait Until Page Contains Element    id=form-agendamento    5s
    Input Text    id=data    ${DATA}
    Input Text    id=hora    ${HORA}
    Input Text    id=local    ${LOCAL}
    Input Text    id=descricao    ${DESCRICAO}
    Click Button    xpath=//button[contains(text(), 'Salvar Agendamento')]
    # Pode aparecer um alert de sucesso. Aceita se aparecer.
    Handle Alert    action=ACCEPT
    Sleep    1s

Criar Novo Usuario
    Click Link    xpath=//a[contains(@href, 'usuarios.html')]
    Wait Until Page Contains Element    xpath=//form[contains(@class, 'usuario-form')]    5s
    Input Text    id=nome    ${NOME_USUARIO}
    Input Text    id=email    ${EMAIL_USUARIO}
    Input Text    id=senha    ${SENHA_USUARIO}
    Click Button    xpath=//button[contains(text(), 'Cadastrar Usuário')]
    Handle Alert    action=ACCEPT
    Sleep    1s

Voltar Ao Dashboard E Fazer Logout
    Click Link    xpath=//a[contains(@href, 'agendamentos.html')]
    Wait Until Page Contains Element    id=form-agendamento    5s
    Click Element    xpath=//a[contains(@class, 'logout')]
    Wait Until Location Contains    login.html    5s

Fechar Navegador
    Close Browser
