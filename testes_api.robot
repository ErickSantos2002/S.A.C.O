*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    BuiltIn

*** Variables ***
${BASE_URL}    http://localhost:8000
${NOME}        Robot Teste
${SENHA}       123456

*** Keywords ***
Gerar Email Único
    ${uuid}=    Evaluate    __import__('uuid').uuid4().hex[:6]
    ${email}=   Set Variable    robot_${uuid}@example.com
    RETURN    ${email}

Cadastrar Novo Usuário
    [Arguments]    ${email}    ${nome}    ${senha}
    ${dados}=    Create Dictionary    nome=${nome}    email=${email}    senha=${senha}
    ${resposta}=    POST On Session    api    /usuarios/cadastro    json=${dados}
    Log    STATUS: ${resposta.status_code}
    Log    BODY: ${resposta.content}
    Should Be Equal As Strings    ${resposta.status_code}    200
    RETURN    ${resposta}

Logar Usuário
    [Arguments]    ${email}    ${senha}
    ${dados}=    Create Dictionary    email=${email}    senha=${senha}
    ${resposta}=    POST On Session    api    /usuarios/login    json=${dados}
    Log    STATUS: ${resposta.status_code}
    Log    BODY: ${resposta.content}
    Should Be Equal As Strings    ${resposta.status_code}    200
    RETURN    ${resposta}

Extrair Token de Resposta
    [Arguments]    ${resposta}
    ${json}=    Evaluate    __import__('json').loads("""${resposta.content.decode("utf-8")}""")
    Dictionary Should Contain Key    ${json}    access_token
    Dictionary Should Contain Key    ${json}    token_type
    RETURN    ${json}

*** Test Cases ***
Cadastro e Login de Usuário com Sucesso
    ${EMAIL}=    Gerar Email Único
    Create Session    api    ${BASE_URL}

    Cadastrar Novo Usuário    ${EMAIL}    ${NOME}    ${SENHA}
    ${res_login}=    Logar Usuário    ${EMAIL}    ${SENHA}
    ${token_json}=   Extrair Token de Resposta    ${res_login}
