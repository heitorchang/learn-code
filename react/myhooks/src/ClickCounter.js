import React, { useState } from 'react';
import './ClickCounter.css';

function ClickCounter(props) {
    const [count, setCount] = useState(0);

    return (
        <div>
        <button className="vote-button" onClick={() => setCount(count + 1)}>Vote</button>
        {props.candidate}: {count} vote(s)
        </div>
    );
}

export default ClickCounter;
