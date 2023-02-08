const toRoman = function(num) {
    let result = ""
    const romanObj = {
        M:  1000,
        CM: 900,
        D:  500,
        CD: 400,
        C:  100,
        XC: 90,
        L:  50,
        XL: 40,
        X:  10,
        IX: 9,
        V:  5,
        IV: 4,
        I:  1,
      };
    while(num > 0){
        for(let i in romanObj){
            if (num / romanObj[i] >= 1){
                result += i
                num -= romanObj[i]
                console.log(num)
                break; // break out from the for loop only
            }
        }
    }
    console.log(result)
    return result
};

module.exports = {toRoman}