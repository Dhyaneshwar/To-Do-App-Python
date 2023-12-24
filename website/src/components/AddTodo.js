import React, { useState } from "react";
import "./AddTodo.css";

export const AddTodo = ({ setTodos }) => {
  const [newTodo, setNewTodo] = useState("");

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      handleAddTodo();
    }
  };

  const handleInputChange = (event) => {
    setNewTodo(event.target.value);
  };

  const handleAddTodo = () => {
    setTodos((todoList) => [...todoList, newTodo]);
    setNewTodo("");
  };

  return (
    <input
      type="text"
      className="AddTodoInput"
      value={newTodo}
      onChange={handleInputChange}
      onKeyDown={handleKeyDown}
      placeholder="Add new todo"
    />
  );
};
