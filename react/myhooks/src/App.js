import React from 'react';
import logo from './logo.svg';
import './App.css';

// import VoteCounter from './VoteCounter';
// import useTotalVotes from './useTotalVotes';
import BallotBox from './BallotBox';
import BlackBox from './BlackBox';

function App() {
  // const BlackBox = <BlackBox boxName="My black box" />;
        
  return (
    <div className="ballot-box">
      <BallotBox />
    </div>
  );
}

export default App;

/*
  <div className="App">
  <header className="App-header">
  <img src={logo} className="App-logo" alt="logo" />
  <p>
  Edit <code>src/App.js</code> and save to reload.
  </p>
  <a
  className="App-link"
  href="https://reactjs.org"
  target="_blank"
  rel="noopener noreferrer"
  >
  Learn React
  </a>
  </header>
  </div>
*/
