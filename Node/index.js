const { exec } = require("child_process");
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function tempsExec(lang, path) {
    var timer = process.hrtime();
    switch(lang) {
        case 'js':
            exec('node ' + path, (error, stdout, stderr) => {
                console.log(stdout);
            })
            break;
        case 'py':
            exec(path, (error, stdout, stderr) => {
                console.log(stdout);
            })
            break;
    }
    return console.log(process.hrtime(timer));
}

function envoieReq(host, number) {
    console.log('EnvoieRequete')
}

function inputUser(data) {
    readline.question('Quelle test effectué: ', test => {
        switch(test) {
            case 'te':
                tempsExec('js', './test.js');
                break;
            case 'er':
                envoieReq();
                break;
        }
    });
}

inputUser();
