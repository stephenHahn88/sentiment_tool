const express = require("express");
const analysesRouter = require("../Routes/analyses-routes")

const server = express()

server.use(express.static('public'))
server.use(express.json({ limit: '1mb' }))

server.use('/api/analyses', analysesRouter)

module.exports = server