
import logo from './logo.svg';
import './App.css';
import Clock from './Clock';
import Componente1, {Anagrafica, Messaggio} from './Componente1';

/*function getDate(date) {
return date.toLocaleDateString()+" "+date.toLocaleTimeString(); }*/

function App() {
  const persone = [{
      id: "1",  
      nome: "Roberto",
      cognome: "Del",
    },{
      id: "2",
      nome: "Nicholas",
      cognome: "Marsella",
    },];
  return (
    <div className="App">
      <h1>Prima App React {nome}</h1>
      <button onClick={()=>salutami("Rob", "Del")} className="btn btn-primary">Salutami</button>
      <Componente1>pippo</Componente1>
      <Componente1>{persona1}</Componente1>
      <Componente1>{persona2}</Componente1>
      {persone.map((persona) => (
        <Componente1 key={persona.id} {...persona} />
      ))}
      <h2>
      {
        new Date().toLocaleDateString() + new Date().toLocaleTimeString()
      }
      </h2>
      <Clock timezone="1" country="ITALY"></Clock>
      <Clock timezone="4" country="USA"></Clock>
      <Clock timezone="8" country="JAPAN"></Clock>

      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

