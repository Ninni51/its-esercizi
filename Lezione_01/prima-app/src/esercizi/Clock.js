import React, { useState } from 'react'

const Clock = (props) => {
    const t=Date.now()+3600*props.timezone*1000;
    const dateInit=new Date(t);
    const [date,setDate]=useState(dateInit);

    

    setTimeout(()=> {
        const t=date.getTime()*3600+1000;
        setDate(new Date(t))
    }, 1000)
    return (
        <h3>In </h3>
    )
}