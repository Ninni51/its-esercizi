import { useState } from "react";

const CambiaNome = () => {
    const [nome, setNome] = useState("Roberto"); 
    const cambia=()=>{
/*        if(nome=="Roberto"){ 
           setNome("Mario")
    } else{
        setNome("Roberto")
    }*/
    setNome(current=>{
        if(current=="Roberto")
            return "Mario"
        return "Roberto"
    })
}
    return (
        <div>
            {nome} <div>
                <button class="btn btn-dark">Cambia</button>
            </div>
        </div>
    )
};
export default CambiaNome;