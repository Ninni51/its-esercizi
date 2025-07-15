function Esercizio2() {
  const mostraDettagli = () => {
    alert(
      `ID: ${utente.id}\nNome: ${utente.nome} ${utente.cognome}\nEtà: ${utente.eta}\nProfessione: ${utente.professione}\nEmail: ${utente.email}`
    );
  };
    const utenti = [
  {
    id: 1,
    nome: "Nicholas",
    cognome: "Marsella",
    eta: 22,
    professione: "Studente",
    email: "marsella.nicholas@gmail.it",
  },
  {
    id: 2,
    nome: "Mario",
    cognome: "Rossi",
    eta: 35,
    professione: "Tuttologo",
    email: "mario.rossi@yahoo.com",
  },
  {
    id: 3,
    nome: "Il",
    cognome: "Gabibbo",
    eta: 400,
    professione: "demone",
    email: "lorem.ipsum@hell.com",
  },
];
return (
    <div className="card h-100">
    <div className="card-header text-center">Esercizio2</div>
    <div className="card-body text-center">{utente.nome} {utente.cognome} {utente.età}{utente.professione}{utente.email}</div>
    <div className="card-footer text-center"><button className="btn btn-sm btn-outline-info" onClick={mostraDettagli}>Mostra Dettagli</button></div>
    </div>
)
}