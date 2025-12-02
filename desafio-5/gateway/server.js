const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 8080;

const USERS_SERVICE_URL = 'http://users-service:5001';
const ORDERS_SERVICE_URL = 'http://orders-service:5002';

app.get('/', (req, res) => {
    res.send('<h1>API Gateway Ativo</h1><p>Rotas: /users, /orders</p>');
});

app.get('/users', async (req, res) => {
    try {
        console.log("Encaminhando para Users Service...");
        const response = await axios.get(`${USERS_SERVICE_URL}/users`);
        res.json(response.data);
    } catch (error) {
        console.error("Erro no Users Service:", error.message);
        res.status(500).json({ error: 'Erro ao comunicar com Users Service' });
    }
});

app.get('/orders', async (req, res) => {
    try {
        console.log("Encaminhando para Orders Service...");
        const response = await axios.get(`${ORDERS_SERVICE_URL}/orders`);
        res.json(response.data);
    } catch (error) {
        console.error("Erro no Orders Service:", error.message);
        res.status(500).json({ error: 'Erro ao comunicar com Orders Service' });
    }
});

app.listen(PORT, () => {
    console.log(`Gateway rodando em http://localhost:${PORT}`);
});