import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, { useState, useEffect } from 'react';

function App() {
  const url = 'http://127.0.0.1:8000/'
  const [title, setTitle] = useState('')


  useEffect(() =>  {
    axios.get(url).then((response) => {setTitle(response.data)})
  })
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {title}
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
  );
}

export default App;
