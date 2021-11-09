import React from "react";
import { Table } from "semantic-ui-react";

export const Orders = ({orders}) => {
    return (
     <Table>
         <Table.Header>
            <Table.Row>
            <Table.HeaderCell>Order Number</Table.HeaderCell>
            <Table.HeaderCell>Order Status</Table.HeaderCell>
            <Table.HeaderCell>Created On</Table.HeaderCell>
            </Table.Row>
        </Table.Header>
         {orders.map(order => {
             return(
                     <Table.Body>
                         <Table.Row>
                             <Table.Cell>{order.order_number}</Table.Cell>
                             <Table.Cell>{order.order_status}</Table.Cell>
                             <Table.Cell>{order.order_created_date}</Table.Cell>
                         </Table.Row>
                     </Table.Body>
             )
         })}
     </Table>   
    )
};