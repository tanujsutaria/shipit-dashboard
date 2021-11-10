import React from "react";
import { Table } from "semantic-ui-react";

export const Orders = ({orders}) => {
    return (
     <Table>
         <Table.Header>
            <Table.Row>
            <Table.HeaderCell>Order Barcode</Table.HeaderCell>
            <Table.HeaderCell>Order Status</Table.HeaderCell>
            <Table.HeaderCell>Created By</Table.HeaderCell>
            </Table.Row>
        </Table.Header>
         {orders.map(order => {
             return(
                     <Table.Body>
                         <Table.Row key = {order.ordr_pk}>
                             <Table.Cell>{order.ordr_barCode}</Table.Cell>
                             <Table.Cell>{order.stts_name}</Table.Cell>
                             <Table.Cell>{order.ordr_createdBy}</Table.Cell>
                         </Table.Row>
                     </Table.Body>
             )
         })}
     </Table>   
    )
};