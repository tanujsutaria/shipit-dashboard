import './App.css';
import React, {useEffect, useState} from 'react';
import { Orders } from './components/Orders';


function App() {
  const [orders, setOrders] = useState([]);
  useEffect(() => {
    fetch("/orders").then(response =>
      response.json().then(data => {
        setOrders(data.Orders);
      }));
  },[]);
  return (
    <div className="App">
      <Orders orders = {orders}/>
    </div>
  );
}

export default App;
