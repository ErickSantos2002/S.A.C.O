"""
test_agendamentos.py
---------------------
Testa criação e listagem de agendamentos.
"""

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_criar_listar_agendamento():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Login para obter token
        login = await ac.post("/usuarios/login", json={
            "email": "joao@example.com",
            "senha": "123456"
        })
        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # Criar agendamento
        response = await ac.post("/agendamentos/", headers=headers, json={
            "data_hora": "2025-05-10T10:00:00",
            "local": "Sala A",
            "descricao": "Reunião de planejamento"
        })
        assert response.status_code == 200
        assert response.json()["local"] == "Sala A"

        # Criar conflito (mesmo horário)
        conflict = await ac.post("/agendamentos/", headers=headers, json={
            "data_hora": "2025-05-10T10:00:00",
            "local": "Sala B",
            "descricao": "Outro evento"
        })
        assert conflict.status_code == 400

        # Listar agendamentos
        lista = await ac.get("/agendamentos/", headers=headers)
        assert lista.status_code == 200
        assert isinstance(lista.json(), list)
        assert len(lista.json()) >= 1
