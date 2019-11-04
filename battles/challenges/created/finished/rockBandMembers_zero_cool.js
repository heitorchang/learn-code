const indices = {"B": 1, "D": 2, "G": 4, "V": 8};
const limit = 1e9 + 7;

function rockBandMembers(students, i = 0, used = 0, memo = {}) {
    if(used === 15) return 1;
    if(i >= students.length) return 0;

    const hash = 100 * i + used;
    if(hash in memo) return memo[hash];

    let total = rockBandMembers(students, i + 1, used, memo);
    const [name, roles] = students[i].split(",");

    for(const role of roles) {
        const index = indices[role];
        if((used & index) === 0) 
            total = (total + rockBandMembers(students, i + 1, used ^ index, memo)) % limit;
    }

    memo[hash] = total;
    return total;
}
