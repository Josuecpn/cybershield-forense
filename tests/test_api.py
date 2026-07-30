def test_deve_retornar_lista_de_atacantes_vazia(client):
    """TDD Red: A API deve iniciar sem nenhum atacante registrado."""
    response = client.get("/api/v1/atacantes")
    assert response.status_code == 200
    assert response.json() == []

def test_deve_retornar_lista_de_atacantes_vazia(client):
    """TDD Green: A API deve iniciar sem nenhum atacante registrado."""
    response = client.get("/api/v1/atacantes")
    assert response.status_code == 200
    assert response.json() == []


def test_deve_criar_um_novo_atacante_com_sucesso(client):
    """TDD Red: O sistema deve ser capaz de registrar um IP suspeito no banco."""
    # Arrange (Dados fictícios de um servidor atacante na Rússia)
    payload = {
        "ip_origem": "185.92.22.10",
        "pais": "Rússia",
        "asn": "Hosting Operator LLC",
        "reputacao_score": 8.5
    }
    
    # Act (Envia a requisição POST para a API)
    response = client.post("/api/v1/atacantes", json=payload)
    
    # Assert (Verificações do resultado)
    assert response.status_code == 201
    dados = response.json()
    assert dados["id"] is not None
    assert dados["ip_origem"] == "185.92.22.10"
    assert dados["reputacao_score"] == 8.5

def test_deve_vincular_um_incidente_a_um_atacante_existente(client):
    """TDD Red: O monitor deve ser capaz de registrar uma tentativa de ataque vinculada a um IP."""
    # 1. Primeiro criamos o Atacante para garantir que o IP exista no banco de testes
    atacante_payload = {
        "ip_origem": "45.230.12.4",
        "pais": "Brasil",
        "asn": "Telefônica Brasil",
        "reputacao_score": 5.0
    }
    client.post("/api/v1/atacantes", json=atacante_payload)

    # 2. Arrange: Prepara os dados do ataque cibernético (Injeção SQL)
    incidente_payload = {
        "ip_origem": "45.230.12.4",
        "metodo_http": "POST",
        "url_requisitada": "/admin/login",
        "status_code": 401,
        "payload_suspeito": "admin'--",
        "user_agent": "Mozilla/5.0",
        "tipo_ataque": "SQL Injection"
    }

    # 3. Act: Envia a requisição POST para registrar o incidente
    response = client.post("/api/v1/incidentes", json=incidente_payload)

    # 4. Assert: Verifica se o incidente foi criado e associado corretamente
    assert response.status_code == 201
    dados = response.json()
    assert dados["id"] is not None
    assert dados["metodo_http"] == "POST"
    assert dados["tipo_ataque"] == "SQL Injection"