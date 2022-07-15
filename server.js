const express = require('express');
// const Datastore = require('nedb');
// const knex = require('knex');
// const config = require("knexfile");
// const db = knex(config.development)
const sqlite = require('sqlite3');
const { Client } = require('pg');
const Analyses = require('./models/dbHelpers')

const server = express()
server.use(express.static('public'))
server.use(express.json({ limit: '1mb' }))

const PORT = process.env.PORT || 8080
server.listen(PORT, () => console.log(`listening at ${PORT}`))


// const database = new Datastore('database.db')
// database.loadDatabase()

// const client = new Client({
//     connectionString: process.env.DATABASE_URL,
//     ssl: {
//         reject Unauthorized: false
//     }
// });
//
// await client.connect();

server.get('/api/analyses', (request, response) => {
    Analyses.find()
        .then(analyses => {
            response.status(200).json(analyses)
        })
        .catch(error => {
            response.status(500).json({message: error})
        })
})

server.post('/api/analyses', (request, response) => {
    Analyses.add(request.body)
        .then(analysis => {
            response.status(200).json(analysis)
        })
        .catch(error => {
            response.status(500).json({message: error})
        })
})
