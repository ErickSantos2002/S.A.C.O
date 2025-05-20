import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
import uuid

async def test_criar_listar_agendamento():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        email = f"erick_{uuid.uuid4().hex[:6]}@example.com"

        # Criar usuário (cadastro)
        await ac.post("/usuarios/cadastro", json={
            "nome": "Erick",
            "email": email,
            "senha": "123456"
        })

        # Login para obter token
        login = await ac.post("/usuarios/login", json={
            "email": email,
            "senha": "123456"
        })

        assert login.status_code == 200
        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # Criar agendamento
        response = await ac.post("/agendamentos/", headers=headers, json={
            "data_hora": "2025-05-10T19:00:00",
            "local": "Sala A",
            "descricao": "Perguntar a Lucas se vai ter chamada"
        })
        print("STATUS AGENDAMENTO:", response.status_code)
        print("RESPOSTA AGENDAMENTO:", response.json())

        assert response.status_code == 200
        assert response.json()["local"] == "Sala A"

        # Criar conflito (mesmo horário)
        conflict = await ac.post("/agendamentos/", headers=headers, json={
            "data_hora": "2025-05-10T19:00:00",
            "local": "Sala B",
            "descricao": "Já perguntei a lucas se teve chamada?"
        })
        assert conflict.status_code == 400

        # Listar agendamentos
        lista = await ac.get("/agendamentos/", headers=headers)
        assert lista.status_code == 200
        assert isinstance(lista.json(), list)
        assert len(lista.json()) >= 1
