const express = require('express');
const{ Pool } = require("pg")

const app = express();

//connect to pg database

const pool = new Pool({
    host: 'localhost',
    port: 5432,
    user: 'postgres',
    password: 'islom2006',
    database: 'postgres'
})

pool.connect()
.then(()=>{
    console.log("Connected to database")
})
.catch((err)=>{
    console.log("Error in database");
    console.log(err);
})

const PORT = 7777

app.use('/tesha',(request,response)=>{
    response.send('SERVER SAID PINCHILING "Bombaclastic!!!"')
})

app.listen(PORT,()=>{
    console.log(`Girgittoningiz ${PORT} in ready for service `);
});

