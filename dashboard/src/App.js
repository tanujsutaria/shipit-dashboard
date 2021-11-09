import './App.css';
import React, {useEffect} from 'react';

function App() {
  useEffect(() => {
    fetch("/orders")
  })
  return (
    <div className="App">
    </div>
  );
}

export default App;
