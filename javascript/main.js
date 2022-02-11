import express from 'express'

const app = express()
const port = 3000

app.get('/validate', (req, res) => {
    res.send('TODO: validate word results')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})