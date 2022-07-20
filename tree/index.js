const express = require('express')
const app = express()

app.get('/', function (request, response) {
  response.sendFile('/Users/zhangtianhong/I-keep-leetcode/tree/README.md')
})

const PORT = 8000
app.listen(PORT, () => {
  console.log(`App is listening on ${PORT}`)
})
