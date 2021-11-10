import './App.css';
import React, {useEffect, useState} from 'react';
import { Orders } from './components/Orders';
import { Container } from 'semantic-ui-react';

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
    <Container style={{ marginTop: 40}}>
      <Orders orders = {orders}></Orders>
     </Container>
    </div>
  );
}

export default App;
