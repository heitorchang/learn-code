import React, { useState } from 'react';
import VoteCounter from './VoteCounter';
import './BallotBox.css';


export default function BallotBox() {
    const [totalVotes, setTotalVotes] = useState(0);
    const [voterLabel, setVoterLabel] = useState("You're an undecided minion. Vote for someone.");
    
    const handleClick = (candidate) => {
        setTotalVotes(totalVotes + 1);
        changeVoterLabel(candidate);
    }

    const changeVoterLabel = (candidate) => {
        setVoterLabel(candidate + "minion detected.");
    }

    const candidates = ["Bolso", "Haddad", "Ciro", "Alckmin", "Marina", "Meirelles"];
    
    return (
        <div>
        <p className="voter-label">
        {voterLabel}
        </p>
        {
            candidates.map(candidate =>
                <VoteCounter candidate={candidate} onClick={handleClick} ballotBoxTotal={totalVotes} />)
        }
        <b>
        Total votes: {totalVotes}
        </b>
        </div>
    );
}
