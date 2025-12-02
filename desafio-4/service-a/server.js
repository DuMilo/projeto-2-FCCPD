const express = require('express');
const app = express();
const PORT = 3000;

const users = [
    { id: 1, name: "Milo", role: "Data Scientist", since: 2021 },
    { id: 2, name: "Giullia", role: "Security Analyst", since: 2023 },
    { id: 3, name: "Sofia", role: "Java Developer", since: 2019 }
];

app.get('/users', (req, res) => {
    console.log(`[Service A] Recebi uma requisição em /users`);
    res.json(users);
});

app.listen(PORT, () => {
    console.log(`Service A rodando na porta ${PORT}`);
});