import ProfiloUtente from "./Esercizio2";
import { utenti } from "./utenti";

function App() {
  const gruppi = [];
  for (let i = 0; i < utenti.length; i += 3) {
    gruppi.push(utenti.slice(i, i + 3));
  }

  return (
    <div className="container">
      {gruppi.map((gruppo, idx) => (
        <div className="row mb-4" key={idx}>
          {gruppo.map((utente) => (
            <div className="col-md-4" key={utente.id}>
              <ProfiloUtente utente={utente} />
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default App;
