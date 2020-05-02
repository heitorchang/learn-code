import React, { useState } from 'react';
import VoteCounter from './VoteCounter';

export default function BallotBox() {
    const [totalVotes, setTotalVotes] = useState(0);
    const [voterLabel, setVoterLabel] = useState("You're an undecided minion.");
    
    const handleClick = (candidate) => {
        setTotalVotes(totalVotes + 1);
        changeVoterLabel(candidate);
    }

    const changeVoterLabel = (candidate) => {
        setVoterLabel(candidate + "minion detected.");
    }
    
    return (
        <div>
        <p>
        {voterLabel}
        </p>
        Total votes: {totalVotes}
        <br />
        <VoteCounter candidate="Ciro" onClick={handleClick} />
        <VoteCounter candidate="Bolso" onClick={handleClick} />
        <VoteCounter candidate="Marina" onClick={handleClick} />
        </div>
    );
}
