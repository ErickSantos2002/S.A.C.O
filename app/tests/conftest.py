import pytest
from httpx import AsyncClient
from app.main import app
import uuid

@pytest.fixture
async def auth_headers():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        email = f"test_{uuid.uuid4().hex[:6]}@example.com"
        senha = "123456"

        # Cadastro
        response = await ac.post("/usuarios/cadastro", json={
            "nome": "Usuário Teste",
            "email": email,
            "senha": senha
        })
        assert response.status_code == 200

        # Login
        login = await ac.post("/usuarios/login", json={
            "email": email,
            "senha": senha
        })
        assert login.status_code == 200
        token = login.json()["access_token"]
        return {"Authorization": f"Bearer {token}"}
