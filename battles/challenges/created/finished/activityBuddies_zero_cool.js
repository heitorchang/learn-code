function activityBuddies(ratings) {
    const howManyStudents = ratings.length;
    const howManyActivities = ratings[0].length;
    
    if(howManyActivities * 2 === howManyStudents) return Array(howManyActivities).fill(2);
    
    let best = 0;
    let result = Array(howManyActivities).fill(0);
    
    // dfs match, backtrack if not enough students left for all activities
    (function match(
        student = 0, 
        score = 0, 
        signedUp = Array(howManyActivities).fill(0), 
        lacking = howManyActivities * 2
    ) {
        if(student === howManyStudents) return {signedUp: signedUp, score};
        
        for(let activity = 0; activity < howManyActivities; activity++) {
            if(signedUp[activity] < 2) {
                lacking--;
                signedUp[activity]++;
            
                const next = match(student + 1, score + ratings[student][activity], signedUp, lacking);

                if(best < next.score) {
                    best = next.score;
                    result = [...next.signedUp];
                }
                
                signedUp[activity]--;
                lacking++;
            } else if(lacking <= howManyStudents - student - 1) {
                signedUp[activity]++;
            
                const next = match(student + 1, score + ratings[student][activity], signedUp, lacking);

                if(best < next.score) {
                    best = next.score;
                    result = [...next.signedUp];
                }
                
                signedUp[activity]--;
            }
        }
        
        return {signedUp: result, score: best};
    })();
    
    return result;
}
