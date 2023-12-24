import React from "react";
import "./Checkbox.css";

const Checkbox = ({ id, value, setTodoCompleted }) => {
  const handleOnChange = (event) => {
    setTodoCompleted(Number(event.target.id));
  };

  return (
    <>
      <input
        className="checkbox"
        type="checkbox"
        id={id}
        name={value}
        onChange={handleOnChange}
      />
      <label htmlFor={id}>{value}</label>
      <br />
    </>
  );
};

export default Checkbox;
