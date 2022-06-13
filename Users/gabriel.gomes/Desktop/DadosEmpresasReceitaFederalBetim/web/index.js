var fs = require('fs')

var csv = require('fast-csv')

var stream = fs.createReadStream("dados.csv")

var streamCsv = csv().on('data', data => console.log(data))

stream.pipe(streamCsv)