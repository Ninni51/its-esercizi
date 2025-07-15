const Tabellina = () => {
  const tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const multiplier = 5;

  return (
    <div>
      {tab.map((el) => (
        <div key={el}>
          {el} x {multiplier} = {el * multiplier}
        </div>
      ))}
    </div>
  );
};