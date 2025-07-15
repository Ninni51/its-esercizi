import { useState } from "react";
import Componente1, { Anagrafica, Messaggio } from "./Componente1";
import { anagrafica } from "./dati/dati";
import Stampanumeri from "./Stampanumeri";

const arr1 = [1, 2]; 

function App() {
    const initialSaluto = "Ciao";
    const [a, b] = arr1;

    const [saluta, setSaluta] = useState(initialSaluto);

    const salutami = () => { 
        setSaluta("Arrivederci");
        console.log("saluto changed to: Arrivederci");
    };

    return (
        <div>
            <p>{saluta}</p>
            <button onClick={salutami}>Saluta</button>
            <Componente1 />
            <Anagrafica data={anagrafica} />
            <Messaggio testo={saluta} />
            <Stampanumeri numeri={[a, b]} />
        </div>
    );
}

export default App;
