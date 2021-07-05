import React from 'react'
import { StockMenu as Menu } from '../common';
import './styles/TableStyle.css'


const Stock  = ({children}) => (<>
   <h1>Stock</h1>
   <Menu/>
   {children}
</>)

export default Stock