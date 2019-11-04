function booAnalysis(sounds) {
    const amounts = [];
    let lastChar = "u";
    let howMany = 0;
    
    for(const char of sounds) {
        if(char === lastChar) howMany++;
        else {
            if(amounts.length || lastChar === "o") amounts.push(howMany);
            howMany = 1;
        }
        
        lastChar = char;
    }
    
    if(lastChar === "o") amounts.push(howMany);
    
    function count(i = 1, used = 0, memo = {}) {
        if(i > amounts.length - 1) return 0;
        
        const remaining = Math.min(amounts[i - 1] - used, amounts[i + 1]);
        const hash = i * 1e6 + remaining;
        if(hash in memo) return memo[hash];
        
        let best = 0;
        
        for(let amt = remaining; amt >= 0; amt--) {
            const length = amt ? 2 * amt + amounts[i] : 0;
            best = Math.max(best, count(i + 2, amt, memo) + length);
        }
        
        memo[hash] = best;
        return best;
    }
    
    return count();
}
