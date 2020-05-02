import React, { useState, useEffect, useRef } from 'react';
import './ClickCounter.css';
import useTotalVotes from './useTotalVotes';

export default function VoteCounter(props) {
    const isInitialMount = useRef(true);

    // doesn't work
    // const [totalVotes, incrementTotalVotes] = useTotalVotes();
    
    const [votes, setVotes] = useState(0);

    useEffect(() => {
        if (isInitialMount.current) {
            isInitialMount.current = false;
        } else {
            // document.title = `${props.candidate}minion detected`;
        }
    }, [votes]);
        
    return (
        <div>
        <button className="vote-button" onClick={() => {
            setVotes(votes + 1);
            // incrementTotalVotes();
            props.onClick(props.candidate);
        }}>
            Vote
            </button>
        {props.candidate}: {votes} vote(s)
        </div>
    );
}
