def test_deve_retornar_lista_de_atacantes_vazia(client):
    """TDD Red: A API deve iniciar sem nenhum atacante registrado."""
    response = client.get("/api/v1/monitor/atacantes")
    assert response.status_code == 200
    assert response.json() == []
