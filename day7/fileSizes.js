
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

class ElfDir {
    constructor(name, parentDir) {
        this.name = name;
        this.contents = {};
        this.dirSize = 0;
        this.parentDir = parentDir;
    }

    addFile(fileName, size) {
        this.contents[fileName] = new ElfFile(size);
        this.increaseSize(size)
    }

    addDir(dirName) {
        this.contents[dirName] = new ElfDir(dirName, this);
    }

    increaseSize(size) {
        let sizeInt = parseInt(size);
        console.log("increasing size for directory ", this.name)
        this.parentDir && this.parentDir.increaseSize(sizeInt);
        this.dirSize += sizeInt;
    }
}

class ElfFile {
    constructor(size) {
        this.size = size;
    }
}

function readInput(tld, currDir) {
    readline.question('cmd ', text => {
        if (text === 'done') {
            console.log(tld);
            addUpLargeFiles(tld, 0);
            readline.close();
            return;
        }

        let inputArray = text.split(" ");

        if (inputArray[0] == '$' && inputArray[1] == 'ls') {
            readInput(tld, currDir);

        } else if (inputArray[0] == '$' && inputArray[1] == 'cd') {
            if (inputArray[2] == '/') {
                currDir = tld;
            } else if (inputArray[2] == '..') {
                currDir = currDir.parentDir;
            } else {
                currDir = currDir.contents[inputArray[2]]
            }
            
        } else if (inputArray[0] == 'dir') {
            currDir.addDir(inputArray[1]);
        } else {
            currDir.addFile(inputArray[1], inputArray[0]);
        }
        readInput(tld, currDir);
    })
}

let size = 0;
function addUpLargeFiles(dir) {
    console.log('add large files', dir.name)
    let keys = Object.keys(dir.contents);
    for (let i = 0; i < keys.length; i++) {
        let item = dir.contents[keys[i]];
        if (item instanceof ElfDir) {
            console.log(item.dirSize)
            size += item.dirSize <= 100000 ? item.dirSize : 0;
            console.log(size)
            addUpLargeFiles(item);
        }
    }
    if (dir.name == '/') {
        console.log(size)
    }
}

const tld = new ElfDir('/', null);
readInput(tld, tld)

