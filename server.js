const express = require('express');
const { Pool } = require("pg");
const app = express();

// Connect to pg database
const pool = new Pool({
    host: 'localhost',
    port: 5432,
    user: 'postgres',
    password: 'islom2006',
    database: 'postgres'
});

pool.connect()
    .then(() => {
        console.log("Connected to database");
    })
    .catch((err) => {
        console.log("Error in database");
        console.log(err);
    });

const PORT = 7777;

app.get("/authors", async (req, res) => {
    try {
        const { country, birth_year } = req.query; // Fixed: correct variable names
        
        if (country && birth_year) {
            const result = await pool.query(
                `SELECT * FROM authors WHERE country = $1 AND birth_year = $2`, // Fixed: = instead of >
                [country, birth_year]
            );
            res.status(200).json(result.rows);
        } else {
            const result = await pool.query(
                `SELECT * FROM authors`
            );
            res.status(200).json(result.rows);
        }
    } catch (error) {
        console.log(error);
        res.status(500).json({ error: "Internal server error" }); // Added error response
    }
});
// Middleware
app.use(express.json());

// POST  api 
/*
app.post('/sukhoi', async (req, res) => {
    try {
        console.log(req.body); // Log the request body
        const { model, aircraft_type, first_flight, max_speed_kmh, range_km, service_ceiling_m, crew, status } = req.body;
        const result = await pool.query(
        `INSERT INTO sukhoi (model, aircraft_type, first_flight, max_speed_kmh, range_km, service_ceiling_m, crew, status)
         VALUES ($1, $2, $3, $4, $5, $6, $7, $8) RETURNING *`,
        [model, aircraft_type, first_flight, max_speed_kmh, range_km, service_ceiling_m, crew, status]
        );
       // write me full json data to test in thunder client in body
       
       

        res
            .status(201)
            .json({ message: "New aircraft added", aircraft: result.rows[0] });

    } catch (error) {
        console.log(error);
        res.status(500).json({ error: "Internal server error" });
    }
});
/*
app.put('/sukhoi/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const {model, aircraft_type, first_flight, max_speed_kmh, range_km, service_ceiling_m, crew, status} = req.body;
        if (!model || !aircraft_type || !first_flight || !max_speed_kmh || !range_km || !service_ceiling_m || !crew || !status) {
            return res.status(400).json({ message: "All fields are required" });
        }
        const result = await pool.query(
            `UPDATE sukhoi SET 
            model = $1,
            aircraft_type = $2,
            first_flight = $3,
            max_speed_kmh = $4,
            range_km = $5,
            service_ceiling_m = $6,
            crew = $7,
            status = $8 
            WHERE id = $9 RETURNING *`,
            [model, aircraft_type, first_flight, max_speed_kmh, range_km, service_ceiling_m, crew, status, id]
        );  
        res
            .status(200)
            .json({ message: "Aircraft updated", aircraft: result.rows[0] });
    } catch (error) {
        console.log(error);
        res.status(500).json({ error: "Internal server error" });
    }
});
*/

// Delete api

app.get('/sukhoi/list', async (req, res)=>{
    try{
        const result = await pool.query('SELECT * FROM sukhoi');
        res.status(200).json(result.rows);
    }catch (error){
        console.log(error);
        res.status(500).json({error: "Internal server error"});
    }
});

app.get('/sukhoi/id', async (req, res) => {
    try {
        const { id } = req.params;
        const result = await pool.query('SELECT * FROM sukhoi WHERE id = $1', [id]);

        if (result.rowCount === 0) {
            return res.status(404).json({ message: "Aircraft not found" });
        }

        res.status(200).json(result.rows[0]);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: "Internal server error" });
    }
});


app.delete('/sukhoi/:id', async (req,res)=>{
    try{
        const {id} = req.params;
        const result = 
        await pool.query('DELETE FROM sukhoi WHERE id = $1 RETURNING *', [id]);
        if (result.rowCount === 0){
            res.status(404).json({message: "Aircraft not found"});

        }
        res.status(200).json({message: "Aircraft deleted from sukhoi", aircraft: result.rows[0]});
    } catch (error){
        console.log(error);
        res.status(500).json({error: "Internal server error"}); 
    }
})

app.use('/tesha', (request, response) => {
    response.send('SERVER SAID PINCHILING "Bombaclastic!!!"');
});

app.listen(PORT, () => {
    console.log(`Girgittoningiz ${PORT} in ready for service`); // Fixed: proper template literal

});
