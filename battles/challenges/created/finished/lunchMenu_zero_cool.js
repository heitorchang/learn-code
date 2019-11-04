function lunchMenu(menu) {
    const allDishes = [...new Set(menu.reduce((c, d) => [...c, ...d], []))];
    const indices = {};
    const bits = {};
    
    for(let j = 0; j < allDishes.length; j++) {
        const item = allDishes[j];
        const index = /(?:^| )bean/.test(item) ? -(j + 1) : (j + 1);
        indices[item] = index;
        bits[item] = 1 << j;
    }
    
    return (function count(i = 0, b = 2, dishes = 0, combs = new Set()) {
        if(i >= 5) combs.add(dishes);
        else {
            for(const item of menu[i]) {
                // did we already eat this item?
                if((dishes & bits[item]) === 0) {
                    // does it have beans?
                    if(indices[item] < 0) {
                        // can we handle another bean dish?
                        if(b > 0) count(i + 1, b - 1, dishes ^ bits[item], combs);
                    } else count(i + 1, b, dishes ^ bits[item], combs);
                }
            }

            return combs.size;
        }
    })();
}
