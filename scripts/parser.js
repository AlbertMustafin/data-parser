const fs = require('fs');
const readline = require('readline');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
    this.data = [];
  }

  async parseFile() {
    const fileStream = fs.createReadStream(this.filePath);
    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity
    });
    rl.on('line', (line) => {
      this.data.push(line);
    });
    await new Promise((resolve, reject) => {
      rl.on('close', () => {
        resolve();
      });
      rl.on('error', (err) => {
        reject(err);
      });
    });
  }

  async parse() {
    await this.parseFile();
    return this.data;
  }
}

module.exports = Parser;