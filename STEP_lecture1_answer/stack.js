'use strict'
// Please don't delete the 'use strict' line above

// 普通のstackの実装
const normalStack = new Array();
const pushNum = [5, 1, 2, 3];

// 配列pushNumの値を左から順にnormalStackにいれる
for (var n of pushNum){
    normalStack.push(n);
    console.log(`${n}を追加`);
    console.log(normalStack);
}

// このstackから最大値を探す
function serchMaxFromNormalStack(stack){
    const copyOfStack = [...stack];
    var popedValue;
    var ans = 0;
    for(var i=0; i < stack.length; i++){
        popedValue = copyOfStack.pop()
        if (popedValue > ans){
            // ans をこえる大きさの値がポップされたときに、その値を保存する
            ans = popedValue;
        }
    }

    return ans
}

// 5が返るはず
console.log("normalStackの最大値：");
console.log(serchMaxFromNormalStack(normalStack));


// 以下、lectureの中で説明があったStack
const maxSaveStack = new Array();

// pushするものは上のコードと同様
// const pushNum = [5, 1, 2, 3];

// 配列pushNumの値を左から順にmaxSaveStackにいれる
// push時点での最大値もセットで保存
var maxValue = 0;

for (var n of pushNum){
    if (maxValue < n){
        // maxValueを更新
        maxValue = n;
    }
    maxSaveStack.push([n, maxValue]);
    console.log(`${n}を追加：この時点で最大値は${maxValue}`);
    console.log(maxSaveStack);
}

// このstackから最大値を探す
function serchMaxFromStack(stack){
    var popedValue = stack.pop();

    // popされた配列の中身は、[最新の値, 最大値]
    return popedValue[1];
}

// 5が返るはず
console.log("maxSaveStackの最大値：");
console.log(serchMaxFromStack(maxSaveStack));
