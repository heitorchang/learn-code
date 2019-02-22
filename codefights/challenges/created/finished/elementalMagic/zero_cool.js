function elementalMagic(yourHP, monsters) {
    const parts = monsters.map(mon => mon.split(","));
    const weaknesses = parts.map(part => part[0]);
    const zorbs = parts.map(part => part[1]);
    
    // unbeatable enemy, run!
    if(zorbs.includes("BFW")) return "R";
    
    const healths = parts.map(part => parseInt(part[2]));
    const damage = {};
    
    for(const spell of "BFW") {
        const mons = Array.from(
            {length: parts.length}, 
            (_, i) => -2 
                      + 3 * (zorbs[i].includes(spell)) 
                      - 3 * (weaknesses[i].includes(spell))
        );
        damage[spell] = mons;
    }
    
    // bfs, backtrack on 0hp
    const queue = [["", healths, yourHP]];
    
    while(queue.length) {
        const [spells, monHealths, hp] = queue.shift();
        
        // all enemies defeated?
        if(monHealths.every(hp => hp <= 0)) return spells;
        
        for(const spell of "BFW") {
            const newHealths = monHealths.map((hp, i) => hp > 0 ? hp + damage[spell][i] : hp);
            const hpRemaining = hp - newHealths.filter(hp => hp > 0).length;
            if(hpRemaining > 0) queue.push([spells + spell, newHealths, hpRemaining]);
        }
    }
    
    // they're too strong! get outta there!
    return "R";
}
