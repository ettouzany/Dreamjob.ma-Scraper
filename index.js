const express = require('express')
const app = express()
const port = 4000

app.get('/', (req, res) => {
    //run  python script to get data from database
    const python = require('child_process').spawn('python3', ['./test.py']);
    console.log('python script started');
    console.log(python);
    //run python script and wait for it to finish
    python.on('close', (code) => {
        console.log(`python script finished with code ${code}`);
        //read data from file
        const fs = require('fs');
        const data = fs.readFileSync('./output.json');
        const json = JSON.parse(data);
        console.log(json);
        //send data to client
        res.send(json);
    }
    );
}
);


//     python.stdout.on('close', (code) => {
//         console.log(`python script finished with code ${code}`);
//         //read data from file
//         const fs = require('fs');
//         const data = fs.readFileSync('./output.json');
//         const json = JSON.parse(data);
//         console.log(json);
//         //send data to client
//         res.send(json);
//     }
//     );
// })

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
