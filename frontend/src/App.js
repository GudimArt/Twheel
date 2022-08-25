import './styles/App.css';
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

      </header>
    </div>
  );
}

export default App;
