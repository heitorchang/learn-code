// O(log(width + height))
function poolTableBounce(width, height) {
    const gcd = (a, b) => b % a ? gcd(b % a, a) : a;
    const lcm = (a, b) => a * b / gcd(a, b);
    
    const multiple = lcm(width / 2, height);
    const [x, y] = [width / 2, height].map(dim => multiple / dim);
    const absval = Math.abs(x % 4 - 2);
    
    return y % 2 ? 3 - absval : 4 + absval;
}






function poolTableBounceBrute(width, height) {
    let [x, y] = [0, 0];
    let [dx, dy] = [1, 1];
    
    function checkPockets(x, y) {
        if(y === 0 && x === width / 2) {
            return 5;
        }
        
        if(y === height) {
            if(x === 0) return 1;
            if(x === width / 2) return 2;
            if(x === width) return 3;
        }
        
        return -1;
    }
    
    while(true) {
        const offsetX = dx === 1 ? width - x : x;
        const offsetY = dy === 1 ? height - y : y;
        const offset = Math.min(offsetX, offsetY);
        
        x += dx * offset;
        y += dy * offset;
        
        if(x === width || x === 0) dx *= -1;
        if(y === height || y === 0) dy *= -1;
        
        const pocket = checkPockets(x, y);
        if(pocket !== -1) return pocket;
    }
}
