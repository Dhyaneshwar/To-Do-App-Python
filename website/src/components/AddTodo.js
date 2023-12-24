import React, { useState } from "react";

export const AddTodo = (props) => {
  const [newTodo, setNewTodo] = useState("");

  const handleInputChange = (event) => {
    setNewTodo(event.target.value);
  };

  const handleAddTodo = () => {
    const { setTodos } = props;
    setTodos((todoList) => [...todoList, newTodo]);
    setNewTodo("");
  };

  return (
    <>
      <input type="text" value={newTodo} onChange={handleInputChange} />
      <button onClick={handleAddTodo}>Add</button>
    </>
  );
};
