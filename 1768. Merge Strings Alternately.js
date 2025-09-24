/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let firstLength = word1.length, secondLength = word2.length;
    let firstPointer = 0
    let secondPointer = 0
    let result = ''

    while (firstPointer < firstLength && secondPointer < secondLength){
        result+=word1[firstPointer++];
        result+=word2[secondPointer++];
    }

    while (firstPointer < firstLength){
        result += word1[firstPointer++]
    }

    while (secondPointer < secondLength){
        result += word2[secondPointer++]
    }

    return result;
};
