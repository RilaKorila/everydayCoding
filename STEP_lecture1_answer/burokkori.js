'use strict'
// Please don't delete the 'use strict' line above


function burokkori(str){
    // 文字列のWとGの数を数える
    var counterW = 0;
    var counterG = 0;

    for(var i=0; i<str.length; i++){
        if (str[i] === "W"){
            counterW += 1;
        }
        else{
            counterG += 1;
        }
    }

    console.log(counterG, counterW);

    // 最小の合計数が答え
    var ans = str.length;
    // 境界線より左のW
    var leftW = 0;
    // 境界線より右のG
    var rightG = counterG;

    // 「境界線より左のW」と「境界線より右のG」の数を数える
    for(var i=0; i<str.length; i++){
        if (str[i] === "W"){
            // 今、Wにいるなら、
            // 次の境界線では、「境界線より左のW」の数がふえ、「境界線より右のG」の数はそのまま
            leftW += 1;
        }
        else{
            // 今、Gにいるなら、
            // 次の境界線では、「境界線より左のW」の数はそのままで、「境界線より右のG」の数は１つ減る
            rightG -= 1;
        }

        // 合計値がansより小さければansに保存しておく
        if (ans > leftW + rightG){
            ans = leftW + rightG;
        }
    }

    return ans;
}

function test(actual, expected) {
    if (JSON.stringify(actual) === JSON.stringify(expected)) {
      console.log("Yay! Test PASSED.");
    } else {
      console.error("Test FAILED. Keep trying!");
      console.log("    actual: ", actual);
      console.log("  expected: ", expected);
      console.trace();
    }
  }

const test1 = "WGGGGW"
const test2 = "GWGWG"
const test3 = "GWGGWGWW"

// テストケース１
test(burokkori(test1), 1)

// テストケース２
test(burokkori(test2), 2)

// テストケース3
test(burokkori(test2), 2)
