import React, { useState } from 'react'

const CleanUp = () => {
    const[size,setSize] = useState(window.innerWidth)
    return (
        <h1>{size}</h1>
    )
}

export default CleanUp