// 問題
// https://paiza.jp/works/mondai/drankfast/d1_step_distance


process.stdin.resume();
process.stdin.setEncoding('utf8');
// 自分の得意な言語で
// Let's チャレンジ！！
var lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', (line) => {
  lines.push(line);
});
reader.on('close', () => {
    const inputs = lines[0];
    
    const d = inputs[0];
    const s = inputs[1];
  
    if (d*100000 / s >= 100000){
        console.log('yes');
    }
    else{
        console.log('no');
    }
});
