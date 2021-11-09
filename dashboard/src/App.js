import './App.css';
import React, {useEffect} from 'react';

function App() {
  useEffect(() => {
    fetch("/orders").then(response =>
      response.json().then(data => {
        console.log(data)
      }));
  },[]);
  return (
    <div className="App">
    </div>
  );
}

export default App;
