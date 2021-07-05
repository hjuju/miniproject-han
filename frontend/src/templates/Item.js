import React from 'react'
import { ItemMenu as Menu } from '../common';
import './styles/TableStyle.css'


const Item  = ({children}) => (<>
   <h1>Item</h1>
   <Menu/>
   {children}
</>)

export default Item