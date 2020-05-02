// Keep track of total votes

import React, { useState } from 'react';

export default function useTotalVotes() {
    const [totalVotes, setTotalVotes] = useState(0);

    function incrementTotalVotes() {
        setTotalVotes(totalVotes + 1);
    }

    return [totalVotes, incrementTotalVotes];
}
