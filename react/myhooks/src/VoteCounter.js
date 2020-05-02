import React, { useState, useEffect, useRef } from 'react';
import './ClickCounter.css';

function VoteCounter(props) {
    const isInitialMount = useRef(true);
    
    const [votes, setVotes] = useState(0);

    useEffect(() => {
        if (isInitialMount.current) {
            isInitialMount.current = false;
        } else {
            document.title = `${props.candidate}minion detected`;
        }
    });
        
    return (
        <div>
        <button className="vote-button" onClick={() => setVotes(votes + 1)}>Vote</button>
        {props.candidate}: {votes} vote(s)
        </div>
    );
}

export default VoteCounter;
