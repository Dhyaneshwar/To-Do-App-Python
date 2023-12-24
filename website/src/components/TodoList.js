import React, { useState } from "react";
import Checkbox from "./Checkbox";
import { AddTodo } from "./AddTodo";

export const TodoList = () => {
  const [todos, setTodos] = useState([]);
  return (
    <>
      <div>TodoList</div>
      {todos.map((todo, index) => (
        <Checkbox id={index} value={todo} />
      ))}
      <AddTodo setTodos={setTodos} />
    </>
  );
};
