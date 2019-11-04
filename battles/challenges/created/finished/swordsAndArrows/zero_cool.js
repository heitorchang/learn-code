function swordsAndArrows(grid) {
    const knightRanges = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    const archerRanges = [[3, 0], [2, 1], [1, 2], [0, 3], 
                          [-1, 2], [-2, 1], [-3, 0], [-2, -1], 
                          [-1, -2], [0, -3], [1, -2], [2, -1]];
    const width = grid[0].length;
    
    // scan the map for friendly units
    const knights = [];
    const archers = [];
    
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            if(grid[i][j] === "K") knights.push([i, j]);
            if(grid[i][j] === "A") archers.push([i, j]);
        }
    }
    
    // bfs each unit to find possible attack points
    function getAttackPoints(x, y, moves, ranges) {
        const queue = [[x, y, moves]];
        const visited = new Set();
        visited.add(1e5 * x + y);
        
        const attackPoints = [];
        
        while(queue.length) {
            const [x, y, moves] = queue.shift();
            
            // check for enemies in range
            for(const [dx, dy] of ranges) {
                const [attackX, attackY] = [x + dx, y + dy];
                if(attackX in grid 
                   && 0 <= attackY 
                   && attackY < width 
                   && grid[attackX][attackY] === "E" ) {
                    attackPoints.push([1e5 * x + y, 1e5 * attackX + attackY]);
                }
            }
            
            // advance
            if(moves > 0) {
                for(const [dx, dy] of [[1, 0], [0, 1], [-1, 0], [0, -1]]) {
                    const [nextX, nextY] = [x + dx, y + dy];
                    const nextHash = 1e5 * nextX + nextY;
                    
                    if(nextX in grid 
                       && 0 <= nextY 
                       && nextY < width 
                       && grid[nextX][nextY] !== "E" 
                       && !visited.has(nextHash)) {
                        visited.add(nextHash);
                        queue.push([nextX, nextY, moves - 1]);
                    }
                }
            }
        }
        
        return attackPoints;
    }
    
    const attackPoints = [];
    
    for(const [x, y] of knights) {
        attackPoints.push(getAttackPoints(x, y, 7, knightRanges));
    }
    
    for(const [x, y] of archers) {
        attackPoints.push(getAttackPoints(x, y, 4, archerRanges));
    }
    
    // backtracking recursion over all attack positions 
    // to find the arrangement with maximum damage
    function assign(attackPoints, 
                    i = attackPoints.length - 1, 
                    enemiesAttacked = new Set(), 
                    spotsOccupied = new Set(), 
                    total = 0) {
        if(i < 0) return total;
        
        let best = assign(attackPoints, i - 1, enemiesAttacked, spotsOccupied, total);
        
        for(const [pos, enemy] of attackPoints[i]) {
            if(!enemiesAttacked.has(enemy) && !spotsOccupied.has(pos)) {
                enemiesAttacked.add(enemy);
                spotsOccupied.add(pos);
                
                best = Math.max(
                    best, 
                    assign(
                        attackPoints, 
                        i - 1, 
                        enemiesAttacked, 
                        spotsOccupied, 
                        total + 1
                    )
                );
                
                enemiesAttacked.delete(enemy);
                spotsOccupied.delete(pos);
            }
        }
        
        return best;
    }
    
    return assign(attackPoints);
}
