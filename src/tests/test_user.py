def test_user_register(client):
    data = {"nome": "guilherme", "email": "gg@g.com", "senha": "123"}

    response = client.post("/api/users", data=data)
    result = response.get_json()
    assert result["message"] == "usuário registrado com sucesso!"
