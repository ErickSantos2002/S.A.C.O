*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.google.com

*** Test Cases ***
Verificar Tela de Login
    Open Browser    ${URL}    Chrome
    Title Should Be    Google
    Close Browser
