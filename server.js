const express = require('express');
const Datastore = require('nedb')

const app = express()

// const portNumber = 8080
const port = process.env.PORT || 8080
app.listen(port, () => console.log("listening at " + port))
app.use(express.static('public'))
app.use(express.json({ limit: '1mb' }))

const database = new Datastore('database.db')
database.loadDatabase()

app.post('/api', (request, response) => {
    const data = request.body
    data.analysis = data.analysis.split("\,\n")
    data.timestamp = Date.now()

    database.insert(data)
    response.json({
        status: "success"
    });
})
