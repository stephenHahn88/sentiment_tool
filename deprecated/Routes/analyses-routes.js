const express = require("express");
const Analyses = require("../models/dbHelpers");

const router = express.Router()

router.get('/', (request, response) => {
    Analyses.find()
        .then(analyses => {
            response.status(200).json(analyses)
        })
        .catch(error => {
            response.status(500).json({message: error})
        })
})

router.post('/', (request, response) => {
    Analyses.add(request.body)
        .then(analysis => {
            response.status(200).json(analysis)
        })
        .catch(error => {
            response.status(500).json({message: error})
        })
})

module.exports = router