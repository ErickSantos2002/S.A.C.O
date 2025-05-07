"""
test_users.py
--------------
Testa cadastro e login de usuários com FastAPI e HTTPX.
"""

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_cadastro_login_usuario():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Cadastro
        response = await ac.post("/usuarios/cadastro", json={
            "nome": "João",
            "email": "joao@example.com",
            "senha": "123456"
        })
        assert response.status_code == 200
        assert response.json()["email"] == "joao@example.com"

        # Login
        response = await ac.post("/usuarios/login", json={
            "email": "joao@example.com",
            "senha": "123456"
        })
        assert response.status_code == 200
        assert "access_token" in response.json()
