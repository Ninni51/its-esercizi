const Stampanumeri = () => {
  const num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  return (
    <div>
      {num.map((el) => (
        <div key={el}>{el}</div>
      ))}
    </div>
  );
};

