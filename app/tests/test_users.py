import pytest
from httpx import AsyncClient
from app.main import app
import uuid

@pytest.mark.asyncio
async def test_cadastro_login_usuario():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        email = f"erick_{uuid.uuid4().hex[:6]}@example.com"

        # Cadastro
        response = await ac.post("/usuarios/cadastro", json={
            "nome": "Erick",
            "email": email,
            "senha": "123456"
        })

        print("STATUS CADASTRO:", response.status_code)
        print("RESPOSTA CADASTRO:", response.json())

        assert response.status_code == 200
        assert response.json()["email"] == email

        # Login
        login = await ac.post("/usuarios/login", json={
            "email": email,
            "senha": "123456"
        })

        assert login.status_code == 200
        assert "access_token" in login.json()
